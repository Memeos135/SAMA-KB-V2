# Loss Given Default (LGD)

Concept node for Loss Given Default, the IRB risk component expressing the economic loss rate on a facility if the obligor defaults. The underlying material sets out the minimum requirements for banks permitted to use own-LGD estimates, including the downturn/long-run default-weighted average floor, treatment of dependence between borrower and collateral or guarantor risk, and currency mismatch; related context also covers loss data thresholds used in the operational risk capital calculation. It binds SAMA-licensed banks applying the advanced IRB approach and, for disclosure, banks completing Pillar 3 credit risk templates.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[F-IRB Collateral Recognition and LGD]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 124): "12.10 The LGD applicable to a collateralized transaction (LGD*) must be calculated as the exposure weighted average of the LGD applicable to the unsecured part of an exposure (LGDU) and the LGD applicable to the collateralized part of an exposure (LGDS)."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 117): "12.10 The LGD applicable to a collateralized transaction (LGD*) must be calculated as the exposure weighted average of the LGD applicable to the unsecured part of an exposure (LGDU) and the LGD applicable to the collateralized part of an exposure (LGDS)."

### [[Foundation and Advanced IRB Approaches]] — `references` [EXTRACTED]
- **What this link tells you:** When determining which loss-given-default figures a bank may use, the choice between the foundation and advanced IRB approaches is the controlling gate. The LGD provisions set out how a long-run default-weighted average loss rate is derived and how it interacts with the PD estimate, but the F-IRB/A-IRB scope provisions decide whether the bank supplies its own LGD or applies supervisory values. For a compliance decision, confirm the bank's approved approach first; that permission fixes the extent to which internal LGD estimation and its evidentiary requirements apply, including for counterparty credit risk exposures within the template's scope.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 177): "The bank may: (i) use an appropriate PD estimate to infer the long-run default- weighted average loss rate given default; or (ii) use a long-run default-weighted average loss rate given default to infer the appropriate PD."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 823): "Scope of application: The template is mandatory for banks using an advanced IRB (A-IRB) or foundation IRB (F-IRB) approach to compute RWA for counterparty credit risk exposures, whatever CCR approach is used to determine exposure at default."

### [[IRB Approach Overview|IRB Approach: Overview]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 177): "The bank may: (i) use an appropriate PD estimate to infer the long-run default- weighted average loss rate given default; or (ii) use a long-run default-weighted average loss rate given default to infer the appropriate PD."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 116): "LGD under the F-IRB approach: collateral recognition 12.8 In addition to the eligible financial collateral recognized in the standardized approach, under the F-IRB approach some other forms of collateral, known as eligible IRB collateral, are also recognized."

### [[IRB Risk Components (PD, LGD, EAD, M)]] — `references` [EXTRACTED]
- **What this link tells you:** For an IRB calculation, the LGD input is not free-standing judgement: the risk-components rule imports the dedicated LGD provision, including how LGD must be constructed where multiple loss sources (such as default and dilution risk) are covered by the same protection. This is a defined-term dependency inside the credit risk capital framework, so estimation, floors and any supervisory-set values in the referenced provision govern the number fed into the risk-weight function. Consequently, an LGD estimate that is defensible in model terms is still non-compliant if it departs from the referenced construction rules.
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 318): "a single reserve or overcollateralization is available to cover losses from either source) within a securitization, the LGD input must be constructed as a weighted average of the LGD for default risk and the 100% LGD for dilution risk.The weights are the stand-alone IRB capital c"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Treatment of Expected Losses and Provisions]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 177): "The bank may: (i) use an appropriate PD estimate to infer the long-run default- weighted average loss rate given default; or (ii) use a long-run default-weighted average loss rate given default to infer the appropriate PD."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 10): "IRB Approach: Treatment of expected losses and provisions 174 Calculation of expected losses 174 Calculation of provisions 175 Treatment of EL and provisions 176 16."

### [[Treatment of Guarantees and Credit Derivatives in IRB]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 177): "The bank may: (i) use an appropriate PD estimate to infer the long-run default- weighted average loss rate given default; or (ii) use a long-run default-weighted average loss rate given default to infer the appropriate PD."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 122): "Treatment of guarantees and credit derivatives 12.21 There are two approaches for recognition of credit risk mitigation (CRM) in the form of guarantees and credit derivatives in the IRB approach: a foundation approach for banks using supervisory values of LGD, and an advanced app"

## Lookup terms

`Loss Given Default`, `LGD`, `own-LGD estimates`, `downturn LGD`, `long-run default-weighted average loss rate`, `A-IRB risk components`, `collateral dependence`, `IRB minimum requirements`

#graphify/enriched #community/irb-credit-risk-disclosures
