# cyber-disclosure-readiness — spec sheet

Plugin: `risk-reporting`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Drafts the second-line readiness pack for SEC cybersecurity disclosure: 8-K Item 1.05 trigger analysis, 10-K Item 106 governance and risk-management disclosure, materiality determination workpaper, and the disclosure-controls map. Output is a named-section pack a disclosure committee, securities counsel, or SEC reporting lead can take into the materiality call after qualified review.

Best for:
- A material cybersecurity incident has occurred (or is suspected) and the firm needs the materiality determination, the 8-K Item 1.05 trigger analysis, and the disclosure draft pulled together for the disclosure committee.
- The 10-K Item 106 cyber risk-management and governance disclosure is being refreshed for the upcoming filing cycle.
- The firm is standing up or refreshing its cyber disclosure controls and procedures (DCP) under Exchange Act Rule 13a-15 and needs the second-line readiness view.
- A regulator-driven climate-disclosure overlap question lands in the disclosure committee (because the same machinery — DCP, materiality, 8-K triggers — applies).

Not the right tool when:
- The artifact is the enterprise risk committee pack (use `risk-committee-pack`; cyber appears there as an overlay).
- The artifact is an internal incident response runbook (out of scope; this skill is the disclosure decision, not incident handling).
- The artifact is a vendor cyber due-diligence pack (use `third-party-operational-resilience/skills/vendor-diligence`).
- The trigger is a non-public regulator-only notification (e.g., NYDFS Part 500 §500.17 reporting). Use the regulator-specific notification skill in `third-party-operational-resilience` once it exists; this skill is SEC-disclosure-anchored.

Anchored to: SEC Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure final rule, Release Nos. 33-11216 / 34-97989 (July 26, 2023); Form 8-K Item 1.05 (material cybersecurity incidents); Form 8-K Item 1.06 (where applicable, foreign private issuers under Form 6-K); Regulation S-K Item 106 (cybersecurity risk management, strategy, and governance); Exchange Act Rule 13a-15 / 15d-15 (disclosure controls and procedures); SEC TSC Industries v. Northway materiality standard (1976) [verify pin cite]; SEC Climate Disclosure Rule (final March 2024) [verify current effectiveness — subject to litigation and stay history], for the disclosure machinery overlap.

## Source anchors

