# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## 10k-item-106-large-accelerated-filer

### Example: 10-K Item 106 disclosure refresh for a large accelerated filer

Public-source-derived, no named institution. Structural reference patterns are public 10-K Item 106 disclosures filed in 2024 spring and 2025 spring filing seasons (e.g., the structural pattern in JPMorgan Chase's 10-K Item 106 filed February 2024 and the structural pattern in Bank of America's 10-K Item 106 filed February 2024 [verify section references at draft time]) — used as structural references only; this example does not claim or copy substantive disclosure language.

#### Input

- Institution: a large accelerated filer; SEC-registered bank holding company; with state-member-bank subsidiary, registered broker-dealer subsidiary, and registered investment adviser subsidiary. NYDFS-licensed.
- Engagement scope supplied: primary regulators FRB, OCC, NYDFS, SEC; persona = head of disclosure preparing 10-K cycle; sector overlays = banking, capital-markets; cross-cutting overlays = cyber (core), climate.
- Trigger: large accelerated filer is preparing the FY 10-K. Item 106 was first disclosed in the prior-year 10-K. The second-line review function is refreshing Item 106 for the current year, with three changes: (1) a new third-party assessor engagement for cyber program review (replacing a different prior assessor); (2) a refreshed board-oversight cadence — cyber risk is now reported quarterly to the Risk Committee with an annual deep-dive to the full board (the prior-year cadence was twice-yearly to the Risk Committee with no full-board deep-dive); (3) a refreshed CISO function structure with a new dotted-line reporting to the CRO (the prior-year structure was solid-line to CIO only).
- Source posture: public (regulatory text); plus firm policy (information security policy, board charter, prior-year 10-K Item 106, Risk Committee charter); plus system of record (board minutes through the period, cyber-risk-register output, third-party assessor engagement letter and report).
- Material effects to date: zero material cybersecurity incidents in the FY period; prior-year period had one incident filed under Item 1.05 (currently in remediation; carried through this year's material-effects narrative).
- Filer category: large accelerated filer. Item 106 is in scope (effective for FY ending on or after December 15, 2023).

#### Output sketch

The skill emits a markdown pack and the structured record. Headlines from Artifact B:

- **Filing context**: filing period end = December 31; filing type = 10-K; prior-year filing reference (filed February of prior year); year-over-year diff scope = "material refresh" (three substantive changes named above).
- **Item 106(b) draft** — five discrete subsections per the rule's required elements:
  - 106(b)(1) processes — describes the firm's cyber risk-management lifecycle: identification, assessment, mitigation, monitoring; references the firm's information-security program in FFIEC-aligned terms (because the firm operates against FFIEC expectations and the language is internally consistent); does not name FFIEC but uses the program's vocabulary.
  - 106(b)(1)(i) integration — describes how the cyber risk-management processes integrate into the firm's enterprise risk-management framework; cyber is a separately-rated risk category in the enterprise heat map (consistent with the firm's risk taxonomy).
  - 106(b)(1)(ii) third-party engagement — describes the firm's engagement of independent third-party assessors for periodic cyber-program review; does not name the assessor entity (the rule does not require it); discloses that the firm replaced its prior assessor with a new assessor for the current year and the current year's assessment is in progress.
  - 106(b)(1)(iii) third-party service-provider oversight — describes the firm's third-party risk management program for cyber including critical-vendor cyber-attestation, ongoing monitoring, contractual incident-notification provisions, and concentration-risk view; references the firm's TPRM framework consistent with interagency third-party risk management guidance.
  - 106(b)(2) material effects — names the prior-year incident (with reference to the prior-year 8-K Item 1.05 filing accession), summarizes its current remediation status, and concludes that it has not had, and is not reasonably likely to have, a material effect on the firm's business strategy, results of operations, or financial condition based on facts known as of the filing date.
