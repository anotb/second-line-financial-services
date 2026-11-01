# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## cfpb-circular-adverse-action-ai-ml

### Example: CFPB Circular on adverse-action notices using AI/ML credit decisioning (mid-size consumer bank)

#### Input

A mid-size consumer bank ($25B in assets, OCC-supervised national bank, with a meaningful unsecured personal-lending and credit-card business) is reading the **May 12, 2025 CFPB withdrawal of a broad set of circulars including Circular 2022-03 and Circular 2023-03 on adverse-action notices using AI/ML credit decisioning**. Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary continue to apply on their own terms; the withdrawal removes the bureau's interpretive layer but does not change what the regulation requires. The bank's model risk officer flags the withdrawal; the head of regulatory affairs commissions the impact assessment to confirm that the bank's adverse-action reason-code generation pipeline still meets the regulatory text without depending on the withdrawn circular. Engagement scope is supplied: institution = national bank, primary regulators = OCC and CFPB (CFPB direct supervision applies above $10B), persona = head of regulatory affairs and head of consumer compliance, source posture = public-plus-firm-policy, sector overlay = banking, cross-cutting overlays = conduct (fair-lending implication) and AI-governance (model-risk implication). Time pressure: 14-day read for the regulatory-change-committee; finalised assessment by 21 days.

#### Why this scenario matters

This is the canonical impact-assessment use of the skill on a regulatory withdrawal: the source is a bureau action that removes interpretive guidance without amending the underlying rule. The implementation lens hits multiple obligation domains (fair-lending, model-risk, consumer-disclosure) on the strength of Reg B §1002.9 and the Official Staff Commentary, not the withdrawn circulars. The strategy lens reads against the broader May 2025 CFPB guidance withdrawal pattern, state-AG and prudential-regulator continuity on the same fact patterns, and examiner-posture signal from OCC and FRB enforcement. The cross-cutting overlay set (conduct + AI-governance) is operative; loading only the banking sector overlay misses the fair-lending and model-risk specifics.

#### Output sketch

