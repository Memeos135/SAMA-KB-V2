# Netting Set

Defined-term node for the netting set, the unit of aggregation used in SAMA's counterparty credit risk framework (SA-CCR) for computing replacement cost, potential future exposure add-ons and the treatment of collateral. It governs how trades under legally enforceable netting arrangements are grouped, how one margin agreement covering several netting sets is handled, and how collateral taken outside a netting set is recognised. It binds SAMA-licensed banks calculating regulatory capital for counterparty credit risk.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[Counterparty Credit Risk (CCR)]] — `references` [EXTRACTED]
- **What this link tells you:** Any determination of counterparty credit risk exposure depends first on how transactions are grouped into netting sets, since the CCR calculation is performed at netting-set level. The netting set definition also governs how collateral is recognised, including collateral held outside a set but available against defaults on that set only, which is treated as independent collateral in the replacement cost step. In practice the reader must confirm netting set boundaries and legal enforceability of netting before relying on any reduced CCR exposure figure.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 361): "Risk class: A defined list of risks that are used as the basis for calculating market risk capital requirements: general interest rate risk, credit spread risk (non-securitisation), credit spread risk (securitisation: non-correlation trading portfolio), credit spread risk (securi"

### [[Hedging Set]] — `conceptually_related_to` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"
- **Caveat:** Relation is a similarity heuristic, not a cross-reference.

### [[SA-CCR for OTC Derivatives]] — `references` [EXTRACTED]
- **What this link tells you:** Netting set is a defined term that determines the unit of account for SA-CCR, so the decision on how to group transactions and allocate collateral is made under the netting set provisions before any exposure figure is produced. Because collateral held outside a netting set but available against default on only that set is treated as independent collateral within the replacement cost calculation, misclassifying the netting perimeter directly changes the regulatory exposure amount. The reader should confirm the enforceability of the netting arrangement before relying on any netted SA-CCR result.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 567): "The Standardized Approach for Counterparty Credit Risk (SA-CCR) applies to over the-counter (OTC) derivatives, exchange-traded derivatives and long settlement transactions.5 Banks that do not have approval to apply the internal model method (IMM) for the relevant transactions mus"

### [[Standardized Approach for CCR (SA-CCR)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 71): "This floor is set out in 6.54(1) of the standardized approach for counterparty credit risk (SA- CCR), 9.60 of the Minimum Capital Requirements for Credit Risk of comprehensive approach within the standardized approach to credit risk and 7.24(1) of the internal models method (IMM)"

## Lookup terms

`netting set`, `SA-CCR`, `replacement cost`, `potential future exposure`, `PFE add-on`, `margin agreement`, `independent collateral amount`, `counterparty credit risk`

#graphify/enriched #community/sa-ccr-netting-sets
