"""Page-anchored corpus reads and deterministic citation checking.  No tokens.

Two string operations that the v1 workflow paid a model to do:

  fetch  - open one page of one document instead of the whole file.  The corpus
           holds a 1.9 MB instrument; a digger handed `stem + page` should not
           pull it into context to quote two sentences.
  verify - decide whether a quote really sits at the locator the memo claims.
           A model reading page numbers is slower and less reliable at this
           than str.find, and it is the reviewer's one strict duty.

Comparison is done after normalising whitespace, case, quote glyphs and Arabic
presentation forms, because a verbatim slice of an OCR'd page can differ from
the memo by invisible characters alone - and a false MISSING is worse than no
check at all.

    python -m sama.cite fetch --stem SAMA_EN_1734_VER1 --pages 10-14
    python -m sama.cite verify --claim "SAMA_EN_1734_VER1:12:Minimum contents must include"
    python -m sama.cite verify --claims claims.json

No agent in this workflow may create a file, so `--claim` is the path they use:
an argv string needs no temp file, no write permission and no console-encoding
negotiation.  `--claims PATH` and `--claims -` remain for humans and scripts.
"""

from __future__ import annotations

import argparse
import codecs
import difflib
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence

from . import config
from .common import (
    md_table, parse_md_pages, stem_for, strip_presentation_forms, utf8_console,
)

# Typographic substitutions a memo picks up when a quote is re-typed or passed
# through a model.  None of them change the text, all of them break str.find.
_GLYPHS = str.maketrans({
    "\u2018": "'", "\u2019": "'", "\u201a": "'", "\u201b": "'",
    "\u201c": '"', "\u201d": '"', "\u201e": '"',
    "\u2013": "-", "\u2014": "-", "\u2212": "-", "\u00a0": " ",
    "\u2026": "...", "\u00ad": "",
})


def normalise(text: str) -> str:
    """Everything that must be equal for two quotes to count as the same text."""
    t = strip_presentation_forms(text or "").translate(_GLYPHS)
    return re.sub(r"\s+", " ", t).strip().casefold()


# --------------------------------------------------------------------------- #
# Documents
# --------------------------------------------------------------------------- #

def resolve_stem(stem: str) -> Optional[Path]:
    """Corpus path for a stem.

    Arabic-titled documents carry no SAMA_* stem and keep their filename, so a
    direct hit is tried first and a scan is the fallback.
    """
    direct = config.CORPUS_MD / f"{stem}.md"
    if direct.exists():
        return direct
    for path in config.CORPUS_MD.glob("*.md"):
        if path.stem == stem or stem_for(path.name) == stem.upper():
            return path
    return None


def parse_pages_arg(spec: Optional[str]) -> Optional[List[int]]:
    """`12`, `10-14`, `3,7,10-12` -> a sorted page list.  None means all."""
    if not spec:
        return None
    out: List[int] = []
    for part in spec.replace(" ", "").split(","):
        if not part:
            continue
        if "-" in part:
            lo, hi = part.split("-", 1)
            out.extend(range(int(lo), int(hi) + 1))
        else:
            out.append(int(part))
    return sorted(set(out))


