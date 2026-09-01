"""Stage 1 - crawl rulebook.sama.gov.sa and download in-force PDFs.

A single visit to each page yields structure, publication status and PDF links
together, so the site is walked once rather than once per kind of information.

Only instruments the regulator presents as In-Force are downloaded.  Filtering at
acquisition means superseded material never enters the corpus, and there is no
retirement problem to solve further down the pipeline.

Outputs (reports/crawl/):
  tree.json, manifest.json, crawl_report.md, downloaded_files.txt
"""

from __future__ import annotations

import hashlib
import re
import time
import urllib.parse
import urllib.request
from collections import deque
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from . import config
from .common import (
    abs_url, is_in_force, md_table, norm_slug, safe_url, sha256_file,
    stem_for, write_json,
)

# Extracts structure, status and PDF links in one page evaluation.
_PAGE_JS = """() => {
    const main = document.querySelector('main, .region-content, #main-content, article') || document.body;
    const text = (main.innerText || '').slice(0, 12000);
    const pdfs = [];
    document.querySelectorAll('a[href]').forEach(el => {
        const h = el.getAttribute('href') || '';
        if (h.includes('file_store') && h.includes('.pdf')) {
            pdfs.push({ href: h, text: (el.innerText || '').trim().slice(0, 120) });
        }
    });
    const links = [];
    document.querySelectorAll('a[href]').forEach(a => {
        const r = a.getBoundingClientRect();
        if (r.left > 500 || r.top < 200 || r.top > 950) return;
        const t = (a.innerText || '').trim().replace(/\\s+/g, ' ');
        const h = a.getAttribute('href') || '';
        if (!t || t.length < 2) return;
        if (h.startsWith('javascript') || h === '#') return;
        if (h.includes('sama.gov.sa/en-US')) return;
        links.push({ x: Math.round(r.left), y: Math.round(r.top), href: h, title: t });
    });
    links.sort((a, b) => a.y - b.y || a.x - b.x);
    return { text, pdfs, links };
}"""

_CIRCULAR_JS = """(indexSlug) => {
    const main = document.querySelector('main, .region-content, #main-content, article') || document.body;
    const seen = new Set(); const out = [];
    main.querySelectorAll('a[href]').forEach(a => {
        let h = a.getAttribute('href') || '';
        if (h.startsWith('en/')) h = '/' + h;
        if (!h.startsWith('/en/')) return;
        h = h.split('?')[0].replace(/\\/$/, '');
        const t = (a.innerText || '').trim().replace(/\\s+/g, ' ');
        if (!t || t.length < 3) return;
        if (h.includes('entiresection') || h.includes('file_store')) return;
        if (h.includes('/revisions/') || h === indexSlug) return;
        if (h.endsWith('-circulars')) return;
        if (!h.includes('/node/') && t.length < 10) return;
        if (seen.has(h)) return;
        seen.add(h);
        out.push({ href: h, title: t.slice(0, 200) });
    });
    return out;
}"""

DOC_NO_RE = re.compile(r"No:\s*([^\n|]+)", re.I)
STATUS_RE = re.compile(r"Status:\s*([^\n|]+)", re.I)


@dataclass
class PdfRecord:
    file_id: str
    stem: Optional[str]
    pdf_url: str
    filename: str
    link_label: str = ""
    source_slug: str = ""
    source_title: str = ""
    tree_path: str = ""
    source_kind: str = "tree"
    document_no: Optional[str] = None
    status: Optional[str] = None
    in_force: bool = False
    local_path: Optional[str] = None
    sha256: Optional[str] = None
    content_length: Optional[int] = None
    action: str = "pending"
    error: Optional[str] = None


def _reject_bytes(data: bytes, declared: Optional[int]) -> Optional[str]:
    """Why this payload is not a usable PDF, or None if it is."""
    if declared is not None and len(data) != declared:
        return f"got {len(data)} bytes, Content-Length said {declared}"
    if len(data) < config.MIN_PDF_BYTES:
        return f"only {len(data)} bytes"
    if not data.startswith(b"%PDF"):
        return "no %PDF header — error page or wrong content"
    return None


def _reject_file(path: Path) -> Optional[str]:
    """Same check against a file already on disk."""
    try:
        size = path.stat().st_size
        if size < config.MIN_PDF_BYTES:
            return f"only {size} bytes"
        with path.open("rb") as f:
            if f.read(4) != b"%PDF":
                return "no %PDF header"
    except OSError as exc:
        return f"unreadable: {exc}"
    return None


def _should_skip(href: str) -> bool:
    slug = norm_slug(href)
    if slug in config.SKIP_HREFS or not slug.startswith("/en/"):
        return True
    return "/entiresection/" in slug


def _direct_children(links: List[dict], current_slug: str) -> List[dict]:
    """Sidebar children of the active node, identified by x-indent."""
    cur = norm_slug(current_slug)
    idx = px = None
    for i, lk in enumerate(links):
        if norm_slug(lk["href"]) == cur:
            idx, px = i, lk["x"]
    if idx is None:
        return []
    desc = []
    for lk in links[idx + 1:]:
        if lk["x"] <= px:
            break
        desc.append(lk)
    if not desc:
        return []
    min_x = min(lk["x"] for lk in desc)
    return [lk for lk in desc if lk["x"] == min_x]


def _top_level(links: List[dict]) -> List[dict]:
    en = [lk for lk in links if lk["href"].startswith("/en/") and not _should_skip(lk["href"])]
    if not en:
        return []
    min_x = min(lk["x"] for lk in en)
    return [lk for lk in en if lk["x"] == min_x]


def _file_id(url: str, stem: Optional[str]) -> str:
    if stem:
        return stem
    name = urllib.parse.unquote(url.split("/")[-1].split("?")[0])
    return re.sub(r"[^\w.\-]+", "_", name)[:120] or hashlib.sha256(url.encode()).hexdigest()[:16]


def _filename(rec: PdfRecord) -> str:
    if rec.stem:
        return f"{rec.stem}.pdf"
    return rec.filename if rec.filename.lower().endswith(".pdf") else f"{rec.filename}.pdf"


def _records_from_page(data: dict, slug: str, tree_path: str, title: str, kind: str) -> List[PdfRecord]:
    text = data.get("text", "")
    m = STATUS_RE.search(text)
    status = m.group(1).strip()[:80] if m else None
    m2 = DOC_NO_RE.search(text)
    doc_no = m2.group(1).strip()[:80] if m2 else None
    in_force = is_in_force(status)

    out: List[PdfRecord] = []
    seen: Set[str] = set()
    for item in data.get("pdfs", []):
        url = abs_url(item.get("href", ""))
        if "file_store" not in url and "rulebook.sama.gov.sa" not in url:
            continue
        if url in seen:
            continue
        seen.add(url)
        stem = stem_for(url) if "SAMA_" in url.upper() else None
        if stem and not stem.startswith("SAMA_"):
            stem = None
        basename = urllib.parse.unquote(url.split("/")[-1].split("?")[0])
        out.append(PdfRecord(
            file_id=_file_id(url, stem), stem=stem, pdf_url=url, filename=basename,
            link_label=item.get("text", ""), source_slug=slug, source_title=title,
            tree_path=tree_path, source_kind=kind, document_no=doc_no,
            status=status, in_force=in_force,
        ))
    return out


def _merge(by_id: Dict[str, PdfRecord], found: List[PdfRecord]) -> None:
    for rec in found:
        cur = by_id.get(rec.file_id)
        if not cur:
            by_id[rec.file_id] = rec
        else:
            if not cur.tree_path and rec.tree_path:
                cur.tree_path = rec.tree_path
            # An instrument listed on several pages counts as in force if any
            # page presents it that way.
            cur.in_force = cur.in_force or rec.in_force


