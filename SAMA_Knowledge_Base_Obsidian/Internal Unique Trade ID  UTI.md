# Internal Unique Trade ID / UTI

Covers the trade identifier fields used in SAMA TR reporting: the 'Unique trade ID' (item 15), which may be provisionally left blank where a foreign generating entity has not supplied it by the T+1 deadline and must then be added by modification report, and the 'Internal unique trade ID' (item 14), which must match a previously reported code on all subsequent lifecycle reports and cannot itself be modified or corrected. It also underpins the 'Linked UTI' field used when a trade is novated for central clearing. Applies to reporting banks submitting lifecycle event reports.

**Regimes:** governance/risk, banking prudential, other

## Sources

- `corpus/markdown/SAMA_EN_10593_VER1_0.md`

## Connections

### [[Common Data (Appendix A Table 2)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 26): "15 Section 2c - ١ Unique trade | The UTI ID could be the same as the "Internal | Up to 52 alphanumerical character code using Details on the | ID unique trade id" except in those trades in which | exclusively upper-case alphabetical characters (A-Z) transaction the other counterp"
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 55): "besides mandatory fields described in the first bullet of this paragraph, table 2 item 14 “Internal unique trade ID” shall be populated with a code that is fully coincident with a previously reported “Internal unique trade ID”."

### [[Life Cycle Events (Appendix B)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 26): "15 Section 2c - ١ Unique trade | The UTI ID could be the same as the "Internal | Up to 52 alphanumerical character code using Details on the | ID unique trade id" except in those trades in which | exclusively upper-case alphabetical characters (A-Z) transaction the other counterp"
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 53): "Appendix B List of reportable life cycle events for OTC derivative transactions:"

## Lookup terms

`Unique trade ID UTI`, `Internal unique trade ID item 14`, `Linked UTI`, `trade identifier OTC derivative`, `T+1 blank UTI`, `modification report to populate UTI`

#graphify/enriched #community/trade-reporting-data-fields
