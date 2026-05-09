# Banking sector overlay — concentration-risk-review

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-specific concentration framings the generic skill does not own.

## Hyperscaler-on-bank concentration

- **Large-bank cloud concentration**. Public OCC supervisory practice has framed hyperscaler concentration as a risk-appetite item for $50B-and-above covered banks under 12 CFR Part 30 Appendix D §III risk-governance framework [verify subsection labels]. Treat the hyperscaler dimension as a board-level concentration once it crosses the firm's own risk-appetite threshold; the supervisory expectation is that the firm has a number, not just a narrative.
- **Sub-region concentration within a single hyperscaler**. The FFIEC Joint Statement on cloud (April 2020) reads concentration not just at the hyperscaler level but at the region and sub-region level [verify section]. Multi-region promises documented in contracts do not equal multi-resilience for control-plane outages, identity-layer outages, or shared-billing outages; the substitutability read names what fails together.
- **Hidden hyperscaler concentration via SaaS vendors**. Many SaaS arrangements that look like distinct vendors share a hyperscaler footprint. The fourth-party dimension surfaces this; the technology-stack-hyperscaler dimension reads it back through the cross-arrangement lens.

## Sponsor-bank-on-fintech concentration (the BaaS dimension at the bank end)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date] [verify section]. For sponsor banks, concentration on a small set of programme partners (each carrying many end-user fintechs and substantial deposit balances) is a well-supervised concentration. The dimension reads as `sponsor-bank-baas` from the sponsor bank's side and as `single-vendor` from a partner-fintech-using-the-sponsor side.
- **End-customer reconciliation and FBO subledger concentration**. The supervisory expectation is that the sponsor bank can produce a portfolio-level view of partner-programme dependencies; this skill is the structured artifact that view sits in.

## Community-bank fintech-partner concentration

- **Joint statement on community-bank fintech due diligence** (OCC / FRB / FDIC, August 27, 2021) [verify exact title and date] [verify section]. For community banks, single-fintech-partner concentration carrying multiple critical functions (deposits, lending, payments) is a recognised supervisory concern. The dimension reads as `single-vendor` with a function-spread sub-finding; recommend a function-by-function diversification view in the recommended actions.

## Bank Service Company Act and the regulator-access posture

- **Bank Service Company Act, 12 USC §1867(c)**. Statutory examiner-access right over bank service providers. The supervisory expectation is that the bank can produce, on request, a portfolio view of bank service providers; the structured record from this skill is the artifact that supports that ask.

## ICT-third-party concentration where the firm is a EU subsidiary of a US BHC

- **Cross-frame layering**. A US BHC with EU banking subsidiaries: the EU subsidiary's concentration view is shaped by DORA Article 29 preliminary assessment requirements; the BHC's own consolidated TPRM consumes the EU subsidiary's view as input but is not bound by the EU regime for its own arrangements outside DORA scope. Two views, one underlying truth in the firm's TPRM data.
- **UK PRA SS2/21 dimension** for groups with a UK PRA-regulated bank: the UK overlay applies at the UK entity; this skill's substantive concentration framings align with the EBA outsourcing-guideline concentration limb across both regimes.

## Output-template additions for banking

- Risk-governance-framework cascade: a row showing how the concentration finding maps to the firm's risk-appetite and to the board-level reporting cycle for $50B-and-above covered banks.
- Sponsor-bank programme-partner concentration view (where applicable).
- Hyperscaler-by-region-and-sub-region read with explicit substitutability under shared-control-plane and shared-identity-layer scenarios.

## Common pitfalls in banking concentration reviews

- Reading hyperscaler concentration as a single number without the sub-region breakdown.
- Treating multi-region as multi-resilience by default.
- For sponsor banks, undercounting the concentration carried by a small number of programme partners with disproportionate deposit balances and end-user counts.
- For community banks, missing the function-spread carried by a single fintech partner.
- Skipping the BHC-vs-EU-subsidiary view layering and producing a single concentration view that blurs both regimes.
