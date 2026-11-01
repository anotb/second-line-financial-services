# Example: CFPB Section 1071 small-business-lending data rule decomposed into atomic obligations

## Input

The CFPB's final rule on Small Business Lending under the Equal Credit Opportunity Act (Regulation B), 88 FR 35150 (May 31 2023), codified at 12 CFR 1002.101 through 12 CFR 1002.114 (Subpart B of Regulation B), as **revised by the May 1, 2026 final rule**. Under the revised rule the threshold is a single 1,000-covered-transactions trigger; the rule is effective June 30, 2026 and the compliance date is January 1, 2028. The 2023 tiered compliance schedule (Tier 1 / 2 / 3 at 2,500 / 500 / 100 origination thresholds with staged dates of October 1 2024 / April 1 2025 / January 1 2026) is superseded.

A community bank's regulatory-change committee has the rule on the agenda. The bank originated 1,150 covered originations in each of 2024 and 2025; it crosses the revised 1,000 threshold and is a covered FI. The bank's compliance-and-fair-lending officer needs the atomic obligation list before the bank's lending-product team scopes data-collection workflow changes, before legal opens the question of how the firewall obligation interacts with the bank's existing two-loan-officer underwriting model, and before the data-and-analytics team scopes the FFIEC submission process.

## Why this scenario matters

The 1071 rule is well-suited to demonstrate the atomic-obligation discipline because it combines a threshold-driven scope determination, a multi-element data-collection obligation (20+ data points per covered application), a firewall obligation with a notice-based exception, recordkeeping, reporting, and an effective-date / compliance-date pair that has shifted recently (the May 2026 revised final rule replaces the 2023 tiered schedule with a single 1,000-transaction threshold and a January 1, 2028 compliance date). Compressing the data-collection elements into a single "the bank must collect Section 1071 data" obligation loses the granularity needed for the bank's product team to scope the workflow changes; the rule actually decomposes into separate obligations for covered-FI determination, each data-point category, the firewall, the firewall-exception notice, recordkeeping, and reporting.

## Output sketch

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

## Reading the output

The extraction is the input to `obligation-mapping`, which then overlays firm-side context: which named role at the bank owns covered-FI determination (typically the compliance officer with input from finance for origination-volume data); which loan-origination system carries the §1002.107(a) data points and how the demographic data fields will be added; which firewall procedure the bank will adopt and whether it will rely on the §1002.108(b) notice exception; the FFIEC-submission workflow; record-retention configuration. None of that firm-side context is in this register.

The extraction also feeds `policy-diff` (does the bank's existing fair-lending policy and small-business-lending policy reference the §1002.107 data points?) and `implementation-plan` (the transition table feeds the milestone build for the bank's tier-3 January 2026 compliance gate, with adjustment for the post-litigation dates as confirmed in the open-question resolution).

The two open questions in OBL-005 and the post-litigation date confirmation are tracked for legal and regulatory-change-lead resolution before downstream skills consume the register.
