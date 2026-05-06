# qa-workpaper — spec sheet

Plugin: `compliance-testing`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Reviews a completed control-test workpaper for QA: scope alignment to the test plan, source-criteria sufficiency, evidence reliability, procedure execution rigor, exception classification, conclusion support, severity calibration, reviewer separation, and remediation handoff. Output is a QA review note that lists deficiencies, accept/return decision, and required rework before workpaper closure.

Best for:
- A second-line QA function or independent reviewer is performing the standard QA pass over a completed workpaper before issue closure or examiner sharing.
- An internal audit director is rolling up workpaper-quality metrics across a testing cycle and needs structured QA notes per workpaper.
- A Federal Reserve / OCC examination is imminent and the team is doing a self-QA sweep on the workpaper population that the examiner will likely sample.

Not the right tool when:
- The workpaper has not been drafted (use `workpaper-drafter`).
- The test plan itself is being reviewed (that is design-stage review of `test-plan-builder` output, not QA of a completed workpaper).
- Exceptions identified during QA need their own classification (use `exception-analysis` for the QA-identified deviations from the methodology, not for the original control deviations).

Boundary: `test-plan-builder` is **pre-fieldwork**; `workpaper-drafter` is **during/post-fieldwork**; `qa-workpaper` is **review of the completed workpaper after fieldwork is closed**. The three skills are sequential; QA is the last step before workpaper closure.

Anchored to: IIA Performance Standard 2340 (Engagement Supervision) and Standard 1300 (Quality Assurance and Improvement Program) [verify section]; AICPA AU-C 230, Audit Documentation [verify paragraph]; PCAOB QC 1000 [verify if relevant in second-line context — borrowed methodology only]; FFIEC IT Examination Handbook, Audit booklet (April 2012) §V (audit communication) [verify section]; SR 08-8 (Federal Reserve, October 2008) [verify section]; OCC PPM 5310-3 [verify exact reference and date].

## Source anchors

Primary:
- IIA International Professional Practices Framework — Performance Standard 2340 (Engagement Supervision) and Standard 1300 (Quality Assurance and Improvement Program). Use for: framing supervision review and the QAIP. [verify section labels against current IPPF release]
- AICPA AU-C 230, Audit Documentation. Use for: experienced-auditor sufficiency standard, retention, completion timing. [verify paragraph references]
- FFIEC IT Examination Handbook, Audit booklet, April 2012, §V (audit communication and reporting). Use for: financial-services workpaper-quality conventions. [verify section labels]
- SR 08-8 (Federal Reserve, October 16, 2008). Use for: program-level expectations on testing rigor and review. [verify section labels]

Secondary (overlay only):
- COSO 2013 Internal Control — Integrated Framework, Principle 17 (Evaluates and Communicates Deficiencies). [verify principle reference]
- OCC PPM 5310-3 (compliance management systems for OCC-supervised banks). [verify exact reference and current effective date]
- IIA Practice Guide on Quality Assurance and Improvement Program [verify current edition].

## Sector overlays needed

