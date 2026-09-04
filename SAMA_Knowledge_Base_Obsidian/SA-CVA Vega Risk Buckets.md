# SA-CVA Vega Risk Buckets

Governs the vega risk component of the standardized approach to CVA capital (SA-CVA), computed as the simple sum of independently calculated vega requirements across five risk classes (interest rate, FX, reference credit spread, equity, commodity), with no vega charge for counterparty credit spread risk. It requires vega sensitivities to be calculated in all cases regardless of whether the portfolio contains options, applying volatility shifts to both path-generation and option-pricing volatilities, and addresses index hedge sensitivities and the SA-CVA multiplier that SAMA may raise for model risk. It binds banks approved by SAMA to use SA-CVA.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[Standardized Approach for CVA (SA-CVA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 96): "The primary differences of the SA-CVA from the standardized approach for market risk are: (1) The SA-CVA features a reduced granularity of market risk factors; and (2) The SA-CVA does not include default risk and curvature risk."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 849): "23.2.1 CVA risk under the basic approach (BA-CVA): Template CVA1: The reduced basic approach for CVA (BA-CVA) Purpose: To provide the components used for the computation of RWA under the reduced BA-CVA for CVA risk."

## Lookup terms

`SA-CVA vega risk`, `vega risk classes`, `CVA sensitivities`, `delta risk classes`, `mCVA multiplier`, `reference credit spread risk`, `volatility shift`, `index hedge sensitivity`

#graphify/enriched #community/cva-&-counterparty-exposure
