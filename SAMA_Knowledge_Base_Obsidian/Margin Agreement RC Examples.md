# Margin Agreement RC Examples

A node within SAMA's counterparty credit risk capital rules covering how margin agreements affect exposure measurement, including the replacement cost and potential future exposure components of SA-CCR (EAD = alpha × (RC + PFE)) and the internal model method treatment of margined netting sets. It sets out what an EPE model must capture (unilateral vs bilateral margin, call frequency, margin period of risk, thresholds, minimum transfer amounts) and the supervisory floors on the margin period of risk, including higher floors for large or illiquid-collateral netting sets. It binds banks calculating regulatory capital for counterparty credit risk on derivatives and repo-style transactions.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[Replacement Cost (RC)]] — `references` [EXTRACTED]
- **What this link tells you:** Before computing replacement cost for a derivative netting set, the bank must first decide whether that netting set is margined or unmargined, and that classification is governed by the margin-agreement provisions in the counterparty credit risk rules rather than by the replacement cost text alone. The two instruments sit in the same Basel-aligned SAMA capital framework and share the defined terms 'margined netting set' and 'variation margin', so the RC formula is only correctly applied once the counterparty's obligation to post variation margin is confirmed. The practical consequence is that a one-way arrangement in which only the bank posts margin cannot be treated as margined, which changes the RC formula used and therefore the reported exposure and capital outcome.
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 19): "Margined netting sets are netting sets covered by a margin agreement under which the bank’s counterparty has to post variation margin; all other netting sets, including those covered by a one-way margin agreement where only the bank posts variation margin, are treated as unmargin"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 692): "One example in which the replacement cost formula for margined trades can be applied is when the bank is a clearing member and is calculating replacement cost for its own trades with a central counterparty (CCP)."

### [[Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_4283_VER1 · Page 19): "Margined netting sets are netting sets covered by a margin agreement under which the bank’s counterparty has to post variation margin; all other netting sets, including those covered by a one-way margin agreement where only the bank posts variation margin, are treated as unmargin"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"

## Lookup terms

`margin agreement`, `margin period of risk`, `SA-CCR`, `replacement cost (RC)`, `potential future exposure (PFE)`, `netting set`, `EAD alpha 1.4`, `effective EPE`, `variation margin`, `counterparty credit risk`

#graphify/enriched #community/sa-ccr-netting-sets
