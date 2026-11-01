# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## cfpb-1071-small-business-lending

### Example: CFPB Section 1071 small-business-lending data rule decomposed into atomic obligations

#### Input

The CFPB's final rule on Small Business Lending under the Equal Credit Opportunity Act (Regulation B), 88 FR 35150 (May 31 2023), codified at 12 CFR 1002.101 through 12 CFR 1002.114 (Subpart B of Regulation B), as **revised by the May 1, 2026 final rule**. Under the revised rule the threshold is a single 1,000-covered-transactions trigger; the rule is effective June 30, 2026 and the compliance date is January 1, 2028. The 2023 tiered compliance schedule (Tier 1 / 2 / 3 at 2,500 / 500 / 100 origination thresholds with staged dates of October 1 2024 / April 1 2025 / January 1 2026) is superseded.

A community bank's regulatory-change committee has the rule on the agenda. The bank originated 1,150 covered originations in each of 2024 and 2025; it crosses the revised 1,000 threshold and is a covered FI. The bank's compliance-and-fair-lending officer needs the atomic obligation list before the bank's lending-product team scopes data-collection workflow changes, before legal opens the question of how the firewall obligation interacts with the bank's existing two-loan-officer underwriting model, and before the data-and-analytics team scopes the FFIEC submission process.

#### Why this scenario matters

The 1071 rule is well-suited to demonstrate the atomic-obligation discipline because it combines a threshold-driven scope determination, a multi-element data-collection obligation (20+ data points per covered application), a firewall obligation with a notice-based exception, recordkeeping, reporting, and an effective-date / compliance-date pair that has shifted recently (the May 2026 revised final rule replaces the 2023 tiered schedule with a single 1,000-transaction threshold and a January 1, 2028 compliance date). Compressing the data-collection elements into a single "the bank must collect Section 1071 data" obligation loses the granularity needed for the bank's product team to scope the workflow changes; the rule actually decomposes into separate obligations for covered-FI determination, each data-point category, the firewall, the firewall-exception notice, recordkeeping, and reporting.

#### Output sketch

