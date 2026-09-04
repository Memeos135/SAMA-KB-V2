# Hypothetical P&L (HPL)

Concept node for the hypothetical P&L used in backtesting and the PLA test, measuring the change in end-of-day portfolio value holding positions unchanged, excluding intraday trading and new or modified deals (unlike actual P&L). The rules bind banks on what must be excluded (fees and commissions, CVA and DVA-type adjustments capitalised elsewhere), which valuation adjustments must be included, the ban on smoothing non-daily adjustments, and the treatment of adjustments not computable at desk level, with SAMA agreement or support required in specified cases.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[Backtesting]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 109): "Backtesting requirements 12.4 Backtesting requirements compare the value-at-risk (VaR) measure calibrated to a one-day holding period against each of the actual P&L (APL) and hypothetical P&L (HPL) over the prior 12 months."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 465): "Backtesting requirements 12.4 Backtesting requirements compare the value-at-risk (VaR) measure calibrated to a one-day holding period against each of the actual P&L (APL) and hypothetical P&L (HPL) over the prior 12 months."

### [[P&L Attribution (PLA) Test]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 116): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 474): "(1) If a trading desk is in the PLA test amber zone, it cannot return to the PLA test green zone until: (a) the trading desk produces outcomes in the PLA test green zone; and (b) the trading desk has satisfied its backtesting exceptions requirements over the prior 12 months."

### [[Risk-Theoretical P&L (RTPL)]] — `conceptually_related_to` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 5): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 5): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Caveat:** Relation is a similarity heuristic, not a cross-reference.

### [[Spearman Correlation Metric]] — `shares_data_with` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 116): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 116): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."

## Lookup terms

`hypothetical P&L`, `HPL`, `actual P&L APL`, `backtesting trading desk`, `valuation adjustments exclusion`, `CVA DVA exclusion from P&L`, `market data snapshot time alignment`

#graphify/enriched #community/internal-models-approach