- **Item 106(c) draft** — two discrete subsections:
  - 106(c)(1) board oversight — names the Risk Committee of the Board with cyber oversight; describes the cadence (refreshed: quarterly committee briefings, annual full-board deep-dive); describes the processes by which the Risk Committee is informed (CISO written report ahead of each meeting; quarterly KRI dashboard; ad-hoc briefings on material incidents and on supervisory-finding updates).
  - 106(c)(2) management role — names the CISO as the management position responsible for cyber risk; describes the named expertise (CISO with named credentials and prior experience; new dotted-line reporting to CRO is described); describes the reporting line to the board through the CRO and the Risk Committee Chair; describes the firm's Cybersecurity Steering Committee (chaired by the CISO with members from operational risk, technology, audit, GC office, business-unit heads).
- **Material effects to date — structured record**: one entry for the prior-year incident, with affected period (prior-year FY), effect summary (one paragraph), linked 8-K Item 1.05 reference (filing date and accession number).
- **Source trace per claim** — each governance and risk-management assertion is anchored:
  - Risk Committee oversight assertion → Risk Committee charter section + board minutes through the FY.
  - Quarterly cadence → board calendar + Risk Committee meeting minutes.
  - Full-board deep-dive → board calendar + full-board meeting minutes for the annual session.
  - CISO function structure → information security policy + organization chart effective dates + HR record of CRO dotted-line reporting effective date.
  - Third-party assessor engagement → engagement letter + scope-of-work document.
  - Cybersecurity Steering Committee → committee charter + meeting minutes.
- **Year-over-year diff** — one row per Item 106 element with prior-year text, current-year text, and rationale:
  - 106(b)(1)(ii) third-party assessors: rationale = "new assessor engaged for current year"; the diff is substantive.
  - 106(c)(1) board oversight: rationale = "cadence refreshed from twice-yearly Risk Committee to quarterly Risk Committee plus annual full-board deep-dive, effective Q1 of FY".
  - 106(c)(2) management role: rationale = "CISO function structure refreshed with new dotted-line reporting to CRO, effective Q2 of FY".
  - Other elements: rationale = "no substantive change — refreshed for currency".
- **Sign-off block**: head of disclosure, securities counsel, CISO, audit-committee secretary acknowledgement, disclosure committee chair; sign-off date.
- **Reviewer questions for the disclosure committee**: (1) the FFIEC-program-aligned language in 106(b)(1) is internally consistent with the firm's information-security policy; does the disclosure committee want explicit FFIEC reference in the disclosure or to retain the program-vocabulary-only treatment; (2) the new third-party assessor's engagement is in progress with the report due in Q2 of next year; does the disclosure address that timing or refer to it as "ongoing"; (3) the CISO-to-CRO dotted-line reporting refresh is recent (Q2 of current year); how does the disclosure committee want to characterize the maturity of the new structure; (4) the prior-year incident's current remediation status is described in 106(b)(2); does the disclosure committee want any additional detail on remediation milestones or hold to the materially-affected language; (5) the Risk Committee charter section reference is to the prior-year charter; has the charter been refreshed in the current year and if so, the source-trace pointer should reference the current charter.
- **Confidence label** = high on governance posture (well-evidenced through board minutes, charters, organization-chart records); medium on certain risk-management process claims pending the third-party assessor sign-off in Q2 of next year. Confidence label per the schema = medium overall (taking the lower of the discrete-section confidences).
- **Verification flags carried forward**: SEC C&DIs for Item 106 (verify current question numbers); FFIEC IT Handbook section labels (verify); prior-year 8-K Item 1.05 filing accession (verify against EDGAR).

#### Why this scenario matters

