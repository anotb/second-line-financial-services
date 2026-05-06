# Example: SEC cybersecurity disclosure final rule decomposed into atomic obligations

## Input

The SEC's final rule on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure, 88 FR 51896 (July 26 2023), codified at 17 CFR 229.106 (Reg S-K Item 106), 17 CFR 232.405 (inline XBRL), 17 CFR 240.13a-11 and 17 CFR 240.15d-11 (Form 8-K coverage), and 17 CFR 249.308 (Form 8-K Item 1.05). Effective date September 5 2023. Compliance dates: incident-disclosure compliance December 18 2023 for non-smaller reporting companies; June 15 2024 for smaller reporting companies. Risk-management-and-strategy compliance with annual reports for fiscal years ending on or after December 15 2023; SRC delay of one year for those disclosures.

The regulatory-change committee at a public-company registrant has the rule on the agenda. The change lead needs the atomic obligation list before the committee meets, before the firm's existing 8-K materiality framework is updated, before the firm's 10-K disclosure controls run their next quarterly review, and before legal opens the question of how to handle the Attorney-General-national-security delay. This is the canonical net-new-rule extraction case for this skill.

## Why this scenario matters

The SEC cyber rule is well-suited to demonstrate the atomic-obligation discipline because the rule combines event-driven disclosure (the 4-business-day Form 8-K Item 1.05 obligation) with annual disclosure (the Reg S-K Item 106 disclosures), each with their own conditions, frequencies, exceptions, and evidence shapes. Compressing the event-driven and annual obligations into a single "the firm must comply with the SEC cyber rule" obligation is the most common defect; the rule actually decomposes into at least seven atomic obligations across the operative sections.

## Output sketch

