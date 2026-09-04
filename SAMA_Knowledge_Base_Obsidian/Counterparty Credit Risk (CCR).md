# Counterparty Credit Risk (CCR)

Concept node for Counterparty Credit Risk — the risk that a counterparty defaults before final settlement where there is bilateral risk of loss — under SAMA's minimum capital requirements framework for CCR and CVA, including related risks such as rollover risk and general/specific wrong-way risk. It also anchors the Pillar 3 rows where CCR RWA and capital charges are reported separately from general credit risk. Binds banks, with quarterly Q17 reporting to SAMA within 30 days of quarter-end and effect from 1 January 2023.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[Basel III Framework]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Central Counterparty (CCP)]] — `references` [EXTRACTED]
- **What this link tells you:** Whether a trade is cleared through a central counterparty changes the counterparty credit risk analysis, because the CCP becomes the relevant counterparty and a distinct treatment applies to cleared exposures and default fund contributions. The CCR rules and the CCP provisions therefore operate on the same exposure but assign different capital consequences depending on clearing status and CCP qualification. The reader should establish the clearing arrangement and the CCP's status first, since that classification drives which capital treatment, and which CVA consequences, apply.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 654): "For example, when hedging the counterparty credit spread component of CVA risk for a specific counterparty by buying credit protection on the counterparty: if the counterparty’s credit spread widens, the CVA (expressed as a positive value) increases resulting in the positive CVA "

### [[Credit Valuation Adjustment (CVA)]] — `conceptually_related_to` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 560): "Credit valuation adjustment A credit valuation adjustment that reflects the market value of the credit risk of the counterparty to the firm, but does not reflect the market value of the credit risk of the bank to the counterparty."
- **Caveat:** Relation is a similarity heuristic, not a cross-reference.

### [[Internal Models Method (IMM)]] — `references` [EXTRACTED]
- **What this link tells you:** Deciding how to measure counterparty credit risk exposure turns on whether the bank uses the internal model method or a standardised alternative, so the two instruments must be read together. IMM is a permitted approach within the CCR regime, and the disclosure architecture recognises it separately, including a dedicated flow statement of CCR RWA determined under IMM for derivatives and securities financing transactions. Consequence: banks on IMM inherit both the CCR exposure rules and the additional IMM-specific conditions and reporting lines; those not approved for IMM should not populate IMM-based outputs.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 826): "Template CCR7: RWA flow statements of CCR exposures under Internal Model Method (IMM) Purpose: Present a flow statement explaining changes in counterparty credit risk RWA determined under the Internal Model Method for counterparty credit risk (derivatives and SFTs)."

### [[Minimum Capital Requirements for CCR and CVA]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 89): "However, all banks using the BA-CVA must calculate the reduced version of BA-CVA capital Version Minimum Capital Requirements for Counterparty Credit Risk (CCR) and 89 of 145 Issue Date December 2022 Page Number Credit Valuation Adjustment (CVA) 1.1"

### [[Netting Set]] — `references` [EXTRACTED]
- **What this link tells you:** Any determination of counterparty credit risk exposure depends first on how transactions are grouped into netting sets, since the CCR calculation is performed at netting-set level. The netting set definition also governs how collateral is recognised, including collateral held outside a set but available against defaults on that set only, which is treated as independent collateral in the replacement cost step. In practice the reader must confirm netting set boundaries and legal enforceability of netting before relying on any reduced CCR exposure figure.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"

### [[SA-CCR for OTC Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** If you are determining counterparty credit risk exposure, the general CCR provisions do not stand alone: SA-CCR is the prescribed default measurement method for OTC derivatives, exchange-traded derivatives and long settlement transactions where the bank lacks approval for the internal model method. The CCR chapter sets the scope and definitions; SA-CCR supplies the exposure calculation that gives those obligations effect within the same SAMA framework. The consequence is that absence of IMM approval is decisive — the firm must default to SA-CCR rather than treat measurement method as a matter of internal choice.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 567): "The Standardized Approach for Counterparty Credit Risk (SA-CCR) applies to over the-counter (OTC) derivatives, exchange-traded derivatives and long settlement transactions.5 Banks that do not have approval to apply the internal model method (IMM) for the relevant transactions mus"

## Lookup terms

`counterparty credit risk`, `CCR`, `CVA`, `SA-CCR`, `wrong-way risk`, `rollover risk`, `Q17 reporting template`, `bilateral risk of loss`

#graphify/enriched #community/basel-capital-requirements
