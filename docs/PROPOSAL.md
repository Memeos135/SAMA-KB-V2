# SAMA Regulatory Knowledge Base — Project Proposal

**Status:** Approved for build · **Version:** 1.0 · **Owner:** Legal & Compliance

---

## 1. Executive summary

Saudi Central Bank (SAMA) rules governing our licensed activities are published as
several hundred PDFs across the SAMA Rulebook — laws, implementing regulations,
circulars and guides, in English and Arabic, spanning AML/CTF, payments, BNPL and
finance companies, consumer protection, credit information, sanctions, and
governance. Answering a single regulatory question today means knowing which of
those documents matter, opening them individually, and reading around the
cross-references between them.

This project builds an automated pipeline that turns that corpus into a
**knowledge graph and a searchable Obsidian vault**, where every regulatory
concept is a node, every cross-reference is a traceable link, and every link
carries a **verbatim quotation with an exact page citation** back to the source
instrument.

The output is consumed two ways: by a person browsing the vault, and by an
agent workflow that answers regulatory questions with cited evidence.

The design principle throughout: **the corpus is the authority; the graph is
navigation.** Nothing in the knowledge base is ever presented as a substitute for
the regulatory text, and every assertion in it resolves to a page a human can open.

---

## 2. Problem statement

| Problem | Consequence |
|---|---|
| Rules are distributed across hundreds of separate PDFs | No single view of what applies to a given activity |
| Obligations cross-reference each other implicitly | Dependencies are discovered by accident, not by design |
| Regimes use different words for the same actor (BNPL "Consumer" vs AML "Customer"; merchant-as-customer) | Cross-regime gaps go unnoticed until a review finds them |
| A material share of the corpus is Arabic, some of it scanned or badly encoded | Those instruments are effectively invisible to text search |
| Superseded instruments sit alongside in-force ones | Risk of relying on a repealed rule |
| Answering a question requires reading rather than retrieving | Slow, and completeness cannot be evidenced |

The last two are the ones that carry real risk. A knowledge base that quietly
includes a repealed circular, or that silently drops a document because its text
could not be decoded, is worse than no knowledge base — it produces confident
answers with invisible holes.

---

## 3. Objectives

**Primary**

1. Acquire every in-force instrument from the SAMA Rulebook automatically.
2. Convert each to searchable text, including Arabic, with measured quality.
3. Build a knowledge graph of concepts and their relationships.
4. Ground every relationship in a verbatim quote with an exact page citation.
5. Publish an Obsidian vault usable by both humans and the agent workflow.
6. Report the knowledge base's own quality honestly, including what it does not know.

**Explicit non-goals**

- Not a source of legal advice. It routes to primary text; it does not replace counsel.
- Not an update/monitoring service. This is a **build-once** pipeline; refresh is
  a re-run, not an incremental sync.
- Not a general document store. Non-regulatory material is out of scope.

---

## 4. Design principles

**1. Corpus text wins.** The graph, the vault and any generated prose are
navigation aids. Where they disagree with `corpus/markdown/`, the corpus is right.

**2. Use a language model only where nothing else can do the job.** Retrieving a
quotation and locating its page are string operations — a script does them
exactly, for free, every time. Summarising a regulatory theme is synthesis, and
that is what the model is for. Cost follows this line, and so does reliability.

**3. Missing measurements are reported as missing.** A quality dimension that
cannot be computed grades `N/A` and is excluded from the score. A quality report
that cannot fail is not a quality report.

**4. Bad input is quarantined, not ingested.** A document that fails conversion
is held out of the graph and named in the report, rather than contributing empty
or garbled nodes.

**5. Every artifact is re-derivable.** Only source code, configuration and agent
definitions are durable. Corpus, graph, vault and reports are outputs and can be
deleted at any time.

**6. Never half-update the live graph.** The existing graph is snapshotted before
a build and replaced only after a successful extraction.

---

## 5. Solution architecture

