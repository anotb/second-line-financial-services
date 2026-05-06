# workpaper-drafter — spec sheet

Plugin: `compliance-testing`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Drafts a control-test workpaper from completed testing: source criteria, evidence inspected, procedures performed, results per sample item, exceptions identified, conclusion on design and operating effectiveness, reviewer questions. Output is the standard testing workpaper that examiners and QA reviewers expect, formatted so each conclusion ties back to evidence.

Best for:
- A compliance-testing or internal-audit team has completed evidence inspection and procedure execution and needs the workpaper drafted from those results.
- A second-line reviewer is documenting a targeted review (e.g., regulatory-change triggered) and needs the testing workpaper as the artifact.
- A QA reviewer is rebuilding a workpaper that failed prior QA — same evidence, restated workpaper.

Not the right tool when:
- Testing has not been done yet (use `test-plan-builder`, `control-sampling`, `evidence-request-builder` first).
- The work is QA on a completed workpaper (use `qa-workpaper`). The boundary: `workpaper-drafter` writes the workpaper from results; `qa-workpaper` reviews the completed workpaper for sufficiency. Sequential.
- Exceptions need classification before they go in the workpaper conclusion (use `exception-analysis`; this skill consumes its register).

Anchored to: IIA Performance Standard 2330 (Documenting Information) [verify section]; AICPA AU-C 230, Audit Documentation [verify paragraph]; AICPA AU-C 500, Audit Evidence [verify paragraph]; AICPA AU-C 530, Audit Sampling §A18-A22 (evaluating sample results) [verify paragraph]; FFIEC IT Examination Handbook, Audit booklet (April 2012) §IV (audit testing) and §V (audit communication) [verify section]; SR 08-8 (Federal Reserve, October 2008) [verify section]; OCC PPM 5310-3 [verify exact reference and date].

## Source anchors

Primary:
- IIA International Professional Practices Framework — Performance Standard 2330 (Documenting Information). Use for: workpaper completeness, retention, supervision-review expectations. [verify section labels against current IPPF release]
- AICPA AU-C 230, Audit Documentation. Use for: methodology anchor on documentation that is sufficient for an experienced auditor with no prior connection to the engagement to understand the work performed and conclusions reached. [verify paragraph references]
- AICPA AU-C 500, Audit Evidence. Use for: framing the link between evidence and conclusion. [verify paragraph references]
- AICPA AU-C 530, Audit Sampling. Use for: documenting evaluation of sample results. [verify paragraph references]
- FFIEC IT Examination Handbook, Audit booklet, April 2012, §IV (audit testing) and §V (audit communication). [verify section labels]
- SR 08-8 (Federal Reserve, October 16, 2008). Use for: testing-program documentation expectations. [verify section labels]

Secondary (overlay only):
- OCC PPM 5310-3 (compliance management systems for OCC-supervised banks). [verify exact reference and current effective date]
- COSO 2013 Internal Control — Integrated Framework, Principle 17. [verify principle reference]

## Sector overlays needed

