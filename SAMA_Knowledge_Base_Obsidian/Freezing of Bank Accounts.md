# Freezing of Bank Accounts

Node addressing restriction and suspension of activity on bank accounts, drawing on the inoperative-account rules that limit withdrawals and transfers once an account is classified dormant, unclaimed or abandoned, and on the constraints banks face regarding balances in those accounts. Sets who may transact on a restricted account (customer in person, legal agent, heirs' agent or authorised signatory for juristic persons, with defined exceptions for electronic channels), the dual-supervision requirement for reactivation, and the prohibition on banks disposing of balances. Binds banks; should be read alongside the disclosure and enforcement node for blocking imposed at SAMA's instruction.

**Regimes:** banking prudential, consumer protection, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_1644_VER1.md`

## Connections

### [[Electronic Record System]] — `shares_data_with` [INFERRED]
- **What this link tells you:** When deciding whether an account must be frozen because identification documents have lapsed, the bank is relying on the same customer identity data it is required to hold in the unified electronic registration system for bank accounts. Both provisions sit within the same account rules: the freezing rule presupposes that ID validity and expiry status are captured and maintained in the electronic record built on the prescribed classification. Practically, defects or gaps in the electronic record translate directly into failures to freeze on time, so the two should be assessed as one control chain rather than separate duties. This linkage is inferred from the shared instrument rather than an explicit cross-reference, so verify the primary text before relying on it.
- **Grounding — this node** (SAMA_EN_1644_VER1 · Page 10): "Freezing of Bank Accounts Upon Expiration of Identification Documents: 3.1 Freezing of bank accounts: As a rule between banks and customers, the relationship must start and continue under valid identification documents and IDs for all transactions, whether those covered by the de"
- **Grounding — related node** (SAMA_EN_1644_VER1 · Page 9): "Electronic Record: For the purpose of setting up a unified electronic database for bank accounts, all banks shall establish an electronic registration system in accordance with the classification set forth in Appendix (C) and its updates and based on the information provided in t"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it.

### [[Inoperative Accounts (DormantUnclaimedAbandoned)|Inoperative Accounts (Dormant/Unclaimed/Abandoned)]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** When a bank decides how to treat a customer account with no recent activity, these provisions of the same rules operate as a single sequenced framework rather than distinct regimes. The inoperative-account provisions set the defined stages and time thresholds — active, dormant, then unclaimed after the stated period from the last recorded debit transaction or documented contact — and the freezing provisions determine the restrictions and handling that follow once a stage is reached. The consequence is that any freeze or restriction must be justified by reference to the correct stage and its trigger date, and reclassification of an account changes the permitted actions; misclassifying the stage exposes the bank to both consumer-protection and operational findings.
- **Grounding — this node** (SAMA_EN_1644_VER1 · Page 15): "5.2 Durations, periods and requirements for dealing with inoperative accounts: 5.2.1 Active accounts: Accounts shall be considered active if a debit transaction is carried out by a customer or his/her legal agent before a period of (24) months is completed."
- **Grounding — related node** (SAMA_EN_1644_VER1 · Page 16): "5.2.3 Unclaimed accounts: Accounts shall be considered unclaimed after completing five years (60 months), including the dormant phase, from the date of the last recorded debit transaction or reliable and documented correspondence, and the bank becoming unable to reach the custome"
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

### [[Rules for Bank Accounts]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_1644_VER1 · Page 10): "Freezing of Bank Accounts Upon Expiration of Identification Documents: 3.1 Freezing of bank accounts: As a rule between banks and customers, the relationship must start and continue under valid identification documents and IDs for all transactions, whether those covered by the de"
- **Grounding — related node** (SAMA_EN_1644_VER1 · Page 15): "5.2 Durations, periods and requirements for dealing with inoperative accounts: 5.2.1 Active accounts: Accounts shall be considered active if a debit transaction is carried out by a customer or his/her legal agent before a period of (24) months is completed."

## Lookup terms

`freezing accounts`, `blocking`, `account suspension`, `withdrawal restriction`, `dormant account activation`, `authorised signatory`, `dual supervision`

#graphify/enriched #community/bank-account-rules
