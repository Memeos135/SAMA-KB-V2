# P&L Attribution (PLA) Test

Node on the profit and loss attribution test, the second gateway (alongside backtesting) determining whether a trading desk remains eligible for the internal models approach. It requires the PLA programme to start when the internal models capital requirement takes effect, a one-year backtesting and PLA report to support SAMA model approval, and quarterly reassessment of desk eligibility, with amber-zone desks attracting a capital surcharge and failing desks reverting to standardised treatment. Binds banks seeking or holding SAMA internal model approval for market risk.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[Aggregation of Capital Requirement]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 474): "(1) If a trading desk is in the PLA test amber zone, it cannot return to the PLA test green zone until: (a) the trading desk produces outcomes in the PLA test green zone; and (b) the trading desk has satisfied its backtesting exceptions requirements over the prior 12 months."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 779): "capital conservation buffer, G-SIB surcharge and countercyclical capital buffer) and Pillar 2 capital requirements (if CET1 capital is required); (ii) CET1 capital that banks must maintain to meet the minimum regulatory capital ratios and any CET1 capital used to meet Tier 1 capi"

### [[Backtesting]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 474): "(1) If a trading desk is in the PLA test amber zone, it cannot return to the PLA test green zone until: (a) the trading desk produces outcomes in the PLA test green zone; and (b) the trading desk has satisfied its backtesting exceptions requirements over the prior 12 months."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 466): "12.7 The scope of the portfolio subject to bank-wide backtesting should be updated quarterly based on the results of the latest trading desk-level backtesting, risk factor eligibility test and PLA tests."

### [[Expected Shortfall (ES)]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** These two provisions appear to interact at the point of deciding whether a trading desk may keep using the internal models approach: expected shortfall is the measure that produces the model-based capital number, while the P&L attribution test, alongside backtesting, is the gateway that determines desk eligibility and zone status. On that reading, a desk in the amber zone attracts a capital add-on and cannot return to green until it produces green-zone outcomes and clears its backtesting exceptions over the prior twelve months; failure ultimately pushes the desk to the standardised approach. This relationship is inferred rather than stated as an express cross-reference, so the reader should verify the primary text of the market risk chapters before relying on the sequencing for a capital decision.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 474): "(1) If a trading desk is in the PLA test amber zone, it cannot return to the PLA test green zone until: (a) the trading desk produces outcomes in the PLA test green zone; and (b) the trading desk has satisfied its backtesting exceptions requirements over the prior 12 months."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 845): "Definitions and instructions Row Number Explanation 1 Unconstrained expected shortfall: Expected shortfall (ES) as defined in SMAR13.1 to SMAR13.12, calculated without supervisory constraints on cross-risk factor correlations."
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

### [[Hypothetical P&L (HPL)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 474): "(1) If a trading desk is in the PLA test amber zone, it cannot return to the PLA test green zone until: (a) the trading desk produces outcomes in the PLA test green zone; and (b) the trading desk has satisfied its backtesting exceptions requirements over the prior 12 months."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 116): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."

### [[Internal Models Approach (IMA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 474): "(1) If a trading desk is in the PLA test amber zone, it cannot return to the PLA test green zone until: (a) the trading desk produces outcomes in the PLA test green zone; and (b) the trading desk has satisfied its backtesting exceptions requirements over the prior 12 months."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 842): "For banks that use the internal models approach (IMA), the standardised approach capital requirement in this template must be calculated based on the portfolios in trading desks that do not use the IMA (ie trading desks that are not deemed eligible to use the IMA per the terms of"

### [[Internal Models Approach General Provisions|Internal Models Approach: General Provisions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 474): "(1) If a trading desk is in the PLA test amber zone, it cannot return to the PLA test green zone until: (a) the trading desk produces outcomes in the PLA test green zone; and (b) the trading desk has satisfied its backtesting exceptions requirements over the prior 12 months."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 523): "16- Guidance on use of the internal models approach Trading desk-level backtesting 16.1 An additional consideration in specifying the appropriate risk measures and trading outcomes for profit and loss (P&L) attribution test and backtesting arises because the internally modelled r"

### [[Kolmogorov-Smirnov Test Metric]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 472): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 116): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."

### [[Principles for Modellability of Risk Factors]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 489): "The impact of the capital surcharge is limited by the formula: 13.44 For the purposes of calculating the capital requirement, the risk factor eligibility test, the PLA test and the trading desk-level backtesting are applied on a quarterly basis to update the modellability of risk"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Risk-Theoretical P&L (RTPL)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 474): "(1) If a trading desk is in the PLA test amber zone, it cannot return to the PLA test green zone until: (a) the trading desk produces outcomes in the PLA test green zone; and (b) the trading desk has satisfied its backtesting exceptions requirements over the prior 12 months."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 5): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Spearman Correlation Metric]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 472): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 116): "PLA test metrics 12.34 The PLA requirements are based on two test metrics: (1) the Spearman correlation metric to assess the correlation between RTPL and HPL; and (2) the Kolmogorov-Smirnov (KS) test metric to assess similarity of the distributions of RTPL and HPL."

## Lookup terms

`P&L attribution test`, `PLA test`, `PLA amber zone`, `trading desk eligibility`, `risk factor eligibility test`, `one-year backtesting and PLA report`, `model approval market risk`

#graphify/enriched #community/internal-models-approach