- Item 106(b) and Item 106(c) are discrete subsections; rolling them together is the failure mode. The pack treats each required element as a discrete row.
- Year-over-year diff and rationale is required. "Rolled forward unchanged" Item 106 is a frequent finding; this example shows three substantive changes documented with effective dates and rationale.
- "Material effects to date" is treated as a stated determination. The empty case (no current-period incidents) and the non-empty case (the prior-year incident with linked 8-K Item 1.05 reference) are both addressed substantively.
- Specific titles and qualifications matter in 106(c). The example names the Risk Committee, the cadence, the CISO function structure, and the Cybersecurity Steering Committee. Generic "the appropriate management committee" reads as boilerplate.
- Source trace per claim links each governance assertion to a board minute, charter section, organization-chart record, or policy reference. The source-trace block is the evidence the disclosure committee and the audit-committee secretary review before sign-off.
- The confidence label is honestly mixed (high on governance, medium on risk-management pending the new assessor sign-off). The schema treats the overall label as the lower bound; reviewer questions surface where the label is medium.

#### Anchors

- SEC Final Rule (Release Nos. 33-11216 / 34-97989), Reg S-K Item 106(b), 106(c).
- Exchange Act Rule 13a-15 (DCP).
- FFIEC IT Examination Handbook, Information Security booklet (September 2016).
- 12 CFR Part 30 Appendix D (OCC Heightened Standards) — Section IV's independent risk committee expectations.
- Interagency Guidance on Third-Party Relationships (June 2023) — for the 106(b)(1)(iii) third-party service-provider oversight content.
- SEC Compliance and Disclosure Interpretations (C&DIs) on Item 106.

See `references/source-anchors.md` for full citations and verification flags.

## 8k-item-105-bank-affiliated-registrant

### Example: 8-K Item 1.05 trigger pack for a bank-affiliated SEC registrant

Public-source-derived, no named institution. The structural reference patterns are public 8-K Item 1.05 filings from calendar year 2024 (the early Item 1.05 filings post-effectiveness, which set the four-element disclosure pattern: nature, scope, timing, material impact / reasonably likely material impact).

Verification posture: the Microsoft 8-K filed January 17, 2024 and the UnitedHealth Group / Change Healthcare 8-K filed February 22, 2024 are public structural references for the four-element pattern. This example does not name either; it adapts the pattern to a hypothetical bank-affiliated registrant. The MGM Resorts 8-K filed September 12, 2023 was a pre-Item-1.05 filing under Item 8.01 and is not an Item 1.05 reference.

#### Input

