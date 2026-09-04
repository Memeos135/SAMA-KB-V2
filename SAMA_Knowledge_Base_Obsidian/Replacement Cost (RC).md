# Replacement Cost (RC)

Concept node for Replacement Cost as a component of SA-CCR exposure at default, including the formula for margined trades using threshold, minimum transfer amount and net independent collateral amount, illustrated by worked margin-agreement examples. It also intersects with prudent valuation adjustment disclosure where fair-valued derivative positions are concerned. Relevant to banks calculating counterparty credit risk exposures under SA-CCR.

**Regimes:** banking prudential

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[Derivative Exposures Treatment]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 786): "10 Future administrative costs: PVAs to take into account the administrative costs and future hedging costs over the expected life of the exposures for which a direct exit price is not applied for the closeout costs."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 699): "5.4 Exposure measure should include the following exposures: (i) On-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures); (ii) Derivative exposures; (iii) Securities financing transaction (SFT) exposures; and (iv) Off-bala"

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** If you are fixing the counterparty credit risk exposure amount for a derivatives netting set, you cannot settle EAD without first settling replacement cost, because RC is one of the two components the standardised CCR measure is built from alongside potential future exposure. The link is a direct definitional dependency inside the same SAMA capital instrument, so the RC rules — including the conservative fallback where RC cannot be determined — govern the input rather than sitting beside it. Practically, an RC determination that is disputed or defaulted to the conservative proxy flows straight through to reported EAD, capital requirements and the related Pillar 3 credit-risk disclosures.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 334): "Whenever the replacement cost is unknown, the exposure measure for CCR will be calculated in a conservative manner by using the sum of the notional amounts of the derivatives in the netting set as a proxy for the replacement cost, and the multiplier used in the calculation of the"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."

### [[Margin Agreement RC Examples]] — `references` [EXTRACTED]
- **What this link tells you:** Before computing replacement cost for a derivative netting set, the bank must first decide whether that netting set is margined or unmargined, and that classification is governed by the margin-agreement provisions in the counterparty credit risk rules rather than by the replacement cost text alone. The two instruments sit in the same Basel-aligned SAMA capital framework and share the defined terms 'margined netting set' and 'variation margin', so the RC formula is only correctly applied once the counterparty's obligation to post variation margin is confirmed. The practical consequence is that a one-way arrangement in which only the bank posts margin cannot be treated as margined, which changes the RC formula used and therefore the reported exposure and capital outcome.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 692): "One example in which the replacement cost formula for margined trades can be applied is when the bank is a clearing member and is calculating replacement cost for its own trades with a central counterparty (CCP)."
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 19): "Margined netting sets are netting sets covered by a margin agreement under which the bank’s counterparty has to post variation margin; all other netting sets, including those covered by a one-way margin agreement where only the bank posts variation margin, are treated as unmargin"

### [[Net Independent Collateral Amount (NICA)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 596): "Eligible collateral which is taken outside a netting set, but is available to a bank to offset losses due to counterparty default on one netting set only, should be treated as an independent collateral amount associated with the netting set and used within the calculation of repl"

### [[SA-CCR for OTC Derivatives]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 334): "Whenever the replacement cost is unknown, the exposure measure for CCR will be calculated in a conservative manner by using the sum of the notional amounts of the derivatives in the netting set as a proxy for the replacement cost, and the multiplier used in the calculation of the"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 574): "The SA-CCR uses the following five asset classes: (1) Interest rate derivatives (2) Foreign exchange derivatives (3) Credit derivatives (4) Equity derivatives."

### [[Standard Margin Agreements RC Examples]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 692): "One example in which the replacement cost formula for margined trades can be applied is when the bank is a clearing member and is calculating replacement cost for its own trades with a central counterparty (CCP)."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 568): "Margined netting sets are netting sets covered by a margin agreement under which the bank’s counterparty has to post variation margin; all other netting sets, including those covered by a one-way margin agreement where only the bank posts variation margin, are treated as unmargin"

## Lookup terms

`replacement cost`, `RC`, `SA-CCR`, `margined trades`, `minimum transfer amount`, `MTA`, `threshold TH`, `NICA`, `variation margin`, `prudent valuation adjustment`

#graphify/enriched #community/sa-ccr-derivative-exposures
