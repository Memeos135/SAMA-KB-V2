# Trade Reporting Data Fields

## Why this community

Data-field architecture for derivatives/trade reporting to SAMA: what must be reported per trade, how each report is identified, and how subsequent changes to a live trade are represented.

## How members connect

- Common Data operates as the master reporting table; the trade identifier and action-type fields are elements it points to, so obligations attach through it.
- The Unique Trade ID is the linking key that lets lifecycle events, collateral updates and corrections be matched to the original submission.
- Action Type plus the lifecycle-event appendix together determine which report type must be filed on modification, termination, error or compression — an obligation chain, not a menu.
- Evolutive collateral data is a companion table sharing key common fields, so collateral updates must stay reconcilable with trade-level data.

## Start here

- [[Common Data (Appendix A Table 2)]]
- [[Internal Unique Trade ID  UTI|Internal Unique Trade ID / UTI]]
- [[Action Type (Item 53)]]

## Members

- [[Action Type (Item 53)]]
- [[Common Data (Appendix A Table 2)]]
- [[Evolutive Collateral Data (Table 3)]]
- [[Internal Unique Trade ID  UTI|Internal Unique Trade ID / UTI]]
- [[Life Cycle Events (Appendix B)]]

#community/trade reporting data fields