- Institution: a bank holding company SEC registrant with a state-member-bank subsidiary (covered by 12 CFR Part 225 Subpart N), a NYDFS-licensed national-bank subsidiary, a registered broker-dealer subsidiary, and a registered investment adviser subsidiary. Large accelerated filer.
- Engagement scope supplied: primary regulators FRB, OCC, NYDFS, SEC; persona = head of disclosure, with disclosure committee and securities counsel as named reviewers; sector overlays = banking, capital-markets; cross-cutting overlays = cyber (core), privacy.
- Trigger: on Monday morning, the firm's SOC detected unauthorized access to a customer-information system at the broker-dealer subsidiary. Initial scope assessment confirmed access to customer account information (names, account numbers, SSNs); the count of affected customers was estimated at 50,000 to 200,000 and was being refined. The CISO briefed the head of operational risk and the GC office Monday afternoon. The disclosure committee was convening Tuesday morning to discuss materiality.
- Source posture: public (regulatory text); plus firm policy (firm's DCP, the disclosure-committee charter, the materiality-determination protocol); plus system-of-record evidence (incident-response system, materiality-workpaper template, draft 8-K body).
- Filer category: large accelerated filer. The 8-K Item 1.05 is in scope (effective December 18, 2023 for non-SRC filers).

#### Output sketch

The skill emits a markdown pack and three structured records (one per artifact, but for this trigger only Artifact A is in scope; Artifacts B and C are referenced but not produced).

Headlines from Artifact A:

- **Cover and clock posture**: incident reference INC-2026-0042; detection Monday 06:14 ET; materiality determination "pending" as of Tuesday 09:00 ET (committee in session); disclosure clock has not started (clock starts at materiality determination, not detection); filing-clock posture = "pending — materiality call in session".
- **Incident timeline** distinguishes knowns (unauthorized access detected Monday 06:14; containment achieved Monday 14:00; vendor incident-response engaged Monday 17:00) from unknowns (full scope; whether SSNs were exfiltrated as opposed to merely accessed; whether other systems were touched; whether the threat actor had broader access than confirmed).
- **Materiality determination workpaper**:
  - Facts: unauthorized access to a customer-information system; 50,000-200,000 customer estimate, refining; access confirmed; exfiltration unconfirmed; containment achieved.
  - Reasonable-investor analysis: applying the TSC / Basic standard, the disclosure committee considers whether a reasonable investor would consider this incident important to an investment decision. Quantitatively the financial impact is modest in isolation; qualitatively the customer-impact count and the reputational dimension are weighty. The probability-magnitude analysis under Basic considers reasonably foreseeable consequences (customer-remediation cost, potential follow-on enforcement actions from NYDFS or SEC, possible class-action exposure).
  - Quantitative impact: financial impact estimate $5M to $25M direct response cost (range; confidence medium); customer-impact count 50,000 to 200,000 (refining); operational-impact summary = customer-information-system access, no operational disruption.
  - Qualitative impact: reputational (high; customer-impact count is the driver); regulatory (NYDFS examination engagement likely; SEC Reg S-P customer-notice trigger likely); strategic (modest); competitive (modest).
  - Aggregation analysis: prior incidents in the period reviewed; one prior phishing campaign in Q1 affected 200 customers and was determined not material on its own; Instruction 1 aggregation analysis under Item 1.05 considered; aggregation conclusion = the prior incident does not aggregate with this one (different threat actor, different attack vector, different system); empty-array aggregation is a stated determination, documented.
  - Determination = pending (committee in session). Once determined, `disclosure_clock_start` populates with the determination datetime and `disclosure_filing_due` computes as 4 business days from that.
- **Item 1.05 disclosure draft (placeholder, pending determination)**: drafted to the four required elements with "to the extent known" framing on scope and impact. Forensic detail (specific systems, threat-actor identification, IOCs, remediation specifics) is held out of the draft.
- **Delay-provision analysis**: not invoked. Rationale: the incident does not pose a substantial risk to national security or public safety. AG notification process not initiated.
- **Parallel-clocks table** (the row securities counsel pulls on first):

  | Regulator | Clock basis | Status |
  |---|---|---|
  | SEC (8-K Item 1.05) | 4 business days from materiality determination | pending (clock not started) |
  | OCC (12 CFR Part 53) | 36 hours from determination of notification incident | NOT-APPLICABLE (national-bank subsidiary not directly affected; incident is at broker-dealer subsidiary) |
  | FRB (12 CFR Part 225 Subpart N) | 36 hours from determination of notification incident | UNDER REVIEW (BHC consolidation question; head of operational risk evaluating whether the broker-dealer-subsidiary incident is material to BHC operations) |
  | NYDFS (23 NYCRR Part 500 §500.17) | 72 hours from determination of cybersecurity event | IN-PROGRESS (NYDFS-licensed national-bank subsidiary; CISO determined cybersecurity event Monday 14:00; clock starts there) |
  | SEC Reg S-P (17 CFR Part 248.30) | 30 days from awareness of unauthorized access (broker-dealer is covered institution) | IN-PROGRESS (Reg S-P clock running from Monday morning detection of unauthorized access; customer-notice content being drafted in parallel) |
  | State breach-notification (CA, NY, TX, IL, MA most cited; full state map TBD) | varies by state | IN-PROGRESS (state-by-state customer count being mapped) |
  | FINRA Rule 4530(a) | 30 days from event (FINRA-member broker-dealer) | UNDER REVIEW (whether 4530(a)(1) regulatory-action trigger applies depends on regulatory-engagement posture) |
  | Counterparty contractual | per contract | IN-PROGRESS (clearing-broker and custodian agreements identified; notifications being drafted) |

  The SEC clock has not started. Several other clocks have. Senior reviewer's job: resolve in parallel.
- **DCP trace**: detection (SOC analyst, Monday 06:14, log pointer); triage (IR lead, Monday 06:30, triage record pointer); containment (IR lead with vendor support, Monday 14:00, containment memo pointer); escalation to second line (CISO to head of operational risk, Monday 14:30, escalation memo pointer); escalation to GC office (head of operational risk to deputy GC for securities, Monday 16:00, escalation memo pointer); escalation to disclosure committee (committee secretary, Monday 18:00, convening notice pointer); materiality call (disclosure committee in session, Tuesday 09:00, meeting minutes pending). The trace is the evidence that DCP functioned for cyber.
- **Sign-off block**: committee chair, securities counsel, CISO, CFO; sign-off date pending materiality determination.
- **Reviewer questions for the disclosure committee**: (1) does the customer-impact-count uncertainty (50K-200K range) prevent a current materiality determination, or is the worst-case basis sufficient under the "to the extent known" framing; (2) does the prior Q1 phishing-campaign aggregation analysis hold given a different threat actor and different system; (3) the Reg S-P 30-day clock has started; should the 8-K filing precede the Reg S-P customer notice or follow it; (4) is the BHC-consolidation question on the federal banking agency 36-hour clock resolved.

#### Why this scenario matters

- The 4-business-day clock starts at materiality determination, not at detection. The pack rejects any draft that conflates these; the schema computes `disclosure_filing_due` from `materiality_determination_date`, and the clock-not-started posture is a stated determination.
- Aggregation analysis under Item 1.05 Instruction 1 is surfaced explicitly even when the conclusion is that prior incidents do not aggregate. Empty-array aggregation is a stated determination, documented.
- The Item 1.05 disclosure draft holds to the four required elements only. Forensic detail and remediation specifics are kept out.
- The parallel-clocks table is multi-regulator. The SEC clock is one row among several; for a bank-holding-company registrant with a NYDFS-licensed banking subsidiary and a FINRA-member broker-dealer subsidiary, the count of regulator clocks running on a single incident is high, and the senior reviewer's job is to resolve them in parallel.
- The DCP trace is the evidence that the firm's disclosure controls and procedures functioned for cyber. The trace is what an SEC enforcement question, an examination engagement, or a future MWA-equivalent finding tests.
- Confidence label = medium (scope determination ongoing; customer-impact count refining); human review required = yes; the materiality-call meeting minutes attach the workpaper.

#### Anchors

- SEC Final Rule (Release Nos. 33-11216 / 34-97989), Form 8-K Item 1.05, Reg S-K Item 106.
- Exchange Act Rule 13a-15 (DCP).
- TSC Industries v. Northway, 426 U.S. 438 (1976); Basic v. Levinson, 485 U.S. 224 (1988).
- 12 CFR Part 225 Subpart N (FRB Computer-Security Incident Notification Rule).
- 23 NYCRR Part 500 §500.17.
- 17 CFR Part 248.30 (Reg S-P, May 2024 amendments).
- FINRA Rule 4530.

See `references/source-anchors.md` for full citations and verification flags.

## troubleshooting

### Troubleshooting: cyber-disclosure-readiness

Recurring failure modes when a cyber-disclosure-readiness pack looks complete but is not. The reviewer review should catch these; the builder review should preempt them.

#### Disclosure clock conflated with detection

Symptom: `disclosure_clock_start` populated with the detection date; `disclosure_filing_due` computed as 4 business days from detection.

Why it happens: detection feels like the natural starting event; the rule's "from materiality determination" language is easy to read past.

Fix: the 4-business-day clock starts at materiality determination, not detection. The schema's `disclosure_clock_start` equals `materiality_determination_date`; `disclosure_filing_due` computes from that. Detection-to-determination gap is a process metric (recorded in the DCP trace) and supports "without unreasonable delay" evidence; it is not the clock.

#### Materiality call treated as the cyber team's call

Symptom: workpaper's `materiality_determined_by_role` = "CISO" or "head of cyber risk".

Why it happens: cyber has the facts; "the cyber team made the call" feels natural.

Fix: materiality is a disclosure determination made by the disclosure committee with securities counsel input under the firm's DCP. The cyber team contributes facts and quantitative inputs; they do not own the determination. The standard composition is "disclosure committee chair, with securities counsel input"; the workpaper records this.

#### Item 1.05 disclosure draft over-discloses

Symptom: the draft includes forensic detail (specific systems named, IOCs, threat-actor identification, remediation specifics, vendor names). The draft reads like an incident-response status report rather than an investor disclosure.

Why it happens: the cyber team contributed the facts and the draft inherits the operational level of detail; the four-element structure is followed loosely or not at all.

Fix: Item 1.05 calls for nature, scope, timing, and material impact (or reasonably likely material impact). The draft holds to those four elements. Forensic detail, IOCs, named threat actors, remediation specifics, system-name detail belong in the incident-response file and not in the 8-K. Reg FD considerations and ongoing-investigation prejudice argue against them. The "to the extent known" framing handles incomplete scope determination.

#### Aggregation analysis missing or empty without documentation

Symptom: `aggregation_with_prior_incidents` is an empty array; `materiality_aggregation_analysis` is null.

Why it happens: empty array reads as "nothing to aggregate"; the analysis is treated as redundant.

Fix: empty-array aggregation is a stated determination, not an absence. Document the analysis: prior incidents in the period reviewed; reasoning that they do not aggregate (different threat actor, different attack vector, different system, distinct in time); empty-array conclusion is documented under Item 1.05 Instruction 1. The analysis is what a future enforcement question or audit pull tests.

#### SEC clock treated as the only clock

Symptom: parallel-clocks table contains one row (SEC 8-K Item 1.05). Federal banking agency 36-hour, NYDFS 72-hour, Reg S-P 30-day, state breach-notification, FINRA Rule 4530, HIPAA, counterparty contractual rows are absent.

Why it happens: the work is anchored to the SEC rule; other regulators feel "out of scope" for the disclosure pack.

Fix: the parallel-clocks table is multi-regulator by design. Surface every clock applicable to the registrant. For a typical bank-holding-company registrant with subsidiaries spanning bank, broker-dealer, and investment-adviser activities, the count of regulator clocks running on a single incident is high. Missing one is a frequent regulator finding.

#### Reg S-P treated as substitute for Item 1.05 (or vice versa)

Symptom: Reg S-P customer notice and 8-K Item 1.05 filing treated as two ways of saying the same thing.

Why it happens: both involve cyber and customer information; the distinction collapses.

Fix: the two notifications run on different audiences (investors versus affected individuals), different timing (4 business days from materiality determination versus 30 days from awareness of unauthorized access), and different content rules (four required elements versus the Reg S-P content elements). One does not satisfy the other; they are independent obligations.

#### Item 106 rolled forward unchanged

Symptom: `year_over_year_diff` is empty or all rationales = "no change". The disclosure is identical (or near-identical) to the prior year's.

Why it happens: Item 106 disclosure is annual and stable in its bones; refreshing it feels like make-work in the absence of changes.

Fix: year-over-year diff and rationale are required. Underlying facts (board cadence, management positions, third-party engagements, material effects) change. Even where no substantive change exists, "no substantive change, refreshed for currency" is a documented rationale, not a default. Rolled-forward-unchanged Item 106 is a frequent finding.

#### Item 106(c) board-oversight or management-role disclosure reads as boilerplate

Symptom: 106(c)(1) names "the appropriate management committee" or "an experienced senior management team"; 106(c)(2) names "the firm's cybersecurity organization" without specifics.

Why it happens: prior-year text was boilerplate, the refresh inherits the boilerplate, the substantive specifics are siloed elsewhere.

Fix: 106(c)(1) names the specific board committee (Risk Committee, Audit Committee, Cybersecurity Committee), the cadence (e.g., "quarterly Risk Committee briefings, annual full-board deep-dive"), and the processes by which the board or committee is informed. 106(c)(2) names the positions (CISO, CIO, CRO), the named expertise (credentials, prior experience, reporting line), and the management committees (e.g., Cybersecurity Steering Committee chaired by CISO). Specifics matter; reviewers flag boilerplate.

#### SEC Climate Disclosure Rule asserted as currently effective

Symptom: a climate-cross-cutting overlay claim asserts the SEC Climate Disclosure Rule is in force; references to current-effective status are unqualified.

Why it happens: the rule was finalized March 2024 and the headline regulatory change is memorable; the legal challenges and the SEC's voluntary stay are not.

Fix: never assert current effectiveness of the SEC Climate Disclosure Rule without checking SEC posture as of the report date. Default posture: cite the rule with `[verify current effectiveness]` and lean on TCFD or CSRD or state-required disclosure for substantive content. The cross-cutting climate overlay carries the verification discipline; SKILL.md and the source-anchors file flag the rule with the verification posture.

#### DCP trace incomplete

Symptom: DCP trace records detection and filing only; the intermediate stages (triage, escalation to second line, escalation to GC, escalation to disclosure committee, materiality call, disclosure decision) are absent.

Why it happens: the intermediate stages are operational and feel less load-bearing than the bookend events.

Fix: the DCP trace is the evidence that DCP under Rule 13a-15 functioned for cyber. Each stage carries the actor role, the timestamp, and a documentation pointer. Missing intermediate stages is what an SEC enforcement question, an examination engagement, or a future MWA-equivalent finding flags.

#### Foreign private issuer treated as domestic 8-K filer

Symptom: an FPI registrant's pack uses the 8-K Item 1.05 spine; references to Form 6-K and Form 20-F Item 16K are missing.

Why it happens: the scope did not flag FPI status, or the practitioner is operating off a domestic-issuer template.

Fix: FPIs are not subject to Form 8-K and therefore not subject to Item 1.05 directly. FPIs furnish on Form 6-K. Form 20-F Item 16K parallels Item 106 for FPI annual disclosure. The pack adapts to FPI mode when the filer category is named in the scope or in the cover.

#### Voluntary Item 1.05 filing for non-material incident

Symptom: `materiality_determination` = "not-material" but the disclosure is filed under Item 1.05 anyway, often with reduced safe-harbor language.

Why it happens: the firm wants to surface the incident publicly and Item 1.05 feels like the natural venue.

Fix: voluntary Item 1.05 filings receive reduced safe-harbor treatment per SEC staff C&DIs; voluntary disclosures should be filed under Item 8.01 (Other Events) with a narrative that does not invoke Item 1.05's materiality assertion. Artifact A's `materiality_determination` value of "not-material" prevents an Item 1.05 disclosure draft from emitting.

#### "Reasonably likely material impact" treated as speculative

Symptom: the disclosure draft excludes any forward-looking impact analysis on the rationale that current realized impact is below threshold.

Why it happens: "reasonably likely" reads as conjectural; the safer posture feels like sticking to realized.

Fix: the "or reasonably likely to materially affect" language has substance. Material impact reasonably foreseeable as of the determination date, even if not yet realized, is required disclosure. The workpaper's `materiality_basis_quantitative.financial_impact_reasonably_foreseeable` field captures the analysis; the disclosure draft surfaces it under the material-impact element.

#### Confidence label = "high" with non-empty verification-flag list

Symptom: the schema's `confidence_label` = "high" while the `verification_flags_carried_forward` array contains multiple unresolved items.

Why it happens: confidence is treated as an aspirational marker, not as a structured claim.

Fix: high confidence is incompatible with a non-empty verification-flag list. The label is medium at best where flags are present; the schema does not enforce this directly but the reviewer review does. The verification-flag list is the visible record of what is unresolved.

#### Pack stops too late

Symptom: the skill produces and asserts disclosure committee sign-off, files the 8-K, posts to the SEC reporting workflow.

Why it happens: builder over-runs the human-review gate.

Fix: the pack is a draft until the disclosure committee, securities counsel, and the named officers attest. The skill stops at the draft and surfaces the reviewer questions for the disclosure committee; it does not assert sign-off, file, or distribute.