```yaml
assessment_id: RIA-2026-CFPB-AAN-AIML-01
engagement_id: ENG-2026-RCM-CFPB-AAN
as_of_date: 2026-05-06

decision_required: log the CFPB withdrawal of Circulars 2022-03 / 2023-03 in the regulatory-change inventory as a status change rather than a new obligation; reconfirm that the bank's adverse-action reason-code pipeline meets Reg B §1002.9 and Comment 9(b)(2)-3 on the regulatory text alone; refresh the fair-lending-and-credit-decisioning policy and the model-risk-management policy to remove citations that depend on the withdrawn circulars; do not relax the operating standard.
recommended_posture: implementation lens — confirm the adverse-action reason-code generation pipeline still supports specific principal reasons, refresh policy citations to anchor on Reg B and the Official Staff Commentary, retain the existing operating bar; strategy lens — track state-AG and prudential-regulator posture on the same fact patterns, watch for examiner pivot to OCC and FRB enforcement, no relaxation of internal standards.

source_citation:
  regulator: CFPB
  regulator_office: CFPB Office of the Director
  instrument_type: guidance withdrawal
  citation: CFPB withdrawal of broad set of circulars and policy statements (May 12, 2025), including Circular 2022-03 and Circular 2023-03 on adverse-action notices using complex algorithms / AI
  section: bureau-wide withdrawal action
  publication_date: 2025-05-12
  effective_date: 2025-05-12 (withdrawals took effect on publication)
  url: https://www.consumerfinance.gov/compliance/circulars/
  related_instruments:
    - ECOA Reg B §1002.9 (operative regulatory text — not affected by withdrawal)
    - Reg B Official Staff Commentary, Comment 9(b)(2)-3 (operative — not affected)
    - CFPB Circulars 2022-03 and 2023-03 [historical only after May 12, 2025]

in_scope: true
in_scope_rationale: |
  The bank operates AI/ML credit-decisioning models for unsecured personal lending and credit-card underwriting. Reg B §1002.9 reason-code requirements apply; the circular interprets the reason-code requirement when AI/ML is the basis for the decision. The bank's $25B asset size places it under CFPB direct supervision (above $10B threshold).

scope:
  institution_types: [national bank]
  affected_business_units: [head of unsecured personal lending, head of credit cards, head of consumer-credit-decisioning, head of credit-risk modelling]
  affected_products: [unsecured personal loans, credit cards]
  affected_geographies: [federal]
  thresholds_named:
    - threshold_text: $10B in total assets places the firm under CFPB direct supervision
      firm_read: above the threshold ($25B in assets)
      source: 12 USC §5515 [verify subsection]

effective_date_posture:
  mandatory_compliance_date: n/a — interpretive circular
  transition_period: n/a
  early_adoption_posture: not applicable; the circular interprets existing Reg B §1002.9, so the bank's compliance posture is "in compliance now" with the firm's reason-code generation pipeline assessed against the circular's interpretation

affected_obligation_domains:
  - fair-lending
  - model-risk
  - consumer-disclosure
  - AI-governance
  - UDAAP

policy_impact:
  - policy_area: fair-lending-and-credit-decisioning policy
    expected_change_type: amendment
    rationale: tighten the policy's section on AI/ML model use in credit decisioning to reflect the circular's interpretation; specify that reason-code generation must reflect the principal reasons for the AI/ML model's decision
  - policy_area: model risk management policy
    expected_change_type: cross-reference-update
    rationale: cross-reference the circular's interpretation in the policy section on AI/ML model documentation and validation
  - policy_area: adverse-action-notice procedure
    expected_change_type: procedure-refresh
    rationale: refresh the procedure's section on reason-code mapping for AI/ML-driven decisions; specify that generic reason codes are insufficient when the AI/ML model produces non-standard reasons

control_impact:
  - control_objective: reason-code mapping for AI/ML-driven adverse-action decisions reflects the principal reasons the model declined the application
    expected_change_type: existing-control-objective-rescoped
    anticipated_evidence_gap: documentation of the mapping methodology between AI/ML model output and reason-code generation; testing evidence that the mapping reflects principal reasons
  - control_objective: adverse-action notices contain accurate, specific, and not-overly-generic reasons
    expected_change_type: testing-methodology-change
    anticipated_evidence_gap: testing methodology updates to sample AI/ML-driven adverse-action notices and validate reason-code accuracy against the model's actual decision basis
  - control_objective: fair-lending model risk review covers reason-code generation alongside model performance and disparate-impact analysis
    expected_change_type: existing-control-objective-rescoped
    anticipated_evidence_gap: model risk review reports updated to include reason-code-generation review

reporting_impact:
  - report_or_disclosure: adverse-action notices to denied applicants
    change_type: existing-public-disclosure-amended
  - report_or_disclosure: fair-lending committee reporting
    change_type: existing-report-amended

technology_data_impact:
  - system_or_data_area: credit-decisioning platform
    implication: implement reason-code-generation logic that maps AI/ML model output to specific reasons; instrument the model output for explainability; retain reason-code-mapping documentation
    new_data_field: model-reason-code metadata field on the adverse-action record
    model_inventory_implication: tier-2 and tier-3 AI/ML credit-decisioning models updated documentation for reason-code methodology
  - system_or_data_area: model risk governance system
    implication: model-validation reports updated to cover reason-code generation

third_party_impact:
  - arrangement_type: model-vendor
    expected_change_type: evidence-pack-refresh
    rationale: where the credit-decisioning platform vendor supplies the model or the explainability layer, refresh the vendor evidence pack to cover reason-code methodology; trigger right-to-audit if the vendor's documentation is insufficient

customer_impact:
  - change_area: adverse-action
    implication: customers receive more specific, accurate adverse-action notices; the disclosed reasons reflect the actual basis of the AI/ML model's decision rather than generic reason codes

cost_to_comply:
  implementation_one_time:
    indicative_range: $1M to $3M one-time
    basis: similar-prior-project benchmark (the bank's prior model-explainability build for the AI/ML credit-decisioning platform); vendor-quote range for reason-code-mapping refresh
    confidence: medium
  ongoing_run_rate:
    indicative_range: $200K to $500K annual
    basis: ongoing testing, monitoring, and model risk review burden
    confidence: medium
  cost_drivers:
    - reason-code-mapping methodology and documentation
    - testing-methodology refresh
    - model risk review-process refresh
    - vendor evidence-pack refresh
    - adverse-action-notice template refresh
    - training for credit-policy and adverse-action-notice teams
  agency_estimate_reference:
    agency_estimate_summary: the CFPB withdrawal action does not include a cost estimate; the underlying Reg B §1002.9 and Comment 9(b)(2)-3 obligations are unchanged, so cost-of-compliance does not increase from the withdrawal itself. Cost in this read is policy-citation refresh and confirmatory testing rather than control rebuild.
    firm_divergence_note: the firm's read is that the operative bar is unchanged and that the cost-to-comply is the cost of policy-citation refresh plus confirmatory testing of the existing pipeline.
    source_pin: CFPB withdrawal action May 12, 2025; firm's existing credit-decisioning-platform documentation

regulatory_strategy:
  firm_position: neutral-with-operational-concerns
  regulator_engagement_posture:
    - industry-association-comment-letter
    - ongoing-supervisory-dialogue
  comment_period_posture:
    owner_role: n/a — interpretive circular, no comment period
    draft_pathway: n/a
  public_consultation_posture: none
  peer_industry_alignment: industry consensus is that the circular's interpretation is consistent with ECOA / Reg B §1002.9; the operational concern is the depth of model-explainability documentation required and the reason-code-mapping methodology; trade-association coordination supports a clarifying engagement with the CFPB on what constitutes principal-reason adequacy
  industry_associations_engaged:
    - ABA fair-lending committee
    - Consumer Bankers Association UDAAP and fair-lending engagement
  escalation_triggers:
    - trigger: model-explainability documentation gap identified during the model risk review refresh
      escalation_level: CRO
    - trigger: fair-lending disparity finding tied to reason-code-generation methodology
      escalation_level: general-counsel

open_questions:
  - question: where the AI/ML model's decision reflects a complex multi-feature interaction, what level of reason-code specificity meets the circular's "principal reasons" interpretation
    owner_role: legal
    blocker_for: rule-to-obligation-extraction-kickoff
    due_date: 2026-05-13
  - question: whether the bank's current reason-code taxonomy in the credit-decisioning platform is sufficient or whether a refresh is required
    owner_role: model-risk
    blocker_for: implementation-plan-sequencing
    due_date: 2026-05-20
  - question: whether the trade-association coordination letter has reached consensus posture on principal-reason adequacy
    owner_role: compliance
    blocker_for: strategy-posture-finalisation
    due_date: 2026-05-27

recommended_next_steps:
  - next_step: kick off rule-to-obligation-extraction on the circular's reason-code interpretive guidance
    owner_role: head of consumer compliance
    target_date: 2026-05-13
  - next_step: run policy-diff against the fair-lending-and-credit-decisioning policy and the model risk management policy
    owner_role: head of policy and standards
    target_date: 2026-05-20
  - next_step: commission implementation-plan for the reason-code-mapping refresh, the testing-methodology refresh, the model risk review-process refresh, and the adverse-action-notice template refresh
    owner_role: head of regulatory change
    target_date: 2026-05-27
  - next_step: refine cost-to-comply with finance partner; confirm one-time and run-rate ranges
    owner_role: finance business partner for consumer compliance
    target_date: 2026-05-20

review_gates: [scope, evidence, authority, impact, decision]
human_review_required: true
confidence_label: medium

source_trace:
  - claim: ECOA / Reg B §1002.9 requires creditors to provide specific reasons for adverse action
    source: 12 CFR §1002.9
    section: §1002.9(a)(2) and (b)(2) [verify subsection]
    url: https://www.ecfr.gov/current/title-12/chapter-X/part-1002
    section_confidence: high
  - claim: the CFPB had previously interpreted the principal-reasons requirement as applying to AI/ML model decisions with specificity (Circulars 2022-03 / 2023-03); that interpretive layer was withdrawn May 12, 2025. The underlying obligation under Reg B §1002.9 and Comment 9(b)(2)-3 is unchanged.
    source: CFPB Circulars 2022-03 (May 26, 2022) and 2023-03 (September 19, 2023) — withdrawn May 12, 2025
    section: applicability section on AI/ML adverse-action notices [historical reference]
    url: https://www.consumerfinance.gov/compliance/circulars/
    section_confidence: high (withdrawal status); historical only on substantive interpretation
  - claim: CFPB direct supervision applies for depository institutions with $10B+ in total assets
    source: 12 USC §5515
    section: §5515(a) [verify subsection]
    url: https://www.law.cornell.edu/uscode/text/12/5515
    section_confidence: high
  - claim: model risk review covering reason-code generation is consistent with SR 11-7 model documentation expectations
    source: FRB SR 11-7 — Guidance on Model Risk Management
    section: §V model documentation
    url: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm
    section_confidence: high
```

