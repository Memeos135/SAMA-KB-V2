# Internal Risk Transfer

Concept node covering the treatment of internal risk transfers — internal transactions moving risk between a bank's banking book and trading book, or between trading desks — for minimum capital purposes. It sets the conditions under which a banking book hedge executed internally is recognised for capital (documentation, a dedicated SAMA-approved internal risk transfer desk for general interest rate risk, and exact matching with an external market hedge), and specifies the consequences when those conditions fail, including exclusion of the trading book leg from market risk capital and capitalisation of short credit or equity positions under market risk rules. It binds SAMA-licensed banks calculating Pillar 1 market risk and banking book capital requirements.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3553_VER1.md`

## Connections

### [[Banking Book]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 381): "Alternatively, the internal risk transfer desk may obtain the external hedge from the market via a separate non-internal risk transfer trading desk acting as an agent, if and only if the GIRR internal risk transfer entered into with the non-internal risk transfer trading desk exa"
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 23): "Treatment of internal risk transfers 5.18 An internal risk transfer is an internal written record of a transfer of risk within the banking book, between the banking and the trading book or within the trading book (between different desks)."

### [[Credit Valuation Adjustment (CVA)]] — `references` [EXTRACTED]
- **What this link tells you:** If the bank hedges CVA risk through an internal desk rather than directly in the market, this link determines whether that hedge is recognised for capital purposes: recognition in the CVA capital calculation depends on satisfying the internal risk transfer conditions set out in the market risk framework, including how the internal transfer is externalised. The two instruments form an obligation chain — the CVA rules define the hedging benefit, the internal risk transfer rules define when an intra-bank transaction can carry that benefit. Practically, a CVA desk relying on internal hedges must evidence compliance with the internal risk transfer requirements or forgo the capital relief and accept the resulting SA-CVA or BA-CVA outcome.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 381): "Alternatively, the internal risk transfer desk may obtain the external hedge from the market via a separate non-internal risk transfer trading desk acting as an agent, if and only if the GIRR internal risk transfer entered into with the non-internal risk transfer trading desk exa"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 852): "a b SA-CVA RWA Number of counterparties 1 Interest rate risk 2 Foreign exchange risk 3 Reference credit spread risk 4 Equity risk 5 Commodity risk 6 Counterparty credit spread risk 7 Total (sum of rows 1 to 6) Linkages across templates [CVA3:7/a] is equal to [OV1:10/a] if the ban"

### [[Trading Book]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 381): "Alternatively, the internal risk transfer desk may obtain the external hedge from the market via a separate non-internal risk transfer trading desk acting as an agent, if and only if the GIRR internal risk transfer entered into with the non-internal risk transfer trading desk exa"
- **Grounding — related node** (SAMA_EN_3553_VER1 · Page 23): "Treatment of internal risk transfers 5.18 An internal risk transfer is an internal written record of a transfer of risk within the banking book, between the banking and the trading book or within the trading book (between different desks)."

### [[Trading Book  Banking Book Boundary|Trading Book / Banking Book Boundary]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 379): "Treatment of internal risk transfers 5.18 An internal risk transfer is an internal written record of a transfer of risk within the banking book, between the banking and the trading book or within the trading book (between different desks)."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 372): "5- Boundary between the banking book and the trading book Scope of the trading book 5.1 A trading book consists of all instruments that meet the specifications for trading book instruments set out in [5.2] through [5.13]."

## Lookup terms

`internal risk transfer`, `banking book / trading book boundary`, `internal risk transfer desk`, `external hedge exact match`, `trading book leg`, `GIRR internal risk transfer`, `market risk capital recognition`, `short credit position banking book`

#graphify/enriched #community/trading-book-boundary
