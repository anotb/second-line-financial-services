# Example: CFPB Section 1071 small business lending data rule at a community bank

## Input

A community national bank originated approximately 800 covered small business credit transactions in each of the last two calendar years, placing it in the second compliance tier under the CFPB's small business lending data rule (12 CFR Part 1002 Subpart B, Section 1071, March 2023 final rule, with subsequent amendments and the post-litigation tiered effective dates). The rule-to-obligation-extraction output identifies 47 atomic obligations across data collection, firewall, recordkeeping, reporting, and consumer-notice domains. The policy-diff against the bank's current Regulation B written program produces 23 gaps. The bank's regulatory change PMO needs an implementation plan that lands the bank in compliance ahead of its tier-2 effective date with milestones, owners by role, governance cadence, and a regulator-readiness rehearsal.

## Why this scenario matters

The 1071 rule is the canonical mid-criticality regulatory change for a smaller bank. Tiered effective dates, demonstration of a privacy firewall between underwriters and demographic data, LOS or origination-platform changes, recordkeeping with strict retention, an annual Filing Instructions Guide submission to the CFPB, and a consumer-facing notice. The plan tests several boundaries the implementation-plan skill is built for: tiered compliance dates, evidence-based acceptance criteria for a firewall control, a mock submission as a regulator-readiness checkpoint, a second-line review gate before the firewall goes live, and a BAU handoff that lands the obligation in the firm's obligation inventory with ongoing monitoring.

## Output sketch

