"""Stage 2 - PDF to markdown, with quality assessment in the same pass.

Conversion and grading share one PDF open and one definition of "is this Arabic
broken", so a document cannot be converted by one set of thresholds and judged by
another.

Routing:
  1. extract the text layer per page
  2. route to OCR when the text layer is thin, when isolated-Arabic is high, OR
     when the page carries Arabic presentation-form glyphs.  The third condition
     catches PDFs that stored rendered glyph shapes in visual order: they look
     healthy on every conventional metric - normal page count, high character
     density, no replacement characters - and are entirely unsearchable.
  3. repair any residual presentation forms to logical order
  4. grade the result; grade F is quarantined instead of entering the graph

Outputs (reports/conversion/):
  conversion_quality.json, CONVERSION_QUALITY_REPORT.md
"""

from __future__ import annotations

import re
import shutil
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING, Dict, List, Optional, Sequence, Tuple

from . import config

if TYPE_CHECKING:  # pragma: no cover
    import fitz
from .common import (
    AR_PF, AR_STD, arabic_share, isolated_arabic_rate, md_table, pages_to_md,
    parse_md_pages, pf_share, repair_arabic, sanitize_text, stem_for, write_json,
)

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
CIRCULAR_RE = re.compile(
    r"(?:\(?\d{3,}(?:[./]\d+)*\)?|Art(?:icle)?\.?\s*\d+|\u0627\u0644\u0645\u0627\u062f\u0629\s*\d+)",
    re.I,
)
CODE_RE = re.compile(r"\b[A-Z]{2,}(?:[-_/][A-Z0-9]+){1,}\b")
# Replacement char and stray control codes: a direct signal of a lossy decode.
GARBAGE_RE = re.compile("[\ufffd\u0000-\u0008\u000b\u000c\u000e-\u001f]")
# Anything outside word chars, Arabic (both blocks) and ordinary punctuation.
WEIRD_RE = re.compile(f"[^\\w{AR_STD}{AR_PF}.,;:!?()\\[\\]{{}}\"'%/\\\\@#$&*+=<>|~`^-]")


@dataclass
class DocReport:
    stem: str
    pdf_path: str
    route: str = "text"                 # text | ocr | failed
    artifact_path: str = ""
    pdf_pages: int = 0
    artifact_pages: int = 0
    page_count_match: bool = False
    pdf_text_chars: int = 0
    artifact_chars: int = 0
    coverage: Optional[float] = None
    chars_per_page: float = 0.0
    empty_pages: int = 0
    thin: bool = False
    arabic_share: float = 0.0
    isolated_arabic_rate: float = 0.0
    pf_share_before: float = 0.0        # presentation forms in the raw text layer
    pf_share_after: float = 0.0         # ... and in what we actually wrote
    arabic_risk: str = "n/a"            # low | medium | high | n/a
    token_retention: Optional[float] = None
    tokens_pdf: int = 0
    tokens_kept: int = 0
    garbage_ratio: float = 0.0
    ocr_reason: str = ""
    quarantined: bool = False
    flags: List[str] = field(default_factory=list)
    grade: str = "N/A"
    score: float = 0.0
    error: Optional[str] = None


# --------------------------------------------------------------------------- #
# Extraction
# --------------------------------------------------------------------------- #

def extract_page_text(page: "fitz.Page") -> str:
    """Read a page's text layer in reading order.

    Blocks are sorted top-to-bottom then left-to-right.  No reshaping or bidi
    display transform is applied: those produce *presentation* forms for
    rendering, and writing them to disk is what makes a corpus unsearchable.
    Storage stays logical-order.
    """
    blocks = page.get_text("blocks") or []
    text_blocks = [b for b in blocks if len(b) >= 5 and (b[4] or "").strip()]
    text_blocks.sort(key=lambda b: (round(b[1], 1), round(b[0], 1)))
    return "\n".join((b[4] or "").replace("\x00", "").strip()
                     for b in text_blocks if (b[4] or "").strip()).strip()


