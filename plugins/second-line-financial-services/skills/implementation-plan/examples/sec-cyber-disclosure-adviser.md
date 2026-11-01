# Example: SEC cybersecurity disclosure rule at a registered investment adviser with a public-company parent

## Input

A registered investment adviser is a wholly-owned subsidiary of a public company that files Forms 10-K and 8-K with the SEC. The 2023 SEC final rule on cybersecurity risk management, strategy, governance, and incident disclosure (Release Nos. 33-11216; 34-97989) brings new obligations to the parent: 8-K Item 1.05 reporting of material cybersecurity incidents within four business days of materiality determination, and annual Regulation S-K Item 106 disclosure of cybersecurity risk management, strategy, and governance. The adviser does not file 8-K but contributes to parent disclosure. The chief compliance officer at the adviser, the CISO at the group level, the head of regulatory reporting at the parent, and outside counsel coordinate on a consolidated implementation plan covering the parent and the adviser. The plan reaches steady state ahead of the parent's first 10-K filing under the rule.

## Why this scenario matters

This is a multi-entity, multi-discipline plan: SEC corporate disclosure, cyber risk governance, and adviser compliance running concurrently. The implementation-plan skill is built for this shape. The plan tests the materiality-determination playbook (a control-design milestone, not a disclosure milestone), the 8-K Item 1.05 trigger workflow under a tight four-business-day window, the 10-K Item 106 narrative drafting cycle aligned to the parent's reporting calendar, the disclosure-committee charter update, and the second-line review at the parent level for both 8-K and 10-K disclosures. Materiality is the load-bearing decision; the plan invests in the playbook and the disclosure-committee process rather than a disclosure-templating exercise.

## Output sketch

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

## Why the plan shape matters

- The materiality-determination playbook (WS-01) is the load-bearing control; the plan invests there ahead of disclosure-templating, because the harder decision is materiality, not disclosure.
- The disclosure committee is named as a standing governance body with out-of-cycle escalation rights on incident materiality. This matches the rule's four-business-day clock; a quarterly committee cannot make this call in time.
- The tabletop programme (RR-01, RR-02) rehearses ambiguous-materiality scenarios; a single incident-response tabletop on a clear-cut scenario does not test the playbook.
- Acceptance criteria for the 10-K Item 106 narrative milestone (MS-04-01) name pre-clearance with the auditor, audit-committee review, and iXBRL tagging. These are evidence artifacts, not activities.
- The adviser-side workstream (WS-05) is light, because the adviser is not the filer; the plan records the escalation procedure under IAA Rule 206(4)-7 written-policies framework so the adviser's compliance program reflects the obligation.
- The `confidence_label: high` is honest because the plan is in steady state by the time of writing; in earlier states the label would be `medium` due to the open materiality-call questions and untested tabletops.
