# Vega Risk

Concept node for Vega risk, the optionality-volatility component of the sensitivities-based method in SAMA's standardised market risk framework. It applies to instruments whose cash flows cannot be expressed as a linear function of notional (i.e. instruments with optionality), which are subject to both vega and curvature capital requirements; non-optional instruments such as coupon bonds are outside vega and curvature scope, subject to a limited elective inclusion for curvature. Binds banks computing market risk capital under the mandated standardised approach.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[Curvature Risk]] — `references` [INFERRED]
- **What this link tells you:** For any decision on market risk capital under the sensitivities-based method, curvature and vega cannot be treated as substitutes: instruments with optionality generate both a vega charge and a curvature charge, computed per risk class and then aggregated. Both provisions sit within the same market risk framework and share the defined risk-class list, which drives the buckets and correlations used in each calculation. The reader should therefore ensure optional exposures are captured in both components and, given this link is inferred, confirm the aggregation mechanics in the primary text.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

### [[Sensitivities-Based Method]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 385): "Instruments subject to each component of the sensitivities-based method 7.2 In applying the sensitivities-based method, all instruments held in trading desks as set out in [4] and subject to the sensitivities-based method (ie excluding instruments where the value at any point in "

## Lookup terms

`vega risk`, `implied volatility risk factor`, `optionality`, `non-linear instruments`, `prepayment options`, `sensitivities-based method`, `vega capital requirement`

#graphify/enriched #community/market-risk-capital-methods
