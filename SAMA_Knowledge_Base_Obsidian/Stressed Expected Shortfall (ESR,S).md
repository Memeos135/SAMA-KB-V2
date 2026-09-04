# Stressed Expected Shortfall (ESR,S)

Concept node on stressed expected shortfall as the calibration basis for internal-model market risk capital, including the data-quality principle that inputs must reflect prices observed or quoted during the stress period and be sourced from the historical stress window where possible. It also touches adjacent IMA model-validation mechanics (front/back office versus risk price comparisons, data update frequency, P&L attribution zones and backtesting). Binds banks with IMA model approval for market risk.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[Aggregate Capital Requirement for Modellable Risk Factors (IMCC)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 113): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 101): "42 In particular, a bank may add modellable risk factors, and replace non-modellable risk factors by a basis between these additional modellable risk factors and these non- modellable risk factors."

### [[Expected Shortfall (ES) Model]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 118): "Calculation of expected shortfall 13.1 Banks will have flexibility in devising the precise nature of their expected shortfall (ES) models, but the following minimum standards will apply for the purpose of calculating market risk capital requirements."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 113): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"

### [[Reduced Set of Risk Factors]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 91): "(e) The market risk capital requirements for risk factors that do not satisfy the risk factor eligibility test must be determined using stressed expected shortfall (SES) models as specified in [13.16] to [13.17] The model approval process requires an overall assessment of a bank’"
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 5): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

## Lookup terms

`stressed expected shortfall`, `ES R,S`, `expected shortfall calibration`, `period of stress data`, `risk factor data quality principles`, `PLA test amber zone`, `backtesting exceptions`, `internal models approach`

#graphify/enriched #community/internal-models-approach
