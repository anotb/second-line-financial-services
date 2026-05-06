# Example: OCC targeted exam at a regional bank — third-party risk and cyber

## Input

A $30B regional national bank receives a 60-day notice of an OCC targeted examination on third-party risk management and cyber, scope-confirmed in writing as a focused review against the June 2023 interagency third-party-risk guidance and against the bank's compliance with the 36-hour computer-security-incident notification rule (12 CFR Part 53). Fieldwork window is six weeks, virtual-and-on-site combined. The bank's head of regulatory affairs runs the engagement; the CRO and CISO co-own the substantive content; the chief compliance officer is the named primary contact for examination correspondence; outside counsel is engaged for privilege review on internal-investigation materials touching a 2025 incident notified under Part 53.

The bank carries one open MRA on third-party concentration in the core-banking-platform vendor, issued at the prior cycle exam and on track for a 2026-Q3 closure submission. No MRIAs. No consent order.

## Why this scenario matters

This is the canonical generic-exam-brief use of the skill at a bank: the engagement is targeted and scope-bounded, so the substantive readiness sprint does not warrant the full `banking-supervision-readiness` package, but the engagement-side machinery (regulator, scope confirmation, document handling, request-list mapping, gap matrix on the in-scope topics, evidence index, response posture) is the operative scaffolding the regulatory affairs lead runs during the exam window. The Part 53 36-hour-rule slice is a high-stakes incident-notification topic that benefits from a clean evidence trace; the third-party-risk slice benefits from a clean gap-matrix view.

## Output sketch

