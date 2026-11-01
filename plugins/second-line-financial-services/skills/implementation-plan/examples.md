# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## cfpb-1071-community-bank

### Example: CFPB Section 1071 small business lending data rule at a community bank

#### Input

A community national bank originated approximately 1,200 covered small business credit transactions in each of the last two calendar years, putting it above the **§1071 revised final rule (May 1, 2026)** single 1,000-covered-transactions threshold (which supersedes the 2023 tiered schedule). Under the revised rule the bank is a covered FI; the rule is effective June 30, 2026 and the compliance date is January 1, 2028. The rule-to-obligation-extraction output identifies 47 atomic obligations across data collection, firewall, recordkeeping, reporting, and consumer-notice domains. The policy-diff against the bank's current Regulation B written program produces 23 gaps. The bank's regulatory change PMO needs an implementation plan that lands the bank in compliance by the January 1, 2028 compliance date with milestones, owners by role, governance cadence, and a regulator-readiness rehearsal.

#### Why this scenario matters

The 1071 rule is the canonical mid-criticality regulatory change for a smaller bank. The May 2026 revised final rule replaces the 2023 tiered schedule with a single 1,000-transaction threshold and a January 1, 2028 compliance date; the implementation programme reads against the revised rule. Demonstration of a privacy firewall between underwriters and demographic data, LOS or origination-platform changes, recordkeeping with strict retention, an annual Filing Instructions Guide submission to the CFPB, and a consumer-facing notice. The plan tests several boundaries the implementation-plan skill is built for: a long compliance-date runway, evidence-based acceptance criteria for a firewall control, a mock submission as a regulator-readiness checkpoint, a second-line review gate before the firewall goes live, and a BAU handoff that lands the obligation in the firm's obligation inventory with ongoing monitoring.

#### Output sketch

```yaml
plan_id: IMPL-2026-CFPB-1071-COMMBANK-01
engagement_id: ENG-2026-RCM-1071-01
as_of_date: 2026-05-06

trigger:
  trigger_type: final-rule
  source_citation: CFPB final rule, Small Business Lending Under the Equal Credit Opportunity Act (Regulation B), 12 CFR Part 1002 Subpart B Section 1071, March 30 2023; revised by the §1071 revised final rule, May 1, 2026 (single 1,000-transaction threshold; effective June 30, 2026; compliance January 1, 2028)
  trigger_id: REG-CFPB-1071
  trigger_date: 2026-05-01

effective_date: 2026-06-30
compliance_dates:
  - description: 'All covered FIs (single 1,000-covered-transactions threshold under the May 2026 revised final rule; supersedes the 2023 Tier 1 / 2 / 3 schedule)'
    date: 2028-01-01
    rationale: 'Bank originated approximately 1,200 covered transactions in each of the last two calendar years; covered FI under the revised rule.'

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
  rationale: January 1, 2028 compliance date under the May 2026 revised final rule provides adequate runway given the gap inventory; early-adopt does not earn supervisory credit and adds risk; late-with-contingency carries enforcement risk under CFPB supervision.
  contingency_plan: if material milestones slip inside the final 60 days before compliance date, manual data capture for first reporting cycle; deputy CCO engages CFPB Office of Supervision Policy via the bank's CFPB primary contact.

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
  - claim: 1071 single 1,000-covered-transactions threshold and January 1, 2028 compliance date apply (May 2026 revised final rule supersedes the 2023 tiered schedule).
    source: §1071 revised final rule (May 1, 2026)
    section: §1002.105 (revised threshold); §1002.114 (revised effective and compliance dates)
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

#### Why the plan shape matters

- The tiered-compliance-dates section names the tier the bank is in and the rationale, so the plan does not silently assume the latest-tier date.
- Acceptance criteria for the firewall milestones (MS-02-01, MS-02-02) name the artifacts (design memo, second-line review, UAT log, control test workpaper) rather than the activity (build the firewall). Examiners read the artifacts.
- The mock-submission readiness checkpoint (RR-01) tests the reporting build against the actual CFPB Filing Instructions Guide validation, surfacing data-quality risk months before go-live.
- The second-line review gate is named per workstream where it is required (firewall, recordkeeping, mock submission), not as a generic checkpoint at the end.
- The BAU handoff names the obligation inventory entries, the monitoring cadence, and the KRIs that pick up signal in BAU. The plan does not end at go-live.
- The `confidence_label: medium` is honest because three open legal questions and two resource asks remain unresolved.

## sec-cyber-disclosure-adviser

### Example: SEC cybersecurity disclosure rule at a registered investment adviser with a public-company parent

#### Input

A registered investment adviser is a wholly-owned subsidiary of a public company that files Forms 10-K and 8-K with the SEC. The 2023 SEC final rule on cybersecurity risk management, strategy, governance, and incident disclosure (Release Nos. 33-11216; 34-97989) brings new obligations to the parent: 8-K Item 1.05 reporting of material cybersecurity incidents within four business days of materiality determination, and annual Regulation S-K Item 106 disclosure of cybersecurity risk management, strategy, and governance. The adviser does not file 8-K but contributes to parent disclosure. The chief compliance officer at the adviser, the CISO at the group level, the head of regulatory reporting at the parent, and outside counsel coordinate on a consolidated implementation plan covering the parent and the adviser. The plan reaches steady state ahead of the parent's first 10-K filing under the rule.

#### Why this scenario matters

This is a multi-entity, multi-discipline plan: SEC corporate disclosure, cyber risk governance, and adviser compliance running concurrently. The implementation-plan skill is built for this shape. The plan tests the materiality-determination playbook (a control-design milestone, not a disclosure milestone), the 8-K Item 1.05 trigger workflow under a tight four-business-day window, the 10-K Item 106 narrative drafting cycle aligned to the parent's reporting calendar, the disclosure-committee charter update, and the second-line review at the parent level for both 8-K and 10-K disclosures. Materiality is the load-bearing decision; the plan invests in the playbook and the disclosure-committee process rather than a disclosure-templating exercise.

#### Output sketch

```yaml
plan_id: IMPL-2026-SEC-CYBER-DISC-01
engagement_id: ENG-2026-RCM-SEC-CYBER-01
as_of_date: 2026-05-06

