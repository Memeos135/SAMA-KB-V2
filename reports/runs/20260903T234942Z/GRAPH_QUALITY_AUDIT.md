# Graph Quality Audit

> Generated: 2026-09-03T23:47:37+00:00
> Graph: 1495 nodes, 1618 edges
> Method: deterministic structural audit + verbatim drift check (no LLM)

## Overall grade: **B**

> 1 dimension(s) scored **N/A** and are excluded from the average. An N/A is a missing measurement, not a pass.

| Dimension | Grade | Value | Note |
|---|---|---|---|
| Grounding | N/A | - | stored excerpts still present verbatim in their source |
| Broken Arabic Exposure | A | 0.0% | share of nodes resting on presentation-form Arabic (lower is better) |
| Structure | C | 52.0% | nodes with degree >= 2 |
| Dedup | A | 100.0% | nodes not in a duplicate-label cluster |
| Locator Coverage | D | 0.0% | edges carrying an exact page locator |
| Extraction Coverage | B | 76.0% | A-grade documents adequately covered |

## Integrity (graphify diagnose multigraph)
- CLEAN — no dangling/missing/collapsed/self-loop edges

## Broken-Arabic exposure (measured from the corpus)

- Corpus documents with presentation-form Arabic >= 2%: **0** of 378
- Nodes resting on those documents: **0 / 1495** (0.0%)

| Stem | Presentation-form share |
|---|---|
| `SAMA_EN_9451_VER1` | 1.4% |

## Grounding drift

- Stored excerpts: **0** (checkable: 0)
- rate: n/a

_Excerpts are sliced directly from the corpus, so this should read 100%. Anything lower means a source file changed after grounding ran — re-run the ground stage._

## Locators

- Edges with an exact page locator: **0 / 1618**
- Nodes carrying source_location from extraction: **0 / 1495**

## Enrichment coverage

- Node summaries: **0 / 1495**
- Community blurbs: **0**
- Edge narratives: **0** (selective by design — grounding covers every edge)

## Structure

- Isolated: **182** · degree-1: **535** (36%)
- Top hubs: Finance Companies Control Law (40), Banking Control Law (22), Anti-Money Laundering Law (17), Minimum Capital Requirements for Credit Risk (15), SAMA Payment Services Regulation 1430 (14), Exposure at Default (EAD) (14)

## Edges

- Confidence: INFERRED=152, EXTRACTED=1461, AMBIGUOUS=5
- Relations: references=1341, conceptually_related_to=147, cites=101, semantically_similar_to=17, shares_data_with=11, implements=1
- Orphans: 0 · self-loops: 0

## Duplicate-label clusters

- none (dedup ran)

## Per-document coverage