Primary (cyber):
- SEC Final Rule, Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure, Release Nos. 33-11216 and 34-97989, adopted July 26, 2023, effective dates phased from December 2023 (large filers) and June 2024 (smaller reporting companies). Use for: the binding text of Item 1.05 and Item 106. Section anchors:
  - Item 1.05 of Form 8-K — material cybersecurity incidents; 4-business-day filing window from the date the registrant determines materiality (not from the date of incident); content elements: nature, scope, timing, and material impact (or reasonably likely material impact). Delay provision under Section II.B requires US Attorney General notification of substantial risk to national security or public safety [verify pin cite of delay provision text].
  - Item 106 of Regulation S-K — cybersecurity risk management, strategy, and governance disclosures in 10-K. Subitems: 106(b) risk management and strategy; 106(c) governance (board oversight; management's role and expertise).
  - Form 6-K cross-references for foreign private issuers (Item 1.05 equivalent treatment).
- SEC Cybersecurity Disclosure FAQ / Compliance and Disclosure Interpretations (CD&Is) [verify current versions; SEC has issued staff guidance post-adoption]. Use for: incremental staff interpretations of "material" and the delay provision.
- TSC Industries, Inc. v. Northway, Inc., 426 U.S. 438 (1976), and Basic Inc. v. Levinson, 485 U.S. 224 (1988). Use for: the materiality standard the rule incorporates by reference (substantial likelihood that a reasonable investor would consider important) [verify pin cites].
- Exchange Act Rules 13a-15 and 15d-15. Use for: disclosure controls and procedures (DCP) framework that governs the trigger flow from incident detection through disclosure decision.

Secondary (cyber, supporting):
- NIST SP 800-61 Rev. 2, Computer Security Incident Handling Guide (2012). Use for: incident classification taxonomy that feeds the trigger analysis.
- FFIEC IT Examination Handbook, Information Security booklet (September 2016). Use for: incident-response control expectations cited in the 10-K Item 106 risk-management narrative.
- NYDFS 23 NYCRR 500 (Part 500), §500.17 (notice of cybersecurity event). [verify section after Part 500 amendments effective November 2023.] Use for: parallel regulator notification timelines that often run alongside the SEC Item 1.05 decision; the readiness pack must surface both clocks even though this skill is SEC-anchored.

Cross-cutting overlays (climate is required for this skill because the disclosure machinery overlaps):
- SEC Climate Disclosure Rule (Release Nos. 33-11275, 34-99678; final March 2024). [verify current effectiveness — the rule has been subject to legal challenges, was voluntarily stayed by the SEC pending judicial review, and current status must be checked at the report date.] Use for: the disclosure-machinery overlap. The DCP, the disclosure committee process, the materiality lens, and the 8-K / 10-K mechanics are common between cyber and climate; readiness assessments often run jointly. The cross-cutting overlay covers what the climate rule adds (Item 1500-series in S-K, financial-statement effects in S-X Article 14) without re-anchoring full climate sources.
- TCFD Recommendations (June 2017; Implementing 2021). Use for: where the firm reports climate voluntarily because SEC climate rule is not yet effective.

## Sector overlays needed

- `banking.md` — Covers FFIEC IT booklet incident-response expectations, OCC Bulletin 2023-17 (or successor) on cyber incident notification [verify], and the federal banking agencies' Computer-Security Incident Notification Rule (effective May 2022; 12 CFR Parts 53, 225, 304) [verify section]. The 36-hour bank-regulator notification clock often runs alongside the 4-business-day SEC clock; the readiness pack must show both.
- `insurance.md` — Covers NAIC Insurance Data Security Model Law (Model #668) [verify section] state adoption variation, and state DOI-specific cyber-event notification timelines.
- `capital-markets.md` — Covers SEC Regulation S-P amendments (May 2024) on customer-information incident notification [verify section, 30-day clock]; FINRA notification expectations under FINRA Rule 4530 where applicable [verify].
- `payments-fintech.md` — Covers PCI DSS notification obligations (contractual, not regulatory, but operationally adjacent), and CFPB supervisory expectations for large nonbanks; Reg E error-resolution clocks where customer transactions are affected.

## Cross-cutting overlays needed

- `cyber.md` — Required (this skill is the cyber disclosure skill; the cyber overlay is its core anchor set, kept here so the SKILL.md remains a workflow rather than a regulatory primer). Anchors: SEC Item 1.05, Item 106, Rule 13a-15; NIST SP 800-61; FFIEC IT booklet; NYDFS Part 500 §500.17; federal banking agencies' Computer-Security Incident Notification Rule (12 CFR 53/225/304).
- `climate.md` — Required. Same disclosure machinery (DCP, disclosure committee, materiality, 8-K/10-K) handles climate-related material events and the 10-K climate disclosure. Anchors: SEC Climate Disclosure Rule [verify current effectiveness]; TCFD 2017 + 2021. The overlay covers how the climate rule's "material climate-related events" mechanic interacts with the same Item 1.05 8-K trigger flow when a climate event (e.g., a major physical-risk loss, a transition-related impairment) crosses materiality.
- `privacy.md` — Optional. Where the cyber incident involves customer financial information, GLBA Safeguards Rule (16 CFR 314) [verify section], state breach-notification laws, and SEC Reg S-P amendments interlock. The readiness pack must surface privacy-notification clocks alongside the SEC clock; the depth lives in the privacy overlay.
- `conduct.md` — Not required at v1.

## Output template named sections

The skill produces three linked artifacts. The output template covers all three.

Artifact A: 8-K Item 1.05 trigger and disclosure decision pack (incident-driven)
- Cover: incident reference ID, date detected, date materiality determined (or pending), filing-clock posture
- Incident timeline (detection, containment, scope determination, materiality call, disclosure)
- Materiality determination workpaper:
  - Facts of the incident (what is known; what is unknown; what is reasonably knowable as of the determination date)
  - Reasonable-investor analysis (TSC / Basic standard) [verify pin cite]
  - Quantitative impact (financial, customer, operational; current and reasonably foreseeable)
  - Qualitative impact (reputational, regulatory, strategic, competitive)
  - Aggregation of related incidents (Item 1.05 instruction on a series of related occurrences)
  - Determination (material / not material / pending), determined-by, determined-on
- Item 1.05 disclosure draft (the 8-K body itself, structured as the rule requires: nature, scope, timing, material impact / reasonably likely material impact)
- Delay-provision analysis (whether a US Attorney General national-security/public-safety delay applies)
- Parallel notification clocks (federal banking agencies' 36-hour rule; NYDFS 72-hour; state breach-notification clocks; counterparty contractual clocks)
- Disclosure controls trace (how the incident moved through the DCP)
- Sign-off block (disclosure committee chair, securities counsel, CISO or designee, CFO, date)
- Reviewer questions

Artifact B: 10-K Item 106 disclosure pack (annual)
- Item 106(b) risk management and strategy disclosure draft
  - Processes for assessing, identifying, and managing material risks from cybersecurity threats
  - Whether and how the processes are integrated into the firm's overall risk management
  - Engagement of assessors, consultants, auditors, or other third parties
  - Processes to oversee and identify material risks from third-party service-provider use
  - Whether risks from cybersecurity threats have materially affected, or are reasonably likely to materially affect, the firm
- Item 106(c) governance disclosure draft
  - Board oversight: which committee, frequency, reporting cadence
  - Management's role: positions / committees responsible, expertise (cite specific titles and qualifications), reporting to board
- Source trace per claim
- Sign-off block

Artifact C: Disclosure-controls (DCP) readiness map
- Trigger detection points (where in the firm an incident becomes visible)
- Escalation paths (first-line to second-line to disclosure committee)
- Materiality-determination protocol (named decision-makers, criteria, time-box)
- Required documentation per stage
- Gaps and remediation

Tail (across all three artifacts):
- Source trace per material claim
- Confidence label (high / medium / low / unknown)
- Human-review gates and recommended owner actions

## Structured output fields

Schemas to add in phase 2 (this skill's output is rich enough to warrant skill-specific schemas under `schemas/`):

`cyber-incident-disclosure.schema.json` (for Artifact A):
- `incident_id`: string. Stable internal ID; not the SEC filing accession number.
- `detection_date`: string. ISO date.
- `materiality_determination_date`: string. ISO date or null.
- `materiality_determination`: enum. `material` / `not-material` / `pending`.
- `materiality_basis_quantitative`: object. `financial_impact_estimate`, `customer_impact_count`, `operational_impact_summary`, `currency`, `confidence` (enum).
- `materiality_basis_qualitative`: array of strings. Each item is a discrete qualitative factor.
- `aggregation_with_prior_incidents`: array of strings (incident_id references). Item 1.05 instruction on related occurrences.
- `disclosure_clock_start`: string. ISO datetime — the materiality determination, not detection.
- `disclosure_filing_due`: string. ISO datetime — 4 business days from clock start.
- `delay_provision_invoked`: boolean.
- `delay_basis`: string or null. AG notification rationale.
- `parallel_notification_clocks`: array of objects with `regulator` (string), `clock_basis` (string, e.g., "36 hours from determination"), `due` (ISO datetime), `status` (enum: not-started / in-progress / submitted / not-applicable).
- `item_105_draft_text`: string. The 8-K body draft.
- `dcp_trace`: array of objects with `stage` (enum: detection / triage / escalation / materiality-call / disclosure-decision / filing), `actor_role`, `timestamp`, `documentation_pointer`.
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `human_review_required`: boolean. Always true for v1.

`item-106-disclosure.schema.json` (for Artifact B):
- `filing_period_end`: string. ISO date.
- `risk_management_disclosure`: object with subfields for each Item 106(b) element listed in the output template.
- `governance_disclosure`: object with subfields for each Item 106(c) element.
- `material_effects_to_date`: array of objects with `incident_id`, `effect_summary`, `affected_filing_period`.
- `source_trace`: array of objects with `claim` (string), `evidence_pointer` (string), `evidence_type` (enum: policy / minutes / risk-register / system-output / external-report).
- `confidence_label`: enum.
- `human_review_required`: boolean.

`dcp-readiness.schema.json` (for Artifact C):
- `dcp_id`: string.
- `trigger_points`: array of objects.
- `escalation_paths`: array of objects.
- `materiality_protocol`: object with `decision_makers` (array of role strings), `criteria` (array of strings), `time_box_hours` (integer).
- `gaps`: array of objects with `gap_description`, `severity` (enum), `owner`, `target_remediation_date`.
- `confidence_label`: enum.

## Example scenarios

### Scenario 1: 8-K Item 1.05 trigger analysis modelled on a public 2024-25 disclosure

Input: a public registrant's cyber incident detected on a Monday, with confirmed unauthorized access to a customer-information system, scope still being determined. The incident response team has briefed the CISO; the disclosure committee is convening to make the materiality call. Source posture: SEC Final Rule (Release 33-11216), TSC / Basic materiality standard, and the firm's DCP. Reference patterns from public 8-K Item 1.05 disclosures filed in calendar 2024 (e.g., Microsoft 8-K filed January 17, 2024; UnitedHealth Group / Change Healthcare 8-K filed February 22, 2024; MGM Resorts 8-K filed September 12, 2023 [verify the pre-rule status of MGM as a contextual reference rather than an Item 1.05 example]). Cite the Microsoft January 2024 disclosure as the structural reference: it is one of the earliest Item 1.05 filings post-effectiveness and demonstrates the four-element disclosure pattern (nature, scope, timing, material impact / reasonably likely impact).

Output emphasizes:
- Materiality workpaper separates known facts from unknowns; the reasonable-investor analysis cites TSC and Basic with pin cites [verify].
- Disclosure-clock posture: the 4-business-day clock starts on the materiality-determination date, not detection. Phase 2 must explicitly reject any draft that conflates these.
- Aggregation analysis: the Item 1.05 instruction on related occurrences is applied; if a prior intrusion in the same period was determined not material on its own, the workpaper documents the aggregation analysis.
- Parallel-clocks table shows: federal banking agencies' 36-hour notification (if the registrant is a covered banking organization), NYDFS 72-hour (if NYDFS-licensed), state breach-notification clocks, and any counterparty contractual notification.
- Item 1.05 draft text is structured into the four required elements only, with clear "to the extent known" framing on scope and impact.
- Delay provision: not invoked; AG notification process documented as not initiated, with rationale.
- Confidence label: medium (scope determination ongoing).
- Human review required: yes; materiality-call meeting minutes attach the workpaper.

### Scenario 2: 10-K Item 106 disclosure refresh for a large accelerated filer

Input: a large accelerated filer is preparing the FY 10-K. Item 106 was first disclosed in the prior-year 10-K; the second-line review function is refreshing the disclosure for the current year, including a new third-party assessor engagement and a refreshed board-oversight cadence (cyber risk now reported quarterly to the Risk Committee, with an annual deep-dive to the full board). Source posture: SEC Final Rule, the firm's information security policy, the board charter, the prior-year 10-K, and the firm's 2025 third-party assessor report. Reference pattern: anonymized structure based on public 10-K Item 106 disclosures filed in 2024 spring and 2025 spring filing seasons (e.g., the structural pattern in JPMorgan Chase's 10-K Item 106 filed February 2024 [verify section reference]; the structural pattern in Bank of America's 10-K Item 106 filed February 2024 [verify]) — used as structural references only; the example does not claim or copy substantive disclosure language.

Output emphasizes:
- Item 106(b) disclosure draft hits each required element discretely (process for assessing/identifying/managing; integration with overall risk management; third-party engagement; third-party-service-provider risk; material effects).
- Item 106(c) disclosure draft names the specific board committee (Risk Committee), the cadence (quarterly plus annual full-board), and management's positions and expertise (CISO with named credentials and reporting line).
- "Material effects to date" array is empty for the current period; prior-period material effects (if any) are explicitly addressed under "no material effects" framing or substantively where applicable.
- Source trace per claim: each governance assertion is anchored to a board minute, charter section, or risk-register entry.
- Confidence label: high (governance posture is well-evidenced); medium on certain risk-management process claims pending the third-party assessor sign-off.
- Human review required: yes; securities counsel and the audit-committee secretary review before disclosure committee sign-off.

## Common pitfalls

1. Conflating the disclosure clock start with the detection date. The 4-business-day clock under Item 1.05 starts on the materiality determination, not on detection. Phase 2 SKILL.md must call this out explicitly and the structured output must compute `disclosure_filing_due` from `materiality_determination_date`, not `detection_date`.
2. Treating the materiality call as the cyber team's call. Materiality is a disclosure determination, made by the disclosure committee with securities counsel input under the firm's DCP. The cyber team contributes facts and quantitative inputs; they do not own the determination.
3. Over-disclosure of incident detail. Item 1.05 calls for nature, scope, timing, and material impact (or reasonably likely material impact). It does not require, and Reg FD considerations argue against, disclosure of forensic detail, IOCs, or remediation specifics that could prejudice ongoing investigation. Phase 2 must include a "minimum-required disclosure" check against the four elements.
4. Missing aggregation analysis. Item 1.05 instruction on related occurrences requires aggregation across a series of incidents that may individually appear non-material but together cross materiality. Phase 2 workpaper must surface aggregation explicitly.
5. Stale Item 106 disclosure. The Item 106 disclosure is annual but the underlying facts (board cadence, management positions, third-party engagements) change. A "rolled forward unchanged" Item 106 disclosure is a frequent finding; phase 2 must require year-over-year diff and rationale.
6. SEC climate rule overreach. Phase 2 must not assert the SEC Climate Disclosure Rule is currently effective without checking SEC's posture as of the report date. The rule was finalized March 2024, voluntarily stayed by the SEC pending Eighth Circuit review, and current status is unsettled. Default posture: cite with `[verify current effectiveness]` and use TCFD for substantive content. The cross-cutting climate overlay must carry this caveat front-and-centre.
7. Ignoring parallel clocks. Federal banking agencies' 36-hour rule (12 CFR 53/225/304) [verify], NYDFS Part 500 §500.17 72-hour rule [verify], state breach-notification clocks, and Reg S-P amendments (May 2024) all run on different clocks from the SEC's. The readiness pack must surface every clock applicable to the registrant; missing one is a frequent regulator finding.
8. Foreign private issuer confusion. FPIs report under Form 6-K, not 8-K, and the trigger flow is different. Phase 2 must support an FPI mode and not assume domestic-issuer treatment.
9. Treating "reasonably likely material impact" as speculative. The "or reasonably likely to materially affect" language in Item 1.05 has substance: it requires disclosure of material impact reasonably foreseeable as of the determination date, even if not yet realized. Phase 2 workpaper must address both realized and reasonably-likely impact.