```yaml
extraction_id: RTOE-2026-CFPB-1071-01
as_of_date: 2026-05-06

source_citation:
  regulator: CFPB
  regulator_office: CFPB Office of Markets
  instrument_type: final-rule
  citation: 88 FR 35150; 12 CFR 1002.101 — 1002.114
  section_reference: 12 CFR Part 1002 Subpart B
  publication_date: 2023-05-31
  revised_publication_date: 2026-05-01  # §1071 revised final rule supersedes the 2023 tiered schedule
  effective_date: 2026-06-30
  compliance_dates:
    - date: 2028-01-01
      tier_or_topic: All covered FIs (single 1,000-covered-transactions threshold under the May 2026 revised final rule)
  transition_period: single compliance date under the May 2026 revised final rule (the 2023 Tier 1 / 2 / 3 schedule of October 1 2024 / April 1 2025 / January 1 2026 is superseded)
  url: https://www.consumerfinance.gov/rules-policy/final-rules/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b/

extraction_summary:
  obligation_count: 8
  by_section:
    - section_reference: 12 CFR 1002.105(b)
      obligation_count: 1
    - section_reference: 12 CFR 1002.107
      obligation_count: 3
    - section_reference: 12 CFR 1002.108
      obligation_count: 2
    - section_reference: 12 CFR 1002.111
      obligation_count: 1
    - section_reference: 12 CFR 1002.109
      obligation_count: 1

obligations:
  - obligation_id: OBL-001
    source_pin:
      section: 12 CFR 1002.105(b)
    action_verb: must determine
    party_obligated: financial institution (broadly defined to include depositories and non-depositories engaging in financial activity; see §1002.106 for the full definition)
    requirement_statement: Each financial institution must determine whether it is a covered financial institution by determining whether it originated at least 1,000 covered transactions in each of the two preceding calendar years (May 2026 revised final rule; supersedes the 2023 100-origination threshold).
    condition_or_trigger: each calendar year, looking back at the prior two calendar years
    deadline: prior to the start of each calendar year
    frequency: periodic
    action_type: governance
    evidence_expected:
      - covered-FI determination memo or worksheet retained per §1002.111
      - origination-volume data extract from loan-origination system
    cross_refs: [OBL-002, OBL-003, OBL-004, OBL-005, OBL-006, OBL-007, OBL-008]
    defined_terms_used: ["covered financial institution", "covered origination", "covered credit transaction"]
    confidence: high
    status: draft

  - obligation_id: OBL-002
    source_pin:
      section: 12 CFR 1002.107(a)(1) through (a)(17)
    action_verb: shall collect
    party_obligated: covered financial institution
    requirement_statement: The covered FI must collect, from each covered application, the loan- and applicant-level data points enumerated in §1002.107(a)(1) through (a)(17), including unique identifier, application date, application method, application recipient, credit type, credit purpose, amount applied for, amount approved or originated, action taken, action-taken date, denial reasons, pricing information, census tract, gross annual revenue, NAICS code, number of workers, time in business, and number of principal owners.
    condition_or_trigger: receipt of a covered application
    deadline: at the time of the application or in connection with the action taken on it; collected and reported per §1002.109
    frequency: on_event
    action_type: recordkeeping
    evidence_expected:
      - completed loan-application register entries
      - underwriting-system data extract per application
    cross_refs: [OBL-007, OBL-008]
    defined_terms_used: ["covered application", "covered credit transaction", "small business", "applicant"]
    confidence: high
    status: draft

  - obligation_id: OBL-003
    source_pin:
      section: 12 CFR 1002.107(a)(18) through (a)(20)
    action_verb: shall request
    party_obligated: covered financial institution
    requirement_statement: The covered FI must request, from each applicant, the demographic data on minority-owned-business status, women-owned-business status, LGBTQI+-owned-business status, and the principal owners' ethnicity, race, and sex (with multiple checkbox and free-text response options as enumerated).
    condition_or_trigger: receipt of a covered application
    deadline: at the time of the application
    exception: applicants are not required to provide the demographic data; the FI must request and accept any information provided or the applicant's choice not to provide it. The FI does not penalise applicants for not providing.
    frequency: on_event
    action_type: notice_or_disclosure
    evidence_expected:
      - demographic-data request and response capture in application system
      - applicant-disclosure language confirming the request was made
    cross_refs: [OBL-004, OBL-005, OBL-007, OBL-008]
    defined_terms_used: ["minority-owned business", "women-owned business", "LGBTQI+-owned business", "principal owner"]
    confidence: high
    status: draft

  - obligation_id: OBL-004
    source_pin:
      section: 12 CFR 1002.108(a)
    action_verb: shall maintain procedures
    party_obligated: covered financial institution
    requirement_statement: The covered FI must maintain procedures reasonably designed to limit the access by employees and officers involved in making any determination concerning a covered application to the demographic data collected under §1002.107(a)(18) through (a)(20), where feasible.
    condition_or_trigger: ongoing programme requirement
    deadline: in effect by the FI's tier-specific compliance date
    frequency: continuous
    action_type: governance
    evidence_expected:
      - written firewall procedures
      - access-control configuration in loan-origination system limiting demographic-data access by underwriter role
      - access-log monitoring and exception reporting
    cross_refs: [OBL-003, OBL-005]
    confidence: high
    status: draft

  - obligation_id: OBL-005
    source_pin:
      section: 12 CFR 1002.108(b)
    action_verb: shall provide notice
    party_obligated: covered financial institution
    requirement_statement: Where it is not feasible for the covered FI to limit access by employees and officers involved in making determinations concerning a covered application to the demographic data, the FI must provide a notice to the applicant that one or more such employees or officers may have access to the applicant's demographic data.
    condition_or_trigger: applicability of the firewall-exception condition (firewall not feasible)
    deadline: at or before the time the demographic-data request is made
    frequency: on_event
    action_type: notice_or_disclosure
    evidence_expected:
      - firewall-exception notice text in application form or workflow
      - record of feasibility determination
    cross_refs: [OBL-003, OBL-004]
    defined_terms_used: ["principal owner"]
    confidence: medium
    status: open-question
    open_questions:
      - For a community bank with a single loan officer who performs both intake and underwriting, is the firewall infeasible? What is the threshold of "feasibility" for purposes of §1002.108(a)? Resolution: legal and compliance review.

  - obligation_id: OBL-006
    source_pin:
      section: 12 CFR 1002.111
    action_verb: shall retain
    party_obligated: covered financial institution
    requirement_statement: The covered FI must retain evidence of compliance with Subpart B, including the small-business lending application register, for at least three years after the FI submits the data to the Bureau under §1002.109.
    condition_or_trigger: submission of the §1002.109 data
    deadline: three years from the date of submission
    frequency: continuous
    action_type: recordkeeping
    evidence_expected:
      - retained register and evidentiary records
      - records-management retention-policy entry
    cross_refs: [OBL-002, OBL-003, OBL-007]
    confidence: high
    status: draft

  - obligation_id: OBL-007
    source_pin:
      section: 12 CFR 1002.109
    action_verb: shall report
    party_obligated: covered financial institution
    requirement_statement: The covered FI must compile the §1002.107 data on covered applications and report the data to the Bureau by June 1 of each year covering the preceding calendar year, in the format prescribed by the Bureau.
    condition_or_trigger: each calendar year following the FI's tier-specific compliance date
    deadline: June 1 of each year, covering the prior calendar year
    frequency: periodic
    action_type: reporting
    evidence_expected:
      - submitted data file and submission confirmation
      - data-quality validation log
    cross_refs: [OBL-002, OBL-003, OBL-006]
    confidence: high
    status: draft

  - obligation_id: OBL-008
    source_pin:
      section: 12 CFR 1002.107(c) (small business definition by reference to SBA size standards)
    action_verb: shall determine
    party_obligated: covered financial institution
    requirement_statement: The covered FI must determine, for each application, whether the applicant is a small business as defined in §1002.106 (gross annual revenue not greater than $5 million for the preceding fiscal year, or as otherwise defined for the relevant industry per §1002.106).
    condition_or_trigger: receipt of an application that may be a covered application
    deadline: at the time of the application
    frequency: on_event
    action_type: governance
    evidence_expected:
      - small-business determination logic in application workflow
      - data-element capture supporting the determination
    cross_refs: [OBL-002]
    defined_terms_used: ["small business", "gross annual revenue"]
    confidence: high
    status: draft

cross_references:
  - from_obligation_id: OBL-001
    to_obligation_id: OBL-002
    relationship: phases_into
    notes: Covered-FI determination triggers all downstream collection and reporting obligations.
  - from_obligation_id: OBL-002
    to_obligation_id: OBL-006
    relationship: produces_record_for
  - from_obligation_id: OBL-003
    to_obligation_id: OBL-004
    relationship: governs
    notes: Firewall procedures govern access to the demographic data collected under OBL-003.
  - from_obligation_id: OBL-005
    to_obligation_id: OBL-004
    relationship: is_exception_to
    notes: §1002.108(b) is the notice-based exception when the §1002.108(a) firewall is not feasible.
  - from_obligation_id: OBL-002
    to_obligation_id: OBL-007
    relationship: reports_outcome_of
  - from_obligation_id: OBL-003
    to_obligation_id: OBL-007
    relationship: reports_outcome_of

defined_terms:
  - term: covered financial institution
    definition: A financial institution that originated at least 1,000 covered transactions in each of the two preceding calendar years (under the May 2026 revised final rule; supersedes the 2023 100-origination threshold).
    source_section: 12 CFR 1002.105(b)
    obligation_ids_using_term: [OBL-001, OBL-002, OBL-003, OBL-004, OBL-005, OBL-006, OBL-007, OBL-008]
  - term: covered application
    definition: An oral or written request for a covered credit transaction that is made in accordance with procedures used by a financial institution for the type of credit requested.
    source_section: 12 CFR 1002.103
    obligation_ids_using_term: [OBL-002, OBL-003, OBL-004, OBL-005, OBL-008]
  - term: covered credit transaction
    definition: An extension of business credit (with enumerated exclusions, including HMDA-reportable transactions, leases, consumer-designated credit used for business purposes per certain conditions, factoring, and others under §1002.104).
    source_section: 12 CFR 1002.104
    obligation_ids_using_term: [OBL-001, OBL-002]
  - term: small business
    definition: A business that meets the size standards under §1002.106 (gross annual revenue not greater than $5 million for the preceding fiscal year; alternative size standards for certain industries).
    source_section: 12 CFR 1002.106
    obligation_ids_using_term: [OBL-002, OBL-008]
  - term: minority-owned business
    definition: A business that is more than 50% owned by minority individuals (as enumerated by ethnicity and race categories).
    source_section: 12 CFR 1002.102
    obligation_ids_using_term: [OBL-003]
  - term: women-owned business
    definition: A business that is more than 50% owned by women.
    source_section: 12 CFR 1002.102
    obligation_ids_using_term: [OBL-003]
  - term: LGBTQI+-owned business
    definition: A business that is more than 50% owned by individuals who identify as lesbian, gay, bisexual, transgender, queer or questioning, or intersex.
    source_section: 12 CFR 1002.102
    obligation_ids_using_term: [OBL-003]

transition_table:
  - stage: effective-date
    date: 2023-08-29
    applicable_obligation_ids: [OBL-001]
    description: Rule joins 12 CFR; covered-FI determination obligation begins for the look-back assessment.
  - stage: rule effective date (May 2026 revised final rule)
    date: 2026-06-30
    applicable_obligation_ids: [OBL-001]
    description: §1071 revised final rule effective; covered-FI determination obligation begins to run.
  - stage: compliance date (May 2026 revised final rule)
    date: 2028-01-01
    applicable_obligation_ids: [OBL-002, OBL-003, OBL-004, OBL-005, OBL-006, OBL-007, OBL-008]
    description: Single compliance date under the May 2026 revised final rule; supersedes the 2023 Tier 1 / 2 / 3 schedule.

open_extraction_questions:
  - obligation_ids: [OBL-005]
    question: Feasibility threshold for §1002.108(a) firewall when a single loan officer performs both intake and underwriting at a small community bank.
    section_reference: 12 CFR 1002.108
    reviewer: legal
    blocker_for: obligation-mapping
  - obligation_ids: [OBL-001, OBL-002, OBL-003, OBL-004, OBL-005, OBL-006, OBL-007, OBL-008]
    question: Confirm the May 1, 2026 revised final rule text against the published Federal Register version, including the single 1,000-transaction threshold and the June 30 2026 / January 1 2028 effective and compliance dates.
    section_reference: §1071 revised final rule (May 2026); §1002.105 (revised); §1002.114 (revised)
    reviewer: regulatory-change-lead
    blocker_for: implementation-plan

handoff_targets: [obligation-mapping, policy-diff, implementation-plan]

confidence_label: medium
human_review_required: true
reviewer:
  role: regulatory-change lead
  review_status: pending

source_trace:
  - claim: Covered-FI threshold is 1,000 covered transactions in each of the two preceding calendar years (May 2026 revised final rule; supersedes the 2023 100-origination threshold)
    source: §1071 revised final rule (May 1, 2026)
    section: 12 CFR 1002.105(b) (revised)
    date: 2026-05-01
    url: https://www.consumerfinance.gov/rules-policy/final-rules/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b/
  - claim: Demographic-data request must be made; applicant is not required to provide
    source: 88 FR 35150
    section: 12 CFR 1002.107(a)(18) through (a)(20)
    date: 2023-05-31
  - claim: Submission to the Bureau by June 1 each year covering prior calendar year
    source: 88 FR 35150
    section: 12 CFR 1002.109
    date: 2023-05-31
```