```yaml
plan_id: IMPL-2026-CFPB-1071-COMMBANK-01
engagement_id: ENG-2026-RCM-1071-01
as_of_date: 2026-05-06

trigger:
  trigger_type: final-rule
  source_citation: CFPB final rule, Small Business Lending Under the Equal Credit Opportunity Act (Regulation B), 12 CFR Part 1002 Subpart B Section 1071, March 30 2023, as amended (post-Texas-litigation tiered dates)
  trigger_id: REG-CFPB-1071
  trigger_date: 2023-03-30

effective_date: 2026-04-01
tiered_compliance_dates:
  - tier: 'Tier 2 (annual originations 500-2,499)'
    date: 2026-04-01
    rationale: 'Bank originated approximately 800 covered transactions in each of the last two calendar years; tier 2 applies.'

obligations_in_scope:
  - OBL-1071-01  # data collection scope
  - OBL-1071-02  # firewall design
  - OBL-1071-03  # demographic data collection
  - OBL-1071-04  # pricing data collection
  - OBL-1071-05  # recordkeeping retention
  - OBL-1071-06  # annual filing
  - OBL-1071-07  # consumer notice
  # ...truncated for sketch; 47 total

gaps_in_scope:
  - GAP-PD-01  # written program does not address firewall
  - GAP-PD-02  # LOS does not capture six required pricing fields
  - GAP-CG-01  # control gap, no segregation between underwriters and demographic-data collectors
  - GAP-CG-02  # no standard rejection-reason taxonomy aligned to the rule
  # ...truncated; 23 total

scope_and_source_posture:
  jurisdiction: federal
  institution_type: community national bank, OCC-supervised
  in_scope_products: [small business term loan, small business line of credit, business credit card, agricultural credit]
  in_scope_business_units: [small business banking, agricultural lending]
  in_scope_legal_entities: [the national bank]
  geographies: [bank footprint]
  out_of_scope:
    - consumer mortgage (HMDA-covered, separate program)
    - consumer auto and unsecured (not 1071-covered)
  source_posture: public-plus-firm-policy

workstreams:
  - workstream_id: WS-01
    name: Data-collection program design
    owner_role: head of small business banking compliance
    second_line_oversight_role: deputy CCO (consumer compliance)
    obligations_covered: [OBL-1071-01, OBL-1071-02, OBL-1071-03, OBL-1071-04]
    gaps_covered: [GAP-PD-01]
    milestones:
      - milestone_id: MS-01-01
        name: Written program update covering 1071 data collection, firewall, and recordkeeping
        due_date: 2025-09-30
        acceptance_criteria:
          - written program v5.0 approved by the small business banking committee
          - second-line review memo confirming alignment to 12 CFR Part 1002 Subpart B
          - policy-diff residual-gap list reduced to zero from 7 (GAP-PD-01 cluster)
        evidence_artifacts:
          - 'small business banking compliance program v5.0, approved 2025-09-30'
          - 'second-line review memo dated 2025-09-25'
        second_line_review_required: true
        status: in-progress
        confidence: high

  - workstream_id: WS-02
    name: Firewall design and operational separation
    owner_role: head of small business banking
    second_line_oversight_role: deputy CCO (consumer compliance)
    dependencies_on_other_workstreams: [WS-01]
    obligations_covered: [OBL-1071-02]
    gaps_covered: [GAP-CG-01]
    milestones:
      - milestone_id: MS-02-01
        name: Firewall design walkthrough with second line and outside counsel
        due_date: 2025-10-31
        acceptance_criteria:
          - firewall design memo signed by deputy CCO and outside counsel
          - second-line review confirming the design meets §1002.108 firewall requirements
        evidence_artifacts:
          - 'firewall design memo, 2025-10-31'
        second_line_review_required: true
        status: in-progress
        confidence: medium
      - milestone_id: MS-02-02
        name: Firewall control implementation in LOS and operational handoff
        due_date: 2025-12-15
        dependencies: [MS-02-01]
        acceptance_criteria:
          - LOS access controls confirm underwriters cannot view demographic fields by user-acceptance-test result
          - operational separation confirmed by control test workpaper
          - exception path documented with handling protocol
        evidence_artifacts:
          - UAT result log, 2025-12-15
          - control test workpaper, 2025-12-30
        second_line_review_required: true
        status: not-started
        confidence: medium

  - workstream_id: WS-03
    name: LOS and origination-platform changes
    owner_role: head of business banking technology
    second_line_oversight_role: deputy CCO (consumer compliance)
    dependencies_on_other_workstreams: [WS-01]
    obligations_covered: [OBL-1071-01, OBL-1071-03, OBL-1071-04]
    gaps_covered: [GAP-PD-02]
    milestones:
      - milestone_id: MS-03-01
        name: LOS data-field changes covering all required 1071 fields
        due_date: 2025-11-30
        acceptance_criteria:
          - LOS captures all data fields per §1002.107
          - rejection-reason taxonomy aligned to the rule's data points
          - field-level data dictionary signed by data governance
        evidence_artifacts:
          - LOS release notes, 2025-11-30
          - data dictionary v3.0, 2025-11-30
        second_line_review_required: false
        status: in-progress
        confidence: medium

  - workstream_id: WS-04
    name: Staff training and operational readiness
    owner_role: head of small business banking
    second_line_oversight_role: head of compliance training
    dependencies_on_other_workstreams: [WS-01, WS-02, WS-03]
    obligations_covered: [OBL-1071-01, OBL-1071-02, OBL-1071-03]
    milestones:
      - milestone_id: MS-04-01
        name: Training rollout to in-scope staff
        due_date: 2026-01-31
        acceptance_criteria:
          - training-completion record covers 100% of in-scope underwriters, originators, and operations staff with attestation captured by 2026-01-31
          - training content reviewed and signed by deputy CCO
        evidence_artifacts:
          - training completion log, 2026-01-31
          - attestation register
        status: not-started
        confidence: medium

  - workstream_id: WS-05
    name: Recordkeeping and retention
    owner_role: head of business banking operations
    second_line_oversight_role: head of records management
    obligations_covered: [OBL-1071-05]
    milestones:
      - milestone_id: MS-05-01
        name: Records retention schedule updated for 1071-covered transactions
        due_date: 2025-12-31
        acceptance_criteria:
          - retention schedule v6.1 incorporates the rule's retention periods
          - records-management system enforces the retention policy by automated rule
        evidence_artifacts:
          - retention schedule v6.1, 2025-12-31
        status: in-progress
        confidence: high

  - workstream_id: WS-06
    name: Reporting build and CFPB submission preparation
    owner_role: head of regulatory reporting
    second_line_oversight_role: deputy CCO (consumer compliance)
    dependencies_on_other_workstreams: [WS-03, WS-05]
    obligations_covered: [OBL-1071-06]
    milestones:
      - milestone_id: MS-06-01
        name: Mock submission against the CFPB Filing Instructions Guide layout
        due_date: 2026-02-28
        acceptance_criteria:
          - mock submission file passes the CFPB validation rules in the Filing Instructions Guide for the test calendar year
          - validation-error log empty or all errors resolved
        evidence_artifacts:
          - mock submission file, 2026-02-28
          - validation log, 2026-02-28
        second_line_review_required: true
        status: not-started
        confidence: medium

  - workstream_id: WS-07
    name: Consumer notice and applicant-facing changes
    owner_role: head of small business banking
    second_line_oversight_role: deputy CCO (consumer compliance)
    obligations_covered: [OBL-1071-07]
    milestones:
      - milestone_id: MS-07-01
        name: Applicant-facing notice rolled out across origination channels
        due_date: 2026-03-15
        acceptance_criteria:
          - notice deployed in all in-scope origination channels (branch, online, RM-led)
          - notice text reviewed by legal
          - sample-test confirms notice presented at the required point in the application flow
        evidence_artifacts:
          - notice deployment confirmation log, 2026-03-15
          - sample-test workpaper, 2026-03-20
        status: not-started
        confidence: medium

governance_checkpoints:
  - body: 1071 programme working group
    cadence: weekly
    decision_rights: operational decisions; T+5 slippage acceptance; tactical scope adjustments
    escalation_trigger: T+10 slippage; new gap discovered; vendor-delivery risk
    membership_roles: [programme manager, workstream owners, second-line lead, technology delivery lead]
    reporting_artifact: RAG status pack
  - body: regulatory change steering committee
    cadence: biweekly
    decision_rights: scope changes; resource asks; T+30 slippage acceptance
    escalation_trigger: T+30 slippage; budget overrun > 10%; CFPB follow-up question
    membership_roles: [programme sponsor, head of small business banking, head of business banking compliance, head of regulatory affairs, deputy CCO]
    reporting_artifact: RAG status pack, milestone tracker, risk register
  - body: executive risk committee
    cadence: monthly
    decision_rights: enterprise risk impact; cross-programme dependencies; readiness sign-off
    escalation_trigger: risk-appetite breach; firewall design failure; pre-effective-date readiness gap
    membership_roles: [CRO, CCO, head of regulatory affairs, programme sponsor]
    reporting_artifact: executive RAG, top risks
  - body: board risk committee
    cadence: quarterly through 2025; monthly Q1-2026 pre-effective-date
    decision_rights: board oversight; final pre-go-live sign-off; programme close-out attestation
    escalation_trigger: pre-effective-date readiness gap with customer impact; CFPB engagement
    membership_roles: [board members, CRO, CCO]
    reporting_artifact: board pre-read

implementation_risks:
  - risk_id: R-01
    description: Firewall design fails second-line or counsel review, requiring rework after MS-02-01.
    category: regulator-interpretation
    likelihood: medium
    impact: high
    mitigation: early second-line involvement at design stage; outside-counsel review before MS-02-01; tabletop walkthrough.
    owner_role: head of small business banking
    early_warning_indicator: open design questions remaining at T-30 to MS-02-01.
  - risk_id: R-02
    description: LOS vendor delivery slips on the rejection-reason taxonomy or the data dictionary, blocking WS-04 training and WS-06 mock submission.
    category: vendor
    likelihood: medium
    impact: high
    mitigation: vendor delivery checkpoints at T-60, T-30, T-14; backup plan to capture fields manually for the first reporting cycle.
    owner_role: head of business banking technology
    early_warning_indicator: missed vendor delivery checkpoint at T-30.
  - risk_id: R-03
    description: Data quality on legacy origination data does not support a clean mock submission; validation errors compound.
    category: data-readiness
    likelihood: high
    impact: medium
    mitigation: data quality assessment at MS-03-01; remediation sprint between MS-03-01 and MS-06-01.
    owner_role: head of regulatory reporting
    early_warning_indicator: validation error rate above threshold in interim test runs.
  - risk_id: R-04
    description: Operational separation between underwriters and demographic-data collectors not workable in a small branch network.
    category: control-drift
    likelihood: medium
    impact: high
    mitigation: design firewall around system access rather than physical separation; document the operational protocol; control-test workpaper at quarterly cadence post go-live.
    owner_role: head of small business banking
    early_warning_indicator: branch-level UAT shows access leakage.
  - risk_id: R-05
    description: Post-litigation tiered effective date moves again; programme assumptions break.
    category: regulator-interpretation
    likelihood: low
    impact: high
    mitigation: monitoring the CFPB rulemaking docket; quarterly programme reset against the latest official date.
    owner_role: head of regulatory affairs
    early_warning_indicator: CFPB notice on the docket; pending Supreme Court action on related case.

resource_asks:
  - role: business analyst with 1071 LOS implementation experience
    headcount: 1
    vendor_or_internal: vendor
    justification: WS-03 LOS changes require specialised 1071 mapping experience the in-house team does not have; vendor BA can be on board within four weeks.
    if_declined: MS-03-01 slips by approximately six weeks, cascading into WS-04 training and WS-06 mock submission; firewall MS-02-02 unaffected.
  - role: data quality engineer
    headcount: 1
    vendor_or_internal: internal
    justification: legacy origination data needs cleanup ahead of MS-06-01 mock submission; without cleanup the validation error rate will be unacceptable.
    if_declined: validation error rate at MS-06-01 above the threshold; rework cycle adds two months.
  - role: outside counsel review on firewall design
    budget_amount: USD 75k
    vendor_or_internal: vendor
    justification: counsel review at MS-02-01 is the practitioner pattern given §1002.108 interpretive uncertainty.
    if_declined: design risk on MS-02-01 elevates from medium to high; second-line may not sign off without counsel review.

regulator_readiness_checkpoints:
  - checkpoint_id: RR-01
    name: Mock submission against CFPB Filing Instructions Guide layout for the test year
    target_date: 2026-02-28
    evidence_produced: mock submission file, validation log
    owner_role: head of regulatory reporting
  - checkpoint_id: RR-02
    name: Firewall control-design walkthrough with second line and outside counsel
    target_date: 2025-10-31
    evidence_produced: firewall design memo, second-line review memo
    owner_role: head of small business banking
  - checkpoint_id: RR-03
    name: Tabletop on the firewall control with branch-level operating team
    target_date: 2026-03-15
    evidence_produced: tabletop findings, remediation log
    owner_role: head of small business banking
  - checkpoint_id: RR-04
    name: Pre-effective-date attestation by deputy CCO covering policy, control design, and data quality
    target_date: 2026-03-25
    evidence_produced: deputy-CCO attestation memo
    owner_role: deputy CCO (consumer compliance)

effective_date_posture:
  posture: on-time
  rationale: tier-2 effective date provides adequate runway given the gap inventory; early-adopt does not earn supervisory credit and adds risk; late-with-contingency carries enforcement risk under CFPB supervision.
  contingency_plan: if MS-03-01 or MS-06-01 slips past 2026-03-15, manual data capture for first reporting cycle; deputy CCO engages CFPB Office of Supervision Policy via the bank's CFPB primary contact.

open_questions:
  - question: Does the firewall design require physical-and-logical separation, or is logical separation alone sufficient given the branch footprint?
    audience: external-counsel
    decision_unlocked: firewall design at MS-02-01
    needed_by: 2025-10-15
  - question: Are agricultural credit transactions to operators below the small-business threshold covered or excluded?
    audience: legal
    decision_unlocked: scope of WS-01 obligation list
    needed_by: 2025-09-15
  - question: For voluntarily-collected demographic data on declined applicants pre-rule, what is the disposition?
    audience: legal
    decision_unlocked: WS-05 retention schedule
    needed_by: 2025-11-30

handoff_to_bau:
  target_owner_role: head of small business banking compliance
  evidence_pack: 1071 closure evidence pack, regulatory-affairs SharePoint, 1071 site, closure folder
  monitoring_cadence: monthly KRI review covering data-quality validation rate; quarterly control test on firewall; annual filing submission by March of each year
  obligation_inventory_pointer: firm obligation inventory, Regulation B / 1071 entries OBL-1071-01 through OBL-1071-47
  kri_kpi_pointers:
    - 1071 data-quality validation pass rate, monthly
    - firewall control test exception count, quarterly
    - applicant-facing notice presentation rate, monthly sample test

review_gates: [scope, evidence, authority, impact, decision]

confidence_label: medium

source_trace:
  - claim: 1071 final rule effective dates were tiered post-litigation; the bank's tier-2 effective date applies based on its origination volume.
    source: CFPB final rule, Small Business Lending Under the Equal Credit Opportunity Act (Regulation B), 12 CFR Part 1002 Subpart B, with subsequent amendments
    section: §1002.114 effective date and small filer compliance dates
    url: https://www.consumerfinance.gov/rules-policy/final-rules/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b/
  - claim: The rule's firewall requirement applies to underwriters' access to demographic information.
    source: 12 CFR Part 1002 Subpart B
    section: §1002.108 firewall
    url: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/subpart-B
  - claim: Annual filing under the rule follows the CFPB Filing Instructions Guide.
    source: CFPB Filing Instructions Guide for small business lending data
    section: section on filing layout and validation rules
    url: https://www.consumerfinance.gov/data-research/small-business-lending/
  - claim: CFPB MRA convention and supervisory follow-up posture.
    source: CFPB Supervision and Examination Manual
    section: examination-process section on MRAs and supervisory follow-up
    url: https://www.consumerfinance.gov/compliance/supervision-examinations/
```

## Why the plan shape matters

- The tiered-compliance-dates section names the tier the bank is in and the rationale, so the plan does not silently assume the latest-tier date.
- Acceptance criteria for the firewall milestones (MS-02-01, MS-02-02) name the artifacts (design memo, second-line review, UAT log, control test workpaper) rather than the activity (build the firewall). Examiners read the artifacts.
- The mock-submission readiness checkpoint (RR-01) tests the reporting build against the actual CFPB Filing Instructions Guide validation, surfacing data-quality risk months before go-live.
- The second-line review gate is named per workstream where it is required (firewall, recordkeeping, mock submission), not as a generic checkpoint at the end.
- The BAU handoff names the obligation inventory entries, the monitoring cadence, and the KRIs that pick up signal in BAU. The plan does not end at go-live.
- The `confidence_label: medium` is honest because three open legal questions and two resource asks remain unresolved.
