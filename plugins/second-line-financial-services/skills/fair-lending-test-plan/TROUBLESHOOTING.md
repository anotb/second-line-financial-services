# Troubleshooting: fair-lending-test-plan

Recurring failure modes when a fair-lending test plan looks complete but is not. The drafter should preempt these; the fair-lending-committee reviewer should catch the rest.

## The plan lists test types without specifying any of them

Symptom: the plan names "regression on underwriting", "comparative file review", "redlining test" as line items, with no model specification, no sample-size calculation, no covariate list, no statistical-significance threshold, no data-source pointers. A regression with no model spec is not a plan; it is a topic.

Why it happens: the drafter mistook a checklist of test types for a plan. Common at first-cycle stage and on plan refresh where the prior plan was inherited and never re-specified.

Fix: every entry in `tests[]` must include `method`, `data_required[]`, `statistical_threshold`, and `owner`. A test entry that fails any of these on intake is not yet a test; surface it as an open question in `open_questions[]` instead of carrying it as a planned test.

## The demographic proxy method is defaulted across the plan

Symptom: every test in the plan uses BISG, including the mortgage tests. Or the plan does not record the proxy method at all.

Why it happens: BISG is the dominant non-mortgage proxy method and the drafter applied it without thinking through where stronger evidence is available. Mortgage uses HMDA self-reported demographics under §1002.13; small-business under §1071 uses the §1071 self-reported demographics where the operative compliance dates apply.

Fix: schema requires `tests[].demographic_proxy_method` per test, with a justification. Defaulting to BISG on mortgage tests when HMDA is available is a reviewer flag.

## AI/ML in the path, no LDA search in the plan

Symptom: the model inventory in scope includes one or more AI/ML models, the plan covers underwriting and pricing, and the plan has no LDA search blocks.

Why it happens: the drafter built the plan from a non-AI template and did not load the AI overlay; or treated LDA as optional polish. The CFPB Circulars (2022-03 and 2023-03) and the April 2023 Joint Statement frame LDA search as the bureau's expectation for creditors using complex models.

Fix: when `model_inventory_in_scope[].ai_ml` is true on any model in path for a tested decision, `tests[].lda_required` must be true on the corresponding test, and `tests[].lda_method` is populated. Document rejected alternatives.

## The plan covers underwriting only, ignoring marketing and steering

Symptom: scope is limited to underwriting and pricing. Marketing distribution, steering, and adverse-action review are absent.

Why it happens: underwriting is the historical center of fair-lending testing; marketing and steering are operationally less mature. But they are decision points before underwriting where redlining-equivalent harm and protected-class targeting also live.

Fix: scope must explicitly cover marketing and steering where the institution operates in those layers. Where the in-scope products use digital-channel acquisition, marketing-distribution testing is non-optional. Where LO incentives or product-placement design exist, steering review is in scope.

## The plan has no legal-privilege posture

Symptom: `legal_privilege_posture` field is blank or marked `n/a`.

Why it happens: the drafter treated privilege as a counsel decision to be made later; or treated the test plan as a routine compliance artifact that does not need a privilege posture.

Fix: privilege posture is a basic discipline for the test plan; the field is mandatory. Record `attorney-client-privileged`, `attorney-work-product`, `not privileged`, or `tbd-counsel-direction-pending`. If counsel has not yet directed, surface the question to counsel before plan finalization, not after the test memos land.

## Committee approval gate is missing

Symptom: the plan is fully drafted, the tests are well-specified, and there is no record of which committee approves the plan or what the approval criteria are.

Why it happens: the drafter treated the plan as the work product itself rather than as the input to a committee approval gate. The plan that is never approved is the plan that is never run.

Fix: `committee_approval_gate.committee` and `committee_approval_gate.approval_criteria[]` are mandatory. The plan is in `draft` status until the committee approves; the test execution does not begin until the gate clears.

## Servicing and loss-mit absent without a justification

Symptom: scope covers originations only. Servicing and loss-mit are absent and the plan does not record why.

Why it happens: the operational maturity of servicing fair-lending testing is uneven and the drafter excluded the area by default rather than by assessment.

Fix: scope-exclusion entries are recorded with a reason. "Servicing and loss-mit covered under separate plan" or "Servicing and loss-mit out of scope this cycle per fair-lending committee direction; included in next-cycle plan" is acceptable; unexplained absence is not.

## The plan is the determination

Symptom: the plan reads like it has already concluded that no fair-lending issues exist; or the plan reads like it has already concluded that issues exist. Either is a failure mode.

Why it happens: drafter conflated the plan with the test result. The plan is the operational specification; the result lives in the test memos and the committee read.

Fix: the plan states hypotheses to be tested, methods to test them, and thresholds for what would constitute a finding. It does not pre-decide the result. Where complaint themes or risk-assessment outliers indicate likely findings, record them in scope-trigger and assumption fields, not in the test outcome.

## Source-trace and confidence label absent

Symptom: the plan cites no sources for the methodological choices it makes. Statistical thresholds appear without basis; sample sizes appear without rationale.

Why it happens: the drafter borrowed methodology from prior plans or from external references without recording the source.

Fix: methodology choices that derive from FFIEC procedures, the Interagency Fair Lending Examination Procedures, the CFPB circulars, or the firm's own fair-lending policy carry source pointers. The confidence label at the end of the plan reflects how well the plan can support the committee approval decision.

## Sponsor-bank arrangement treated as a footnote

Symptom: the plan covers a sponsor-bank fintech program and lists the sponsor bank as a passive recipient of test results rather than as the accountable creditor of record.

Why it happens: the drafter is operating from the program-operator's perspective and treating sponsor-bank involvement as administrative.

Fix: where the institution is a sponsor-bank-program operator, the sponsor bank is the creditor of record under most arrangements and the bank's fair-lending program owns second-line review. The plan reflects joint ownership, joint approval, and a clear statement of which entity carries which duty.

## Plan ignores the model card on AI/ML models in path

Symptom: the model inventory in scope lists AI/ML models with version IDs but the plan does not cite the corresponding model cards; or the plan tests a hypothesis that contradicts what the model card states without acknowledging the conflict.

Why it happens: the drafter built the plan in isolation from the model risk machinery.

Fix: the model card and the fair-lending test plan are mutually-referencing artifacts. The plan cites `card_reference` per in-scope model and reads the card before specifying the per-feature review and the LDA search. Where the plan stresses a card-stated assumption (e.g., the card claims a feature is not protected-class-correlated and the plan tests that claim), the plan records the relationship explicitly.
