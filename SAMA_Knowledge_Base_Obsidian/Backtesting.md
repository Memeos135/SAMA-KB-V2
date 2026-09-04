# Backtesting

Node setting the backtesting regime for internal market risk models: daily comparison of a one-day 99th percentile VaR against actual and hypothetical P&L over the prior 12 months (250 trading days), at both bank-wide and trading desk level, with the green/amber/red zone framework driving supervisory consequences. Consequences escalate from no add-on, to a capital add-on scaled to the number of exceptions, to an automatic increase in the multiplication factor or withdrawal of model permission. Binds banks using internal models; SAMA holds the assessment, notification and disallowance powers, and banks must document and explain every exception.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[Actual P&L (APL)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 465): "Backtesting requirements 12.4 Backtesting requirements compare the value-at-risk (VaR) measure calibrated to a one-day holding period against each of the actual P&L (APL) and hypothetical P&L (HPL) over the prior 12 months."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 109): "Backtesting requirements 12.4 Backtesting requirements compare the value-at-risk (VaR) measure calibrated to a one-day holding period against each of the actual P&L (APL) and hypothetical P&L (HPL) over the prior 12 months."

### [[Backtesting GreenAmberRed Zones|Backtesting Green/Amber/Red Zones]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 525): "Bank-wide backtesting Statistical considerations in defining the backtesting zones 16.9 To place the definitions of three zones of the bank-wide backtesting in proper perspective, however, it is useful to examine the probabilities of obtaining various numbers of exceptions under "
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 528): "Notes to Table 2: The table defines the backtesting green, amber and red zones that SAMA will use to assess backtesting results in conjunction with the internal models approach to market risk capital requirements."

### [[Hypothetical P&L (HPL)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 465): "Backtesting requirements 12.4 Backtesting requirements compare the value-at-risk (VaR) measure calibrated to a one-day holding period against each of the actual P&L (APL) and hypothetical P&L (HPL) over the prior 12 months."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 109): "Backtesting requirements 12.4 Backtesting requirements compare the value-at-risk (VaR) measure calibrated to a one-day holding period against each of the actual P&L (APL) and hypothetical P&L (HPL) over the prior 12 months."

### [[IMM Model Validation]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** For a decision on whether a bank's internal model remains fit for regulatory capital purposes, validation requirements and backtesting outcomes are best assessed as complementary evidence rather than separate exercises. Validation covers the approaches, assumptions and benchmarks used to test a model, while bank-wide backtesting supplies the quantitative exception counts and zone classification that can trigger supervisory consequences such as multiplier increases or model restrictions. This linkage is inferred from subject matter rather than an express cross-reference, so the reader should verify in the primary texts whether backtesting is formally incorporated into the validation obligation or stands as a distinct requirement.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 525): "Bank-wide backtesting Statistical considerations in defining the backtesting zones 16.9 To place the definitions of three zones of the bank-wide backtesting in proper perspective, however, it is useful to examine the probabilities of obtaining various numbers of exceptions under "
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 843): "(E) Validation of models and modelling processes (a) The approaches used in the validation of the models and modelling processes, describing general approaches used and the types of assumptions and benchmarks on which they rely."
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

### [[Internal Models Approach (IMA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 523): "16- Guidance on use of the internal models approach Trading desk-level backtesting 16.1 An additional consideration in specifying the appropriate risk measures and trading outcomes for profit and loss (P&L) attribution test and backtesting arises because the internally modelled r"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 842): "For banks that use the internal models approach (IMA), the standardised approach capital requirement in this template must be calculated based on the portfolios in trading desks that do not use the IMA (ie trading desks that are not deemed eligible to use the IMA per the terms of"

### [[Internal Models Approach General Provisions|Internal Models Approach: General Provisions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 523): "16- Guidance on use of the internal models approach Trading desk-level backtesting 16.1 An additional consideration in specifying the appropriate risk measures and trading outcomes for profit and loss (P&L) attribution test and backtesting arises because the internally modelled r"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 474): "13- Internal models approach: capital requirements calculation The internal models approach is based on the use Expected Shortfall (ES) techniques."

### [[Multiplication Factor mc]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 467): "12.10 The backtesting green zone generally would not initiate a SAMA increase in capital requirements for backtesting (ie no backtesting add-on would apply)."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 101): "42 In particular, a bank may add modellable risk factors, and replace non-modellable risk factors by a basis between these additional modellable risk factors and these non- modellable risk factors."

### [[P&L Attribution (PLA) Test]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 466): "12.7 The scope of the portfolio subject to bank-wide backtesting should be updated quarterly based on the results of the latest trading desk-level backtesting, risk factor eligibility test and PLA tests."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 474): "(1) If a trading desk is in the PLA test amber zone, it cannot return to the PLA test green zone until: (a) the trading desk produces outcomes in the PLA test green zone; and (b) the trading desk has satisfied its backtesting exceptions requirements over the prior 12 months."

### [[Value-at-Risk (VaR)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 5): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

## Lookup terms

`backtesting`, `backtesting exceptions / outliers`, `green amber red zone`, `backtesting add-on`, `VaR 99th percentile`, `actual P&L / hypothetical P&L`, `multiplication factor`, `desk-level backtesting`

#graphify/enriched #community/internal-models-approach
