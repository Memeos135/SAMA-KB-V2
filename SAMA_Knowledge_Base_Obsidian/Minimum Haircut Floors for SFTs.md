# Minimum Haircut Floors for SFTs

Chapter-level rules setting minimum haircut floors for certain non-centrally cleared securities financing transactions (SFTs) with specified counterparties, including the in-scope transaction list, the floor percentages by collateral type and residual maturity, and the portfolio-level formula. It also defines the carve-outs: SFTs with central banks, qualifying cash-collateralized securities lending, and collateral upgrade trades where the received securities cannot be re-used. Binds SAMA-licensed banks calculating counterparty credit risk capital; it does not apply where a jurisdiction prohibits transacting below the floors.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[SFT Exposures (Leverage Ratio)]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When deciding how to treat a securities financing transaction, check both the capital-side haircut rules and the leverage ratio exposure measure, because the same SFT can be captured twice under different logics. The haircut floors sit in the credit risk mitigation / capital adequacy framework and govern collateral valuation and holding-period scaling, whereas the leverage ratio provisions determine whether and how the SFT is added to the exposure measure, without the same recognition of collateral. The link is inferred rather than an express cross-reference, so a firm should not assume a haircut recognised for capital purposes reduces the leverage exposure measure; verify the primary text of both instruments before concluding.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 85): "The 10-business day haircuts provided in paragraphs 9.49 to 9.50 are the default haircuts and these haircuts must be scaled up or down using the formula below, where: (1) H = haircut (2) H10 = 10-business day haircut for instrument (3) TM = minimum holding period for the type of "
- **Grounding — related node** (SAMA_EN_4303_VER1 · Page 6): "Banks meeting these conditions must include any retained securitization exposures in their leverage ratio exposure measure.In all other cases, traditional securitizations exposures that do not meet the operational requirements for the recognition of risk transference or synthetic"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

### [[SFT Exposures Treatment]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** These two provisions apply to the same transactions but answer different questions, so do not use one to satisfy the other. The minimum haircut floors and the holding-period scaling of supervisory haircuts govern how collateral is recognised for credit risk mitigation and risk-weighted asset purposes, whereas the SFT exposures treatment governs how securities financing transactions enter the leverage ratio exposure measure. The practical consequence is that a securities financing transaction must be assessed twice — once for haircut adequacy and RWA effect, once for leverage exposure — and the reader should verify the primary text for each, since this relationship is inferred rather than expressly cross-referenced.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 85): "The 10-business day haircuts provided in paragraphs 9.49 to 9.50 are the default haircuts and these haircuts must be scaled up or down using the formula below, where: (1) H = haircut (2) H10 = 10-business day haircut for instrument (3) TM = minimum holding period for the type of "
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 699): "5.4 Exposure measure should include the following exposures: (i) On-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures); (ii) Derivative exposures; (iii) Securities financing transaction (SFT) exposures; and (iv) Off-bala"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

## Lookup terms

`minimum haircut floors`, `securities financing transactions`, `SFT`, `repo-style transactions`, `collateral upgrade transaction`, `cash-collateralized securities lending`, `in-scope SFTs`, `shadow banking securities lending and repos`

#graphify/enriched #community/leverage-ratio-exposures
