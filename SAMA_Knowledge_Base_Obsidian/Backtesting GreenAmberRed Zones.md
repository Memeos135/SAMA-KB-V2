# Backtesting Green/Amber/Red Zones

This node is labelled for the backtesting traffic-light classification (green, amber/yellow and red zones) used to assess internal model exception counts and drive capital multiplier or model-use consequences. Note that the supplied context material actually shows Pillar 3 credit risk mitigation disclosure content (Template CR3, secured versus unsecured carrying amounts), so the node's underlying source coverage should be verified before relying on it for backtesting rules. Any backtesting classification obligations would bind SAMA-licensed banks with approved internal models for market risk.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[Backtesting]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 528): "Notes to Table 2: The table defines the backtesting green, amber and red zones that SAMA will use to assess backtesting results in conjunction with the internal models approach to market risk capital requirements."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 525): "Bank-wide backtesting Statistical considerations in defining the backtesting zones 16.9 To place the definitions of three zones of the bank-wide backtesting in proper perspective, however, it is useful to examine the probabilities of obtaining various numbers of exceptions under "

### [[Multiplication Factor mc]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 528): "Notes to Table 2: The table defines the backtesting green, amber and red zones that SAMA will use to assess backtesting results in conjunction with the internal models approach to market risk capital requirements."
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 101): "42 In particular, a bank may add modellable risk factors, and replace non-modellable risk factors by a basis between these additional modellable risk factors and these non- modellable risk factors."

## Lookup terms

`backtesting green amber red zone`, `traffic light approach`, `VaR exceptions / outliers`, `backtesting multiplier`, `internal models approach validation`, `Template CR3`, `credit risk mitigation disclosure`

#graphify/enriched #community/internal-models-approach
