"""Shared primitives: Arabic handling, stems, page maps, URLs, markdown, hashing.

The Arabic section is the important one.  A PDF may store its text layer either
as standard Arabic (U+0600-06FF) or as *presentation forms* (U+FB50-FDFF,
U+FE70-FEFF) - rendered glyph shapes, usually in visual rather than reading
order.  A character class covering only the first range scores a
presentation-form document as containing no Arabic at all, which is exactly the
document most in need of repair.

Everything Arabic-related therefore lives here, once, and covers both ranges.  No
other module may define its own.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import unicodedata
import urllib.parse
from pathlib import Path
from typing import Iterable, Iterator, List, Optional, Sequence, Tuple

from . import config

# --------------------------------------------------------------------------- #
# Arabic
# --------------------------------------------------------------------------- #

AR_STD = r"؀-ۿ"                          # standard Arabic block
AR_PF = r"ﭐ-﷿ﹰ-﻿"              # presentation forms A + B

ARABIC_STD_RE = re.compile(f"[{AR_STD}]")
ARABIC_PF_RE = re.compile(f"[{AR_PF}]")
ARABIC_ANY_RE = re.compile(f"[{AR_STD}{AR_PF}]")

_MIRROR = str.maketrans("()[]{}<>", ")(][}{><")
# Latin/digit runs keep their own left-to-right order inside an RTL line, so
# they have to be flipped back after the line is reversed.
_LTR_RUN_RE = re.compile(r"[0-9A-Za-z][0-9A-Za-z.,:/_\-]*")


def is_presentation_form(ch: str) -> bool:
    o = ord(ch)
    return 0xFB50 <= o <= 0xFDFF or 0xFE70 <= o <= 0xFEFF


def _non_space(text: str) -> List[str]:
    return [c for c in text if not c.isspace()]


def pf_share(text: str) -> float:
    """Share of non-space characters that are Arabic presentation forms.

    Anything above a couple of percent means the text layer is visually-ordered
    glyph soup rather than readable text.
    """
    ns = _non_space(text)
    if not ns:
        return 0.0
    return sum(1 for c in ns if is_presentation_form(c)) / len(ns)


def arabic_share(text: str) -> float:
    ns = _non_space(text)
    if not ns:
        return 0.0
    return sum(1 for c in ns if ARABIC_ANY_RE.match(c)) / len(ns)


def isolated_arabic_rate(text: str) -> float:
    """Rate of 1-2 letter Arabic fragments among Arabic tokens.

    Counts both character ranges, so a presentation-form document cannot score a
    misleading 0.0.
    """
    tokens = re.findall(r"\S+", text)
    ar = [t for t in tokens if ARABIC_ANY_RE.search(t)]
    if not ar:
        return 0.0
    short = sum(1 for t in ar if len(ARABIC_ANY_RE.findall(t)) <= 2 and len(t) <= 3)
    return short / len(ar)


def repair_arabic(text: str) -> str:
    """Convert visually-ordered presentation-form Arabic back to logical order.

    NFKC maps each presentation glyph to its base letter; reversing the line
    restores reading order.  Latin/digit runs are flipped back afterwards
    because they are stored left-to-right even inside an RTL line.

    This is a *fallback*.  Documents that need it are also routed to OCR, which
    produces better text; the repair is what keeps them readable when OCR is
    unavailable or fails.  Text with no presentation forms is returned untouched:
    a corpus is searched, not rendered, so logical order is always what we want
    on disk.
    """
    if not text or not ARABIC_PF_RE.search(text):
        return text
    out: List[str] = []
    for line in text.split("\n"):
        if not ARABIC_PF_RE.search(line):
            out.append(line)
            continue
        norm = unicodedata.normalize("NFKC", line)
        flipped = norm[::-1].translate(_MIRROR)
        flipped = _LTR_RUN_RE.sub(lambda m: m.group(0)[::-1], flipped)
        out.append(flipped.strip())
    return "\n".join(out)


def strip_presentation_forms(text: str) -> str:
    """Drop stray presentation-form glyphs and tidy the debris they leave."""
    if not text or not ARABIC_PF_RE.search(text):
        return text
    t = "".join(c for c in text if not is_presentation_form(c))
    t = re.sub(r"\(\s*/\s*", "(", t)
    t = re.sub(r"\s*/\s*\)", ")", t)
    t = re.sub(r"\(\s*\)", "", t)
    t = re.sub(r"\s+([,.;:])", r"\1", t)
    return re.sub(r"\s{2,}", " ", t).strip()


def sanitize_text(text: str) -> str:
    """Drop nulls and lone surrogates so a UTF-8 write can never crash."""
    if not text:
        return ""
    return "".join(
        "�" if 0xD800 <= ord(ch) <= 0xDFFF else ch
        for ch in text.replace("\x00", "")
    )


# --------------------------------------------------------------------------- #
# Stems
# --------------------------------------------------------------------------- #

STEM_RE = re.compile(r"(SAMA_(?:EN|AR)_(\d+)_VER(\d+)(?:_(\d+))?)", re.I)


def parse_stem(name: str) -> Optional[dict]:
    m = STEM_RE.search(name)
    if not m:
        return None
    return {
        "stem": m.group(1).upper(),
        "doc_id": m.group(2),
        "ver": int(m.group(3)),
        "suffix": int(m.group(4)) if m.group(4) else 0,
    }


def stem_for(name: str) -> str:
    """Canonical stem for a filename, falling back to the bare name.

    Arabic-titled documents carry no SAMA_* stem, so they keep their filename.
    """
    m = STEM_RE.search(name)
    return m.group(1).upper() if m else Path(name).stem


def stem_of_source(source_file: Optional[str]) -> str:
    return Path(source_file).stem if source_file else ""


# --------------------------------------------------------------------------- #
# Markdown page maps
# --------------------------------------------------------------------------- #

PAGE_HDR_RE = re.compile(r"^## Page (\d+)\s*$", re.MULTILINE)


class Page(tuple):
    """(number, body, start_offset, end_offset) with named access."""

    __slots__ = ()

    def __new__(cls, number: int, body: str, start: int, end: int):
        return super().__new__(cls, (number, body, start, end))

    number = property(lambda self: self[0])
    body = property(lambda self: self[1])
    start = property(lambda self: self[2])
    end = property(lambda self: self[3])


def parse_md_pages(text: str) -> List[Page]:
    """Split a corpus .md into pages, keeping absolute offsets.

    Offsets are what make deterministic grounding possible: once an excerpt is
    sliced out of the source we already know which page it came from, so the
    locator is exact rather than inferred.
    """
    matches = list(PAGE_HDR_RE.finditer(text))
    if not matches:
        body = re.sub(r"^# .*\n+", "", text, count=1)
        return [Page(1, body.strip(), 0, len(text))] if body.strip() else []
    pages: List[Page] = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        pages.append(Page(int(m.group(1)), text[start:end].strip(), start, end))
    return pages


def page_for_offset(pages: Sequence[Page], offset: int) -> Optional[int]:
    for p in pages:
        if p.start <= offset < p.end:
            return p.number
    return None


def pages_to_md(title: str, bodies: Sequence[str]) -> str:
    parts = [f"# {title}", ""]
    for i, body in enumerate(bodies, 1):
        parts += [f"## Page {i}", "", sanitize_text(body or ""), ""]
    return "\n".join(parts).rstrip() + "\n"


_SENTENCE_SPLIT = re.compile(r"(?<=[.!?؟۔])\s+|\n{2,}")


def sentences(text: str, offset: int = 0) -> Iterator[Tuple[str, int]]:
    """Yield (sentence, absolute_offset) pairs."""
    pos = 0
    for chunk in _SENTENCE_SPLIT.split(text):
        if not chunk:
            continue
        idx = text.find(chunk, pos)
        if idx < 0:
            idx = pos
        pos = idx + len(chunk)
        s = chunk.strip()
        if s:
            yield s, offset + idx + (len(chunk) - len(chunk.lstrip()))


_STOPWORDS = {
    "the", "and", "of", "for", "to", "a", "an", "in", "on", "law", "sama",
    "saudi", "central", "bank", "rules", "guide", "article", "provisions",
    "regulation", "regulations", "circular", "framework", "requirements",
}


def keywords(label: str, limit: int = 8) -> List[str]:
    words = re.findall(rf"[A-Za-z{AR_STD}{AR_PF}0-9]{{3,}}", (label or "").lower())
    return [w for w in words if w not in _STOPWORDS][:limit]


# --------------------------------------------------------------------------- #
# Sources
# --------------------------------------------------------------------------- #

def resolve_source(source_file: Optional[str]) -> Optional[Path]:
    """Map a graph node's source_file to a corpus path (graphify paths are
    relative to the extract root)."""
    if not source_file:
        return None
    for cand in (
        config.CORPUS_DIR / source_file,
        config.ROOT / source_file,
        config.CORPUS_MD / Path(source_file).name,
    ):
        if cand.exists():
            return cand
    return None


# --------------------------------------------------------------------------- #
# URLs / hashing
# --------------------------------------------------------------------------- #

def abs_url(href: str) -> str:
    if href.startswith("http"):
        return href
    if href.startswith("/"):
        return config.BASE_URL + href
    return config.BASE_URL + "/" + href.lstrip("/")


def norm_slug(href: str) -> str:
    return href.split("?")[0].rstrip("/")


def safe_url(url: str) -> str:
    """Percent-encode spaces and stray characters in the path component."""
    parts = urllib.parse.urlsplit(url)
    path = urllib.parse.quote(parts.path, safe="/%:@")
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def is_in_force(status: Optional[str]) -> bool:
    if not status:
        return False
    norm = status.strip().lower().split("\t")[0].split("  ")[0].strip()
    return norm in config.IN_FORCE_STATUSES


# --------------------------------------------------------------------------- #
# Obsidian wikilinks
# --------------------------------------------------------------------------- #

WIKILINK_FORBIDDEN = set('<>:"/\\|?*')


def strip_forbidden(name: str) -> str:
    """The export's filename rule: delete forbidden characters, no replacement."""
    return "".join(c for c in name if c not in WIKILINK_FORBIDDEN)


def wikilink(label: str) -> str:
    """A link that resolves to the exported filename while displaying the real
    label.  ``[[AML/CTF Guide]]`` would both fail to resolve and spawn a phantom
    node, so it becomes ``[[AMLCTF Guide|AML/CTF Guide]]``."""
    if any(c in WIKILINK_FORBIDDEN for c in label):
        return f"[[{strip_forbidden(label)}|{label}]]"
    return f"[[{label}]]"


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #

def md_table(headers: Sequence[str], rows: Iterable[Sequence]) -> str:
    out = ["| " + " | ".join(str(h) for h in headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        cells = ["" if c is None else str(c).replace("|", "/") for c in r]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def read_json(path: Path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def utf8_console() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass
