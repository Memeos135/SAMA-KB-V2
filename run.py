#!/usr/bin/env python3
"""SAMA Knowledge Base — first-run pipeline.

    crawl → convert → build → enrich → audit

Build-once by design: there is no baseline, no delta and no update mode.
Refreshing the knowledge base is a full re-run, which keeps the pipeline small
and removes a whole class of partial-state bugs. Because acquisition filters to
in-force instruments, a re-run also retires superseded material automatically.

Stages are independent and safe to repeat. The enrichment resume log means the
paid stage picks up where it stopped rather than paying twice.

    python run.py --all
    python run.py --stage convert
    python run.py --stage enrich --skip-model     # free tier only
    python run.py --all --dry-run
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _load_env(path: Path = ROOT / ".env") -> None:
    """Load KEY=VALUE lines from .env without adding a dependency.

    Values already present in the environment win, so an explicit `export`
    always overrides the file. Secrets stay out of tracked source; .env is
    gitignored.
    """
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip("\"'")
        if key and value and not os.environ.get(key):
            os.environ[key] = value


_load_env()   # must run before sama.config reads the environment

from sama import audit, config, convert, crawl, enrich, graph  # noqa: E402
from sama.common import utf8_console  # noqa: E402

STAGES = ("crawl", "convert", "build", "enrich", "audit")


def _preflight(stages) -> list:
    """Report what is and is not ready before anything runs."""
    rows = []

    def ok(name, good, detail):
        rows.append((name, "ok" if good else "MISSING", detail))
        return good

    ok("python", sys.version_info >= (3, 9), f"{sys.version.split()[0]} (need >= 3.9)")

    if "convert" in stages:
        try:
            import fitz  # noqa: F401
            ok("PyMuPDF", True, "installed")
        except ImportError:
            ok("PyMuPDF", False, "pip install -r requirements.txt")

    if "crawl" in stages:
        try:
            import playwright  # noqa: F401
            ok("playwright", True, "installed (needs: python -m playwright install chromium)")
        except ImportError:
            ok("playwright", False, "pip install -r requirements.txt")

    if "convert" in stages:
        tess = config.tesseract_cmd()
        ok("tesseract", bool(tess), tess or "install tesseract, or set TESSERACT_CMD")
        ok("tessdata", config.TESSDATA.exists(), str(config.TESSDATA))

    if "build" in stages:
        ok("graphify", shutil.which(config.GRAPHIFY_BIN) is not None,
           shutil.which(config.GRAPHIFY_BIN) or f"'{config.GRAPHIFY_BIN}' not on PATH")
        ok("ANTHROPIC_API_KEY", bool(os.environ.get("ANTHROPIC_API_KEY", "").strip()),
           "used by graphify extract")

    if "enrich" in stages:
        has_key = bool(os.environ.get(config.ENRICH_KEY_ENV, "").strip()
                       or os.environ.get("ANTHROPIC_API_KEY", "").strip())
        ok(config.ENRICH_KEY_ENV, has_key,
           f"model {config.ENRICH_MODEL} (falls back to ANTHROPIC_API_KEY)")
        if has_key and not config.ENRICH_WORKSPACE_ID:
            rows.append(("workspace-id", "check",
                         "unset — required only if the key is identity-linked"))

    width = max(len(r[0]) for r in rows)
    print("\nPreflight")
    print("-" * (width + 40))
    for name, status, detail in rows:
        print(f"  {name.ljust(width)}  {status:<8} {detail}")
    print()
    return [r for r in rows if r[1] != "ok"]


def main() -> int:
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all", action="store_true", help="run every stage in order")
    ap.add_argument("--stage", choices=STAGES, action="append", default=[],
                    help="run one stage (repeatable)")
    ap.add_argument("--from-stage", choices=STAGES, help="run this stage and everything after it")
    ap.add_argument("--dry-run", action="store_true", help="preflight only, run nothing")

    ap.add_argument("--max-pages", type=int, default=0, help="crawl: cap pages visited")
    ap.add_argument("--headed", action="store_true", help="crawl: show the browser")
    ap.add_argument("--manifest-only", action="store_true", help="crawl: do not download")

    ap.add_argument("--limit", type=int, default=0, help="convert: cap PDFs processed")
    ap.add_argument("--stems", nargs="*", help="convert: only these stems")
    ap.add_argument("--force-ocr", action="store_true", help="convert: OCR everything")

    ap.add_argument("--skip-extract", action="store_true", help="build: reuse the current graph")
    ap.add_argument("--no-dedup", action="store_true", help="build: keep duplicate-label nodes")

    ap.add_argument("--skip-model", action="store_true",
                    help="enrich: deterministic grounding + render only, no API calls")
    ap.add_argument("--skip-edge-narratives", action="store_true",
                    help="enrich: node summaries and communities only")
    ap.add_argument("--limit-nodes", type=int, default=0, help="enrich: cap nodes (smoke test)")
    ap.add_argument("--apply-only", action="store_true",
                    help="enrich: re-render notes from existing grounding + log")
    args = ap.parse_args()

    stages = list(args.stage)
    if args.from_stage:
        stages += list(STAGES[STAGES.index(args.from_stage):])
    if args.all or not stages:
        stages = list(STAGES)
    stages = [s for s in STAGES if s in set(stages)]

    config.ensure_dirs()
    missing = _preflight(stages)
    if args.dry_run:
        print("Dry run — nothing executed.")
        print(f"Stages that would run: {' → '.join(stages)}")
        return 1 if missing else 0
    if missing:
        print("Refusing to start: resolve the MISSING items above "
              "(or pick stages that do not need them with --stage).")
        return 1

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = config.RUNS_DIR / stamp
    run_dir.mkdir(parents=True, exist_ok=True)
    print(f"Run: {run_dir}\nStages: {' → '.join(stages)}")

    t0 = time.time()
    rc = 0
    for stage in stages:
        print(f"\n{'=' * 70}\n== {stage.upper()}\n{'=' * 70}")
        st = time.time()
        if stage == "crawl":
            code = crawl.run(max_pages=args.max_pages, headless=not args.headed,
                             manifest_only=args.manifest_only)
        elif stage == "convert":
            code = convert.run(limit=args.limit, stems=args.stems, force_ocr=args.force_ocr)
        elif stage == "build":
            code = graph.run(skip_extract=args.skip_extract, no_dedup=args.no_dedup)
        elif stage == "enrich":
            code = enrich.run(skip_model=args.skip_model,
                              skip_edges=args.skip_edge_narratives,
                              limit_nodes=args.limit_nodes or None,
                              apply_only=args.apply_only)
        else:
            code = audit.run()
        print(f"-- {stage} finished in {time.time() - st:.1f}s (exit {code})")
        if code != 0:
            rc = code
            if stage != "crawl":     # crawl exits non-zero on partial download failures
                print(f"Stopping: {stage} failed.")
                break

    for name in ("crawl/crawl_report.md", "conversion/CONVERSION_QUALITY_REPORT.md",
                 "graph/GRAPH_QUALITY_AUDIT.md", "graph/dedup.json"):
        src = config.REPORTS / name
        if src.exists():
            shutil.copy2(src, run_dir / Path(name).name)

    print(f"\n{'=' * 70}")
    print(f"Run complete in {time.time() - t0:.1f}s (exit {rc}) → {run_dir}")
    if config.USAGE_LOG.exists():
        enrich.report_usage()
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