#### Why the assessment shape matters

- The two-lens design pulls the strategy posture forward: a circular is interpretive, so the engagement posture (trade-association coordination, ongoing supervisory dialogue) is what makes the assessment honest about what the firm is actually doing.
- The cross-cutting overlay set (conduct + AI-governance) is operative; loading only the banking sector overlay misses the fair-lending model risk review handoff between MRM and the fair-lending officer.
- The cost-to-comply read is medium confidence and bottom-up from a similar prior project; the assessment names the basis rather than presenting a precision-without-grounding range.
- Open questions route to legal, model risk, and compliance with due dates; the assessment is operationally usable rather than a static document.
- The `confidence_label: medium` is the honest read because three open questions remain and the cost-to-comply range is bottom-up rather than vendor-confirmed.

## nydfs-genai-cybersecurity-letter

### Example: NYDFS October 2024 Industry Letter on cybersecurity risks arising from GenAI (state-chartered bank using GenAI for customer service)

#### Input

A state-chartered bank ($8B in assets, NYDFS-supervised state-licensed bank with NY headquarters and FDIC insurance) has deployed a GenAI customer-service assistant for retail customers (FAQ answering, account-balance lookup with authentication, lending-product information) on a third-party LLM platform with a sponsor-tenant agreement. The bank's CISO flags the NYDFS Industry Letter [verify date and section]; the head of regulatory affairs commissions the impact assessment. Engagement scope is supplied: institution = state-chartered bank, primary regulators = NYDFS and FDIC, persona = head of regulatory affairs and CISO, source posture = public-plus-firm-policy, sector overlay = banking, cross-cutting overlays = cyber and AI-governance. Time pressure: 7-day read for the operational-risk-committee; finalised assessment by 14 days.

