# Troubleshooting: adverse-action-review

Recurring defects in the adverse-action notice review and in the artifact this skill produces. The defects below repeat across engagements; treat the list as a checklist when the artifact is in second-line review.

## Notice-population scope defects

**Reviewed only outright denials.** §1002.2(c) covers counteroffers not accepted, terms-less-favorable actions, incomplete-application notices, and existing-account adverse changes. A review that names the denial subset only misses populations the regulators expect to see covered. Fix: enumerate the §1002.2(c) action categories in scope on the population panel; if a category is excluded, name the exclusion explicitly with a reason.

**Population framed as "Q3 declines" without the §1002.2(c) action category split.** The action category drives which §1002.9 timing clock applies. Fix: per-decision action category is a population-level field, not an inference; pull it from the decision system.

**Sample frame defaults to random across the whole population.** Risk-based sampling by product, vintage, channel, decision-system version, or notice-template version is often more useful. Fix: name the sample frame and the rationale; default to the focal-product cohort when the engagement has a focal trigger.

## Timing-compliance defects

**§1002.9(c) incomplete-application clock applied where the application was complete.** Recurring defect; the 90-day clock under §1002.9(c) only applies where the incompleteness was actually flagged to the applicant. Fix: per-decision check that the incompleteness notice was sent before the §1002.9(c) clock is invoked.

**Counteroffer clock applied where there was no counteroffer.** Some systems route a soft-decline pattern (smaller amount, longer tenor) into the counteroffer track without sending the counteroffer notice. Fix: per-decision check that the counteroffer was actually offered to the applicant before the counteroffer-not-accepted clock is invoked.

**"Days elapsed" calculated from the wrong start date.** The §1002.9(a)(1) clock starts when the application is complete, not when the application is received. Fix: the population data must include both received-date and complete-date; the panel uses complete-date.

## Content-compliance defects

**Sample-form reason selected because it was closest, not because it was the principal reason.** This is the CFPB Circular 2023-03 defect. Fix: per-decision evidence that the cited reason is the principal reason actually relied upon — feature contribution score, model output, or named scoring rule.

**Generic statement substituted for specific reason.** "You did not meet our credit standards" or "credit application incomplete" (when the application was complete) are recurring generic-reason-only defects. Fix: per-decision specificity test against the Staff Commentary; generic statements are content failures regardless of whether sample-form reasons are also cited.

**FCRA risk-based pricing notice not sent where a credit score was used in adverse action.** Reg V §1022.74 sets a separate disclosure obligation that survives whether the Reg B notice content is otherwise compliant. Fix: per-decision FCRA-overlay-applicable flag and a content-compliance check on FCRA disclosure where the flag is true.

**Combined Reg B / Reg V notice tested as a single artifact.** The two regimes carry separate content requirements; a single test conflates the two. Fix: separate content-compliance fields per regime; the combined notice can pass one and fail the other.

## Model-supported reasons defects

**"The model is a black box" treated as a defense.** CFPB Circular 2022-03 forecloses this position. Fix: every AI / complex-model decision must produce a per-decision feature contribution artifact (SHAP, LIME, leave-one-out, monotonic constraint trace, or the firm's named explainability method). Where the artifact is absent, the row carries `[evidence needed]` and routes to model risk for the explainability ask.

**Vendor-of-record reason coding accepted as the creditor's compliance evidence.** Vendor returns a numeric score and a reason flag from a fixed dictionary; the creditor must demonstrate the cited reason reflects the actual principal feature contribution. Fix: vendor explainability artifact tested against the cited reason per decision; absent evidence is a finding, not a routing question.

**Impossible-mapping defects ("value of collateral" cited on unsecured product).** Notice template defect that produces inaccurate notices regardless of the underlying model. Fix: notice-template release control should include an impossible-mapping check; the review surfaces the pattern and recommends the control change.

## Disparate-impact panel defects

**BISG-flagged disparity reported as a finding of disparate impact.** BISG is a probabilistic proxy; the panel produces signals, not findings. Fix: every BISG-derived statistic carries the BISG caveat; the recommended action routes the signal to `fair-lending-test-plan` for finding-grade work.

**HMDA self-reported demographics ignored on dwelling-secured population in favor of BISG.** HMDA is stronger evidence and must be used directly for the dwelling-secured perimeter. Fix: per-product proxy choice with rationale; dwelling-secured uses HMDA, non-dwelling uses BISG.

**Reason-mix disparity panel skipped.** Reason-mix disparity (which reasons are cited disproportionately for which cohorts) is a separate signal from decline-rate disparity and often surfaces issues the rate panel does not. Fix: include both panels every time; even a clean rate panel can carry a reason-mix signal.

**Geography panel run without CRA assessment-area overlap.** A redlining red flag inside the CRA assessment area routes to the CRA officer alongside the fair-lending committee. Fix: per-MSA assessment-area overlap field on the geography panel; the routing follows the overlap.

## Recommended-action defects

**"Issue re-notices to affected applicants" recommended without counsel review.** Re-issuance language and customer-communication scope are counsel decisions. Fix: re-issuance recommendations name counsel as a reviewer; the artifact does not direct customer communication.

**Recommendation routes only to consumer compliance.** Most material recommendations cross-route (model risk for reason-generation fixes, fair-lending committee for redlining flags, CRA officer for assessment-area overlap, privacy team for customer-notice content involving data sources). Fix: cross-routing field per recommendation.

**No named owner role on the recommendation.** The recommendation is owner-routed for human decision; an unnamed-owner recommendation is a draft observation, not an action. Fix: owner role per recommendation (not individual; role).

**Timeline ranges of "two to four weeks" or "one to two quarters."** Fake-precision filler. Fix: a single proposed due date that the named owner can accept, push back on, or rebid. The proposal, not the range.

## Source-trace and confidence defects

**A single confidence label across the artifact.** Source-cited facts, management assertions, public-source obligations, generated inferences, and open legal or compliance questions each carry a different evidence basis. Fix: per-claim confidence label with the evidence type recorded.

**Materials cited by URL without section reference.** SKILL.md and the artifact cite by file path to `references/source-anchors.md`; that file carries the full citation, section reference, and excerpt. URL-only citations are a content-quality-check failure. Fix: cite the reference file; the reference file carries the URL.

**Per-decision evidence dropped at the population level into the source trace.** The source trace records the artifact's claims; per-decision evidence belongs in the per-decision tables (sections 3, 4, 5). Fix: separate the artifact-level claim trace from the per-decision evidence trail.
