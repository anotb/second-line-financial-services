# Example: CFPB Circular on adverse-action notices using AI/ML credit decisioning — mid-size consumer bank

## Input

A mid-size consumer bank ($25B in assets, OCC-supervised national bank, with a meaningful unsecured personal-lending and credit-card business) is reading the CFPB Circular on adverse-action notices using AI/ML credit decisioning [verify exact circular number, publication date, and section]. The circular addresses ECOA / Reg B §1002.9 reason-code requirements when the firm uses AI/ML in credit underwriting. The bank's model risk officer flags it; the head of regulatory affairs commissions the impact assessment. Engagement scope is supplied: institution = national bank, primary regulators = OCC and CFPB (CFPB direct supervision applies above $10B), persona = head of regulatory affairs and head of consumer compliance, source posture = public-plus-firm-policy, sector overlay = banking, cross-cutting overlays = conduct (fair-lending implication) and AI-governance (model-risk implication). Time pressure: 14-day read for the regulatory-change-committee; finalised assessment by 21 days.

## Why this scenario matters

This is the canonical impact-assessment use of the skill on a circular: the source is short and pointed, the implementation lens hits multiple obligation domains (fair-lending, model-risk, consumer-disclosure), and the strategy lens is rich (industry-association coordination on circular interpretation, examiner-posture signal from CFPB Supervisory Highlights, fair-lending model-risk handoff between MRM and the fair-lending officer). The cross-cutting overlay set (conduct + AI-governance) is operative; loading only the banking sector overlay misses the fair-lending and model-risk specifics. The bank does not run the overlay set in autopilot; it loads the conduct overlay because the circular is fair-lending, and the AI-governance read because the circular is AI/ML-anchored.

## Output sketch

```yaml
assessment_id: RIA-2026-CFPB-AAN-AIML-01
engagement_id: ENG-2026-RCM-CFPB-AAN
as_of_date: 2026-05-06

decision_required: ingest the CFPB Circular into the regulatory-change inventory; kick off rule-to-obligation-extraction; commission policy-diff against the fair-lending-and-credit-decisioning policy and the model-risk-management policy; sign onto the trade-association coordination letter.
recommended_posture: implementation lens — refresh the adverse-action reason-code generation pipeline for AI/ML-driven decisions, refresh the fair-lending model-risk review programme, and tighten reason-code documentation; strategy lens — neutral with operational concerns, sign onto the trade-association coordination letter, no firm-direct comment because the circular is interpretive.

source_citation:
  regulator: CFPB
  regulator_office: CFPB Office of Supervision Policy
  instrument_type: circular
  citation: CFPB Circular [verify circular number and date]
  section: applicability section on AI/ML adverse-action notices
  publication_date: [verify]
  effective_date: n/a — interpretive circular, applies as of publication
  url: https://www.consumerfinance.gov/compliance/circulars/[verify]
  related_instruments:
    - ECOA Reg B §1002.9 [verify subsection]
    - CFPB Bulletin on adverse-action notices [verify if applicable]
    - CFPB Supervisory Highlights edition referencing AI/ML credit decisioning [verify edition]

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
    agency_estimate_summary: the CFPB Circular itself does not include a cost estimate (interpretive circulars generally do not); the underlying ECOA / Reg B reason-code rule predates the AI/ML interpretive question
    firm_divergence_note: the firm's read on cost is bottom-up from the credit-decisioning-platform refresh and the testing-methodology refresh
    source_pin: CFPB Circular [verify]; firm's prior credit-decisioning-platform refresh project record

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
  - claim: the CFPB has interpreted the principal-reasons requirement as applying to AI/ML model decisions with specificity
    source: CFPB Circular [verify circular number]
    section: applicability section on AI/ML adverse-action notices
    url: https://www.consumerfinance.gov/compliance/circulars/[verify]
    section_confidence: medium
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

## Why the assessment shape matters

- The two-lens design pulls the strategy posture forward: a circular is interpretive, so the engagement posture (trade-association coordination, ongoing supervisory dialogue) is what makes the assessment honest about what the firm is actually doing.
- The cross-cutting overlay set (conduct + AI-governance) is operative; loading only the banking sector overlay misses the fair-lending model risk review handoff between MRM and the fair-lending officer.
- The cost-to-comply read is medium confidence and bottom-up from a similar prior project; the assessment names the basis rather than presenting a precision-without-grounding range.
- Open questions route to legal, model risk, and compliance with due dates; the assessment is operationally usable rather than a static document.
- The `confidence_label: medium` is the honest read because three open questions remain and the cost-to-comply range is bottom-up rather than vendor-confirmed.