trigger:
  trigger_type: final-rule
  source_citation: SEC final rule, Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure, Release Nos. 33-11216; 34-97989, July 26 2023
  trigger_id: REG-SEC-CYBER-DISC
  trigger_date: 2023-07-26

effective_date: 2024-12-15

obligations_in_scope:
  - OBL-CYB-01  # 8-K Item 1.05 incident disclosure
  - OBL-CYB-02  # 8-K Item 1.05 timing (four business days from materiality)
  - OBL-CYB-03  # 8-K Item 1.05 amendment procedure
  - OBL-CYB-04  # 10-K Item 106(b) risk management and strategy
  - OBL-CYB-05  # 10-K Item 106(c) governance, including board oversight
  - OBL-CYB-06  # iXBRL tagging for Item 106
  # ...truncated

gaps_in_scope:
  - GAP-PD-01  # disclosure-committee charter does not address Item 1.05 trigger
  - GAP-PD-02  # IR procedure does not capture materiality assessment
  - GAP-CG-01  # incident response procedure does not bridge to disclosure decision
  - GAP-CG-02  # board-oversight narrative is undocumented
  # ...truncated

scope_and_source_posture:
  jurisdiction: federal
  institution_type: registered investment adviser, subsidiary of a public-company parent
  in_scope_products: [parent 10-K filing; parent 8-K filings; adviser internal cyber program]
  in_scope_business_units: [parent disclosure / SEC reporting; group cyber; adviser compliance]
  in_scope_legal_entities: [the public-company parent; the registered adviser]
  out_of_scope:
    - SEC adviser-specific cybersecurity rule (proposed, not final at plan date)
    - other 8-K items
    - other 10-K items beyond Item 106
  source_posture: public-plus-firm-policy