def ocr_page(page: "fitz.Page", tmp_png: Path, tess_cmd: str) -> str:
    import pytesseract
    from PIL import Image

    pytesseract.pytesseract.tesseract_cmd = tess_cmd
    tmp_png.parent.mkdir(parents=True, exist_ok=True)
    page.get_pixmap(dpi=config.DPI).save(str(tmp_png))
    try:
        with Image.open(tmp_png) as im:
            if im.mode not in ("RGB", "L"):
                im = im.convert("RGB")
            return (pytesseract.image_to_string(im, lang=config.OCR_LANG) or "").strip()
    finally:
        tmp_png.unlink(missing_ok=True)   # renders are intermediates, not artifacts


def route_for(text: str, page_count: int) -> Tuple[bool, str]:
    """Decide whether a document needs OCR, and say why."""
    cpp = len(text) / max(page_count, 1)
    pf = pf_share(text)
    iso = isolated_arabic_rate(text)
    reasons = []
    if cpp < config.THIN_CPP:
        reasons.append(f"thin_text:{cpp:.0f}cpp")
    if pf >= config.PF_SHARE_OCR:
        reasons.append(f"presentation_forms:{pf:.0%}")
    if iso >= config.ISOLATED_AR_OCR:
        reasons.append(f"isolated_arabic:{iso:.2f}")
    return bool(reasons), ",".join(reasons)


# --------------------------------------------------------------------------- #
# Assessment
# --------------------------------------------------------------------------- #

def _tokens(text: str) -> set:
    out = {m.group(0).lower() for m in EMAIL_RE.finditer(text)}
    for m in CIRCULAR_RE.finditer(text):
        t = re.sub(r"\s+", " ", m.group(0)).strip().lower()
        if len(t) >= 3:
            out.add(t)
    out |= {m.group(0).lower() for m in CODE_RE.finditer(text)}
    return out


def _garbage_ratio(text: str) -> float:
    nons = re.sub(r"\s+", "", text)
    if not nons:
        return 0.0
    bad = len(GARBAGE_RE.findall(text))
    weird = len(WEIRD_RE.findall(nons))
    return min(1.0, (bad + weird * 0.25) / len(nons))


def _grade(score: float) -> str:
    for cut, g in ((0.85, "A"), (0.70, "B"), (0.55, "C"), (0.40, "D")):
        if score >= cut:
            return g
    return "F"


