"""Single source of truth for paths, thresholds and model/key selection.

Everything in this file is either a fixed project path or an environment
override.  No other module may hardcode a path, a threshold or a model name.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _env_path(name: str, default: Path) -> Path:
    raw = os.environ.get(name, "").strip()
    return Path(raw) if raw else default


# --------------------------------------------------------------------------- #
# Paths
#
# Directory names are part of the contract with the OpenCode agent permissions
# (`corpus/markdown/**`) and the personas in docs/agents/ - do not rename these
# without updating both.
# --------------------------------------------------------------------------- #

PDF_DIR = ROOT / "scanner-sama-docs"          # downloaded rulebook PDFs
CORPUS_DIR = ROOT / "corpus"                  # graphify ingest root
CORPUS_MD = CORPUS_DIR / "markdown"           # converted regulatory text
QUARANTINE = ROOT / "quarantine"              # grade-F conversions, kept out of the graph
OCR_TMP = ROOT / ".ocr-tmp"                   # page renders; deleted after OCR

GRAPH_DIR = ROOT / "graphify-out"
GRAPH_JSON = GRAPH_DIR / "graph.json"
GROUNDING_JSON = GRAPH_DIR / "grounding.json"        # deterministic, no tokens
ENRICH_LOG = GRAPH_DIR / "enrichment.jsonl"         # append-only resume log
USAGE_LOG = GRAPH_DIR / "usage.jsonl"               # per-call token/cost ledger

VAULT_DIR = _env_path("GRAPHIFY_VAULT_DIR", ROOT / "SAMA_Knowledge_Base_Obsidian")

REPORTS = ROOT / "reports"
CRAWL_REPORTS = REPORTS / "crawl"
CONV_REPORTS = REPORTS / "conversion"
GRAPH_REPORTS = REPORTS / "graph"
RUNS_DIR = REPORTS / "runs"
CONV_JSON = CONV_REPORTS / "conversion_quality.json"

ARCHIVE = ROOT / "archive"
SNAPSHOTS = ARCHIVE / "graphify-snapshots"

TESSDATA = ROOT / "tools" / "tessdata"

# Directories that must exist before a run; all are re-derivable.
RUNTIME_DIRS = (
    PDF_DIR, CORPUS_MD, QUARANTINE, GRAPH_DIR, VAULT_DIR,
    CRAWL_REPORTS, CONV_REPORTS, GRAPH_REPORTS, RUNS_DIR, SNAPSHOTS,
)


# --------------------------------------------------------------------------- #
# Crawl
# --------------------------------------------------------------------------- #

BASE_URL = "https://rulebook.sama.gov.sa"
ENTRY_PAGE = "/en/finance-sector-0"
USER_AGENT = "SAMA-KB-Crawl/2.0"

# Only ingest instruments the regulator currently presents as in force. Applied
# uniformly to tree pages and circular pages, so superseded material never
# enters the corpus.
IN_FORCE_STATUSES = {"in-force", "in force"}
REQUIRE_IN_FORCE = os.environ.get("SAMA_REQUIRE_IN_FORCE", "1") != "0"

# A download is accepted only once the bytes have been checked.  A truncated
# body and an error page served as HTTP 200 both arrive without raising, so
# neither the status code nor the absence of an exception is evidence.
FETCH_MAX_RETRIES = 3
FETCH_BACKOFF_BASE = 2.0
MIN_PDF_BYTES = 1024

SKIP_HREFS = {
    "/en", "/en/search", "/en/view-revision-updates", "/en/terms-and-conditions",
}
SECTOR_NAV_SLUGS = {
    "/en/laws-and-implementing-regulations", "/en/all-financial-institutions",
    "/en/banking-sector-0", "/en/finance-sector-0",
    "/en/payment-systems-and-payment-services-providers",
    "/en/money-exchange-sector-0", "/en/credit-bureaus",
    "/en/regulatory-sandbox", "/en/sama-circulars",
}


# --------------------------------------------------------------------------- #
# Conversion / OCR routing
# --------------------------------------------------------------------------- #

DPI = 200
OCR_LANG = "eng+ara"

THIN_CPP = 400            # chars/page below this => text layer is unusable
ISOLATED_AR_OCR = 0.12    # rate of 1-2 letter Arabic fragments => broken bidi
PF_SHARE_OCR = 0.02       # share of Arabic *presentation-form* glyphs => the
                          # text layer holds rendered glyphs in visual order and
                          # is unsearchable, however dense it looks

EMPTY_PAGE_CHARS = 20
COVERAGE_WARN = 0.85
COVERAGE_FAIL = 0.60
ARABIC_SHARE_WARN = 0.15
ISOLATED_AR_WARN = 0.08
GARBAGE_WARN = 0.05

NEAR_DUP_THRESHOLD = 0.90
NEAR_DUP_LENGTH_BAND = 0.10   # only compare docs within +/-10% length

# Grade F documents are quarantined instead of being fed to the graph.
QUARANTINE_GRADE = "F"


def tesseract_cmd() -> str | None:
    """Locate the tesseract binary without assuming a Windows install path."""
    env = os.environ.get("TESSERACT_CMD", "").strip()
    if env and Path(env).exists():
        return env
    found = shutil.which("tesseract")
    if found:
        return found
    for cand in (
        "/opt/homebrew/bin/tesseract",
        "/usr/local/bin/tesseract",
        "/usr/bin/tesseract",
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    ):
        if Path(cand).exists():
            return cand
    return None


# --------------------------------------------------------------------------- #
# Graph build
# --------------------------------------------------------------------------- #

GRAPHIFY_BIN = os.environ.get("GRAPHIFY_BIN", "graphify")

# The extraction backend is pinned: graphify 0.9.23 breaks on models that emit
# thinking blocks.  Enrichment talks to the API directly and is not subject to
# that constraint, so it is configured separately below.
GRAPHIFY_MODEL = os.environ.get("GRAPHIFY_MODEL", "claude-opus-4-8")
GRAPHIFY_MODE = os.environ.get("GRAPHIFY_MODE", "deep")
GRAPHIFY_API_KEY_ENV = "ANTHROPIC_API_KEY"

DEDUP_NODES = os.environ.get("SAMA_DEDUP_NODES", "1") != "0"


# --------------------------------------------------------------------------- #
# Enrichment (model layer)
# --------------------------------------------------------------------------- #

API_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"

ENRICH_MODEL = os.environ.get("SAMA_ENRICH_MODEL", "claude-opus-5")
ENRICH_KEY_ENV = "SAMA_ENRICH_API_KEY"      # falls back to ANTHROPIC_API_KEY

# Identity-linked API keys must name the workspace the request acts in; the API
# rejects them with HTTP 400 otherwise. Ordinary org keys ignore this.
ENRICH_WORKSPACE_ID = os.environ.get("SAMA_ENRICH_WORKSPACE_ID", "").strip()

ENRICH_WORKERS = int(os.environ.get("SAMA_ENRICH_WORKERS", "6"))
ENRICH_MAX_RETRIES = 5
ENRICH_BACKOFF_BASE = 2.0

NODE_BATCH = 6
COMMUNITY_BATCH = 4
EDGE_BATCH = 5

MAX_CONTEXT_CHARS = 4500     # per node, sent once per node (not once per edge)
MAX_EXCERPT_CHARS = 280

# Per-edge narratives are the expensive tier, so they are earned rather than
# universal.  An edge qualifies when it crosses communities, when its confidence
# is not EXTRACTED (the reader needs framing to know how far to trust it), or
# when it touches a hub.
EDGE_NARRATIVE_CROSS_COMMUNITY = True
EDGE_NARRATIVE_LOW_CONFIDENCE = {"INFERRED", "AMBIGUOUS"}
EDGE_NARRATIVE_HUB_DEGREE = 8
EDGE_NARRATIVE_MAX = int(os.environ.get("SAMA_EDGE_NARRATIVE_MAX", "400"))

WEAK_RELATIONS = {"conceptually_related_to", "semantically_similar_to"}

# Published list prices (USD per million tokens) used only for the run ledger.
PRICES = {
    "claude-opus-5": (5.0, 25.0),
    "claude-opus-4-8": (5.0, 25.0),
    "claude-sonnet-5": (3.0, 15.0),
    "claude-haiku-4-5-20251001": (1.0, 5.0),
}


def enrich_api_key() -> str:
    """Key for the enrichment model.  Deliberately separate from the graphify
    key so the two stages can bill to different accounts."""
    for env in (ENRICH_KEY_ENV, "ANTHROPIC_API_KEY"):
        key = os.environ.get(env, "").strip()
        if key:
            return key
    raise SystemExit(
        f"No enrichment API key. Set {ENRICH_KEY_ENV} (preferred) or ANTHROPIC_API_KEY:\n"
        f'  export {ENRICH_KEY_ENV}="sk-ant-..."'
    )


# --------------------------------------------------------------------------- #
# Audit thresholds
# --------------------------------------------------------------------------- #

GROUND_A, GROUND_B, GROUND_C = 0.90, 0.75, 0.60
UNDEREXTRACT_FRAC = 0.5


def ensure_dirs() -> None:
    for d in RUNTIME_DIRS:
        d.mkdir(parents=True, exist_ok=True)