#### Reading the output

The extraction is the input to `obligation-mapping`, which then overlays firm-side context: which named role at the bank owns covered-FI determination (typically the compliance officer with input from finance for origination-volume data); which loan-origination system carries the §1002.107(a) data points and how the demographic data fields will be added; which firewall procedure the bank will adopt and whether it will rely on the §1002.108(b) notice exception; the FFIEC-submission workflow; record-retention configuration. None of that firm-side context is in this register.

The extraction also feeds `policy-diff` (does the bank's existing fair-lending policy and small-business-lending policy reference the §1002.107 data points?) and `implementation-plan` (the transition table feeds the milestone build for the bank's tier-3 January 2026 compliance gate, with adjustment for the post-litigation dates as confirmed in the open-question resolution).

The two open questions in OBL-005 and the post-litigation date confirmation are tracked for legal and regulatory-change-lead resolution before downstream skills consume the register.

## sec-cyber-disclosure-final-rule

### Example: SEC cybersecurity disclosure final rule decomposed into atomic obligations

#### Input

The SEC's final rule on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure, 88 FR 51896 (July 26 2023), codified at 17 CFR 229.106 (Reg S-K Item 106), 17 CFR 232.405 (inline XBRL), 17 CFR 240.13a-11 and 17 CFR 240.15d-11 (Form 8-K coverage), and 17 CFR 249.308 (Form 8-K Item 1.05). Effective date September 5 2023. Compliance dates: incident-disclosure compliance December 18 2023 for non-smaller reporting companies; June 15 2024 for smaller reporting companies. Risk-management-and-strategy compliance with annual reports for fiscal years ending on or after December 15 2023; SRC delay of one year for those disclosures.

