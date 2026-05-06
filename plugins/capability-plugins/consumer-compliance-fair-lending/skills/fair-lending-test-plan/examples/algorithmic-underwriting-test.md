# Example: algorithmic-underwriting test plan for a fintech consumer-credit platform

## Input

A fintech personal-loan platform operates with a sponsor bank under a marketing and program-management arrangement. The platform underwrites with an in-house ML scoring model that consumes traditional credit features plus alternative data (cash-flow signals from a permissioned bank-data connection, employment-tenure inferred from payroll-data integration, device and behavioral signals from the application session). The model has a current model card and was last validated 11 months ago. Complaint themes for the prior six months include adverse-action notices that recipients found vague (the bureau's CFPB Circular 2023-03 angle on AI/complex-model adverse-action accuracy is in scope). The fair-lending team is the program-bank's second-line; the fintech's compliance team is the program-operator first-line. Source posture is public-plus-firm-policy-plus-evidence; sponsor-bank counsel directs.

## Why this scenario matters

This is the algorithmic-discrimination pattern flagged by the April 2023 Joint Statement and the CFPB AI circulars. The plan must include less-discriminatory-alternative testing because an AI/ML model drives the underwriting decision. The plan also has to deal with the bank-fintech split: where sponsor-bank duty sits, where program-operator duty sits, what the contract-of-record (program agreement) says about second-line review and remediation. The marketing-funnel skew test is not optional; protected-class targeting can happen pre-application.

## Output sketch

```yaml
plan_id: FL-PLAN-2026-FT-PL-01
risk_assessment_ref: FL-RA-2026-Q1-fintech-program
trigger: complaint-theme-trigger
as_of_date: 2026-05-06

scope:
  products: [unsecured-personal]
  decision_points: [marketing, underwriting, pricing, adverse-action]
  period: {start: 2025-01-01, end: 2025-12-31}
  geographies: [US-national-program-footprint]
  channels: [digital-direct, partner-marketplace]
  exclusions:
    - Servicing and loss mitigation (separate plan)
    - Collections (separate plan)
    - Fraud-deny decisioning (separate fraud-fairness review)

prohibited_bases_tested: [race, ethnicity, national-origin, sex, age, marital-status]

model_inventory_in_scope:
  - model_id: PL-UW-SCORE-v4
    version: 4.2.1
    decision_use: underwriting-score
    ai_ml: true
    vendor_or_inhouse: in-house
    validation_status: validated
    card_reference: MC-PL-UW-SCORE-v4
  - model_id: PL-PRICING-TIER-v2
    version: 2.0.0
    decision_use: pricing-tier
    ai_ml: true
    vendor_or_inhouse: in-house
    validation_status: validated
    card_reference: MC-PL-PRICING-TIER-v2
  - model_id: MKT-LOOKALIKE-v3
    version: 3.1.0
    decision_use: marketing-targeting
    ai_ml: true
    vendor_or_inhouse: vendor-fine-tuned
    validation_status: in-validation
    card_reference: MC-MKT-LOOKALIKE-v3

tests:
  - test_id: FL-T-01
    test_type: regression-underwriting
    decision_point: underwriting
    hypothesis: >
      The underwriting decision (approve / counter / decline) is not associated
      with prohibited-basis indicators after controlling for legitimate
      credit-relevant features.
    method: >
      Logistic regression on the full 2025 underwriting population. Outcome:
      decline indicator. Controls: traditional credit features plus the
      alternative-data buckets the model uses (cash-flow signal bands,
      employment-tenure buckets). Robust standard errors. Sensitivity test
      with model-score as the regressor instead of the decision.
    demographic_proxy_method: BISG
    demographic_proxy_caveats: >
      BISG carries known accuracy variation by region and surname concentration;
      report results with BISG-uncertainty intervals and re-run on the subset
      with high-confidence proxy assignment.
    data_required:
      - {field: underwriting-decision-and-features, system_of_record: underwriting-data-warehouse, owner: data-engineering, gap_flag: available}
      - {field: applicant-name-and-address, system_of_record: application-platform, owner: platform-eng, gap_flag: available}
      - {field: model-score-and-feature-contributions, system_of_record: ml-platform-feature-store, owner: ml-platform, gap_flag: available}
    statistical_threshold: p < 0.05 on prohibited-basis coefficients; effect-size threshold per firm fair-lending policy
    lda_required: true
    lda_method: >
      Feature-removal sweep on the alternative-data feature buckets that the
      model card notes as moderately correlated with protected-class proxies;
      threshold-adjustment search across approval cutoffs that hold approval
      volume constant; alternative-model class trial (gradient-boosted vs.
      monotonic-constraint variant). Document rejected alternatives per the
      bureau's AI-circular expectation.
    owner: fintech-fair-lending-analyst
    reviewer: sponsor-bank-fair-lending-officer
    due_date: 2026-09-30
    escalation_path: Sponsor-Bank Fair Lending Committee; fintech AI Risk Committee (joint read)

  - test_id: FL-T-02
    test_type: regression-pricing
    decision_point: pricing
    hypothesis: >
      Approved-loan APR does not vary by prohibited basis after controlling
      for credit and program-eligible covariates.
    method: >
      OLS regression of APR on prohibited-basis indicators with controls
      for credit-score band, model-score band, term, loan amount, channel,
      and origination month. Robust standard errors clustered by program
      partner where applicable.
    demographic_proxy_method: BISG
    statistical_threshold: p < 0.05 on prohibited-basis coefficients
    lda_required: true
    lda_method: >
      Pricing-tier threshold sweep on the model-driven tier boundaries;
      alternative pricing function (linear vs. step) trial.
    owner: fintech-fair-lending-statistician
    reviewer: sponsor-bank-fair-lending-officer
    due_date: 2026-09-30
    escalation_path: Sponsor-Bank Fair Lending Committee

  - test_id: FL-T-03
    test_type: marketing-distribution
    decision_point: marketing
    hypothesis: >
      Digital-channel impression and click-through distribution is not skewed
      against prohibited-basis populations relative to the addressable
      US-adult population in the program footprint.
    method: >
      Audience-skew test on the lookalike-model audience and on the served
      impression set. Compare to addressable-population baseline. Cross-check
      against the platform's privacy-and-targeting controls (cross-reference
      marketing-claim-review).
    demographic_proxy_method: geocoded
    data_required:
      - {field: ad-audience-definition-and-spend, system_of_record: ad-platform-export, owner: marketing-ops, gap_flag: partial}
      - {field: served-impression-and-click-data, system_of_record: ad-platform-export, owner: marketing-ops, gap_flag: partial}
    statistical_threshold: standardized-mean-difference > 0.20
    lda_required: true
    lda_method: Audience-feature removal on lookalike inputs that correlate with protected-class proxies.
    owner: fintech-marketing-compliance
    reviewer: sponsor-bank-fair-lending-officer
    due_date: 2026-09-30
    escalation_path: Sponsor-Bank Fair Lending Committee

  - test_id: FL-T-04
    test_type: model-feature-review
    decision_point: underwriting
    hypothesis: >
      No model feature in PL-UW-SCORE-v4 functions as a proxy for a
      prohibited basis under Reg B 1002.6 effects-test framing.
    method: >
      Per-feature correlation with BISG-derived protected-class proxies;
      Reg B 1002.6 effects-test analysis on features flagged with elevated
      correlation; counsel review of any feature that survives the
      effects-test screen.
    demographic_proxy_method: BISG
    lda_required: true
    lda_method: Per-feature removal where effects-test screen surfaces a flag.
    owner: fintech-fair-lending-analyst
    reviewer: sponsor-bank-fair-lending-officer
    due_date: 2026-08-30
    escalation_path: Sponsor-Bank Fair Lending Committee; fintech AI Risk Committee

  - test_id: FL-T-05
    test_type: comparative-file-review
    decision_point: adverse-action
    hypothesis: >
      Adverse-action notices issued to declined prohibited-basis applicants
      reflect specific and accurate reasons under Reg B 1002.9 and the
      bureau's AI-circular standard.
    method: >
      Sample of declined applications; pull the model-score, the feature-
      contribution explanation passed to the adverse-action engine, and the
      issued notice; compare against the model card's documented reasoning
      method. Cross-reference adverse-action-review.
    demographic_proxy_method: BISG
    sample_size: 100
    lda_required: false
    owner: fintech-compliance-analyst
    reviewer: sponsor-bank-consumer-compliance-officer
    due_date: 2026-08-30
    escalation_path: Sponsor-Bank Consumer Compliance Committee

controls_hypothesis:
  - Pre-prod model gate (sponsor-bank model-risk sign-off and AI risk committee read)
  - Marketing-audience approval gate (sponsor-bank consumer-compliance review)
  - Adverse-action notice template review per Reg B 1002.9

committee_approval_gate:
  committee: Sponsor-Bank Fair Lending Committee (joint with fintech AI Risk Committee)
  approval_criteria:
    - LDA testing is included for every test where an AI/ML model drives the decision
    - demographic-proxy method per test is justified (BISG with caveats; geocoded for marketing)
    - sponsor-bank fair-lending duty under the program agreement is reflected in test ownership and review
    - privilege posture confirmed by sponsor-bank counsel
  approval_status: draft

legal_privilege_posture: attorney-client-privileged

reporting_plan:
  test_result_memo: true
  fair_lending_committee_deck: true
  regulator_ready_summary: true
  board_ras_breach_trigger: true

open_questions:
  - Sponsor-bank counsel to confirm whether the LDA-search work product is filed under the program agreement's joint-defense framework.
  - Whether the lookalike model's vendor will provide the audience-feature documentation required for FL-T-03 LDA work; if not, FL-T-03 lda_method may need to narrow.
  - Whether the model card for PL-UW-SCORE-v4 needs a refresh before the test cycle to reflect the v4.2.1 release notes.

assumptions_and_dependencies:
  - Sponsor-bank counsel directs the fair-lending review; privilege posture as marked.
  - BISG accuracy is sufficient for the program footprint; high-uncertainty subset is handled per FL-T-01 caveat.
  - Model card MC-PL-UW-SCORE-v4 is the operative governance artifact for the in-scope underwriting model.

confidence_label: medium
```

## What this plan does and does not do

The plan operationalizes the risk-assessment finding for the program. It does not finalize a fair-lending determination, take any model out of production, change any adverse-action notice, or trigger any external action. The Sponsor-Bank Fair Lending Committee approves the plan with the fintech AI Risk Committee in joint read; the analytics teams run the tests; the resulting memos return to the committee under privilege.

The LDA testing is mandatory because the underwriting, pricing, and marketing-targeting models are AI/ML. The bureau's expectation under CFPB Circular 2023-03 and the April 2023 Joint Statement is that creditors using AI or complex models actively look for less-discriminatory alternatives; the plan's LDA blocks make that search visible and documented.

Pattern derived from public CFPB and FTC algorithmic-discrimination enforcement themes and from the public CFPB Circulars on AI / complex models in adverse action. No named institution is implied; the program-bank / fintech split is the structural pattern, not a specific firm.