#### Why this scenario matters

This is the canonical impact-assessment use of the skill on an NYDFS Industry Letter: the Industry Letter is interpretive of an existing regulation (Part 500), so the implementation lens reads against existing covered-entity-scope obligations rather than a brand-new rule. The cross-cutting overlay set (cyber + AI-governance) is operative; loading only the cyber overlay misses the AI-governance specifics that the Industry Letter brings (third-party LLM platform risk, prompt-injection control, data-leakage control). The strategy lens is rich on examiner-posture-shift signal: NYDFS Industry Letters historically signal cross-state convention, and other state regulators (Connecticut, California) have followed NYDFS's posture on cyber-and-AI topics. The bank also has an FDIC overlay to consider; FDIC has not issued a parallel Industry Letter, but the bank's FDIC examination cycle will read against any cyber posture shift.

#### Output sketch

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

#### Why the assessment shape matters

- The cross-cutting overlay set (cyber + AI-governance) is operative; loading only the cyber overlay misses the AI-use-case-intake refresh and the model-supply-chain risk specifics that the Industry Letter brings.
- The strategy lens picks up an examiner-posture-shift signal that the implementation lens alone misses: NYDFS Industry Letters historically signal cross-state convention, so the bank's examination posture for FDIC and for any other state where the bank operates is influenced by the same letter even though the letter is technically NYDFS-only.
- The third-party impact section is the longest section because the rule's primary deployment vehicle (a sponsor-tenant LLM platform) carries the operative cyber risk; the assessment names the vendor evidence-pack refresh and the right-to-audit possibility.
- Open questions route to TPRM, legal, and CISO with due dates; the assessment is operationally usable rather than a static document.
- The `confidence_label: medium` is the honest read because three open questions remain, the cost-to-comply range is bottom-up, and the Industry Letter's interpretive scope (internal-only vs customer-facing) is not yet settled.

## troubleshooting

### Troubleshooting: regulatory-impact-assessment

The impact assessment is the second line's first read on a regulatory item; mistakes at this stage shape every downstream skill (rule-to-obligation-extraction, policy-diff, implementation-plan, exam-brief). The defects below recur across teams and across regulators.

#### 1. Treating the assessment as a legal interpretation