def assess(rep: DocReport, md_text: str, pdf_full: str) -> DocReport:
    pages = parse_md_pages(md_text)
    rep.artifact_pages = len(pages)
    rep.page_count_match = rep.artifact_pages == rep.pdf_pages
    if not rep.page_count_match:
        rep.flags.append(f"page_count_mismatch:pdf={rep.pdf_pages},md={rep.artifact_pages}")

    bodies = [p.body for p in pages]
    rep.artifact_chars = sum(len(b.strip()) for b in bodies)
    rep.empty_pages = sum(1 for b in bodies if len(b.strip()) <= config.EMPTY_PAGE_CHARS)
    rep.chars_per_page = rep.artifact_chars / max(rep.artifact_pages, 1)
    rep.thin = rep.chars_per_page < config.THIN_CPP

    ocr_enriched = rep.route == "ocr"
    if rep.pdf_text_chars > 0 and not ocr_enriched:
        rep.coverage = min(1.5, rep.artifact_chars / rep.pdf_text_chars)
        if rep.coverage < config.COVERAGE_FAIL:
            rep.flags.append(f"coverage_fail:{rep.coverage:.2f}")
        elif rep.coverage < config.COVERAGE_WARN:
            rep.flags.append(f"coverage_warn:{rep.coverage:.2f}")
    elif ocr_enriched:
        rep.flags.append("ocr_route_coverage_not_comparable")
    else:
        rep.flags.append("pdf_has_no_text_layer")

    rep.arabic_share = round(arabic_share(md_text), 3)
    rep.isolated_arabic_rate = round(isolated_arabic_rate(md_text), 3)
    rep.pf_share_after = round(pf_share(md_text), 4)

    # Presentation forms surviving into the artifact mean the repair did not
    # take, so they are graded explicitly.
    if rep.pf_share_after >= config.PF_SHARE_OCR:
        rep.arabic_risk = "high"
        rep.flags.append(f"presentation_forms_remain:{rep.pf_share_after:.0%}")
    elif rep.arabic_share >= config.ARABIC_SHARE_WARN:
        if rep.isolated_arabic_rate >= 0.20:
            rep.arabic_risk = "high"
            rep.flags.append(f"arabic_isolated_high:{rep.isolated_arabic_rate:.2f}")
        elif rep.isolated_arabic_rate >= config.ISOLATED_AR_WARN:
            rep.arabic_risk = "medium"
            rep.flags.append(f"arabic_isolated_medium:{rep.isolated_arabic_rate:.2f}")
        else:
            rep.arabic_risk = "low"

    if not ocr_enriched:
        pdf_tokens = _tokens(pdf_full)
        rep.tokens_pdf = len(pdf_tokens)
        if pdf_tokens:
            kept = pdf_tokens & _tokens(md_text)
            rep.tokens_kept = len(kept)
            rep.token_retention = len(kept) / len(pdf_tokens)
            if rep.token_retention < 0.7:
                rep.flags.append(f"token_retention_low:{rep.token_retention:.2f}")

    rep.garbage_ratio = round(_garbage_ratio(md_text), 4)
    if rep.garbage_ratio > config.GARBAGE_WARN:
        rep.flags.append(f"garbage_ratio:{rep.garbage_ratio:.3f}")
    if rep.empty_pages:
        rep.flags.append(f"empty_pages:{rep.empty_pages}")

    score = 1.0
    if not rep.page_count_match:
        score -= 0.25
    if rep.coverage is not None:
        if rep.coverage < config.COVERAGE_FAIL:
            score -= 0.30
        elif rep.coverage < config.COVERAGE_WARN:
            score -= 0.12
        if rep.coverage > 1.15:
            score -= 0.05
    if rep.thin:
        score -= 0.20
    if rep.arabic_risk == "high":
        score -= 0.30
    elif rep.arabic_risk == "medium":
        score -= 0.12
    if rep.token_retention is not None and rep.token_retention < 0.7:
        score -= 0.10
    if rep.empty_pages:
        score -= min(0.15, 0.02 * rep.empty_pages)
    if rep.garbage_ratio > config.GARBAGE_WARN:
        score -= 0.08
    if rep.artifact_chars < 200:
        score = min(score, 0.2)
    rep.score = max(0.0, round(score, 3))
    rep.grade = _grade(rep.score)
    return rep


# --------------------------------------------------------------------------- #
# Per-document conversion
# --------------------------------------------------------------------------- #

def convert_pdf(pdf: Path, tess_cmd: Optional[str], force_ocr: bool = False) -> DocReport:
    # Imported here so the pure routing/assessment helpers stay importable (and
    # testable) without PyMuPDF present.
    import fitz

    stem = stem_for(pdf.name)
    rep = DocReport(stem=stem, pdf_path=str(pdf.relative_to(config.ROOT)))
    try:
        doc = fitz.open(pdf)
    except Exception as exc:
        rep.route, rep.grade, rep.error = "failed", "F", f"open_failed: {exc}"[:200]
        rep.flags.append("pdf_open_failed")
        return rep

    try:
        rep.pdf_pages = doc.page_count
        raw_pages = [extract_page_text(p) for p in doc]
        raw_joined = "\n".join(raw_pages)
        rep.pdf_text_chars = len(raw_joined)
        rep.pf_share_before = round(pf_share(raw_joined), 4)

        need_ocr, reason = route_for(raw_joined, doc.page_count)
        if force_ocr:
            need_ocr, reason = True, "forced"

        if need_ocr and not tess_cmd:
            rep.flags.append("ocr_needed_but_tesseract_missing")
            need_ocr = False

        if need_ocr:
            rep.route, rep.ocr_reason = "ocr", reason
            print(f"[{stem}] OCR ({reason}) pages={doc.page_count}", flush=True)
            bodies = []
            for i, page in enumerate(doc, 1):
                if i % 10 == 0 or i == 1:
                    print(f"    OCR {i}/{doc.page_count}", flush=True)
                bodies.append(ocr_page(page, config.OCR_TMP / f"{stem}_{i}.png", tess_cmd))
        else:
            rep.route = "text"
            print(f"[{stem}] text (pages={doc.page_count}, pf={rep.pf_share_before:.0%})", flush=True)
            bodies = raw_pages

        # Repair any presentation forms that survived either route.
        bodies = [repair_arabic(sanitize_text(b)) for b in bodies]

        config.CORPUS_MD.mkdir(parents=True, exist_ok=True)
        out = config.CORPUS_MD / f"{stem}.md"
        md_text = pages_to_md(pdf.name, bodies)
        out.write_text(md_text, encoding="utf-8")
        rep.artifact_path = str(out.relative_to(config.ROOT))

        assess(rep, md_text, raw_joined)

        if rep.grade == config.QUARANTINE_GRADE:
            config.QUARANTINE.mkdir(parents=True, exist_ok=True)
            shutil.move(str(out), str(config.QUARANTINE / out.name))
            rep.quarantined = True
            rep.artifact_path = str((config.QUARANTINE / out.name).relative_to(config.ROOT))
            rep.flags.append("quarantined_grade_F")
            print(f"    -> quarantined (grade F, score {rep.score})", flush=True)
        return rep
    except Exception as exc:
        rep.route, rep.grade, rep.error = "failed", "F", str(exc)[:200]
        return rep
    finally:
        doc.close()


