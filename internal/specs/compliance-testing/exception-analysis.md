# exception-analysis — spec sheet

Plugin: `compliance-testing`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Classifies control deviations identified during testing — distinguishing isolated misses from systemic issues, design gaps from operating-effectiveness gaps, evidence gaps from genuine control failures, and disagreements over criteria from real exceptions. Output is an exception register with severity ranking, root-cause hypothesis, and a handoff package to issue write-up.

Best for:
- A compliance-testing or audit reviewer has finished sample testing and is sitting on a list of deviations that need to be classified before they become findings.
- A QA reviewer is challenging a workpaper's exception treatment because the line between "evidence gap" and "control failure" was blurred.
- A repeat-issue review needs to confirm whether deviations across testing cycles are the same root cause or coincidental.

Not the right tool when:
- The test has not been run yet (use `test-plan-builder`, then `workpaper-drafter`).
- The exception has already been classified and the work is drafting the issue (use `risk-compliance-core/skills/issue-writeup`; this skill produces the input that `issue-writeup` consumes).
- The work is QAing the workpaper end-to-end (use `qa-workpaper`).

Anchored to: IIA Performance Standard 2410 (Criteria for Communicating) and the IPPF guidance on root-cause analysis [verify section]; AICPA AU-C 530, Audit Sampling §A18-A22 (evaluating sample results) [verify paragraph]; AICPA AU-C 265, Communicating Internal Control Related Matters Identified in an Audit [verify paragraph]; SR 08-8 (Federal Reserve, October 2008) on issue identification expectations within a compliance risk management program [verify section]; OCC PPM 5310-3 [verify exact reference and date]; CFPB Compliance Management System Review Procedures, monitoring and corrective-action sections [verify section].

## Source anchors

Primary:
- IIA International Professional Practices Framework — Performance Standard 2410 (Criteria for Communicating). Use for: framing what counts as a finding (criteria, condition, cause, effect) and the methodology bar for root-cause analysis. [verify section labels against current IPPF release]
- AICPA AU-C 530, Audit Sampling §A18-A22 (evaluating sample results). Use for: methodology anchor on projecting deviations to the population and distinguishing anomalies from systemic issues. [verify paragraph references]
- AICPA AU-C 265, Communicating Internal Control Related Matters. Use for: severity framing (deficiency / significant deficiency / material weakness analogues) — borrowed methodology in second-line testing, not a direct legal standard. [verify paragraph references]
- SR 08-8 (Federal Reserve, October 16, 2008). Use for: program-level expectations on issue identification, escalation, and tracking. [verify section labels]
- CFPB Compliance Management System Review Procedures. Use for: monitoring and corrective-action expectations. [verify section labels]

Secondary (overlay only):
- COSO 2013 Internal Control — Integrated Framework, Principle 17 (Evaluates and Communicates Deficiencies). [verify principle reference]
- OCC PPM 5310-3 (compliance management systems for OCC-supervised banks). [verify exact reference and current effective date]
- FFIEC IT Examination Handbook, Audit booklet (April 2012) §IV.D (evaluating audit findings) [verify section labels].

## Sector overlays needed

