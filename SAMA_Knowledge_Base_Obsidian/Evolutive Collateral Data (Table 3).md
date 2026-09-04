# Evolutive Collateral Data (Table 3)

Field-level reporting specification (Table 3, evolutive/common data) for collateral attributes of OTC derivative contracts reported to a trade repository under SAMA's OTC derivatives reporting and risk mitigation requirements (version 4.0, September 2025). It sets the permitted values and formats for collateralisation status, portfolio-basis flag and portfolio code, initial and variation margin posted/received, excess collateral, and the associated ISO currency codes. It binds reporting counterparties subject to the SAMA trade repository reporting obligation.

**Regimes:** governance/risk, banking prudential, other

## Sources

- `corpus/markdown/SAMA_EN_10593_VER1_0.md`

## Connections

### [[Common Data (Appendix A Table 2)]] — `shares_data_with` [INFERRED]
- **What this link tells you:** When completing a trade repository submission, the collateral fields and the common data fields form one report rather than separate filings, so field-level consistency across the tables determines whether the report is accepted as complete and accurate. The link is inferred from the shared reporting appendix structure, where common data identifies the report and its action type (including corrections to previously submitted erroneous fields) and collateral data populates valuation and margin attributes. Practically, an error in either table engages the correction mechanism, so remediation should be scoped across both rather than to the table where the error was first noticed; confirm field definitions in the primary appendix.
- **Grounding — this node** (SAMA_EN_10593_VER1_0 · Page 43): "3 13 Parties to the | Currency of the | Specify the currency of the excess collateral | ISO 4217 Currency Code, 3 alphabetical characters contract - excess collateral | posted Collateral posted 3 14 Parties to the | Excess Value of collateral received in excess of the | Up to 20 "
- **Grounding — related node** (SAMA_EN_10593_VER1_0 · Page 40): "— a previously submitted report contains erroneous data fields, in which case the report correcting the erroneous data fields of the previous report shall be identified as ‘correction’;"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

## Lookup terms

`OTC derivatives trade repository reporting`, `collateral portfolio code`, `initial margin posted`, `variation margin received`, `excess collateral`, `uncollateralised / partially collateralised / fully collateralised`, `evolutive data fields`, `ISO 4217 currency code`

#graphify/enriched #community/trade-reporting-data-fields