# --------------------------------------------------------------------------- #
# Near-duplicates
# --------------------------------------------------------------------------- #

def _shingles(text: str, k: int = 12, cap: int = 4000) -> set:
    s = re.sub(r"\s+", " ", text).lower()
    if len(s) < k:
        return {s} if s else set()
    step = max(1, (len(s) - k) // cap)
    return {s[i:i + k] for i in range(0, len(s) - k + 1, step)}


def near_duplicates(md_files: Sequence[Path]) -> List[dict]:
    """Length-bucketed Jaccard.

    Documents whose lengths differ by more than the similarity threshold cannot
    be near-duplicates, so bucketing by length keeps this from degenerating into
    an all-pairs comparison over unbounded shingle sets.
    """
    docs = []
    for p in md_files:
        t = p.read_text(encoding="utf-8", errors="replace")
        docs.append((p, len(t), _shingles(t)))
    docs.sort(key=lambda d: d[1])

    pairs: List[dict] = []
    for i, (pa, la, sa) in enumerate(docs):
        if not sa:
            continue
        for pb, lb, sb in docs[i + 1:]:
            if lb > la * (1 + config.NEAR_DUP_LENGTH_BAND):
                break
            if not sb:
                continue
            sim = len(sa & sb) / len(sa | sb)
            if sim >= config.NEAR_DUP_THRESHOLD:
                pairs.append({"a": pa.name, "b": pb.name, "similarity": round(sim, 3),
                              "identical": sim >= 0.999})
    return pairs


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #

def write_report(reports: List[DocReport], dupes: List[dict], elapsed: float) -> Path:
    config.CONV_REPORTS.mkdir(parents=True, exist_ok=True)
    by_grade: Dict[str, int] = {}
    for r in reports:
        by_grade[r.grade] = by_grade.get(r.grade, 0) + 1
    mean = sum(r.score for r in reports) / max(len(reports), 1)
    quarantined = [r for r in reports if r.quarantined]
    ocr = [r for r in reports if r.route == "ocr"]
    pf_rescued = [r for r in reports
                  if r.pf_share_before >= config.PF_SHARE_OCR and r.pf_share_after < config.PF_SHARE_OCR]

    lines = [
        "# Conversion Quality Report", "",
        f"> Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"> Elapsed: {elapsed:.1f}s", "",
        "## Summary", "",
        md_table(["Metric", "Value"], [
            ["PDFs processed", len(reports)],
            ["Routed to OCR", len(ocr)],
            ["Mean score", f"{mean:.3f}"],
            ["Grades", ", ".join(f"{g}:{by_grade[g]}" for g in "ABCDF" if by_grade.get(g))],
            ["Quarantined (grade F)", len(quarantined)],
            ["Presentation-form docs repaired", len(pf_rescued)],
            ["Near-duplicate pairs", len(dupes)],
        ]), "",
        "## Per-document", "",
        md_table(
            ["Stem", "Route", "Grade", "Score", "PDF pp", "MD pp", "Coverage",
             "chars/pp", "PF before", "PF after", "AR risk", "Flags"],
            [[r.stem, r.route, f"**{r.grade}**", f"{r.score:.2f}", r.pdf_pages,
              r.artifact_pages, f"{r.coverage:.2f}" if r.coverage is not None else "-",
              f"{r.chars_per_page:.0f}", f"{r.pf_share_before:.0%}", f"{r.pf_share_after:.0%}",
              r.arabic_risk, ("; ".join(r.flags) or "-")[:90]]
             for r in sorted(reports, key=lambda x: (x.grade, -x.score, x.stem))]), "",
    ]

    if quarantined:
        lines += ["## Quarantined", "",
                  "These conversions failed and were moved out of `corpus/markdown/` so they "
                  "never reach the graph. Re-source the PDF or OCR manually.", ""]
        lines += [f"- `{r.stem}` — score {r.score:.2f} — {'; '.join(r.flags)}" for r in quarantined]
        lines.append("")

    if dupes:
        lines += ["## Near-duplicate pairs", "",
                  md_table(["A", "B", "Similarity", "Identical"],
                           [[d["a"], d["b"], f"{d['similarity']:.3f}",
                             "yes" if d["identical"] else "no"] for d in dupes]), ""]

    actions = []
    for r in sorted(reports, key=lambda x: x.score):
        if r.route == "failed":
            actions.append(f"**{r.stem}**: conversion failed — {r.error}")
        elif r.arabic_risk == "high":
            actions.append(f"**{r.stem}**: Arabic still broken after OCR — re-source the PDF.")
        elif r.coverage is not None and r.coverage < config.COVERAGE_WARN:
            actions.append(f"**{r.stem}**: coverage {r.coverage:.2f} — investigate dropped text.")
        elif r.empty_pages >= 3:
            actions.append(f"**{r.stem}**: {r.empty_pages} empty pages — verify blanks vs failure.")
    lines += ["## Priority actions", ""]
    lines += [f"{i}. {a}" for i, a in enumerate(actions[:40], 1)] or ["- None."]
    lines.append("")

    out = config.CONV_REPORTS / "CONVERSION_QUALITY_REPORT.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    write_json(config.CONV_JSON, {
        "generated": datetime.now(timezone.utc).isoformat(),
        "documents": [asdict(r) for r in reports],
        "near_duplicates": dupes,
        "summary": {
            "count": len(reports), "mean_score": round(mean, 3),
            "grades": {g: by_grade.get(g, 0) for g in "ABCDF"},
            "quarantined": [r.stem for r in quarantined],
            "ocr_routed": [r.stem for r in ocr],
        },
    })
    return out


