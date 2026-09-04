# Curvature Risk

Concept node for Curvature risk, the sensitivities-based method component capturing the incremental non-linear price risk of options not captured by delta, measured through upward and downward stress shocks to each regulatory risk factor. It specifies how curvature risk weights are derived (for GIRR, CSR and commodity, a parallel shift based on the most punitive delta risk weight) and how curvature correlations are obtained by squaring delta correlations, with special treatment for CSR non-securitisations and securitisations (CTP). Binds banks calculating market risk capital under SAMA's mandated standardised approach.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[Equity Risk Buckets and Correlations]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Sensitivities-Based Method]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 385): "Instruments subject to each component of the sensitivities-based method 7.2 In applying the sensitivities-based method, all instruments held in trading desks as set out in [4] and subject to the sensitivities-based method (ie excluding instruments where the value at any point in "

### [[Vega Risk]] — `references` [INFERRED]
- **What this link tells you:** For any decision on market risk capital under the sensitivities-based method, curvature and vega cannot be treated as substitutes: instruments with optionality generate both a vega charge and a curvature charge, computed per risk class and then aggregated. Both provisions sit within the same market risk framework and share the defined risk-class list, which drives the buckets and correlations used in each calculation. The reader should therefore ensure optional exposures are captured in both components and, given this link is inferred, confirm the aggregation mechanics in the primary text.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

## Lookup terms

`curvature risk`, `CVR`, `upward and downward shock scenarios`, `curvature risk weight`, `parallel shift`, `squared delta correlations`, `correlation trading portfolio`, `sensitivities-based method`

#graphify/enriched #community/market-risk-capital-methods