workstreams:
  - workstream_id: WS-01
    name: Materiality-determination playbook
    owner_role: parent general counsel
    second_line_oversight_role: parent chief compliance officer; adviser chief compliance officer
    obligations_covered: [OBL-CYB-01, OBL-CYB-02]
    gaps_covered: [GAP-PD-02, GAP-CG-01]
    milestones:
      - milestone_id: MS-01-01
        name: Materiality-determination playbook drafted and approved by disclosure committee
        due_date: 2024-09-30
        acceptance_criteria:
          - playbook describes the materiality-assessment process from incident detection through disclosure decision
          - playbook bridges incident-response procedure (CISO-owned) to disclosure decision (general-counsel-owned)
          - playbook signed by general counsel, CISO, parent CCO
        evidence_artifacts:
          - 'cybersecurity materiality-determination playbook v1.0, 2024-09-30'
        second_line_review_required: true
        status: complete
        confidence: high
      - milestone_id: MS-01-02
        name: First tabletop on the playbook with disclosure committee, IR team, group communications
        due_date: 2024-11-15
        dependencies: [MS-01-01]
        acceptance_criteria:
          - tabletop scenario covers a credible incident profile
          - tabletop findings logged with named owner per finding
          - playbook updates incorporated into v1.1
        evidence_artifacts:
          - tabletop findings memo, 2024-11-30
          - playbook v1.1, 2024-12-05
        status: complete
        confidence: high

  - workstream_id: WS-02
    name: Disclosure-committee charter and process update
    owner_role: parent corporate secretary
    second_line_oversight_role: parent CCO
    dependencies_on_other_workstreams: [WS-01]
    obligations_covered: [OBL-CYB-01, OBL-CYB-02, OBL-CYB-03]
    gaps_covered: [GAP-PD-01]
    milestones:
      - milestone_id: MS-02-01
        name: Disclosure-committee charter updated to include Item 1.05 trigger and standing cyber agenda item
        due_date: 2024-10-31
        acceptance_criteria:
          - charter v3.0 names cybersecurity-incident materiality as a standing committee responsibility
          - charter approved by audit committee
        evidence_artifacts:
          - 'disclosure-committee charter v3.0, approved 2024-10-31'
          - audit-committee minutes
        status: complete
        confidence: high

  - workstream_id: WS-03
    name: 8-K Item 1.05 procedure and template
    owner_role: parent head of regulatory reporting
    second_line_oversight_role: parent CCO; outside counsel
    dependencies_on_other_workstreams: [WS-01, WS-02]
    obligations_covered: [OBL-CYB-01, OBL-CYB-02, OBL-CYB-03]
    milestones:
      - milestone_id: MS-03-01
        name: 8-K Item 1.05 procedure approved
        due_date: 2024-11-30
        acceptance_criteria:
          - procedure names the four-business-day clock starting at materiality determination
          - procedure addresses delayed-disclosure exception under §240.13a-11(c) (national security and public safety)
          - procedure addresses amendment workflow when previously-undetermined facts become determinable
          - procedure reviewed by outside counsel
        evidence_artifacts:
          - 8-K Item 1.05 procedure v1.0, 2024-11-30
          - outside-counsel review memo
        second_line_review_required: true
        status: complete
        confidence: high

  - workstream_id: WS-04
    name: 10-K Item 106 narrative build
    owner_role: parent head of regulatory reporting
    second_line_oversight_role: parent CCO; CISO; outside counsel
    obligations_covered: [OBL-CYB-04, OBL-CYB-05, OBL-CYB-06]
    gaps_covered: [GAP-CG-02]
    milestones:
      - milestone_id: MS-04-01
        name: First-year Item 106 narrative drafted and reviewed
        due_date: 2025-01-31
        acceptance_criteria:
          - narrative covers Item 106(b) risk management and strategy
          - narrative covers Item 106(c) governance including board oversight
          - narrative reviewed by outside counsel and audit committee
          - iXBRL tags applied per the rule
        evidence_artifacts:
          - 'draft 10-K Item 106 v1.0, 2025-01-31'
          - outside-counsel review memo
          - audit-committee minutes
        second_line_review_required: true
        status: complete
        confidence: high

  - workstream_id: WS-05
    name: Adviser-side coordination and CCO awareness
    owner_role: adviser chief compliance officer
    second_line_oversight_role: adviser deputy CCO
    obligations_covered: [OBL-CYB-01]
    milestones:
      - milestone_id: MS-05-01
        name: Adviser CCO procedure for incident escalation to parent disclosure committee
        due_date: 2024-12-15
        acceptance_criteria:
          - procedure names the trigger for escalation from adviser to parent disclosure committee
          - procedure incorporated into the adviser's compliance program under IAA Rule 206(4)-7 written-policies framework
        evidence_artifacts:
          - adviser cyber-incident escalation procedure v1.0, 2024-12-15
        status: complete
        confidence: high

