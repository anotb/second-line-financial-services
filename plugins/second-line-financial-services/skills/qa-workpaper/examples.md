# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## examiner-prep-tprm-sweep

### Example: Examiner-prep QA sweep on a portfolio of TPRM workpapers

Public-source-derived. No named institution. Mirrors the standard examiner-prep QA sweep done six weeks before a Federal Reserve targeted exam on third-party risk.

#### Input

- **QA scope**: examiner-prep-sweep on 14 TPRM workpapers from the most recent testing cycle.
- **Trigger**: a Federal Reserve targeted exam on third-party risk is six weeks out. The second-line QA function is doing an examiner-prep sweep on the TPRM workpaper population the examiner is likely to sample.
- **Engagement scope supplied**: institution = mid-size bank holding company (large complex banking organisation under SR 08-8); primary regulators = FRB, OCC for the lead bank, plus state DFI; persona = QA reviewer (independent of the workpaper reviewers); source posture = public-plus-firm-policy-plus-evidence; sector overlays = banking and payments-fintech (the TPRM portfolio includes sponsor-bank fintech-program testing); cross-cutting overlays = cyber (TPRM portfolio includes vendor-IAM testing).
- **Inputs to the QA reviewer**: 14 completed TPRM workpapers, their underlying exception registers, the firm TPRM methodology, source-anchor file pointers (interagency TPRM guidance June 2023, joint statement on bank deposit arrangements July 2024, IIA Standard 1300, AICPA AU-C 230 / 530, FFIEC IT booklet).

#### Output sketch

The skill produces an Excel workbook (per-workpaper QA tabs plus a portfolio summary tab) plus a Word QA memo. Headlines from the memo:

##### Executive summary

- **Portfolio decision: 9 accept, 4 conditional-accept, 1 return-for-rework.** Aggregate severity across the 14 workpapers: 1 critical, 5 major, 14 minor.
- **Methodology drift across reviewers** is the dominant population-level finding; recommendation seed routes back to a methodology refresh before the next testing cycle, not just to per-workpaper rework.
- **Three workpapers have issue closure approval status flagged "not-approved"** pending rework; one has the underlying issue in `issue-writeup` already opened.

##### QA scope

- 14 TPRM workpapers from the Q4 2025 testing cycle. Coverage: 6 critical-vendor monitoring workpapers, 4 SOC 2 reliance workpapers, 2 exit-plan-testing workpapers, 2 sponsor-bank deposit-program workpapers. Methodology references applied: AICPA AU-C 230 / 530, IIA Standard 1300 and 2340, interagency TPRM guidance June 2023, firm TPRM methodology.

##### Population-level deficiency themes

