# Troubleshooting: qa-workpaper

Recurring defects in QA review notes and the pattern that catches them.

## 1. QA as proofreading

Symptom: the QA review note's deficiency register reads heavy on formatting and stylistic items; substantive deficiencies on evidence reliability, conclusion support, and severity calibration are absent or thin.

Why it goes wrong: the QA reviewer treated the workpaper as a document to copy-edit rather than a methodology artifact to challenge. Spelling and formatting are minor deficiencies; the QA's job is methodology rigor.

Catch it: count the deficiencies by category. If `formatting` outnumbers the substantive categories (`evidence-reliability`, `conclusion-support`, `severity-calibration`, `procedure-execution`, `exception-classification`), walk back through the workpaper looking for substantive issues. The sample re-perform tab is the discipline that surfaces substantive issues; do it before declaring the QA done.

## 2. QA reviewer is also the workpaper reviewer

Symptom: the QA reviewer role and the workpaper reviewer role are the same on the QA review note's header.

Why it goes wrong: same problem as preparer-reviewer overlap on the workpaper. The QA reviewer must be independent of the original review; otherwise the QA is a self-review and adds no independence.

Catch it: the QA review note's header has three distinct role names (preparer, workpaper reviewer, QA reviewer). Where the testing function is small and the same person fills two roles, the separation is on role label and on review responsibility, not on body, but the QA review note's audit trail records the separate sign-offs explicitly. Where genuine independence is not achievable, the QA scope is `targeted-re-review` by a different role and the limitation is documented in the QA review note.

## 3. Severity inflation in QA notes

Symptom: every deficiency on the deficiency tab is rated critical or major; no minor deficiencies; the decision is uniformly return-for-rework.

Why it goes wrong: the severity scale (critical / major / minor) has consequences. Critical returns the workpaper. Use it only for things that fail the experienced-auditor sufficiency standard or break methodology floors (reviewer-separation, fundamental conclusion failures, evidence that does not support the conclusion). Major is rework-required-but-can-re-issue. Minor is note-for-future-cycles. A QA review note that returns every workpaper for rework loses credibility and wastes preparer cycles.

Catch it: read the severity rationale aloud for each critical and major deficiency. Does the rationale name the methodology floor that was breached or the experienced-auditor sufficiency standard that was failed? If the rationale is "this should have been better", the rating is not yet defensible. Push back to AICPA AU-C 265 deficiency / significant deficiency / material weakness severity hierarchy or to the firm methodology severity rubric in `references/firm-overlay.md`.

## 4. Skipping sample re-perform on high-stakes workpapers

Symptom: the QA review note's sample re-perform tab is empty on a high-stakes workpaper (consumer-facing, examiner-prep, post-issue re-QA, large-deviation-rate population).

Why it goes wrong: the QA is most credible when it has independently re-performed a small subsample. Without re-perform, the QA reviewer's deficiency findings rest on document review alone; that is a weaker QA posture and a weaker examiner-prep posture.

Catch it: the QA scope drives the re-perform expectation. Full-review and examiner-prep-sweep typically include re-perform on at least three to five sample items selected across the stratification. Targeted-re-review may skip re-perform if the targeted section does not turn on sample-level results. Post-issue re-QA includes re-perform on the items the issue was elevated against. Where re-perform is skipped, the QA review note documents why in the limitations section.

## 5. Confusing workpaper closure with issue closure

Symptom: the QA review note's decision is `accept` and the deliverable reads as if every issue identified in the workpaper is also closed.

Why it goes wrong: a clean workpaper documents the test; the issues identified still have remediation lifecycles in `risk-compliance-core/skills/issue-writeup` and downstream tracking. Closing the workpaper does not close the issue. Conflating the two creates audit-trail problems (an issue that the QA review note implied was closed but that downstream tracking shows as open).

Catch it: the QA review note's decision section has two separate fields: `decision` (accept / return-for-rework / conditional-accept) and `issue_closure_approval` (approved / not-approved / not-applicable). The latter is read against the firm's issue-closure machinery, not against the workpaper's QA outcome. Where the workpaper carries open issues, `issue_closure_approval` is `not-applicable` (the workpaper does not close the issue) or `not-approved` (the QA reviewer believes the issue is not yet ready to close; this is rare and routed to the issue owner separately).

