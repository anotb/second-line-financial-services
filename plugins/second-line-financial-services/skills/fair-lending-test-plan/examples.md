# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## algorithmic-underwriting-test

### Example: algorithmic-underwriting test plan for a fintech consumer-credit platform

#### Input

A fintech personal-loan platform operates with a sponsor bank under a marketing and program-management arrangement. The platform underwrites with an in-house ML scoring model that consumes traditional credit features plus alternative data (cash-flow signals from a permissioned bank-data connection, employment-tenure inferred from payroll-data integration, device and behavioral signals from the application session). The model has a current model card and was last validated 11 months ago. Complaint themes for the prior six months include adverse-action notices that recipients found vague (the §1002.9 specificity angle on AI/complex-model adverse-action accuracy is in scope; CFPB Circular 2023-03 informed earlier framing but was withdrawn May 12, 2025). The fair-lending team is the program-bank's second-line; the fintech's compliance team is the program-operator first-line. Source posture is public-plus-firm-policy-plus-evidence; sponsor-bank counsel directs.

#### Why this scenario matters

This is the algorithmic-discrimination pattern flagged by the April 2023 Joint Statement and the CFPB AI circulars. The plan must include less-discriminatory-alternative testing because an AI/ML model drives the underwriting decision. The plan also has to deal with the bank-fintech split: where sponsor-bank duty sits, where program-operator duty sits, what the contract-of-record (program agreement) says about second-line review and remediation. The marketing-funnel skew test is not optional; protected-class targeting can happen pre-application.

#### Output sketch

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

#### What this plan does and does not do

The plan operationalizes the risk-assessment finding for the program. It does not finalize a fair-lending determination, take any model out of production, change any adverse-action notice, or trigger any external action. The Sponsor-Bank Fair Lending Committee approves the plan with the fintech AI Risk Committee in joint read; the analytics teams run the tests; the resulting memos return to the committee under privilege.

The LDA testing is mandatory because the underwriting, pricing, and marketing-targeting models are AI/ML. The April 2023 Joint Statement's expectation that creditors using AI or complex models actively look for less-discriminatory alternatives stands on its own anchors; CFPB Circular 2023-03 reinforced the point but was withdrawn May 12, 2025. The plan's LDA blocks make that search visible and documented regardless.

Pattern derived from public CFPB and FTC algorithmic-discrimination enforcement themes and from the public CFPB Circulars on AI / complex models in adverse action. No named institution is implied; the program-bank / fintech split is the structural pattern, not a specific firm.

## mortgage-redlining-test

### Example: mortgage redlining test plan for a regional bank

#### Input

A $40B regional bank operates across six MSAs in the mid-Atlantic. The annual fair-lending risk assessment flagged two MSAs as outliers on origination distribution relative to peer aggregate HMDA, and complaint themes for the prior 18 months show a cluster of access-and-information complaints in majority-minority census tracts in those same MSAs. Source posture is public-plus-firm-policy-plus-evidence; the bank's HMDA LAR, branch and LO geographic data, and marketing-spend ledger are available. The CCO and the head of fair lending are jointly sponsoring the plan; outside counsel directs the work for privilege.

#### Why this scenario matters

This is the canonical DOJ Combatting Redlining Initiative pattern: peer-comparison HMDA outliers plus complaint signals plus geographic distribution data. The plan has to set comparator selection (peer set, MSA scoping), evidence sources for marketing and branch distribution, and the boundary between the redlining test and the comparative file review of the underwriting decisions inside those MSAs. Privilege posture is load-bearing because outside counsel is directing.

#### Output sketch

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

#### What this plan does and does not do

The plan operationalizes the risk-assessment finding for the two flagged MSAs. It does not finalize a redlining determination, run the regression, or trigger any external action. The Fair Lending Committee approves the plan; the analytics team runs the tests; the resulting test memos return to the committee under privilege; counsel decides on any external posture.

Pattern derived from public DOJ Combatting Redlining Initiative consent orders and the Interagency Fair Lending Examination Procedures comparator-MSA methodology.

## troubleshooting

### Troubleshooting: fair-lending-test-plan

Recurring failure modes when a fair-lending test plan looks complete but is not. The drafter should preempt these; the fair-lending-committee reviewer should catch the rest.

#### The plan lists test types without specifying any of them

Symptom: the plan names "regression on underwriting", "comparative file review", "redlining test" as line items, with no model specification, no sample-size calculation, no covariate list, no statistical-significance threshold, no data-source pointers. A regression with no model spec is not a plan; it is a topic.

Why it happens: the drafter mistook a checklist of test types for a plan. Common at first-cycle stage and on plan refresh where the prior plan was inherited and never re-specified.

Fix: every entry in `tests[]` must include `method`, `data_required[]`, `statistical_threshold`, and `owner`. A test entry that fails any of these on intake is not yet a test; surface it as an open question in `open_questions[]` instead of carrying it as a planned test.

#### The demographic proxy method is defaulted across the plan

Symptom: every test in the plan uses BISG, including the mortgage tests. Or the plan does not record the proxy method at all.

Why it happens: BISG is the dominant non-mortgage proxy method and the drafter applied it without thinking through where stronger evidence is available. Mortgage uses HMDA self-reported demographics under §1002.13; small-business under §1071 uses the §1071 self-reported demographics where the operative compliance dates apply.

