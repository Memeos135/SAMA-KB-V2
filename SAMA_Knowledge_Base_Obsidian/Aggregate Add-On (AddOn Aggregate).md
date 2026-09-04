# Aggregate Add-On (AddOn Aggregate)

Explains the aggregate add-on component of potential future exposure under SA-CCR: add-ons are computed per asset class within a netting set and summed with no diversification benefit across the five asset classes, then scaled by a multiplier that recognizes excess collateral or negative mark-to-market, subject to a floor. It also covers the related replacement cost formulation using threshold, minimum transfer amount and net independent collateral amount, and the allocation of derivatives to asset classes by primary risk driver. It binds banks measuring counterparty credit risk exposure under SA-CCR.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[Derivative Exposures (Leverage Ratio)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"
- **Grounding — related node** (SAMA_EN_4303_VER1 · Page 5): "5.4 Exposure measure should include the following exposures: (i) On-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures); (ii) Derivative exposures; (iii) Securities financing transaction (SFT) exposures; and (iv) Off-bala"

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** When calculating EAD for counterparty credit risk you must apply the aggregate add-on, since it drives the potential future exposure element that combines with replacement cost to produce the exposure measure. The connection spans two SAMA capital instruments, which means the add-on methodology and multiplier logic set out in the other document is the operative source for that input and should be read as the controlling text, not restated locally. For a decision, this means any change in add-on treatment or collateral recognition alters EAD and therefore capital and disclosure outcomes; confirm which version of each instrument is in force before relying on the calculation.
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."

## Lookup terms

`SA-CCR`, `aggregate add-on`, `AddOn aggregate`, `potential future exposure`, `PFE multiplier`, `netting set`, `replacement cost`, `NICA threshold MTA`, `primary risk driver`, `asset class add-on`

#graphify/enriched #community/leverage-ratio-exposures
