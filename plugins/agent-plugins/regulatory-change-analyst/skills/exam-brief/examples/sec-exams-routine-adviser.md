# Example: SEC EXAMS routine examination at an SEC-registered investment adviser

## Input

An SEC-registered investment adviser ($4B regulatory AUM, separately managed accounts plus two private funds, 28 employees) receives an EXAMS notification letter for a routine (non-cause) examination. Initial document request list arrives the following week with a 14-day production window for the first wave; rolling production negotiated for larger items. Fieldwork is virtual-only with one-week of synchronous interviews scheduled six weeks after notification. The CCO runs the engagement as the named primary contact for examination correspondence; the general counsel oversees privilege; the CIO and head of trading own substantive content for portfolio-management and trading items; the head of marketing owns Marketing Rule items. Outside counsel is engaged on retainer for advice but not for routine production.

The adviser has no prior deficiency letter open; the most recent EXAMS exam closed three years prior with two non-significant deficiencies (Code of Ethics record-keeping; one Form ADV item) both remediated and confirmed in the firm's prior response.

## Why this scenario matters

This is the canonical generic-exam-brief use of the skill at an SEC adviser when the firm chooses not to run the substantive `adviser-exam-readiness` sprint (or has already run it and is using exam-brief for the engagement-side mechanics during the live exam). The engagement-side machinery is the operative scaffolding: scope confirmation, request-list mapping with rolling-production staging, privilege posture for internal compliance materials, off-channel-communications evidence preparation (a recurring EXAMS focus area), Marketing Rule books-and-records readiness, custody-rule SLOA inventory, deficiency-letter response posture. The exam is non-adversarial in posture but the brief flags the Wells trigger as a contingency in the response-posture section.

## Output sketch

