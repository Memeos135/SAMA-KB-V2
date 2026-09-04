# RWA for Market Risk

A concept node on risk-weighted assets and Pillar 1 capital requirements for market risk within SAMA's Basel-aligned RWA overview and disclosure instructions. The available context frames it alongside the other RWA components (credit risk, counterparty credit risk, CVA, equity positions, settlement risk, securitisation and operational risk) and the general rule that the capital requirement is normally 8% of RWA, subject to any applicable floor or scaling adjustment. It binds banks preparing regulatory capital calculations and Pillar 3 disclosures for SAMA.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4376_VER1.md`

## Connections

### [[Basic Approach for CVA (BA-CVA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 849): "23.2.1 CVA risk under the basic approach (BA-CVA): Template CVA1: The reduced basic approach for CVA (BA-CVA) Purpose: To provide the components used for the computation of RWA under the reduced BA-CVA for CVA risk."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 849): "23.2.1 CVA risk under the basic approach (BA-CVA): Template CVA1: The reduced basic approach for CVA (BA-CVA) Purpose: To provide the components used for the computation of RWA under the reduced BA-CVA for CVA risk."

### [[Credit Valuation Adjustment (CVA) Framework]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 560): "Credit valuation adjustment A credit valuation adjustment that reflects the market value of the credit risk of the counterparty to the firm, but does not reflect the market value of the credit risk of the bank to the counterparty."

### [[Output Floor Requirements]] — `references` [EXTRACTED]
- **What this link tells you:** The output floor is calculated on total standardised risk-weighted assets, and the framework identifies market risk RWA as one of the components that must be included alongside credit and operational risk. The reference means the market risk RWA rules are incorporated into the floor calculation, so a bank using internal models for market risk must still produce the standardised equivalent. For a compliance decision, verify that the standardised market risk figure is computed and fed into the floor comparison; excluding it would understate the floor and could mask a binding capital constraint.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 728): "Minimum risk-based capital requirements 3 Risk-weighted assets and Output Floor requirements 4 RWA for credit risk 5 RWA for market risk 6 RWA for operational risk 6 Calculation of the output floor 7 Version Issuance Date Page Number Output Floor Requirements 1.1 December 2022 2 "
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 728): "Minimum risk-based capital requirements 3 Risk-weighted assets and Output Floor requirements 4 RWA for credit risk 5 RWA for market risk 6 RWA for operational risk 6 Calculation of the output floor 7 Version Issuance Date Page Number Output Floor Requirements 1.1 December 2022 2 "

### [[SAMA Minimum Capital Requirements for CCR and CVA]] — `references` [EXTRACTED]
- **What this link tells you:** When computing total RWA and capital ratios, market risk RWA and the CCR/CVA capital requirements are separate components of the same denominator and must be assembled consistently. The market risk framework defines the risk classes and RWA output, while the CCR and CVA framework sets the counterparty-side requirements that feed the same minimum ratios, buffers and Pillar 2 add-ons. The consequence is that scoping decisions (for example whether an exposure sits in the trading book market risk charge or attracts a CVA charge) affect where capital is held, not whether it is held, so both instruments should be checked before concluding on a capital treatment.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 779): "capital conservation buffer, G-SIB surcharge and countercyclical capital buffer) and Pillar 2 capital requirements (if CET1 capital is required); (ii) CET1 capital that banks must maintain to meet the minimum regulatory capital ratios and any CET1 capital used to meet Tier 1 capi"

### [[SCCR - Minimum Capital Requirements for CCR and CVA]] — `references` [EXTRACTED]
- **What this link tells you:** Deciding the capital treatment of counterparty credit risk and CVA requires reading the market risk framework alongside it, because CVA risk is measured using market risk concepts — notably the defined risk classes such as credit spread risk — that the market risk instrument establishes. The cross-reference means the definitions and risk-class taxonomy are sourced from the market risk rules rather than restated in the CCR/CVA rules, and both feed the same total RWA and capital ratio calculation. For the reader, a CVA capital determination should be evidenced against the market risk definitions to avoid inconsistent classification or double-counting across the two RWA components.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 779): "capital conservation buffer, G-SIB surcharge and countercyclical capital buffer) and Pillar 2 capital requirements (if CET1 capital is required); (ii) CET1 capital that banks must maintain to meet the minimum regulatory capital ratios and any CET1 capital used to meet Tier 1 capi"

### [[Standardized Approach for CVA (SA-CVA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 852): "a b SA-CVA RWA Number of counterparties 1 Interest rate risk 2 Foreign exchange risk 3 Reference credit spread risk 4 Equity risk 5 Commodity risk 6 Counterparty credit spread risk 7 Total (sum of rows 1 to 6) Linkages across templates [CVA3:7/a] is equal to [OV1:10/a] if the ban"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 849): "23.2.1 CVA risk under the basic approach (BA-CVA): Template CVA1: The reduced basic approach for CVA (BA-CVA) Purpose: To provide the components used for the computation of RWA under the reduced BA-CVA for CVA risk."

## Lookup terms

`RWA market risk`, `market risk capital charge`, `trading book capital requirement`, `Pillar 1 capital requirement`, `overview of risk-weighted assets`, `standardised approach market risk`, `internal models approach`

#graphify/enriched #community/cva-&-counterparty-exposure
