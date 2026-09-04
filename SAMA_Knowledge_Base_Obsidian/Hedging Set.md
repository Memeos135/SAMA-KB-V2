# Hedging Set

Concept node for the hedging set, the grouping of derivative trades within a netting set that determines the extent of offsetting permitted when calculating asset-class add-ons: separate sets per currency for interest rate, per currency pair for FX, single sets for credit and equity, and four commodity categories, with special sets for basis and volatility transactions. Supervisory factors are applied at hedging-set level to convert effective notionals into add-ons. Binds banks computing counterparty credit risk exposure amounts under SAMA's minimum capital requirements.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[Netting Set]] — `conceptually_related_to` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"
- **Caveat:** Relation is a similarity heuristic, not a cross-reference.

### [[Potential Future Exposure (PFE) Add-on]] — `references` [EXTRACTED]
- **What this link tells you:** The PFE add-on cannot be calculated without first constructing hedging sets, so a decision on add-on treatment depends on the hedging-set definitions and supervisory factors in the counterparty credit risk instrument. The relationship is an obligation chain within the same capital framework: effective notionals are determined at hedging-set level and then scaled by the prescribed supervisory factor to produce the add-on that feeds the exposure calculation. Note that the excerpt captured for the add-on node does not obviously address hedging sets, so the reader should verify the exact provisions in the primary text before relying on the specific paragraph mapping.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 688): "Next, the hedging set level add-ons (𝐴𝑑𝑑𝑂𝑛ℎ𝑠) must be recalculated by multiplying the recalculated effective notionals of each hedging set (𝐸𝑁ℎ𝑠) by the prescribed supervisory factor of the hedging set (𝑆𝐹𝑈𝑆𝐷)."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 158): "Project may issue unlimited additional debt Project may issue extremely limited additional debt Project may issue limited additional debt Project may issue no additional debt 13.14 Table 25 below sets out the supervisory rating grades for income producing real estate exposures an"

## Lookup terms

`hedging set`, `netting set`, `basis transactions`, `volatility transactions`, `supervisory factor`, `asset class add-on`, `currency pair hedging set`, `commodity hedging sets`

#graphify/enriched #community/sa-ccr-netting-sets
