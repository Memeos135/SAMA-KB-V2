# Aggregate Add-On

Explains the aggregate add-on component of the PFE calculation for each netting set under SA-CCR, built up from asset-class-level add-ons and multiplied by the collateral/negative-MTM multiplier to produce PFE. It sits alongside the replacement cost formula (threshold, minimum transfer amount and net independent collateral amount, floored at zero) in determining counterparty credit risk exposure. Binds banks computing counterparty credit risk capital under the standardised approach.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`

## Connections

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 573): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."

## Lookup terms

`aggregate add-on`, `AddOn aggregate`, `PFE multiplier`, `netting set add-on`, `replacement cost RC`, `NICA`, `threshold and minimum transfer amount`, `SA-CCR`

#graphify/enriched #community/counterparty-credit-risk-components
