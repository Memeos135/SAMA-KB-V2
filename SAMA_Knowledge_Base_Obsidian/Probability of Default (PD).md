# Probability of Default (PD)

Deals with probability of default as an IRB parameter and its supervisory validation, including the Pillar 3 backtesting template comparing modelled PD against realised default rates over at least a five-year average, and the related disclosure of movements in defaulted exposures. It also anchors the definition of a defaulted exposure (past due more than 90 days under the standardised approach, net of write-offs and gross of provisions). Mandatory for banks using F-IRB or A-IRB, with model-scope commentary obligations.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[Foundation and Advanced IRB Approaches]] — `references` [EXTRACTED]
- **What this link tells you:** The same approach-scope logic applies to probability of default: whether a bank uses its own PD estimates, and under what estimation and disclosure conditions, follows from its F-IRB or A-IRB permission for the relevant exposures. The linkage is at the level of the parameter chain (PD feeding RWA for counterparty credit risk exposures) rather than a specific numbered cross-reference, and the excerpt captured for the PD node concerns an unrelated basket default swap illustration. Treat this connection as directional guidance only and verify the primary PD provisions in the instrument before relying on it for a capital or disclosure decision.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 499): "In the example cited above, the capital requirement for a basket default swap covering defaults five to eight would be calculated as the sum of the capital requirements for a 5th- to-default swap, a 6th-to-default swap, a 7th-to-default swap and an 8th-to-default swap."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 823): "Scope of application: The template is mandatory for banks using an advanced IRB (A-IRB) or foundation IRB (F-IRB) approach to compute RWA for counterparty credit risk exposures, whatever CCR approach is used to determine exposure at default."

### [[IRB Approach Overview|IRB Approach: Overview]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 499): "In the example cited above, the capital requirement for a basket default swap covering defaults five to eight would be calculated as the sum of the capital requirements for a 5th- to-default swap, a 6th-to-default swap, a 7th-to-default swap and an 8th-to-default swap."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 116): "LGD under the F-IRB approach: collateral recognition 12.8 In addition to the eligible financial collateral recognized in the standardized approach, under the F-IRB approach some other forms of collateral, known as eligible IRB collateral, are also recognized."

### [[IRB Risk Components (PD, LGD, EAD, M)]] — `references` [EXTRACTED]
- **What this link tells you:** Deciding whether an IRB output is acceptable requires reading the risk-components rule together with the PD provision, which sets how default probability is defined, expressed and floored for use in the risk-weight function. The relationship is hierarchical and definitional: the components rule identifies PD as an input, the referenced provision supplies its regulatory meaning and units. For the reader, this means PD ratings and calibrations must be validated against the referenced definition of default and any minimum values, not merely against internal model performance.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 115): "Explanation of the risk-weight functions 11.2 Regarding the risk-weight functions for deriving risk weighted assets set out in this chapter: (1) Probability of default (PD) and loss-given-default (LGD) are measured as decimals (2) Exposure at default (EAD) is measured as currency"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Treatment of Expected Losses and Provisions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 499): "In the example cited above, the capital requirement for a basket default swap covering defaults five to eight would be calculated as the sum of the capital requirements for a 5th- to-default swap, a 6th-to-default swap, a 7th-to-default swap and an 8th-to-default swap."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 10): "IRB Approach: Treatment of expected losses and provisions 174 Calculation of expected losses 174 Calculation of provisions 175 Treatment of EL and provisions 176 16."

### [[Treatment of Guarantees and Credit Derivatives in IRB]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 499): "In the example cited above, the capital requirement for a basket default swap covering defaults five to eight would be calculated as the sum of the capital requirements for a 5th- to-default swap, a 6th-to-default swap, a 7th-to-default swap and an 8th-to-default swap."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 122): "Treatment of guarantees and credit derivatives 12.21 There are two approaches for recognition of credit risk mitigation (CRM) in the form of guarantees and credit derivatives in the IRB approach: a foundation approach for banks using supervisory values of LGD, and an advanced app"

## Lookup terms

`probability of default`, `PD backtesting`, `Template CR9`, `defaulted exposure definition`, `past due 90 days`, `stock of defaulted loans CR2`, `default rate validation`, `IRB model approval`

#graphify/enriched #community/irb-credit-risk-disclosures
