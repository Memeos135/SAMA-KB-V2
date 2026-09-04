# Action Type (Item 53)

Item 53 'Action type' is the field that classifies each submission to the SAMA-authorised trade repository — New (N), Modify (M), Error (E), Early Termination (C), Correction (R), Valuation update (V) and Compression (Z) — and drives which other fields are mandatory, conditionally mandatory, potential or not relevant. It governs how banks report lifecycle events such as modifications, novations (termination plus new report), notional increases/decreases, erroneous submissions and early terminations. Binds reporting banks under the OTC derivatives TR reporting requirements.

**Regimes:** governance/risk, banking prudential, other

## Sources

- `corpus/markdown/SAMA_EN_10593_VER1_0.md`

## Connections

### [[Common Data (Appendix A Table 2)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 6): "An interbranch transaction refers to a principal-to-principal transaction (or a back-to-back transaction) conducted between different branches of the same bank, including any transaction undertaken to transfer the risk of the transaction (or portfolio transactions) from one branc"
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 54): "In the case that the novation takes place before T+1, the reporting counterparty shall only submit a single report (post-novation) with table 2 item 53 “Action type” populated with the value “N” and table 1 item 2 “ID of the other Counterparty” populated with the LEI of the CCP."

### [[Life Cycle Events (Appendix B)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 6): "An interbranch transaction refers to a principal-to-principal transaction (or a back-to-back transaction) conducted between different branches of the same bank, including any transaction undertaken to transfer the risk of the transaction (or portfolio transactions) from one branc"
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 53): "Appendix B List of reportable life cycle events for OTC derivative transactions:"

## Lookup terms

`Action type item 53`, `action type codes N M E C R V Z`, `modification report`, `error report`, `early termination report`, `correction report`, `novation reporting`

#graphify/enriched #community/trade-reporting-data-fields