```yaml
extraction_id: RTOE-2026-SEC-CYBER-01
as_of_date: 2026-05-06

source_citation:
  regulator: SEC
  regulator_office: SEC Division of Corporation Finance
  instrument_type: final-rule
  citation: 88 FR 51896
  section_reference: 17 CFR 229.106; 17 CFR 249.308; Form 8-K Item 1.05
  publication_date: 2023-07-26
  effective_date: 2023-09-05
  compliance_dates:
    - date: 2023-12-18
      tier_or_topic: incident-disclosure compliance for non-smaller reporting companies
    - date: 2024-06-15
      tier_or_topic: incident-disclosure compliance for smaller reporting companies
    - date: 2023-12-15
      tier_or_topic: risk-management-and-strategy disclosure (with annual reports for fiscal years ending on or after this date)
  url: https://www.sec.gov/files/rules/final/2023/33-11216.pdf

extraction_summary:
  obligation_count: 7
  by_section:
    - section_reference: Form 8-K Item 1.05
      obligation_count: 2
    - section_reference: 17 CFR 229.106(b)
      obligation_count: 1
    - section_reference: 17 CFR 229.106(c)(1)
      obligation_count: 1
    - section_reference: 17 CFR 229.106(c)(2)
      obligation_count: 1
    - section_reference: 17 CFR 232.405
      obligation_count: 1
    - section_reference: Form 8-K Item 1.05(c)
      obligation_count: 1

obligations:
  - obligation_id: OBL-001
    source_pin:
      section: Form 8-K Item 1.05 instructions
      preamble_context: 88 FR 51896 at 51908-51910 on materiality determination
    action_verb: must
    party_obligated: registrant (each Section 13(a) and 15(d) reporting company)
    requirement_statement: The registrant must determine without unreasonable delay following discovery whether a cybersecurity incident is material.
    condition_or_trigger: discovery of a covered cybersecurity incident
    deadline: without unreasonable delay following discovery; the rule does not name a calendar deadline for the determination itself, but the determination starts the 4-business-day clock for OBL-002
    exception: none for the determination itself
    frequency: on_event
    action_type: governance
    evidence_expected:
      - incident-determination memo or record signed by named-role decision-maker
      - cyber-incident-response playbook entries logging the determination event
    cross_refs: [OBL-002]
    defined_terms_used: ["cybersecurity incident", "cybersecurity threat"]
    applicability:
      institution_types: [SEC-registered Section 13(a) and 15(d) reporting companies]
    confidence: medium
    status: open-question
    open_questions:
      - At what point does the 4-business-day clock start when a determination is made and then revised? Resolution: legal review.

  - obligation_id: OBL-002
    source_pin:
      section: Form 8-K Item 1.05(a)
      sentence_or_subsection: "the registrant shall file a current report on Form 8-K..."
    action_verb: shall
    party_obligated: registrant
    requirement_statement: The registrant must file a Form 8-K Item 1.05 disclosing the material cybersecurity incident within 4 business days of the materiality determination, describing the material aspects of the nature, scope, and timing of the incident and the material impact or reasonably likely material impact on the registrant.
    condition_or_trigger: materiality determination per OBL-001
    deadline: within 4 business days of the materiality determination
    exception: Attorney-General-national-security delay under Item 1.05(c) (limited to circumstances where disclosure poses substantial risk to national security or public safety; the Attorney General notifies the SEC in writing; the registrant may delay up to 30 days, with one 30-day extension, and additional limited extensions in extraordinary circumstances)
    frequency: on_event
    action_type: notice_or_disclosure
    evidence_expected:
      - filed Form 8-K Item 1.05
      - disclosure-controls-and-procedures attestation that the filing was timely
      - if delay invoked, Attorney-General notification record
    cross_refs: [OBL-001]
    defined_terms_used: ["cybersecurity incident"]
    confidence: high
    status: draft

  - obligation_id: OBL-003
    source_pin:
      section: 17 CFR 229.106(b)(1)
    action_verb: shall describe
    party_obligated: registrant
    requirement_statement: The registrant must describe its processes, if any, for assessing, identifying, and managing material risks from cybersecurity threats in sufficient detail for a reasonable investor to understand those processes.
    condition_or_trigger: annual report (Form 10-K Part I Item 1C)
    deadline: filing of the annual report; for fiscal years ending on or after December 15 2023 (with a one-year delay for SRCs)
    frequency: periodic
    action_type: notice_or_disclosure
    evidence_expected:
      - cybersecurity risk-management-process documentation linking to the disclosure
      - Form 10-K Item 1C disclosure
    cross_refs: [OBL-004, OBL-005, OBL-007]
    defined_terms_used: ["cybersecurity threat"]
    confidence: high
    status: draft

  - obligation_id: OBL-004
    source_pin:
      section: 17 CFR 229.106(c)(1)
    action_verb: shall describe
    party_obligated: registrant
    requirement_statement: The registrant must describe the board of directors' oversight of risks from cybersecurity threats, including the identification of any board committee or subcommittee responsible for the oversight and the processes by which the board or such committee is informed about such risks.
    condition_or_trigger: annual report
    deadline: filing of the annual report
    frequency: periodic
    action_type: governance
    evidence_expected:
      - board or committee charter cybersecurity-oversight provisions
      - board-meeting minutes showing cybersecurity briefings
      - Form 10-K Item 1C disclosure
    cross_refs: [OBL-003, OBL-005]
    confidence: high
    status: draft

  - obligation_id: OBL-005
    source_pin:
      section: 17 CFR 229.106(c)(2)
    action_verb: shall describe
    party_obligated: registrant
    requirement_statement: The registrant must describe management's role in assessing and managing the registrant's material risks from cybersecurity threats, including the relevant management positions or committees responsible for assessing and managing such risks, the relevant expertise of such persons, the processes by which such persons are informed about and monitor the prevention, detection, mitigation, and remediation of cybersecurity incidents, and whether such persons or committees report information about such risks to the board of directors or a committee or subcommittee of the board of directors.
    condition_or_trigger: annual report
    deadline: filing of the annual report
    frequency: periodic
    action_type: governance
    evidence_expected:
      - description of the management position(s) and expertise
      - management-reporting cadence to the board
      - Form 10-K Item 1C disclosure
    cross_refs: [OBL-003, OBL-004]
    confidence: high
    status: draft

  - obligation_id: OBL-006
    source_pin:
      section: 17 CFR 232.405
    action_verb: must tag
    party_obligated: registrant
    requirement_statement: The registrant must tag the disclosures required under Item 1.05 and Item 106 in inline XBRL.
    condition_or_trigger: any required filing of Item 1.05 or Item 106 disclosures
    deadline: with the filing; phased in by registrant size
    frequency: on_event
    action_type: notice_or_disclosure
    evidence_expected:
      - inline XBRL tagging in the filed document
      - filing-system validation log
    cross_refs: [OBL-002, OBL-003, OBL-004, OBL-005]
    confidence: high
    status: draft

  - obligation_id: OBL-007
    source_pin:
      section: Form 8-K Item 1.05(c)
    action_verb: may delay
    party_obligated: registrant
    requirement_statement: The registrant may delay the disclosure required under Item 1.05(a) if the United States Attorney General determines that immediate disclosure would pose a substantial risk to national security or public safety and notifies the Commission of such determination in writing.
    condition_or_trigger: Attorney-General national-security or public-safety determination
    deadline: delay up to 30 days from the original 4-business-day deadline; one 30-day extension and additional extraordinary-circumstances extensions per the rule
    frequency: on_event
    action_type: notice_or_disclosure
    evidence_expected:
      - Attorney-General notification to the SEC
      - registrant's record of the delay invocation
    cross_refs: [OBL-002]
    confidence: medium
    status: open-question
    open_questions:
      - The Attorney-General delay is initiated by the AG, not by the registrant. What is the registrant's posture if it believes a delay is warranted but the AG has not yet notified the SEC? Resolution: outside-counsel review.

cross_references:
  - from_obligation_id: OBL-001
    to_obligation_id: OBL-002
    relationship: produces_record_for
    notes: The materiality determination starts the 4-business-day clock for the Form 8-K filing.
  - from_obligation_id: OBL-002
    to_obligation_id: OBL-007
    relationship: is_exception_to
    notes: Item 1.05(c) is the national-security delay exception to Item 1.05(a) timing.
  - from_obligation_id: OBL-006
    to_obligation_id: OBL-002
    relationship: governs
    notes: Inline-XBRL tagging applies to the Item 1.05 filing.

defined_terms:
  - term: cybersecurity incident
    definition: An unauthorised occurrence, or a series of related unauthorised occurrences, on or conducted through a registrant's information systems that jeopardises the confidentiality, integrity, or availability of a registrant's information systems or any information residing therein.
    source_section: 17 CFR 229.106(a)
    obligation_ids_using_term: [OBL-001, OBL-002]
  - term: cybersecurity threat
    definition: Any potential unauthorised occurrence on or conducted through a registrant's information systems that may result in adverse effects on the confidentiality, integrity, or availability of a registrant's information systems or any information residing therein.
    source_section: 17 CFR 229.106(a)
    obligation_ids_using_term: [OBL-001, OBL-003]
  - term: information systems
    definition: Electronic information resources, owned or used by the registrant, including physical or virtual infrastructure controlled by such information resources, or components thereof, organised for the collection, processing, maintenance, use, sharing, dissemination, or disposition of the registrant's information to maintain or support the registrant's operations.
    source_section: 17 CFR 229.106(a)
    obligation_ids_using_term: [OBL-001, OBL-002, OBL-003]

transition_table:
  - stage: effective-date
    date: 2023-09-05
    applicable_obligation_ids: [OBL-001, OBL-002, OBL-003, OBL-004, OBL-005, OBL-006, OBL-007]
    description: Rule joins 17 CFR
  - stage: incident-disclosure compliance — non-SRC
    date: 2023-12-18
    applicable_obligation_ids: [OBL-001, OBL-002, OBL-006, OBL-007]
  - stage: incident-disclosure compliance — SRC
    date: 2024-06-15
    applicable_obligation_ids: [OBL-001, OBL-002, OBL-006, OBL-007]
  - stage: risk-management-and-strategy disclosure compliance
    date: 2023-12-15
    applicable_obligation_ids: [OBL-003, OBL-004, OBL-005, OBL-006]
    description: Annual reports for fiscal years ending on or after this date; SRC delay of one year for the disclosures.

open_extraction_questions:
  - obligation_ids: [OBL-001]
    question: What is the registrant's escalation path when the materiality determination is contested between security, legal, and finance? Resolution: governance overlay needed.
    section_reference: Form 8-K Item 1.05 instructions
    reviewer: legal
    blocker_for: obligation-mapping
  - obligation_ids: [OBL-007]
    question: Posture when the registrant believes a delay is warranted but the AG has not yet notified the SEC.
    section_reference: Form 8-K Item 1.05(c)
    reviewer: external-counsel
    blocker_for: obligation-mapping

handoff_targets: [obligation-mapping, policy-diff, implementation-plan]

confidence_label: medium
human_review_required: true
reviewer:
  role: regulatory-change lead
  review_status: pending

source_trace:
  - claim: Form 8-K Item 1.05 4-business-day clock starts at the materiality determination, not at incident discovery
    source: 88 FR 51896 at 51908
    section: Form 8-K Item 1.05(a) instructions
    date: 2023-07-26
    url: https://www.sec.gov/files/rules/final/2023/33-11216.pdf
  - claim: SRC compliance for incident disclosure delayed to 2024-06-15
    source: 88 FR 51896
    section: Compliance dates discussion
    date: 2023-07-26
```

## Reading the output

The extraction is the input to `risk-compliance-core/obligation-mapping`, which then overlays firm-side context: which named role at the registrant owns the materiality determination (typically a cyber-disclosure committee combining the CISO, general counsel, and disclosure controls owner); which evidence system carries the determination memo; whether the firm's existing 8-K materiality framework already accounts for cyber-incident reporting; how the 4-business-day clock interacts with the firm's pre-existing disclosure-controls-and-procedures cadence. None of that firm-side context is in this register; it lives in the next skill.

The extraction also feeds `policy-diff` (does the firm's existing cybersecurity policy or incident-response policy contain language consistent with the rule's defined terms and processes?) and `implementation-plan` (the transition table feeds the milestone build for the December 18 2023 and June 15 2024 compliance gates and the December 15 2023 annual-report compliance gate).

The two open questions in OBL-001 and OBL-007 are tracked for legal and outside-counsel resolution before downstream skills consume the register.
