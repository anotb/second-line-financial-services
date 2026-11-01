# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Sector overlay — banking

Loaded when the scope names banking (national bank, federal savings association, state-member bank, state non-member bank, holding company, federal branch). The overlay carries banking-specific implementation-plan conventions on top of the generic spine.

#### Heightened Standards posture

Banks meeting the asset thresholds in 12 CFR Part 30 Appendix D (Heightened Standards) carry an enterprise-wide risk governance framework that the regulatory-change programme reports up through. Implementation plans for material rule changes at a Heightened-Standards bank route through:

- the Risk Governance Framework as the enterprise context (the plan does not invent a parallel governance structure);
- the bank's Three-Lines-of-Defense framework with named first-line, independent risk-management, and internal audit roles;
- the board risk committee for oversight of material implementation programmes, with frequency of reporting calibrated to criticality.

For non-Heightened-Standards banks, the equivalent posture is the bank's risk governance arrangement under the OCC's general supervisory expectations or the FRB's SR letters on bank governance.

#### MRA and MRIA cadence

Implementation plans triggered by an MRA or MRIA inherit the agency-specific convention. Federal banking agencies (OCC, FRB, FDIC) share the MRA / MRIA two-tier mechanism. CFPB uses Matters Requiring Attention by parallel convention. The plan's effective date is the deadline the agency communicated in the supervisory letter or examination report; the plan's regulator-readiness checkpoints lead the deadline by enough margin for second-line review and any monitor confirmation.

Where a consent order is in place, the order's milestone schedule is the binding constraint and the implementation-plan milestones map one-to-one to the order's milestones. The independent monitor or compliance committee role named in the order is named in the plan's governance checkpoints. The order's reporting requirements (monthly, quarterly) drive the cadence; the plan does not under-govern relative to the order.

#### Capital-plan and CCAR/DFAST remediation

Where the rule change or remediation touches the capital plan (Reg YY enhanced prudential standards, capital plan rule, CCAR or DFAST-derived MRAs), the implementation plan integrates with the bank's annual capital-plan submission cycle. Milestones align to the FRB's SR 15-18 / SR 15-19 supervisory expectations on capital planning at large bank holding companies (or the equivalent state-member or community bank framework). The bank's capital working group is a governance checkpoint; the head of capital management is a workstream owner where the plan touches stress-testing, capital-actions, or the capital-adequacy process.

#### SR letters that frame governance

For a bank-side regulatory-change programme of material scope, the implementation plan reflects the FRB SR letters that frame supervision of governance, change management, and operational risk:

- SR 13-19 (Outsourcing) — third-party-touching elements of the implementation;
- SR 21-3 / OCC Bulletin 2021-X (operational resilience) where the change touches resilience;
- SR 11-7 / OCC 2026-13 where the change touches model risk;
- SR 16-11 / OCC Bulletin 2017-43 / SR 13-1 framing of supervisory review at large banks;
- SR 95-51 / SR 02-22 / SR 16-11 ratings frameworks where the bank's risk-management ratings flow into supervisory engagement.

Cite the specific SR letters that apply to the rule change at hand, not the full list.

#### Workstream and milestone shape

The bank-specific workstream pattern for a material rule change generally includes:

- written-program updates (policy, procedure, standards) reviewed by second line;
- system and platform changes (core banking, LOS, fraud, payments) with named technology delivery owners;
- control build with second-line confirmation of design before go-live;
- staff training across the in-scope first-line population;
- regulatory reporting build (call report, FFIEC reports, agency-specific reporting) with mock submission against the published technical specifications;
- internal-audit review of the build before BAU handoff.

Internal audit involvement before BAU handoff is the bank-specific second-line-plus-third-line pattern; banks generally do not close a material remediation without internal-audit confirmation that the control runs as designed.

#### BAU handoff conventions

The bank's obligation inventory generally lives within the compliance management system or the firm's GRC platform. The implementation-plan handoff names the GRC entry, the responsible role in BAU, and the monitoring cadence (quarterly control test, annual attestation, monthly KRI). For BSA-touching changes, the BSA officer is the BAU owner; for fair-lending-touching changes, the fair-lending officer; for cyber-touching changes, the CISO. The plan does not finalise without naming the BAU owner role.

#### Sources