- `banking.md` — Bank-specific workpaper conventions for HMDA, Reg DD, Reg E, Reg Z, BSA/AML; CRA testing workpaper structure; CFPB CMS exam-cycle workpaper expectations [verify].
- `insurance.md` — NAIC Model Audit Rule (Model #205) [verify section] documentation conventions for ICFR-relevant tests; state DOI market-conduct workpaper conventions.
- `capital-markets.md` — FINRA 3120 / 3130 [verify] supervisory testing workpaper conventions; SEC Rule 17a-4 / FINRA 4511 recordkeeping evidence treatment.
- `payments-fintech.md` — Sponsor-bank workpaper conventions; Reg E error-resolution case-file documentation; payments-operations reconciliation workpapers.

## Cross-cutting overlays needed

- `cyber.md` — Required when the workpaper covers cyber controls. Anchors: NYDFS Part 500 §500.7 evidence types, FFIEC IT booklet, NIST SP 800-53A control-test documentation conventions [verify].
- `privacy.md` — Optional, for GLBA Safeguards testing workpapers [verify].
- `climate.md` — Not required at v1.
- `conduct.md` — Required when the workpaper covers consumer-facing testing. CFPB UDAAP exam manual conventions [verify section]; consumer-harm framing distinct from technical control conclusion.

## Output template named sections

Standard testing workpaper sections (the artifact a regulator or QA reviewer expects):

1. Header
   - Workpaper ID, test ID, control ID, obligation ID, period under test, business unit, jurisdiction, preparer, preparer date, reviewer, reviewer date.
2. Scope and source posture
   - Scope statement, source posture, reference to test plan.
3. Source criteria
   - Named criteria with section references; verbatim or paraphrased excerpts as needed.
4. Walkthrough summary
   - Roles interviewed, processes observed, screens inspected, walkthrough date, walkthrough conclusion (design effectiveness signal).
5. Evidence inspected
   - Numbered evidence list with reliance classification and reconciliation to the evidence request list.
6. Procedures performed
   - Each procedure (matched to the test plan) with execution notes and procedure-level conclusion.
7. Sample-level results
   - Sample table: sample ID, evidence reviewed, procedure outcome per sample, exception flag.
8. Exceptions identified
   - Reference to the exception register (`exception-analysis` output) with summary by classification and severity.
9. Aggregation and projection
   - Observed deviation rate vs. tolerable; population projection commentary; anomaly versus systemic call.
10. Conclusion
    - Design-effectiveness conclusion (effective / partially effective / not effective / inconclusive).
    - Operating-effectiveness conclusion (effective / partially effective / not effective / inconclusive).
    - Combined conclusion if requested by the test plan.
    - Conclusion language must avoid claims of legal violation; second-line conclusions are about control effectiveness, not legal opinion.
11. Issues elevated
    - List of issues handed off to `risk-compliance-core/skills/issue-writeup` with handoff package references.
12. Reviewer questions
    - Questions raised during testing or review for follow-up.
13. Limitations and reliance
    - Period coverage, scope exclusions, reliance on prior testing, reliance on management-prepared or vendor-supplied evidence.
14. Workpaper sign-off block
    - Preparer sign-off, reviewer sign-off (separate role), QA sign-off placeholder.
15. Source trace and confidence label
    - Anchored standards, firm methodology references, confidence label.

## Structured output fields

Schema: new `workpaper.schema.json` (Phase 2 to add).

Wrapper object:
- `workpaper_id`: string.
- `test_id`: string. Foreign key.
- `control_id`: string. Foreign key.
- `obligation_id`: string. Foreign key.
- `period_start`, `period_end`: string (ISO date).
- `business_unit`, `jurisdiction`: string.
- `preparer`: object with `role`, `date_prepared`.
- `reviewer`: object with `role`, `date_reviewed`, `sign_off_status`.
- `source_posture`: enum. `public-only` / `firm-policy-overlay` / `mixed`.
- `criteria`: array of objects with `source`, `section`, `text`.
- `walkthrough_summary`: object with `date`, `roles_interviewed`, `processes_observed`, `screens_inspected`, `design_conclusion_signal`.
- `evidence_inspected`: array of objects with `evidence_id`, `description`, `system_of_record`, `reliance_classification`, `request_id` (foreign key into evidence-request).
- `procedures_performed`: array of objects with `procedure_id`, `description`, `execution_notes`, `procedure_conclusion`.
- `sample_results`: array of objects with `sample_id`, `evidence_reviewed`, `procedure_outcomes` (object keyed by procedure_id), `exception_flag` (boolean), `exception_id` (nullable).
- `exception_register_id`: string. Foreign key into `exception.schema.json`.
- `aggregation`: object with `deviation_rate_observed`, `tolerable_deviation_rate`, `projection_commentary`.
- `conclusion`: object with `design_effectiveness` (enum: `effective` / `partially-effective` / `not-effective` / `inconclusive`), `operating_effectiveness` (same enum), `combined` (same enum, nullable).
- `issues_elevated`: array of objects with `issue_handoff_id` and `severity`.
- `reviewer_questions`: array of strings.
- `limitations`: array of strings.
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `human_review_required`: boolean. Always true.

## Example scenarios

### Scenario 1: HMDA LAR data-integrity workpaper for the annual compliance-testing cycle

Input: compliance-testing has completed the annual HMDA LAR data-integrity test (Reg C, 12 CFR 1003 [verify section]). Sample of 60 LAR records inspected against underlying loan files. Six exceptions previously classified by `exception-analysis`: two transposition errors on dollar amounts, three missing-data points (rate spread, lien position), one mismatched property-type code.

Output emphasizes:
- Header references test plan ID and the annual HMDA testing cycle.
- Source criteria cites Reg C 12 CFR 1003.4 (data points) [verify section] and the FFIEC HMDA Filing Instructions Guide [verify edition].
- Evidence inspected lists: LAR extract per sample ID; underlying loan file (URLA, AUS findings, rate-lock); demographic firewall evidence.
- Procedures performed include: re-perform of selected LAR fields against source documents; reconciliation of LAR to the loan-origination system extract.
- Sample-level results table flags 6 exceptions with cross-reference to the exception register.
- Aggregation: observed deviation rate 10% on data points vs. firm tolerable 3%; projection commentary calls out concentration in non-residential refinances.
- Conclusion: design-effectiveness effective; operating-effectiveness partially effective. Combined: not effective at the data-point level for the specific loan segment.
- Issues elevated: data-integrity issue on the rate-spread calculation queue; documentation issue on lien-position capture at origination.
- Confidence label high; reviewer question on whether the projection warrants resubmission consideration (escalates to the issue write-up, not concluded here).

### Scenario 2: NYDFS Part 500 access-recertification workpaper for second-line cyber testing

Input: second-line cyber testing has completed the quarterly access-recertification control test on 30 packets (NYDFS Part 500 §500.7 [verify], FFIEC IT booklet anchors). Eight exceptions classified by `exception-analysis`: one design gap (blanket-approval form), two operating misses (timing), one critical (un-revoked privileged), one data-integrity (terminated employee retained access), three documentation gaps.

Output emphasizes:
- Header references the cyber-testing program and NYDFS reporting cycle.
- Source criteria cites NYDFS Part 500 §500.7 (access privileges) [verify] and the firm's IAM control standard.
- Evidence inspected lists recertification packets, IAM entitlement extract, manager attestation logs, revocation tickets, HR offboarding feed.
- Procedures performed include: per-packet re-perform of attestation review; IAM-system reperformance for revocations; HR-IAM feed reconciliation for terminated employees.
- Sample-level results identify 8 exceptions and the design-gap finding.
- Aggregation: observed deviation rate 27% vs. firm tolerable 5% (standard) and 0% (privileged).
- Conclusion: design-effectiveness not effective (form does not enforce per-entitlement attestation); operating-effectiveness not effective. Combined: not effective.
- Issues elevated: design-gap issue, critical privileged-access issue (repeat issue), HR-IAM data-integrity issue.
- Limitations: workpaper does not test entitlement-provisioning at onboarding (separate control, separate workpaper).
- Confidence label high; reviewer question on whether the design-gap issue warrants notification under NYDFS Part 500 §500.17(b) [verify] in the next annual certification cycle (legal review required, not concluded here).

## Common pitfalls

1. Conclusions that are not tied to evidence. Every conclusion sentence must point to a procedure result that points to an evidence item. The workpaper's "experienced reviewer with no prior connection" test (AU-C 230) [verify paragraph] is the bar.
2. Mixing evidence inspection with conclusion language. Evidence inspected is what was looked at. Conclusions are what the look-at supports. Separate sections, no narrative blending.
3. Stating legal violations. Second-line workpapers conclude on control effectiveness, not legal compliance. Use "control did not operate as designed" or "evidence does not support the criterion" — not "the firm violated Reg X."
4. Forgetting reviewer separation. Preparer and reviewer must be different roles. A workpaper signed by the same person at preparer and reviewer is a QA fail.
5. Skipping limitations. The limitations section is the reviewer's protection: it explicitly names what the workpaper does not conclude on.
6. Workpaper drift from test plan. If the procedures executed do not match the test plan, either the plan must be amended pre-fieldwork (with reviewer sign-off) or the divergence must be documented as a scope change in the workpaper. Silent drift is a QA finding.