The regulatory-change committee at a public-company registrant has the rule on the agenda. The change lead needs the atomic obligation list before the committee meets, before the firm's existing 8-K materiality framework is updated, before the firm's 10-K disclosure controls run their next quarterly review, and before legal opens the question of how to handle the Attorney-General-national-security delay. This is the canonical net-new-rule extraction case for this skill.

#### Why this scenario matters

The SEC cyber rule is well-suited to demonstrate the atomic-obligation discipline because the rule combines event-driven disclosure (the 4-business-day Form 8-K Item 1.05 obligation) with annual disclosure (the Reg S-K Item 106 disclosures), each with their own conditions, frequencies, exceptions, and evidence shapes. Compressing the event-driven and annual obligations into a single "the firm must comply with the SEC cyber rule" obligation is the most common defect; the rule actually decomposes into at least seven atomic obligations across the operative sections.

#### Output sketch

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

#### Reading the output

The extraction is the input to `obligation-mapping`, which then overlays firm-side context: which named role at the registrant owns the materiality determination (typically a cyber-disclosure committee combining the CISO, general counsel, and disclosure controls owner); which evidence system carries the determination memo; whether the firm's existing 8-K materiality framework already accounts for cyber-incident reporting; how the 4-business-day clock interacts with the firm's pre-existing disclosure-controls-and-procedures cadence. None of that firm-side context is in this register; it lives in the next skill.