governance_checkpoints:
  - body: programme working group
    cadence: weekly during build (through 2025-Q1)
    decision_rights: operational decisions; T+5 slippage acceptance
    escalation_trigger: T+10 slippage; new gap discovered; outside-counsel-flagged interpretive question
    membership_roles: [programme manager, parent corporate secretary, parent CCO, CISO, parent head of regulatory reporting, adviser CCO, outside counsel]
    reporting_artifact: RAG status pack
  - body: disclosure committee
    cadence: standing; out-of-cycle on incident materiality questions
    decision_rights: materiality determinations; 8-K Item 1.05 disclosure decisions; 10-K Item 106 narrative approval
    escalation_trigger: any incident assessed as potentially material; any 10-K narrative change after pre-clearance
    membership_roles: [parent general counsel, parent CFO, parent CCO, parent head of investor relations, parent corporate secretary]
    reporting_artifact: incident-materiality memo (per incident); 10-K Item 106 narrative draft
  - body: audit committee
    cadence: quarterly; out-of-cycle on a material incident
    decision_rights: oversight of cyber risk management programme; 10-K Item 106 governance disclosure approval
    escalation_trigger: material incident; auditor-raised concerns on the cyber programme
    membership_roles: [audit committee chair, audit committee members, parent CFO, CISO, parent CCO]
    reporting_artifact: cyber programme dashboard; 10-K Item 106 narrative draft

implementation_risks:
  - risk_id: R-01
    description: Materiality determination on a borderline incident triggers an 8-K filing under time pressure with incomplete facts.
    category: regulator-interpretation
    likelihood: medium
    impact: high
    mitigation: tabletop programme covering ambiguous-materiality scenarios; outside-counsel on retainer for materiality calls; amendment-workflow rehearsed.
    owner_role: parent general counsel
    early_warning_indicator: tabletop reveals a materiality call the team cannot make in four business days.
  - risk_id: R-02
    description: 10-K Item 106 narrative pre-clearance with auditor surfaces governance gaps requiring board-action before filing.
    category: scope-creep
    likelihood: low
    impact: medium
    mitigation: pre-clearance with auditor at MS-04-01 minus 60 days; board action items identified ahead of the filing window.
    owner_role: parent head of regulatory reporting
    early_warning_indicator: auditor question on board oversight at pre-clearance.
  - risk_id: R-03
    description: Coordination breakdown between CISO and disclosure committee on incident facts; disclosure committee operates from incomplete information.
    category: interdependency
    likelihood: medium
    impact: high
    mitigation: standing CISO seat at disclosure committee for any potential-materiality discussion; named CISO deputy for handoff continuity.
    owner_role: CISO
    early_warning_indicator: tabletop reveals CISO-to-committee information lag.
  - risk_id: R-04
    description: Adviser-side incident coordinator does not escalate quickly enough to parent disclosure committee.
    category: control-drift
    likelihood: low
    impact: high
    mitigation: adviser CCO standing item on the disclosure committee agenda; escalation-procedure tabletop with adviser staff.
    owner_role: adviser CCO
    early_warning_indicator: adviser-side incident not escalated in time during a tabletop.

resource_asks:
  - role: outside counsel cybersecurity-disclosure retainer
    budget_amount: USD 200k for first year
    vendor_or_internal: vendor
    justification: Item 1.05 materiality calls happen under time pressure; counsel-on-retainer model is the practitioner pattern.
    if_declined: materiality calls take longer; risk of late disclosure or over-disclosure.
  - role: dedicated programme manager through first 10-K cycle
    headcount: 1
    vendor_or_internal: internal
    justification: cross-entity coordination across parent disclosure, group cyber, and adviser compliance requires named programme management.
    if_declined: handoff and coordination quality declines; tabletop programme suffers.

regulator_readiness_checkpoints:
  - checkpoint_id: RR-01
    name: First Item 1.05 tabletop
    target_date: 2024-11-15
    evidence_produced: tabletop findings memo, playbook updates
    owner_role: parent general counsel
  - checkpoint_id: RR-02
    name: Second Item 1.05 tabletop with ambiguous-materiality scenario
    target_date: 2025-03-15
    evidence_produced: tabletop findings memo, playbook updates
    owner_role: parent general counsel
  - checkpoint_id: RR-03
    name: 10-K Item 106 narrative pre-clearance with auditor
    target_date: 2024-12-15
    evidence_produced: pre-clearance memo
    owner_role: parent head of regulatory reporting
  - checkpoint_id: RR-04
    name: Annual disclosure-committee training
    target_date: 2025-01-15
    evidence_produced: training-completion log
    owner_role: parent corporate secretary

