# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — concentration-risk-review

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-specific concentration framings the generic skill does not own.

#### Hyperscaler-on-bank concentration

- **Large-bank cloud concentration**. Public OCC supervisory practice has framed hyperscaler concentration as a risk-appetite item for $50B-and-above covered banks under 12 CFR Part 30 Appendix D §III risk-governance framework [verify subsection labels]. Treat the hyperscaler dimension as a board-level concentration once it crosses the firm's own risk-appetite threshold; the supervisory expectation is that the firm has a number, not just a narrative.
- **Sub-region concentration within a single hyperscaler**. The FFIEC Joint Statement on cloud (April 2020) reads concentration not just at the hyperscaler level but at the region and sub-region level [verify section]. Multi-region promises documented in contracts do not equal multi-resilience for control-plane outages, identity-layer outages, or shared-billing outages; the substitutability read names what fails together.
- **Hidden hyperscaler concentration via SaaS vendors**. Many SaaS arrangements that look like distinct vendors share a hyperscaler footprint. The fourth-party dimension surfaces this; the technology-stack-hyperscaler dimension reads it back through the cross-arrangement lens.

#### Sponsor-bank-on-fintech concentration (the BaaS dimension at the bank end)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date] [verify section]. For sponsor banks, concentration on a small set of programme partners (each carrying many end-user fintechs and substantial deposit balances) is a well-supervised concentration. The dimension reads as `sponsor-bank-baas` from the sponsor bank's side and as `single-vendor` from a partner-fintech-using-the-sponsor side.
- **End-customer reconciliation and FBO subledger concentration**. The supervisory expectation is that the sponsor bank can produce a portfolio-level view of partner-programme dependencies; this skill is the structured artifact that view sits in.

#### Community-bank fintech-partner concentration

- **Joint statement on community-bank fintech due diligence** (OCC / FRB / FDIC, August 27, 2021) [verify exact title and date] [verify section]. For community banks, single-fintech-partner concentration carrying multiple critical functions (deposits, lending, payments) is a recognised supervisory concern. The dimension reads as `single-vendor` with a function-spread sub-finding; recommend a function-by-function diversification view in the recommended actions.

#### Bank Service Company Act and the regulator-access posture

- **Bank Service Company Act, 12 USC §1867(c)**. Statutory examiner-access right over bank service providers. The supervisory expectation is that the bank can produce, on request, a portfolio view of bank service providers; the structured record from this skill is the artifact that supports that ask.

#### ICT-third-party concentration where the firm is a EU subsidiary of a US BHC

- **Cross-frame layering**. A US BHC with EU banking subsidiaries: the EU subsidiary's concentration view is shaped by DORA Article 29 preliminary assessment requirements; the BHC's own consolidated TPRM consumes the EU subsidiary's view as input but is not bound by the EU regime for its own arrangements outside DORA scope. Two views, one underlying truth in the firm's TPRM data.
- **UK PRA SS2/21 dimension** for groups with a UK PRA-regulated bank: the UK overlay applies at the UK entity; this skill's substantive concentration framings align with the EBA outsourcing-guideline concentration limb across both regimes.

#### Output-template additions for banking

- Risk-governance-framework cascade: a row showing how the concentration finding maps to the firm's risk-appetite and to the board-level reporting cycle for $50B-and-above covered banks.
- Sponsor-bank programme-partner concentration view (where applicable).
- Hyperscaler-by-region-and-sub-region read with explicit substitutability under shared-control-plane and shared-identity-layer scenarios.

#### Common pitfalls in banking concentration reviews

- Reading hyperscaler concentration as a single number without the sub-region breakdown.
- Treating multi-region as multi-resilience by default.
- For sponsor banks, undercounting the concentration carried by a small number of programme partners with disproportionate deposit balances and end-user counts.
- For community banks, missing the function-spread carried by a single fintech partner.
- Skipping the BHC-vs-EU-subsidiary view layering and producing a single concentration view that blurs both regimes.

## capital-markets

### Capital-markets sector overlay — concentration-risk-review

When the scope flags capital markets, load this overlay alongside `references/source-anchors.md`. It carries the capital-markets-specific concentration framings the generic skill does not own.

#### Reg SCI concentration on critical SCI systems

- **Reg SCI (17 CFR §242.1000-1007)** [verify rule subpart]. SCI entities (national securities exchanges, registered clearing agencies, certain ATSs, plan processors, exempt clearing agencies) must assess third-party concentration as part of the SCI policies-and-procedures framework. The dimension reads as `single-vendor` and `function-level` with the SCI-system criticality cutoff. Substitutability read names that SCI-system substitution is heavily regulated and rarely fast.

#### Market-data and exchange-feed concentration

- A capital-markets firm may take consolidated tape, exchange feeds, and reference-data from a small set of vendors. Concentration on one consolidated-tape provider, one reference-data vendor for instrument identifiers, and one corporate-actions vendor is the standard pattern. The dimension reads as `technology-stack-shared-utility`; the substitutability read names that market-data vendor migration is contractually possible but operationally invasive (every downstream consumer must re-test).

