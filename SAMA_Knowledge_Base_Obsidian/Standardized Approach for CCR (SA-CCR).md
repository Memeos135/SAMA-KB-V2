# Standardized Approach for CCR (SA-CCR)

This node sets out the Standardised Approach for Counterparty Credit Risk (SA-CCR), its scope over OTC derivatives, exchange-traded derivatives and long settlement transactions, and its mandatory use by banks without IMM approval. It also covers how CCR exposure (EAD) feeds into standardised or IRB credit risk RWA, exemptions where the CCR charge is zero (certain purchased credit protection and sold banking-book CDS), and the reference to minimum haircut floors for in-scope SFTs. It binds banks calculating CCR capital under SAMA's framework.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[Default Fund Contributions]] — `references` [EXTRACTED]
- **What this link tells you:** When a clearing member bank sizes capital for its default fund contribution to a CCP, the underlying trade exposures must be measured using the standardized approach for counterparty credit risk, so the two instruments must be read together rather than in isolation. The default fund methodology is a downstream calculation that takes SA-CCR exposure inputs (including applicable floors) as given, which makes SA-CCR the controlling measurement basis. Practically, any change in SA-CCR classification or parameters flows through to the default fund capital charge, and a compliance review of one should trigger review of the other.
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 629): "The second step in calculating the clearing member bank's capital requirement for its default fund contribution (𝐾𝐶𝑀𝑖) is to apply the following formula,34 where: (1) 𝐾𝐶𝑀𝑖 is the capital requirement on the default fund contribution of clearing member bank i (2) 𝐷𝐹𝐶𝑀𝑃𝑟𝑒𝑓 is the to"

### [[Derivative Exposures (Leverage Ratio)]] — `references` [EXTRACTED]
- **What this link tells you:** The leverage ratio exposure measure includes derivative exposures, and those exposures are measured using the counterparty credit risk methodology — SA-CCR for banks without internal model method approval — so the two provisions form a single measurement chain rather than parallel rules. A bank's IMM approval status therefore drives both its CCR capital calculation and the derivative component of its leverage ratio exposure measure. Confirm approval scope by transaction type before selecting the method, since an incorrect choice misstates both ratios simultaneously.
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 18): "The Standardized Approach for Counterparty Credit Risk (SA-CCR) applies to over the-counter (OTC) derivatives, exchange-traded derivatives and long settlement transactions.5 Banks that do not have approval to apply the internal model method (IMM) for the relevant transactions mus"
- **Grounding — related node** (SAMA_EN_4303_VER1 · Page 5): "5.4 Exposure measure should include the following exposures: (i) On-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures); (ii) Derivative exposures; (iii) Securities financing transaction (SFT) exposures; and (iv) Off-bala"

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** For derivative and other counterparty credit risk positions, EAD is not derived from the general credit-risk rules but from the SA-CCR (or, where approved, the internal models method), so the first decision is to classify the exposure type before choosing the EAD measure. The cross-reference is explicit: floors and equivalent constraints are set in parallel provisions of SA-CCR, the comprehensive approach under standardised credit risk, and IMM, so the same economic exposure must not be double-counted or measured on an inconsistent basis. The consequence is that any EAD reported for counterparty exposures should be traced back to the SA-CCR provisions and their floor, not to the general EAD text alone.
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."

### [[Margin Agreement RC Examples]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 19): "Margined netting sets are netting sets covered by a margin agreement under which the bank’s counterparty has to post variation margin; all other netting sets, including those covered by a one-way margin agreement where only the bank posts variation margin, are treated as unmargin"

### [[Minimum Capital Requirements for Credit Risk]] — `cites` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Netting Set]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"

### [[RWA for Credit Risk]] — `references` [EXTRACTED]
- **What this link tells you:** When computing credit risk RWA for derivative and other counterparty exposures, you cannot treat the credit risk rules as self-contained: the exposure amount input is determined under the standardized approach for counterparty credit risk, which the credit risk framework cross-references directly (including the floor applied consistently across SA-CCR, the comprehensive approach to collateral within standardized credit risk, and the internal models method). Both sit in the same SAMA Basel-aligned capital hierarchy, so the defined terms and calibration in SA-CCR govern the counterparty exposure measure that the credit risk chapter then risk-weights. Practically, a capital calculation or validation decision must reconcile both instruments; applying credit risk weights to an exposure measured outside SA-CCR would understate or misstate the requirement.
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

## Lookup terms

`SA-CCR`, `standardised approach counterparty credit risk`, `EAD netting set`, `internal model method IMM approval`, `CCR exemptions`, `sold credit default swap banking book`, `minimum haircut floors SFT`, `IRB maturity adjustment cap`

#graphify/enriched #community/sa-ccr-netting-sets
