# Expected Shortfall (ES)

Node on Expected Shortfall as the core risk measure in the internal models approach for market risk, including the distinction between unconstrained and constrained ES (sum of partial ES across regulatory risk factor classes), and its aggregation with the default risk capital requirement, the stressed ES capital add-on for non-modellable risk factors and any amber-zone surcharge. It also touches adjacent counterparty exposure measures (EE, EPE, Effective EPE, CVA) used elsewhere in the capital framework. Applies to banks calculating market risk capital under SAMA-approved internal models and reporting the associated disclosure templates.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[IMCC Capital for Modellable Risk Factors|IMCC: Capital for Modellable Risk Factors]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 469): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 457): "42 In particular, a bank may add modellable risk factors, and replace non-modellable risk factors by a basis between these additional modellable risk factors and these non- modellable risk factors."

### [[Internal Models Approach]] — `references` [EXTRACTED]
- **What this link tells you:** When deciding whether a bank may compute market risk capital under the internal models approach, the ES measure is not an optional add-on but the risk metric the approach is built on. The internal models rules define the capital requirement by reference to expected shortfall, so the two instruments form a single obligation chain: model approval conditions and the calibration/measurement requirements for ES must be read together. Practically, a model that does not meet the ES specification cannot be treated as compliant with the internal models approach, and the reader should assess both texts before signing off on IMA use.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 474): "13- Internal models approach: capital requirements calculation The internal models approach is based on the use Expected Shortfall (ES) techniques."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 118): "13- Internal models approach: capital requirements calculation The internal models approach is based on the use Expected Shortfall (ES) techniques."

### [[Internal Models Approach (IMA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 474): "13- Internal models approach: capital requirements calculation The internal models approach is based on the use Expected Shortfall (ES) techniques."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 474): "13- Internal models approach: capital requirements calculation The internal models approach is based on the use Expected Shortfall (ES) techniques."

### [[Internal Models Approach General Provisions|Internal Models Approach: General Provisions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 474): "13- Internal models approach: capital requirements calculation The internal models approach is based on the use Expected Shortfall (ES) techniques."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 474): "13- Internal models approach: capital requirements calculation The internal models approach is based on the use Expected Shortfall (ES) techniques."

### [[Liquidity Horizons by Risk Factor]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 845): "The constrained ES disclosed should be the sum of partial expected shortfall capital requirements (ie all other risk factors should be held constant) for the range of broad regulatory risk factor classes (interest rate risk, equity risk, foreign exchange risk, commodity risk and "
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[P&L Attribution (PLA) Test]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** These two provisions appear to interact at the point of deciding whether a trading desk may keep using the internal models approach: expected shortfall is the measure that produces the model-based capital number, while the P&L attribution test, alongside backtesting, is the gateway that determines desk eligibility and zone status. On that reading, a desk in the amber zone attracts a capital add-on and cannot return to green until it produces green-zone outcomes and clears its backtesting exceptions over the prior twelve months; failure ultimately pushes the desk to the standardised approach. This relationship is inferred rather than stated as an express cross-reference, so the reader should verify the primary text of the market risk chapters before relying on the sequencing for a capital decision.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 845): "Definitions and instructions Row Number Explanation 1 Unconstrained expected shortfall: Expected shortfall (ES) as defined in SMAR13.1 to SMAR13.12, calculated without supervisory constraints on cross-risk factor correlations."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 474): "(1) If a trading desk is in the PLA test amber zone, it cannot return to the PLA test green zone until: (a) the trading desk produces outcomes in the PLA test green zone; and (b) the trading desk has satisfied its backtesting exceptions requirements over the prior 12 months."
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

## Lookup terms

`Expected Shortfall`, `ES`, `constrained vs unconstrained ES`, `partial expected shortfall`, `default risk capital (DRC)`, `stressed expected shortfall (SES)`, `non-modellable risk factor capital requirement`, `expected positive exposure`, `credit valuation adjustment`

#graphify/enriched #community/internal-models-approach
