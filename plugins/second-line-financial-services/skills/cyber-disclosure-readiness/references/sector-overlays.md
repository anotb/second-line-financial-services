# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for cyber-disclosure-readiness

When the scope names banking, the federal banking agencies' Computer-Security Incident Notification Rule (12 CFR Parts 53/225/304) runs on a 36-hour clock alongside the SEC 4-business-day clock; bank service providers face a 4-hour customer-notification trigger; and FFIEC IT-Handbook expectations underpin the Item 106(b) risk-management narrative.

Loaded by: `cyber-disclosure-readiness/SKILL.md` when `scope.sector_overlay_set` includes `banking`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- Federal banking agencies' Computer-Security Incident Notification Rule:
  - 12 CFR Part 53 (OCC; national banks and federal savings associations).
  - 12 CFR Part 225 Subpart N (FRB; state member banks and BHCs).
  - 12 CFR Part 304 Subpart C (FDIC; state nonmember banks and savings associations).
  Effective May 1, 2022.
- FFIEC IT Examination Handbook, Information Security booklet (September 2016) and Architecture, Infrastructure, and Operations booklet (June 2021) — Sections on incident response, third-party risk management, business continuity [verify section].
- OCC Heightened Standards (12 CFR Part 30 Appendix D) — risk-governance framework and risk-appetite-statement expectations cover cyber as part of the operational and reputational categories.
- FFIEC Cybersecurity Assessment Tool (CAT) — sunset; verify any successor or refreshed framework at draft time.
- Interagency Guidelines Establishing Information Security Standards (12 CFR Part 30 Appendix B for OCC; 12 CFR Part 208 Appendix D-2 for FRB; 12 CFR Part 364 Appendix B for FDIC) and the 2005 Interagency Guidance on Response Programs.
- OCC Bulletins on third-party risk and operational resilience that touch on cyber-incident expectations [verify current bulletin numbers at draft time].

#### What changes for banking-flagged disclosure-readiness work

##### 1. The 36-hour clock joins the parallel-clocks table

For banking organizations covered by 12 CFR Parts 53/225/304, the 36-hour clock from determination of a "notification incident" runs alongside the SEC 4-business-day clock. The two clocks resolve from different basis events:

- 36-hour clock: starts at determination that the computer-security incident materially disrupted or degraded (or is reasonably likely to materially disrupt or degrade) the bank's banking operations, customer-service delivery, business-line revenue or franchise value, or US financial stability.
- 4-business-day SEC clock: starts at materiality determination under the TSC standard.

A single incident can determine to be a "notification incident" before, simultaneously with, or after determining materiality for SEC purposes. The pack tracks both clocks and shows the basis events for each.

##### 2. Bank service providers face a 4-hour customer-notification trigger

Where the registrant is a bank service provider (a vendor providing services to a banking organization), 12 CFR Parts 53/225/304 require notification to affected banking-organization customers as soon as possible after determining a computer-security incident has caused, or is reasonably likely to cause, a service disruption of four or more hours.

This trigger runs on the service-provider side, independent of the registrant-side 36-hour clock. The pack flags bank-service-provider status in the scope and surfaces the 4-hour trigger when applicable.

##### 3. FFIEC IT-Handbook content underpins Item 106(b)

For bank-affiliated registrants, the Item 106(b)(1) processes-for-assessing-identifying-managing draft typically references the firm's information-security program in FFIEC-aligned terms (governance, risk-assessment, risk-mitigation, supervisory examination, board oversight). The FFIEC IT Handbook is the bank-supervisory frame; alignment of the firm's program to it is the standard banking-sector narrative.

Banks are not required to name FFIEC alignment in the Item 106 disclosure, but where the firm operates against FFIEC expectations, the disclosure benefits from internal consistency with the FFIEC-aligned program documentation.

##### 4. Heightened Standards covered banks carry the additional cyber-governance lens

