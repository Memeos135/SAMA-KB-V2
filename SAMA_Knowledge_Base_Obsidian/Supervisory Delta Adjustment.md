# Supervisory Delta Adjustment

Concept node for the supervisory delta adjustment, a trade-level parameter applied to adjusted notional amounts to reflect the direction (long/short in the primary risk factor) and non-linearity of a derivative; set at +1/-1 for non-option, non-CDO-tranche instruments and by prescribed formulas for options and CDO tranches using supervisory volatility. Applied in computing effective notionals for counterparty credit risk add-ons under SAMA's minimum capital requirements, and reflected in leverage ratio reporting adjustments. Binds banks in scope of SAMA's prudential capital and leverage framework.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[Effective Notional]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 575): "In this case, for each asset class to which the position is allocated, banks must determine appropriately the sign and delta adjustment of the relevant risk driver (the role of delta adjustments in SA-CCR is outlined further in 6.32 below)."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 683): "Effective notional, 𝐷𝑖(USD, thousands) Maturity Factor, Trade # Notional (USD Adjusted notional, 𝑑𝑖 𝑀𝐹𝑖 Delta, 𝛿𝑖 thousands) (USD, thousands) 1 10,000 10,000 (9/12)0.5 1 8,660 2 20,000 20,000 1 -1 -20,000 3 10,000 10,000 1 1 10,000 12.48."

### [[Potential Future Exposure (PFE) Add-on]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 158): "Project may issue unlimited additional debt Project may issue extremely limited additional debt Project may issue limited additional debt Project may issue no additional debt 13.14 Table 25 below sets out the supervisory rating grades for income producing real estate exposures an"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 158): "Project may issue unlimited additional debt Project may issue extremely limited additional debt Project may issue limited additional debt Project may issue no additional debt 13.14 Table 25 below sets out the supervisory rating grades for income producing real estate exposures an"

## Lookup terms

`supervisory delta`, `delta adjustment`, `primary risk factor`, `long or short position`, `option delta`, `supervisory volatility`, `CDO tranche delta`, `adjusted notional`

#graphify/enriched #community/sa-ccr-add-on-parameters