#### Central-counterparty and clearing-member concentration

- For firms that clear through central counterparties, concentration on a small set of CCPs and a small set of clearing members is a recognised structural feature. The operational-third-party dimension this skill covers is the technology and connectivity-vendor concentration that supports access to those CCPs and clearing members, not the CCP-credit concentration itself (which sits with treasury and credit-risk teams).

#### Post-trade-processor and transfer-agent concentration

- A small set of post-trade processors and transfer agents covers most of the US capital-markets infrastructure. A firm whose recordkeeping, corporate-actions processing, and dividend-disbursement flows all sit on one transfer agent is concentration; the substitutability read names that transfer-agent migration is multi-year and disruptive to investor experience.

#### Adviser and fund compliance-program dimension

- **Investment Advisers Act Rule 206(4)-7**. The adviser must adopt and implement compliance policies reasonably designed to prevent violation of the federal securities laws; service-provider concentration is part of that adequacy assessment.
- **Investment Company Act Rule 38a-1(a)(4)**. Fund CCO must oversee the compliance program of each service provider to the fund. Where one service provider supports multiple funds in the complex, concentration reads as a fund-board-level item; recommended actions cluster for the fund board.
- **Investment Advisers Act Rule 206(4)-2 (Custody Rule)**. Where the firm uses one qualified custodian across multiple advisory products, concentration reads against the adviser's surprise-examination and account-statement-delivery obligations [verify section]. Custody-vendor migration is contractually possible but operationally heavy.

#### Reg S-P and the cyber lens

- **17 CFR Part 248 (Reg S-P) as amended May 16, 2024** [verify exact compliance dates by entity type and size]. Concentration in customer-information-safeguarding vendors (encryption, key-management, identity-and-access-management) reads in the cross-cutting cyber overlay.

#### Output-template additions for capital markets

- SCI-systems-row in the function-level dimension where the firm is an SCI entity.
- Market-data-vendor row in technology-stack-shared-utility.
- Transfer-agent and post-trade-processor row in single-vendor.
- Fund-board reviewer-question cluster where the engagement supports a fund complex.

#### Common pitfalls in capital-markets concentration reviews

- Conflating CCP-credit concentration with the operational-vendor concentration that supports CCP access. Two different reviews.
- Treating market-data-vendor concentration as a procurement question. It is an operational-resilience question because the downstream consumers are bound to the vendor's instrument-identifier and pricing conventions.
- Missing the fund-board-level reviewer cluster in fund-complex engagements. The fund board is a separate forum from the adviser's risk committee.
- Reading the SCI dimension narrowly as the named SCI systems without the third-party-vendor concentration that supports those systems.

## insurance

### Insurance sector overlay — concentration-risk-review

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. It carries the insurance-specific concentration framings the generic skill does not own.

#### Policy-administration system concentration

- A small set of policy-administration vendors covers most of the US carrier market. A carrier whose pricing, billing, claims, and renewal flows all sit on one PAS vendor is concentration even where the contract is sound. The dimension reads as `single-vendor` with a function-spread sub-finding; the substitutability read names that PAS migration is multi-year, expensive, and rarely fully rehearsed.

#### Claims-TPA concentration

- A property-and-casualty carrier may use one TPA across multiple lines of business; a workers'-compensation carrier may use one TPA for a substantial book. The TPA's own infrastructure (cloud, workflow vendor, sub-contracted adjusters) carries the concentration's downstream dependencies. The fourth-party dimension surfaces these; recommend a sub-contractor-chain re-ask in `vendor-diligence` where rank-2 visibility is thin.

#### Reinsurance and retrocession-vendor concentration

- Reinsurance counterparty concentration is a separate (and well-developed) discipline; this skill does not replicate the reinsurance-credit concentration view. It does cover the concentration in operational vendors that support reinsurance accounting, claims-recovery processing, and treaty administration. The line is: counterparty credit concentration sits with the actuarial and reinsurance teams; operational-vendor concentration that supports reinsurance flows sits here.

#### Holding-company filing dimension

- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and **Holding Company Model Regulation (Model #450)** [verify model number]. Form B and Form F filings carry the holding-company-level material-vendor concentration view across affiliates; the structured record from this skill is the supporting artifact for the operational-risk concentration items in Form F [verify Form F section reference]. State-by-state adoption.
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]. Critical outsourced functions and their concentration posture belong in the ORSA Summary Report; this skill's output is the input to the ORSA section that addresses operational-third-party concentration.

#### Analytics-vendor and ECDIS concentration in life and health

- **Colorado SB 21-169** and **NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting** (January 2024) [verify exact circular number] [verify section]. Where multiple lines of business depend on a single ECDIS or analytics-vendor, the concentration is read as `technology-stack-other` and as `ai-provider` where applicable. State-by-state adoption.

#### NAIC Bulletin on AI-vendor concentration

- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023). Carrier accountability for vendor and third-party AI extends to the concentration question: a carrier dependent on one AI vendor across pricing, claims, and underwriting use cases carries concentration the bulletin reads as part of the AIS Programme third-party-AI-accountability element. State-by-state adoption.