The named regulatory anchors for banking-side implementation are in `references/source-anchors.md` under the federal banking blocks. Citations include 12 CFR Part 30 Appendix D, OCC Heightened Standards FAQ, the FRB SR letters cited above, and the FFIEC IT Examination Handbook Management Booklet.

## capital-markets

### Sector overlay — capital markets and asset management

Loaded when the scope names capital markets or asset management (registered investment adviser, registered investment company, broker-dealer, exchange, alternative trading system, transfer agent, securities-based swap dealer, custodian, fund administrator). The overlay carries SEC and FINRA implementation-plan conventions on top of the generic spine.

#### SEC deficiency-letter remediation

Implementation plans triggered by an SEC Division of Examinations deficiency letter follow the deficiency letter's response cadence. Response is generally due within 30 days, with the firm's response describing planned remediation. The plan's milestones map to the response commitments; failure to deliver against committed remediation is a credibility issue with the next-cycle exam.

For higher-stakes findings (e.g., custody-rule failures, marketing-rule failures, MNPI controls failures, electronic-communications failures), Division-of-Enforcement referral is a possibility; the plan's governance cadence elevates accordingly, with general counsel in standing membership and outside counsel engagement.

#### FINRA examination findings remediation

FINRA examination findings flow through the FINRA Member Supervision examination cycle. The plan responds to the findings letter within FINRA's specified window (generally 30 days). Where findings escalate to disciplinary action (Notice of Charges, Letter of Acceptance Waiver and Consent, formal complaint), the plan integrates with the disciplinary timeline and outside counsel runs the response.

The FINRA Annual Regulatory Oversight Report and Examination Findings and Observations Report frame the examiner's anticipated focus areas; the implementation plan reflects these where the firm's remediation is broader than a single finding.

#### IAA Rule 206(4)-7 written-policies framework

For investment advisers, the compliance programme runs under IAA Rule 206(4)-7, which requires written policies and procedures, a chief compliance officer, and an annual compliance review. Implementation plans for a regulatory change at an adviser integrate with the Rule 206(4)-7 framework: the change is reflected in the written policies, the CCO's annual review captures the change, and the change is added to the adviser's annual compliance-testing programme.

For ICA Rule 38a-1, the parallel rule applies to registered investment companies. The fund board oversight role is a governance checkpoint; material implementation plans report to the fund board (or the relevant fund-board committee, generally the audit committee or the compliance committee).

#### Custody and books-and-records

Implementation plans touching custody (IAA Rule 206(4)-2) or books-and-records (IAA Rule 204-2; Securities Exchange Act Rule 17a-3 and 17a-4 for broker-dealers) carry tight evidence requirements. Acceptance criteria for custody-related milestones cite the rule's verification, segregation, and reporting requirements; books-and-records milestones cite the retention period and electronic-records preservation standards (rule 17a-4(f) for broker-dealers; recent SEC amendments to electronic recordkeeping for advisers).

#### Marketing-rule remediation

Implementation plans triggered by marketing-rule (IAA Rule 206(4)-1) findings or by SEC risk alerts on marketing follow the marketing-rule sub-domain (testimonials, performance, hypothetical performance, third-party ratings). The plan's controls integrate with the adviser's compliance program; a marketing-rule plan that does not name the marketing-review process and the CCO's role in approving advertising fails the second-line gate.

#### Electronic-communications remediation

Following the Division of Enforcement's pattern of off-channel communications enforcement, plans touching electronic communications (texts, encrypted apps, personal devices) name the policy, the supervisory technology, the training, and the disciplinary framework. The plan's governance cadence escalates given the high enforcement profile.

#### Workstream shape

Typical capital-markets workstream pattern:

- written-policy update under Rule 206(4)-7 / Rule 38a-1 / FINRA supervisory-procedures framework;
- system or platform changes (OMS, EMS, surveillance, books-and-records, electronic-communications);
- control build with CCO confirmation;
- staff training across in-scope supervisory persons and access persons;
- annual compliance-review integration;
- fund-board reporting where ICA Rule 38a-1 applies;
- examiner-readiness rehearsal where the change is high-stakes.

#### Governance shape

Generally CCO-led with a compliance committee, fund-board committee, or executive committee depending on the entity. The plan's governance cadence integrates with the CCO's annual review cycle and the fund-board's reporting calendar.

#### BAU handoff conventions

The adviser's compliance programme is the BAU home for the obligation. The plan's handoff names the CCO, the annual-compliance-review integration, and the testing programme that picks up the new control.