def crawl(max_pages: int = 0, headless: bool = True) -> Tuple[List[PdfRecord], dict]:
    from playwright.sync_api import sync_playwright

    tree: Dict[str, dict] = {}
    by_id: Dict[str, PdfRecord] = {}
    # A page that fails to load takes its PDFs — and, on a tree page, its whole
    # unvisited subtree — with it.  Recording the slug is what keeps that from
    # being invisible: nothing downstream can infer a document it never saw.
    failed_pages: List[dict] = []
    stats: dict = {"pages_visited": 0, "pages_with_pdf": 0, "circular_indexes": 0,
                   "circular_pages": 0, "skipped_not_in_force": 0,
                   "failed_pages": failed_pages}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page(viewport={"width": 1600, "height": 1000})
        page.set_default_timeout(30000)

        page.goto(abs_url(config.ENTRY_PAGE), wait_until="domcontentloaded")
        page.wait_for_timeout(2000)
        first = page.evaluate(_PAGE_JS)
        sectors = _top_level(first["links"])
        if not sectors:
            browser.close()
            raise RuntimeError(f"No top-level sectors on {config.ENTRY_PAGE}")

        for lk in sectors:
            slug = norm_slug(lk["href"])
            tree[slug] = {"slug": slug, "title": lk["title"], "depth": 0,
                          "parent": None, "children": []}

        queue: deque = deque(tree.keys())
        expanded: Set[str] = set()
        circular_indexes: List[str] = []

        while queue:
            slug = queue.popleft()
            if slug in expanded:
                continue
            if max_pages and len(expanded) >= max_pages:
                print(f"  [cap] stopping at --max-pages {max_pages}", flush=True)
                break
            expanded.add(slug)
            node = tree[slug]

            try:
                page.goto(abs_url(slug), wait_until="domcontentloaded")
                page.wait_for_timeout(700)
                data = page.evaluate(_PAGE_JS)
            except Exception as exc:
                print(f"  ERR {slug}: {exc}", flush=True)
                failed_pages.append({"slug": slug, "kind": "tree",
                                     "title": node["title"], "error": str(exc)[:200]})
                continue

            stats["pages_visited"] += 1
            found = _records_from_page(data, slug, node["title"], node["title"], "tree")
            if found:
                stats["pages_with_pdf"] += 1
                _merge(by_id, found)

            for lk in _direct_children(data["links"], slug):
                ch = norm_slug(lk["href"])
                if _should_skip(ch):
                    continue
                if ch not in tree:
                    tree[ch] = {"slug": ch, "title": lk["title"],
                                "depth": node["depth"] + 1, "parent": slug, "children": []}
                    node["children"].append(ch)
                    queue.append(ch)
                elif ch not in expanded:
                    queue.append(ch)

            if not node["children"] and "circular" in slug.lower():
                circular_indexes.append(slug)

            if len(expanded) % 25 == 0:
                print(f"  visited {len(expanded)} | queued {len(queue)} | pdfs {len(by_id)}", flush=True)

        stats["circular_indexes"] = len(circular_indexes)
        targets: List[Tuple[str, str]] = []
        seen_c: Set[str] = set()
        for idx_slug in circular_indexes:
            try:
                page.goto(abs_url(idx_slug), wait_until="domcontentloaded")
                page.wait_for_timeout(800)
                for row in page.evaluate(_CIRCULAR_JS, norm_slug(idx_slug)):
                    cslug = norm_slug(row["href"])
                    if cslug in config.SECTOR_NAV_SLUGS or cslug in seen_c or cslug in tree:
                        continue
                    seen_c.add(cslug)
                    targets.append((cslug, row["title"]))
            except Exception as exc:
                print(f"  ERR index {idx_slug}: {exc}", flush=True)
                failed_pages.append({"slug": idx_slug, "kind": "circular_index",
                                     "title": "", "error": str(exc)[:200]})

        print(f"\n=== circular detail pages ({len(targets)}) ===", flush=True)
        for i, (cslug, ctitle) in enumerate(targets, 1):
            if i % 25 == 0 or i == 1:
                print(f"[circular {i}/{len(targets)}] {ctitle[:70]}", flush=True)
            try:
                page.goto(abs_url(cslug), wait_until="domcontentloaded")
                page.wait_for_timeout(400)
                data = page.evaluate(_PAGE_JS)
            except Exception as exc:
                print(f"  ERR circular {cslug}: {exc}", flush=True)
                failed_pages.append({"slug": cslug, "kind": "circular",
                                     "title": ctitle, "error": str(exc)[:200]})
                continue
            stats["circular_pages"] += 1
            _merge(by_id, _records_from_page(data, cslug, ctitle, ctitle, "circular"))

        browser.close()

    records = list(by_id.values())
    if config.REQUIRE_IN_FORCE:
        keep = [r for r in records if r.in_force]
        stats["skipped_not_in_force"] = len(records) - len(keep)
        records = keep

    write_json(config.CRAWL_REPORTS / "tree.json", {
        "generated": datetime.now(timezone.utc).isoformat(),
        "entry": config.ENTRY_PAGE, "nodes": len(tree), "tree": tree,
    })
    return records, stats


def plan(records: List[PdfRecord]) -> List[PdfRecord]:
    config.PDF_DIR.mkdir(parents=True, exist_ok=True)
    for rec in records:
        dest = config.PDF_DIR / _filename(rec)
        rec.local_path = str(dest.relative_to(config.ROOT)).replace("\\", "/")
        if not dest.exists():
            rec.action = "download"
            continue
        # A file already on disk is trusted only once it has been checked.
        # Otherwise a truncated leftover is skipped by every later run, and
        # re-running the stage quietly stops being a repair.
        bad = _reject_file(dest)
        if bad:
            rec.action = "redownload"
            rec.error = f"on disk but unusable: {bad}"
        else:
            rec.sha256 = sha256_file(dest)
            rec.content_length = dest.stat().st_size
            rec.action = "skip_exists"
    return records