The extraction also feeds `policy-diff` (does the firm's existing cybersecurity policy or incident-response policy contain language consistent with the rule's defined terms and processes?) and `implementation-plan` (the transition table feeds the milestone build for the December 18 2023 and June 15 2024 compliance gates and the December 15 2023 annual-report compliance gate).

The two open questions in OBL-001 and OBL-007 are tracked for legal and outside-counsel resolution before downstream skills consume the register.

## troubleshooting

### Troubleshooting: rule-to-obligation-extraction

The extraction skill produces the atomic obligation list a discrete piece of net-new regulatory rule text imposes. The recurring defects below cause the register to lose substance, lose portability across firms, or lose alignment with the downstream `obligation-mapping` skill that consumes it.

#### 1. Compressing multiple obligations into one row

**Symptom**: A paragraph that says "the institution shall (i) document, (ii) test annually, and (iii) report to the board" lands in the register as one row that reads "the institution must document, test, and report annually." Downstream `obligation-mapping` cannot cleanly assign the three sub-obligations to three different owners with three different evidence shapes.

**Why it happens**: The extraction reads the paragraph as a single sentence and produces a single row. The paragraph is structurally three obligations that share a subject and a frame, not one obligation.

**Resolution**:
- Apply the atomic-obligation discipline: each enumerated sub-clause ((i), (ii), (iii); a, b, c; first, second, third) is potentially its own row. Whether to split is determined by whether the actor, frequency, action_type, or evidence shape differ.
- The default presumption is split. Combining is a deliberate decision, not a default.
- The downstream test: can `obligation-mapping` assign each row to a single owner and a single evidence shape? If not, split further.
- The defined-terms section is one place this defect hides: a row that invokes three defined terms with different scopes is often three rows in disguise.

