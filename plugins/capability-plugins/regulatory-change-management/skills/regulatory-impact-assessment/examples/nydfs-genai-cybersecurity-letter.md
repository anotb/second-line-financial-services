# Example: NYDFS October 2024 Industry Letter on cybersecurity risks arising from GenAI — state-chartered bank using GenAI for customer service

## Input

A state-chartered bank ($8B in assets, NYDFS-supervised state-licensed bank with NY headquarters and FDIC insurance) has deployed a GenAI customer-service assistant for retail customers (FAQ answering, account-balance lookup with authentication, lending-product information) on a third-party LLM platform with a sponsor-tenant agreement. The bank's CISO flags the NYDFS Industry Letter [verify date and section]; the head of regulatory affairs commissions the impact assessment. Engagement scope is supplied: institution = state-chartered bank, primary regulators = NYDFS and FDIC, persona = head of regulatory affairs and CISO, source posture = public-plus-firm-policy, sector overlay = banking, cross-cutting overlays = cyber and AI-governance. Time pressure: 7-day read for the operational-risk-committee; finalised assessment by 14 days.

## Why this scenario matters

This is the canonical impact-assessment use of the skill on an NYDFS Industry Letter: the Industry Letter is interpretive of an existing regulation (Part 500), so the implementation lens reads against existing covered-entity-scope obligations rather than a brand-new rule. The cross-cutting overlay set (cyber + AI-governance) is operative; loading only the cyber overlay misses the AI-governance specifics that the Industry Letter brings (third-party LLM platform risk, prompt-injection control, data-leakage control). The strategy lens is rich on examiner-posture-shift signal: NYDFS Industry Letters historically signal cross-state convention, and other state regulators (Connecticut, California) have followed NYDFS's posture on cyber-and-AI topics. The bank also has an FDIC overlay to consider; FDIC has not issued a parallel Industry Letter, but the bank's FDIC examination cycle will read against any cyber posture shift.

## Output sketch