```
                     rulebook.sama.gov.sa
                              │
            ┌─────────────────▼─────────────────┐
            │  1. CRAWL                          │   free
            │  one browser pass: tree structure, │
            │  publication status, PDF links     │
            │  in-force filter applied at source │
            └─────────────────┬─────────────────┘
                              │  scanner-sama-docs/*.pdf
            ┌─────────────────▼─────────────────┐
            │  2. CONVERT                        │   free
            │  text layer → markdown             │
            │  OCR fallback on thin text,        │
            │  broken Arabic, or glyph soup      │
            │  graded in the same pass;          │
            │  grade F → quarantine              │
            └─────────────────┬─────────────────┘
                              │  corpus/markdown/*.md
            ┌─────────────────▼─────────────────┐
            │  3. BUILD                          │   paid (extraction)
            │  snapshot → extract → dedup →      │
            │  cluster → label → export vault    │
            │  promote only on success           │
            └─────────────────┬─────────────────┘
                              │  graphify-out/graph.json
            ┌─────────────────▼─────────────────┐
            │  4. ENRICH                         │
            │    ground()  verbatim excerpts +   │   free
            │              exact page locators + │
            │              derived caveats       │
            │    enrich()  node summaries,       │   paid
            │              community themes,     │
            │              selected narratives   │
            │    render()  write vault notes     │   free
            │    index()   routing index         │   free
            └─────────────────┬─────────────────┘
                              │  SAMA_Knowledge_Base_Obsidian/
            ┌─────────────────▼─────────────────┐
            │  5. AUDIT                          │   free
            │  read-only quality report          │
            └───────────────────────────────────┘
```

### 5.1 Stage detail

**Crawl.** A single headless-browser pass walks the Rulebook's sidebar tree,
recording structure, publication status and PDF links from each page in one
visit, then follows circular index pages to their detail pages. Only instruments
the regulator presents as **In-Force** are downloaded — the filter is applied at
acquisition, so superseded material never enters the corpus and there is no
retirement problem to solve later.

**Convert.** Each PDF's text layer is read in reading order. A document is routed
to 200 DPI OCR when any of three conditions holds:

- the text layer is too thin to be usable (< 400 characters per page);
- it contains **Arabic presentation-form glyphs**, which indicate the PDF stored
  rendered glyph shapes in visual order rather than readable text;
- it shows a high rate of isolated one- and two-letter Arabic fragments, the
  signature of broken bidirectional extraction.

The second condition is the one that matters most and is easiest to miss. A PDF
that stores Arabic as presentation forms can look perfectly healthy on every
conventional metric — normal page count, high character density, no replacement
characters — while being completely unsearchable. Detection covers both the
standard Arabic block (`U+0600–06FF`) **and** the presentation-form blocks
(`U+FB50–FDFF`, `U+FE70–FEFF`), in one shared implementation.

Text is stored in **logical order**, never display order. Reshaping and
bidirectional display transforms are deliberately absent: they are for rendering,
and writing their output to disk is what makes a corpus unsearchable. Where
presentation forms survive, they are normalised back to base letters and
reversed to reading order.

Every document is then graded in the same pass — page-count fidelity, text
coverage against the source, empty pages, Arabic risk, token retention, decode
garbage — and anything grading **F** is moved to `quarantine/` so it cannot
contribute nodes.

**Build.** The graph is snapshotted, extracted, and promoted only if extraction
produced a usable result. Nodes denoting the same entity extracted from different
source documents are then **merged on normalised label** — unioning their edges,
retaining every source, and dropping the self-loops and parallel edges that
merging creates. Without this step a law cited by ten circulars becomes ten
near-identical notes and a reader cannot tell which is authoritative. Merging
happens before clustering, so communities and the vault export both see one node
per entity.

**Enrich.** Split into a free tier and a paid tier.

*Free — deterministic.* For each relationship, the supporting sentence is
selected from the source document by keyword scoring and **sliced directly out of
the file**. It is therefore verbatim by construction and cannot drift from the
source. Because the slice's byte offset is known, its page number is derived
exactly rather than estimated. Caveats are computed from data already held —
relationship confidence, weak relation types, and the measured Arabic quality of
the cited source.

*Paid — synthesis.* The model produces what retrieval cannot: a short orientation
summary and lookup terms per concept, a theme and reading order per community,
and a decision-framing narrative for the subset of relationships that earn one —
those crossing regimes, those the reader should not take at face value, and those
on high-traffic hubs. Each concept's source context is sent **once**, not once per
relationship; the system prompt is cacheable; calls run concurrently with backoff
on transient errors; and every call is written to a token and cost ledger.

**Audit.** Read-only. Reports grounding integrity, broken-Arabic exposure measured
directly from the corpus, locator coverage, duplicate clusters, connectivity,
enrichment coverage and graph integrity — grading any dimension it cannot measure
as `N/A` and excluding it from the overall score.

---

## 6. Deliverables