#### Output-template additions for insurance

- Form F and ORSA cross-reference for the holding-company filing dimension.
- Policy-administration-system row in the function-level dimension.
- Claims-TPA row with sub-contractor-chain visibility for the rank-2 disclosed adjuster network.
- AI-provider row read against the NAIC Bulletin AIS Programme expectations where AI is in scope.

#### Common pitfalls in insurance concentration reviews

- Confusing reinsurance counterparty credit concentration with operational-vendor concentration that supports reinsurance flows. Two different reviews, two different owners.
- Reading PAS concentration as a single-vendor finding without the function-spread sub-finding.
- Missing the ECDIS and analytics-vendor concentration in life and health where state-specific obligations apply.
- For AI vendors used across multiple lines, undercounting the AIS-Programme accountability dimension.
- Treating the structured record as the Form F filing or the ORSA section. The record is an input; the regulated filing has its own legal artifact.

## payments-fintech

### Payments and fintech sector overlay — concentration-risk-review

When the scope flags payments-fintech, load this overlay alongside `references/source-anchors.md`. It carries the payments and fintech-specific concentration framings the generic skill does not own.

#### Sponsor-bank concentration (the partner-fintech end of the BaaS dimension)

- A fintech that uses a single sponsor bank for deposit-product issuance carries concentration that is not optional in many products. The dimension reads as `sponsor-bank-baas`. The substitutability read names that sponsor-bank substitution is contractually possible but in practice constrained by the sponsor-bank market's small number of active programme banks, the supervisory posture toward new programmes (currently cautious in the post-2024 supervisory environment), and the operational difficulty of migrating end-user balances. A fintech with one sponsor bank for deposits and a second small sponsor bank for a lending product still carries elevated concentration on the deposit side.

#### BIN-sponsor concentration

- For card-issuing fintechs, the BIN sponsor is the regulatory and operational anchor; using one BIN sponsor for a single card programme is the norm and not by itself concentration, but using one BIN sponsor across multiple card programmes (consumer debit, business debit, credit, virtual) is concentration. The dimension reads as `bin-sponsor`. Substitutability read names that BIN re-issuance is operationally costly and customer-disruptive.

#### Payment-rails access concentration

- For a payments firm, access to the rails (FedNow, RTP, ACH, card networks, cross-border correspondent) sits behind a small set of vendor-of-record access points. Concentration on one ACH originator or one card-network gateway is the standard pattern; the dimension reads as `payment-rails`. Substitutability read names that rails-access substitution is contractually possible but operationally heavy and may require re-certification with the rails operator.
- **NACHA Operating Rules (current edition)** Third-Party Sender registration and risk-management rules carry concentration framing for ACH originators with multiple Third-Party Senders [verify rule citations]. Where the firm sits as a Third-Party Sender for multiple ACH originators, the concentration reads from the originator side as well.

#### Programme-partner concentration at a sponsor bank

- The mirror of the partner-fintech-end view: from the sponsor bank's side, concentration sits on a small set of programme-partner fintechs each carrying many end-users and meaningful deposit balances. Cross-loaded with the banking overlay where the firm is the sponsor bank.

#### MSB and PSP concentration

- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1022.380 (initial registration within 180 days of becoming an MSB; renewal every two years). MSB concentration on a single agent network or a single sub-MSB carries the BSA/AML supervisory focus; the dimension reads as `single-vendor` with a regulatory-posture sub-finding. Note: 31 CFR §1010.380 is the separate BOI / Corporate Transparency Act reporting rule, not the MSB-registration cite.
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state]. Where the rule applies, the supervisory frame for digital-payment-application providers reads concentration in the technology-stack and shared-utility dimensions.

#### Cross-border correspondent concentration

- For a cross-border payments firm, correspondent-bank access concentration is a structural feature. The dimension reads as `single-vendor` with a jurisdictional sub-finding (where the correspondent bank's jurisdiction concentrates the firm's sanctions and AML exposure). Substitutability read names that correspondent-bank substitution depends on the correspondent's risk-appetite for the firm's customer base and is not always available on demand.

#### Output-template additions for payments-fintech

- Sponsor-bank programme-partner row (from either side, depending on the firm's role).
- BIN-sponsor row in `bin-sponsor`.
- Payment-rails row with per-rail breakdown.
- ACH Third-Party Sender row where applicable.
- Cross-border correspondent row with jurisdictional sub-finding.

#### Common pitfalls in payments-fintech concentration reviews

- Treating sponsor-bank concentration as substitutable on procurement timelines. It is not.
- Reading BIN-sponsor concentration as one programme rather than across the firm's card-product set.
- Missing the ACH Third-Party Sender concentration when the firm sits as the originator's sender for multiple originators.
- Conflating MSB agent-network concentration with general single-vendor concentration. The BSA/AML supervisory frame applies and the recommended actions cluster for the BSA officer rather than the head of TPRM.
- Reading correspondent-bank substitutability against benign-conditions only. Stressed substitutability in correspondent banking is a known thin market.
