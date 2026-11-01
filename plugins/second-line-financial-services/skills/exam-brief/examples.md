# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## occ-targeted-exam-bank

### Example: OCC targeted exam at a regional bank (third-party risk and cyber)

#### Input

A $30B regional national bank receives a 60-day notice of an OCC targeted examination on third-party risk management and cyber, scope-confirmed in writing as a focused review against the June 2023 interagency third-party-risk guidance and against the bank's compliance with the 36-hour computer-security-incident notification rule (12 CFR Part 53). Fieldwork window is six weeks, virtual-and-on-site combined. The bank's head of regulatory affairs runs the engagement; the CRO and CISO co-own the substantive content; the chief compliance officer is the named primary contact for examination correspondence; outside counsel is engaged for privilege review on internal-investigation materials touching a 2025 incident notified under Part 53.

The bank carries one open MRA on third-party concentration in the core-banking-platform vendor, issued at the prior cycle exam and on track for a 2026-Q3 closure submission. No MRIAs. No consent order.

#### Why this scenario matters

This is the canonical generic-exam-brief use of the skill at a bank: the engagement is targeted and scope-bounded, so the substantive readiness sprint does not warrant the full `banking-supervision-readiness` package, but the engagement-side machinery (regulator, scope confirmation, document handling, request-list mapping, gap matrix on the in-scope topics, evidence index, response posture) is the operative scaffolding the regulatory affairs lead runs during the exam window. The Part 53 36-hour-rule slice is a high-stakes incident-notification topic that benefits from a clean evidence trace; the third-party-risk slice benefits from a clean gap-matrix view.

#### Output sketch

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

#### Why the brief shape matters in flight

- The request-list mapping is the operative production tracker; the regulatory-affairs lead runs the daily standup against it.
- The interview-prep section names off-limits topics so the interviewee carries a clean redirect for any privileged territory.
- The supervisory-history section makes the open MRA visible to the engagement and ties the closure submission timing to the exam window; suppressing the open MRA would distort the brief.
- The self-identified-issues section signals credibility to the examiner and short-circuits a finding the firm would have received anyway.
- The anticipated-reviewer-questions section is grounded in the June 2023 guidance, the open MRA, and the prior incident; each question references a concrete source pattern, not a generic FAQ.
- The response-posture section pre-positions the named response owner and the privilege posture for the cyber segments; counsel does not get surprised when the supervisory letter lands.
- The `confidence_label: medium` is the honest read because three request-list items are partial or escalated; `high` would require the partial items to clear before the brief sign-off.

## sec-exams-routine-adviser

### Example: SEC EXAMS routine examination at an SEC-registered investment adviser

#### Input

An SEC-registered investment adviser ($4B regulatory AUM, separately managed accounts plus two private funds, 28 employees) receives an EXAMS notification letter for a routine (non-cause) examination. Initial document request list arrives the following week with a 14-day production window for the first wave; rolling production negotiated for larger items. Fieldwork is virtual-only with one-week of synchronous interviews scheduled six weeks after notification. The CCO runs the engagement as the named primary contact for examination correspondence; the general counsel oversees privilege; the CIO and head of trading own substantive content for portfolio-management and trading items; the head of marketing owns Marketing Rule items. Outside counsel is engaged on retainer for advice but not for routine production.

The adviser has no prior deficiency letter open; the most recent EXAMS exam closed three years prior with two non-significant deficiencies (Code of Ethics record-keeping; one Form ADV item) both remediated and confirmed in the firm's prior response.

#### Why this scenario matters

This is the canonical generic-exam-brief use of the skill at an SEC adviser when the firm chooses not to run the substantive `adviser-exam-readiness` sprint (or has already run it and is using exam-brief for the engagement-side mechanics during the live exam). The engagement-side machinery is the operative scaffolding: scope confirmation, request-list mapping with rolling-production staging, privilege posture for internal compliance materials, off-channel-communications evidence preparation (a recurring EXAMS focus area), Marketing Rule books-and-records readiness, custody-rule SLOA inventory, deficiency-letter response posture. The exam is non-adversarial in posture but the brief flags the Wells trigger as a contingency in the response-posture section.

#### Output sketch

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

#### Why the brief shape matters in flight