```yaml
brief_id: EXBR-2026-SEC-RTN-01
engagement_id: ENG-2026-SEC-RTN-01
as_of_date: 2026-05-06

regulator: SEC
regulator_office: SEC Division of Examinations, Northeast Regional Office, Investment Adviser/Investment Company examination program

exam_type: targeted
trigger: routine cycle (risk-based selection within EXAMS adviser program)

scope_window:
  fieldwork_start: 2026-06-15
  fieldwork_end: 2026-06-19
  review_period_start: 2024-01-01
  review_period_end: 2026-04-30
  in_scope_products:
    - separately managed accounts (SMA)
    - two private funds (one private equity, one private credit)
  in_scope_business_units: [the adviser]
  in_scope_legal_entities: [the SEC-registered adviser]
  geographies: [US]
  out_of_scope:
    - any sub-advised mutual fund mandate (handled by the fund's adviser)
    - any business of the adviser's affiliated insurance agency
  scope_confirmation_source: SEC EXAMS document request letter dated 2026-05-08

lead_examiner_role: examiner-in-charge, SEC EXAMS Northeast Regional Office, IA/IC examination program
lead_firm_contact_role: chief compliance officer

points_of_contact:
  - topic: examination correspondence and Marketing Rule
    primary_role: chief compliance officer
    backup_role: deputy CCO
    external_counsel_engaged: false
  - topic: portfolio management, trading, best execution
    primary_role: chief investment officer
    backup_role: head of trading
    external_counsel_engaged: false
  - topic: custody rule and SLOA inventory
    primary_role: chief operating officer
    backup_role: head of operations
    external_counsel_engaged: false
  - topic: Code of Ethics, personal trading, MNPI
    primary_role: chief compliance officer
    backup_role: deputy CCO
    external_counsel_engaged: false
  - topic: electronic communications and off-channel-communications evidence
    primary_role: chief compliance officer
    backup_role: head of IT
    external_counsel_engaged: true
  - topic: private-fund matters, including 38a-1 (n/a as adviser is not registered investment company adviser; private-fund adviser items)
    primary_role: chief operating officer
    backup_role: deputy CCO
    external_counsel_engaged: true

document_handling:
  production_channel: SEC EDS / secure file transfer
  privilege_review_lead_role: general counsel
  privilege_log_required: true
  redaction_workflow: counsel-supervised redaction; burned-in; metadata stripped; reviewer named per document
  deduplication_method: hash-based at production-package level
  production_log_location: compliance shared drive, EXBR-2026-SEC-RTN-01 folder, production-log workbook
  confidential_supervisory_information_handled: false

request_list_items:
  - item_id: RL-01
    text: Form ADV Parts 1, 2A, 2B, and 3 (Form CRS) currently in effect and as of each annual amendment during the review period.
    owner_role: chief compliance officer
    status: ready
    due_date: 2026-05-22
    artifact_pointers:
      - IARD filings, current and prior amendments, with effective dates
    privilege_posture: producible
    confidence: high
  - item_id: RL-02
    text: Compliance policies and procedures, including the IAA Rule 206(4)-7 annual review report for each year in the review period.
    owner_role: chief compliance officer
    status: ready
    due_date: 2026-05-22
    artifact_pointers:
      - Compliance Manual v12 (current); v10 and v11 (prior versions in effect during review period)
      - 2024 and 2025 annual review reports
    privilege_posture: redacted-and-producible
    confidence: high
    notes: portions of annual review reports are counsel-reviewed work product; redaction posture set by GC
  - item_id: RL-03
    text: Code of Ethics, including the personal-trading reporting log and any violations during the review period.
    owner_role: chief compliance officer
    status: ready
    due_date: 2026-05-22
    artifact_pointers:
      - Code of Ethics v5
      - personal-trading reports for review period; pre-clearance log; violation log (zero violations)
    privilege_posture: producible
    confidence: high
  - item_id: RL-04
    text: Marketing materials disseminated during the review period including pitchbooks, fund offering materials, performance presentations, RFP responses, and one-on-one client communications that constitute advertisements.
    owner_role: head of marketing
    status: partial
    due_date: 2026-05-29
    artifact_pointers:
      - marketing materials repository, dated index for review period
      - flag, scope of "one-on-one communications that constitute advertisements" requires legal review on the Marketing Rule definition; CCO and GC scoping
    privilege_posture: under-review
    confidence: medium
  - item_id: RL-05
    text: Performance composites and supporting data, including any hypothetical, predecessor, model, or back-tested performance, and any third-party-rating use.
    owner_role: head of marketing
    status: partial
    due_date: 2026-06-05
    artifact_pointers:
      - composite construction documentation; GIPS verification report (most recent)
      - hypothetical-performance materials with the supporting policies and procedures evidence
    privilege_posture: producible
    confidence: medium
  - item_id: RL-06
    text: Custody-rule documentation including qualified-custodian list, surprise-audit reports for the review period, account-statement delivery evidence, SLOA inventory and authorisations.
    owner_role: chief operating officer
    status: ready
    due_date: 2026-05-29
    artifact_pointers:
      - qualified-custodian list with effective dates
      - 2024 and 2025 surprise-audit reports
      - SLOA inventory current as of 2026-04-30 with authorisation evidence per relationship
    privilege_posture: producible
    confidence: high
  - item_id: RL-07
    text: Best-execution committee minutes and supporting analyses for the review period.
    owner_role: chief investment officer
    status: ready
    due_date: 2026-05-29
    artifact_pointers:
      - best-execution committee minutes 2024 and 2025
      - quarterly best-execution analyses with broker scorecards
    privilege_posture: producible
    confidence: high
  - item_id: RL-08
    text: Electronic-communications policies, including handling of personal-device, encrypted-app, and off-channel communications, and any surveillance evidence.
    owner_role: chief compliance officer
    status: escalated
    due_date: 2026-05-29
    artifact_pointers:
      - Electronic Communications Policy v3.2 (effective 2024-09)
      - personal-device attestation program evidence; surveillance reports for review period
      - any internal investigations on off-channel-communications during review period (counsel-led; privilege review required)
    privilege_posture: under-review
    confidence: medium
    notes: counsel-led; outside counsel consulting on privilege posture
  - item_id: RL-09
    text: Form PF filings during the review period and supporting calculations.
    owner_role: chief operating officer
    status: ready
    due_date: 2026-06-05
    artifact_pointers:
      - Form PF filings, IARD filings, supporting workbooks
    privilege_posture: producible
    confidence: high
  - item_id: RL-10
    text: Trade allocation and aggregation policy and supporting trade-allocation evidence for the review period.
    owner_role: head of trading
    status: ready
    due_date: 2026-06-05
    artifact_pointers:
      - Trade Allocation Policy v4
      - trade allocation reports for review period; allocation-deviation log (de-minimis)
    privilege_posture: producible
    confidence: high

interview_prep:
  - interviewee_role: chief compliance officer
    topic: 206(4)-7 annual review process; off-channel communications surveillance
    scheduled_date: 2026-06-16
    prep_session_date: 2026-06-09
    counsel_attending: true
    key_documents:
      - Compliance Manual v12
      - 2025 annual review report (unredacted internal copy for prep only)
      - electronic-communications surveillance summary
    anticipated_topics:
      - testing methodology and risk-prioritisation in the annual review
      - tone-from-the-top for Marketing Rule and off-channel
      - personal-device attestation efficacy; surveillance findings and remediation
    off-limits-topics:
      - any matter under outside-counsel privileged review (CCO will redirect to GC and counsel)
  - interviewee_role: chief investment officer
    topic: portfolio management, best execution, trade allocation
    scheduled_date: 2026-06-17
    prep_session_date: 2026-06-10
    counsel_attending: false
    key_documents:
      - Trade Allocation Policy v4
      - best-execution committee minutes 2024 and 2025
      - personal-trading-pre-clearance evidence (CIO's own)
    anticipated_topics:
      - principal-trading and cross-trading posture
      - allocation methodology for IPOs and limited-allocation opportunities
      - best-execution evaluation framework
  - interviewee_role: chief operating officer
    topic: custody rule, Form PF, valuation
    scheduled_date: 2026-06-18
    prep_session_date: 2026-06-11
    counsel_attending: false
    key_documents:
      - SLOA inventory 2026-04-30
      - 2024 and 2025 surprise audit reports
      - Form PF filings and supporting workbooks
    anticipated_topics:
      - SLOA classification methodology
      - valuation-policy application for the two private funds
      - Form PF triggering-event monitoring posture

supervisory_history:
  open_mras: []
  open_mrias: []
  consent_orders: []
  self_identified_issues:
    - issue_id: SID-2026-04-01
      topic: scope of "advertisement" definition under the Marketing Rule for certain one-on-one communications requires CCO and GC scoping; in flight
      remediation_status: in flight, target completion 2026-05-29 (in time for production)
      owner_role: chief compliance officer
    - issue_id: SID-2026-04-02
      topic: hypothetical-performance materials supporting policies require refresh on documentation depth (controls in place, documentation depth being upgraded)
      remediation_status: in flight, target completion 2026-08-31
      owner_role: head of marketing

anticipated_reviewer_questions:
  - question: Walk us through the firm's definition of "advertisement" under the Marketing Rule and how the firm operationalises the books-and-records requirements for one-on-one communications.
    source_pattern: SEC Marketing Rule (IAA Rule 206(4)-1); recurring EXAMS focus per multiple risk alerts since 2022
    talking_point: Marketing Rule Compliance Procedure §3 names the firm's definitional approach; books-and-records process documented; periodic CCO testing
  - question: How does the firm surveille for off-channel communications, and what does the firm do when it identifies off-channel use?
    source_pattern: off-channel-communications enforcement actions across BD and IA registrants 2021 onward; recurring EXAMS focus
    talking_point: Electronic Communications Policy v3.2; personal-device attestation program; periodic surveillance reports; incident-response procedure for identified off-channel use
  - question: For the SLOA inventory, what is the methodology that determines which authorisations create custody and which do not, and how is the inventory kept current?
    source_pattern: Custody Rule (IAA Rule 206(4)-2); recurring EXAMS focus on SLOA classification
    talking_point: SLOA Classification Procedure §2 names the firm's methodology under the no-action-letter framework; quarterly review by COO and CCO; current inventory dated 2026-04-30
  - question: How does the firm test the 206(4)-7 annual review against the prior cycle's findings and against current EXAMS priorities?
    source_pattern: IAA Rule 206(4)-7; recurring EXAMS focus on annual-review testing depth
    talking_point: 2025 annual review methodology documented in §1.1 of the report; testing prioritisation against the 2025 EXAMS priorities letter and the 2024 deficiency letters issued in peer firms
  - question: Describe the AI-use posture of the firm in research, marketing, and client communications.
    source_pattern: SEC EXAMS focus on AI/predictive analytics in adviser practices; pending AI rulemaking; emerging examiner pattern
    talking_point: AI Use Policy v1.1 (effective 2025-08); prohibited-use list; books-and-records protocol for AI-assisted outputs; CCO review for AI-generated marketing
  - question: For the two private funds, what is the firm's posture on conflicts of interest, fees and expenses, and side-letter terms.
    source_pattern: ongoing EXAMS focus on private-fund advisers (separate from the vacated Private Fund Advisers Rule); IAA antifraud reach
    talking_point: Conflicts Disclosure Schedule current; fees and expenses methodology in fund LPA; side-letter inventory and most-favoured-nation election process documented

exit_meeting_prep:
  scheduled_date: 2026-06-19
  firm_attendees_roles: [chief compliance officer, general counsel, chief operating officer]
  anticipated_findings:
    - possible deficiency on documentation depth for hypothetical-performance materials supporting policies
    - possible deficiency on definitional documentation for one-on-one communications under the Marketing Rule
    - possible recommendation on SLOA inventory cadence
  disagreement_posture: limited; firm intends to push back if examiner suggests off-channel surveillance is inadequate without specific evidence; counsel-led written response if needed
  response_window_days: 30

response_posture:
  named_response_owner_role: chief compliance officer (cover letter); general counsel (any matter touching privilege or pointing toward Wells)
  response_due_calculation_basis: 30 days from receipt of deficiency letter
  remediation_plan_template_pointer: compliance shared drive, EXAMS-response-templates folder
  board_or_committee_reporting_required: false (no fund board; firm board reporting per firm governance)
  external_counsel_for_response: false (default); contingent escalation to outside counsel if Wells signals appear

post_exam_followup:
  lessons_learned_session_date: 2026-07-15
  after-action-record-pointer: compliance shared drive, EXBR-2026-SEC-RTN-01 folder, after-action folder
  next_cycle_preparation_owner_role: chief compliance officer

review_gates: [scope, evidence, authority, impact, decision]

confidence_label: medium

source_trace:
  - claim: 14-day initial production window is EXAMS standard.
    source: SEC Division of Examinations published process [verify exact reference]
    section: examination process overview
    url: https://www.sec.gov/exams
  - claim: 30-day deficiency-letter response window is EXAMS standard.
    source: SEC Division of Examinations published process [verify exact reference]
    section: examination process overview
    url: https://www.sec.gov/exams
  - claim: Marketing Rule applies to one-on-one communications that constitute advertisements under the rule definition.
    source: 17 CFR 275.206(4)-1 (IAA Rule 206(4)-1)
    section: §275.206(4)-1(e)(1) definition of "advertisement"
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1
  - claim: Custody Rule SLOA classification framework rests on the SEC staff no-action letter framework.
    source: 17 CFR 275.206(4)-2 (IAA Rule 206(4)-2) and SEC staff no-action positions on SLOAs
    section: §275.206(4)-2; staff no-action letters [verify specific cite]
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-2
  - claim: Off-channel-communications enforcement is a sustained EXAMS and Division of Enforcement focus area.
    source: SEC enforcement actions and EXAMS risk alerts on electronic communications [verify specific risk alert citations]
    section: risk alerts on electronic communications and books-and-records
    url: https://www.sec.gov/exams
```

## Why the brief shape matters in flight

- Rolling production is the operative posture; the request-list mapping carries staged due dates, not one bulk deadline.
- The off-channel-communications request line is the high-stakes one; counsel-led with privilege posture set in advance.
- The Marketing Rule production turns on the firm's definitional posture; the brief flags the in-flight CCO/GC scoping so the production lands clean.
- The interview-prep section pre-positions the CCO to redirect privileged territory to general counsel; counsel attends the CCO interview because two of the topics carry privilege posture.
- The anticipated-reviewer-questions section is grounded in current EXAMS priorities and recurring enforcement themes; each question references a concrete source pattern.
- The response-posture section names the contingent escalation to outside counsel if Wells signals appear; the contingency is named, not improvised.
- The `confidence_label: medium` reflects three partial or escalated request items; the brief sign-off cannot move to `high` until those items clear.
