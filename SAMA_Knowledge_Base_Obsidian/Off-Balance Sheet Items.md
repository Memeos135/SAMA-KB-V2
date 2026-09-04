# Off-Balance Sheet Items

Concept node covering off-balance sheet items as they enter regulatory credit risk measurement and Pillar 3 disclosure, notably in the CR1 credit quality of assets template where gross carrying values must include guarantees given (maximum callable amount) and irrevocable loan commitments, gross of credit conversion factors and credit risk mitigation, with revocable commitments excluded. It also feeds the reconciliation of accounting to regulatory consolidation categories in the disclosure templates. Binds all banks subject to SAMA's disclosure and capital adequacy framework.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[Counterparty Credit Risk Framework]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 53): "Off-balance sheet items 7.86 Off-balance sheet items will be converted into credit exposure equivalents through the use of credit conversion factors (CCF)."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 48): "Exposures that give rise to counterparty credit risk 7.94 For exposures that give rise to counterparty credit risk according to paragraph 5.3 in The Counterparty Credit Risk (CCR) Framework (i.e."

### [[Credit Conversion Factors (CCF)]] — `references` [EXTRACTED]
- **What this link tells you:** Off-balance sheet items are not risk-weighted directly; the provision requires them first to be converted into credit exposure equivalents using credit conversion factors, so the two sections operate as a mandatory two-step calculation. The link is an express internal cross-reference in the same instrument, with the CCF rule defining the mechanism and the off-balance sheet section defining the population. In practice, a review of credit RWA must test both the completeness of the off-balance sheet inventory and the correctness of the CCF assigned to each item type; an error in either step propagates to the capital ratio.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 53): "Off-balance sheet items 7.86 Off-balance sheet items will be converted into credit exposure equivalents through the use of credit conversion factors (CCF)."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 53): "Off-balance sheet items 7.86 Off-balance sheet items will be converted into credit exposure equivalents through the use of credit conversion factors (CCF)."

### [[Leverage Ratio Exposure Measure]] — `references` [EXTRACTED]
- **What this link tells you:** When a bank determines the denominator of its leverage ratio, it cannot stop at balance-sheet, derivative and SFT positions: the exposure measure provision expressly enumerates off-balance sheet exposures as a fourth component and therefore pulls in the off-balance sheet items section as the operative treatment. The link is a direct internal cross-reference within the same SAMA capital framework instrument, so the two provisions form a single obligation chain rather than parallel rules. Practically, any assessment of leverage ratio compliance must apply the off-balance sheet measurement rules; omitting commitments, guarantees or similar items understates the exposure measure and overstates the ratio.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 699): "5.4 Exposure measure should include the following exposures: (i) On-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures); (ii) Derivative exposures; (iii) Securities financing transaction (SFT) exposures; and (iv) Off-bala"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 700): "Banks meeting these conditions must include any retained securitization exposures in their leverage ratio exposure measure.In all other cases, traditional securitizations exposures that do not meet the operational requirements for the recognition of risk transference or synthetic"

### [[SA-CCR for OTC Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** The off-balance sheet EAD rules expressly carve out derivatives, which is a scope boundary rather than a gap: derivative exposures are measured under SA-CCR (or IMM where approved) instead of the foundation or advanced off-balance sheet approaches. Both provisions belong to the same SAMA capital framework, so the carve-out only makes sense read against the SA-CCR chapter. For a decision, the practical step is to classify the instrument first — misclassifying a derivative as a general off-balance sheet item would apply the wrong EAD methodology.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 133): "Exposure measurement for off-balance sheet items (with the exception of derivatives) 12.31 For off-balance sheet items there are two approaches for the estimation of EAD: a foundation approach and an advanced approach."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 133): "Exposure measurement for off-balance sheet items (with the exception of derivatives) 12.31 For off-balance sheet items there are two approaches for the estimation of EAD: a foundation approach and an advanced approach."

## Lookup terms

`off-balance sheet exposures`, `guarantees given`, `irrevocable loan commitments`, `gross carrying value`, `Template CR1 credit quality of assets`, `Pillar 3 disclosure`, `regulatory consolidation`

#graphify/enriched #community/fund-investment-exposures