| # | Deliverable | Description |
|---|---|---|
| 1 | Pipeline | Seven modules plus one entry point; five stages, independently runnable |
| 2 | Corpus | `corpus/markdown/` — searchable text, logical-order Arabic, per-document quality grade |
| 3 | Knowledge graph | `graphify-out/graph.json` — deduplicated concepts, typed and confidence-tagged relationships |
| 4 | Obsidian vault | Concept notes with summaries, sources, and grounded connections; community notes |
| 5 | Routing index | `_INDEX_Routing.md` — regime → concept → source document → page |
| 6 | Quality reports | Conversion quality, graph audit, dedup statistics, per-run snapshots |
| 7 | Cost ledger | Per-call token counts and estimated spend |
| 8 | Test suite | Regression tests for Arabic detection and repair, OCR routing, locators, dedup, audit honesty |
| 9 | Documentation | README, pipeline reference, runbook, agent specifications |

### 6.1 What a concept note contains

```markdown
# Customer Due Diligence (CDD)

Defines the identification and verification measures a financial institution must
apply before establishing a business relationship. Binds banks, finance companies
and payment service providers.

**Regimes:** AML/CTF, payments

## Sources
- `corpus/markdown/SAMA_EN_1704_VER1.md`
- `corpus/markdown/SAMA_EN_5565_VER1.md`

## Connections

### [[Beneficial Owner Verification]] — `imposes_obligation_on` [EXTRACTED]
- **What this link tells you:** When scoping onboarding obligations for a finance
  company, CDD and beneficial-owner identification cannot be treated as separate
  workstreams, because …
- **Grounding — this node** (SAMA_EN_1704_VER1 · Page 12): "…"
- **Grounding — related node** (SAMA_EN_10959_VER1 · Page 3): "…"
- **Caveat:** Source SAMA_EN_10959_VER1 contains broken Arabic — treat quotes
  from it as indicative only.

## Lookup terms
`cdd`, `due diligence`, `onboarding`, `identification`, `verification`
```

Every quotation is a literal slice of the cited file at the cited page.

---

## 7. Agent workflow integration

The vault is built to serve a structured question-answering workflow with
separated responsibilities:

```
Orchestrator → Legal/Compliance → Corpus Mapper ×N  (survey → coverage map)
                                → Corpus Extractor ×N (dig → evidence packs)
             → Completeness Reviewer ⇄ Legal
             → Output Formatter
```

The knowledge base serves the **Mapper** — the agent that decides where to look.
The routing index takes it from a question to a shortlist of source documents and
pages without reading the corpus first; concept notes tell it what each candidate
covers and how instruments relate.

The **Extractor** then quotes from `corpus/markdown/` directly. This is the
guardrail: the vault decides *where to look*, the corpus decides *what is true*.
Enrichment prose is never the authority for a legal proposition, and the agent
specifications state this explicitly.

---

## 8. Quality management

### 8.1 Measured dimensions

| Dimension | Measures |
|---|---|
| Grounding integrity | Stored excerpts still present verbatim in their cited source |
| Broken-Arabic exposure | Share of concepts resting on documents with unreadable Arabic |
| Locator coverage | Relationships carrying an exact page citation |
| Dedup cleanliness | Concepts not sitting in a duplicate-label cluster |
| Structure | Concepts with more than one relationship |
| Extraction coverage | High-grade documents adequately represented in the graph |
| Enrichment coverage | Concepts, communities and selected relationships enriched |

### 8.2 Honesty rules

- A dimension that cannot be measured grades **N/A**, is excluded from the
  average, and is called out at the top of the report. It never grades as a pass.
- Broken-Arabic exposure is measured from the corpus itself, so it is reported
  even before any grading has run.
- Documents that fail conversion are named in the report, not silently dropped.
- Where grounding finds a supporting sentence on only one side of a relationship,
  the note says so.

### 8.3 Acceptance criteria

| Criterion | Target |
|---|---|
| Grounding integrity | 100% (verbatim by construction) |
| Page locator coverage | 100% of grounded relationships |
| Broken-Arabic exposure | < 1% of concepts |
| Duplicate-label clusters | 0 after dedup |
| Quarantined documents | Named individually with a stated cause |
| Test suite | Passing, no network or API access required |

---

## 9. Technical approach

| Area | Choice | Rationale |
|---|---|---|
| Language | Python ≥ 3.9 | Ecosystem for PDF, OCR and browser automation |
| PDF | PyMuPDF | Reliable text-layer access and page rendering |
| OCR | Tesseract (`eng+ara`) | Bundled language data; no external service, no data egress |
| Acquisition | Playwright (Chromium) | The Rulebook's navigation is script-rendered |
| Graph | Graphify CLI | Extraction, clustering, labelling, Obsidian export |
| Model access | Anthropic API via stdlib HTTP | No SDK dependency; full control of caching, retry and cost logging |
| Arabic | Standard library `unicodedata` | Normalisation and repair without display-form libraries |
| Configuration | One module, environment-overridable | No path, threshold or model name is hardcoded anywhere else |
| Secrets | Environment / gitignored `.env` | Never in tracked source; never printed |