Fix: schema requires `tests[].demographic_proxy_method` per test, with a justification. Defaulting to BISG on mortgage tests when HMDA is available is a reviewer flag.

#### AI/ML in the path, no LDA search in the plan

Symptom: the model inventory in scope includes one or more AI/ML models, the plan covers underwriting and pricing, and the plan has no LDA search blocks.

Why it happens: the drafter built the plan from a non-AI template and did not load the AI overlay; or treated LDA as optional polish. The CFPB Circulars (2022-03 and 2023-03) and the April 2023 Joint Statement frame LDA search as the bureau's expectation for creditors using complex models.

Fix: when `model_inventory_in_scope[].ai_ml` is true on any model in path for a tested decision, `tests[].lda_required` must be true on the corresponding test, and `tests[].lda_method` is populated. Document rejected alternatives.

#### The plan covers underwriting only, ignoring marketing and steering

Symptom: scope is limited to underwriting and pricing. Marketing distribution, steering, and adverse-action review are absent.

Why it happens: underwriting is the historical center of fair-lending testing; marketing and steering are operationally less mature. But they are decision points before underwriting where redlining-equivalent harm and protected-class targeting also live.

Fix: scope must explicitly cover marketing and steering where the institution operates in those layers. Where the in-scope products use digital-channel acquisition, marketing-distribution testing is non-optional. Where LO incentives or product-placement design exist, steering review is in scope.

#### The plan has no legal-privilege posture

Symptom: `legal_privilege_posture` field is blank or marked `n/a`.

Why it happens: the drafter treated privilege as a counsel decision to be made later; or treated the test plan as a routine compliance artifact that does not need a privilege posture.

Fix: privilege posture is a basic discipline for the test plan; the field is mandatory. Record `attorney-client-privileged`, `attorney-work-product`, `not privileged`, or `tbd-counsel-direction-pending`. If counsel has not yet directed, surface the question to counsel before plan finalization, not after the test memos land.

#### Committee approval gate is missing

Symptom: the plan is fully drafted, the tests are well-specified, and there is no record of which committee approves the plan or what the approval criteria are.

Why it happens: the drafter treated the plan as the work product itself rather than as the input to a committee approval gate. The plan that is never approved is the plan that is never run.

Fix: `committee_approval_gate.committee` and `committee_approval_gate.approval_criteria[]` are mandatory. The plan is in `draft` status until the committee approves; the test execution does not begin until the gate clears.

#### Servicing and loss-mit absent without a justification

Symptom: scope covers originations only. Servicing and loss-mit are absent and the plan does not record why.

Why it happens: the operational maturity of servicing fair-lending testing is uneven and the drafter excluded the area by default rather than by assessment.

Fix: scope-exclusion entries are recorded with a reason. "Servicing and loss-mit covered under separate plan" or "Servicing and loss-mit out of scope this cycle per fair-lending committee direction; included in next-cycle plan" is acceptable; unexplained absence is not.

#### The plan is the determination

Symptom: the plan reads like it has already concluded that no fair-lending issues exist; or the plan reads like it has already concluded that issues exist. Either is a failure mode.

Why it happens: drafter conflated the plan with the test result. The plan is the operational specification; the result lives in the test memos and the committee read.

Fix: the plan states hypotheses to be tested, methods to test them, and thresholds for what would constitute a finding. It does not pre-decide the result. Where complaint themes or risk-assessment outliers indicate likely findings, record them in scope-trigger and assumption fields, not in the test outcome.

#### Source-trace and confidence label absent

Symptom: the plan cites no sources for the methodological choices it makes. Statistical thresholds appear without basis; sample sizes appear without rationale.

Why it happens: the drafter borrowed methodology from prior plans or from external references without recording the source.

Fix: methodology choices that derive from FFIEC procedures, the Interagency Fair Lending Examination Procedures, the CFPB circulars, or the firm's own fair-lending policy carry source pointers. The confidence label at the end of the plan reflects how well the plan can support the committee approval decision.

#### Sponsor-bank arrangement treated as a footnote

Symptom: the plan covers a sponsor-bank fintech program and lists the sponsor bank as a passive recipient of test results rather than as the accountable creditor of record.

Why it happens: the drafter is operating from the program-operator's perspective and treating sponsor-bank involvement as administrative.

Fix: where the institution is a sponsor-bank-program operator, the sponsor bank is the creditor of record under most arrangements and the bank's fair-lending program owns second-line review. The plan reflects joint ownership, joint approval, and a clear statement of which entity carries which duty.

#### Plan ignores the model card on AI/ML models in path

Symptom: the model inventory in scope lists AI/ML models with version IDs but the plan does not cite the corresponding model cards; or the plan tests a hypothesis that contradicts what the model card states without acknowledging the conflict.

Why it happens: the drafter built the plan in isolation from the model risk machinery.

Fix: the model card and the fair-lending test plan are mutually-referencing artifacts. The plan cites `card_reference` per in-scope model and reads the card before specifying the per-feature review and the LDA search. Where the plan stresses a card-stated assumption (e.g., the card claims a feature is not protected-class-correlated and the plan tests that claim), the plan records the relationship explicitly.