```yaml
brief_id: EXBR-2026-OCC-TPR-CYB-04
engagement_id: ENG-2026-OCC-TGT-04
as_of_date: 2026-05-06

regulator: OCC
regulator_office: OCC Midsize and Community Bank Supervision (Northeastern District)

exam_type: targeted
trigger: risk-based selection (third-party concentration follow-up; sector-wide cyber emphasis)

scope_window:
  fieldwork_start: 2026-07-06
  fieldwork_end: 2026-08-14
  review_period_start: 2024-01-01
  review_period_end: 2026-06-30
  in_scope_products:
    - core banking platform (deposits, loans, payments)
    - third-party-managed cloud infrastructure (IaaS, PaaS)
    - retail digital channels (web, mobile)
  in_scope_business_units: [retail bank, commercial bank, technology and operations]
  in_scope_legal_entities: [the national bank]
  geographies: [Northeastern US footprint]
  out_of_scope:
    - BSA / AML program (separate cycle)
    - fair lending and CRA (separate cycle)
    - capital and liquidity (separate cycle)
    - model risk (separate cycle)
  scope_confirmation_source: OCC scope memorandum dated 2026-05-04

lead_examiner_role: examiner-in-charge, OCC Midsize and Community Bank Supervision Northeastern District
lead_firm_contact_role: head of regulatory affairs

points_of_contact:
  - topic: third-party risk management
    primary_role: head of third-party risk management
    backup_role: deputy CRO
    external_counsel_engaged: false
  - topic: cyber program and Part 53 incident notification
    primary_role: CISO
    backup_role: deputy CISO
    external_counsel_engaged: true
  - topic: business-continuity and operational resilience
    primary_role: head of operational resilience
    backup_role: COO chief of staff
    external_counsel_engaged: false
  - topic: examination correspondence
    primary_role: chief compliance officer
    backup_role: head of regulatory affairs

document_handling:
  production_channel: OCC Examiner View portal
  privilege_review_lead_role: deputy general counsel (regulatory)
  privilege_log_required: true
  redaction_workflow: counsel-supervised redaction in firm document-review platform; burned-in redactions; metadata stripped; reviewer named per document
  deduplication_method: hash-based dedup at production-package level; production log keyed by document hash and wave
  production_log_location: regulatory-affairs SharePoint, exam EXBR-2026-OCC-TPR-CYB-04 site, production-log workbook
  confidential_supervisory_information_handled: true

request_list_items:
  - item_id: RL-01
    text: Third-party risk management policy and standards in effect during the review period.
    owner_role: head of third-party risk management
    status: ready
    due_date: 2026-07-13
    artifact_pointers:
      - policy management system, TPRM Policy v4.2 (effective 2024-04) and v4.3 (effective 2025-08)
      - TPRM Standards v3.1 (effective 2025-01)
    privilege_posture: producible
    confidence: high
  - item_id: RL-02
    text: Inventory of all third-party relationships with criticality tier as of 2026-06-30, with the top 25 critical relationships identified.
    owner_role: head of third-party risk management
    status: ready
    due_date: 2026-07-13
    artifact_pointers:
      - TPRM register export, dated 2026-06-30, system-of-record extract
    privilege_posture: producible
    confidence: high
  - item_id: RL-03
    text: Pre-contract due diligence packages for the top 25 critical relationships.
    owner_role: head of third-party risk management
    status: partial
    due_date: 2026-07-20
    artifact_pointers:
      - vendor diligence packs in TPRM system, links per relationship ID
      - flag, three packages predate the June 2023 interagency guidance and have legacy structure; refresh under way
    privilege_posture: redacted-and-producible
    confidence: medium
  - item_id: RL-04
    text: Ongoing-monitoring evidence for the top 25 critical relationships covering the review period.
    owner_role: head of third-party risk management
    status: ready
    due_date: 2026-07-20
    artifact_pointers:
      - quarterly performance reviews, escalation log, SLA-breach log
    privilege_posture: producible
    confidence: high
  - item_id: RL-05
    text: Cybersecurity program description, governance documents, and current information-security policy.
    owner_role: CISO
    status: ready
    due_date: 2026-07-13
    artifact_pointers:
      - Cyber Program Description v6.1 (effective 2025-11)
      - Information Security Policy v8.4 (effective 2025-11)
    privilege_posture: producible
    confidence: high
  - item_id: RL-06
    text: Independent testing of cybersecurity controls during the review period (penetration tests, red-team exercises, third-party assessments).
    owner_role: CISO
    status: partial
    due_date: 2026-07-27
    artifact_pointers:
      - 2024 and 2025 annual pen-test reports, third-party
      - 2025 red-team exercise report (privileged segments require redaction)
    privilege_posture: under-review
    confidence: medium
  - item_id: RL-07
    text: 12 CFR Part 53 notification log; documentation of any incident assessed during the review period for notification eligibility, including those determined non-notifiable with the rationale.
    owner_role: CISO
    status: escalated
    due_date: 2026-07-13
    artifact_pointers:
      - incident-notification log, 2024-01 through 2026-06
      - the 2025-Q4 incident notified under Part 53; counsel-led timeline; supporting evidence binder
    privilege_posture: under-review
    confidence: medium
    notes: counsel-led; outside counsel reviewing pre-production
  - item_id: RL-08
    text: Business continuity and incident-response plans; tabletop exercise reports for the review period.
    owner_role: head of operational resilience
    status: ready
    due_date: 2026-07-20
    artifact_pointers:
      - BCM and IR plan, current versions; tabletop reports dated 2024-Q2, 2024-Q4, 2025-Q2, 2025-Q4, 2026-Q1
    privilege_posture: producible
    confidence: high

interview_prep:
  - interviewee_role: CISO
    topic: cybersecurity program governance and Part 53 notification posture
    scheduled_date: 2026-07-22
    prep_session_date: 2026-07-15
    counsel_attending: true
    key_documents:
      - Cyber Program Description v6.1
      - Part 53 notification procedure
      - 2025-Q4 incident binder summary memo
    anticipated_topics:
      - notification-decision rationale on the 2025-Q4 incident
      - third-party-vendor coordination on the 2025-Q4 incident
      - control-gap remediation tracking
    off-limits-topics:
      - ongoing internal-investigation work-product (counsel will redirect)
  - interviewee_role: head of third-party risk management
    topic: TPRM program against the June 2023 interagency guidance
    scheduled_date: 2026-07-23
    prep_session_date: 2026-07-16
    counsel_attending: false
    key_documents:
      - TPRM Policy v4.3
      - TPRM register snapshot as of 2026-06-30
      - open MRA closure submission package
    anticipated_topics:
      - core-banking-platform concentration (links to open MRA)
      - vendor-by-vendor criticality methodology
      - ongoing-monitoring cadence for critical relationships
      - exit-plan posture for top 5 critical relationships

supervisory_history:
  open_mras:
    - mra_id: MRA-2025-09
      issued_date: 2025-04-15
      topic: third-party concentration in the core-banking-platform vendor
      due_date: 2026-09-30
      status: open
      owner_role: head of third-party risk management
  open_mrias: []
  consent_orders: []
  self_identified_issues:
    - issue_id: SID-2026-04-01
      topic: legacy diligence packages for three critical relationships predate June 2023 interagency guidance; refresh in flight
      remediation_status: in flight, target completion 2026-08-31
      owner_role: head of third-party risk management
    - issue_id: SID-2026-04-02
      topic: pen-test scope did not include one cloud-hosted retail-channel boundary in 2024; corrected for 2025
      remediation_status: closed; 2025 pen-test confirmed corrected scope
      owner_role: CISO

anticipated_reviewer_questions:
  - question: How does the firm operationalise the "critical activities" definition under the June 2023 interagency guidance, and how does the resulting list reconcile with the firm's own criticality tier?
    source_pattern: June 2023 interagency third-party-risk guidance, recurring focus area in OCC examiner communications
    talking_point: criticality methodology documented in TPRM Standards §4; reconciliation table available; methodology reviewed by internal audit 2025-Q3
  - question: For the 2025-Q4 Part 53 incident, walk us through the notification-decision timeline and the supporting evidence.
    source_pattern: 12 CFR Part 53; recurring OCC focus on incident-notification timing
    talking_point: counsel-led timeline binder; production through privilege review; live walk-through with CISO and counsel
  - question: How does the firm's exit plan for the core-banking-platform vendor address the concentration MRA, and what is the testable evidence that the exit plan is current?
    source_pattern: MRA-2025-09; recurring OCC focus on exit plans for critical concentrated vendors
    talking_point: exit plan v2.1 dated 2026-04; tabletop walkthrough conducted 2026-Q2; alternative-provider readiness evidenced
  - question: Describe the surveillance and oversight of fourth parties for the top 5 critical relationships.
    source_pattern: June 2023 interagency third-party-risk guidance; recurring OCC focus on visibility into the subcontractor chain
    talking_point: fourth-party register maintained for the top 5; flow-down clauses in the contract; change-notice mechanism evidenced
  - question: What changed in the cyber program after the 2025-Q4 incident, and how is the change reflected in policy, control, and testing?
    source_pattern: post-incident lessons-learned focus; OCC examiner pattern after Part 53 notifications
    talking_point: lessons-learned memo; policy updates to v8.4; control updates to MFA and EDR coverage; subsequent pen-test confirmed remediation

exit_meeting_prep:
  scheduled_date: 2026-08-14
  firm_attendees_roles: [head of regulatory affairs, CRO, CISO, head of TPRM, deputy general counsel (regulatory)]
  anticipated_findings:
    - possible MRA on legacy diligence packages refresh pace
    - possible recommendation on fourth-party visibility methodology beyond the top 5
    - acknowledgement of in-flight closure of MRA-2025-09 (no new MRA expected on the topic)
  disagreement_posture: limited; firm intends to push back on any finding implying inadequate notification on the 2025-Q4 incident; counsel-led written response if needed
  response_window_days: 30

response_posture:
  named_response_owner_role: chief compliance officer (cover letter); head of TPRM and CISO (substantive responses)
  response_due_calculation_basis: 30 days from receipt of supervisory letter (per OCC convention)
  remediation_plan_template_pointer: regulatory-affairs SharePoint, supervisory-response-templates folder
  board_or_committee_reporting_required: true
  external_counsel_for_response: true (cyber and Part 53 segments only)

post_exam_followup:
  lessons_learned_session_date: 2026-09-15
  after-action-record-pointer: regulatory-affairs SharePoint, exam EXBR-2026-OCC-TPR-CYB-04 site, after-action folder
  next_cycle_preparation_owner_role: head of regulatory affairs

review_gates: [scope, evidence, authority, impact, decision]

confidence_label: medium

source_trace:
  - claim: 30-day response window after receipt of supervisory letter is OCC convention.
    source: Comptroller's Handbook, Bank Supervision Process booklet
    section: report-of-examination and supervisory-letter sections [verify section]
    url: https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/index-comptrollers-handbook.html
  - claim: 36-hour notification rule for computer-security incidents at national banks.
    source: 12 CFR Part 53
    section: §53.3 notification of computer-security incidents to primary federal regulator
    url: https://www.ecfr.gov/current/title-12/chapter-I/part-53
  - claim: June 2023 interagency third-party-risk guidance is the operative TPRM expectations document for OCC, FRB, and FDIC.
    source: Interagency Guidance on Third-Party Relationships, OCC FRB FDIC, June 2023
    section: section II program elements; section III risk-based diligence
    url: https://www.occ.gov/news-issuances/news-releases/2023/nr-ia-2023-53.html
  - claim: CSI handling for OCC supervisory materials runs under 12 CFR Part 4 Subpart C.
    source: 12 CFR Part 4 Subpart C
    section: §§4.31 through 4.39 [verify subsection]
    url: https://www.ecfr.gov/current/title-12/chapter-I/part-4
```

## Why the brief shape matters in flight

- The request-list mapping is the operative production tracker; the regulatory-affairs lead runs the daily standup against it.
- The interview-prep section names off-limits topics so the interviewee carries a clean redirect for any privileged territory.
- The supervisory-history section makes the open MRA visible to the engagement and ties the closure submission timing to the exam window; suppressing the open MRA would distort the brief.
- The self-identified-issues section signals credibility to the examiner and short-circuits a finding the firm would have received anyway.
- The anticipated-reviewer-questions section is grounded in the June 2023 guidance, the open MRA, and the prior incident; each question references a concrete source pattern, not a generic FAQ.
- The response-posture section pre-positions the named response owner and the privilege posture for the cyber segments; counsel does not get surprised when the supervisory letter lands.
- The `confidence_label: medium` is the honest read because three request-list items are partial or escalated; `high` would require the partial items to clear before the brief sign-off.