**Separation of model concerns.** Extraction and enrichment are configured with
independent models and independent API keys. Extraction is pinned to the model the
graph toolchain supports; enrichment calls the API directly and is free to use a
newer one. The two can bill to different accounts.

---

## 10. Cost model

Two stages consume tokens.

| Stage | Work | Driver |
|---|---|---|
| Build | Concept and relationship extraction across the corpus | One-time, scales with corpus size |
| Enrich (paid tier) | Concept summaries, community themes, selected narratives | Scales with graph size |

Controls:

- The free tier delivers a complete, fully grounded, fully cited vault at **zero
  token cost**. The paid tier is additive.
- Concept context is sent once per concept rather than once per relationship.
- The system prompt is marked cacheable.
- Relationship narratives are capped and selected, not universal.
- `--limit-nodes` and `--skip-model` allow rehearsal before committing spend.
- Every call is logged with token counts; the run prints a running total.

Cost figures in the ledger are estimates derived from a configurable price table
and should be reconciled against the provider console. Token counts are exact.

---

## 11. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Rulebook markup changes | Crawl breaks | Single crawl implementation; failure is loud, not silent |
| Arabic PDFs that defeat both text extraction and OCR | Instruments unusable | Detected, graded F, quarantined and named — never silently ingested |
| Extraction quality varies by document | Uneven graph coverage | Per-document coverage reported against corpus median |
| Model output drift | Inconsistent summaries | Model confined to synthesis; all citations are deterministic |
| Cost overrun | Budget | Free tier covers grounding; paid tier capped, resumable, metered |
| Partial run failure | Corrupt state | Stages independent; graph promoted only on success; enrichment resumable |
| Reliance on a repealed instrument | **Compliance risk** | In-force filter at acquisition; every claim cites a page a human can verify |
| Over-reliance on the knowledge base | **Compliance risk** | Corpus-wins rule enforced in agent specifications; unresolved gaps surfaced, not hidden |

---

## 12. Delivery plan

| Phase | Scope | Exit criteria |
|---|---|---|
| 1 — Foundation | Configuration, shared primitives, Arabic handling, test suite | Tests pass without network or API access |
| 2 — Acquisition | Crawl with in-force filtering | Manifest and PDFs on disk; report produced |
| 3 — Conversion | Text/OCR routing, grading, quarantine | Conversion quality report; quarantine list reviewed |
| 4 — Graph | Extract, dedup, cluster, export | Zero duplicate-label clusters; graph integrity clean |
| 5 — Grounding | Deterministic excerpts, locators, caveats, routing index | 100% verbatim; 100% locator coverage on grounded edges |
| 6 — Enrichment | Concept summaries, communities, selected narratives | Coverage reported; ledger reconciled |
| 7 — Validation | Audit; agent workflow smoke test | Audit grades reviewed; no dimension silently N/A |

Phases 1–5 produce a **complete and usable knowledge base at zero token cost for
enrichment**. Phase 6 is a discrete, separately-authorised spend.

---

## 13. Operating model

**Build once.** There is no incremental update path, by design. A refresh is a
full re-run, which keeps the pipeline small and removes an entire class of
partial-state bugs.

**Refresh cadence.** Recommended at least annually, and after any material SAMA
publication affecting our licensed activities. Because acquisition filters to
in-force instruments, a re-run also retires superseded material automatically.

**Resumability.** Stages are independent. Enrichment maintains an append-only
resume log, so an interrupted paid pass continues rather than repeating.

**Ownership.** Legal & Compliance owns the corpus and the agent specifications.
The pipeline is maintained as code, with configuration in one module and secrets
in the environment.

---

## 14. Success criteria

The project succeeds if:

1. Every in-force SAMA instrument in scope is present, searchable, and graded.
2. Every relationship in the knowledge base cites a verbatim quotation and an
   exact page in a named source document.
3. A regulatory question can be routed to the right instruments and pages without
   reading the corpus first.
4. The knowledge base reports its own limits — quarantined documents, one-sided
   grounding, unmeasured dimensions — rather than presenting uniform confidence.
5. Rebuilding is one command, and re-running any stage is safe.

The fourth is the one to hold the project to. A knowledge base that is 95%
complete and says so is usable for compliance work. One that is 95% complete and
presents as 100% is not.