- Rolling production is the operative posture; the request-list mapping carries staged due dates, not one bulk deadline.
- The off-channel-communications request line is the high-stakes one; counsel-led with privilege posture set in advance.
- The Marketing Rule production turns on the firm's definitional posture; the brief flags the in-flight CCO/GC scoping so the production lands clean.
- The interview-prep section pre-positions the CCO to redirect privileged territory to general counsel; counsel attends the CCO interview because two of the topics carry privilege posture.
- The anticipated-reviewer-questions section is grounded in current EXAMS priorities and recurring enforcement themes; each question references a concrete source pattern.
- The response-posture section names the contingent escalation to outside counsel if Wells signals appear; the contingency is named, not improvised.
- The `confidence_label: medium` reflects three partial or escalated request items; the brief sign-off cannot move to `high` until those items clear.

## troubleshooting

### Troubleshooting: exam-brief

The exam-brief is the engagement playbook the regulatory affairs lead and head of compliance run during an active examination. It sits next to the substantive readiness pack (which lives in the sector skills `banking-supervision-readiness` and `adviser-exam-readiness`); confusion between the two is the most common defect this skill produces. Other recurring defects below.

#### 1. Running exam-brief when the sector readiness skill is the right tool

**Symptom**: A full-scope OCC bank exam or a substantive SEC adviser exam comes through the door, and the team produces an exam-brief artifact instead of the sector-readiness sprint. The artifact reads as a thin engagement playbook with no substantive obligation-by-obligation status mapping.

**Why it happens**: The skill description's "Best for" list got read; the "Not the right tool when" list did not.

**Resolution**:
- For a full-scope federal banking exam at a bank under Heightened Standards, route to `banking-supervision-readiness`. That readiness sprint carries the substantive scaffolding for capital, BSA/AML, fair lending, CRA, and the Heightened Standards expectations.
- For a substantive SEC adviser, BD, or investment-company exam, route to `adviser-exam-readiness`. That readiness sprint carries IAA Rule 206(4)-7 cadence, marketing rule, custody rule, books-and-records, and Form ADV-specific scaffolding.
- Use exam-brief when the engagement is targeted, topic-specific, horizontal, or for-cause and the engagement-side mechanics are the operative scaffolding.
- Default to chaining: exam-brief produces the engagement playbook; the sector skill produces the substantive readiness pack. The two artifacts read together for full-scope sector engagements where both skills run.

#### 2. Sector overlay defaulted to banking by reflex

**Symptom**: A CFPB non-bank exam at a fintech, a state DOI market-conduct exam at an insurer, or an SEC EXAMS adviser exam comes through, and the brief loads `references/sector-overlays.md#banking` because banking was the practitioner's home territory. The MRA / MRIA convention shows up in a context where it does not exist; the engagement-playbook section quotes federal banking response windows that do not apply.

**Why it happens**: Banking is the home territory for many financial-services practitioners; the overlay loads on autopilot.

**Resolution**:
- Sector overlay loads from the scope record's `sector_overlay_set`, not from practitioner habit.
- If `sector_overlay_set = [insurance]`, load `references/sector-overlays.md#insurance` and remove banking-specific framing (MRA / MRIA, 12 CFR Part 4 CSI regime) from the brief.
- If `sector_overlay_set = [capital-markets]`, load `references/sector-overlays.md#capital-markets`; the response-window default is 30 days from deficiency letter for SEC EXAMS and varies for FINRA, not the banking convention.
- If `sector_overlay_set = [payments-fintech]`, load `references/sector-overlays.md#payments-fintech`; CFPB non-bank uses Matters Requiring Attention by parallel convention but state money-transmitter exams use state-specific findings mechanisms.
- A multi-track engagement (e.g., a fintech with a CFPB non-bank exam and a parallel state money-transmitter cycle exam) loads two overlays and carries each engagement separately in the brief.

#### 3. The out-of-scope list is empty

**Symptom**: Mid-exam, the examiner expands a request line to cover a product or business unit the firm reasonably understood to be out of scope. The firm has no written scope confirmation to point at; the engagement absorbs the expansion without challenge.

**Why it happens**: Scope confirmation went unwritten or got buried in email; the brief did not capture it.

**Resolution**:
- Capture the scope confirmation in writing in the `scope_window.scope_confirmation_source` field with a date and a pointer to the document.
- The `scope_window.out_of_scope` array carries what the regulator confirmed in writing as out of scope. An empty array signals the conversation has not happened. Force the conversation early.
- When the examiner expands scope mid-exam, request a written scope amendment. The amended scope goes in a new revision of the brief, dated, with the expansion noted. The firm gets a clean record of what changed and when.
- For SEC EXAMS engagements, the document request letter is the operative scope reference. For OCC, FRB, FDIC, and CFPB engagements, the scope memorandum or first-day letter is operative.