effective_date_posture:
  posture: on-time
  rationale: rule effective dates are non-negotiable; 8-K Item 1.05 effective December 18 2023 (90 days after Federal Register publication; smaller reporting companies later); 10-K Item 106 first applies to fiscal years ending on or after December 15 2023.
  contingency_plan: if a material incident lands before MS-03-01, manual-process Item 1.05 disclosure under outside-counsel direction; programme accelerates to close the gap.

open_questions:
  - question: For a borderline-materiality incident at the adviser subsidiary, does the parent's Item 1.05 disclosure obligation attach, and on what trigger?
    audience: external-counsel
    decision_unlocked: adviser-to-parent escalation procedure under MS-05-01
    needed_by: 2024-12-01
  - question: For an incident affecting a critical service provider, is the four-business-day clock the firm's materiality determination or the service provider's?
    audience: external-counsel
    decision_unlocked: 8-K Item 1.05 procedure under MS-03-01
    needed_by: 2024-11-15

handoff_to_bau:
  target_owner_role: parent corporate secretary (disclosure committee secretariat); parent CCO (programme oversight); CISO (cyber programme); adviser CCO (adviser-side awareness)
  evidence_pack: cyber disclosure programme closure pack, regulatory-affairs SharePoint, cyber-disclosure site, closure folder
  monitoring_cadence: standing disclosure committee with cyber agenda item; annual tabletop; annual 10-K Item 106 narrative refresh; per-incident materiality logging
  obligation_inventory_pointer: firm obligation inventory, SEC cyber disclosure entries OBL-CYB-01 through OBL-CYB-06
  kri_kpi_pointers:
    - tabletop frequency and findings
    - 8-K Item 1.05 filings count and timing
    - 10-K Item 106 narrative annual review status

review_gates: [scope, evidence, authority, impact, decision]

confidence_label: high

source_trace:
  - claim: 8-K Item 1.05 requires disclosure of a material cybersecurity incident within four business days of the materiality determination.
    source: SEC final rule, Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure
    section: Item 1.05 of Form 8-K (Release Nos. 33-11216; 34-97989), Section II.A
    url: https://www.sec.gov/files/rules/final/2023/33-11216.pdf
  - claim: Regulation S-K Item 106(b) requires disclosure of cybersecurity risk management and strategy in Form 10-K.
    source: SEC final rule, Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure
    section: Regulation S-K Item 106(b)
    url: https://www.sec.gov/files/rules/final/2023/33-11216.pdf
  - claim: Regulation S-K Item 106(c) requires disclosure of cybersecurity governance including board oversight.
    source: SEC final rule, Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure
    section: Regulation S-K Item 106(c)
    url: https://www.sec.gov/files/rules/final/2023/33-11216.pdf
  - claim: SEC EDGAR Filing Manual sets the iXBRL tagging requirements for Item 106.
    source: SEC EDGAR Filer Manual
    section: section on Item 106 inline XBRL tagging
    url: https://www.sec.gov/edgar/filer-information
  - claim: Adviser-side compliance programme requirements apply under IAA Rule 206(4)-7.
    source: SEC, Investment Advisers Act Rule 206(4)-7
    section: Rule 206(4)-7 written compliance policies and procedures
    url: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7