#### Sources

Named regulatory anchors for capital-markets implementation are in `references/source-anchors.md` under the SEC and FINRA blocks. Citations include IAA Rule 206(4)-7, IAA Rule 206(4)-1, IAA Rule 206(4)-2, ICA Rule 38a-1, Exchange Act Rules 17a-3 and 17a-4, SEC Division of Examinations annual priorities, SEC risk alerts, FINRA Rule 3110 supervision, FINRA Annual Regulatory Oversight Report.

## insurance

### Sector overlay — insurance

Loaded when the scope names insurance (life insurer, P&C insurer, health insurer, reinsurer, captive, MGA). The overlay carries insurance-specific implementation-plan conventions on top of the generic spine.

#### State-DOI driven remediation

Insurance regulation is state-led. An implementation plan triggered by a state insurance department finding (market-conduct or financial-condition exam) is calibrated to the lead state's expectations under the NAIC Market Conduct Examiners Handbook or the NAIC Financial Condition Examiners Handbook. Where the insurer is multi-state, the lead-state convention under the Interstate Insurance Product Regulation Compact (IIPRC) or the Coordinated Examination framework applies; the plan names the lead state and the participating states.

Remediation timelines reflect the lead state's supervisory letter or order. Some states use formal market-conduct examination reports with corrective-action plans; others use less formal supervisory letters. The plan's effective date follows the lead state's instrument.

#### ORSA-driven remediation

For risk-based supervisory triggers under the Risk Management and Own Risk and Solvency Assessment Model Act (NAIC RMORSA), the insurer's ORSA report is the framing document for any enterprise-risk-driven remediation. Implementation plans for ORSA-flagged gaps integrate with the insurer's ORSA cycle and report up through the same enterprise risk committee that owns ORSA. The chief risk officer is generally the programme sponsor.

#### NAIC AI Bulletin and state AI activity

For AI governance changes under the NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023, with state-by-state adoption), the implementation plan covers governance, data, model risk, third-party AI, testing and validation, and consumer-impact monitoring. Adoption by state varies; the plan names the states the insurer is operating in and tracks state-level adoption status. NYDFS Insurance Circular Letter No. 7 (2024) and Colorado Regulation 10-1-1 are state-specific overlays on top of the NAIC bulletin.

#### Workstream shape

Typical insurance-side workstream pattern for a material change:

- product filing changes coordinated with the lead state through SERFF (System for Electronic Rate and Form Filing);
- policy-form, rate, and rule revisions with state-by-state approval cycles;
- claim-handling procedure updates with operations training;
- agent and producer training and licensing-system updates;
- actuarial analysis where pricing or reserving is implicated;
- statutory financial reporting changes coordinated with the financial reporting team;
- ORSA report updates where enterprise-risk implications arise.

#### Governance shape

Insurance governance is generally lighter than large-bank Heightened Standards but still committee-driven. Standing committees relevant to a regulatory-change programme include the enterprise risk committee, the product committee, the actuarial committee, and the audit committee. The plan's governance cadence integrates with the insurer's existing committee calendar; standing-up a new committee is a flag that the existing structure is mis-calibrated for the change.

#### State-level filing and approval mechanics

Many implementation plans include a SERFF filing as a milestone with the lead state, followed by state-by-state filings. Each state-level approval is its own milestone with a date that depends on state response time. The plan's effective-date posture accounts for the slowest-responding state where the change must be uniform.

#### BAU handoff conventions

The insurer's obligation inventory generally lives in a compliance-management system or a state-by-state filing log. The plan's handoff names the BAU owner (chief compliance officer, head of state-relations, head of product compliance, head of agent oversight depending on the change), the monitoring cadence, and the SERFF or state-specific filing schedule for ongoing changes.

#### Sources

Named regulatory anchors for insurance-side implementation are in `references/source-anchors.md` under the insurance blocks. Citations include the NAIC Market Conduct Examiners Handbook, the NAIC Financial Condition Examiners Handbook, the NAIC Model Bulletin on AI, RMORSA, NYDFS Insurance Circular Letters, and state-specific regulations as the rule change implicates.

## payments-fintech

### Sector overlay — payments and fintech

Loaded when the scope names payments or fintech (non-bank money transmitter, payment processor, prepaid issuer, neobank operating through a sponsor bank, BNPL provider, PFM, crypto exchange or custodian, remittance provider, P2P platform). The overlay carries non-bank supervision implementation-plan conventions on top of the generic spine.

