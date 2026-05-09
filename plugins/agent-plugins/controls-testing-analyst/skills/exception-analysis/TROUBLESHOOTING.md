# Troubleshooting: exception-analysis

Recurring defects in exception registers and the pattern that catches them.

## 1. Treating every deviation as a finding

Symptom: every row in the register reads `control-failure` or `design-gap`; nothing classifies as `evidence-gap` or `anomaly`; disposition is uniformly `elevated-to-issue`.

Why it goes wrong: the preparer is collapsing classification into "exception" because the test plan called the deviation an exception. Six buckets exist for a reason; not every deviation is a control-side problem.

Catch it: if classification is uniform across the register, walk three rows back through the criterion and the condition. Ask: did the system do the right thing and just fail to record it (`evidence-gap`)? Did the test surface a one-off with positive evidence it does not recur (`anomaly`)? Did the tester and control owner read the criterion differently (`scope-disagreement`)? If the answers are all "no" across the register, the uniformity is real; if any answer is "yes" on a row, reclassify.

## 2. Confusing evidence gap with control failure

Symptom: a row classifies as `control-failure` but the condition reads "no evidence in the file" without a corroborating-system check; or a row classifies as `evidence-gap` but no corroborating evidence is named.

Why it goes wrong: the disambiguation between evidence-gap and control-failure is the most common classification error. Evidence-gap is "the system did the right thing, the file does not record it"; control-failure is "the system did not do the right thing." The disambiguation requires a corroborating-system check.

Catch it: every `evidence-gap` row names the corroborating evidence (system audit log, downstream system state, attestation, alternative record). Every `control-failure` row that hinges on absent documentation names what corroborating system was checked and showed no record. If neither side names the corroboration, the classification is not yet defensible.

The cyber overlay carries the disambiguation pattern in detail; load it for cyber populations.

## 3. Skipping root-cause hypothesis

Symptom: `root_cause_hypothesis.description` reads "human error", "training gap", "system limitation", or is blank.

Why it goes wrong: surface labels do not name the control attribute that failed. The downstream issue write-up needs the cause field populated with a specific weakness; without it, the recommendation seed cannot land and the issue is unactionable.

Catch it: read the description aloud. Does it name what specifically failed at the design or operation level? "Reviewer-leave delegation procedure does not require IAM-recertification reassignment" passes. "Training gap" does not. Where the root cause is genuinely unknown, the field reads "root cause analysis pending" with an open action; do not invent a cause to fill the field, but do not let "human error" stand as the cause either.

## 4. Projecting anomalies

Symptom: a row classifies as `anomaly` without positive evidence the deviation does not recur; or the aggregation reads `anomaly` because the sample size felt small.

Why it goes wrong: AICPA AU-C 530 [verify §A22 in the current edition] makes the methodology bar explicit: a deviation can be an anomaly only when there is positive evidence it is non-recurring. Default is systemic; downgrade to anomaly demands evidence, not intuition.

Catch it: any `anomaly` classification or any `aggregation.anomaly_or_systemic = anomaly` carries a named-evidence sentence in the description or the projection commentary. "Sample of one, treating as anomaly" is not evidence. "The condition arose from a one-time data-load event on a date the firm independently verified, with corroborating logs showing the event did not recur in the period" is evidence.

## 5. Severity inflation by the first-line owner

Symptom: severity is uniformly high or critical across the register; severity rationale fields are sparse; the preparer notes "owner self-rated as critical".

Why it goes wrong: first-line owners sometimes self-identify high or critical to pre-empt examiner attention, on the theory that an aggressively self-rated finding looks better than a regulator-rated one. The pattern distorts the population view, fills the issue ladder with mis-prioritised items, and burns reviewer attention.

Catch it: severity rationale references the firm's published thresholds (where they exist), frequency, customer impact, regulatory exposure, and compensating controls. If the rationale is one sentence and the severity is critical, the rating is not yet defensible. Push back to the calibration rubric in `references/firm-overlay.md` (firm-installed) or to the AU-C 265 deficiency / significant-deficiency / material-weakness severity hierarchy.

The exception works the other way too: severity deflation by first-line owners ("we'll just call it a low and close it") happens; the same rationale-field discipline catches it.

## 6. Empty handoff packages

Symptom: rows with disposition `elevated-to-issue` have empty or sparse `issue_handoff` fields; the issue writer downstream re-discovers criterion, condition, cause, effect, and recommendation seed from the workpaper.

Why it goes wrong: the whole point of the handoff is to make `risk-compliance-core/skills/issue-writeup` not re-discover work. An empty handoff package means the issue writer reads the workpaper from scratch; the integration between the two skills loses its value.

Catch it: every `elevated-to-issue` row has all five handoff fields populated (criterion, condition, cause, effect, recommendation seed) before the register is signed off. The reviewer's last check before sign-off is the handoff completeness; an empty package is a sign-off blocker.

The recommendation seed is declarative ("redesign recertification form to require per-entitlement attestation"), not interrogative ("consider whether the form should be redesigned"). The issue writer refines the seed but should not have to invent it.

## 7. Aggregation read against the wrong tolerable rate

Symptom: aggregation commentary reads against a tolerable rate that does not match the test plan; or aggregation commentary invents a tolerable rate the test plan did not set.

Why it goes wrong: the tolerable deviation rate is set in `test-plan-builder` for a reason. Inventing or substituting it in the register undermines the sample design and produces an unsupportable projection.

Catch it: the tolerable rate in `aggregation.tolerable_deviation_rate` is pulled from the test plan by `test_id`. If the test plan did not set one, that is a test-plan defect to flag back, not a number to invent here. The aggregation commentary then reads "tolerable rate not set in the test plan; flagging back to test-plan-builder for amendment".

## 8. Mixing register voice with legal-conclusion voice

Symptom: the register concludes that "the firm violated Reg X" or "the entity is non-compliant with §Y".

Why it goes wrong: the register concludes on control effectiveness and exception classification, not on legal violation. Legal-violation language is for legal counsel and regulator-led determinations.

Catch it: the register reads "the control did not operate as designed for the [population] during the period, the criterion being [rule with section]". The capital-markets sector overlay carries the language-hygiene pattern in detail because the surrounding enforcement environment makes the discipline particularly important there; the same pattern applies across sectors.

## 9. Reviewer-separation breaks

Symptom: preparer and reviewer roles are the same; or the reviewer signs off without a separate role.

Why it goes wrong: reviewer separation is structural, not advisory. The same role cannot both classify and review classification.

Catch it: `preparer.role` and `reviewer.role` differ. Where the testing function is small and the same person fills two roles, the separation is on role label and on review responsibility, not on body, but the register's audit trail records the separate sign-off explicitly.

## 10. Repeat-issue flag false-negative

Symptom: a row classifies a deviation that is the third consecutive cycle of the same condition without flagging `repeat_issue: true`.

Why it goes wrong: the issue log was not checked before classification. Repeat exceptions are different severity and different issue-writeup handoff; missing the repeat-issue flag mis-sets both.

Catch it: before sign-off, every row's condition and root-cause hypothesis is searched against the issue log for the same control or population. Where the search returns a prior open or recently closed issue, the repeat-issue flag is on and `prior_issue_id` is populated. Where the search returns nothing, the flag is off but the search itself is documented in the limitations-and-reliance field so the reviewer can see the check happened.
