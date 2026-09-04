# Value-at-Risk (VaR)

A concept node covering value-at-risk and the surrounding defined vocabulary of SAMA's market risk capital framework, including risk factor, risk position, risk bucket, risk class, sensitivity, delta risk, embedded derivative and the look-through approach. It functions mainly as a definitional anchor for how market risk measures and capital charges are constructed. It is relevant to all banks calculating market risk capital requirements under SAMA rules.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[Backtesting]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 5): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Default Risk Capital (DRC) Requirement]] — `references` [EXTRACTED]
- **What this link tells you:** When sizing market risk capital for trading book positions, treat default risk as a distinct component rather than something already absorbed by a general value-at-risk style measure. Both items sit inside the same market risk capital regime, which enumerates default risk alongside interest rate, credit spread, equity, FX and commodities risk as risks attracting capital, while VaR is the loss-measurement concept used in the modelled treatment. The practical consequence is that a bank cannot rely on its VaR output alone to evidence adequate market risk capital; the default risk charge must be identified and computed on its own terms, and the reader should confirm the exact interaction in the primary market risk text.
- **Grounding — this node** (SAMA_EN_3553_VER1 · Page 8): "3.3 The risks subject to market risk capital requirements include but are not limited to: (1) Default risk, interest rate risk, credit spread risk, equity risk, foreign exchange (FX) risk and commodities risk for trading book instruments; and (2) FX risk and commodities risk for "
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 364): "3.3 The risks subject to market risk capital requirements include but are not limited to: (1) Default risk, interest rate risk, credit spread risk, equity risk, foreign exchange (FX) risk and commodities risk for trading book instruments; and (2) FX risk and commodities risk for "

## Lookup terms

`value-at-risk`, `VaR`, `risk factor definition`, `risk position`, `risk class`, `risk bucket`, `delta risk / vega risk`, `look-through approach`, `embedded derivative`

#graphify/enriched #community/internal-models-approach
