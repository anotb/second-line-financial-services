# Example: XGBoost personal-loan decline sample

## Input description

A regional bank uses an XGBoost-based credit decisioning model for unsecured personal loans. The adverse-action notice template draws reasons from a fixed list of twenty FCRA-style reason codes mapped to feature buckets. The consumer compliance second-line samples 200 declines from the prior quarter for review under §1002.9, with attention to the CFPB Circulars 2022-03 and 2023-03 on AI / complex-model specificity and accuracy. Sector overlay: banking. Cross-cutting overlay: privacy.

## Output sketch

The memo opens with the population (200 declines, Q3, unsecured personal loan, random sample within the focal product). The §1002.9 timing-compliance panel returns clean (29 days median, no breaches of the 30-day clock).

The §1002.9 content-compliance panel returns two material defect patterns:

- 18% of notices cite "length of credit history" as one of the principal reasons. The model's per-decision SHAP contributions for those 36 decisions are dominated by debt-to-income ratio and recent inquiries; "length of credit history" is in the top five contributions for only 4 of the 36. Defect type: sample-form-substitution under Circular 2023-03 — the cited reason does not reflect the principal reasons actually relied upon.
- 6% of notices cite "value of collateral" on a product that has no collateral. The reason-code dictionary maps a feature bucket to the collateral sample-form code that does not apply to unsecured products. Defect type: impossible-mapping. This is a notice-template defect that produces inaccurate notices regardless of the underlying model.

The AI / complex-model findings section anchors the sample-form-substitution defect to Circular 2023-03 and the impossible-mapping defect to the Staff Commentary specificity standard (the cited reason is not accurate). The disparate-impact panel runs descriptive decline-rate disparity by BISG-derived race / ethnicity (BISG caveat applied) and surfaces a 2.1x decline-rate disparity for one cohort that warrants formal fair-lending testing — flagged and routed to `fair-lending-test-plan`, not produced as a finding here.

Recommended actions:

1. Notice re-issuance for the 12 decisions in the impossible-mapping subset (collateral cited on unsecured product). Owner: consumer compliance second-line. Control: notice template release control. Due: 30 days. Counsel reviews re-issuance language.
2. Model reason-generation fix: realign the reason-code dictionary so the model's top-N feature contributions map to accurate reason codes, and add a release-gate check that flags impossible mappings before deployment. Owner: model risk; first line is the underwriting model owner. Control: model release control. Due: next model release cycle.
3. Notice re-issuance review for the 36 decisions in the sample-form-substitution subset, with counsel direction on whether re-issuance is required versus disclosed in remediation. Owner: counsel + consumer compliance second-line.
4. Fair-lending escalation on the 2.1x cohort decline-rate disparity to `fair-lending-test-plan` for formal regression. Owner: fair-lending lead. Cross-route to MRM committee.
5. Privacy-team check on the per-decision SHAP feature contribution data classification (model IP + applicant attributes); confirm review-workflow data handling. Owner: privacy team.

The memo closes with three open questions for counsel (re-issuance scope, customer-communication language, regulator-engagement posture if a CFPB inquiry is anticipated) and the source-trace table tying each material claim back to §1002.9, the Staff Commentary, the two CFPB Circulars, and the bank's MRM model card.

## Why this scenario matters

It exercises the seam between Reg B specificity (Staff Commentary), AI / complex-model accuracy (CFPB Circular 2023-03), and the model-card / explainability fabric (SR 11-7 / OCC Bulletin 2026-13). It produces the two recurring defect types — sample-form-substitution and impossible-mapping — and shows how the artifact recommends action without finalizing any customer-facing change. It also shows the routing pattern to `fair-lending-test-plan` for the disparate-impact signal: the adverse-action review surfaces the red flag, the formal test produces the finding.

Pattern derived from public CFPB enforcement themes on adverse-action notices using complex models. No named institution.
