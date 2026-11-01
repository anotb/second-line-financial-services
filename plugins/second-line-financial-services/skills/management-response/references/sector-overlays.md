# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for management-response

When the scope record names `banking` for a management-response engagement, this overlay sets banking-supervisor-shaped conventions for the response artifact. Banking is the primary case for this skill; the formal-letter conventions and the supervisory-severity-ladder defaults are tightest here.

Loaded by: `management-response/SKILL.md` when `scope.sector_overlay_set` includes `banking`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- FRB SR 13-13 (Supervisory Considerations for the Communication of Supervisory Findings, June 2013) — the principal federal-banking-agency framework for the MRA / MRIA distinction and the management-response posture the FRB expects.
- OCC Comptroller's Handbook Bank Supervision Process booklet — the OCC's operative framework for routine findings communication and corrective actions; PPM 5310-3 (enforcement actions) applies once a matter has escalated beyond routine supervision.
- FDIC Risk Management Manual of Examination Policies — the FDIC's framework for examination findings and Matters Requiring Board Attention.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards) — for OCC-supervised covered banks, the framework binding on the response (board oversight; risk governance framework). The published Appendix uses lettered Roman-numeral headings without the III.B-style sub-numbering colloquially used.
- FRB SR 12-17 (Consolidated Supervision Framework for Large Financial Institutions, December 2012) and SR 19-3 (LFI rating system) — for BHCs above thresholds, the consolidated supervision framework that contextualises the response.
- Federal banking agencies' interagency guidance on third-party risk management (June 2023) — frequent subject of supervisory findings.
- BCBS principles for sound management of operational risk (revised March 2021) — for operational-risk findings, the prudential framework the response references.

#### What changes for banking-flagged management responses

##### 1. Severity ladder defaults

The banking-supervision frame distinguishes Matters Requiring Attention from Matters Requiring Immediate Attention. The skill applies tier-specific defaults the responding role can adjust:

- **MRIA**: monthly written progress reports to the supervisory office until closure; firm-level signatory typically the CEO or General Counsel (in addition to the CRO or process-owner responding role); board-level attention required (the response is read at the next risk committee or audit committee meeting, with the chair acknowledging receipt); compressed action-plan envelope (typically 6 to 12 months, with shorter envelopes for specific MRIAs the supervisor flags as urgent); evidence-of-effectiveness method usually includes a supervisor walk-through in addition to control-test or KRI-trend evidence.
- **MRA**: quarterly written progress reports; firm-level signatory typically the CRO or process-owner responding role; risk committee notification rather than board-level attention required (depending on materiality); action-plan envelope typically 12 to 18 months; evidence-of-effectiveness method usually two consecutive quarters at GREEN on the relevant KRI or two consecutive quarterly control-test passes.
- **Matters Requiring Board Attention** (FDIC equivalent of MRA in many examination contexts): cadence and signatory follow the FDIC examination team's specification in the report of examination; defaults follow the MRA convention above.

Defaults are starting points, not constraints; the supervisory team's specification in the finding communication overrides the default.

##### 2. Addressee conventions

