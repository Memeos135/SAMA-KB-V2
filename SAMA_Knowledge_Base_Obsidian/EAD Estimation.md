# EAD Estimation

This node sets the requirements for estimating exposure at default (EAD) under the IRB framework, covering the definition of EAD as expected gross exposure at obligor default, the floor at current drawn amount for on-balance sheet items, and the additional standards applying to own-EAD estimates for off-balance sheet items under the advanced approach. It requires long-run default-weighted average estimates with a margin of conservatism, conservatism where default frequency and EAD are positively correlated, and prohibits capping reference data at outstanding principal or facility limits. It binds banks approved by SAMA to use advanced IRB EAD estimates.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[Risk Quantification]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 206): "The additional minimum requirements for internal estimation of EAD under the advanced approach, therefore, focus on the estimation of EAD for off- balance sheet items (excluding transactions that expose banks to counterparty credit risk as set out in chapter 5 of the Counterparty"
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 168): "Risk-weighted assets for default risk 14.2 For receivables belonging unambiguously to one asset class, the IRB risk weight for default risk is based on the risk-weight function applicable to that particular exposure type, as long as the bank can meet the qualification standards f"

### [[Undrawn Limit Factor (ULF) Approach]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 209): "(1) An acceptable approach could include using an estimation method other than the ULF approach that avoids the instability issue by not using potentially small undrawn limits that could approach zero in the denominator or, as appropriate, switching to a method other than the ULF"
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 209): "(1) An acceptable approach could include using an estimation method other than the ULF approach that avoids the instability issue by not using potentially small undrawn limits that could approach zero in the denominator or, as appropriate, switching to a method other than the ULF"

## Lookup terms

`EAD`, `exposure at default`, `own-EAD estimates`, `credit conversion factor`, `CCF`, `off-balance sheet items`, `advanced IRB`, `margin of conservatism`, `EAD reference data`

#graphify/enriched #community/irb-risk-parameter-estimation
