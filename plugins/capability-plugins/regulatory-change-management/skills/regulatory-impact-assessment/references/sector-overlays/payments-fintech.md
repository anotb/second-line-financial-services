# Payments and fintech sector overlay — regulatory-impact-assessment

When the engagement scope flags payments or fintech and the rule touches non-bank consumer-finance providers, money transmitters, payment processors, prepaid issuers, BNPL providers, crypto-asset firms, neobanks operating under sponsor-bank arrangements, or bank-fintech partnerships, load this overlay alongside `references/source-anchors.md`. The overlay carries the CFPB larger-participant authority, the state-money-transmitter overlay, the bank-fintech partnership posture, and the strategy-lens posture for non-bank engagement.

## Institution-type and regulatory-frame scoping

Payments and fintech impact assessments turn on legal-entity type, activity, partnership structure, and licensing footprint:

- **Non-bank consumer-finance providers** (mortgage servicers, debt collectors, payday lenders, BNPL providers, larger participants in consumer-financial-product markets) under CFPB direct supervision per the larger-participant rule [verify Part 1090 subsection].
- **State-licensed money transmitters** under state money-transmitter statutes (state-by-state). The Conference of State Bank Supervisors (CSBS) Money Transmitter Modernization Act / Money Services Business Model Act is the harmonisation vehicle, with state-by-state adoption variance.
- **Federally registered MSBs** under FinCEN registration (31 CFR 1022) [verify subsection].
- **Sponsor-bank-arrangement fintechs**: a non-bank fintech offering a banking-like product (deposit account, debit card, payments capability) under a sponsor-bank's charter. The sponsor-bank carries the regulatory exposure; the fintech operates under contract.
- **Neobanks**: digital-only fintechs offering banking-like products, typically under sponsor-bank arrangements (very few have direct charters).
- **Payment processors and acquirers** under card-network rules (Visa, Mastercard, AmEx, Discover) and state money-transmission rules where applicable.
- **Prepaid card issuers** under Reg E (12 CFR Part 1005) [verify subsection], state money-transmission rules where applicable, and CFPB rules for prepaid accounts (12 CFR Part 1005 Subpart A) [verify subsection].
- **Crypto-asset firms** under federal frameworks (FinCEN MSB registration, SEC, CFTC depending on the asset's classification) and state-by-state money-transmitter and BitLicense-type rules.
- **Lending fintechs** under federal consumer-credit rules (TILA, Reg Z; ECOA, Reg B; FCRA; FDCPA) and state lending licensing rules.

## Threshold and tier semantics

The assessment's threshold determination reads against payments-and-fintech tier mechanics:

- **CFPB larger-participant thresholds**: the CFPB's larger-participant rule (12 CFR Part 1090) [verify subpart and section] sets activity-volume thresholds that bring non-bank firms under direct CFPB supervision (e.g., consumer reporting, debt collection, student loan servicing, automobile financing, international money transmission, BNPL where applicable; verify the most-recent larger-participant rule scope).
- **State money-transmitter licensing thresholds**: state-by-state money-transmitter statutes set activity-volume and net-worth thresholds for licensure.
- **FinCEN MSB registration thresholds**: 31 CFR 1010.100(ff) [verify subsection] sets the MSB definition; firms meeting the definition register with FinCEN.
- **Sponsor-bank tier**: sponsor-bank capital, asset size, and primary regulator drive the bank-side regulatory exposure that flows to the fintech under the partnership.
- **Card-network volume tiers**: Visa, Mastercard, and AmEx tier merchants and processors by transaction volume; tier-specific compliance expectations apply (PCI DSS Level 1 through 4).

## Named-policy and named-control patterns

Payments-and-fintech impact assessments routinely touch the named-policy areas below; the policy-impact section typically references one or more:

- **BSA-AML Programme** for the firm's MSB or money-transmitter scope under FinCEN rules (31 CFR 1022) and state requirements.
- **OFAC Sanctions Programme** for the firm's payments and customer-onboarding scope.
- **Reg E Programme** for consumer-error-resolution, provisional-credit, and unauthorised-EFT handling under 12 CFR Part 1005.
- **Reg Z Programme** for credit-card, BNPL-where-applicable, and lending disclosures under 12 CFR Part 1026.
- **TILA-RESPA Integrated Disclosure (TRID) Programme** for mortgage lenders.
- **FCRA Programme** for adverse-action, credit-reporting, and dispute handling.
- **FDCPA Programme** for collection activities (where applicable).
- **State Money Transmitter Licensing Programme**: state-by-state license maintenance, surety-bond compliance, net-worth covenants, consumer-protection rules.
- **Sponsor-Bank Partnership Programme** with the bank-side allocation pattern: which obligations the bank retains, which the fintech operates, and which are jointly executed. The June 2023 interagency third-party-risk guidance is the operative bank-side framework for the partnership.
- **Customer Identification Programme (CIP)** under 31 CFR 1020 (for bank partners) or 31 CFR 1022 (for the MSB) [verify subsection].
- **Cybersecurity Programme** anchored on PCI DSS, NYDFS Part 500 for NYDFS-licensed entities, and FFIEC IT Handbook expectations flowed down through sponsor-bank contracts.
- **Privacy Programme** anchored on the GLBA Privacy Rule, the GLBA Safeguards Rule, state privacy laws (CCPA / CPRA), and CFPB consumer-financial-data rules.
- **Dispute-Handling and Complaint-Management Programme** anchored on Reg E, Reg Z, CFPB complaint-tracking expectations, and card-network dispute rules.
- **Open Banking and Data Sharing Programme** under CFPB Section 1033 (12 CFR Part 1033) [verify final-rule citation, subsection, and effective date].

The assessment's policy-impact section names the policy area, the expected change type, and the rationale; the skill does not draft policy language.

## Reporting-impact patterns

Payments-and-fintech reporting touches:

- **FinCEN SAR and CTR** under 31 CFR 1022 (for MSBs), 1020 (for bank partners), 1023 (for broker-dealers in money-services activity).
- **State money-transmitter reports**: quarterly call reports, annual financial reports, transaction-volume reports under state statutes.
- **CFPB complaint-database reporting**: CFPB-supervised firms respond to consumer complaints in the CFPB consumer complaint database with response timing and documentation expectations.
- **Card-network operator reports**: chargeback ratios, fraud ratios, dispute-volume reports under network rules.
- **Prepaid card disclosures** under 12 CFR Part 1005 [verify subsection].
- **Section 1033 data-access reporting** under the CFPB open-banking rule [verify final-rule reporting requirements].
- **Sponsor-bank-issued reports**: the sponsor-bank's regulatory reports cover the bank-fintech-partnership program-level data; the fintech's contributions feed those reports.

## Sponsor-bank partnership posture

Bank-fintech partnerships carry a bank-side and fintech-side regulatory exposure pattern:

- **Bank-side allocation**: under the June 2023 interagency third-party-risk guidance, the sponsor-bank retains primary regulatory exposure for the partnership. The fintech operates under contract; the bank's regulator examines the fintech's operations through the bank's third-party-risk-management framework. Recent enforcement actions against sponsor banks (2023-2024) have raised the bar on bank-side oversight expectations, particularly around BSA-AML programme effectiveness, consumer-protection-rule adherence, and operational resilience.
- **Fintech-side direct exposure**: where the fintech holds direct CFPB supervision under the larger-participant rule, holds state money-transmitter licenses, or operates as an FinCEN-registered MSB, the fintech carries direct regulatory exposure for those frameworks alongside the sponsor-bank partnership.
- **Partnership documentation**: the master service agreement, the BSA-AML programme allocation, the consumer-protection-rule allocation, the data-handling allocation, and the exit-plan documentation are the operative partnership artifacts. Rule changes routinely require partnership-document refresh.
- **Sponsor-bank concentration risk**: where multiple sponsor-bank arrangements implicate similar customer bases or payment flows, the bank-side concentration-risk read drives partnership-portfolio decisions. A new rule that disproportionately affects sponsor-bank-arrangement fintechs (e.g., an AML rule expansion, a Section 1071 expansion to non-bank lenders under bank partnership) carries portfolio-level escalation.

## Strategy-lens posture for CFPB and state engagements

The payments-and-fintech strategy lens has identifiable patterns:

- **Industry-association alignment**: Financial Technology Association (FTA), American Fintech Council (AFC), Money Transmission Regulators Association (state-side), Financial Innovation Now (FIN) for payments and tech-sector engagement. Larger card networks engage through their own channels; merchant payments through the Merchant Risk Council; BNPL through trade-association working groups.
- **CFPB engagement convention**: the CFPB holds public listening sessions on significant rulemakings; non-bank firms engage through trade-association channels and as direct commenters. The CFPB's RFI (Request for Information) cycle precedes some rulemakings; the assessment reads RFI responses for industry posture signal.
- **State-by-state engagement**: state money-transmitter regulators engage through CSBS and through state-specific bulletins. The Money Transmission Modernization Act is the state-harmonisation vehicle; state-by-state adoption progresses unevenly.
- **Examiner-posture-shift signal**: CFPB Director speeches, CFPB Supervisory Highlights, OCC and FRB and FDIC interagency communications on bank-fintech partnerships, and NYDFS Industry Letters drive examiner-posture signal.
- **Sponsor-bank coordination**: where the rule affects the bank-fintech partnership, the fintech and the sponsor-bank coordinate the strategy posture. Comment letters on bank-fintech-partnership topics often run through both bank-side and fintech-side trade associations.
- **Escalation triggers**: For non-bank-supervised firms, escalation typically runs to the chief compliance officer, the head of legal, and the head of the partnership programme. For sponsor-bank-arrangement fintechs, the sponsor-bank's regulatory-affairs lead is a parallel escalation point. Items with state-by-state cumulative-cost implications or with sponsor-bank-partnership renegotiation implications escalate to the executive committee.

## Cost-to-comply patterns

Payments-and-fintech cost-to-comply reads typically calibrate against:

- **CFPB Economic Analysis** in the rule's adopting release (the CFPB prepares cost-and-benefit analyses under OMB Circular A-4).
- **State-by-state cumulative cost** for state-money-transmitter rule changes.
- **Trade-association cost-survey data**: FTA, AFC, MRA periodically publish cost-to-comply reads.
- **Prior-rule benchmarks**: the firm's prior cost-to-comply on prepaid-account-rule implementation, debt-collection-rule implementation (Reg F), or Section 1033 implementation serves as a benchmark.
- **Sponsor-bank contract pass-through**: where the rule increases the sponsor-bank's compliance burden, the bank's contractual pass-through to the fintech is a cost-to-comply input.

## When to escalate beyond regulatory-change-committee

For payments-and-fintech, the escalation triggers below typically fire:

- **Chief compliance officer**: any rule with a CFPB direct-supervision-scope implication; any rule with a state-money-transmitter-license implication.
- **Head of legal**: any rule requiring partnership-document refresh (master service agreement, programme agreement); any rule with a state-by-state legal-research implication.
- **Head of the partnership programme (sponsor-bank-arrangement fintechs)**: any rule affecting the bank-fintech-partnership allocation pattern.
- **Executive committee**: any rule with multi-state cumulative-cost implications; any rule with a strategic-product-decision implication (de-risk a product line, exit a state, restructure a partnership).
- **Board (where applicable for the fintech)**: any rule with strategic-business-model implications; any consent-order-pattern theme that names a peer fintech under similar product or partnership structure.

The escalation triggers are firm-specific; the overlay names the pattern, and `references/firm-overlay.md` overrides with firm-specific thresholds.
