# Maturity Factor (MF)

Concept node for the maturity factor, the time-scaling parameter applied together with adjusted notional and supervisory delta to derive a trade's effective notional, with distinct treatments for margined and unmargined netting sets (unmargined trades with remaining maturity over one year receiving a factor of one). The cited source material also situates maturity-related bucketing in the market risk modellability/risk factor eligibility context. Relevant to banks calculating counterparty credit and market risk capital requirements under SAMA rules.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[Effective Notional]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 688): "That is: Adjusted Effective notional, 𝐷𝑖 (USD, thousands) Base currency Notional notional, 𝑑𝑖 (USD, thousands) Maturity Factor, Delta, IR Trade Maturity (USD thousands) # (hedging bucket 𝑀𝐹𝑖 𝛿𝑖 set) 1 10,000 USD 3 78,694 1.5 ∗√14 250 ⁄ 1 27,934 2 10,000 USD 2 36,254 1.5 ∗√14 250 "
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 688): "That is: Adjusted Effective notional, 𝐷𝑖 (USD, thousands) Base currency Notional notional, 𝑑𝑖 (USD, thousands) Maturity Factor, Delta, IR Trade Maturity (USD thousands) # (hedging bucket 𝑀𝐹𝑖 𝛿𝑖 set) 1 10,000 USD 3 78,694 1.5 ∗√14 250 ⁄ 1 27,934 2 10,000 USD 2 36,254 1.5 ∗√14 250 "

### [[Margin Period of Risk (MPOR)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 457): "42 In particular, a bank may add modellable risk factors, and replace non-modellable risk factors by a basis between these additional modellable risk factors and these non- modellable risk factors."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Potential Future Exposure (PFE) Add-on]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 457): "42 In particular, a bank may add modellable risk factors, and replace non-modellable risk factors by a basis between these additional modellable risk factors and these non- modellable risk factors."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 874): "This amount should be reported with the 1.4 alpha factor applied as specified in SLEV7.2.2 (ii) and (v) 8 9 Add-on amount for the potential future exposure (PFE) of all derivative exposures calculated in accordance with SLEV7.2.2 (ii) and (v)."

## Lookup terms

`maturity factor`, `MF`, `margined netting set`, `unmargined trades`, `margin period of risk`, `remaining maturity`, `maturity bucket`, `effective notional`

#graphify/enriched #community/sa-ccr-add-on-parameters