```yaml
assessment_id: RIA-2026-NYDFS-GENAI-CYB-02
engagement_id: ENG-2026-RCM-NYDFS-GENAI
as_of_date: 2026-05-06

decision_required: ingest the Industry Letter into the regulatory-change inventory; commission policy-diff against the information-security policy and the AI-use-case-intake policy; refresh the AI-use-case-intake review for the GenAI customer-service assistant; trigger third-party LLM platform evidence-pack refresh.
recommended_posture: implementation lens — the bank's existing Part 500 cybersecurity programme covers most of the Industry Letter's interpretive ground; targeted refresh on prompt-injection control, data-leakage control, and AI-use-case-intake review is operative; strategy lens — neutral with operational concerns, NYDFS engagement through trade-association channels, no firm-direct comment because the Industry Letter is interpretive.

source_citation:
  regulator: NYDFS
  regulator_office: NYDFS Cybersecurity Division
  instrument_type: industry-letter
  citation: NYDFS Industry Letter on Cybersecurity Risks Arising from GenAI [verify date and section]
  publication_date: October 2024 [verify exact date]
  url: https://www.dfs.ny.gov/industry_guidance/[verify]
  related_instruments:
    - NYDFS 23 NYCRR Part 500
    - NYDFS Insurance Circular Letter on the use of external consumer data and information sources in underwriting [verify date]
    - NYDFS prior cyber Industry Letters on third-party risk and on penetration testing [verify dates]

in_scope: true
in_scope_rationale: |
  The bank is NYDFS-supervised under Part 500 (covered entity by virtue of NYDFS state-banking license). The bank uses GenAI in customer-service operations through a third-party LLM platform; the Industry Letter applies to NYDFS-supervised covered entities deploying or contemplating GenAI.

scope:
  institution_types: [state-chartered bank]
  affected_business_units: [head of consumer banking, CISO, head of customer service operations, head of model risk, head of vendor management]
  affected_products: [retail consumer-banking customer-service channel]
  affected_geographies: [New York; the firm's NY-licensed footprint]
  thresholds_named:
    - threshold_text: NYDFS covered-entity scope under 23 NYCRR §500.1(c)
      firm_read: in scope (state-chartered bank with NY license)
      source: 23 NYCRR §500.1(c) [verify subsection]

effective_date_posture:
  mandatory_compliance_date: n/a — interpretive Industry Letter; underlying Part 500 obligations apply now
  transition_period: n/a; the letter sets supervisory expectations, not new rule provisions
  sunset_or_contingency: NYDFS may issue subsequent Industry Letters or amendments to Part 500 that supersede or extend the October 2024 posture
  early_adoption_posture: not applicable; the bank's existing Part 500 compliance posture covers most of the interpretive ground

affected_obligation_domains:
  - cyber
  - AI-governance
  - third-party-risk
  - operational-resilience
  - data-management

policy_impact:
  - policy_area: information security policy
    expected_change_type: amendment
    rationale: add a section on AI-system cybersecurity, including prompt-injection control, data-leakage control, model-supply-chain risk, and access-segregation for AI platforms
  - policy_area: AI-use-case-intake policy
    expected_change_type: amendment
    rationale: tighten the policy's section on customer-facing use cases, third-party LLM platform deployment, and data-handling expectations
  - policy_area: third-party risk management policy
    expected_change_type: cross-reference-update
    rationale: cross-reference NYDFS §500.11 third-party SP security policy to the AI-system-cyber-risk programme
  - policy_area: information-classification policy
    expected_change_type: procedure-refresh
    rationale: refresh the procedure to cover non-public-information handling in GenAI prompts and responses; specify which information categories are permissible for AI-platform-handling

control_impact:
  - control_objective: GenAI customer-service assistant operates without disclosing non-public-information beyond authenticated session boundaries
    expected_change_type: new-control-objective
    anticipated_evidence_gap: data-leakage control documentation, output-filtering testing, data-classification-tag enforcement
  - control_objective: prompt-injection attempts on the GenAI customer-service assistant are detected and blocked
    expected_change_type: new-control-objective
    anticipated_evidence_gap: prompt-injection testing methodology, red-team exercise documentation, detection-control coverage
  - control_objective: third-party LLM platform meets the bank's cybersecurity-control expectations
    expected_change_type: existing-control-objective-rescoped
    anticipated_evidence_gap: vendor evidence pack covering platform-cyber-controls, model-supply-chain risk, training-data handling, output-filtering, prompt-injection-detection
  - control_objective: AI-use-case-intake covers cybersecurity risk assessment and information-classification review before deployment
    expected_change_type: existing-control-objective-rescoped
    anticipated_evidence_gap: intake-review documentation for the deployed GenAI customer-service assistant; periodic re-review

reporting_impact:
  - report_or_disclosure: CISO board reporting under §500.4(b) and §500.16
    change_type: existing-report-amended
  - report_or_disclosure: Section 500.17 cybersecurity-event notification
    change_type: existing-report-amended

technology_data_impact:
  - system_or_data_area: third-party LLM platform (sponsor-tenant deployment)
    implication: implement prompt-injection-detection control; implement output-filtering control; segregate authenticated-customer-session boundaries; instrument the platform for cybersecurity-event detection feeding the bank's incident-response process
  - system_or_data_area: customer-authentication platform
    implication: confirm authentication boundary integrity for AI-assistant interactions; ensure that authentication tokens or non-public-information cannot leak into the LLM platform's logging or training-data feedback loops
    new_data_field: AI-platform-interaction audit-trail field on the customer-session record
  - system_or_data_area: customer-service knowledge-base
    implication: classify knowledge-base content for permissible AI-platform-handling; instrument retrieval-augmented-generation pipeline data-handling

third_party_impact:
  - arrangement_type: model-vendor
    expected_change_type: evidence-pack-refresh
    rationale: refresh the third-party LLM platform vendor evidence pack to cover the Industry Letter's enumerated cyber-and-AI control expectations; if the vendor's evidence is insufficient, trigger right-to-audit
  - arrangement_type: cloud-infrastructure
    expected_change_type: contract-amendment
    rationale: where the LLM platform operates on cloud infrastructure under a separate contract, ensure the contract's cybersecurity flow-down covers the AI-system-cyber risk

customer_impact:
  - change_area: communication
    implication: customers may experience tighter response boundaries from the GenAI assistant (the assistant declines to handle topics outside the AI-use-case-intake scope, refers to a human agent more frequently); customers benefit from improved cyber posture

cost_to_comply:
  implementation_one_time:
    indicative_range: $500K to $1.5M one-time
    basis: similar-prior-project benchmark (the bank's prior third-party-cloud-platform onboarding); vendor-quote range for prompt-injection-detection and output-filtering controls; internal-build estimate for AI-use-case-intake refresh
    confidence: medium
  ongoing_run_rate:
    indicative_range: $150K to $400K annual
    basis: ongoing testing, monitoring, third-party evidence-pack refresh, board reporting cadence
    confidence: medium
  cost_drivers:
    - prompt-injection-detection and output-filtering control build
    - third-party LLM platform vendor evidence-pack refresh (incl. right-to-audit if invoked)
    - AI-use-case-intake review refresh
    - information-classification policy refresh and training
    - red-team exercise covering AI platform
    - CISO board reporting cadence refresh
  agency_estimate_reference:
    agency_estimate_summary: NYDFS does not publish a cost estimate for Industry Letters; the underlying Part 500 framework predates the GenAI-specific interpretive guidance
    firm_divergence_note: bottom-up firm estimate from build-out and vendor refresh
    source_pin: NYDFS Industry Letter [verify]; firm's prior third-party-cloud-onboarding project record

regulatory_strategy:
  firm_position: neutral-with-operational-concerns
  regulator_engagement_posture:
    - industry-association-comment-letter
    - ongoing-supervisory-dialogue
  comment_period_posture:
    owner_role: n/a — interpretive Industry Letter, no comment period
    draft_pathway: n/a
  public_consultation_posture: none
  peer_industry_alignment: industry consensus is that the Industry Letter is broadly consistent with the existing Part 500 framework and signals NYDFS examiner posture rather than introducing new obligations; trade-association engagement (NY Bankers Association and BPI cyber working groups) supports clarifying-question dialogue with NYDFS on prompt-injection-detection and output-filtering control expectations
  industry_associations_engaged:
    - NY Bankers Association cyber and AI committee
    - BPI BITS cyber working group
    - FS-ISAC AI-and-cyber working group
  escalation_triggers:
    - trigger: data-leakage event in the GenAI customer-service assistant before remediation lands
      escalation_level: CRO
    - trigger: NYDFS examiner request for AI-use-case inventory and AI-system-cybersecurity-control evidence in the next examination cycle
      escalation_level: general-counsel
    - trigger: cost-to-comply over $1M one-time
      escalation_level: executive-committee

open_questions:
  - question: whether the existing third-party LLM platform vendor's SOC 2 Type 2 with carve-out covers the Industry Letter's enumerated AI-system-cyber controls or whether a supplemental attestation is required
    owner_role: TPRM
    blocker_for: implementation-plan-sequencing
    due_date: 2026-05-13
  - question: whether the Industry Letter's posture extends to internal-only AI use cases (e.g., the bank's AI-assisted code-review tool, the AI-assisted drafting tool used in operations) or only to customer-facing or non-public-information-handling use cases
    owner_role: legal
    blocker_for: rule-to-obligation-extraction-kickoff
    due_date: 2026-05-13
  - question: whether the bank's existing red-team exercise scope captures prompt-injection testing or whether a supplemental red-team is required
    owner_role: CISO
    blocker_for: implementation-plan-sequencing
    due_date: 2026-05-20

recommended_next_steps:
  - next_step: kick off rule-to-obligation-extraction on the Industry Letter's enumerated cyber-and-AI control expectations
    owner_role: head of regulatory change
    target_date: 2026-05-13
  - next_step: run policy-diff against the information-security policy, the AI-use-case-intake policy, and the third-party risk management policy
    owner_role: head of policy and standards
    target_date: 2026-05-20
  - next_step: trigger third-party LLM platform vendor evidence-pack refresh and right-to-audit if needed
    owner_role: head of vendor management
    target_date: 2026-05-27
  - next_step: refine cost-to-comply with finance partner; confirm one-time and run-rate ranges
    owner_role: finance business partner for technology and cyber
    target_date: 2026-05-20

review_gates: [scope, evidence, authority, impact, decision]
human_review_required: true
confidence_label: medium

source_trace:
  - claim: NYDFS Part 500 covered-entity scope includes state-chartered banks with NY licenses
    source: 23 NYCRR Part 500
    section: §500.1(c) covered-entity definition
    url: https://www.dfs.ny.gov/industry_guidance/cybersecurity
    section_confidence: high
  - claim: NYDFS issued the Industry Letter on cybersecurity risks arising from GenAI in October 2024
    source: NYDFS Industry Letter
    section: [verify date and section]
    url: https://www.dfs.ny.gov/industry_guidance/[verify]
    section_confidence: medium
  - claim: §500.11 requires a third-party SP security policy
    source: 23 NYCRR Part 500
    section: §500.11
    url: https://www.dfs.ny.gov/industry_guidance/cybersecurity
    section_confidence: high
  - claim: §500.16 requires an incident-response plan and §500.17 requires notification of cybersecurity events
    source: 23 NYCRR Part 500
    section: §§500.16, 500.17
    url: https://www.dfs.ny.gov/industry_guidance/cybersecurity
    section_confidence: high
  - claim: SR 11-7 applies to AI/ML models in production
    source: FRB SR 11-7 — Guidance on Model Risk Management
    section: §V model documentation
    url: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm
    section_confidence: high
```

## Why the assessment shape matters

- The cross-cutting overlay set (cyber + AI-governance) is operative; loading only the cyber overlay misses the AI-use-case-intake refresh and the model-supply-chain risk specifics that the Industry Letter brings.
- The strategy lens picks up an examiner-posture-shift signal that the implementation lens alone misses: NYDFS Industry Letters historically signal cross-state convention, so the bank's examination posture for FDIC and for any other state where the bank operates is influenced by the same letter even though the letter is technically NYDFS-only.
- The third-party impact section is the longest section because the rule's primary deployment vehicle (a sponsor-tenant LLM platform) carries the operative cyber risk; the assessment names the vendor evidence-pack refresh and the right-to-audit possibility.
- Open questions route to TPRM, legal, and CISO with due dates; the assessment is operationally usable rather than a static document.
- The `confidence_label: medium` is the honest read because three open questions remain, the cost-to-comply range is bottom-up, and the Industry Letter's interpretive scope (internal-only vs customer-facing) is not yet settled.