**Symptom**: The assessment opines on whether the rule applies to the firm as a matter of law, characterises a regulator's interpretive position as binding, or settles an ambiguous-applicability question without legal review. Counsel reads the assessment and rewrites the in-scope-determination section to remove the legal conclusion.

**Why it happens**: The line between scoping the rule and interpreting it is thin under time pressure; the practitioner reaches for a conclusion when the question warrants a routed open question.

**Resolution**:
- The skill names obligations and routes open questions; it does not opine on whether the rule applies as a matter of law.
- Where applicability is ambiguous (a threshold question, an activity-classification question, a state-by-state-adoption question, an AI-system definitional question), the assessment carries an `open_questions` entry routed to legal with a due date.
- The `in_scope_rationale` field cites the source pin and names the firm-side facts; it does not interpret the rule's text beyond what the source itself says.
- Where the rule's interpretive position is the question (a CFPB Circular, a regulator speech, a consent-order-pattern theme), the assessment characterises the regulator's position with quoted or paraphrased language and routes interpretive questions to qualified review.

#### 2. Loading every sector and cross-cutting overlay for completeness

**Symptom**: The assessment loads all four sector overlays and all four cross-cutting overlays; the assessment reads as a generic compendium with no operative direction. The strategy lens is diluted across sectors that do not apply to the firm; the implementation lens carries cyber-and-conduct-and-climate-and-privacy threads when the rule is privacy-only.

**Why it happens**: The instinct toward completeness overrides the discipline of loading what the scope flags.

**Resolution**:
- Sector overlay loads from the scope record's `sector_overlay_set`, not from practitioner habit.
- Cross-cutting overlay loads from the scope record's `cross_cutting_overlay_set`, not from "every cross-cutting topic the rule could plausibly touch."
- A multi-sector firm (e.g., a bank holding company with a registered broker-dealer subsidiary and a state-chartered insurer) loads sector overlays for the legal entities the rule actually scopes. A rule scoping advisers loads capital-markets only; a rule scoping bank-holding-company-level requirements loads banking; a rule scoping insurer subsidiaries loads insurance.
- Cross-cutting overlay sets are typically a single overlay or two overlays at most. A privacy-anchored rule loads privacy. A cyber-anchored rule loads cyber. A rule that is both AI-and-cyber loads cyber plus the AI-related sections of the conduct or other relevant overlay where the rule has a fair-lending or conduct intersection.

#### 3. The strategy lens is missing or pro-forma

**Symptom**: The assessment's strategy section reads as boilerplate ("the firm will engage through industry-association channels"; "no public position"; "comment letter to be drafted"). The CRO chief of staff reads it for an actual posture and finds none.

**Why it happens**: The implementation lens is the practitioner's home territory; the strategy lens requires industry-association coordination, examiner-posture reading, and litigation-and-engagement-history awareness that the practitioner may not have at hand.

**Resolution**:
- The strategy section reads against named industry associations the firm engages with on the rule (BPI, ABA, ICBA, SIFMA, ICI, IAA, ACLI, NAFCU, MBA, FTA, AFC, others); the assessment names which association(s) the firm is on, and where peer alignment runs.
- Examiner-posture-shift signal reads against named, dated regulator speeches, supervisory-priorities communications, and Supervisory Highlights editions; not "the regulator has emphasised X" without a citation.
- Comment-period posture is dated and routed: if the rule is proposed and the comment period closes on a specific date, the comment posture has an internal owner, a draft pathway, an approval gate, and a submission target date.
- Escalation triggers read against firm-specific thresholds: cost-to-comply, board-reporting expectation, material-risk-management-framework implication, consent-order-pattern peer reference. Escalation triggers without thresholds drift.

#### 4. Cost-to-comply with precision but no basis

**Symptom**: The financial-impact section presents a precise dollar range ("$3M to $5M one-time, $400K annual") without naming the basis. Finance reads it; the partner asks where the numbers came from; the practitioner cannot answer.

**Why it happens**: Cost-to-comply ranges are often the headline number CRO and CFO read first, and the pull toward precision is strong; the basis discipline is harder.

