# Undrawn Limit Factor (ULF) Approach

This node addresses the undrawn limit factor (ULF) method of estimating credit conversion factors and its known instability for facilities close to being fully drawn at the reference date. It requires banks to insulate EAD estimates from that instability, identifies acceptable alternatives (limit factor, balance factor, additional utilisation factor) and rejects capping/flooring or omitting affected observations as inadequate fixes. Applies to banks using advanced IRB EAD models under SAMA's credit risk capital rules.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[EAD Estimation]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 209): "(1) An acceptable approach could include using an estimation method other than the ULF approach that avoids the instability issue by not using potentially small undrawn limits that could approach zero in the denominator or, as appropriate, switching to a method other than the ULF"
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 209): "(1) An acceptable approach could include using an estimation method other than the ULF approach that avoids the instability issue by not using potentially small undrawn limits that could approach zero in the denominator or, as appropriate, switching to a method other than the ULF"

### [[Own-EAD Estimation]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 209): "(1) An acceptable approach could include using an estimation method other than the ULF approach that avoids the instability issue by not using potentially small undrawn limits that could approach zero in the denominator or, as appropriate, switching to a method other than the ULF"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 216): "(1) An acceptable approach could include using an estimation method other than the ULF approach that avoids the instability issue by not using potentially small undrawn limits that could approach zero in the denominator or, as appropriate, switching to a method other than the ULF"

## Lookup terms

`undrawn limit factor`, `ULF`, `region of instability`, `CCF estimation`, `limit utilisation`, `balance factor`, `additional utilisation factor`, `EAD model`

#graphify/enriched #community/irb-risk-parameter-estimation
