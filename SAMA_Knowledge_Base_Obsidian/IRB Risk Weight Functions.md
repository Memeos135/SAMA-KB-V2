# IRB Risk Weight Functions

Covers the IRB risk-weight functions that convert risk components into risk-weighted assets, including the chapter structure for default and dilution risk on purchased receivables and the recognition of credit risk mitigants such as guarantees and first-loss collateral. It sets substitution rules where a guarantee covers default risk, dilution risk, or both, and points to securitisation treatment (SEC-IRBA) where mitigants act as first-loss protection. Relevant to banks calculating IRB capital requirements.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[Firm-Size Adjustment for MSMEs]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 10): "IRB Approach: Risk Weight Functions 108 Explanation of the risk-weight functions 108 Risk-weighted assets for exposures that are in default 109 Risk-weighted assets for corporate, sovereign and bank exposures that are not in default 109 12."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 111): "Firm-size adjustment for micro, small or medium-sized entities (MSMEs) 11.8 Under the IRB approach for corporate credits, banks will be permitted to separately distinguish exposures to MSME borrowers (defined as corporate exposures where the reported revenues for the consolidated"

### [[IRB Approach Overview|IRB Approach: Overview]] — `references` [EXTRACTED]
- **What this link tells you:** The IRB overview sets the eligibility, scope and structure of the internal ratings-based regime, while the risk weight functions supply the formulas that convert risk parameters into risk-weighted assets, including the separate treatment of defaulted exposures. Both sit in the same SAMA instrument, so the overview conditions when a bank may use the functions at all rather than offering an alternative basis. In practice a bank should first establish IRB permission and exposure classification under the overview, then apply the corresponding function; using the formulas outside the permitted scope would not be compliant.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 10): "IRB Approach: Risk Weight Functions 108 Explanation of the risk-weight functions 108 Risk-weighted assets for exposures that are in default 109 Risk-weighted assets for corporate, sovereign and bank exposures that are not in default 109 12."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 3): "IRB Approach: Risk Weight Functions 108 Explanation of the risk-weight functions 108 Risk-weighted assets for exposures that are in default 109 Risk-weighted assets for corporate, sovereign and bank exposures that are not in default 109 12."

### [[IRB Risk Components (PD, LGD, EAD, M)]] — `shares_data_with` [INFERRED]
- **What this link tells you:** Treat these as two halves of one capital calculation: the risk parameters a bank estimates for an IRB exposure class are the direct inputs to the supervisory risk-weight formulas, so a parameter validation weakness propagates straight into reported RWA and the capital ratio. The link is an obligation chain within SAMA's adoption of the Basel credit-risk framework rather than a free-standing cross-reference, so approval conditions or floors applied to parameter estimation constrain the formula output too. Because the connection here is inferred and the supplied extracts read like general glossary material, confirm against the primary IRB text which parameters and formulas apply to the specific exposure class before relying on this for a capital decision.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

## Lookup terms

`risk weight functions IRB`, `dilution risk RWA`, `credit risk mitigants IRB`, `guarantee substitution risk weight`, `SEC-IRBA`, `exposure-weighted LGD`, `purchase price discount receivables`

#graphify/enriched #community/exposure-asset-classes
