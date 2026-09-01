# Pipeline — data flow and artifacts

```
rulebook.sama.gov.sa
        │  crawl        (playwright, one pass: tree + status + PDF links)
        ▼
scanner-sama-docs/*.pdf ─── reports/crawl/{tree,manifest}.json, crawl_report.md
        │  convert      (text layer → OCR when thin / presentation-form / isolated-Arabic)
        ▼
corpus/markdown/*.md ────── reports/conversion/conversion_quality.json
        │                                        CONVERSION_QUALITY_REPORT.md
        │               grade F → quarantine/  (never reaches the graph)
        │  build        (snapshot → extract → dedup → cluster → label → export)
        ▼
graphify-out/graph.json ─── reports/graph/dedup.json
        │
        ▼
SAMA_Knowledge_Base_Obsidian/*.md      (raw graphify export)
        │  enrich
        │    ├─ ground()        free    → graphify-out/grounding.json
        │    ├─ enrich()        paid    → graphify-out/enrichment.jsonl
        │    │                            graphify-out/usage.jsonl
        │    ├─ render()        free    → rewrites vault notes
        │    └─ routing_index() free    → vault/_INDEX_Routing.md
        ▼                                 reports/graph/routing_index.json
        │  audit        (read-only)
        ▼
reports/graph/GRAPH_QUALITY_AUDIT.md + graph_quality_audit.json
```

## Artifacts

| Path | Written by | Survives a re-run? |
|---|---|---|
| `scanner-sama-docs/*.pdf` | crawl | yes — existing files are skipped |
| `corpus/markdown/*.md` | convert | overwritten |
| `quarantine/*.md` | convert | overwritten |
| `graphify-out/graph.json` | build | replaced only after a successful extract |
| `archive/graphify-snapshots/` | build | one snapshot per build |
| `graphify-out/grounding.json` | enrich (free) | regenerated each run |
| `graphify-out/enrichment.jsonl` | enrich (paid) | **append-only resume log** — delete to re-pay |
| `graphify-out/usage.jsonl` | enrich (paid) | append-only cost ledger |
| `SAMA_Knowledge_Base_Obsidian/*.md` | build + enrich | rewritten by render |
| `reports/**` | every stage | overwritten |
| `reports/runs/<stamp>/` | run.py | one directory per run |

## Cost control

Only two stages spend money.

**build** — graph extraction. The model is pinned because graphify 0.9.23 breaks
on models that emit thinking blocks.

**enrich** — split into a free tier and a paid tier:

- *free*: every excerpt, every page locator, every caveat, the routing index
- *paid*: one summary per node (context sent **once**, not once per edge),
  one blurb per community, and a narrative for ~22% of edges

To rehearse without spending anything:

```bash
python run.py --stage enrich --skip-model     # grounding + render only
python run.py --stage enrich --limit-nodes 12 # small paid smoke test
```

Every API call appends to `graphify-out/usage.jsonl`; `run.py` prints the
running total at the end of a run.

## Re-running a stage

Stages are independent and idempotent.

```bash
python run.py --stage convert --stems SAMA_EN_5565_VER1 SAMA_EN_10959_VER1
python run.py --stage build --skip-extract      # re-dedup/cluster/export only
python run.py --stage enrich --apply-only       # re-render from existing data
python run.py --stage audit
```

`enrich` never re-pays for work already in `enrichment.jsonl`. To force a fresh
paid pass, delete that file.