#### 2. Extracting from preamble or commentary as if it were operative text

**Symptom**: The register includes obligations drawn from the SEC adopting-release preamble that do not appear in the codified 17 CFR section. Downstream legal review pushes back on the row because the codified section does not say what the row claims.

**Why it happens**: The preamble feels load-bearing because it is interpretive and the agency uses preamble to explain what it intends the rule to require. Practitioners read the preamble as if it were the rule.

**Resolution**:
- Pin obligations to operative text: the codified CFR section for Federal Register rules; the binding article for EU regulations; the `R` paragraph for FCA Handbook rules; the operative provision for supervisory letters. Preamble or commentary is interpretive context that may inform the row but does not create the obligation.
- Use the `source_pin.preamble_context` field to capture preamble framing that changes how the operative section reads. Do not promote a preamble-only obligation to a freestanding row.
- For an EU regulation, recitals are interpretive. Article text is binding. Pin to the article.
- For an SEC adopting release, the preamble is interpretive. The closing regulatory-text amendments are what codifies. Pin to the codified section.
- For a supervisory letter (OCC bulletin, SR letter, FIL, CFPB circular), the entire instrument is interpretive supervisory guidance, not a codified rule. The pin is the section inside the instrument, and the confidence label reflects that the instrument is supervisory rather than rule-of-law.

#### 3. Missing a defined term that changes scope

**Symptom**: Two extractions of the same rule by two practitioners produce different obligation lists because one captured the rule's defined term ("covered institution," "material," "senior management," "covered application," "ICT third-party service provider") and the other did not. The downstream firm-side mapping is non-portable.

**Why it happens**: Defined terms are easy to miss when the rule body uses the term as if it were ordinary English. The rule's definitions section is the only authoritative source for scope.

**Resolution**:
- Capture every defined term the body invokes in the top-level `defined_terms` section, with the rule's text of definition and the section pin where the term is defined.
- Each obligation row's `defined_terms_used` column lists the terms the row depends on.
- When a term has different definitions across rules (e.g., "cybersecurity event" in NYDFS Part 500 versus "covered cybersecurity incident" in SEC Item 1.05), the extraction captures both definitions with their pins and flags the cross-rule confusion in the open-extraction-questions section.
- Where a state has adopted a NAIC model law with material amendments to the definitions section, capture both the NAIC model definition and the state-adopted version, and pin to the state-adopted version.

#### 4. Skipping the transition and phase-in language

**Symptom**: The register has a single effective date and no transition table. The downstream `implementation-plan` skill cannot sequence remediation milestones because the register doesn't capture which obligations apply when.

**Why it happens**: Effective dates feel simpler than they are. A rule with tier-by-tier compliance dates plus a deferred-effective-date provision plus a sunset clause is a different rule in month 1 than in month 25, but the register treats it as one frozen state.

**Resolution**:
- Capture every staged date in the `transition_table` array. One row per stage.
- Distinguish effective date (rule joins the CFR or OJ) from compliance date (regulated party must comply). They are typically different.
- For tier-by-tier compliance (1071, DORA, CSRD), each tier is a row in the transition table; the obligations applicable in each tier go in the `applicable_obligation_ids` column.
- For phased compliance within a single tier (e.g., assurance requirements phased in for the SEC climate rule), each phase is a row.
- Where a rule has been the subject of post-publication litigation that has stayed or modified the effective dates, capture the dates as of the extraction date and flag the litigation status in the open-extraction-questions section.

#### 5. Mixing extraction with firm-side mapping

**Symptom**: Rows in the register name firm-specific control owners (e.g., "Head of TPRM at the bank"; "Compliance Officer for the credit-card line"), firm-specific evidence systems ("captured in the bank's GRC platform"; "evidenced in JIRA ticket"), or firm-specific policy text ("the bank's existing CDD policy already requires ..."). Downstream `obligation-mapping` cannot cleanly overlay firm context because the register is already half-firm-specific.

