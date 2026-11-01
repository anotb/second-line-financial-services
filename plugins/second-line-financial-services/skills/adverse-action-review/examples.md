# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## mortgage-decline-redlining-flag

### Example: HMDA-reportable mortgage decline review with redlining flag

#### Input description

A national bank's mortgage origination platform issued adverse-action notices on 1,400 declined HMDA-reportable applications in the prior quarter. The fair-lending lead asks for a §1002.9 review of the population, with the disparate-impact panel using HMDA self-reported demographics rather than BISG (mortgage product, self-reported demographics available under §1002.13). Sector overlay: banking. Cross-cutting overlay: privacy.

#### Output sketch

Population panel records 1,400 declines, prior quarter, HMDA-reportable mortgage (first-lien purchase, refi, junior-lien refi, home-improvement, HELOC), with the §1002.2(c) action category split (1,180 outright denials, 145 counteroffers not accepted, 75 incomplete-application notices). Sample frame is 100% review on counteroffers and incompletes (smaller populations, higher defect rate historically), 200-decision random sample on outright denials.

The §1002.9 timing-compliance panel surfaces nine decisions where the notice was sent on day 33 from the completed-application date (clean breach of the 30-day clock under §1002.9(a)(1)). Evidence trail traces the breach to an LOS routing defect that occurred during a system upgrade. All nine are in the review's outright-denial subset.

The §1002.9 content-compliance panel surfaces a recurring "credit application incomplete" reason cited on 22 decisions where the application was actually complete (notice template defect; the §1002.9(c) incomplete-application clock was applied where it should not have been). The Staff Commentary on specificity treats this as a content defect because the cited reason is not accurate. Notices for those 22 decisions are non-compliant.

