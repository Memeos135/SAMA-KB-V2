# Credit Valuation Adjustment (CVA)

Concept node for Credit Valuation Adjustment (CVA) as used in SAMA's minimum capital requirements for counterparty credit risk, covering the CVA framework chapter and its treatment in Pillar 3 RWA disclosure rows. CVA is the counterparty-level adjustment to default-risk-free prices of derivatives and securities financing transactions for potential counterparty default; the framework distinguishes regulatory CVA from accounting CVA and converts CVA capital requirements into RWA via the 12.5 multiplier. Binds banks subject to SAMA's Basel-aligned capital and disclosure rules.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[Counterparty Credit Risk (CCR)]] — `conceptually_related_to` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 560): "Credit valuation adjustment A credit valuation adjustment that reflects the market value of the credit risk of the counterparty to the firm, but does not reflect the market value of the credit risk of the bank to the counterparty."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Caveat:** Relation is a similarity heuristic, not a cross-reference.

### [[Internal Risk Transfer]] — `references` [EXTRACTED]
- **What this link tells you:** If the bank hedges CVA risk through an internal desk rather than directly in the market, this link determines whether that hedge is recognised for capital purposes: recognition in the CVA capital calculation depends on satisfying the internal risk transfer conditions set out in the market risk framework, including how the internal transfer is externalised. The two instruments form an obligation chain — the CVA rules define the hedging benefit, the internal risk transfer rules define when an intra-bank transaction can carry that benefit. Practically, a CVA desk relying on internal hedges must evidence compliance with the internal risk transfer requirements or forgo the capital relief and accept the resulting SA-CVA or BA-CVA outcome.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 852): "a b SA-CVA RWA Number of counterparties 1 Interest rate risk 2 Foreign exchange risk 3 Reference credit spread risk 4 Equity risk 5 Commodity risk 6 Counterparty credit spread risk 7 Total (sum of rows 1 to 6) Linkages across templates [CVA3:7/a] is equal to [OV1:10/a] if the ban"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 381): "Alternatively, the internal risk transfer desk may obtain the external hedge from the market via a separate non-internal risk transfer trading desk acting as an agent, if and only if the GIRR internal risk transfer entered into with the non-internal risk transfer trading desk exa"

### [[Look-Through Approach (LTA)]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank is settling which capital approach applies to a given exposure, this link is a reminder that the CVA risk provisions and the look-through approach for fund exposures sit inside the same consolidated SAMA capital framework and use a common vocabulary of 'standardised' versus alternative approaches, but they govern different risk types. Selecting the standardised or basic approach for CVA risk carries no implication for whether look-through is available for equity investments in funds; each approach-choice condition must be met on its own terms. Because the extracted text on the fund side reads as a contents-level listing, the reader should verify in the primary text whether the cross-reference is substantive or merely navigational before relying on it.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 755): "Credit valuation adjustment (row 3): Definition of standardised approach: The standardised approach for CVA (SA-CVA), the basic approach (BA-CVA) or 100% of a bank’s counterparty credit risk capital requirements (depending on which approach the bank uses for CVA risk)."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 13): "Equity investments in funds 325 The look-through approach 325 The mandate-based approach 326 The fall-back approach 328 Treatment of funds that invest in other funds 328 Partial use of an approach 328 Leverage adjustment 329 Application of the LTA and MBA to banks using the IRB a"

### [[Mandate-Based Approach (MBA)]] — `references` [EXTRACTED]
- **What this link tells you:** For an approach-selection or disclosure decision, treat this as a same-rulebook linkage rather than a substantive dependency: the mandate-based approach is the fallback tier for fund exposures where full look-through is unavailable, while the CVA provisions govern counterparty credit spread risk capital. The shared framework means consistent definitions and consistent Pillar 3 presentation, not interchangeable eligibility. Because the fund-side excerpt appears to be a contents listing, confirm in the primary text whether an operative cross-reference exists before treating one approach determination as informing the other.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 755): "Credit valuation adjustment (row 3): Definition of standardised approach: The standardised approach for CVA (SA-CVA), the basic approach (BA-CVA) or 100% of a bank’s counterparty credit risk capital requirements (depending on which approach the bank uses for CVA risk)."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 13): "Equity investments in funds 325 The look-through approach 325 The mandate-based approach 326 The fall-back approach 328 Treatment of funds that invest in other funds 328 Partial use of an approach 328 Leverage adjustment 329 Application of the LTA and MBA to banks using the IRB a"

### [[Minimum Capital Requirements for CCR and CVA]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 638): "However, all banks using the BA-CVA must calculate the reduced version of BA-CVA capital Version Minimum Capital Requirements for Counterparty Credit Risk (CCR) and 89 of 145 Issue Date December 2022 Page Number Credit Valuation Adjustment (CVA) 1.1"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 89): "However, all banks using the BA-CVA must calculate the reduced version of BA-CVA capital Version Minimum Capital Requirements for Counterparty Credit Risk (CCR) and 89 of 145 Issue Date December 2022 Page Number Credit Valuation Adjustment (CVA) 1.1"

## Lookup terms

`Credit Valuation Adjustment`, `CVA risk capital charge`, `regulatory CVA vs accounting CVA`, `counterparty credit risk (CCR)`, `securities financing transactions`, `RWA 12.5 multiplier`, `Pillar 3 CVA disclosure`

#graphify/enriched #community/basel-capital-requirements