def fetch(records: List[PdfRecord], timeout: int = 120) -> List[PdfRecord]:
    todo = [r for r in records if r.action in ("download", "redownload", "pending")]
    for i, rec in enumerate(todo, 1):
        name = _filename(rec)
        print(f"fetch [{i}/{len(todo)}] {name}", flush=True)
        dest = config.PDF_DIR / name
        part = dest.with_name(dest.name + ".part")
        url = safe_url(rec.pdf_url)
        last = "no attempt made"

        for attempt in range(config.FETCH_MAX_RETRIES):
            if attempt:
                delay = config.FETCH_BACKOFF_BASE ** attempt
                print(f"    retry {attempt}/{config.FETCH_MAX_RETRIES - 1} "
                      f"in {delay:.1f}s ({last})", flush=True)
                time.sleep(delay)
            try:
                req = urllib.request.Request(
                    url, headers={"User-Agent": config.USER_AGENT})
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    declared = resp.headers.get("Content-Length")
                    data = resp.read()
            except Exception as exc:
                last = str(exc)[:200]
                continue
            last = _reject_bytes(data, int(declared) if declared and declared.isdigit() else None)
            if last:
                continue
            # Rename only once the bytes are known good, so an interrupt cannot
            # leave a truncated .pdf that the next run would treat as complete.
            part.write_bytes(data)
            part.replace(dest)
            rec.sha256 = hashlib.sha256(data).hexdigest()
            rec.content_length = len(data)
            rec.action = "downloaded"
            rec.error = None
            break
        else:
            rec.action = "failed"
            rec.error = last

        if part.exists():
            part.unlink()
        time.sleep(0.12)
    return records


def write_report(records: List[PdfRecord], stats: dict, elapsed: float) -> None:
    dl = [r for r in records if r.action == "downloaded"]
    skip = [r for r in records if r.action == "skip_exists"]
    failed = [r for r in records if r.action == "failed"]
    unreachable = stats.get("failed_pages", [])
    on_disk = sorted(config.PDF_DIR.glob("*.pdf"), key=lambda p: p.name.lower())

    lines = [
        "# Rulebook crawl report", "",
        f"> {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"> Elapsed: {elapsed:.1f}s", "",
        "## Scan", "",
        f"- Pages visited: {stats['pages_visited']}",
        f"- Pages with >=1 PDF: {stats['pages_with_pdf']}",
        f"- Circular index pages: {stats['circular_indexes']}",
        f"- Circular detail pages: {stats['circular_pages']}",
        f"- Pages that failed to load: {len(unreachable)}",
        f"- Excluded as not In-Force: {stats['skipped_not_in_force']}"
        + ("" if config.REQUIRE_IN_FORCE else "  _(filter disabled)_"),
        f"- PDFs in manifest: {len(records)}", "",
        "## Fetch", "",
        f"- Downloaded: {len(dl)} | already present: {len(skip)} | failed: {len(failed)}", "",
    ]
    if failed:
        lines += ["## Failed downloads", "",
                  f"Retried {config.FETCH_MAX_RETRIES}x. Re-run the crawl stage to try again.", ""]
        lines += [f"- `{_filename(r)}` — {r.error}" for r in failed] + [""]
    if unreachable:
        lines += ["## Pages that failed to load", "",
                  "Any PDF on these pages is missing from the manifest, and a tree page "
                  "also takes its unvisited children with it. This is a coverage gap, "
                  "not just a fetch failure.", ""]
        lines += [f"- `{p['slug']}` ({p['kind']}) — {p['error']}" for p in unreachable] + [""]
    lines += [f"## PDFs on disk ({len(on_disk)})", ""]
    lines += [f"- `{p.name}`" for p in on_disk] + [""]

    (config.CRAWL_REPORTS / "crawl_report.md").write_text("\n".join(lines), encoding="utf-8")
    (config.CRAWL_REPORTS / "downloaded_files.txt").write_text(
        "\n".join([f"# {len(on_disk)} files"] + [p.name for p in on_disk]) + "\n", encoding="utf-8")
    write_json(config.CRAWL_REPORTS / "manifest.json", {
        "generated": datetime.now(timezone.utc).isoformat(),
        "require_in_force": config.REQUIRE_IN_FORCE,
        "stats": stats, "pdfs": [asdict(r) for r in records],
    })


def run(max_pages: int = 0, headless: bool = True, manifest_only: bool = False) -> int:
    config.ensure_dirs()
    t0 = time.time()
    records, stats = crawl(max_pages=max_pages, headless=headless)
    records = plan(records)
    if not manifest_only:
        records = fetch(records)
    write_report(records, stats, time.time() - t0)
    n_fail = sum(1 for r in records if r.action == "failed")
    n_pages = len(stats.get("failed_pages", []))
    print(f"\nCrawl done: {len(records)} PDFs | failed={n_fail} | "
          f"pages unreachable={n_pages} | {time.time() - t0:.1f}s")
    print(f"Report: {config.CRAWL_REPORTS / 'crawl_report.md'}")
    return 1 if (n_fail or n_pages) else 0