def fetch(stem: str, pages: Optional[Sequence[int]],
          window: int = config.CITE_FETCH_WINDOW,
          max_pages: int = config.CITE_FETCH_MAX_PAGES) -> str:
    """Selected pages of one document, never more than max_pages of them.

    The cap is not a nicety.  This corpus holds a 902-page instrument, and an
    unbounded fetch of it destroys the caller's context window with no warning
    and no way to recover mid-run.  Truncation is announced so the caller can
    ask for the rest deliberately.
    """
    path = resolve_stem(stem)
    if not path:
        return f"NO_SUCH_STEM: {stem} (looked in corpus/markdown/)"

    all_pages = parse_md_pages(path.read_text(encoding="utf-8", errors="replace"))
    parsed = all_pages
    if pages:
        wanted = {p + d for p in pages for d in range(-window, window + 1)}
        parsed = [p for p in all_pages if p.number in wanted]
        if not parsed:
            have = ", ".join(str(p.number) for p in all_pages[:20])
            return f"NO_SUCH_PAGE in {stem}: asked {sorted(wanted)}, document has {have}…"

    rel = path.relative_to(config.ROOT).as_posix()
    out = [f"# {rel}", ""]
    dropped = parsed[max_pages:]
    for p in parsed[:max_pages]:
        out += [f"## Page {p.number}", "", p.body, ""]
    if dropped:
        out += [f"> TRUNCATED — {len(dropped)} further pages matched and were not "
                f"returned ({dropped[0].number}–{dropped[-1].number} of "
                f"{len(all_pages)} in this document). Re-run with a narrower "
                f"`--pages` range to see them; do not assume they are empty.", ""]
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Verification
# --------------------------------------------------------------------------- #