## 6. Treating QA as adversarial

Symptom: the QA review note's tone reads accusatory or gotcha; reviewer questions are framed as challenges rather than questions; the workpaper reviewer pushes back on the QA process rather than on the deficiency content.

Why it goes wrong: the QA finding goes back to the workpaper reviewer, not the auditee. The QA reviewer's job is to make the workpaper better; the workpaper reviewer's job is to defend or correct. Adversarial tone makes both jobs harder and creates friction that delays the closure.

Catch it: read the QA review note as if you were the workpaper reviewer receiving it. Reviewer questions are questions, not accusations. Required actions are declarative, not interrogative ("rewrite the conclusion to control-effectiveness language", not "consider whether the conclusion language might benefit from a rewrite"). Methodology references are cited so the rationale is the standard, not the reviewer's preference.

## 7. QA scope creep into re-running the test

Symptom: the QA review note re-performs every sample item, re-classifies every exception, and effectively redoes the workpaper rather than reviewing it.

Why it goes wrong: the QA scope is review of the completed workpaper, not re-execution of the test. Re-running the test consumes the QA reviewer's time disproportionately, duplicates the preparer's work, and blurs the line between QA and re-test. Re-test is a separate disposition (`re-test-required` in the exception register, leading to a new test cycle).

Catch it: the sample re-perform tab is a small subsample (typically three to seven items, selected across stratification), not the full sample. The QA reviewer challenges the preparer's classification; the QA reviewer does not re-classify every exception. Where the QA reviewer believes the workpaper requires effective re-execution, the decision is `return-for-rework` with the rework items naming what the preparer must redo, not a QA-side re-execution.

## 8. Empty methodology references on deficiency rows

Symptom: deficiency rows on the deficiency tab have empty or generic methodology references ("firm methodology" with no section, "audit standards" with no specific standard).

Why it goes wrong: a deficiency without a named methodology reference is the QA reviewer's preference. Methodology references make the deficiency defensible: the workpaper failed against a named, dated standard or a named firm methodology section, not against the QA reviewer's taste.

Catch it: every deficiency row carries a methodology reference column with at least one specific reference (named standard with section, or named firm methodology with section, or named overlay file path). Generic references ("firm methodology" alone) do not pass; push back to specificity.

## 9. Population-level themes missed in examiner-prep sweeps

Symptom: an examiner-prep-sweep QA review note reads as 14 separate per-workpaper QA notes with no population-level synthesis.

Why it goes wrong: the value of an examiner-prep sweep is the population-level pattern (methodology drift, recurring evidence-reliability failures, severity-floor violations across multiple workpapers). Per-workpaper deficiencies without the population-level synthesis miss the recommendation seed for the next cycle.

Catch it: the QA review note for an examiner-prep-sweep scope carries section 6a (Population-level deficiency themes) before the decision section. The themes name the recurring pattern, the count of workpapers affected, and the recommendation seed for the next testing cycle (typically methodology refresh, reviewer training, or template variant updates). Without this section, the sweep is a batched per-workpaper QA, not a sweep.

## 10. QA confidence label unset or always high

Symptom: the QA review note's confidence label is always `high` regardless of QA scope, re-perform completeness, or methodology depth applied.

Why it goes wrong: the confidence label reflects evidence sufficiency for the QA review itself. A QA done in an examiner-prep window with re-perform on six of fourteen workpapers is not a high-confidence QA on the un-re-performed eight. Defaulting to high masks the real coverage.

Catch it: the confidence label is set against re-perform completeness, methodology depth applied across all eight QA dimensions, time available for the review, and reliance on second-hand inputs (the exception register, the test plan). High requires re-perform across the high-stakes items, methodology depth applied across all dimensions, and time sufficient for the review. Medium and low are honest reflections of what the QA could and could not cover; they are not defects in the QA reviewer's work.
