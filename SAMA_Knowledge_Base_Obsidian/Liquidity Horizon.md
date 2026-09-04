# Liquidity Horizon

A defined-term node setting the regulatory liquidity horizons used to scale expected shortfall from a 10-day base horizon in the internal models approach. It prescribes the assignment of horizons (10 to 120 days) by risk factor category — interest rate, credit spread, equity, FX, commodity and their volatilities — including treatment of repo, dividend, inflation and basis risk factors. It binds banks computing daily ES for bank-wide and desk-level market risk capital.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[Default Risk Capital (DRC) Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** The default risk capital requirement exists precisely because jump-to-default risk is not captured by the credit spread shocks in the sensitivities-based method, so a compliance review must confirm that both charges are computed and that the same risk is neither omitted nor double-counted. Liquidity horizons are the calibration concept underpinning the market risk shocks, which is why the DRC provisions are read against them when demonstrating that the split of coverage is complete. Note that the two extracted excerpts overlap in the same section of the standardised market risk rules, so the precise nature of the cross-reference should be verified against the primary text before it is relied on in an assessment.
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 73): "8- Standardised approach: default risk capital requirement Main concepts of default risk capital requirements 8.1 The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks under the sensitivities-"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 429): "8- Standardised approach: default risk capital requirement Main concepts of default risk capital requirements 8.1 The default risk capital (DRC) requirement is intended to capture jump-to-default (JTD) risk that may not be captured by credit spread shocks under the sensitivities-"

### [[Expected Shortfall (ES) Model]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 124): "The liquidity horizon of the index is the shortest liquidity horizon (out of 10, 20, 40, 60 and 120 days) that is equal to or longer than the weighted average liquidity horizon."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 113): "(1) The trading desk’s risk management model must include all risk factors that are included in the bank’s expected shortfall (ES) model with SAMA parameters and any risk factors deemed not modellable by SAMA, and which are therefore not included in the ES model for calculating t"

## Lookup terms

`liquidity horizon`, `expected shortfall ES`, `internal models approach IMA`, `base horizon 10 days`, `risk factor category`, `97.5th percentile`, `liquidity-adjusted ES`, `specified currencies`

#graphify/enriched #community/internal-models-approach
