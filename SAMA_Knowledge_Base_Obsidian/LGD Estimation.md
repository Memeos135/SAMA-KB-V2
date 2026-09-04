# LGD Estimation

This node covers loss given default (LGD) determination under the IRB approach in SAMA's minimum capital requirements for credit risk, including how LGD for a collateralised transaction is split between the unsecured and collateralised portions after haircuts, and the supervisory LGD parameter floors for corporate exposures by collateral type (with sovereign exposures excluded). It also sets how the floor is pro-rated for partially secured exposures. It binds SAMA-supervised banks using foundation or advanced IRB models for regulatory capital.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3502_VER1.md`

## Connections

### [[Definition of Loss]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 117): "12.10 The LGD applicable to a collateralized transaction (LGD*) must be calculated as the exposure weighted average of the LGD applicable to the unsecured part of an exposure (LGDU) and the LGD applicable to the collateralized part of an exposure (LGDS)."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 541): "Specific criteria on loss data identification, collection and treatment: 9.1 Building of the standardized approach loss data set: In order to build an acceptable loss data set from the available internal data, a bank must develop policies and procedures to address several feature"

### [[Risk Quantification]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3502_VER1 · Page 117): "12.10 The LGD applicable to a collateralized transaction (LGD*) must be calculated as the exposure weighted average of the LGD applicable to the unsecured part of an exposure (LGDU) and the LGD applicable to the collateralized part of an exposure (LGDS)."
- **Grounding — related node** (SAMA_EN_3502_VER1 · Page 168): "Risk-weighted assets for default risk 14.2 For receivables belonging unambiguously to one asset class, the IRB risk weight for default risk is based on the risk-weight function applicable to that particular exposure type, as long as the bank can meet the qualification standards f"

## Lookup terms

`LGD`, `loss given default`, `LGD floor`, `LGD*`, `collateralised exposure`, `IRB approach`, `haircut`, `unsecured LGD`, `credit risk mitigation`

#graphify/enriched #community/irb-risk-parameter-estimation