| Stem | Nodes | Pages | Nodes/pg | Grade | Flags |
|---|---|---|---|---|---|
| SAMA_EN_3487_VER1 | 300 | 902 | 0.333 | A | - |
| SAMA_EN_3502_VER1 | 140 | 349 | 0.401 | A | - |
| SAMA_EN_4234_VER1 | 92 | 168 | 0.548 | A | - |
| SAMA_EN_3553_VER1 | 62 | 175 | 0.354 | A | - |
| SAMA_EN_3575_VER1 | 35 | 92 | 0.38 | A | - |
| SAMA_EN_4283_VER1 | 35 | 145 | 0.241 | A | under_extracted |
| SAMA_EN_5888_VER1 | 31 | 56 | 0.554 | A | - |
| SAMA_EN_1644_VER1 | 30 | 113 | 0.265 | A | - |
| SAMA_EN_1704_VER1 | 23 | 70 | 0.329 | A | - |
| SAMA_EN_4066_VER1 | 22 | 42 | 0.524 | A | - |
| SAMA_EN_2217_VER1 | 20 | 69 | 0.29 | A | - |
| SAMA_EN_9492_VER1 | 18 | 52 | 0.346 | A | - |
| SAMA_EN_2340_VER1 | 17 | 42 | 0.405 | A | - |
| SAMA_EN_4226_VER1 | 16 | 42 | 0.381 | A | - |
| SAMA_EN_8383_VER1 | 15 | 60 | 0.25 | A | - |
| SAMA_EN_2788_VER1 | 15 | 41 | 0.366 | A | - |
| SAMA_EN_6073_VER1 | 15 | 76 | 0.197 | A | under_extracted |
| SAMA_EN_10593_VER1_0 | 14 | 57 | 0.246 | A | under_extracted |
| SAMA_EN_9451_VER1 | 14 | 23 | 0.609 | A | - |
| SAMA_EN_10530_VER1 | 12 | 21 | 0.571 | A | - |
| SAMA_EN_1734_VER1 | 12 | 22 | 0.545 | A | - |
| SAMA_EN_1430_VER1 | 12 | 74 | 0.162 | A | under_extracted |
| SAMA_EN_2898_VER1 | 12 | 28 | 0.429 | A | - |
| SAMA_EN_3837_VER1 | 12 | 56 | 0.214 | A | under_extracted |
| SAMA_EN_10577_VER1 | 11 | 15 | 0.733 | A | - |
| SAMA_EN_9068_VER1 | 11 | 18 | 0.611 | A | - |
| SAMA_EN_11054_VER1 | 10 | 16 | 0.625 | A | - |
| SAMA_EN_2675_VER1_0 | 10 | 22 | 0.455 | A | - |
| SAMA_EN_3081_VER1 | 10 | 23 | 0.435 | A | - |
| SAMA_EN_11051_VER1 | 10 | 42 | 0.238 | A | under_extracted |
| SAMA_EN_3709_VER1 | 10 | 16 | 0.625 | A | - |
| SAMA_EN_4878_VER1 | 9 | 27 | 0.333 | A | - |
| SAMA_EN_11055_VER1 | 9 | 25 | 0.36 | A | - |
| SAMA_EN_4041_VER1 | 9 | 18 | 0.5 | A | - |
| SAMA_EN_11044_VER1 | 8 | 16 | 0.5 | A | - |
| SAMA_EN_10592_VER1 | 8 | 57 | 0.14 | A | under_extracted |
| SAMA_EN_10667_VER1 | 8 | 23 | 0.348 | A | - |
| SAMA_EN_1717_VER1 | 8 | 27 | 0.296 | A | - |
| SAMA_EN_4736_VER1 | 8 | 22 | 0.364 | A | - |
| SAMA_EN_3526_VER1 | 8 | 22 | 0.364 | A | - |
| SAMA_EN_3726_VER1 | 8 | 13 | 0.615 | A | - |
| SAMA_EN_8357_VER1 | 7 | 25 | 0.28 | A | - |
| SAMA_EN_10950_VER1 | 7 | 10 | 0.7 | A | - |
| SAMA_EN_11021_VER1 | 7 | 20 | 0.35 | A | - |
| SAMA_EN_2926_VER1 | 7 | 18 | 0.389 | A | - |
| SAMA_EN_11038_VER1 | 7 | 23 | 0.304 | A | - |
| SAMA_EN_2274_VER1 | 7 | 16 | 0.438 | A | - |
| SAMA_EN_5491_VER1 | 7 | 35 | 0.2 | A | under_extracted |
| SAMA_EN_1822_VER1 | 7 | 21 | 0.333 | A | - |
| SAMA_EN_2757_VER1 | 7 | 19 | 0.368 | A | - |
| SAMA_EN_4303_VER1 | 7 | 32 | 0.219 | A | under_extracted |
| SAMA_EN_7136_VER1 | 7 | 22 | 0.318 | A | - |
| SAMA_EN_10621_VER1 | 6 | 4 | 1.5 | A | - |
| SAMA_EN_2389_VER1 | 6 | 19 | 0.316 | A | - |
| SAMA_EN_7908_VER1 | 6 | 16 | 0.375 | A | - |
| SAMA_EN_2888_VER1 | 6 | 8 | 0.75 | A | - |
| SAMA_EN_2948_VER1 | 6 | 11 | 0.545 | A | - |
| SAMA_EN_3467_VER1 | 6 | 21 | 0.286 | A | - |
| SAMA_EN_3689_VER1 | 5 | 10 | 0.5 | A | - |
| SAMA_EN_9381_VER1 | 5 | 4 | 1.25 | A | - |
| SAMA_EN_10698_VER1 | 5 | 38 | 0.132 | A | under_extracted |
| SAMA_EN_791_VER1 | 5 | 14 | 0.357 | A | - |
| SAMA_EN_853_VER1 | 5 | 20 | 0.25 | A | - |
| SAMA_EN_1989_VER1 | 5 | 16 | 0.312 | A | - |
| SAMA_EN_11045_VER1 | 5 | 10 | 0.5 | A | - |
| SAMA_EN_5565_VER1 | 5 | 42 | 0.119 | A | under_extracted |
| SAMA_EN_190_VER1 | 5 | 13 | 0.385 | A | - |
| SAMA_EN_3032_VER1 | 5 | 12 | 0.417 | A | - |
| SAMA_EN_3366_VER1 | 5 | 11 | 0.455 | A | - |
| SAMA_EN_2081_VER1 | 5 | 22 | 0.227 | A | under_extracted |
| SAMA_EN_1949_VER1 | 4 | 12 | 0.333 | A | - |
| SAMA_EN_5765_VER1 | 4 | 4 | 1.0 | A | - |
| SAMA_EN_11043_VER1 | 4 | 12 | 0.333 | A | - |
| SAMA_EN_10681_VER1 | 4 | 10 | 0.4 | A | - |
| SAMA_EN_11026_VER1 | 4 | 16 | 0.25 | A | - |
| SAMA_EN_8359_VER1 | 4 | 16 | 0.25 | A | - |
| SAMA_EN_3144_VER1 | 4 | 27 | 0.148 | A | under_extracted |
| SAMA_EN_1611_VER1 | 4 | 21 | 0.19 | A | under_extracted |
| SAMA_EN_1715_VER1 | 4 | 9 | 0.444 | A | - |
| SAMA_EN_1868_VER1 | 4 | 10 | 0.4 | A | - |
| SAMA_EN_2659_VER1 | 4 | 15 | 0.267 | A | - |
| SAMA_EN_2864_VER1 | 4 | 10 | 0.4 | A | - |
| SAMA_EN_3372_VER1 | 4 | 20 | 0.2 | A | under_extracted |
| SAMA_EN_3468_VER1 | 4 | 7 | 0.571 | A | - |
| SAMA_EN_4376_VER1 | 4 | 8 | 0.5 | A | - |
| SAMA_EN_6314_VER1 | 4 | 7 | 0.571 | A | - |
| SAMA_EN_8320_VER1_0 | 4 | 13 | 0.308 | A | - |
| SAMA_EN_1272_VER1 | 3 | 6 | 0.5 | A | - |
| SAMA_EN_2327_VER1 | 3 | 4 | 0.75 | A | - |
| SAMA_EN_2348_VER1 | 3 | 4 | 0.75 | A | - |
| SAMA_EN_10928_VER1 | 3 | 10 | 0.3 | A | - |
| SAMA_EN_1897_VER1 | 3 | 6 | 0.5 | A | - |
| SAMA_EN_1948_VER1 | 3 | 12 | 0.25 | A | - |
| SAMA_EN_3276_VER1 | 3 | 16 | 0.188 | A | under_extracted |
| SAMA_EN_353_VER1 | 3 | 24 | 0.125 | A | under_extracted |
| SAMA_EN_5547_VER1 | 3 | 16 | 0.188 | A | under_extracted |
| SAMA_EN_5840_VER1 | 3 | 32 | 0.094 | D | bad_source |
| SAMA_EN_10831_VER1 | 2 | 38 | 0.053 | A | under_extracted |
| SAMA_EN_8684_VER1 | 2 | 2 | 1.0 | A | - |
| SAMA_EN_10575_VER1 | 2 | 7 | 0.286 | A | - |
| SAMA_EN_10647_VER1 | 2 | 7 | 0.286 | A | - |
| SAMA_EN_10832_VER1 | 2 | 1 | 2.0 | A | - |
| SAMA_EN_10866_VER1 | 2 | 2 | 1.0 | A | - |
| SAMA_EN_10910_VER1 | 2 | 1 | 2.0 | A | - |
| SAMA_EN_10911_VER1 | 2 | 17 | 0.118 | A | under_extracted |
| SAMA_EN_10959_VER1 | 2 | 1 | 2.0 | A | - |
| SAMA_EN_11011_VER1 | 2 | 22 | 0.091 | A | under_extracted |
| SAMA_EN_11012_VER1 | 2 | 14 | 0.143 | A | under_extracted |
| SAMA_EN_11056_VER1 | 2 | 6 | 0.333 | A | - |
| SAMA_EN_11065_VER1 | 2 | 5 | 0.4 | A | - |
| SAMA_EN_11067_VER1 | 2 | 9 | 0.222 | A | under_extracted |
| SAMA_EN_11078_VER1 | 2 | 17 | 0.118 | A | under_extracted |
| SAMA_EN_11079_VER1_1 | 2 | 7 | 0.286 | A | - |
| SAMA_EN_11081_VER1 | 2 | 60 | 0.033 | A | under_extracted |
| SAMA_EN_11104_VER1 | 2 | 1 | 2.0 | A | - |
| SAMA_EN_1195_VER1 | 2 | 18 | 0.111 | A | under_extracted |
| SAMA_EN_123_VER1 | 2 | 10 | 0.2 | A | under_extracted |
| SAMA_EN_5885_VER1 | 2 | 51 | 0.039 | A | under_extracted |
| SAMA_EN_1293_VER1 | 2 | 10 | 0.2 | A | under_extracted |
| SAMA_EN_132_VER1_0 | 2 | 13 | 0.154 | A | under_extracted |
| SAMA_EN_1428_VER1 | 2 | 23 | 0.087 | A | under_extracted |
| SAMA_EN_1429_VER1 | 2 | 7 | 0.286 | A | - |
| SAMA_EN_5838_VER1 | 2 | 6 | 0.333 | A | - |
| SAMA_EN_2126_VER1 | 2 | 2 | 1.0 | A | - |
| SAMA_EN_3343_VER1 | 2 | 6 | 0.333 | A | - |
| SAMA_EN_5085_VER1 | 2 | 13 | 0.154 | A | under_extracted |
| SAMA_EN_4778_VER1 | 2 | 10 | 0.2 | A | under_extracted |
| SAMA_EN_5410_VER1 | 2 | 1 | 2.0 | A | - |
| SAMA_EN_5419_VER1 | 2 | 17 | 0.118 | A | under_extracted |
| SAMA_EN_5475_VER1_1 | 2 | 1 | 2.0 | A | - |
| SAMA_EN_5544_VER1 | 2 | 4 | 0.5 | A | - |
| SAMA_EN_5594_VER1 | 2 | 24 | 0.083 | A | under_extracted |
| SAMA_EN_6306_VER1 | 2 | 5 | 0.4 | A | - |
| SAMA_EN_6398_VER1 | 2 | 4 | 0.5 | A | - |
| SAMA_EN_6738_VER1 | 2 | 1 | 2.0 | A | - |
| إصدار وتحديث وتجديد معرّف الكيانات القانونية من خلال مؤسسة مالية | 2 | 5 | 0.4 | A | - |
| SAMA_EN_8984_VER1 | 2 | 12 | 0.167 | A | under_extracted |
| SAMA_EN_9618_VER1 | 2 | 11 | 0.182 | A | under_extracted |
| SAMA_RD%20637_en | 2 | 1 | 2.0 | A | - |
| GDBC-381000095091-1438H | 1 | 1 | 1.0 | A | - |
| Report on Total Remunerations for the Board of Directors and Committees | 1 | 1 | 1.0 | A | - |
| SAMA CIRCULAR NO (GDBC-361000009335-1436H) | 1 | 1 | 1.0 | A | - |
| SAMA circular No (GDBC-341000107020-1434H)EN | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10175_VER1 | 1 | 3 | 0.333 | A | - |
| SAMA_EN_10211_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10212_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10220_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10227_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_1023_VER1 | 1 | 12 | 0.083 | A | under_extracted |
| SAMA_EN_10241_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10244_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10245_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10319_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10320_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10322_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10335_VER1 | 1 | 15 | 0.067 | A | under_extracted |
| SAMA_EN_10356_VER1 | 1 | 15 | 0.067 | A | under_extracted |
| SAMA_EN_10372_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10394_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10395_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10397_VER | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10398_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10399_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10400_VER1 | 1 | 12 | 0.083 | A | under_extracted |
| SAMA_EN_10417_VER1 | 1 | 12 | 0.083 | A | under_extracted |
| SAMA_EN_10419_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10426_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10427_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10464_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10465_VER1 | 1 | 18 | 0.056 | A | under_extracted |
| SAMA_EN_10528_VER | 1 | 18 | 0.056 | A | under_extracted |
| SAMA_EN_10529_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10555_VER | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10556_VER | 1 | 3 | 0.333 | A | - |
| SAMA_EN_10559_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10560_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10590_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10623_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10640_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10646_VER1 | 1 | 7 | 0.143 | A | under_extracted |
| SAMA_EN_10668_VER1 | 1 | 23 | 0.043 | A | under_extracted |
| SAMA_EN_10697_VER1 | 1 | 10 | 0.1 | A | under_extracted |
| SAMA_EN_10721_VER1 | 1 | 10 | 0.1 | A | under_extracted |
| SAMA_EN_10865_VER1 | 1 | 10 | 0.1 | A | under_extracted |
| SAMA_EN_10888_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10908_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10912_VER1 | 1 | 17 | 0.059 | A | under_extracted |
| SAMA_EN_10941_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10949_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10951_VER1 | 1 | 7 | 0.143 | A | under_extracted |
| SAMA_EN_10964_VER1 | 1 | 2 | 0.5 | A | - |
| SAMA_EN_10967_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10968_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10969_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10971_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_10973_VER1 | 1 | 19 | 0.053 | B | - |
| SAMA_EN_11005_VER1 | 1 | 1 | 1.0 | A | - |
| SAMA_EN_11008_VER1 | 1 | 9 | 0.111 | A | under_extracted |
| SAMA_EN_11009_VER1 | 1 | 13 | 0.077 | A | under_extracted |
| SAMA_EN_11010_VER1 | 1 | 9 | 0.111 | A | under_extracted |

## Prioritized fixes

1. **535 degree-1 nodes** — consider a deeper extraction pass.
