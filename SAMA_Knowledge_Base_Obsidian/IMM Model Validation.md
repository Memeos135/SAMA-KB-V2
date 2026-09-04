# IMM Model Validation

Node covering SAMA's validation expectations for internal models used in counterparty credit risk (IMM/EPE models) and, in the market risk context, for risk-factor modellability under the expected shortfall framework. It sets out that banks must backtest exposure models across horizons matching trade maturities, benchmark pricing models independently, reassess parameter-update frequency, and correct discrepancies between realised and forecast exposures, with SAMA able to impose additional capital or deem data unsuitable pending remediation. Binds SAMA-licensed banks that have or seek approval to use internal models for regulatory capital.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`

## Connections

### [[Backtesting]] — `conceptually_related_to` [INFERRED]
- **What this link tells you:** For a decision on whether a bank's internal model remains fit for regulatory capital purposes, validation requirements and backtesting outcomes are best assessed as complementary evidence rather than separate exercises. Validation covers the approaches, assumptions and benchmarks used to test a model, while bank-wide backtesting supplies the quantitative exception counts and zone classification that can trigger supervisory consequences such as multiplier increases or model restrictions. This linkage is inferred from subject matter rather than an express cross-reference, so the reader should verify in the primary texts whether backtesting is formally incorporated into the validation obligation or stands as a distinct requirement.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 843): "(E) Validation of models and modelling processes (a) The approaches used in the validation of the models and modelling processes, describing general approaches used and the types of assumptions and benchmarks on which they rely."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 525): "Bank-wide backtesting Statistical considerations in defining the backtesting zones 16.9 To place the definitions of three zones of the bank-wide backtesting in proper perspective, however, it is useful to examine the probabilities of obtaining various numbers of exceptions under "
- **Caveat:** Link is inferred, not stated in the text — verify the primary instrument before relying on it. Relation is a similarity heuristic, not a cross-reference.

### [[Internal Models Method (IMM)]] — `references` [EXTRACTED]
- **What this link tells you:** Use of the internal model method is not a free methodological choice — it is conditional on the model validation and governance requirements attaching to it. The link is an obligation chain: the IMM exposure model must be validated and controlled, and model or methodology and policy changes are tracked as distinct drivers of RWA movement in the IMM-specific reporting rows. Consequence: any change to the IMM exposures model has both a validation consequence and a disclosure consequence, and unvalidated model changes undermine the bank's entitlement to IMM treatment.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 897): "Row 4 (Model updates – IMM only) and row 5 (Methodology and policy – IMM only) are specifically to include only model and methodology/policy changes relating to the IMM exposures model."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 897): "Row 4 (Model updates – IMM only) and row 5 (Methodology and policy – IMM only) are specifically to include only model and methodology/policy changes relating to the IMM exposures model."

## Lookup terms

`IMM model validation`, `EPE model backtesting`, `internal models method approval`, `risk factor eligibility test (RFET)`, `non-modellable risk factor (NMRF)`, `expected shortfall model`, `pricing model benchmarking`, `counterparty credit risk model`

#graphify/enriched #community/internal-models-approach
