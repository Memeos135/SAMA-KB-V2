# Agent workflow v2 — counsel / digger / auditor

Runs **alongside** v1. Nothing in `docs/agents/*.md` or the v1 entries in
`.opencode/opencode.json` was changed or removed. Pick a stack at the Tab menu:

| Pick | Stack |
|---|---|
| `orchestrator` | v1 — legal → mapper ×N → extractor ×N → reviewer → formatter |
| `counsel` | v2 — retrieve → dig ×N → document → verify |

## Why v2 exists

v1 answered "where do I look" by fanning out model agents to grep 379 corpus files
(11.7 MB, one instrument of 902 pages). That question was already answered offline:
`enrich` wrote lookup terms, regimes, communities and page-exact grounding. v2 reads
those artifacts with a script and spends the model budget on reading law instead.

It also deletes the output formatter. In v1 the last stage before the user compressed
eight researched sections into "1–5 short paragraphs" — a full serial generation whose
only product was less depth. In v2 Counsel writes the document directly.

```
 v1   orchestrator → legal → mapper ×3 → legal → extractor ×3 → legal
                   → reviewer → [loop ×2] → formatter → user
 v2   counsel ─ sama.retrieve      (script, no tokens)
               ├─ digger ×N        (parallel, only when >3 stems)
               ├─ sama.cite verify (counsel runs it)
               └─ auditor          (reads; runs nothing)
```

Roughly eight serial model turns become three.

## Who may do what, and why

Three roles, and each one's permissions are exactly its role:

| Agent | Is | Tools | Cannot |
|---|---|---|---|
| `counsel` | orchestrator + author | `sama.retrieve`, Task `digger`/`auditor` | Read the corpus. Fetch a page. Run `sama.cite`. |
| `digger` | information obtainer | `sama.cite fetch`, read `corpus/markdown/**` | Grep or glob. Search is retrieval's job. |
| `auditor` | fact checker | `sama.cite` | Read the corpus raw. Dig for material. |

`sama.retrieve` sits with counsel because it returns stems, pages and scores — a routing
table, not law. Counsel needs it to know how many diggers to spawn.

The point of the table is that **each boundary is enforced by permission, not by
instruction.** Counsel does not decline to dig; it cannot dig. That matters because a
prompt that asks an agent not to use a tool it holds will lose: fetching a page directly
is faster and simpler than spawning a subagent, so a model will always take that path.
Every stem therefore goes to a digger — there is no floor, and one stem is one digger.

Two rules follow from that table and are worth stating outright, because breaking either
one is what makes an agent hang rather than fail:

**Permissions are declared in `.opencode/opencode.json` and nowhere else.** The agent
`.md` files carry only the prompt. Declaring them twice guarantees drift, and a prompt
that instructs work the permissions forbid produces an agent that probes the sandbox
instead of stopping.

**Every agent has a two-attempt limit.** On a refused or failing command it reports the
failure in its output and continues. It never investigates the permission model, tries
another shell or encoding, or creates a file — no agent in this workflow can write, and
none needs to. Verification uses `--claim` for exactly that reason:

```bash
python -m sama.cite verify --claim "SAMA_EN_1734_VER1:12:Minimum contents must include methods"
```

An argv string needs no temp file, no write permission and no console-encoding
negotiation. `--claims PATH` and `--claims -` remain for humans, and now cope with
PowerShell's UTF-16 redirection.

## Nothing opens a whole document

`sama.retrieve` never emits a "whole document" brief. A stem with no grounded page is
scanned for the facet, then for its own node label; a small document is enumerated page
by page; and anything still without page-level signal is reported under **Surfaced but
not scheduled** rather than handed to a digger. `sama.cite fetch` caps a single call at
`CITE_FETCH_MAX_PAGES` and announces truncation.

Between them that closes the case this corpus makes inevitable: `SAMA_EN_3487_VER1` is
902 pages and 1.9 MB, and one unbounded fetch of it ends a run.

## The two scripts

Retrieval and citation checking are string operations, so they are scripts — the same
split `sama/enrich.py` already makes for grounding.

```bash
# where do I look — term -> node -> stem -> page, over graph.json + grounding.json
python -m sama.retrieve --facet "customer due diligence" --facet "reliance on third parties"
python -m sama.retrieve "APR cap on administrative fees" --regime BNPL/finance --json

# open one page instead of a 1.9 MB file
python -m sama.cite fetch --stem SAMA_EN_1734_VER1 --pages 6,10-14

# does this quote really sit at this locator
python -m sama.cite verify --claims claims.json
```

Thresholds live in `sama/config.py` under *Query-time retrieval*.

### Retrieval is recall-first, by design

A stem retrieved and discarded costs one page read. A stem never retrieved is a silent
hole in the answer. So `sama.retrieve`:

- treats term hits as **entry points**, then expands along graph neighbours and
  communities (`RETRIEVE_EXPAND_*`), because a question rarely names the node that
  holds the answer;
- requires a node to carry `RETRIEVE_MIN_COVERAGE` of a facet's tokens, so one shared
  word cannot make an unrelated node look like a hit and hide a real miss;
- never returns a bare "open the whole document" — a stem with no grounded page is
  scanned for the facet, then for its own node label, and the document's page count is
  reported either way;
- falls back to a **conjunctive full-text scan** of `corpus/markdown/` for any facet the
  index does not know. The index is graph-derived, so a miss there means *never
  extracted as a node*, not *absent from the law*. Anything the scan recovers is
  reported under `Recovered by corpus scan`;
- reports what survives neither as `NOT_FOUND_IN_CONTEXT` — a defensible negative
  rather than a retrieval failure;
- packs the surviving stems into balanced dig buckets, weighted by page count, so no
  digger gets the 902-page instrument plus five others.

### Citation checking is deterministic

`sama.cite verify` compares after normalising whitespace, case, quote glyphs and Arabic
presentation forms, so an OCR'd page does not produce false failures. It separates
`PAGE_MISMATCH` (quote real, locator wrong — the defect a model reviewer misses most)
from `MISSING` (not in the document at all).

## Completeness contract

Counsel emits **every section, every time**; an empty one says so explicitly. The
Facet ledger lists every facet decomposed in step 1 with a status, and the Auditor's
first job is to catch a facet that never reached the ledger — a stated gap is
acceptable, an unstated one is not.

## Before first use

1. **Pin models.** No `model` key is set, so all three inherit your default. The point
   of the split is that `digger` is mechanical and `counsel` is not:

   ```json
   "counsel": { "model": "<your strong model>" },
   "digger":  { "model": "<your fast model>" },
   "auditor": { "model": "<your strong model>" }
   ```

   Set them in `.opencode/opencode.json`. This is the largest single wall-clock lever.

2. **Restart OpenCode**, then Tab → `counsel` and ask the question.

3. `subagent_depth` stays at `5` for v1's sake; v2 never nests deeper than 2.

## Cursor

```
Act as .opencode/agents/counsel.md.
QUESTION: <…>
```

## Rolling back

Delete the `counsel` / `digger` / `auditor` entries from `.opencode/opencode.json`.
The scripts and this directory are inert on their own, and v1 never reads them.
