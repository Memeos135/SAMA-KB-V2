# Agent workflow — Map → Dig

```
orchestrator
  → legal-compliance
       → corpus-mapper × N      (grep/graph → Coverage Map)
       → corpus-extractor × N   (dig P1 stems → Evidence Packs)
  → completeness-reviewer  ⇄  legal-compliance
  → output-formatter
  → you
```

| Agent | OpenCode name | Spec | Job |
|---|---|---|---|
| Orchestrator | `orchestrator` (primary) | `00_orchestrator.md` | Route Tasks |
| Legal / Compliance | `legal-compliance` | `01_legal_compliance.md` | Facets + interpret; owns Map→Dig |
| Corpus Mapper | `corpus-mapper` | `01a_corpus_mapper.md` | Survey only |
| Corpus Extractor | `corpus-extractor` | `01b_corpus_extractor.md` | Dig / quote |
| Completeness Reviewer | `completeness-reviewer` | `02_completeness_reviewer.md` | Gate + pushback |
| Output Formatter | `output-formatter` | `03_output_formatter.md` | User package |

Config: `query_config.md`

## How to use (OpenCode)

1. Restart OpenCode after agent changes.
2. Tab → **`orchestrator`**.
3. Ask the question only.

Expect nested Tasks: Legal → Mappers → Extractors → Reviewer → Formatter.

## Cursor

```
Act as docs/agents/00_orchestrator.md.
QUESTION: <…>
```
