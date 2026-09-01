# Query config — Map → Dig workflow

> Load for **every** regulatory / compliance question.  
> Pipeline: **Orchestrator → Legal → Mapper ×N → Extractor ×N → Reviewer ⇄ Legal → Formatter**.  
> Absolute “never miss anything” is impossible with retrieval limits; this config **forbids silent omission**.

Personas:
- `00_orchestrator.md` — user-facing; Tasks only
- `01_legal_compliance.md` — facets + interpret; Tasks Mapper then Extractor
- `01a_corpus_mapper.md` — Coverage Map (grep/graph survey)
- `01b_corpus_extractor.md` — Evidence Packs (dig assigned stems)
- `02_completeness_reviewer.md` — **strict cites**, loose coverage; prefer `APPROVED_WITH_GAPS`
- `03_output_formatter.md` — user-facing package

OpenCode: Tab → **`orchestrator`**, then ask the question.

---

## 0. Hard rules (always on)

1. **Corpus text wins** over Graphify enrichment, Obsidian paraphrase, or memory.
2. **Cite** every material claim: `corpus/markdown/<file>.md` + `## Page N` and/or article/section.
3. If not in Evidence Pack / opened sources → **`UNCERTAIN`** or **`NOT_FOUND_IN_CONTEXT`** — do not invent.
4. **Do not finalize** until Completeness Reviewer issues `APPROVED` or `APPROVED_WITH_GAPS`.
5. Graph / enrichment = **navigation map only**, not authority.
6. **Separation of duties:** Mapper surveys; Extractor digs/quotes; Legal interprets; Reviewer audits; Formatter presents; Orchestrator routes.
7. Legal must **not** Grep/Glob the corpus; it **Tasks** `corpus-mapper` then `corpus-extractor`.
8. **Parallelism:** fan-out **2–5** (default **3**) Mappers and/or Extractors per wave in **one turn**; soft max **6**. No single mega-brief for multi-facet questions.
9. **Completeness** = survey (map) + prioritized dig + visible gaps — not deep-quoting every community.
10. **Paths:** agents must use **repo-relative** paths only (`corpus/markdown/...`, `graphify-out/...`). Never invent `C:\Users\...` absolute paths — typos hang outside the worktree. `external_directory` is denied.

---

## 1. Modes

| Mode | Behavior |
|---|---|
| `complete` (default) | Full Map→Dig workflow including formatter |
| `legal_only` | Legal Map→Dig only (no review/format) |
| `review_only` | User has a Legal draft; Reviewer (+ optional Legal pushback) then Formatter |

---

## 2. Retrieval

### Map (Mapper)
1. Grep facet keywords across `corpus/markdown/`.
2. Attach hits to graph communities when available (`graphify-out/`).
3. Rank P1/P2/P3; return Coverage Map + dig plan — not long quote packs.

### Dig (Extractor)
1. Open map-assigned stems first.
2. Verbatim excerpts + locators into Evidence Packs.
3. Prefer primary instruments unless the brief asks for forms.
4. Flag OCR/garbled text; note EN twins when relevant.

---

## 3. Pass cycle (`complete` mode)

1. **Legal** facets → parallel **Mappers** → merge maps → parallel **Extractors** on P1 → Legal memo.
2. **Reviewer** audits — **strict on citations**, loose on exhaustive map/dig. Prefer `APPROVED_WITH_GAPS`. `NEEDS_REVISION` only for bad/missing material cites or silent core-ask miss.
3. Outer Orchestrator loop cap: **2** unless user asks for more.
4. **Output Formatter** → Final answer / Coverage / Gaps / Sources.

---

## 4. Copy-paste (Cursor / manual)

```
CONFIG: Follow docs/agents/query_config.md (mode=complete).
Act as docs/agents/00_orchestrator.md.

QUESTION:
<paste question>
```

---

## 5. Honesty clause

This config maximizes completeness and makes misses **visible**.  
It cannot guarantee zero omissions across the entire rulebook in one shot.  
For exam-critical decisions: treat residual `UNCERTAIN` / `NOT_FOUND_IN_CONTEXT` as stop-points for human counsel.