- `banking.md` — MRA / MRIA terminology context (Federal Reserve supervisory tools; do not invent a regulator-issued MRA — second-line drafts in the same shape so the firm's record-keeping aligns with examiner vocabulary). Heightened-standards bank context (12 CFR Part 30 Appendix D §III) [verify].
- `insurance.md` — State DOI market-conduct exception conventions [verify]; NAIC Model Audit Rule (Model #205) [verify section] severity framing for ICFR-relevant findings.
- `capital-markets.md` — FINRA 3110 / 3120 / 3130 [verify] supervision exception treatment; SEC enforcement-style language hygiene (avoid claims of legal violation).
- `payments-fintech.md` — Sponsor-bank oversight exception conventions; Reg E error-resolution exception treatment.

## Cross-cutting overlays needed

- `cyber.md` — Required. Cyber exceptions need careful classification because evidence gaps (no log) often look like control failures. Anchors: NIST SP 800-53 [verify] control-effectiveness language, NYDFS Part 500 §500.16 incident-response.
- `privacy.md` — Optional, for GLBA Safeguards exceptions [verify 16 CFR 314.4].
- `climate.md` — Not required at v1.
- `conduct.md` — Required when sampling consumer-impact populations. UDAAP exceptions need consumer-harm framing distinct from technical control deviation. CFPB UDAAP exam manual [verify section].

## Output template named sections

1. Scope and source posture
   - Test ID, related control ID, related obligation ID, jurisdiction, period under test, source posture.
2. Exception register (numbered, one row per deviation)
   - Exception ID
   - Sample ID and population reference
   - Criterion (named: rule, policy section, methodology)
   - Condition (what the test observed)
   - Classification: control-failure / design-gap / evidence-gap / scope-disagreement / data-integrity / anomaly
   - Severity rating (low / medium / high / critical) with rationale
   - Root-cause hypothesis (people / process / technology / data / governance)
   - Repeat-issue flag and prior-issue ID if any
3. Aggregation and projection
   - Deviation rate observed vs. tolerable deviation rate
   - Population projection commentary (anomaly vs. systemic)
   - Stratum-level breakdown if stratified sample
4. Disposition
   - Items elevated to issue write-up (with handoff fields populated)
   - Items closed at exception level with rationale (e.g., evidence re-supplied and reviewed)
   - Items requiring re-test or expanded sample
5. Reviewer sign-off
   - Reviewer role, reviewer questions, sign-off date placeholder.
6. Handoff package to `risk-compliance-core/skills/issue-writeup`
   - For each elevated exception, the populated fields the issue-writeup skill needs (criterion, condition, cause, effect, recommendation seed).
7. Source trace and confidence label
   - Anchored standards, firm methodology references, confidence label.

## Structured output fields

Schema: new `exception.schema.json` (Phase 2 to add). The handoff to `issue-writeup` populates `issue.schema.json` (existing in `risk-compliance-core`).

Wrapper object:
- `analysis_id`: string.
- `test_id`: string. Foreign key into `test-plan.schema.json`.
- `workpaper_id`: string. Foreign key into the workpaper (workpaper-drafter output).
- `exceptions`: array of objects, each with:
  - `exception_id`: string.
  - `sample_id`: string.
  - `criterion_source`: string.
  - `condition`: string.
  - `classification`: enum. `control-failure` / `design-gap` / `evidence-gap` / `scope-disagreement` / `data-integrity` / `anomaly`.
  - `severity`: enum. `low` / `medium` / `high` / `critical`.
  - `severity_rationale`: string.
  - `root_cause_hypothesis`: object with `category` (enum: `people` / `process` / `technology` / `data` / `governance`) and `description` (string).
  - `repeat_issue`: boolean.
  - `prior_issue_id`: string (nullable).
  - `disposition`: enum. `elevated-to-issue` / `closed-at-exception` / `re-test-required` / `expanded-sample-required`.
  - `issue_handoff`: object (populated when disposition is `elevated-to-issue`) with seed fields for `issue.schema.json`.
- `aggregation`: object with `deviation_rate_observed` (number 0-1), `tolerable_deviation_rate` (number 0-1), `projection_commentary` (string), `stratum_breakdown` (array).
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `reviewer_questions`: array of strings.
- `human_review_required`: boolean. Always true.

Phase 2 should add `exception.schema.json` and a foreign key field on `issue.schema.json` for `source_exception_id`.

## Example scenarios

### Scenario 1: Reg E error-resolution exception classification for a regional bank

Input: compliance-testing has run a Reg E error-resolution test (12 CFR 1005.11) [verify section] on 50 sampled disputes. Six deviations identified: three exceeded the 10-business-day provisional credit window; two had no investigation notes in the case file but had system-logged status changes; one had a different fee reversal amount than the case file documented.

Output emphasizes:
- The three timing deviations classify as `control-failure`, severity high, root-cause hypothesis on the dispute-routing queue's SLA monitor (technology).
- The two missing-notes deviations classify as `evidence-gap` rather than control-failure: system logs show the investigation occurred. Severity medium, root-cause hypothesis on case-management training (people / process). Disposition: closed-at-exception once supplemental evidence (system logs) was reviewed; one of the two flagged for `re-test-required` next cycle to verify the documentation is now happening.
- The fee-amount deviation classifies as `data-integrity`, severity medium, root-cause hypothesis on the reconciliation between the dispute case-management system and core deposit ledger.
- Aggregation: observed deviation rate 12% vs. tolerable 5%; projection commentary notes the timing failures concentrate in one channel (online disputes), suggesting systemic rather than anomaly.
- Three exceptions elevated to issue write-up with handoff package populated.
- Confidence label high; reviewer question on whether the timing-failure root cause warrants its own issue separate from the documentation-gap issue.

### Scenario 2: Logical-access recertification exception classification, NYDFS Part 500 testing

Input: second-line cyber testing has run the quarterly access-recertification control test on 30 packets. Eight deviations identified: four packets had blanket "approved" responses with no per-entitlement review; two packets were completed after the 30-day deadline; one privileged-access packet had a removed user not actually revoked in the IAM system; one packet was for a user no longer employed.

Output emphasizes:
- The four blanket-approval deviations classify as `design-gap` (the form does not require per-entitlement attestation), severity high. Disposition: elevated to issue write-up; this is a control design problem, not a one-off operating miss.
- The two timing deviations classify as `control-failure`, severity medium.
- The one un-revoked privileged access classifies as `control-failure`, severity critical (per the firm's policy floor on privileged access). Repeat-issue flag is on; prior-issue ID linked. Elevated immediately with severity critical.
- The terminated-employee packet classifies as `data-integrity` (HR-IAM feed lag), severity high; root cause spans HR offboarding and IAM provisioning (governance). Elevated.
- Aggregation: observed deviation rate 27% vs. tolerable 5% on standard, 0% on privileged; population projection notes the design-gap finding affects 100% of packets, not just sampled ones.
- Confidence label high on classification, medium on severity ranking for the un-revoked access (firm policy floor versus regulator expectation).

## Common pitfalls

1. Treating every deviation as a finding. Deviations classify into six buckets in this skill; not all become issues.
2. Confusing evidence gap with control failure. If the system did the right thing but the evidence is missing, the issue is documentation, not control operation. Severity and remediation differ.
3. Skipping root-cause hypothesis. A finding without a root cause is unactionable. The skill names a hypothesis (people / process / technology / data / governance) so the issue-writeup recommendation has somewhere to attach.
4. Projecting anomalies. AU-C 530 §A22 [verify paragraph] reminds reviewers that a deviation can be an anomaly only when there is positive evidence it is non-recurring. Default to systemic; demand evidence to downgrade.
5. Severity inflation by the first-line owner ("we'll just self-identify it high") to avoid examiner attention. The severity rationale field is the reviewer's tool to keep the rating defensible.
6. Skipping the handoff package. The whole point of this skill is to make `issue-writeup` (in `risk-compliance-core`) easy. If the handoff fields are empty, the writeup will be re-discovered work.