For OCC Heightened Standards covered banks (12 CFR Part 30 Appendix D, Section II's risk-governance framework), cyber risk is part of the operational and reputational risk categories named in the framework. The Item 106(c) governance disclosure for a Heightened Standards covered bank typically:

- Names the Risk Committee of the Board (the named-by-rule independent risk committee under Section IV) as the committee with cyber oversight.
- References the risk-governance framework and the risk-appetite statement's coverage of cyber.
- Names the CISO's reporting line and the CRO's role in cyber-risk oversight (consistent with the three-lines model articulated in Section V's roles-and-responsibilities expectations).

##### 5. OCC, FRB, and FDIC supervisory examination findings

Cyber-related supervisory findings (MRAs, MRIAs from FRB; MRAs from OCC; MRBAs and MRAs from FDIC) typically run alongside the SEC disclosure work. Where a finding relates to a recent material incident, the disclosure committee considers whether the finding itself requires Item 106 update or 8-K disclosure on its own merits (typically not, but the analysis is recorded).

The DCP map (Artifact C) documents the firm's information flow between the cyber MRA / MRIA process and the disclosure process so that the disclosure committee receives material supervisory-finding context.

##### 6. Banking-specific parallel-clock interactions

The pack's parallel-clocks table for a covered banking organization typically includes:

- 36-hour clock to primary federal regulator (OCC for nationals, FRB for state members and BHCs, FDIC for state nonmembers).
- 4-hour bank-service-provider customer-notification trigger if the entity is a bank service provider to other banking organizations.
- NYDFS §500.17 72-hour clock if the entity is NYDFS-licensed (many banking organizations are).
- 2005 Interagency Guidance customer-notice obligations for banking-agency-supervised entities on unauthorized access to sensitive customer information.
- State breach-notification clocks where customer information is implicated.
- SEC Reg S-P 30-day clock if the banking organization includes a registered broker-dealer or registered investment adviser arm (many BHCs do).
- SEC 4-business-day Item 1.05 clock if the registrant is a 1934-Act-registered issuer (most BHCs are).

The senior reviewer's job is to resolve all clocks in parallel, with the materiality-determination workpaper as the central evidence record.

#### Banking-specific output additions

When banking is in scope:

- Artifact A's parallel-clocks table includes the federal banking agency 36-hour row and (where applicable) the bank-service-provider 4-hour row.
- Artifact A's DCP trace includes the regulatory-notification stage feeding the 36-hour clock alongside the SEC-disclosure stage feeding the 4-business-day clock.
- Artifact B's Item 106(b)(1) draft references the firm's FFIEC-aligned information-security program in language consistent with bank examination findings and supervisory letters.
- Artifact B's Item 106(c) draft for Heightened Standards covered banks names the Risk Committee of the Board (the Section IV independent risk committee), the cadence, and the CISO and CRO roles consistent with Section V's roles-and-responsibilities expectations.
- Artifact C's DCP map documents the federal banking agency notification stage and the supervisory-examination-finding feedback loop.

#### Common pitfalls

- Treating the SEC 4-business-day clock as the only or the dominant clock. For covered banking organizations, the 36-hour clock is faster and runs from a different basis event.
- Conflating "notification incident" determination (12 CFR 53/225/304) with "material cybersecurity incident" determination (Item 1.05). The two standards are different; an incident can be one without being the other.
- Missing the 4-hour bank-service-provider customer-notification trigger when the firm is a service provider to other banks.
- Naming a generic "management committee" in the Item 106(c) governance disclosure for a Heightened Standards covered bank where the rule names the Risk Committee of the Board.
- Inconsistency between the firm's FFIEC-aligned information-security program documentation and the Item 106(b) disclosure narrative.
- Failing to surface OCC, FRB, or FDIC cyber-supervisory findings in the DCP map's information flow into the disclosure committee.
- Treating cyber as a stand-alone risk in the banking context rather than as part of the operational and reputational risk categories named in 12 CFR Part 30 Appendix D Section II.

## capital-markets

### Capital-markets sector overlay for cyber-disclosure-readiness

When the scope names capital markets (broker-dealer, investment adviser, registered investment company, transfer agent), SEC Regulation S-P amendments (May 2024) add a 30-day customer-notification clock; FINRA Rule 4530 reporting may apply for FINRA-member broker-dealers; and registered-fund disclosure carries Form N-CSR / N-1A / N-2 considerations alongside the 10-K stream where applicable.

Loaded by: `cyber-disclosure-readiness/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- SEC Regulation S-P amendments, Release Nos. 34-100155, IA-6604, IC-35193 (final May 16, 2024). Amends 17 CFR Part 248.30 (Safeguards Rule). Covered institutions: broker-dealers, investment advisers (including those exempt from registration), registered investment companies, and transfer agents. Compliance dates phased: large entities 18 months from publication in the Federal Register; smaller entities 24 months [verify entity-type definitions and current compliance dates at draft time].
- FINRA Rule 4530 — Reporting Requirements [verify subsection labels at draft time]. 4530(a)(1) for statutory disqualification, customer complaints meeting specified criteria, regulatory actions; 4530(b) for internal conclusions of violations; 4530(d) for quarterly statistical and summary reports of customer complaints.
- SEC Investment Adviser Rules: Investment Advisers Act Rule 206(4)-7 (compliance program rule) for registered investment advisers; cyber-program failures have been the subject of SEC enforcement actions citing Rule 206(4)-7.
- SEC Investment Company Rules: 17 CFR §270.38a-1 (compliance program rule for registered investment companies).
- Form N-CSR (registered closed-end and open-end management investment companies) and Form N-1A / Form N-2 / Form N-CEN (registration and reporting forms for registered investment companies). Item 16K cybersecurity disclosure for registered investment companies on Form N-CSR pursuant to Release No. 33-11216 [verify form item references at draft time].
- SEC Risk Alerts on cybersecurity for broker-dealers and investment advisers (most recent Division of Examinations Risk Alerts).
- For transfer agents: 17 CFR §240.17Ad-22 transfer-agent rules, with cyber-program implications.

#### What changes for capital-markets-flagged disclosure-readiness work

##### 1. Reg S-P 30-day customer-notification clock joins the parallel-clocks table

The May 2024 amendments require covered institutions to:

- Maintain written policies and procedures for an incident-response program reasonably designed to detect, respond to, and recover from unauthorized access to or use of customer information.
- Notify each affected individual whose sensitive customer information was, or is reasonably likely to have been, accessed or used without authorization, as soon as practicable but not later than 30 days after the institution becomes aware that such access or use has occurred.

The 30-day clock starts at awareness of unauthorized access. This is a different basis event from the SEC 4-business-day Item 1.05 materiality-determination clock.

The customer-notice content requirements include the description of the incident, the type of sensitive customer information affected, and contact information. The notice content is distinct from the 8-K Item 1.05 disclosure; one does not satisfy the other.

##### 2. Sensitive customer information posture

The Reg S-P amendments expanded the "customer information" definition. Sensitive customer information includes (per the rule): any combination of information that would permit a reasonable person to identify a customer of the institution and to conduct fraudulent or unauthorized transactions; or any combination of components that, together, allow access to a customer's account at the institution. The pack carries the determination of what categories of sensitive customer information were accessed or used.

The 30-day clock applies only when sensitive customer information is accessed or used. For other customer information, the institution still has incident-response program obligations but the 30-day customer-notice clock does not run on the same basis.

##### 3. FINRA Rule 4530 for FINRA-member broker-dealers

Cybersecurity events that result in customer complaints meeting the 4530(d) threshold or that constitute a 4530(b) internal conclusion of violation are reportable to FINRA. FINRA Rule 4530(a) reporting is event-driven (typically within 30 days of awareness); 4530(d) is quarterly statistical reporting.

The pack's parallel-clocks table for a FINRA-member registrant carries the 4530(a) and 4530(d) rows alongside the SEC and Reg S-P rows.

##### 4. Investment Advisers Act and Investment Company Act compliance program rules

SEC enforcement actions against registered investment advisers for cybersecurity failures have frequently cited Rule 206(4)-7 (compliance program rule) where the firm's policies and procedures for cyber were inadequate or were not followed in practice. The Item 106(b) disclosure for an RIA registrant typically references the firm's compliance program under Rule 206(4)-7 and the CCO's role in cyber-program oversight.

For registered investment companies, Rule 38a-1 carries similar implications, with the fund's CCO role in cyber-program oversight surfaced in the disclosure.

##### 5. Form N-CSR Item 16K for registered investment companies

The SEC Final Rule (Release No. 33-11216) added cybersecurity disclosure obligations for registered investment companies on Form N-CSR. The disclosure parallels Item 106 of Regulation S-K with adaptations for the fund context. The pack handles registered-fund disclosure as a parallel work-stream to the 10-K Item 106 disclosure, with shared content where the same management oversees both (typical for a fund-and-adviser complex) [verify form item references at draft time].

##### 6. Adviser-and-fund disclosure overlap

Many capital-markets registrants are part of a complex with both adviser-side disclosures (10-K or Form ADV / Part 2 / Form CRS / Risk Alerts) and fund-side disclosures (Form N-CSR / N-1A / N-2 / N-CEN). A cyber incident affecting the adviser's systems can affect the funds advised by the adviser; the disclosure committee considers both venues.

Adviser-side disclosure runs through the 10-K (or 20-F for FPI advisers) under Item 106. Fund-side disclosure runs through Form N-CSR (annual and semi-annual). The two are independent but related; the pack tracks both.

##### 7. Examination-cycle frame

SEC Division of Examinations has identified cybersecurity as a recurring examination priority for advisers, broker-dealers, and registered funds. Risk Alerts published by the Division have set expectations on cyber-program elements; the Item 106(b) narrative typically references the firm's program in language consistent with the Risk Alerts' expectations.

Examination findings on cyber typically result in deficiency letters; material findings can result in enforcement referrals. The DCP map documents the firm's information flow between examination findings and the disclosure committee.

#### Capital-markets-specific output additions

When capital markets is in scope:

- Artifact A's parallel-clocks table includes the Reg S-P 30-day row and (where applicable) FINRA Rule 4530(a) / 4530(d) rows.
- Artifact A's facts-of-the-incident row characterizes whether sensitive customer information was accessed or used (per Reg S-P) and whether customer complaints meeting 4530 thresholds resulted.
- Artifact A's DCP trace includes the Reg S-P customer-notification stage alongside the SEC-disclosure stage.
- Artifact B's Item 106(b) draft references the firm's compliance program under Rule 206(4)-7 (RIA) or Rule 38a-1 (RIC) and the CCO's role in cyber-program oversight where applicable.
- Artifact B carries a Form N-CSR Item 16K cross-link for registered investment companies in the complex [verify form item references at draft time].
- Artifact C's DCP map documents the Reg S-P customer-notification escalation path and the FINRA-reporting feedback loop where applicable.

#### Common pitfalls

- Conflating the Reg S-P 30-day clock with the SEC 4-business-day clock. The two run on different basis events and on different content.
- Treating the 8-K Item 1.05 filing as a substitute for the Reg S-P customer notice. Different audiences, different content.
- Using a single 10-K Item 106 disclosure for an adviser-and-fund complex without considering Form N-CSR Item 16K obligations on the fund side.
- Missing the FINRA Rule 4530(d) quarterly statistical reporting trigger for cyber-related customer complaints.
- Naming a generic "compliance function" in the Item 106(b) disclosure for a registered adviser where Rule 206(4)-7 expects the CCO's role to be discrete and named.
- Inconsistency between the firm's compliance program documentation under Rule 206(4)-7 / Rule 38a-1 and the Item 106(b) disclosure narrative on processes, oversight, and accountability.
- Treating SEC Risk Alerts on cybersecurity as background reading rather than as content that lands in the Item 106(b) draft and the DCP map's gap-analysis row.
- For complex registrants (banks with broker-dealer or investment-adviser subsidiaries), missing the multi-regulator clock interactions: the 36-hour federal banking agency clock + the 30-day Reg S-P clock + the 4-business-day SEC clock + the NYDFS 72-hour clock can all run on the same incident.

## insurance

### Insurance sector overlay for cyber-disclosure-readiness

When the scope names insurance, the NAIC Insurance Data Security Model Law (Model #668) §6 carries a 72-hour cyber-event-notification clock to the state insurance commissioner in adopting states; state DOI-specific cyber-event timelines apply on top of state breach-notification mosaic; and NAIC Bulletin December 2023 (third-party AI accountability) interacts where AI is in the cyber surface.

Loaded by: `cyber-disclosure-readiness/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NAIC Insurance Data Security Model Law (Model #668), 2017. §4 (information security program); §6 (notification of cybersecurity event) — 72-hour clock to commissioner. State adoption varies; verify the specific state DOI's adoption status and any state-specific deviations at draft time.
- NYDFS 23 NYCRR Part 500 §500.17 — 72-hour notice of cybersecurity event for NYDFS-licensed entities (including NYDFS-licensed insurers).
- HIPAA Breach Notification Rule (45 CFR §§164.400-414) for health-insurance carriers and business associates.
- NAIC Insurance Information and Privacy Protection Model Act (Model #670) and Privacy of Consumer Financial and Health Information Regulation (Model #672) — privacy frameworks for state-licensed insurers; current adoption varies.
- NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (Model Bulletin, December 2023) — third-party AI accountability and AIS Program elements; relevant where AI is in the cyber surface.
- State insurance department-specific cyber-event-notification orders and bulletins (varies by state; CA, NY, TX, IL, FL frequently have additional state-specific guidance) [verify state-specific orders at draft time].
- SEC 8-K Item 1.05 and Item 106 apply where the insurer is a public-company filer (a holding-company structure with the insurance entity as a subsidiary frequently has the holding company as the SEC registrant).

#### What changes for insurance-flagged disclosure-readiness work

##### 1. The NAIC Model #668 72-hour clock joins the parallel-clocks table

For state-licensed insurers in adopting states (NY, SC, OH, MS, AL, MI, DE, LA, NH, VA, IN, CT, TN, IA, ND, ME, WI, MN, KY, HI, FL, AK [verify current adopting states at draft time]), §6 of Model #668 requires notification to the commissioner as promptly as possible but in no event later than 72 hours after a determination that a cybersecurity event has occurred meeting the rule's thresholds.

Adopting states sometimes vary the threshold or the timeline. Verify the specific state DOI's text at draft time. Multi-state insurers map state-by-state.

##### 2. NYDFS §500.17 for NYDFS-licensed insurers

NYDFS-licensed insurers (life, health, P&C in NY) are NYDFS-covered entities subject to 23 NYCRR Part 500. The §500.17(a) 72-hour clock and the §500.17(c) 24-hour extortion-payment clock apply alongside the Model #668 clock for insurers licensed in both NY and other adopting states.

##### 3. HIPAA scope for health-insurance carriers

Health-insurance carriers are HIPAA-covered entities. The HIPAA Breach Notification Rule (60-day individual notice; concurrent HHS for 500+; annual log for under-500) applies in addition to NAIC Model #668 and NYDFS §500.17. The pack flags health-carrier status and carries the HIPAA clock in the parallel-clocks table.

Business-associate scope (insurers acting as TPAs, providing FNOL services to other carriers, processing PHI on behalf of healthcare-affiliated counterparties) brings the BAA-side HIPAA obligations.

##### 4. NAIC Bulletin December 2023 — AI accountability

Where AI is in the cyber surface (the firm uses AI in underwriting, claims handling, FNOL triage, fraud detection, or customer-facing functions), the NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (Model Bulletin, December 2023) sets expectations on:

- Senior management and board accountability for the AIS Program.
- Third-party AI vendor governance and the firm's accountability for vendor model failures.
- Testing and validation of AI systems.
- Documentation of AI-system development, deployment, and monitoring.

A cyber incident involving an AI system (model-poisoning, prompt-injection of an AI-driven customer service or claims-triage system, vendor LLM compromise) interacts with the Bulletin's expectations on AIS Program governance and third-party accountability. The pack carries the AIS-Program-aligned narrative where AI is implicated.

##### 5. State DOI cyber-event notification specifics

State DOIs frequently issue additional guidance, orders, or bulletins on cyber-event notification beyond Model #668's 72-hour clock. Examples (illustrative; verify current state guidance at draft time):

- Some states require concurrent notification to the state attorney general or to specific consumer-protection authorities.
- Some states require additional content elements in the notification (root-cause summary, remediation status, affected-individual count by state).
- Some states require ongoing status updates beyond the initial 72-hour notice.

The pack tracks state-specific deviations.

##### 6. Public-company holding-company structure

Many large insurers are organized as holding-company structures with the holding company as the SEC registrant and one or more state-licensed insurance subsidiaries. The SEC Item 1.05 8-K and Item 106 10-K disclosures apply at the holding-company level. The Model #668 §6 and NYDFS §500.17 obligations apply at the licensed-insurer-subsidiary level.

The pack handles the dual-reporting structure: the disclosure committee at the holding-company level, the insurance-subsidiary CISO and compliance function at the entity level, with information flowing up to the disclosure committee for the SEC determination and laterally to each state DOI for the state-licensed-insurer obligations.

##### 7. Investment-and-insurance complex

Some insurers operate as part of a complex with broker-dealer, investment-adviser, and registered-fund affiliates (e.g., variable-annuity issuers with affiliated broker-dealers and registered separate accounts). For these, the capital-markets sector overlay's Reg S-P, FINRA Rule 4530, and Form N-CSR considerations apply on top of the insurance-specific obligations.

#### Insurance-specific output additions

When insurance is in scope:

- Artifact A's parallel-clocks table includes the NAIC Model #668 72-hour row (per state adopting), the NYDFS §500.17 72-hour row if NYDFS-licensed, the HIPAA Breach Notification Rule rows for health-insurance carriers, and state DOI-specific deviations.
- Artifact A's facts-of-the-incident row characterizes whether AI is implicated (and if so, the AIS-Program-aligned narrative per NAIC Bulletin December 2023).
- Artifact B's Item 106(b) draft references the firm's information-security program in NAIC Model #668 §4-aligned terms where applicable.
- Artifact B's Item 106(c) draft for a holding-company registrant names the holding-company-level board committee with cyber oversight (typically the Risk Committee) and the information flow from insurance-subsidiary CISOs.
- Artifact C's DCP map documents the insurance-subsidiary-to-holding-company information flow and the state-DOI parallel reporting tracks.

#### Common pitfalls

- Treating Model #668 as uniform across adopting states. State-specific deviations on threshold, timeline, and content matter.
- Missing the NAIC Bulletin December 2023 alignment when AI is in the cyber surface. AI-related cyber incidents have an AIS-Program governance dimension.
- Conflating the holding-company SEC determination with the insurance-subsidiary state-DOI obligations. The two run on different timelines and to different audiences.
- Omitting HIPAA Breach Notification Rule obligations for health-insurance carriers or for business associates of healthcare counterparties.
- Naming a generic "Risk Committee" in the Item 106(c) governance disclosure for an insurance holding company without distinguishing the holding-company committee from the insurance-subsidiary board governance, where the firm operates with separate insurance-subsidiary boards.
- Treating a cyber incident at an insurance subsidiary as a non-issue at the holding-company level when the subsidiary's operational disruption is material to the holding company's results.
- Failing to surface state DOI-specific orders or bulletins beyond Model #668 in the parallel-clocks table.

## payments-fintech

### Payments-fintech sector overlay for cyber-disclosure-readiness

When the scope names payments-fintech, PCI DSS contractual notification obligations apply on the card-handling side; CFPB supervisory expectations for large nonbanks frame the consumer-facing disclosure posture; and Reg E error-resolution clocks affect customer transactions where a cyber incident causes erroneous or unauthorized transfers.

Loaded by: `cyber-disclosure-readiness/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- PCI DSS v4.0.1 (Payment Card Industry Data Security Standard, current version effective March 31, 2024 through 2025 phase-in for new requirements [verify current version at draft time]). Card-brand contractual obligation, not a regulatory rule directly; enforced through merchant-services contracts, acquirer relationships, and card-brand operating regulations.
- Card-brand operating rules and incident-notification requirements (Visa Core Rules, Mastercard Rules, American Express Operating Regulations, Discover Network Operating Regulations) [verify current versions at draft time]. Each carries incident-notification obligations and forensic-investigation triggers.
- CFPB supervisory expectations for large nonbanks under the Larger Participant Rules and the Section 1024 supervision authority. CFPB has issued circulars and guidance that touch on cyber-program failures and consumer-impact considerations [verify current circulars at draft time].
- Regulation E (12 CFR Part 1005) error-resolution requirements for electronic fund transfers (typically 10 business days for provisional credit on disputed transfers; 45-day investigation for new accounts; 90 days for foreign-initiated or POS errors). Where a cyber incident results in unauthorized EFTs, the Reg E error-resolution clocks apply.
- Regulation Z (12 CFR Part 1026) for credit-card billing errors and unauthorized use; 60-day customer-notice window for billing-error claims.
- NACHA Operating Rules for ACH-related cyber events.
- For state-licensed money transmitters and similar nonbank fintechs: state-specific cybersecurity and incident-notification requirements (varies by state) [verify state-specific rules at draft time].
- NYDFS Part 500 for NYDFS-licensed nonbank entities (some virtual-currency businesses, money transmitters, and fintechs are NYDFS-licensed).

#### What changes for payments-fintech-flagged disclosure-readiness work

##### 1. PCI DSS contractual notification

For card-handling entities, PCI DSS sets the data-security frame and the card-brand operating rules set the incident-notification obligations. PCI DSS itself is not a regulator-enforced rule; it is a contractual obligation enforced through merchant-services contracts, acquirer relationships, and card-brand operating regulations. Notification clocks vary by card brand and by acquirer agreement.

Typical card-brand-side obligations include:

- Notify the acquirer of any suspected or confirmed account-data compromise as soon as discovered.
- Engage a PCI Forensic Investigator (PFI) for events involving account data compromise.
- Comply with card-brand operating rule timelines for forensic investigation and remediation.

The pack carries the contractual-notification obligations as a row in the parallel-clocks table (labelled "card-brand contractual" with the specific card-brand basis); the regulatory-clock columns (SEC, federal banking agency, NYDFS, Reg S-P, state breach-notification, HIPAA where applicable) carry the regulatory clocks alongside.

##### 2. CFPB supervisory expectations

For large nonbanks under CFPB Section 1024 supervision (consumer reporting, debt collection, residential mortgage, payday lending, student loan servicing, auto-loan servicing, large larger-participant categories), CFPB supervisory expectations on cyber-program adequacy and on consumer-facing communications during a cyber incident frame the disclosure posture. CFPB enforcement actions have addressed cyber-program failures.

The Item 106(b) disclosure for a CFPB-supervised nonbank typically references the firm's cyber program in CFPB-aligned terms where applicable.

##### 3. Reg E error-resolution for cyber-driven unauthorized EFTs

Where a cyber incident results in unauthorized electronic fund transfers, the Reg E error-resolution timelines apply:

- Customer notice of unauthorized transfer must be received within 60 days of statement transmission to preserve full Reg E protections.
- Provisional credit within 10 business days of receiving customer notice.
- Investigation completed within 45 days (existing accounts) or 90 days (new accounts, foreign-initiated transfers, POS).
- Final resolution and customer notice.

These clocks run on the customer-account side, independent of the registrant-side disclosure clocks. The pack flags Reg E applicability when EFTs are implicated and carries the customer-impact-count drivers in the materiality workpaper.

##### 4. Reg Z billing-error resolution for credit-card-related cyber events

Where a cyber incident affects credit-card billing (unauthorized charges, fraud-driven billing errors), Reg Z's billing-error resolution requirements apply:

- Customer notice of billing error within 60 days of statement transmission.
- Acknowledgment of customer notice within 30 days; resolution within 90 days.
- Customer's $50 maximum liability for unauthorized credit-card use.

##### 5. NACHA Operating Rules

For ACH-related cyber events (ACH origination, fraudulent ACH transactions), NACHA Operating Rules apply alongside the regulatory clocks. ODFIs (originating depository financial institutions) and RDFIs (receiving depository financial institutions) have specific NACHA-rule obligations on incident reporting and on transaction reversal under specific NACHA rules.

##### 6. BaaS and bank-partner concentration

Many fintechs operate via Banking-as-a-Service relationships with chartered banks. A cyber incident at a fintech can affect the bank-partner's customer base; the bank-partner's federal banking agency 36-hour clock can be triggered by an incident at the fintech (through the bank-service-provider 4-hour customer-notification trigger that the fintech-as-bank-service-provider faces, and through the bank-partner's own determination of whether the incident is a notification incident).

The pack flags BaaS-relationship status and surfaces the bank-partner's regulatory-notification path.

##### 7. State-licensed money transmitter specifics

State money-transmitter licensing (varies by state) brings state-specific cybersecurity and incident-notification requirements. NYDFS-licensed money transmitters are NYDFS-covered entities subject to 23 NYCRR Part 500. California's Money Transmission Act and similar state regimes carry their own cyber-related expectations. Multi-state-licensed money transmitters map state-by-state.

#### Payments-fintech-specific output additions

When payments-fintech is in scope:

- Artifact A's parallel-clocks table includes the card-brand contractual row (Visa, Mastercard, AmEx, Discover as applicable), Reg E error-resolution clocks where EFTs are implicated, Reg Z billing-error clocks where credit cards are implicated, NACHA Operating Rules where ACH is implicated, and state money-transmitter-license-specific rows.
- Artifact A's DCP trace includes the acquirer / card-brand notification stage and the bank-partner notification stage where BaaS applies.
- Artifact B's Item 106(b) draft references PCI DSS-aligned data-security program elements, CFPB supervisory expectations where applicable, and the firm's third-party-bank-partner risk management.
- Artifact B's Item 106(b)(1)(iii) (third-party service-provider oversight) is content-rich for fintechs given heavy reliance on bank partners, payment processors, and shared infrastructure.
- Artifact C's DCP map documents the card-brand notification, bank-partner notification, and consumer-facing communication stages alongside the SEC-disclosure and regulatory-notification stages.

#### Common pitfalls

- Treating PCI DSS as a regulatory rule rather than a contractual obligation. The clocks and the enforcement run on a different basis.
- Missing the bank-partner regulatory-notification path for BaaS-relationship fintechs. The bank-partner's federal banking agency 36-hour clock is on the bank's side but is triggered by events at the fintech.
- Conflating the registrant-side disclosure clocks with the customer-side Reg E and Reg Z error-resolution clocks. The two run on different audiences and different content.
- Naming a generic "compliance function" in the Item 106(b) disclosure for a CFPB-supervised nonbank without referencing the CFPB-aligned program elements where the firm operates against CFPB expectations.
- Inconsistency between the PCI DSS-aligned data-security program documentation and the Item 106(b) disclosure narrative on processes, oversight, and controls.
- Treating a cyber incident at a fintech as a fintech-only matter when the BaaS relationship exposes the bank partner's customer base.
- For state-licensed money transmitters: missing state-specific cybersecurity-rule obligations (NYDFS Part 500, California Money Transmission Act, similar state regimes) in the parallel-clocks table.
- Omitting the customer-side communications obligations (Reg E, Reg Z) when the cyber incident has direct consumer-transaction impact. The disclosure-clock posture is one consideration; the consumer-rights posture is another.