- `banking.md` — CFPB CMS exam manual review-quality posture [verify section]; OCC heightened-standards testing-rigor expectations [verify Part 30 Appendix D].
- `insurance.md` — NAIC Model Audit Rule (Model #205) [verify section] ICFR documentation review expectations; state DOI market-conduct workpaper review conventions.
- `capital-markets.md` — FINRA 3120 / 3130 [verify] supervisory-testing review; SEC examiner expectations on workpaper completeness.
- `payments-fintech.md` — Sponsor-bank workpaper-quality expectations under interagency TPRM (June 2023) ongoing-monitoring evidence [verify section].

## Cross-cutting overlays needed

- `cyber.md` — Optional. Cyber workpapers tend to fail QA on evidence reliability (vendor-supplied scan results, screenshot-only access reviews). Worth a short overlay note.
- `privacy.md` — Not required at v1.
- `climate.md` — Not required at v1.
- `conduct.md` — Optional, for UDAAP-related workpapers where the conclusion language tends to drift toward legal-violation framing (CFPB UDAAP exam manual [verify section]).

## Output template named sections

QA review note structure:

1. Workpaper identifier and review context
   - Workpaper ID, test ID, control ID, period, preparer, reviewer, QA reviewer, QA date.
2. QA scope
   - What the QA covers (full workpaper, targeted re-review, post-issue re-QA, examiner-prep sweep).
3. QA criteria
   - Named methodology references (firm methodology, IIA standard, AU-C standard reference).
4. Deficiency findings (numbered)
   - For each deficiency:
     - Deficiency ID
     - Section of the workpaper affected
     - Category: scope-alignment / criteria-sufficiency / evidence-reliability / procedure-execution / exception-classification / conclusion-support / severity-calibration / reviewer-separation / remediation-handoff / formatting
     - Severity: critical (workpaper must be returned) / major (rework required, can re-issue) / minor (note for future cycles)
     - Specific observation (what the QA reviewer saw)
     - Methodology reference (the criterion the workpaper failed against)
     - Required action (what the preparer or reviewer must do)
5. Sample-level QA re-perform results
   - If QA re-performed selected sample items, the comparison of QA finding to original finding.
6. Severity calibration check
   - Comparison of preparer's severity ratings against firm methodology floors and against analogous prior workpapers.
7. Conclusion support assessment
   - Statement on whether the conclusion is supported by the evidence and procedures.
8. Decision
   - Accept / Return for rework / Conditional accept (specific rework items listed).
   - Issue closure approval status (separate from workpaper closure: a clean workpaper does not necessarily mean a closeable issue).
9. Reviewer questions to original reviewer
   - Questions for the workpaper reviewer to address before re-submission.
10. Reviewer sign-off
    - QA reviewer role, date, escalation path if disagreement persists.
11. Source trace and confidence label
    - Anchored methodology, firm methodology references, QA confidence label.

## Structured output fields

Schema: new `qa-review.schema.json` (Phase 2 to add).

Wrapper object:
- `qa_review_id`: string.
- `workpaper_id`: string. Foreign key into `workpaper.schema.json`.
- `test_id`: string. Foreign key.
- `qa_scope`: enum. `full-review` / `targeted-re-review` / `post-issue-re-qa` / `examiner-prep-sweep`.
- `qa_reviewer_role`: string.
- `qa_date`: string (ISO date).
- `deficiencies`: array of objects, each with:
  - `deficiency_id`: string.
  - `section_affected`: string.
  - `category`: enum (10 values listed in the named-section spec).
  - `severity`: enum. `critical` / `major` / `minor`.
  - `observation`: string.
  - `methodology_reference`: string.
  - `required_action`: string.
- `sample_re_perform_results`: array of objects with `sample_id`, `original_outcome`, `qa_outcome`, `divergence_flag`.
- `severity_calibration_check`: object with `floor_violations` (array), `analogous_comparisons` (array), `commentary` (string).
- `conclusion_support_assessment`: object with `assessment` (enum: `supported` / `partially-supported` / `not-supported`), `rationale` (string).
- `decision`: enum. `accept` / `return-for-rework` / `conditional-accept`.
- `rework_items`: array of strings (populated when decision is conditional or return).
- `issue_closure_approval`: enum. `approved` / `not-approved` / `not-applicable`.
- `reviewer_questions`: array of strings.
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `human_review_required`: boolean. Always true (QA itself is reviewable).

## Example scenarios

### Scenario 1: QA review of a Reg E error-resolution workpaper

Input: a regional bank's QA reviewer is reviewing the completed Reg E error-resolution workpaper. The workpaper concluded design-effective and operating-partially-effective. The QA reviewer is comparing the workpaper to the firm CMS testing methodology and to AU-C 230 / 530 expectations.

Output emphasizes:
- Six deficiencies found:
  - One critical: preparer and reviewer are the same role on the sign-off block (reviewer-separation failure). Workpaper returned.
  - One major: three sample items show "investigation completed" with no evidence ID; the workpaper's exception register did not flag them as evidence gaps. Category: evidence-reliability and exception-classification.
  - One major: conclusion language says "the bank did not comply with Reg E §1005.11(c)" — legal-violation framing. Category: conclusion-support. Required rewrite to control-effectiveness language.
  - Two minor: missing population reconciliation total; missing reliance classification on case-management system extracts.
  - One minor: aggregation section missing stratum-level breakdown though sample was stratified.
- Sample re-perform: QA re-performed five sample items; one re-perform identified a deviation the preparer missed.
- Severity calibration: preparer rated all timing deviations medium; firm methodology floor for Reg E §1005.11(c) timing is high. Severity inflation requested.
- Decision: return for rework with specific rework items listed.
- QA confidence label high.

### Scenario 2: Examiner-prep QA sweep on a portfolio of TPRM workpapers

Input: a Federal Reserve targeted exam on third-party risk is six weeks out. The second-line QA function is doing an examiner-prep sweep on the 14 TPRM workpapers from the most recent testing cycle. Source posture is interagency TPRM guidance (June 2023) [verify section] plus firm TPRM methodology.

Output emphasizes:
- Per-workpaper QA notes batched into one summary review.
- Common deficiencies across the population:
  - Evidence-reliability: vendor-supplied SOC 2 reports cited as evidence without the firm's reliance assessment documented.
  - Conclusion-support: 4 of 14 workpapers conclude on critical-vendor monitoring without any evidence of the firm's KRI dashboard for that vendor.
  - Severity calibration: 2 of 14 workpapers rate exit-plan-testing absence as medium; firm methodology floor (and supervisory expectation) is high.
- Aggregate severity: 1 critical, 5 major, 14 minor.
- Decision: 9 accepted with minor noted; 4 conditional accept (rework items listed); 1 returned (the critical-vendor-no-monitoring conclusion).
- Issue closure approval status flagged on 3 workpapers as "not-approved" pending rework.
- Reviewer questions to the original reviewers focus on: documenting reliance on SOC 2 reports, evidencing the KRI dashboard tie-out, severity floor reconciliation.
- QA confidence label medium overall (the population shows methodology drift across reviewers, suggesting a methodology refresh is needed before the next cycle).

## Common pitfalls

1. QA as proofreading. Spelling and formatting are minor deficiencies. The QA's job is methodology rigor: scope-alignment, evidence reliability, procedure execution, exception classification, conclusion support.
2. Letting the QA reviewer also be the workpaper reviewer. Same problem as preparer-reviewer overlap. The QA reviewer must be independent of the original review.
3. Severity inflation in QA notes ("everything is critical"). The severity scale (critical / major / minor) has consequences: critical returns the workpaper. Use it only for things that fail the experienced-auditor sufficiency standard or break methodology floors.
4. Skipping sample re-perform on high-stakes workpapers. The QA is most credible when it has independently re-performed a small subsample.
5. Confusing workpaper closure with issue closure. A clean workpaper documents the test; the issues identified still have remediation lifecycles in `risk-compliance-core/skills/issue-writeup` and downstream tracking. Closing the workpaper does not close the issue.
6. Treating QA as adversarial. The QA finding goes back to the workpaper reviewer, not the auditee. Tone is methodology-rigorous, not gotcha. Reviewer questions, not accusations.