```

#### Why the plan shape matters

- The materiality-determination playbook (WS-01) is the load-bearing control; the plan invests there ahead of disclosure-templating, because the harder decision is materiality, not disclosure.
- The disclosure committee is named as a standing governance body with out-of-cycle escalation rights on incident materiality. This matches the rule's four-business-day clock; a quarterly committee cannot make this call in time.
- The tabletop programme (RR-01, RR-02) rehearses ambiguous-materiality scenarios; a single incident-response tabletop on a clear-cut scenario does not test the playbook.
- Acceptance criteria for the 10-K Item 106 narrative milestone (MS-04-01) name pre-clearance with the auditor, audit-committee review, and iXBRL tagging. These are evidence artifacts, not activities.
- The adviser-side workstream (WS-05) is light, because the adviser is not the filer; the plan records the escalation procedure under IAA Rule 206(4)-7 written-policies framework so the adviser's compliance program reflects the obligation.
- The `confidence_label: high` is honest because the plan is in steady state by the time of writing; in earlier states the label would be `medium` due to the open materiality-call questions and untested tabletops.

## troubleshooting

### Troubleshooting

Common pitfalls when drafting an implementation plan.

#### Owners are names, not roles

Roles survive turnover; names do not. The plan tracks roles. A separate RACI links the named individual to the role at any point in time. If an upstream input carries a named individual, translate to the role on intake (head of TPRM, CISO, head of regulatory reporting, business-line CRO, head of compliance testing).

#### Acceptance criteria read like activities

"Complete training" is an activity, not evidence. "Training-completion record covers 100% of in-scope staff, attestation captured by [date], retained per recordkeeping policy" is evidence. Examiners ask for the artifact, not the activity log. Restate every activity-shaped acceptance criterion as the artifact that proves closure.

#### Milestones bunch at the mandatory date

A plan with the bulk of milestones in the last month of the transition is high-risk by construction. The realistic recovery path is narrow because dependent milestones cannot start until prior ones close. Push the bulk to mid-transition where the dependency chain allows; where it does not, flag the late-loaded milestone as an explicit implementation risk with a contingency.

#### No second-line review point before go-live

A plan that goes from first-line build to go-live without an explicit second-line review of control design fails the second-line gate. The regulator's expectation is that the second line independently confirms control design and challenges residual gaps before the control runs in production. Name the second-line role per workstream and place a dated review checkpoint before the milestone closes.

#### Plan ends at go-live with no BAU handoff

A remediation that closes without a documented handoff into the obligation inventory and an ongoing monitoring cadence will drift within twelve months. The BAU section names the role that owns the obligation after closure, the closure evidence pack, the monitoring cadence, and the KRI or KPI that picks up signal in BAU. If the plan does not name these, it is not finished.

#### Resource asks are generic

"More resources" does not survive a steering committee. Each ask names the role, the milestone it unblocks, and the consequence if declined. A steering committee can act on "one business analyst with 1071 LOS experience for Q3-Q4, otherwise milestone MS-04 slips by six weeks". It cannot act on "we need more people".

#### Anchored to the wrong source

Implementation-plan structure is rule-agnostic, but the rule citations belong to the trigger. If the trigger is a final rule, anchor to the final rule and the adopting release. If the trigger is an MRA or consent order, anchor to the supervisory letter or order text and to the agency's published supervisory framework. If the trigger is a self-identified issue, anchor to the firm's issue-management policy plus the underlying obligation. Generic citation to OCC or FRB without naming the bulletin or SR letter is not anchoring.

#### Tiered compliance dates collapsed to a single date

A rule with tiered effective dates (e.g., 1071 by origination volume) at an institution that touches more than one tier needs the tier-specific dates carried in the plan. Collapsing to the latest date misreads the smaller-tier obligation and risks under-compliance for the bigger-tier population.

#### Governance cadence does not match criticality

A weekly working group plus a quarterly steering committee may be right for a low-criticality programme. It is wrong for an MRIA-driven programme with material customer impact, where the cadence escalates to weekly working group, biweekly steering, monthly executive risk committee, and quarterly board reporting. Match cadence to criticality; under-governing a high-criticality programme is the more common failure mode than over-governing a small one.

#### Regulator-readiness checkpoints missing

Going live on the mandatory date without a mock submission, a tabletop, and a second-line walkthrough leaves the firm with no rehearsal. The first encounter with the operating control should not be the first day of supervisory attention. Three readiness checkpoints (mock reporting submission, control-design walkthrough, tabletop) sized to the rule are the practitioner pattern.

#### Confidence label inflated

`high` confidence on a plan with five open legal questions and three resource asks unfunded is not credible. The honest read is `medium`. Confidence drops further when the trigger source carries `[verify section]` flags or when the gap inventory is incomplete. The label is a signal to the steering committee about what they are signing off on.

#### Plan drafted from the gap list alone

A plan built only from policy-diff and control-gap output misses the supervisory and governance dimension. The plan also covers governance cadence (steering, executive, board), implementation risks, regulator-readiness checkpoints, effective-date posture, and BAU handoff. A gap-only plan reads like a punch list and lands flat with the steering committee. The full shape is the practitioner artifact.