- **Evidence-reliability (recurring across 8 of 14 workpapers).** Vendor-supplied SOC 2 reports cited as evidence without the firm's reliance assessment documented. The firm's reliance posture (CUEC review, complementary user entity controls posture, scope-period coverage versus the firm's testing period, qualified-opinion read) is missing from the evidence-inspected table on most workpapers.
- **Conclusion-support (recurring across 4 of 14 workpapers).** Workpapers concluding on critical-vendor monitoring as effective without any evidence of the firm's KRI dashboard for that vendor; the conclusion rests on the existence of a vendor-supplied report alone.
- **Severity calibration (recurring across 2 of 14 workpapers).** Two workpapers rate exit-plan-testing absence as medium; firm methodology floor (and supervisory expectation under interagency TPRM guidance June 2023) is high for critical vendors. Severity inflation requested.

##### Deficiency findings (selected; full register in workbook Tab 3)

- **D1 (critical, conclusion-support).** Workpaper WP-2025-Q4-TPRM-007 (critical-vendor monitoring on a payment-processing vendor). Observation: workpaper concludes critical-vendor monitoring effective; no evidence of the firm's KRI dashboard tie-out for the vendor, no evidence of the firm's incident-tracking integration, no evidence of the firm's quarterly-review meeting minutes. Methodology reference: firm TPRM methodology, interagency TPRM guidance June 2023 [verify section]. Required action: return workpaper; redraft conclusion against the firm's actual monitoring evidence; if monitoring evidence is not produced, the conclusion rebases to not-effective and the issue elevates separately.
- **D2-D9 (major, evidence-reliability).** Eight workpapers cite vendor-supplied SOC 2 reports as evidence without firm reliance assessment. Required action per workpaper: add reliance assessment to evidence-inspected table; document CUEC posture and any unaddressed CUECs; document scope-period coverage versus firm testing period.
- **D10 (major, conclusion-support, paired with D2-D9).** Four workpapers conclude on critical-vendor monitoring without KRI dashboard evidence. Required action per workpaper: add KRI dashboard tie-out evidence or rebase conclusion.
- **D11-D12 (major, severity-calibration).** Two workpapers rate exit-plan-testing absence as medium; firm methodology floor is high. Required action: rebase severity to high; re-evaluate disposition (likely elevation to issue).
- **D13-D26 (minor, formatting and miscellaneous).** Fourteen minor deficiencies across the portfolio: missing population reconciliation totals, missing evidence reliance classification on case-management extracts, missing stratum-level breakdowns, scope-statement inconsistencies between test plan and workpaper.

##### Sample re-perform results

- QA re-performed selected items across 6 workpapers (the higher-stakes critical-vendor monitoring and sponsor-bank deposit-program workpapers). Re-perform identified two divergences: one on a SOC 2 reliance workpaper (the SOC 2 report scope did not cover the firm's testing period; the workpaper relied on the report regardless), and one on a sponsor-bank end-customer reconciliation workpaper (the FBO subledger reconciliation evidence was sponsor-supplied; the firm did not independently verify).

##### Severity calibration

- Two floor violations on exit-plan-testing absence (D11-D12). Methodology drift across reviewers is the underlying pattern; the methodology refresh recommendation seed routes the floor reaffirmation into the refresh.

##### Conclusion support

- Aggregate: 9 of 14 workpapers carry supported conclusions (with minor noted); 4 carry partially-supported conclusions pending the rework items (D2-D10); 1 carries a not-supported conclusion (D1, return).

##### Decision

| Workpaper ID | Decision | Rework items (if any) |
|---|---|---|
| WP-2025-Q4-TPRM-001 | accept | (minor noted) |
| WP-2025-Q4-TPRM-002 | accept | (minor noted) |
| WP-2025-Q4-TPRM-003 | conditional-accept | document SOC 2 reliance assessment; add CUEC posture |
| WP-2025-Q4-TPRM-004 | conditional-accept | document KRI dashboard tie-out for critical-vendor monitoring conclusion; add SOC 2 reliance assessment |
| WP-2025-Q4-TPRM-005 | accept | (minor noted) |
| WP-2025-Q4-TPRM-006 | conditional-accept | rebase exit-plan-testing severity to high; re-evaluate disposition |
| WP-2025-Q4-TPRM-007 | return-for-rework | redraft critical-vendor monitoring conclusion against actual monitoring evidence; if evidence not produced, rebase conclusion to not-effective and elevate issue |
| WP-2025-Q4-TPRM-008 | accept | (minor noted) |
| WP-2025-Q4-TPRM-009 | conditional-accept | document SOC 2 reliance assessment; add KRI dashboard tie-out |
| WP-2025-Q4-TPRM-010 | accept | (minor noted) |
| WP-2025-Q4-TPRM-011 | accept | (minor noted) |
| WP-2025-Q4-TPRM-012 | accept | (minor noted) |
| WP-2025-Q4-TPRM-013 | accept | (minor noted) |
| WP-2025-Q4-TPRM-014 | accept | (minor noted) |

- **Issue closure approval status**: 3 workpapers flagged not-approved pending rework (WP-007, WP-004, WP-009 — all on critical-vendor monitoring conclusions); 11 not-applicable.

##### Reviewer questions

- Q1: does the methodology refresh sit before the next testing cycle, or does it sit inside the current cycle as a mid-cycle methodology amendment? — testing manager plus head of compliance testing.
- Q2: should the SOC 2 reliance posture be standardised in the testing template (defaulted to require CUEC posture documentation) or left to per-workpaper preparer discretion? — testing manager.
- Q3: who routes the WP-007 rework to the workpaper reviewer, and what is the closure timeline given the six-week exam window? — head of compliance testing.

##### QA confidence label

- Medium overall. The population shows methodology drift across reviewers, suggesting a methodology refresh is needed before the next cycle. QA re-perform was completed on six of fourteen workpapers; full re-perform across the population was not feasible in the examiner-prep window.

#### Why this scenario matters

- **Boundary check on examiner-prep posture.** The QA scope is examiner-prep-sweep, not in-cycle QA; the deliverable is a portfolio QA memo plus per-workpaper notes, not 14 separate full-review packs.
- **Boundary check on population-level themes.** The dominant finding (methodology drift) is a population-level pattern, not a per-workpaper deficiency. The recommendation seed routes to methodology refresh, not to per-workpaper rework alone.
- **Boundary check on issue closure approval.** Three workpapers are flagged not-approved for issue closure separately from the workpaper-decision column; QA decision and issue closure decision are distinct.
- **Boundary check on QA confidence labelling.** Medium confidence for the portfolio reflects re-perform coverage limits in the examiner-prep window, not a defect in the QA reviewer's work; the confidence label is honest about what the QA could and could not cover in the window.

#### Anchors

- AICPA AU-C 230 (Audit Documentation).
- AICPA AU-C 530 (Audit Sampling) §A18-§A22 [verify paragraph references].
- IIA Standard 1300 [verify section labels] (QAIP) and Standard 2340 [verify section labels] (engagement supervision).
- Interagency Guidance on Third-Party Relationships: Risk Management (FRB / FDIC / OCC, June 2023).
- Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services (FDIC / OCC / FRB, July 25, 2024).
- FFIEC IT Examination Handbook (Audit booklet, April 2012).
- Banking sector overlay (this skill); payments-fintech sector overlay (this skill); cyber cross-cutting overlay (this skill).

See `references/source-anchors.md`, `references/sector-overlays.md#banking`, `references/sector-overlays.md#payments-fintech`, and `references/cross-cutting.md#cyber` for full citations.

## reg-e-error-resolution-bank

### Example: QA review of a Reg E error-resolution workpaper at a regional bank

Public-source-derived. No named institution. Mirrors the standard QA pass over a completed Reg E §1005.11 error-resolution testing workpaper.

#### Input

- **QA scope**: full-review, in-cycle QA before workpaper closure.
- **Workpaper under review**: completed Reg E error-resolution workpaper for Q1 2026 testing cycle (workpaper ID `WP-2026-Q1-RegE-001`, test ID `TP-CMP-RegE-2026-01`, control ID for the dispute-resolution control). Workpaper concluded design effective and operating partially-effective.
- **Engagement scope supplied**: institution = regional state member bank; primary regulators = FRB, CFPB, state DFI; persona = QA reviewer (independent of the workpaper reviewer); source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlays = conduct (consumer-facing).
- **Inputs to the QA reviewer**: the workpaper, the underlying exception register (`ER-CMP-RegE-2026-01` from `exception-analysis`), the test plan, the firm CMS testing methodology, source-anchor file pointers (AICPA AU-C 230 / 530 / 265, IIA Standard 1300 and 2340, CFPB CMS examination procedures, conduct cross-cutting overlay).

#### Output sketch

The skill produces an Excel workbook (review-markup tabs) plus a Word QA memo. Headlines from the memo:

##### Executive summary

- **Decision: return for rework.** Six deficiencies identified: one critical, two major, three minor. Critical deficiency on reviewer-separation returns the workpaper.
- Severity recalibration requested on three exceptions; firm methodology floor for §1005.11(c) timing is high, preparer rated medium.
- Conclusion language requires rewrite from legal-violation framing to control-effectiveness framing; legal question routes to legal counsel and head of regulatory affairs separately.

##### Deficiency findings

- **D1 (critical, reviewer-separation).** Section: sign-off block. Observation: preparer and workpaper reviewer roles are the same on the sign-off block; both signed as "compliance-testing analyst". Methodology reference: firm methodology, IIA Standard 2340 [verify section] engagement supervision. Required action: return workpaper; reassign reviewer to a separate role (compliance-testing manager); re-sign.
- **D2 (major, evidence-reliability and exception-classification).** Section: samples S12-S14. Observation: three sample items in the workpaper's sample-results table show "investigation completed" with no evidence ID; the underlying exception register did not flag them as evidence gaps (no exception X-flagged for these samples). Methodology reference: AICPA AU-C 500 [verify paragraph], firm methodology evidence-reliance posture. Required action: preparer to attach evidence ID per sample item or reclassify as evidence-gap exceptions in the register; re-aggregate deviation rate accordingly.
- **D3 (major, conclusion-support).** Section: conclusion. Observation: conclusion language reads "the bank did not comply with Reg E §1005.11(c)" — legal-violation framing. Methodology reference: firm methodology, conduct cross-cutting overlay. Required action: rewrite to control-effectiveness language: "the dispute-resolution control did not operate within the §1005.11(c) timing clock for [population] sample items during the period". Route legal question to legal counsel and the head of regulatory affairs separately.
- **D4 (minor, criteria-sufficiency).** Section: scope and source posture. Observation: missing population reconciliation total. Methodology reference: firm methodology, banking sector overlay (population definition convention). Required action: add population reconciliation row showing the count of disputes received during the period reconciled against the case-management system extract.
- **D5 (minor, evidence-reliability).** Section: evidence inspected E2. Observation: missing reliance classification on case-management system extract; the extract is the population basis but is not classified. Methodology reference: firm methodology, AICPA AU-C 500 [verify paragraph]. Required action: classify as system-of-record extract; add extract date and run-by role to the evidence-inspected table.
- **D6 (minor, exception-classification).** Section: aggregation and projection. Observation: aggregation section missing stratum-level breakdown though sample was stratified by dispute type. Methodology reference: firm methodology. Required action: add stratum-level breakdown table.

##### Sample re-perform results

- QA re-performed five sample items (S5, S12, S18, S22, S29) selecting from across the dispute-type stratification. Re-perform identified one divergence: sample S12 re-perform showed a deviation the preparer recorded as "pass" on procedure P2 (investigation timeline). The divergence routes into D2 and adds to the workpaper's deviation count.
- Re-perform on S22 confirmed the preparer's exception identification and classification.

##### Severity calibration

- Three exceptions in the workpaper rated medium for §1005.11(c) timing deviations. Firm methodology floor for §1005.11(c) timing is high (per firm policy version effective on the test period). Severity inflation requested: re-rate the three exceptions to high. Two analogous prior workpapers (Q4 2025 and Q3 2025) carried the same exceptions rated high; the rating drift in the Q1 2026 workpaper is inconsistent with the prior cycle.
- One exception (X4, evidence-gap on a single sample item) rated low. No floor violation; consistent with prior cycles. No change.

##### Conclusion support

- Design effectiveness: supported. Walkthrough evidence and procedure outcomes carry the design read.
- Operating effectiveness: partially-supported. Aggregation reads against tolerable rate, but conclusion language drifts to legal-violation framing — see D3. Once the language is corrected and the severity rebase is applied, the underlying evidence supports a partially-effective operating finding.

##### Decision

- **Decision: return for rework.** Critical deficiency on reviewer-separation returns the workpaper.
- **Rework items**: re-sign with separate reviewer role (D1); attach evidence ID or reclassify samples S12-S14 (D2); rewrite conclusion language to control-effectiveness framing (D3); add population reconciliation, evidence reliance classification, and stratum-level breakdown (D4-D6); rebase three exceptions to high severity per firm methodology floor.
- **Issue closure approval status**: not-applicable (the workpaper is not yet through closure, and any open issues identified in the workpaper carry their own remediation lifecycles).

##### Reviewer questions

- Q1: should the §1005.11(c) timing deviations elevate to issue, given the severity rebase to high? — workpaper reviewer plus testing manager.
- Q2: is the segment-level re-test a separate workpaper or a re-issue of this one? — workpaper reviewer.

##### QA confidence label

- High. Sample re-perform was completed for five items (one divergence identified), methodology references applied across all eight QA dimensions, deficiencies cross-checked against firm methodology and the analogous prior workpapers.

#### Why this scenario matters

- **Boundary check on reviewer separation.** A critical deficiency that returns the workpaper. Reviewer separation is a structural QA dimension, not advisory.
- **Boundary check on severity calibration.** Severity inflation requested in this case (rebase up from medium to high); the same rationale-field discipline catches deflation in other cases.
- **Boundary check on conclusion-language hygiene.** Legal-violation framing is a recurring deficiency on consumer-facing workpapers; the QA reviewer rewrites and routes the legal question separately.
- **Boundary check on QA versus issue closure.** The QA decision (return for rework) is distinct from any issue closure decision; the workpaper carries open issues that have their own remediation lifecycles regardless of QA outcome.
- **Boundary check on QA re-perform.** QA re-perform on five sample items identified one divergence the preparer missed; the QA review note routes the divergence into a deficiency rather than letting it pass.

#### Anchors

- AICPA AU-C 230 (Audit Documentation).
- AICPA AU-C 265 (Communicating Internal Control Related Matters).
- AICPA AU-C 530 (Audit Sampling) §A18-§A22 [verify paragraph references].
- IIA Standard 1300 [verify section labels] (QAIP) and Standard 2340 [verify section labels] (engagement supervision).
- Reg E — 12 CFR Part 1005, especially §1005.11.
- CFPB CMS examination procedures.
- Conduct cross-cutting overlay (this skill).

See `references/source-anchors.md`, `references/sector-overlays.md#banking`, and `references/cross-cutting.md#conduct` for full citations.

## troubleshooting

### Troubleshooting: qa-workpaper

Recurring defects in QA review notes and the pattern that catches them.

#### 1. QA as proofreading

Symptom: the QA review note's deficiency register reads heavy on formatting and stylistic items; substantive deficiencies on evidence reliability, conclusion support, and severity calibration are absent or thin.

Why it goes wrong: the QA reviewer treated the workpaper as a document to copy-edit rather than a methodology artifact to challenge. Spelling and formatting are minor deficiencies; the QA's job is methodology rigor.

Catch it: count the deficiencies by category. If `formatting` outnumbers the substantive categories (`evidence-reliability`, `conclusion-support`, `severity-calibration`, `procedure-execution`, `exception-classification`), walk back through the workpaper looking for substantive issues. The sample re-perform tab is the discipline that surfaces substantive issues; do it before declaring the QA done.

#### 2. QA reviewer is also the workpaper reviewer

Symptom: the QA reviewer role and the workpaper reviewer role are the same on the QA review note's header.

Why it goes wrong: same problem as preparer-reviewer overlap on the workpaper. The QA reviewer must be independent of the original review; otherwise the QA is a self-review and adds no independence.

Catch it: the QA review note's header has three distinct role names (preparer, workpaper reviewer, QA reviewer). Where the testing function is small and the same person fills two roles, the separation is on role label and on review responsibility, not on body, but the QA review note's audit trail records the separate sign-offs explicitly. Where genuine independence is not achievable, the QA scope is `targeted-re-review` by a different role and the limitation is documented in the QA review note.

#### 3. Severity inflation in QA notes

Symptom: every deficiency on the deficiency tab is rated critical or major; no minor deficiencies; the decision is uniformly return-for-rework.

Why it goes wrong: the severity scale (critical / major / minor) has consequences. Critical returns the workpaper. Use it only for things that fail the experienced-auditor sufficiency standard or break methodology floors (reviewer-separation, fundamental conclusion failures, evidence that does not support the conclusion). Major is rework-required-but-can-re-issue. Minor is note-for-future-cycles. A QA review note that returns every workpaper for rework loses credibility and wastes preparer cycles.

Catch it: read the severity rationale aloud for each critical and major deficiency. Does the rationale name the methodology floor that was breached or the experienced-auditor sufficiency standard that was failed? If the rationale is "this should have been better", the rating is not yet defensible. Push back to AICPA AU-C 265 deficiency / significant deficiency / material weakness severity hierarchy or to the firm methodology severity rubric in `references/firm-overlay.md`.

#### 4. Skipping sample re-perform on high-stakes workpapers

Symptom: the QA review note's sample re-perform tab is empty on a high-stakes workpaper (consumer-facing, examiner-prep, post-issue re-QA, large-deviation-rate population).

Why it goes wrong: the QA is most credible when it has independently re-performed a small subsample. Without re-perform, the QA reviewer's deficiency findings rest on document review alone; that is a weaker QA posture and a weaker examiner-prep posture.

Catch it: the QA scope drives the re-perform expectation. Full-review and examiner-prep-sweep typically include re-perform on at least three to five sample items selected across the stratification. Targeted-re-review may skip re-perform if the targeted section does not turn on sample-level results. Post-issue re-QA includes re-perform on the items the issue was elevated against. Where re-perform is skipped, the QA review note documents why in the limitations section.

#### 5. Confusing workpaper closure with issue closure

Symptom: the QA review note's decision is `accept` and the deliverable reads as if every issue identified in the workpaper is also closed.

Why it goes wrong: a clean workpaper documents the test; the issues identified still have remediation lifecycles in `issue-writeup` and downstream tracking. Closing the workpaper does not close the issue. Conflating the two creates audit-trail problems (an issue that the QA review note implied was closed but that downstream tracking shows as open).

Catch it: the QA review note's decision section has two separate fields: `decision` (accept / return-for-rework / conditional-accept) and `issue_closure_approval` (approved / not-approved / not-applicable). The latter is read against the firm's issue-closure machinery, not against the workpaper's QA outcome. Where the workpaper carries open issues, `issue_closure_approval` is `not-applicable` (the workpaper does not close the issue) or `not-approved` (the QA reviewer believes the issue is not yet ready to close; this is rare and routed to the issue owner separately).

#### 6. Treating QA as adversarial

Symptom: the QA review note's tone reads accusatory or gotcha; reviewer questions are framed as challenges rather than questions; the workpaper reviewer pushes back on the QA process rather than on the deficiency content.

Why it goes wrong: the QA finding goes back to the workpaper reviewer, not the auditee. The QA reviewer's job is to make the workpaper better; the workpaper reviewer's job is to defend or correct. Adversarial tone makes both jobs harder and creates friction that delays the closure.

Catch it: read the QA review note as if you were the workpaper reviewer receiving it. Reviewer questions are questions, not accusations. Required actions are declarative, not interrogative ("rewrite the conclusion to control-effectiveness language", not "consider whether the conclusion language might benefit from a rewrite"). Methodology references are cited so the rationale is the standard, not the reviewer's preference.

#### 7. QA scope creep into re-running the test

Symptom: the QA review note re-performs every sample item, re-classifies every exception, and effectively redoes the workpaper rather than reviewing it.

Why it goes wrong: the QA scope is review of the completed workpaper, not re-execution of the test. Re-running the test consumes the QA reviewer's time disproportionately, duplicates the preparer's work, and blurs the line between QA and re-test. Re-test is a separate disposition (`re-test-required` in the exception register, leading to a new test cycle).

Catch it: the sample re-perform tab is a small subsample (typically three to seven items, selected across stratification), not the full sample. The QA reviewer challenges the preparer's classification; the QA reviewer does not re-classify every exception. Where the QA reviewer believes the workpaper requires effective re-execution, the decision is `return-for-rework` with the rework items naming what the preparer must redo, not a QA-side re-execution.

#### 8. Empty methodology references on deficiency rows

Symptom: deficiency rows on the deficiency tab have empty or generic methodology references ("firm methodology" with no section, "audit standards" with no specific standard).

Why it goes wrong: a deficiency without a named methodology reference is the QA reviewer's preference. Methodology references make the deficiency defensible: the workpaper failed against a named, dated standard or a named firm methodology section, not against the QA reviewer's taste.

Catch it: every deficiency row carries a methodology reference column with at least one specific reference (named standard with section, or named firm methodology with section, or named overlay file path). Generic references ("firm methodology" alone) do not pass; push back to specificity.

#### 9. Population-level themes missed in examiner-prep sweeps

Symptom: an examiner-prep-sweep QA review note reads as 14 separate per-workpaper QA notes with no population-level synthesis.

Why it goes wrong: the value of an examiner-prep sweep is the population-level pattern (methodology drift, recurring evidence-reliability failures, severity-floor violations across multiple workpapers). Per-workpaper deficiencies without the population-level synthesis miss the recommendation seed for the next cycle.

Catch it: the QA review note for an examiner-prep-sweep scope carries section 6a (Population-level deficiency themes) before the decision section. The themes name the recurring pattern, the count of workpapers affected, and the recommendation seed for the next testing cycle (typically methodology refresh, reviewer training, or template variant updates). Without this section, the sweep is a batched per-workpaper QA, not a sweep.

#### 10. QA confidence label unset or always high

Symptom: the QA review note's confidence label is always `high` regardless of QA scope, re-perform completeness, or methodology depth applied.

Why it goes wrong: the confidence label reflects evidence sufficiency for the QA review itself. A QA done in an examiner-prep window with re-perform on six of fourteen workpapers is not a high-confidence QA on the un-re-performed eight. Defaulting to high masks the real coverage.

Catch it: the confidence label is set against re-perform completeness, methodology depth applied across all eight QA dimensions, time available for the review, and reliance on second-hand inputs (the exception register, the test plan). High requires re-perform across the high-stakes items, methodology depth applied across all dimensions, and time sufficient for the review. Medium and low are honest reflections of what the QA could and could not cover; they are not defects in the QA reviewer's work.