- **FRB findings**: addressee is the supervisory office identified in the SR-13-13-conformant communication (e.g., the relevant Reserve Bank or the Board's Division of Supervision and Regulation for Board-supervised entities). The response form follows formal supervisory-letter convention.
- **OCC findings**: addressee is the OCC supervisory office identified in the supervisory-letter communication (typically the assigned examiner-in-charge or the supervisory-office director). The response form follows the OCC's letter convention; for Heightened Standards-covered banks the response may also need to be acknowledged at the risk committee under the heightened-standards board-oversight expectations.
- **FDIC findings**: addressee is the FDIC regional office or the examiner-in-charge identified in the report of examination; the response is appended to the report.

##### 3. Linkage to 12 CFR Part 30 Appendix D for Heightened Standards-covered banks

For OCC-supervised banks above the Heightened Standards threshold (currently $50 billion average total consolidated assets), the response carries explicit linkage to:

- Risk Governance Framework — the response acknowledges where the finding implicates a deficiency in the framework and what change to the framework is committed.
- Risk Appetite Statement — where the finding implicates a RAS metric or a RAS limit, the response identifies any RAS recalibration request and links to the risk committee pack section.
- Roles and Responsibilities — the response identifies the responsible role at front-line, independent risk management, or internal audit.

This linkage is typically required for MRAs and MRIAs that hit Heightened Standards-covered topics; for more routine findings it is best-practice rather than required. Citations live in `references/source-anchors.md`.

##### 4. Linkage to LFI ratings and BHC supervision

For FRB-supervised BHCs above the LFI rating system thresholds (SR 19-3), the response is read in the context of the firm's LFI rating and may itself contribute to subsequent rating decisions. The response carries explicit linkage to:

- The firm's most recent LFI rating components (Capital Planning and Positions; Liquidity Risk Management and Positions; Governance and Controls).
- The supervisory cycle phase (continuous monitoring vs. target examination vs. horizontal review).

For firms below the LFI thresholds (community-banking and smaller-regional supervision), the rating reference is to the CAMELS components.

##### 5. Concentration with the Annual Review Letter and the supervisory cycle

FRB and OCC findings are typically communicated in or alongside the annual review letter or supervisory communications at the close of an examination cycle. The response is read alongside the firm's other open findings; the response template carries explicit linkage to other open findings sharing root cause or remediation actions (`linked_finding_ids`). Concentration of root cause across multiple findings (for example, a recurring data-quality root cause showing in third-party, model, and BSA/AML findings) is itself a topic the supervisor will press on; the response surfaces this concentration where it exists.

##### 6. Cross-link to other capability skills

- Underlying issue write-up: `issue-writeup`.
- Standing committee pack carrying the finding ageing across the open population: `risk-committee-pack` (issues-and-remediation-status section).
- BCBS 239 self-assessment for data-quality findings: `bcbs239-gap-assessment`.
- Third-party remediation: `contract-gap-review` and `concentration-risk-review`.
- Operational-resilience remediation: `criticality-assessment` (important-business-service mapping) and `resilience-testing-pack`.

#### Banking-specific output additions

Added to the response (mapped to schema where present):

- `addressee.addressee_name` — banking convention names the supervisory office and the regulator (e.g., "FRB-Supervised Office, Federal Reserve Bank of [district]"; "OCC Supervisory Office, [district]"; "FDIC Regional Office, [region]"). Personal names are not used.
- `reporting_cadence.frequency` — defaults to monthly for MRIA, quarterly for MRA / MRBA per the severity-ladder defaults above.
- `firm_level_signatory_role` — populated for MRIAs (typically CEO or General Counsel); optional for MRAs.
- `linked_finding_ids` — banking responses commonly cross-link to other open findings sharing root cause; the response surfaces concentration explicitly.
- `evidence_of_effectiveness_plan.evidence_method` — for MRIAs, typically includes a supervisor walk-through in addition to control-test or KRI-trend evidence.

#### Common pitfalls in banking-flagged management responses

- Treating MRA and MRIA as the same. MRIA carries a more rapid response expectation, board-level attention, a more senior signatory, and a tighter reporting cadence; the response defaults must reflect this.
- Addressee block missing the supervisory office. "FRB" or "OCC" alone is insufficient; the supervisory office and the regulator together are the convention.
- Heightened Standards linkage missing on Heightened-Standards-covered banks. For findings that implicate the risk governance framework, the RAS, or roles and responsibilities, the response must surface the linkage explicitly.
- LFI rating linkage missing on LFI-rated BHCs. For findings that may affect the next LFI rating cycle, the response acknowledges the rating context.
- Concentration of root cause across multiple findings ignored. Where a recurring root cause shows in multiple open findings, the response surfaces this concentration; treating each finding in isolation invites the supervisor to point out the pattern.
- Personal names in the addressee or signatory blocks. Banking convention is roles, not personal names; personnel rotate, and the response may be filed and read months or years later.

## capital-markets

### Capital-markets sector overlay for management-response

When the scope record names `capital-markets` for a management-response engagement, this overlay sets markets-supervisor and self-regulatory-organisation conventions for the response artifact.

Loaded by: `management-response/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- SEC Division of Examinations protocol: deficiency letters issued at the conclusion of broker-dealer, investment-adviser, registered-fund, and transfer-agent examinations, with the firm's response appended to the deficiency letter file.
- FINRA examination protocol: deficiency letters issued by FINRA at the conclusion of broker-dealer examinations under FINRA Rule 9000 series; FINRA Rule 4530 (reporting requirements) for related event reporting.
- CFTC examination conventions for futures commission merchants and swap dealers, under CFTC Regulation 1.10 series and the National Futures Association's parallel examination framework.
- Investment Advisers Act Rule 206(4)-7 (compliance program rule) and Investment Company Act Rule 38a-1 (fund compliance program rule) — the underlying obligations frequently cited in adviser and fund examination findings.
- Exchange Act Rules 15c3-1 (net capital) and 15c3-3 (customer protection) — frequently cited in broker-dealer examination findings.

#### What changes for capital-markets-flagged management responses

##### 1. Addressee conventions

- **SEC EXAMS deficiency letters**: addressee is the SEC examination office identified in the deficiency letter (the regional office or the home-office division). The response form follows the SEC's deficiency-letter protocol; the response is typically due within 30 days of the deficiency letter date unless the SEC specifies otherwise.
- **FINRA examination findings**: addressee is the FINRA examination office identified in the deficiency letter. The response form follows FINRA's protocol; typical response window is 30 days.
- **CFTC and NFA findings**: addressee is the CFTC division office or the NFA examination office, per the communication. CFTC findings on registered FCMs and SDs are coordinated with NFA where NFA conducts the examination.
- **Disclosure Effectiveness Initiative comments and other SEC Corporation Finance comments**: separate workflow; not in scope for this overlay (those go through securities counsel, not through the management-response artifact).

##### 2. Severity convention

SEC EXAMS and FINRA examination findings use a different severity convention from the federal-banking-agency MRA / MRIA distinction:

- **Deficiencies** — formal findings of non-compliance or weakness; the firm is expected to respond with a remediation plan. The deficiency-letter cover identifies whether the SEC or FINRA may make a referral to enforcement.
- **Risk Alerts and observations** — informal findings that the firm may consider but is not required to remediate; the response (where the firm chooses to file one) is shorter.
- **Enforcement referral indicators** — language in the deficiency letter that signals possible enforcement consideration; the response is typically reviewed by securities counsel before submission and may not follow the standard management-response form (counsel may direct a different posture, including silence pending counsel-led engagement with the staff).

##### 3. Response window and form

- **SEC EXAMS**: 30-day response window typical; the response is a written letter from the firm (commonly signed by the CCO of the registered entity, or by the CEO for material deficiencies). The response is appended to the deficiency-letter file and read at the next examination cycle.
- **FINRA**: 30-day response window typical; the response is a written letter signed by the responding role at the broker-dealer (commonly the CCO or the CEO for material deficiencies). Material deficiencies may also trigger a Wells process; counsel-led if so.
- **Item 1.05 / 8-K interaction**: where the underlying event is a cybersecurity incident that may also trigger 8-K Item 1.05 disclosure obligations on the public-company parent, the management response and the disclosure decision are separate workflows. The response carries cross-link to `cyber-disclosure-readiness` for the disclosure-process referral.

##### 4. Linkage to compliance program rules

For investment advisers, findings frequently cite Rule 206(4)-7 (the compliance program rule); the response identifies which element of the compliance program (written policies and procedures; annual review; chief compliance officer designation) the finding implicates.

For registered funds, findings frequently cite Rule 38a-1 (the fund compliance program rule); the response identifies the implicated element including fund-board oversight where applicable.

For broker-dealers, findings frequently cite supervisory rules (FINRA Rule 3110 supervision; FINRA Rule 3120 supervisory control system); the response identifies the implicated element of the supervisory system.

##### 5. Adviser-firm vs fund-board scope

Where the finding touches a registered fund as well as the adviser, the response distinguishes adviser-firm scope from fund-board scope:

- Adviser-firm response is filed by the adviser to the SEC; addressed to the SEC examination office.
- Fund-board response is filed separately by the fund (signed by an officer of the fund or by an independent director of the fund board); addressed to the SEC examination office.
- Where the same finding affects both, the two responses cross-reference; the substantive remediation may be common, but the responding entities and signatories are different.

##### 6. Cross-link to other capability skills

- Underlying issue write-up: `issue-writeup`.
- Standing committee pack carrying the finding ageing: `risk-committee-pack` (issues-and-remediation-status section); for advisers and BDs, this is the firm-level enterprise risk committee pack.
- Cyber-disclosure interactions: `cyber-disclosure-readiness` (8-K Item 1.05 and Item 106 mechanics for the public parent).
- Consumer-conduct findings: `references/cross-cutting.md#conduct` for findings touching retail-investor protection.

#### Capital-markets-specific output additions

Added to the response (mapped to schema where present):

- `addressee.addressee_name` — markets-supervisor convention names the SEC examination office, the FINRA office, or the CFTC / NFA office. Personal names are not used.
- `reporting_cadence.frequency` — typically event-driven for SEC and FINRA deficiency-letter responses (the firm reports on completion of milestones rather than on a fixed cadence), unless the staff specifies otherwise.
- `firm_level_signatory_role` — populated for material deficiencies (typically CCO of the registered entity or CEO for the most material findings); typically the CCO for routine deficiencies.
- `linked_finding_ids` — capital-markets responses commonly cross-link to fund-board responses on the same finding for adviser-fund matters.

#### Common pitfalls in capital-markets-flagged management responses

- Treating an SEC EXAMS deficiency letter as a banking-style MRA. The conventions are different; the response form, the response window, and the severity language follow the SEC's protocol.
- Missing the 30-day response window. SEC and FINRA deficiency letters typically specify 30 days; the action-plan section must reflect the response-window constraint, with milestones inside the window where possible and longer-horizon milestones flagged.
- Adviser-firm response collapsing fund-board scope. Where the finding affects a registered fund, the fund's response is filed separately by the fund; collapsing the two creates governance confusion.
- Securities-counsel review missing on enforcement-referral-indicator language. Where the deficiency letter signals possible enforcement consideration, counsel should review the response before submission; the skill flags this and stops if the responding role has not engaged counsel.
- Compliance program rule linkage missing. Findings citing Rule 206(4)-7, Rule 38a-1, or the FINRA supervision rules should identify the implicated element of the compliance or supervisory program.
- Personal names in the addressee or signatory blocks. SEC and FINRA convention is offices and roles, not personal names.

## insurance

### Insurance sector overlay for management-response

When the scope record names `insurance` for a management-response engagement, this overlay sets state-DOI-shaped and NAIC-peer-review-shaped conventions for the response artifact.

Loaded by: `management-response/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- State Insurance Department examination conventions vary by lead state; the NAIC Financial Condition Examiners Handbook sets the framework most state DOIs follow but does not bind the response form, which is the lead-state DOI's call.
- NAIC Risk Management and Own Risk and Solvency Assessment Model Act (#505) and ORSA Guidance Manual — for findings touching the firm's ORSA framework or the ORSA Summary Report content, the response references the Model #505 framework.
- NAIC Insurance Holding Company System Regulatory Act (Model #440) — for findings touching the holding-company-level risk reporting expectations.
- NAIC Accreditation Standards — for findings flowing from NAIC accreditation peer reviews of the lead state's regulatory program (these are the lead state's findings, not the firm's, but the firm may be in scope as a sample subject).
- NAIC Insurance Data Security Model Law (Model #668) — for cyber-related insurance examination findings in adopting states.

#### What changes for insurance-flagged management responses

##### 1. Addressee conventions

- **Lead-state DOI findings**: addressee is the lead state Insurance Department's named examination office (e.g., "Insurance Department of [state], [bureau]"). The response form follows the lead state's examination protocol; common forms include a written response appended to the examination report and a separate corrective-action plan.
- **Multi-state coordinated examination findings**: where multiple state DOIs participated in the examination, the response is typically addressed to the lead state with copies to participating states. The lead-state's communication identifies the addressee convention.
- **NAIC-led findings**: where a finding is communicated through an NAIC committee or working group (less common; the firm is typically in scope as a sample subject of an accreditation review or a Holding Company Working Group review), the addressee is the NAIC committee chair via the lead state.

##### 2. Severity convention

State DOI examination findings are typically less stratified than the federal-banking-agency MRA / MRIA distinction. Common conventions:

- **Recommendations** — informal observations that the firm is expected to consider but not required to remediate; the response may acknowledge without a full action plan.
- **Required corrective actions** — formal findings the firm is required to remediate; the response carries the full action-plan, evidence-of-effectiveness, and reporting-cadence sections.
- **Material findings** — the most serious tier (used variously by states; some use "material adverse findings" or similar terms); the response carries a more rapid cadence and a more senior firm-level signatory (commonly the President or CEO of the regulated entity in addition to the responding role).

##### 3. Linkage to ORSA framework

For insurers above the Model #505 premium threshold ($500 million single insurer, $1 billion group as adopted by most states), findings that touch the risk-management framework or the ORSA process typically require the response to acknowledge:

- Which ORSA Summary Report section the finding relates to (Section 1 Description of the Insurer's Risk Management Framework; Section 2 Insurer's Assessment of Risk Exposure; Section 3 Group Risk Capital and Prospective Solvency Assessment).
- Whether the next ORSA Summary Report will reflect the remediation; if not, the response identifies the timing relative to the next filing.
- Whether the finding implicates the firm's risk-management policies, in which case the policy revision is itself a milestone in the action plan.

##### 4. Linkage to Holding Company supervision

For insurance holding companies in scope of Model #440, findings touching enterprise-risk-management at the holding-company level typically require the response to acknowledge:

- The Form F (Enterprise Risk Report) implications, where the finding affects content in or omitted from the Form F.
- The lead-state coordination implications, where the finding affects entities in multiple states.

##### 5. Cross-link to other capability skills

- Underlying issue write-up: `issue-writeup`.
- Standing committee pack carrying the finding ageing: `risk-committee-pack` (issues-and-remediation-status section).
- Cyber findings (where Model #668 or Part 500 applies): `references/cross-cutting.md#cyber` and `cyber-disclosure-readiness`.

#### Insurance-specific output additions

Added to the response (mapped to schema where present):

- `addressee.addressee_name` — insurance convention names the lead state DOI examination office; for multi-state examinations, the participating states are listed in the addressee block as copy recipients.
- `finding_reference.finding_type` — insurance findings often map to "external-assessor-finding" in the schema enum where the regulator is a state DOI; alternatively, the firm may set its own internal taxonomy and use "other" with a free-text label.
- `reporting_cadence.frequency` — typically aligned to the firm's ORSA filing cycle (annual) for ORSA-related findings, with interim updates as the lead state requests.
- `linked_finding_ids` — for multi-state examinations, the response cross-links to any related findings from participating states.

#### Common pitfalls in insurance-flagged management responses

- Treating a state DOI examination finding as a federal-banking-style MRA. The conventions are different; the response form follows the lead state's protocol, not the SR-13-13 framework.
- Missing the ORSA linkage on Model #505-relevant findings. Findings that touch the ORSA framework should reference the relevant ORSA Summary Report section explicitly.
- Missing the lead-state convention for multi-state coordinated examinations. The response addressee, copy recipients, and cadence follow the lead state's specification.
- Treating Holding Company supervision as out of scope when the finding touches enterprise-risk-management at the parent. Form F implications are typically a topic the lead state will press on at the holding-company level.
- Personal names in the addressee or signatory blocks. State DOI convention is roles and offices, not personal names.

## payments-fintech

### Payments-fintech sector overlay for management-response

When the scope record names `payments-fintech` for a management-response engagement, this overlay sets consumer-protection-supervisor, state-money-transmitter-licensor, and bank-partnership conventions for the response artifact.

Loaded by: `management-response/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- CFPB supervisory communications including Potential Action and Request for Response (PARR) letters, supervisory letters, and examination findings under 12 CFR Part 1090 (consumer-protection supervision over larger participants in defined markets) and the agency's general supervisory authority.
- State money-transmitter examination conventions (vary by state); the Multistate MSB Licensing Agreement Program (MMLA) provides coordination for many state licensees, but the response form follows the lead state's protocol.
- Federal banking agencies' interagency third-party risk management guidance (June 2023) — for findings flowing through a sponsor bank to a fintech bank-partnership program.
- CFPB Compliance Bulletins and Circulars — interpretive guidance frequently cited in CFPB findings.
- State unfair-deceptive-acts-and-practices (UDAP) statutes — for state-attorney-general findings on consumer-conduct issues.

#### What changes for payments-fintech-flagged management responses

##### 1. Addressee conventions

- **CFPB findings**: addressee is the CFPB supervisory office identified in the communication (typically the assigned examiner-in-charge in the supervisory regional office). Response form follows the CFPB's protocol; PARR letters specifically have a defined response procedure.
- **State money-transmitter examination findings**: addressee is the lead state's Department of Financial Institutions or money-transmitter regulator (varies by state; in some states the Department of Banking or Department of Financial Services). For multi-state coordinated examinations under the MMLA, the lead state convention applies.
- **Sponsor-bank examination findings flowing to the fintech**: addressee is the sponsor bank's designated relationship office (the fintech's response is to the sponsor bank, who carries the response forward to the federal banking agency); the response form follows the sponsor bank's protocol, which typically follows the federal banking agency convention.

##### 2. PARR letter convention

The CFPB's Potential Action and Request for Response letter is a distinct supervisory communication where the CFPB notifies the firm that the agency is considering enforcement action and invites a response. PARR responses are counsel-led; the management-response artifact is one input to the counsel-led response, not a substitute for it.

The skill flags PARR letter responses as requiring counsel review and stops if the responding role has not engaged counsel. The action-plan section may be deferred or partial pending counsel direction.

##### 3. Sponsor-bank-program findings

For fintech firms operating under a sponsor-bank relationship, findings from the sponsor bank's federal banking agency examination of the bank-partnership program flow through the sponsor bank to the fintech. The response convention follows the sponsor bank's protocol, which typically follows the federal banking agency convention but is filtered through the sponsor bank's relationship-management framework.

The response carries:

- The original finding text from the federal banking agency examination (verbatim, per the standard rule).
- The sponsor bank's communication of the finding to the fintech (verbatim where the sponsor bank's communication adds substance).
- The fintech's action plan, which typically includes both (a) actions the fintech takes directly and (b) actions taken in coordination with the sponsor bank.
- A separate field for the sponsor-bank coordination role (the named contact at the sponsor bank to whom the fintech reports progress).

##### 4. State money-transmitter coordination

For multi-state coordinated examinations under the MMLA, the response is typically addressed to the lead state with copies to participating states. The lead-state convention determines the response form, the response window, and the closure procedure. State variations are common; the skill defaults to the lead state's specification.

##### 5. Consumer remediation strand

CFPB findings and state-attorney-general findings frequently turn on remediation the firm owes affected consumers in addition to control redesign. The response carries the consumer-remediation strand alongside the control strand:

- Consumer-remediation methodology (how the affected consumer population is identified; what restitution is owed; how restitution is delivered).
- Consumer-remediation timeline (how quickly affected consumers are notified and made whole; consumer-notice form).
- Consumer-remediation reporting (how the firm reports consumer-remediation completion to the supervisor, separately from control-redesign reporting).

The conduct cross-cutting overlay (`references/cross-cutting.md#conduct`) covers this in more depth.

##### 6. Cross-link to other capability skills

- Underlying issue write-up: `issue-writeup`.
- Standing committee pack: `risk-committee-pack` (issues-and-remediation-status section).
- Consumer-conduct overlay: `references/cross-cutting.md#conduct`.
- Privacy overlay where the finding touches consumer data: `references/cross-cutting.md#privacy`.

#### Payments-fintech-specific output additions

Added to the response (mapped to schema where present):

- `addressee.addressee_name` — payments-fintech convention names the CFPB supervisory office, the lead state DFI, or the sponsor-bank relationship office, per the finding source.
- `finding_reference.finding_type` — `parr` for CFPB PARR letters; `external-assessor-finding` or `other` for state-money-transmitter examination findings (the schema enum may need extension in subsequent versions).
- `reporting_cadence.frequency` — varies by source; CFPB findings typically quarterly written reports until closure; state findings vary by lead state.
- `linked_finding_ids` — payments-fintech responses commonly cross-link to sponsor-bank examination findings or to state-coordinated findings across multiple state licensees.

#### Common pitfalls in payments-fintech-flagged management responses

- Treating a CFPB PARR letter as a routine supervisory finding. PARR letters are counsel-led; the management-response artifact is not the response form for a PARR.
- Sponsor-bank-program response collapsing the federal banking agency finding into the fintech's internal taxonomy. The original federal-banking-agency finding text must be quoted verbatim; the sponsor-bank's filter is documented separately.
- Multi-state response addressed only to the firm's home state. For MMLA-coordinated examinations, the response addressee follows the lead state with copies to participating states.
- Consumer-remediation strand omitted on consumer-protection findings. Findings from the CFPB or state attorneys general frequently turn on consumer remediation; the response carries this strand alongside the control strand.
- Counsel review missing where the finding indicates possible enforcement consideration. CFPB findings can escalate quickly; counsel review is typical, and the skill flags this.
- Personal names in the addressee or signatory blocks. Payments-fintech convention is offices and roles; sponsor-bank relationship contacts may be named by role (e.g., "VP, Bank-Partnership Risk").