#### 4. CSI handled like ordinary documents

**Symptom**: Prior-cycle supervisory letters, examination reports, or MRA correspondence get circulated inside the firm to a wide population for "context." A subsequent records subpoena or M&A diligence ask sweeps in the CSI; the firm is in violation of the regulator's CSI regime.

**Why it happens**: CSI looks like a normal firm document until you read the rule. The regulator's CSI rules (12 CFR Part 4 Subpart C for OCC, Part 261 for FRB, Part 309 for FDIC, Part 1070 Subpart D for CFPB) restrict the firm's onward sharing.

**Resolution**:
- `document_handling.confidential_supervisory_information_handled = true` triggers a controlled CSI-handling protocol: need-to-know population, access logging, no onward sharing without regulator authorisation.
- Where the engagement references a prior cycle's CSI, the brief notes the source and the access-logging posture.
- Where the firm believes a legitimate need-to-know person outside the standard population must see CSI (outside counsel, board members, M&A counterparty under NDA), counsel evaluates whether regulator authorisation is required under the applicable CSI rule.
- Train the engagement team on CSI handling at engagement kickoff. CSI handling is the most common quiet-but-serious posture failure on bank-side engagements.

#### 5. Privilege posture set per-document at the last minute

**Symptom**: The production wave is due in 24 hours; counsel is reviewing 400 documents for privilege; redactions are inconsistent; the privilege log is hand-built; the team works through the weekend.

**Why it happens**: Privilege posture got set per-document at the last minute rather than per-topic in advance.

**Resolution**:
- `document_handling.privilege_review_lead_role` names the responsible role; `privilege_log_required` and `redaction_workflow` set the posture in advance.
- For each request-list item, set `privilege_posture` at the item level (`producible`, `redacted-and-producible`, `privileged-withhold`, `csi-held-by-regulator`, `under-review`). Items in `under-review` get counsel attention early, not late.
- Recurring privileged-territory categories: internal-investigation work product, root-cause-analysis materials counsel-supervised, attorney-client communications on regulatory questions, work-product on litigation-adjacent matters. Pre-categorise.
- For SEC EXAMS engagements, the privilege log accompanies any redacted production; build the log inline as redactions happen, not retrospectively.
- For FINRA Rule 8210 production, the privilege posture is contestable; counsel posture is the operative driver.

#### 6. Anticipated reviewer questions that read as FAQs

**Symptom**: The `anticipated_reviewer_questions` section reads as a generic FAQ pulled from a vendor template. Each question is plausible but not grounded; talking points are generic.

**Why it happens**: The questions were drafted from "what an examiner would probably ask" rather than from current supervisory priorities and recent enforcement themes.

**Resolution**:
- Each question carries `source_pattern` naming the basis: a specific examination priorities letter, a specific risk alert, a specific Supervisory Highlights edition, a specific public consent order, a peer-firm experience.
- For OCC, FRB, FDIC engagements, the most recent semi-annual operating plan or supervisory priorities communication drives the topic mix.
- For CFPB engagements (bank or non-bank), the most recent Supervisory Highlights edition is the operative source.
- For SEC EXAMS engagements, the most recent annual examination priorities letter and the recent risk alerts drive the topic mix; the off-channel-communications enforcement pattern since 2021 has its own gravity.
- For FINRA engagements, the most recent annual Regulatory Oversight Report drives the topic mix.
- Talking points are firm-side response postures, not scripts. A talking point of one or two sentences is enough; longer is over-engineered.

#### 7. Self-identified issues suppressed because they look bad

**Symptom**: The team strips known gaps from the brief because they would "give the examiner ammunition." The examiner finds the gaps anyway; the firm loses the credibility it would have had from self-identification.

**Why it happens**: The instinct to minimise findings overrides the discipline of self-identification.

**Resolution**:
- Self-identification is generally a credibility signal with examiners across regulators (OCC, FRB, FDIC, CFPB, SEC, FINRA, state DOIs all reward it). Suppressing material gaps backfires.
- `supervisory_history.self_identified_issues` captures the gaps the firm intends to surface proactively. Each issue carries a topic, a remediation status with a date, and an owner role.
- The brief's executive summary references the self-identified issues as a credibility item; the response-posture section pre-positions the firm's path to closure.
- Where a gap is genuinely sensitive (privileged investigation in flight, M&A-restricted), counsel sets the posture; surface the existence of the work, not the privileged details.

