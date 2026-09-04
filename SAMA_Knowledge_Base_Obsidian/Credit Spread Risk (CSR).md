# Credit Spread Risk (CSR)

Concept node for credit spread risk as a market risk class, split into non-securitisation, securitisation non-CTP and securitisation CTP, and further split in the CVA framework into counterparty credit spread risk and reference credit spread risk. It drives bucketing, risk weights, correlation parameters and the assignment of eligible hedges, including the rule that a credit spread delta hedge must sit wholly in one risk class. It binds banks computing standardised market risk and SA-CVA capital requirements.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[CS01 Sensitivity]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 5): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Correlation Trading Portfolio (CTP)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Sensitivities-Based Method]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 385): "Instruments subject to each component of the sensitivities-based method 7.2 In applying the sensitivities-based method, all instruments held in trading desks as set out in [4] and subject to the sensitivities-based method (ie excluding instruments where the value at any point in "

## Lookup terms

`credit spread risk`, `CSR non-securitisation`, `CSR securitisation`, `counterparty credit spread risk`, `reference credit spread risk`, `SA-CVA`, `eligible hedge`, `delta risk class`

#graphify/enriched #community/market-risk-capital-methods