#### CFPB non-bank supervision

For larger participants and non-bank entities under CFPB supervisory authority, the CFPB Supervision and Examination Manual is the framing document. CFPB examinations produce Matters Requiring Attention (the parallel to the federal banking MRA convention) and supervisory letters. Implementation plans triggered by a CFPB MRA mirror the federal banking convention; the plan's effective date is the date the CFPB communicated.

CFPB Supervisory Highlights frames the recurring focus areas; the implementation-plan author tracks the most recent edition for the supervisory pattern that explains the firm's MRA. (Many CFPB Circulars on UDAAP, overdraft, NSF, adverse-action with complex algorithms, and account reopening were **withdrawn May 12, 2025; historical only** — anchor design decisions to the regulatory text rather than the withdrawn circular layer. The CFPB Interpretive Rule on BNPL (May 2024) was separately **nullified by Pub. L. 119-11 (May 9, 2025); historical only.**)

#### State money-transmitter remediation

For non-bank money transmitters, state money-transmitter laws and the Money Transmission Modernization Act (MTMA, NMLS-driven) apply. State-by-state remediation cycles can be material when the firm operates in multiple states. The plan tracks state-by-state filings and approvals as separate milestones; the lead state generally drives the substance, with other states adopting in line.

NYDFS, California DFPI, Texas Department of Banking, and the Conference of State Bank Supervisors (CSBS) are common state-side participants in coordinated examinations. The plan names the lead state and the participating states.

#### Sponsor-bank-driven remediation

For neobanks and fintechs operating through a sponsor-bank (BaaS) model, the implementation plan is bilateral: the sponsor bank's regulator (OCC, FRB, FDIC) drives expectations through the sponsor, and the fintech absorbs them through the third-party-risk management framework. The plan names the sponsor bank's role in governance, the contractual SLA changes the implementation requires, and the sponsor-bank's review checkpoints.

The June 2023 Interagency Guidance on Third-Party Relationships (OCC, FRB, FDIC) frames the sponsor-bank's expectations on the fintech. The plan reflects the sponsor-bank's diligence, monitoring, and exit-plan posture.

#### Cyber and incident-notification overlays

Payments and fintech firms generally face multiple incident-notification regimes simultaneously: state breach-notification laws, NYDFS Part 500 (where applicable), the federal banking 36-hour rule via the sponsor bank where the fintech is a service provider, FTC Safeguards Rule notification (effective 2024), state-specific cybersecurity rules (Colorado, California, Massachusetts). The plan's notification workflow names every applicable regime and the fastest clock.

#### Crypto and digital-asset overlays

For crypto-asset firms, the regulatory landscape is fragmented. SEC posture (custody, registration), CFTC posture, state money-transmitter posture, NYDFS BitLicense (Part 200), FinCEN MSB registration, OFAC sanctions screening, and bank-side custody-rule positions all apply differentially. The implementation plan names the regulatory regime each in-scope obligation maps to.

#### Workstream shape

Typical payments-fintech workstream pattern:

- policy and procedure updates;
- platform changes (core processing, KYC, fraud, AML transaction monitoring, sanctions screening);
- third-party / sponsor-bank coordination;
- state-by-state filing or notification where applicable;
- consumer-disclosure changes;
- complaint-handling and consumer-redress workflow updates;
- regulatory reporting (state, federal, FinCEN);
- examiner-readiness for the next-cycle exam.

#### Governance shape

Generally lighter than bank governance: CCO and CRO function with a compliance committee. Where the firm operates under a consent order or material MRA, governance escalates; for material consent orders, monthly board reporting is the practitioner pattern.

#### BAU handoff conventions

The firm's obligation inventory in the GRC platform is the BAU home. The handoff names the CCO or chief risk officer as the obligation owner, the monitoring cadence, and the linkage into ongoing state-by-state filing or sponsor-bank-quarterly-review programmes.

#### Sources

Named regulatory anchors for payments and fintech implementation are in `references/source-anchors.md` under the non-bank-supervision and state-banking blocks. Citations include the CFPB Supervision and Examination Manual, the June 2023 Interagency Guidance on Third-Party Relationships, NYDFS Part 200 (virtual currency), state money-transmitter statutes, FinCEN MSB framework (31 CFR Chapter X), OFAC sanctions framework, and the FTC Safeguards Rule.