**Resolution**:
- `cost_to_comply.implementation_one_time.basis` and `cost_to_comply.ongoing_run_rate.basis` name the basis: peer benchmark, vendor estimate, similar prior project, agency RIA, firm-side estimate.
- `cost_to_comply.implementation_one_time.confidence` and `cost_to_comply.ongoing_run_rate.confidence` carry an honest confidence label (`high` / `medium` / `low` / `unknown`); for first-week assessments on a new rule, `low` or `medium` are usually the honest read.
- Where the firm's read diverges from the agency's RIA estimate (which it routinely does), the assessment names the divergence and the basis. The strategy lens often picks up that divergence as a comment-letter input.
- A range is fine where it reflects genuine uncertainty (e.g., "$1M to $3M" because the vendor-quote variance is real). A precision-without-basis number ("$2.4M") is a false signal.

#### 5. The two-lens assessment collapses into a single lens

**Symptom**: The assessment reads as a pure implementation document (in-scope, policy impact, control impact, cost-to-comply) with no strategy section, or as a pure strategy document (firm position, comment-period posture, peer alignment) with no implementation detail. Audience confusion follows: regulatory affairs reads the strategy version and asks where the policy impact is; CRO chief of staff reads the implementation version and asks where the engagement posture is.

**Why it happens**: The practitioner anchors on the audience they spend most time with and lets the other lens drift.

**Resolution**:
- Both lenses run; the assessment audience is the union of regulatory affairs, head of compliance, head of legal, CRO chief of staff, and head of business affected, not any single role.
- Where the assessment is being prepared for a board pre-read, the board pre-read distils to executive summary, strategy posture, financial impact, and decision request, but the underlying assessment carries both lenses.
- The implementation lens flexes to the source type: an interpretive circular has shorter implementation sections than a 600-page final rule; the strategy lens has shorter comment-period content for a final rule than for a proposed rule.
- The two lenses cross-reference: the cost-to-comply read informs the strategy posture (a high cost-to-comply may shift the firm position from neutral to opposition); the strategy posture informs the implementation pathway (an opposition posture may delay the implementation kickoff pending litigation).

#### 6. The source-identification block is thin

**Symptom**: The source-citation field carries a regulator and a topic ("CFPB on adverse-action notices") but no release number, no publication date, no Federal Register citation. The downstream rule-to-obligation-extraction skill receives an ambiguous handoff and re-identifies the source.

**Why it happens**: The practitioner has the source open in a browser tab and writes the assessment from that context; the precise citation does not make it onto the page.

**Resolution**:
- `source_citation.regulator`, `source_citation.instrument_type`, `source_citation.citation`, `source_citation.publication_date`, and `source_citation.url` are populated in every assessment.
- Where the section reference is unknown, `source_citation.section` carries `[verify section]` rather than fabricated detail.
- Related instruments (the proposed rule that preceded the final, the FAQ that updated the bulletin, the speech that signalled the priority) read in `source_citation.related_instruments`. Downstream skills consume them.
- For a regulator speech or an enforcement-pattern theme, the citation is the speech URL and date or the published consent-order ID; the source-citation block is honest about the soft-source nature of the trigger.

#### 7. Open questions without a routed owner or a due date

**Symptom**: The `open_questions` array carries questions without `owner_role` or `due_date`; the questions sit in the assessment without movement; downstream skills wait for resolution that does not come.

**Why it happens**: Open questions are easy to surface and harder to route; the practitioner adds them to the assessment as a list and moves on.

**Resolution**:
- Every open question carries `owner_role` (legal, compliance, business-head, sponsor, model-risk, TPRM, CISO, BSA-officer, fair-lending-officer, privacy-officer, data-protection-officer) and `blocker_for` (rule-to-obligation-extraction-kickoff, policy-diff-scope, implementation-plan-sequencing, comment-letter-signature, strategy-posture-finalisation, exam-brief-handoff).
- `due_date` is set; an open question without a due date is a question that drifts.
- The assessment's executive summary references the open-question count and the highest-impact blocker; the named lead reads the executive summary and routes the questions before attesting.

#### 8. The transition-period posture is missed

**Symptom**: The assessment names the effective date but says nothing about phase-in stages, transition relief, or sunset clauses. Implementation-plan inherits the assessment and discovers mid-sequencing that a phase-in stage shifts a milestone by 12 months.

**Why it happens**: Effective dates are scanned for the first compliance date; transition-period detail is buried in a later section of the rule and gets skipped.

