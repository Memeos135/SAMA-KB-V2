# RWA for Credit Risk

A concept node covering how risk-weighted assets and Pillar 1 capital requirements for credit risk are determined and reported in SAMA's Basel-aligned disclosure templates (overview of RWA and capital requirement rows). It sets out the split between the standardised approach and the internal ratings-based approaches (F-IRB, A-IRB and supervisory slotting), the treatment of credit risk mitigation using the simple or comprehensive approach with supervisory haircuts, and the phase-in for equity exposures where IRB use is being withdrawn. It also fixes the perimeter by excluding counterparty credit risk, CVA, equity positions, settlement risk, securitisation exposures and amounts below deduction thresholds, which are reported elsewhere. It binds banks subject to SAMA's capital adequacy and Pillar 3 disclosure framework.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4376_VER1.md`

## Connections

### [[Off-Balance Sheet Items (CCFs)]] — `references` [INFERRED]
- **What this link tells you:** For off-balance sheet commitments, guarantees and similar items, the reader must decide which conversion logic applies: the credit conversion factors used to derive risk-weighted assets, or the treatment prescribed for the leverage ratio exposure measure. Both regimes measure the same underlying exposures but serve different capital metrics, one risk-sensitive and one not, so the applicable CCFs and exclusions can diverge. Since the relationship here is inferred, treat it as a prompt to reconcile the two calculations rather than as an authority that one set of factors governs the other, and confirm against the primary text.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_4303_VER1 · Page 5): "5.4 Exposure measure should include the following exposures: (i) On-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures); (ii) Derivative exposures; (iii) Securities financing transaction (SFT) exposures; and (iv) Off-bala"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

### [[Output Floor Requirements]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 728): "Minimum risk-based capital requirements 3 Risk-weighted assets and Output Floor requirements 4 RWA for credit risk 5 RWA for market risk 6 RWA for operational risk 6 Calculation of the output floor 7 Version Issuance Date Page Number Output Floor Requirements 1.1 December 2022 2 "

### [[SCCR - Minimum Capital Requirements for CCR and CVA]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 779): "capital conservation buffer, G-SIB surcharge and countercyclical capital buffer) and Pillar 2 capital requirements (if CET1 capital is required); (ii) CET1 capital that banks must maintain to meet the minimum regulatory capital ratios and any CET1 capital used to meet Tier 1 capi"

### [[SCRE - Minimum Capital Requirements for Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When determining how credit risk RWA is measured for capital adequacy, the RWA provision does not stand alone: it points to the credit risk minimum capital requirements standard as the operative rulebook for exposure classes, risk weights and credit risk mitigation. The two sit in the same SAMA Basel capital hierarchy, with the RWA provision setting the calculation obligation and the credit risk standard supplying the substantive treatment. Consequently, any credit RWA number defended in a compliance or supervisory discussion must be traced back to the treatments in that standard, not to the RWA provision alone.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** When computing credit risk RWA for derivative and other counterparty exposures, you cannot treat the credit risk rules as self-contained: the exposure amount input is determined under the standardized approach for counterparty credit risk, which the credit risk framework cross-references directly (including the floor applied consistently across SA-CCR, the comprehensive approach to collateral within standardized credit risk, and the internal models method). Both sit in the same SAMA Basel-aligned capital hierarchy, so the defined terms and calibration in SA-CCR govern the counterparty exposure measure that the credit risk chapter then risk-weights. Practically, a capital calculation or validation decision must reconcile both instruments; applying credit risk weights to an exposure measured outside SA-CCR would understate or misstate the requirement.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"

## Lookup terms

`RWA credit risk`, `standardised approach credit risk`, `IRB approach F-IRB A-IRB`, `supervisory slotting approach`, `credit risk mitigation haircuts`, `equity exposures IRB phase-in`, `minimum capital requirement 8%`, `OV1 overview of RWA`

#graphify/enriched #community/basel-iii-post-crisis-reforms