#### 8. Open MRA or MRIA without an owner and a date

**Symptom**: The `supervisory_history.open_mras` array carries entries with `status: open` but no `due_date`, no `owner_role`. The brief reads as drift; the examiner reads it the same way.

**Why it happens**: The closure path was not set when the MRA was issued; the issue lived in an issue tracker without firm-side ownership.

**Resolution**:
- Every open MRA, MRIA, or consent-order milestone carries an owner role and a due date in the brief. Missing either is a defect.
- The closure-submission path runs through the firm's issue-management process; the brief references the closure submission timing.
- Where the closure is in flight and the exam window straddles the closure submission, the brief notes the timing in the `anticipated_reviewer_questions` section.
- For consent orders, the milestone status reads against the order's articles; the brief carries the article-by-article status.

#### 9. Response window calculated from the wrong clock

**Symptom**: The team calculates the response window from the exit-meeting date rather than from the receipt of the supervisory letter or deficiency letter; the response is filed late, or the team scrambles to make a deadline that never applied.

**Why it happens**: The exit meeting feels like the close of the exam; in fact, the formal record-of-examination or supervisory letter is the operative trigger.

**Resolution**:
- `response_posture.response_due_calculation_basis` names the operative clock: receipt of supervisory letter (federal banking convention); receipt of deficiency letter (SEC EXAMS); receipt of exam report (FINRA cycle); receipt of CFPB supervisory letter (CFPB non-bank); receipt of state DOI examination report (insurance).
- Where the regulator has stated otherwise in writing, follow the written statement and update the field.
- For consent orders and stipulations, the clock is set by the order's articles, not by general response convention.

#### 10. Engagement-scope record stale or missing

**Symptom**: The brief was drafted from yesterday's understanding; today the regulator has confirmed an expanded scope or a participant office has joined the team. The brief no longer matches the engagement.

**Why it happens**: The scope record was treated as a kickoff artifact rather than a living record. The brief consumed an old version.

**Resolution**:
- Engagement-scope is a status, not a fixed truth. Re-emit the scope record after any material change; re-emit the exam-brief consuming the updated scope.
- Standing scope review in the engagement steering cadence (daily during fieldwork, weekly otherwise).
- Where the brief is run without an scope record at all, ask the four questions (regulator, exam type, scope window, source posture) and default to public posture if the practitioner declines. Note in the brief that scope was not formalised.

#### 11. The brief is treated as the deliverable, not the working artifact

**Symptom**: The brief gets drafted, signed off, and then sits unread for the duration of the exam. The team runs the exam from email, calendar, and informal notes.

**Why it happens**: The brief was treated as a one-time artifact for the kickoff meeting rather than as the operative working artifact for the exam window.

**Resolution**:
- The brief is the operative working artifact. The request-list mapping is the daily standup; the interview-prep section is the prep brief for each interview; the response-posture section is the contingency plan for the close.
- Update the brief continuously: status changes on request-list items, additions to the production log, lessons learned from in-flight examiner signals, additions to anticipated reviewer questions as new themes emerge.
- The post-exam after-action record consumes the final state of the brief; the next cycle's brief starts from the previous cycle's after-action.

#### 12. Boundary with sector-specific exam-readiness skills not respected

**Symptom**: The brief duplicates substantive obligation-by-obligation status mapping that the sector readiness skill is producing in parallel. Two artifacts say almost the same thing with subtle inconsistencies; the examiner notices.

**Why it happens**: The boundary between exam-brief and the sector readiness skills was not respected; both skills produced overlapping content.

**Resolution**:
- exam-brief is the engagement playbook: regulator, scope confirmation, document handling, points of contact, request-list mapping, interview prep, supervisory history, response posture, post-exam follow-up.
- The sector readiness skill is the substantive readiness pack: obligation-by-obligation status, control-by-control evidence, gap analysis against the rule, remediation roadmap.
- The two artifacts cross-reference; they do not duplicate.
- Where a sector readiness skill has produced the substantive pack, the brief's request-list mapping points at the pack's evidence inventory rather than restating it.
- Where exam-brief is run alongside `scoping`, `regulatory-impact-assessment`, `rule-to-obligation-map`, `implementation-plan`, or `policy-diff` in the same plugin, the brief consumes the upstream artifacts and does not restate them.
