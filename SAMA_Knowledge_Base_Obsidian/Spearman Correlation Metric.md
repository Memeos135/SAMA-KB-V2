# Spearman Correlation Metric

A concept node describing the Spearman rank correlation metric, one of the two profit-and-loss attribution test metrics used to assess how closely a trading desk's risk-theoretical P&L tracks its hypothetical P&L. It specifies ranking both 250-day time series by size and computing the rank correlation, and prohibits aligning HPL inputs to RTPL or adjusting either series for operational noise. It applies to banks running trading desks under the internal models approach.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[Hypothetical P&L (HPL)]] — `shares_data_with` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 116): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 116): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."

### [[P&L Attribution (PLA) Test]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 116): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 472): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."

### [[Risk-Theoretical P&L (RTPL)]] — `shares_data_with` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 116): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 5): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

## Lookup terms

`Spearman correlation metric`, `PLA test`, `profit and loss attribution`, `RTPL`, `HPL`, `250 trading days`, `rank correlation`, `trading desk eligibility`

#graphify/enriched #community/internal-models-approach
