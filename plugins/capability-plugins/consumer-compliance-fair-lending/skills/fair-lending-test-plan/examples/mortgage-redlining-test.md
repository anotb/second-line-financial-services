# Example: mortgage redlining test plan for a regional bank

## Input

A $40B regional bank operates across six MSAs in the mid-Atlantic. The annual fair-lending risk assessment flagged two MSAs as outliers on origination distribution relative to peer aggregate HMDA, and complaint themes for the prior 18 months show a cluster of access-and-information complaints in majority-minority census tracts in those same MSAs. Source posture is public-plus-firm-policy-plus-evidence; the bank's HMDA LAR, branch and LO geographic data, and marketing-spend ledger are available. The CCO and the head of fair lending are jointly sponsoring the plan; outside counsel directs the work for privilege.

## Why this scenario matters

This is the canonical DOJ Combatting Redlining Initiative pattern: peer-comparison HMDA outliers plus complaint signals plus geographic distribution data. The plan has to set comparator selection (peer set, MSA scoping), evidence sources for marketing and branch distribution, and the boundary between the redlining test and the comparative file review of the underwriting decisions inside those MSAs. Privilege posture is load-bearing because outside counsel is directing.

## Output sketch

```yaml
plan_id: FL-PLAN-2026-MTG-RDL-01
risk_assessment_ref: FL-RA-2026-Q1
trigger: complaint-theme-trigger
as_of_date: 2026-05-06

scope:
  products: [first-lien-mortgage-purchase, first-lien-mortgage-refi]
  decision_points: [marketing, underwriting, pricing]
  period: {start: 2024-01-01, end: 2025-12-31}
  geographies: [MSA-A, MSA-B]
  channels: [branch, digital, broker]
  exclusions:
    - HELOC (separate plan)
    - Servicing and loss mitigation (separate plan)
    - Non-HMDA-reportable closed-end home-improvement loans
prohibited_bases_tested: [race, ethnicity, national-origin]

model_inventory_in_scope: []  # judgmental underwriting; no AI/ML model in path

tests:
  - test_id: FL-T-01
    test_type: redlining
    decision_point: marketing
    hypothesis: >
      Marketing spend and tracked-impression distribution in MSA-A and MSA-B
      are not lower in majority-minority census tracts than in the rest of the
      MSA after controlling for tract owner-occupancy and median-home-value bands.
    method: >
      Tract-level comparison of marketing spend and impression counts against
      HMDA-eligible owner-occupied unit counts. Peer aggregate HMDA from FFIEC
      for comparator. Matched-MSA selection per Interagency Fair Lending
      Examination Procedures. Branch and LO geographic distribution overlay.
    demographic_proxy_method: geocoded
    demographic_proxy_caveats: >
      Tract demographics from ACS 5-year are stable but lag; flag for any tract
      where ACS vintage misaligns with marketing window.
    data_required:
      - {field: marketing-spend-by-tract, system_of_record: marketing-spend-ledger, owner: marketing-ops, gap_flag: available}
      - {field: branch-and-LO-locations, system_of_record: HR-and-facilities-system, owner: hr-ops, gap_flag: available}
      - {field: HMDA-LAR-2024-2025, system_of_record: HMDA-platform, owner: HMDA-team, gap_flag: available}
    statistical_threshold: standardized-mean-difference > 0.20 with statistical-significance p < 0.05
    lda_required: false
    owner: fair-lending-analyst
    reviewer: head-of-fair-lending
    due_date: 2026-07-15
    escalation_path: Fair Lending Committee

  - test_id: FL-T-02
    test_type: comparative-file-review
    decision_point: underwriting
    hypothesis: >
      Within MSA-A and MSA-B, denial outcomes for prohibited-basis applicants
      are not different from outcomes for similarly-situated control-group
      applicants matched on credit, DTI, LTV, and AUS recommendation.
    method: >
      Matched-pair comparative file review per Interagency Fair Lending
      Examination Procedures. Sample frame: denied applications for
      prohibited-basis applicants in MSA-A and MSA-B in the period; matched
      to approved control-group applicants on credit-score band, DTI band,
      LTV band, AUS recommendation, and product. Override and exception
      decisions read against the credit policy in effect on the decision date.
    demographic_proxy_method: self-reported-HMDA
    sample_size: 200
    data_required:
      - {field: HMDA-LAR-with-applicant-demographics, system_of_record: HMDA-platform, owner: HMDA-team, gap_flag: available}
      - {field: underwriting-narrative-and-exception-log, system_of_record: LOS, owner: mortgage-credit-ops, gap_flag: partial}
      - {field: AUS-output, system_of_record: GSE-AUS-feed, owner: secondary-marketing, gap_flag: available}
    statistical_threshold: per-pair difference review with documented exception coding
    lda_required: false
    owner: fair-lending-analyst
    reviewer: head-of-fair-lending
    due_date: 2026-08-15
    escalation_path: Fair Lending Committee

  - test_id: FL-T-03
    test_type: regression-pricing
    decision_point: pricing
    hypothesis: >
      For first-lien purchase originations in MSA-A and MSA-B, rate spread
      (Reg C) does not vary by prohibited basis after controlling for
      credit-relevant covariates.
    method: >
      OLS regression of rate spread on prohibited-basis indicators with
      controls for credit-score band, LTV band, DTI band, loan amount, lien
      status, occupancy, AUS recommendation, lock period, channel, and
      origination month. Robust standard errors clustered by LO.
    demographic_proxy_method: self-reported-HMDA
    statistical_threshold: p < 0.05 on prohibited-basis coefficients
    lda_required: false
    owner: fair-lending-statistician
    reviewer: head-of-fair-lending
    due_date: 2026-08-15
    escalation_path: Fair Lending Committee

controls_hypothesis:
  - Pricing-exception log review (LO-level deviations)
  - Override review on judgmental denials
  - Marketing-channel approval gate (first-line marketing review)

committee_approval_gate:
  committee: Fair Lending Committee
  approval_criteria:
    - scope and out-of-scope items align to risk-assessment outliers
    - LDA testing is not required because no AI/ML model is in path
    - privilege posture confirmed by counsel
  approval_status: draft

legal_privilege_posture: attorney-client-privileged

reporting_plan:
  test_result_memo: true
  fair_lending_committee_deck: true
  regulator_ready_summary: false
  board_ras_breach_trigger: true

open_questions:
  - Whether to extend MSA-B sample to include 2023 originations to align with the most recent peer HMDA aggregate vintage.
  - Whether the LO-channel steering test (separate plan) should run concurrently to support a joint committee read.

assumptions_and_dependencies:
  - Outside counsel directs the work for the duration; privilege posture as marked.
  - HMDA platform exports include the applicant-demographics fields at the resolution required.
  - Risk-assessment outlier finding remains operative through plan execution.

confidence_label: high
```

## What this plan does and does not do

The plan operationalizes the risk-assessment finding for the two flagged MSAs. It does not finalize a redlining determination, run the regression, or trigger any external action. The Fair Lending Committee approves the plan; the analytics team runs the tests; the resulting test memos return to the committee under privilege; counsel decides on any external posture.

Pattern derived from public DOJ Combatting Redlining Initiative consent orders and the Interagency Fair Lending Examination Procedures comparator-MSA methodology.