**Why it happens**: The practitioner is familiar with the firm and reaches for firm-specific labels by reflex. The extraction collapses into a firm-side mapping.

**Resolution**:
- The skill produces a firm-agnostic register. The actor is whoever the rule names (board; senior management; CISO; covered institution; ICT third-party service provider). The evidence shape is shape, not system (board minute; attestation; log; periodic report; not "captured in GRC platform"). The owner is the regulator-defined party, not a firm-side role.
- If the firm-side mapping is needed, the skill is `obligation-mapping`, not this one. The two chain.
- Where the scope record has firm context, this skill ignores it for register content; firm context is consumed by `obligation-mapping`.
- Run the portability test: would the register read the same for a different firm of the same type? If not, the register is over-specified.

#### 6. Confidence label that hides the defects

**Symptom**: The register carries a single overall confidence of "high" while several rows are pinned to `[verify section]` or carry interpretive readings of preamble. Downstream legal review pushes back because the register's confidence label does not reflect the rows.

**Why it happens**: Practitioners are reluctant to label a register low-confidence because it implies the work is incomplete; the overall label aggregates away the per-row variability.

**Resolution**:
- Confidence is per-row: high where the operative text is unambiguous; medium where interpretation is involved; low where reading between the lines or relying on preamble alone.
- The overall `confidence_label` is `mixed` when rows vary; do not collapse to a single label that hides the variability.
- Each `[verify section]` row is automatically not-high; use medium where the section is genuinely uncertain and the practitioner has read the surrounding text, or low where the section is fabricated or guessed.
- The reviewer reads the per-row confidence first. Hiding low-confidence rows under a high-overall label fails the next read.

#### 7. Treating supervisory letters as if they were rules

**Symptom**: The register pins obligations to OCC Bulletin 2013-29, SR 11-7, or a CFPB circular and labels them with the same confidence as obligations pinned to a Federal Register final rule. Downstream legal review notes that the bulletin is interpretive supervisory guidance, not a rule of law.

**Why it happens**: Supervisory letters operate as if they were rules in practice (examiners apply them; firms comply). The legal status (interpretive supervisory guidance) is different from the operational status (binding for examination purposes).

**Resolution**:
- Use the `instrument_type` enum precisely: `final-rule` for codified rules; `supervisory-letter`, `bulletin`, `circular`, `fil`, `letter-to-credit-unions`, `industry-letter`, `interagency-statement`, `advisory` for the various supervisory instruments.
- Confidence label: high for clearly stated supervisory expectations even where the instrument is interpretive; the operational status is what matters for the firm's compliance posture, but the legal status influences how the firm frames its response if the supervisory expectation is contested.
- For an interagency statement (FFIEC, three-agency banking statement), pin to the statement and note that it carries the joint position of the named agencies.
- For a CFPB circular, pin to the circular and the underlying statute the circular interprets.

#### 8. Treating consent-order articles as the operative source

**Symptom**: A firm not named in a consent order extracts the order's articles into its own register and treats the articles as obligations the firm must satisfy. Downstream legal review notes that the firm has no contractual or statutory obligation to satisfy the articles; the articles bind only the named defendant.

**Why it happens**: Public consent orders are useful supervisory signals. A non-defendant firm with similar exposure may treat the articles as obligations the firm should satisfy as a posture decision. The extraction blurs "should satisfy as posture" with "must satisfy as legal obligation."

**Resolution**:
- Use `instrument_type: consent-order-as-obligation-source` to mark the source as a consent order whose articles are extracted for posture, not because the firm is the named defendant.
- The register's source-trace and the open-extraction-questions section flag that the firm is not the named defendant; the obligations are extracted as posture and require firm-management decision on adoption.
- Confidence labels run lower for consent-order-derived rows (medium at best for non-defendants).
- Where the firm later becomes subject to a similar enforcement matter, the register's posture-derived rows are upgraded to obligations under the firm's own order.

