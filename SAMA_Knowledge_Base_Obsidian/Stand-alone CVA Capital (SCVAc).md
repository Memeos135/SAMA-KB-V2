# Stand-alone CVA Capital (SCVAc)

Concept node for the stand-alone CVA capital charge (SCVAc), the counterparty-level CVA capital component computed under the basic approach (BA-CVA) before recognition of hedges, within SAMA's minimum capital requirements for counterparty credit risk and CVA risk. It feeds the aggregate CVA capital requirement that in turn affects total capital ratios, buffer stacking and the disclosure templates (including capital composition and capital distribution constraint disclosures) referenced in the linked Pillar 3 framework. Binds SAMA-licensed banks calculating regulatory capital on a consolidated and solo basis.

**Regimes:** banking prudential, governance/risk

## Sources

- `corpus/markdown/SAMA_EN_3487_VER1.md`
- `corpus/markdown/SAMA_EN_4283_VER1.md`

## Connections

### [[Exposure at Default (EAD)]] — `references` [EXTRACTED]
- **What this link tells you:** EAD is not only a credit risk output; it feeds the credit valuation adjustment capital calculation, where the stand-alone CVA capital per counterparty and the recognition of eligible hedges depend on the same exposure inputs. The reference reflects an obligation chain within one capital instrument: an EAD determination made for CCR purposes carries through to the CVA charge for counterparties in scope. Consequently, a revision to EAD methodology or to netting and collateral treatment must be assessed for its effect on CVA capital as well, and the two should not be reviewed in isolation.
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 642): "The part of capital requirements that recognizes eligible hedges (𝐾ℎ𝑒𝑑𝑔𝑒𝑑) is calculated formulas follows (where the summations are taken over all counterparties c that are within scope of the CVA charge), where: (1) Both the stand-alone CVA capital (SCVAc) and the correlation pa"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 798): "Table CR2: Changes in stock of defaulted loans and debt securities Purpose: Identify the changes in a bank's stock of defaulted exposures, the flows between non-defaulted and defaulted exposure categories and reductions in the stock of defaulted exposures due to write-offs."

### [[Internal Models Method (IMM)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 642): "The part of capital requirements that recognizes eligible hedges (𝐾ℎ𝑒𝑑𝑔𝑒𝑑) is calculated formulas follows (where the summations are taken over all counterparties c that are within scope of the CVA charge), where: (1) Both the stand-alone CVA capital (SCVAc) and the correlation pa"
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 891): "* RWA and capital requirements under the Standardised Approach for credit risk weighting are to be subdivided in the standardised approach for counterparty credit risk (SA-CCR) and the internal models method (IMM), and the same for RWA and capital requirements under the internal "

### [[Reduced BA-CVA]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 849): "23.2.1 CVA risk under the basic approach (BA-CVA): Template CVA1: The reduced basic approach for CVA (BA-CVA) Purpose: To provide the components used for the computation of RWA under the reduced BA-CVA for CVA risk."
- **Grounding — related node** (SAMA_EN_3487_VER1 · Page 849): "23.2.1 CVA risk under the basic approach (BA-CVA): Template CVA1: The reduced basic approach for CVA (BA-CVA) Purpose: To provide the components used for the computation of RWA under the reduced BA-CVA for CVA risk."

### [[Reduced Version BA-CVA (Kreduced)]] — `references` [EXTRACTED]
- **Grounding — this node** (SAMA_EN_3487_VER1 · Page 849): "23.2.1 CVA risk under the basic approach (BA-CVA): Template CVA1: The reduced basic approach for CVA (BA-CVA) Purpose: To provide the components used for the computation of RWA under the reduced BA-CVA for CVA risk."
- **Grounding — related node** (SAMA_EN_4283_VER1 · Page 93): "The part of capital requirements that recognizes eligible hedges (𝐾ℎ𝑒𝑑𝑔𝑒𝑑) is calculated formulas follows (where the summations are taken over all counterparties c that are within scope of the CVA charge), where: (1) Both the stand-alone CVA capital (SCVAc) and the correlation pa"

## Lookup terms

`SCVAc`, `stand-alone CVA capital`, `BA-CVA`, `CVA risk capital requirement`, `reduced version BA-CVA`, `counterparty credit risk capital`, `CET1 capital ratio`, `capital distribution constraints`

#graphify/enriched #community/cva-&-counterparty-exposure
