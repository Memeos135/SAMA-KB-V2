# SAMA Knowledge Base — session memory

> Runbook for IDE/agent continuity. **Not** a second source of truth for layout —
> see `README.md` for folders, `docs/PIPELINE.md` for data flow, and
> `docs/PROPOSAL.md` for scope and design rationale.

## Project

| Field | Value |
|---|---|
| Objective | SAMA regulatory PDFs → corpus MD → graph → Obsidian vault → agent-queryable notes |
| Mode | **Build-once.** No baseline, no delta, no update path. |
| Entry point | `python run.py --all` |
| Graph toolchain | `graphify` on PATH (`GRAPHIFY_BIN` to override); extraction model pinned |
| Enrichment | direct Anthropic API, `SAMA_ENRICH_MODEL`, `SAMA_ENRICH_API_KEY` |
| Ingest root | `corpus/` (markdown under `corpus/markdown/`) |
| Vault | `SAMA_Knowledge_Base_Obsidian/` — open THIS in Obsidian |
| Agent personas | `docs/agents/` (specs) + `.opencode/agents/` (OpenCode wiring) |

Live counts: read `graphify-out/graph.json` or the audit report. Do not trust
remembered numbers.

## Source-of-truth hierarchy

| Topic | Authoritative |
|---|---|
| Scope, principles, risks | `docs/PROPOSAL.md` |
| Layout & commands | `README.md` |
| Data flow & artifacts | `docs/PIPELINE.md` |
| Paths, thresholds, models | `sama/config.py` — nothing else may hardcode them |
| Regulatory text | `corpus/markdown/*.md` |
| Navigation | `SAMA_Knowledge_Base_Obsidian/_INDEX_Routing.md` |
| Conversion QA | `reports/conversion/` |
| Graph QA | `reports/graph/` |

**Corpus text wins** over the graph, the vault or any generated prose.

## For the agent workflow

The vault is a **navigation layer**, never authority:

- `_INDEX_Routing.md` — regime → concepts, community → start-here, hubs, lookup
  terms → concept → source document, source document → concepts. Start here; it
  exists so the Mapper does not have to read the corpus to decide where to look.
- Concept notes — a short summary, regimes, sources, and per-connection grounding:
  a verbatim excerpt with an exact `stem · Page N` locator.
- Every excerpt is sliced from the corpus, so it can be trusted as a pointer — but
  the Extractor still quotes from `corpus/markdown/` for the record.

Caveats on a connection are machine-derived (relationship confidence, weak
relation type, broken-Arabic source), not model opinion.

## Quality position

- Grounding is verbatim by construction; the audit's grounding score is a **drift
  check** (did a source change after grounding ran?), not a hallucination check.
- Page locators are derived from byte offsets, so they are exact.
- Broken-Arabic exposure is measured directly from the corpus and is reported even
  before anything has been graded.
- Any dimension the audit cannot measure grades **N/A** and is excluded from the
  average — it never grades as a pass.

## Open items

- [ ] First full run: `python run.py --all --dry-run`, then `--all`.
- [ ] After the run, read `reports/graph/GRAPH_QUALITY_AUDIT.md` — expect
      broken-Arabic exposure near 0% and no duplicate-label clusters.
- [ ] Review `quarantine/` and the conversion report's priority actions; decide
      per document whether to re-source the PDF or accept the gap.
- [ ] Tune `SAMA_EDGE_NARRATIVE_MAX` once real queries show how often the
      relationship narratives are actually hit. If the Mapper routes off
      `_INDEX_Routing.md` and community notes alone, this tier can shrink.
- [ ] Reconcile the cost ledger's dollar estimates against the provider console;
      the token counts are exact, the price table in `sama/config.py` is not.

## Recovery

1. Read `README.md` + `docs/PIPELINE.md`.
2. `python run.py --all --dry-run` to see what is wired up.
3. If the graph is broken: restore from `archive/graphify-snapshots/`, or re-run
   `python run.py --from-stage build`.
4. If enrichment stopped mid-way: just re-run it. `enrichment.jsonl` is a resume
   log; completed work is not re-paid.
