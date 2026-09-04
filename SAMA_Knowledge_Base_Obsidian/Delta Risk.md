# Delta Risk

Concept node for Delta risk, the linear sensitivity component of the sensitivities-based method under SAMA's standardised approach to market risk. It covers sensitivities to regulatory delta risk factors across the risk classes (e.g. GIRR, credit spread, equity, FX, commodity), with prescribed risk weights and correlations feeding the aggregate market risk capital requirement; delta risk weights also anchor the curvature shocks. Applies to banks calculating market risk capital on trading book positions and in-scope banking book FX and commodity exposures.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[Risk Bucket]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 5): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Sensitivities-Based Method]] — `references` [EXTRACTED]
- **What this link tells you:** Delta risk cannot be assessed or capitalised as a standalone charge: it is one of the risk components of the sensitivities-based method under the standardised approach to market risk, alongside vega and curvature, and its output only becomes a capital requirement after bucketing and aggregation across the prescribed risk classes. The list of risk classes referenced in the delta provisions is the same list that drives the sensitivities-based method's scope and correlation structure. The consequence is that a delta-sensitivity calculation must be validated against the sensitivities-based method's instrument scope and aggregation rules before any capital figure is relied on.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 385): "Instruments subject to each component of the sensitivities-based method 7.2 In applying the sensitivities-based method, all instruments held in trading desks as set out in [4] and subject to the sensitivities-based method (ie excluding instruments where the value at any point in "

## Lookup terms

`delta risk`, `delta sensitivities`, `GIRR delta`, `delta risk weight`, `weighted sensitivities`, `sensitivities-based method`, `standardised approach market risk`

#graphify/enriched #community/internal-models-approach