def run(pdf_dir: Optional[Path] = None, limit: int = 0, stems: Optional[Sequence[str]] = None,
        force_ocr: bool = False) -> int:
    config.ensure_dirs()
    pdf_dir = pdf_dir or config.PDF_DIR
    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if stems:
        want = {s.upper().replace(".PDF", "") for s in stems}
        pdfs = [p for p in pdfs if stem_for(p.name).upper() in want]
    if limit:
        pdfs = pdfs[:limit]
    if not pdfs:
        print(f"No PDFs in {pdf_dir} — run the crawl stage first.")
        return 1

    tess = config.tesseract_cmd()
    if tess:
        import os
        if config.TESSDATA.exists():
            os.environ["TESSDATA_PREFIX"] = str(config.TESSDATA)
    else:
        print("WARNING: tesseract not found — documents needing OCR will fall back "
              "to repaired text-layer extraction and be graded accordingly.")

    t0 = time.time()
    reports: List[DocReport] = []
    for i, pdf in enumerate(pdfs, 1):
        print(f"\n=== [{i}/{len(pdfs)}] {pdf.name} ===", flush=True)
        reports.append(convert_pdf(pdf, tess, force_ocr=force_ocr))

    if config.OCR_TMP.exists():
        shutil.rmtree(config.OCR_TMP, ignore_errors=True)

    live = [config.CORPUS_MD / f"{r.stem}.md" for r in reports if not r.quarantined]
    dupes = near_duplicates([p for p in live if p.exists()])
    report = write_report(reports, dupes, time.time() - t0)

    ok = sum(1 for r in reports if r.grade not in ("F", "N/A"))
    print(f"\nConverted {ok}/{len(reports)} usable | report: {report}")
    print(f"Corpus: {len(list(config.CORPUS_MD.glob('*.md')))} markdown files")
    return 0
