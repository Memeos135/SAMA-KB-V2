# Common Data (Appendix A Table 2)

Appendix A Table 2 of SAMA's Trade Repository Reporting and Risk Mitigation Requirements sets out the 'common data' reporting fields (economic terms and administrative details) that reporting banks must populate on the TR Operator's templates for each reportable OTC derivative transaction. Key referenced items include the Unique trade ID (item 15), Internal unique trade ID (item 14), Notional (item 19), Early termination date (item 27) and Action type (item 53). It binds SAMA-licensed reporting banks, which must report directly to the SAMA-authorised trade repository and may not outsource or use agents.

**Regimes:** governance/risk, banking prudential, other

## Sources

- `corpus/markdown/SAMA_EN_10593_VER1_0.md`

## Connections

### [[Action Type (Item 53)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 54): "In the case that the novation takes place before T+1, the reporting counterparty shall only submit a single report (post-novation) with table 2 item 53 “Action type” populated with the value “N” and table 1 item 2 “ID of the other Counterparty” populated with the LEI of the CCP."
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 6): "An interbranch transaction refers to a principal-to-principal transaction (or a back-to-back transaction) conducted between different branches of the same bank, including any transaction undertaken to transfer the risk of the transaction (or portfolio transactions) from one branc"

### [[Evolutive Collateral Data (Table 3)]] — `shares_data_with` [INFERRED]
- **What this link tells you:** When completing a trade repository submission, the collateral fields and the common data fields form one report rather than separate filings, so field-level consistency across the tables determines whether the report is accepted as complete and accurate. The link is inferred from the shared reporting appendix structure, where common data identifies the report and its action type (including corrections to previously submitted erroneous fields) and collateral data populates valuation and margin attributes. Practically, an error in either table engages the correction mechanism, so remediation should be scoped across both rather than to the table where the error was first noticed; confirm field definitions in the primary appendix.
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 40): "— a previously submitted report contains erroneous data fields, in which case the report correcting the erroneous data fields of the previous report shall be identified as ‘correction’;"
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 43): "3 13 Parties to the | Currency of the | Specify the currency of the excess collateral | ISO 4217 Currency Code, 3 alphabetical characters contract - excess collateral | posted Collateral posted 3 14 Parties to the | Excess Value of collateral received in excess of the | Up to 20 "
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

### [[Internal Unique Trade ID  UTI|Internal Unique Trade ID / UTI]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 55): "besides mandatory fields described in the first bullet of this paragraph, table 2 item 14 “Internal unique trade ID” shall be populated with a code that is fully coincident with a previously reported “Internal unique trade ID”."
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 26): "15 Section 2c - ١ Unique trade | The UTI ID could be the same as the "Internal | Up to 52 alphanumerical character code using Details on the | ID unique trade id" except in those trades in which | exclusively upper-case alphabetical characters (A-Z) transaction the other counterp"

## Lookup terms

`Common data Table 2`, `Appendix A reporting fields`, `OTC derivative trade reporting template`, `SAMA authorised TR Operator`, `reporting service agreement`, `reportable transaction fields`, `notional field item 19`

#graphify/enriched #community/trade-reporting-data-fields