def _best_ratio(needle: str, haystack: str) -> float:
    """Best similarity of `needle` against any same-length window of `haystack`.

    A whole-page ratio would be dominated by the page, so the page is walked in
    half-quote steps and the best window wins.
    """
    if not needle or not haystack:
        return 0.0
    n = len(needle)
    if len(haystack) <= n:
        return difflib.SequenceMatcher(None, needle, haystack).ratio()
    best, step = 0.0, max(1, n // 2)
    for i in range(0, len(haystack) - n + 1, step):
        r = difflib.SequenceMatcher(None, needle, haystack[i:i + n]).ratio()
        if r > best:
            best = r
            if best >= 0.99:
                break
    return best


def verify_claim(claim: dict) -> dict:
    """One claim -> a status a script can defend.

    EXACT / FUZZY pass.  PAGE_MISMATCH means the quote is real but the locator
    is wrong, which is the failure a model reviewer misses most often.
    """
    cid = str(claim.get("id") or claim.get("claim") or "")[:60]
    stem = str(claim.get("stem") or "")
    quote = str(claim.get("quote") or "")
    page = claim.get("page")
    res = {"id": cid, "stem": stem, "page": page, "status": "MISSING",
           "ratio": 0.0, "found_page": None}

    path = resolve_stem(stem)
    if not path:
        res["status"] = "NO_SUCH_STEM"
        return res
    if len(normalise(quote)) < config.CITE_MIN_QUOTE_CHARS:
        res["status"] = "TOO_SHORT"
        return res

    needle = normalise(quote)
    pages = parse_md_pages(path.read_text(encoding="utf-8", errors="replace"))
    bodies = {p.number: normalise(p.body) for p in pages}

    if page is not None and int(page) in bodies:
        body = bodies[int(page)]
        if needle in body:
            res.update(status="EXACT", ratio=1.0, found_page=int(page))
            return res
        ratio = _best_ratio(needle, body)
        res["ratio"] = round(ratio, 3)
        if ratio >= config.CITE_FUZZY_RATIO:
            res.update(status="FUZZY", found_page=int(page))
            return res
    elif page is not None:
        res["status"] = "NO_SUCH_PAGE"

    for num, body in bodies.items():
        if needle in body:
            res.update(status="PAGE_MISMATCH", ratio=1.0, found_page=num)
            return res
    for num, body in bodies.items():
        ratio = _best_ratio(needle, body)
        if ratio >= config.CITE_FUZZY_RATIO:
            res.update(status="PAGE_MISMATCH", ratio=round(ratio, 3), found_page=num)
            return res
    return res


PASS = {"EXACT", "FUZZY"}


def verify(claims: Sequence[dict]) -> dict:
    rows = [verify_claim(c) for c in claims]
    failed = [r for r in rows if r["status"] not in PASS]
    return {"claims": len(rows), "passed": len(rows) - len(failed),
            "failed": len(failed), "results": rows}


def _render(res: dict) -> str:
    out = ["# Citation check", "",
           md_table(["Claim", "Stem", "Page", "Status", "Ratio", "Found on"],
                    [[r["id"], f"`{r['stem']}`", r["page"], r["status"],
                      r["ratio"], r["found_page"] if r["found_page"] != r["page"] else ""]
                     for r in res["results"]]), ""]
    if res["failed"]:
        out += [f"**{res['failed']} of {res['claims']} claims did not verify.** "
                "Fix these before the answer ships — PAGE_MISMATCH means the quote is "
                "real but the locator is wrong.", ""]
    else:
        out += [f"**All {res['claims']} claims verified against `corpus/markdown/`.**", ""]
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def parse_inline(spec: str) -> dict:
    """`STEM:PAGE:quote text` -> a claim.

    The channel agents use, because it needs nothing they do not have: no temp
    file, no write permission, no console encoding.
    """
    parts = spec.split(":", 2)
    if len(parts) < 3 or not parts[1].strip().isdigit():
        head, _, tail = spec.partition(":")
        return {"id": head.strip()[:40] or "claim", "stem": head.strip(),
                "page": None, "quote": tail.strip()}
    stem, page, quote = (p.strip() for p in parts)
    return {"id": f"{stem} p.{page}", "stem": stem, "page": int(page), "quote": quote}


def _decode(data: bytes) -> str:
    """Whatever the shell produced, get text back.

    PowerShell writes UTF-16LE with a BOM on `>` redirection, which a plain
    utf-8 read rejects outright - a failure that looks like a bug in the claims
    rather than in the shell.
    """
    if data.startswith(codecs.BOM_UTF16_LE) or data.startswith(codecs.BOM_UTF16_BE):
        return data.decode("utf-16")
    return data.decode("utf-8-sig", errors="replace")


def _load_claims(spec: str) -> List[dict]:
    raw = _decode(sys.stdin.buffer.read() if spec == "-" else Path(spec).read_bytes())
    data = json.loads(raw)
    claims = data.get("claims") if isinstance(data, dict) else data
    if not isinstance(claims, list):
        raise SystemExit('Expected {"claims": [...]} or a bare JSON list.')
    return claims


def main(argv: Optional[Sequence[str]] = None) -> int:
    utf8_console()
    ap = argparse.ArgumentParser(
        prog="python -m sama.cite",
        description="Page-anchored corpus reads and deterministic citation checking.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fetch", help="print selected pages of one corpus document")
    f.add_argument("--stem", required=True)
    f.add_argument("--pages", help="12 | 10-14 | 3,7,10-12 (default: whole document)")
    f.add_argument("--window", type=int, default=config.CITE_FETCH_WINDOW,
                   help="neighbouring pages to include either side")
    f.add_argument("--max-pages", type=int, default=config.CITE_FETCH_MAX_PAGES,
                   help="hard ceiling on pages returned by one call")

    v = sub.add_parser("verify", help="check quotes against their claimed locators")
    v.add_argument("--claim", action="append", default=[], metavar="STEM:PAGE:QUOTE",
                   help="one claim inline; repeat per claim. Needs no file, so agents "
                        "use this")
    v.add_argument("--claims", metavar="PATH",
                   help='path to {"claims":[{"id","stem","page","quote"}]}, or - for stdin')
    v.add_argument("--json", action="store_true")
    v.add_argument("--strict", action="store_true", help="exit 1 if any claim fails")

    args = ap.parse_args(argv)

    if args.cmd == "fetch":
        print(fetch(args.stem, parse_pages_arg(args.pages), args.window, args.max_pages))
        return 0

    claims = [parse_inline(c) for c in args.claim]
    if args.claims:
        claims += _load_claims(args.claims)
    if not claims:
        v.error("give at least one --claim, or --claims PATH")

    res = verify(claims)
    print(json.dumps(res, ensure_ascii=False, indent=2) if args.json else _render(res))
    return 1 if (args.strict and res["failed"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