The disparate-impact panel uses HMDA self-reported demographics directly. The decline-rate disparity for one MSA is 4.2x the institution's footprint average for the protected-class cohort, with marketing-distribution evidence showing thin branch coverage and minimal direct-mail volume to majority-minority census tracts within the MSA. The pattern matches DOJ Combatting Redlining Initiative consent-order patterns; the panel surfaces this as a redlining red flag, applies the BISG caveat where BISG-only segments were also analyzed, and routes the finding-grade work to `fair-lending-test-plan` and the bank's CRA officer (the MSA overlaps the bank's CRA assessment area).

The AI / complex-model findings section is short: the underlying mortgage AUS uses Desktop Underwriter, not an internal AI / ML model, so the Circulars 2022-03 / 2023-03 framing applies narrowly to the AUS-deny pass-through pattern (which the bureau has flagged supervisorily) and to the bank's own override layer. The memo records the AUS-recommendation field as a control covariate for any subsequent regression but flags that AUS-recommendation is itself in the fair-lending perimeter per the banking sector overlay.

Recommended actions:

1. Notice re-issuance on the nine timing breaches with counsel-reviewed language. Owner: consumer compliance second-line. Control: notice issuance control. Due: 14 days.
2. Notice re-issuance on the 22 content defects (incomplete-application reason cited on complete applications) with counsel-reviewed language. Owner: consumer compliance second-line. Due: 30 days.
3. LOS routing-defect remediation that produced the timing breaches. Owner: mortgage operations. Control: LOS notice-trigger control. Due: per IT release cycle, with interim manual control.
4. Fair-lending escalation on the 4.2x MSA disparity to `fair-lending-test-plan` for regression and comparative file review; CRA officer coordination given assessment-area overlap. Owner: fair-lending lead + CRA officer. Cross-route: fair-lending committee.
5. Comparative file review on the override layer where the AUS-recommendation pass-through pattern is in scope. Owner: fair-lending statistician.

The memo closes with two open questions for counsel (DOJ Combatting Redlining Initiative posture given the MSA disparity; whether voluntary regulator engagement is appropriate in advance of formal testing) and the source-trace table tying each claim to §1002.9, the Staff Commentary, FHA §3605, the FFIEC Interagency Fair Lending Examination Procedures, and the DOJ initiative.

#### Why this scenario matters

It exercises the dwelling-secured perimeter (FHA + ECOA) where HMDA self-reported demographics are the right proxy choice rather than BISG. It produces the timing-breach pattern (most common §1002.9 defect) and the inaccurate-reason pattern (where the §1002.9(c) clock was misapplied). It also shows how the disparate-impact panel surfaces a redlining red flag that routes to fair-lending testing and CRA coordination; the adverse-action review is the most common entry point to a redlining finding, but the finding follows the formal test.

Pattern derived from public CFPB / DOJ redlining consent-order themes. No named institution.

## xgboost-personal-loan-decline-sample

### Example: XGBoost personal-loan decline sample

#### Input description

A regional bank uses an XGBoost-based credit decisioning model for unsecured personal loans. The adverse-action notice template draws reasons from a fixed list of twenty FCRA-style reason codes mapped to feature buckets. The consumer compliance second-line samples 200 declines from the prior quarter for review under §1002.9, with attention to the CFPB Circulars 2022-03 and 2023-03 on AI / complex-model specificity and accuracy. Sector overlay: banking. Cross-cutting overlay: privacy.

#### Output sketch

The memo opens with the population (200 declines, Q3, unsecured personal loan, random sample within the focal product). The §1002.9 timing-compliance panel returns clean (29 days median, no breaches of the 30-day clock).

The §1002.9 content-compliance panel returns two material defect patterns:

- 18% of notices cite "length of credit history" as one of the principal reasons. The model's per-decision SHAP contributions for those 36 decisions are dominated by debt-to-income ratio and recent inquiries; "length of credit history" is in the top five contributions for only 4 of the 36. Defect type: sample-form-substitution under §1002.9 specificity (formerly captured in Circular 2023-03, withdrawn May 12, 2025; the obligation flows from the regulation and Staff Commentary). The cited reason does not reflect the principal reasons actually relied upon.
- 6% of notices cite "value of collateral" on a product that has no collateral. The reason-code dictionary maps a feature bucket to the collateral sample-form code that does not apply to unsecured products. Defect type: impossible-mapping. This is a notice-template defect that produces inaccurate notices regardless of the underlying model.

The AI / complex-model findings section anchors the sample-form-substitution defect to §1002.9 specificity (Circular 2023-03 informed earlier framing, withdrawn May 12, 2025) and the impossible-mapping defect to the Staff Commentary specificity standard (the cited reason is not accurate). The disparate-impact panel runs descriptive decline-rate disparity by BISG-derived race / ethnicity (BISG caveat applied) and surfaces a 2.1x decline-rate disparity for one cohort that warrants formal fair-lending testing (flagged and routed to `fair-lending-test-plan`, not produced as a finding here).

Recommended actions:

1. Notice re-issuance for the 12 decisions in the impossible-mapping subset (collateral cited on unsecured product). Owner: consumer compliance second-line. Control: notice template release control. Due: 30 days. Counsel reviews re-issuance language.
2. Model reason-generation fix: realign the reason-code dictionary so the model's top-N feature contributions map to accurate reason codes, and add a release-gate check that flags impossible mappings before deployment. Owner: model risk; first line is the underwriting model owner. Control: model release control. Due: next model release cycle.
3. Notice re-issuance review for the 36 decisions in the sample-form-substitution subset, with counsel direction on whether re-issuance is required versus disclosed in remediation. Owner: counsel + consumer compliance second-line.
4. Fair-lending escalation on the 2.1x cohort decline-rate disparity to `fair-lending-test-plan` for formal regression. Owner: fair-lending lead. Cross-route to MRM committee.
5. Privacy-team check on the per-decision SHAP feature contribution data classification (model IP + applicant attributes); confirm review-workflow data handling. Owner: privacy team.

The memo closes with three open questions for counsel (re-issuance scope, customer-communication language, regulator-engagement posture if a CFPB inquiry is anticipated) and the source-trace table tying each material claim back to §1002.9, the Staff Commentary, the now-withdrawn CFPB Circulars (historical reference), and the bank's MRM model card.

#### Why this scenario matters

It exercises the seam between Reg B specificity (Staff Commentary; CFPB Circular 2023-03 was withdrawn May 12, 2025, the obligation survives on the regulation), AI / complex-model accuracy, and the model-card / explainability fabric (SR 11-7 plus OCC Bulletin 2026-13 for traditional models, NIST AI RMF and NIST AI 600-1 for any GenAI / RAG / tool-use / agentic component). It produces the two recurring defect types (sample-form-substitution and impossible-mapping) and shows how the artifact recommends action without finalizing any customer-facing change. It also shows the routing pattern to `fair-lending-test-plan` for the disparate-impact signal: the adverse-action review surfaces the red flag, the formal test produces the finding.

Pattern derived from public CFPB enforcement themes on adverse-action notices using complex models. No named institution.

## troubleshooting

### Troubleshooting: adverse-action-review

Recurring defects in the adverse-action notice review and in the artifact this skill produces. The defects below repeat across engagements; treat the list as a checklist when the artifact is in second-line review.

#### Notice-population scope defects

**Reviewed only outright denials.** §1002.2(c) covers counteroffers not accepted, terms-less-favorable actions, incomplete-application notices, and existing-account adverse changes. A review that names the denial subset only misses populations the regulators expect to see covered. Fix: enumerate the §1002.2(c) action categories in scope on the population panel; if a category is excluded, name the exclusion explicitly with a reason.

**Population framed as "Q3 declines" without the §1002.2(c) action category split.** The action category drives which §1002.9 timing clock applies. Fix: per-decision action category is a population-level field, not an inference; pull it from the decision system.

**Sample frame defaults to random across the whole population.** Risk-based sampling by product, vintage, channel, decision-system version, or notice-template version is often more useful. Fix: name the sample frame and the rationale; default to the focal-product cohort when the engagement has a focal trigger.

#### Timing-compliance defects

**§1002.9(c) incomplete-application clock applied where the application was complete.** Recurring defect; the 90-day clock under §1002.9(c) only applies where the incompleteness was actually flagged to the applicant. Fix: per-decision check that the incompleteness notice was sent before the §1002.9(c) clock is invoked.

**Counteroffer clock applied where there was no counteroffer.** Some systems route a soft-decline pattern (smaller amount, longer tenor) into the counteroffer track without sending the counteroffer notice. Fix: per-decision check that the counteroffer was actually offered to the applicant before the counteroffer-not-accepted clock is invoked.

**"Days elapsed" calculated from the wrong start date.** The §1002.9(a)(1) clock starts when the application is complete, not when the application is received. Fix: the population data must include both received-date and complete-date; the panel uses complete-date.

#### Content-compliance defects

**Sample-form reason selected because it was closest, not because it was the principal reason.** This is the §1002.9 specificity defect (formerly captured in CFPB Circular 2023-03, withdrawn May 12, 2025; the obligation flows from the regulation and the Staff Commentary, not the withdrawn circular). Fix: per-decision evidence that the cited reason is the principal reason actually relied upon (feature contribution score, model output, or named scoring rule).

**Generic statement substituted for specific reason.** "You did not meet our credit standards" or "credit application incomplete" (when the application was complete) are recurring generic-reason-only defects. Fix: per-decision specificity test against the Staff Commentary; generic statements are content failures regardless of whether sample-form reasons are also cited.

**FCRA risk-based pricing notice not sent where a credit score was used in adverse action.** Reg V §1022.74 sets a separate disclosure obligation that survives whether the Reg B notice content is otherwise compliant. Fix: per-decision FCRA-overlay-applicable flag and a content-compliance check on FCRA disclosure where the flag is true.

**Combined Reg B / Reg V notice tested as a single artifact.** The two regimes carry separate content requirements; a single test conflates the two. Fix: separate content-compliance fields per regime; the combined notice can clear one and fail the other.

#### Model-supported reasons defects

**"The model is a black box" treated as a defense.** Reg B §1002.9 forecloses this position on its own terms (CFPB Circular 2022-03, which restated the point, was withdrawn May 12, 2025; the obligation survives the withdrawal). Fix: every AI / complex-model decision must produce a per-decision feature contribution artifact (SHAP, LIME, leave-one-out, monotonic constraint trace, or the firm's named explainability method). Where the artifact is absent, the row carries `[evidence needed]` and routes to model risk for the explainability ask.

**Vendor-of-record reason coding accepted as the creditor's compliance evidence.** Vendor returns a numeric score and a reason flag from a fixed dictionary; the creditor must demonstrate the cited reason reflects the actual principal feature contribution. Fix: vendor explainability artifact tested against the cited reason per decision; absent evidence is a finding, not a routing question.

**Impossible-mapping defects ("value of collateral" cited on unsecured product).** Notice template defect that produces inaccurate notices regardless of the underlying model. Fix: notice-template release control should include an impossible-mapping check; the review surfaces the pattern and recommends the control change.

#### Disparate-impact panel defects

**BISG-flagged disparity reported as a finding of disparate impact.** BISG is a probabilistic proxy; the panel produces signals, not findings. Fix: every BISG-derived statistic carries the BISG caveat; the recommended action routes the signal to `fair-lending-test-plan` for finding-grade work.

**HMDA self-reported demographics ignored on dwelling-secured population in favor of BISG.** HMDA is stronger evidence and must be used directly for the dwelling-secured perimeter. Fix: per-product proxy choice with rationale; dwelling-secured uses HMDA, non-dwelling uses BISG.

**Reason-mix disparity panel skipped.** Reason-mix disparity (which reasons are cited disproportionately for which cohorts) is a separate signal from decline-rate disparity and often surfaces issues the rate panel does not. Fix: include both panels every time; even a clean rate panel can carry a reason-mix signal.

**Geography panel run without CRA assessment-area overlap.** A redlining red flag inside the CRA assessment area routes to the CRA officer alongside the fair-lending committee. Fix: per-MSA assessment-area overlap field on the geography panel; the routing follows the overlap.

#### Recommended-action defects

**"Issue re-notices to affected applicants" recommended without counsel review.** Re-issuance language and customer-communication scope are counsel decisions. Fix: re-issuance recommendations name counsel as a reviewer; the artifact does not direct customer communication.

**Recommendation routes only to consumer compliance.** Most material recommendations cross-route (model risk for reason-generation fixes, fair-lending committee for redlining flags, CRA officer for assessment-area overlap, privacy team for customer-notice content involving data sources). Fix: cross-routing field per recommendation.

**No named owner role on the recommendation.** The recommendation is owner-routed for human decision; an unnamed-owner recommendation is a draft observation, not an action. Fix: owner role per recommendation (not individual; role).

**Timeline ranges of "two to four weeks" or "one to two quarters."** Fake-precision filler. Fix: a single proposed due date that the named owner can accept, push back on, or rebid. The proposal, not the range.

#### Source-trace and confidence defects

**A single confidence label across the artifact.** Source-cited facts, management assertions, public-source obligations, generated inferences, and open legal or compliance questions each carry a different evidence basis. Fix: per-claim confidence label with the evidence type recorded.

**Materials cited by URL without section reference.** SKILL.md and the artifact cite by file path to `references/source-anchors.md`; that file carries the full citation, section reference, and excerpt. URL-only citations are a content-quality-check failure. Fix: cite the reference file; the reference file carries the URL.

**Per-decision evidence dropped at the population level into the source trace.** The source trace records the artifact's claims; per-decision evidence belongs in the per-decision tables (sections 3, 4, 5). Fix: separate the artifact-level claim trace from the per-decision evidence trail.
