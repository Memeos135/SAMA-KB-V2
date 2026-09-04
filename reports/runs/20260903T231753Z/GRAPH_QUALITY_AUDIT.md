# Graph Quality Audit

> Generated: 2026-09-03T23:20:09+00:00
> Graph: 130 nodes, 126 edges
> Method: deterministic structural audit + verbatim drift check (no LLM)

## Overall grade: **B**

| Dimension | Grade | Value | Note |
|---|---|---|---|
| Grounding | A | 100.0% | stored excerpts still present verbatim in their source |
| Broken Arabic Exposure | A | 0.0% | share of nodes resting on presentation-form Arabic (lower is better) |
| Structure | C | 46.2% | nodes with degree >= 2 |
| Dedup | A | 100.0% | nodes not in a duplicate-label cluster |
| Locator Coverage | D | 56.3% | edges carrying an exact page locator |
| Extraction Coverage | C | 61.9% | A-grade documents adequately covered |

## Integrity (graphify diagnose multigraph)
- CLEAN — no dangling/missing/collapsed/self-loop edges

## Broken-Arabic exposure (measured from the corpus)

- Corpus documents with presentation-form Arabic >= 2%: **0** of 378
- Nodes resting on those documents: **0 / 130** (0.0%)

| Stem | Presentation-form share |
|---|---|
| `SAMA_EN_9451_VER1` | 1.4% |

## Grounding drift

- Stored excerpts: **143** (checkable: 143)
- Still verbatim in source: **143** → **100.0%**

_Excerpts are sliced directly from the corpus, so this should read 100%. Anything lower means a source file changed after grounding ran — re-run the ground stage._

## Locators

- Edges with an exact page locator: **71 / 126**
- Nodes carrying source_location from extraction: **0 / 130**

## Enrichment coverage

- Node summaries: **0 / 130**
- Community blurbs: **0**
- Edge narratives: **0** (selective by design — grounding covers every edge)

## Structure

- Isolated: **15** · degree-1: **55** (42%)
- Top hubs: Finance Companies Control Law (17), OTC Derivative Trade Repository Reporting Requirements (9), Counter-Fraud Fundamental Requirements (8), Risk Management Framework for Shari'ah Compliant Banking (7), Targeted Financial Sanctions Rules (7), Finance Companies Regulation (Articles 23-105) (6)

## Edges

- Confidence: EXTRACTED=112, INFERRED=14
- Relations: references=114, semantically_similar_to=7, conceptually_related_to=4, shares_data_with=1
- Orphans: 0 · self-loops: 0

## Duplicate-label clusters

- none (dedup ran)

## Per-document coverage

| Stem | Nodes | Pages | Nodes/pg | Grade | Flags |
|---|---|---|---|---|---|
| SAMA_EN_10593_VER1_0 | 16 | 57 | 0.281 | A | - |
| SAMA_EN_10530_VER1 | 10 | 21 | 0.476 | A | - |
| SAMA_EN_10577_VER1 | 9 | 15 | 0.6 | A | - |
| SAMA_EN_10667_VER1 | 7 | 23 | 0.304 | A | - |
| SAMA_EN_10592_VER1 | 6 | 57 | 0.105 | A | under_extracted |
| SAMA_EN_10950_VER1 | 5 | 10 | 0.5 | A | - |
| SAMA_EN_10621_VER1 | 4 | 4 | 1.0 | A | - |
| SAMA_EN_10681_VER1 | 4 | 10 | 0.4 | A | - |
| SAMA_EN_10698_VER1 | 4 | 38 | 0.105 | A | under_extracted |
| SAMA_EN_11009_VER1 | 3 | 13 | 0.231 | A | - |
| SAMA_EN_10928_VER1 | 3 | 10 | 0.3 | A | - |
| SAMA_EN_10951_VER1 | 3 | 7 | 0.429 | A | - |
| SAMA_EN_10959_VER1 | 3 | 1 | 3.0 | A | - |
| SAMA_EN_10831_VER1 | 2 | 38 | 0.053 | A | under_extracted |
| SAMA_EN_10575_VER1 | 2 | 7 | 0.286 | A | - |
| SAMA_EN_10910_VER1 | 2 | 1 | 2.0 | A | - |
| SAMA_EN_10911_VER1 | 2 | 17 | 0.118 | A | under_extracted |
| SAMA_EN_10968_VER1 | 2 | 1 | 2.0 | A | - |
| SAMA_EN_11008_VER1 | 2 | 9 | 0.222 | A | under_extracted |
| SAMA_EN_11011_VER1 | 2 | 22 | 0.091 | A | under_extracted |
| SAMA_EN_11015_VER1 | 2 | 9 | 0.222 | A | under_extracted |
| SAMA_EN_1023_VER1 | 1 | 12 | 0.083 | A | under_extracted |
| SAMA_EN_10335_VER1 | 1 | 15 | 0.067 | A | under_extracted |
| SAMA_EN_10356_VER1 | 1 | 15 | 0.067 | A | under_extracted |
| SAMA_EN_10400_VER1 | 1 | 12 | 0.083 | A | under_extracted |
| SAMA_EN_10417_VER1 | 1 | 12 | 0.083 | A | under_extracted |
| SAMA_EN_10465_VER1 | 1 | 18 | 0.056 | A | under_extracted |
| SAMA_EN_10528_VER | 1 | 18 | 0.056 | A | under_extracted |
| SAMA_EN_10529_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10419_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10426_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10427_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10245_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10320_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10322_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10227_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10394_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA circular No (GDBC-341000107020-1434H)EN | 1 | 2 | 0.5 | A | - |
| SAMA CIRCULAR NO (GDBC-361000009335-1436H) | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10559_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10623_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10640_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10646_VER1 | 1 | 7 | 0.143 | A | under_extracted |
| SAMA_EN_10647_VER1 | 1 | 7 | 0.143 | A | under_extracted |
| SAMA_EN_10668_VER1 | 1 | 23 | 0.043 | A | under_extracted |
| SAMA_EN_10697_VER1 | 1 | 10 | 0.1 | A | under_extracted |
| SAMA_EN_10721_VER1 | 1 | 10 | 0.1 | A | under_extracted |
| SAMA_EN_10865_VER1 | 1 | 10 | 0.1 | A | under_extracted |
| SAMA_EN_10832_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10866_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10888_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10908_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10912_VER1 | 1 | 17 | 0.059 | A | under_extracted |
| SAMA_EN_10941_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10949_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10964_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10967_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10969_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10971_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10973_VER1 | 1 | 19 | 0.053 | B | - |
| SAMA_EN_11005_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_11010_VER1 | 1 | 9 | 0.111 | A | under_extracted |
| SAMA_EN_11012_VER1 | 1 | 14 | 0.071 | A | under_extracted |
| SAMA_EN_11017_VER1 | 1 | 9 | 0.111 | A | under_extracted |

## Prioritized fixes

1. **55 degree-1 nodes** — consider a deeper extraction pass.