**Resolution**:
- `effective_date_posture.phase_in_stages` is populated where the rule has tier-by-tier phase-in (1071, DORA, CRA modernisation, Basel III Endgame).
- `effective_date_posture.transition_period` carries the transition-relief description with the citation.
- `effective_date_posture.sunset_or_contingency` carries Congressional Review Act dependency, judicial review status, or agency-rulemaking-implementation contingency.
- `effective_date_posture.early_adoption_posture` is named where the firm is considering early compliance.
- Where the rule's effective date is itself uncertain (litigation-stay; vacatur; CRA disapproval), the assessment says so and names what the firm's compliance posture is in the meantime.

#### 9. Customer impact named in technical jargon

**Symptom**: The customer-impact section reads in regulatory-and-system-of-record language ("customer adverse-action notification timing extends from 30 to 45 days; UDAAP-risk surface broadens"). The head of consumer banking reads it and asks what the customer experience actually changes.

**Why it happens**: The practitioner writes the assessment in second-line vocabulary; customer-impact is not the practitioner's natural register.

**Resolution**:
- `customer_impact[*].implication` reads in plain language: what the customer sees, hears, or experiences differently.
- Where the rule introduces a new customer right, the implication names the right ("customer can request data deletion within 45 days; firm responds within 30 days") rather than the regulatory-categorical name.
- Where the rule alters the customer's evidence burden, the implication names the additional burden ("customer at account opening must produce additional KYC documentation including X").
- The customer-impact section reads alongside the operating-model implication; the head of business affected uses both.

#### 10. The assessment is treated as the deliverable, not the kickoff artifact

**Symptom**: The assessment gets drafted, signed off, and then sits unread for the duration of the regulatory item. The downstream skills run from email and ad-hoc steering items; the assessment is not consulted again.

**Why it happens**: The assessment was treated as a one-time document for the regulatory-change-committee rather than as the kickoff artifact for the downstream skills and the inventory record.

**Resolution**:
- The assessment is the kickoff artifact for the chain. `rule-to-obligation-extraction` reads `affected_obligation_domains` and `source_citation`. `policy-diff` reads `policy_impact`. `implementation-plan` reads `affected_obligation_domains`, `effective_date_posture`, and `cost_to_comply`. `exam-brief` reads the assessment when the item enters an exam window.
- The assessment is updated as open questions resolve; a revision log captures the deltas.
- Where a regulator amends the rule (a finalised version of a proposed rule, an FAQ update, a litigation-driven implementation-date change), the assessment is re-emitted with the updated source-citation block and the downstream skills are re-run with the revised handoff.

#### 11. Engagement-scope record stale or missing

**Symptom**: The assessment was drafted from yesterday's understanding; today the firm's footprint has expanded (an acquisition closes; a new state license issues; a registered fund launches), and the in-scope determination no longer matches the firm.

**Why it happens**: The scope record was treated as a kickoff artifact rather than a living record. The assessment consumed an old version.

**Resolution**:
- Engagement-scope is a status, not a fixed truth. Re-emit the scope record after any material change; re-emit the assessment consuming the updated scope.
- Standing scope review at the regulatory-change-committee cadence; for high-impact items, weekly or bi-weekly scope check.
- Where the assessment is run without an scope record at all, ask the questions (institution, primary regulators, persona, source posture, time pressure) and default to public posture if the practitioner declines. Note in the assessment that scope was not formalised.

#### 12. Boundary with downstream skills not respected

**Symptom**: The assessment duplicates rule-to-obligation-extraction (decomposing the rule into atomic obligations row by row), policy-diff (drafting policy language), or implementation-plan (sequencing milestones with dates and owners). Two artifacts say almost the same thing with subtle inconsistencies.

**Why it happens**: The boundary between the impact assessment and the downstream skills was not respected; the practitioner pulled work forward.

**Resolution**:
- The impact assessment names the surface area and routes the handoffs; it does not decompose obligations row by row, draft policy language, or sequence milestones.
- `affected_obligation_domains` are high-level domains, not atomic obligations.
- `policy_impact[*].rationale` is a sentence on why the policy area is affected; it is not a draft of the policy amendment.
- `cost_to_comply` is an indicative range with a basis; it is not a milestone-level cost-and-resource plan.
- Where the assessment has been pulled too far forward, the named lead routes the work back to the appropriate downstream skill.
