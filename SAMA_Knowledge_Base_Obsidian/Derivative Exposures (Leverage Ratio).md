# Derivative Exposures (Leverage Ratio)

Part of SAMA's leverage ratio framework dealing with how derivative exposures enter the leverage ratio exposure measure, including replacement cost plus add-on treatment, recognition (or non-recognition) of purchased credit protection such as total return swaps, and the option to exclude offset portions of written credit derivatives from the PFE netting set to avoid double counting. It also frames the boundary with securities financing transactions. It binds banks subject to SAMA's Basel III leverage ratio requirements.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_4303_VER1.md`

## Connections

### [[Aggregate Add-On (AddOn Aggregate)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4303_VER1 · Page 5): "5.4 Exposure measure should include the following exposures: (i) On-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures); (ii) Derivative exposures; (iii) Securities financing transaction (SFT) exposures; and (iv) Off-bala"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 24): "The formula for PFE is as follows, where: (1) AddOnaggregate⁡is the aggregate add-on component (see 6.27 below) (2) multiplier is defined as a function of three inputs: V, C and AddOnaggregate 𝑃𝐹𝐸= 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑒𝑟∗AddOnaggregate Multiplier (recognition of excess collateral and negativ"

### [[Leverage Ratio Exposure Measure]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4303_VER1 · Page 6): "Banks meeting these conditions must include any retained securitization exposures in their leverage ratio exposure measure.In all other cases, traditional securitizations exposures that do not meet the operational requirements for the recognition of risk transference or synthetic"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 700): "Banks meeting these conditions must include any retained securitization exposures in their leverage ratio exposure measure.In all other cases, traditional securitizations exposures that do not meet the operational requirements for the recognition of risk transference or synthetic"

### [[Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** The leverage ratio exposure measure includes derivative exposures, and those exposures are measured using the counterparty credit risk methodology — SA-CCR for banks without internal model method approval — so the two provisions form a single measurement chain rather than parallel rules. A bank's IMM approval status therefore drives both its CCR capital calculation and the derivative component of its leverage ratio exposure measure. Confirm approval scope by transaction type before selecting the method, since an incorrect choice misstates both ratios simultaneously.
- **Grounding — this node** (SAMA_EN_4303_VER1 · Page 5): "5.4 Exposure measure should include the following exposures: (i) On-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures); (ii) Derivative exposures; (iii) Securities financing transaction (SFT) exposures; and (iv) Off-bala"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 18): "The Standardized Approach for Counterparty Credit Risk (SA-CCR) applies to over the-counter (OTC) derivatives, exchange-traded derivatives and long settlement transactions.5 Banks that do not have approval to apply the internal model method (IMM) for the relevant transactions mus"

### [[Treatment of Cash Variation Margin]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4303_VER1 · Page 14): "7.2.4 Treatment of cash variation margin: (i) Treatment of derivative exposures for the purpose of the Leverage ratio exposure measure, the cash portion of variation margin exchanged between counterparties may be viewed as a form of pre- settlement payment if the following condit"
- **Grounding — related node** (SAMA_EN_4303_VER1 · Page 14): "7.2.4 Treatment of cash variation margin: (i) Treatment of derivative exposures for the purpose of the Leverage ratio exposure measure, the cash portion of variation margin exchanged between counterparties may be viewed as a form of pre- settlement payment if the following condit"

### [[Written Credit Derivatives Treatment]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4303_VER1 · Page 23): "7.2.15 Since written credit derivatives are included in the Leverage ratio exposure measure at their effective notional amounts, and are also subject to amounts for PFE, the Leverage ratio exposure measure for written credit derivatives may be overstated."
- **Grounding — related node** (SAMA_EN_4303_VER1 · Page 23): "7.2.15 Since written credit derivatives are included in the Leverage ratio exposure measure at their effective notional amounts, and are also subject to amounts for PFE, the Leverage ratio exposure measure for written credit derivatives may be overstated."

## Lookup terms

`leverage ratio exposure measure`, `derivative exposures`, `written credit derivatives`, `total return swap`, `effective notional amount`, `potential future exposure`, `Tier 1 capital deductions`, `prudent valuation adjustment`

#graphify/enriched #community/leverage-ratio-exposures