#### 9. Stopping at the rule and missing the implementing technical standards

**Symptom**: Extraction of an EU regulation captures the article-level obligations but misses the implementing or regulatory technical standards (RTS / ITS) adopted as Commission Delegated Regulations. Downstream implementation work surfaces the missing detail late.

**Why it happens**: EU regulations frequently delegate operational detail to RTS and ITS issued by ESMA, EBA, or EIOPA and adopted as Commission Delegated Regulations. The regulation cites the delegation; the practitioner reads the regulation but not the delegated regulation.

**Resolution**:
- For EU regulations, list the cross-referenced RTS and ITS in the source list and extract obligations from the delegated regulations as separate registers (one extraction per Commission Delegated Regulation).
- The rule's article text is the binding obligation; the RTS / ITS provide operational detail. The extraction may pin some obligations to the regulation article and others to the RTS, depending on which carries the operative requirement.
- For DORA specifically, there are multiple RTS and ITS (e.g., RTS on the policy on the use of ICT services supporting critical or important functions; RTS on subcontracting of ICT services supporting critical or important functions; ITS on the templates for incident reporting). Extraction should capture each as a separate source.

#### 10. Not flagging litigation or revision risk

**Symptom**: A rule that has been the subject of post-publication litigation (vacated; stayed; remanded for further proceedings) lands in the register as if the rule were operative as published. Downstream implementation-plan work proceeds on stale dates.

**Why it happens**: Practitioners extract from the rule as published and do not check operational status at extraction time. The register lacks an operational-status flag.

**Resolution**:
- At extraction time, check the operational status: is the rule effective? Has any provision been stayed or vacated? Are compliance dates as published, or have they been adjusted?
- The `source_citation.compliance_dates` array captures the dates in effect at the extraction date, with notes on the post-publication adjustment history.
- The open-extraction-questions section flags any provision under live litigation or under regulator-announced amendment.
- Confidence labels on rows that depend on the litigated provision run lower.
- Re-extract on material change: if the rule is amended or the litigation resolves, the register is re-emitted with a revision-log entry.

#### 11. Engagement-scope record stale or missing

**Symptom**: The extraction was drafted from yesterday's understanding of the engagement; today the regulator has issued an interim final rule that supersedes the source under extraction, or the firm has changed its sector posture in a way that changes the overlay set. The register no longer matches the engagement.

**Why it happens**: The scope record was treated as a kickoff artifact rather than a living record. The extraction consumed an old version.

**Resolution**:
- Engagement-scope is a status, not a fixed truth. Re-emit the scope record after any material change; re-emit the extraction consuming the updated scope.
- Where the extraction is run without an scope record at all, ask the four questions (regulator and instrument; publication / effective / compliance dates; source posture; firm boundary) and default to public-only posture if the practitioner declines. Note in the register that scope was not formalised.

#### 12. Boundary with `obligation-mapping` not respected

**Symptom**: The extraction register and the firm-side obligation register (produced by `obligation-mapping`) duplicate substantive content. Subtle inconsistencies appear at the row level: this register names the rule's actor as "covered institution"; the firm-side register names the actor as "the bank's BSA officer." Downstream consumers cannot tell which is operative.

**Why it happens**: The boundary between extraction and mapping was not respected; both skills produced overlapping content for the same row.

**Resolution**:
- The two skills chain; they do not duplicate. Extraction produces the regulator-side, firm-agnostic obligation list. Mapping overlays firm-side context on top.
- The shared key is `obligation_id`. The mapping skill's register references the extraction's `obligation_id` and adds firm-side columns (named owner; firm-side control objective; named evidence system; firm policy reference; risk taxonomy tag; review-gate posture). It does not restate the extraction's regulator-side columns.
- Where the firm-side register and the extraction register diverge on the regulator-side columns (actor name; requirement statement; deadline; exception; defined-term scope), the extraction register is operative; the mapping register has drifted and needs revision.
- The schema contract (the cross-skill `obligation_id` plus the extraction's regulator-side columns) is additive. Breaking changes to the schema ship as a versioned migration with downstream skills told in advance.
