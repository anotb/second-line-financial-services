# issue-writeup — spec sheet

Plugin: `risk-compliance-core` (canonical home; v0.2 duplicate in `compliance-testing` is dropped)
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Drafts a finding write-up using the standard condition / criteria / cause / effect (CCCE) structure plus severity rationale, remediation, owner, target date, and evidence-gap flag. Output is a one-issue artifact written to the shape an audit committee, regulator, or issue-tracking system will accept.

Best for:
- Drafting a finding from an internal audit fieldwork test, a compliance test exception, a vendor-monitoring exception, or a model-validation finding.
- Translating an MRA / MRIA letter or examiner-issued matter into the firm's internal issue format with traced criteria.

Not the right tool when:
- The work is a multi-issue summary (use `risk-reporting/skills/risk-committee-pack` for committee narrative, or assemble multiple issue-writeup outputs).
- The work is the test that produces the exception (use `compliance-testing/skills/control-test-workpaper`).
- The work is an unconfirmed observation (issues require a confirmed condition; observations belong elsewhere).

Anchored to: IIA International Professional Practices Framework, Standard 2410 (criteria for communicating engagement results) [verify section]; OCC Bulletin 2014-39 (matters requiring attention) [verify section]; FRB SR 13-13 [verify] supervisory letter framework for matters requiring attention; FFIEC IT Examination Handbook, Audit booklet (April 2012) §IV.C reportable conditions [verify section]; AICPA AU-C 265 (communicating internal control related matters) [verify section] for the criteria-condition-cause-effect framing as applied in financial-services internal control reporting.

## Source anchors

Primary:
- IIA IPPF, Standard 2410, "Criteria for Communicating." Use for: structure of an audit communication (criteria, condition, cause, effect, recommendation). [verify section labels]
- OCC Bulletin 2014-39 — supervisory matters requiring attention (MRA) and matters requiring immediate attention (MRIA). Use for: severity calibration when the issue is being drafted in response to an examiner letter. [verify section labels]
- FRB SR 13-13 — supervisory considerations for the communication of supervisory findings. Use for: severity and escalation framing. [verify section labels]
- FFIEC IT Examination Handbook, Audit booklet, April 2012. §IV.C reportable conditions and §IV.D follow-up. Use for: closure-evidence and remediation tracking expectations. [verify section labels]
- AICPA AU-C 265 — communicating internal control related matters, applied as the underlying CCCE framing. [verify section labels]

Secondary (overlay only):
- BCBS 239 §V supervisory expectations [verify] — when the issue is a risk-data-reporting deficiency.
- OCC Bulletin 2026-13 §III.D documentation [verify] — when the issue is a model-risk finding.

## Sector overlays needed

- `banking.md` — Covers OCC MRA/MRIA framework, FRB supervisory finding framework, FDIC supervisory letter shape; severity conventions for federally regulated institutions.
- `insurance.md` — Covers NAIC examination findings format and state DOI MOU / consent agreement language patterns [verify].
- `capital-markets.md` — Covers SEC EXAMS deficiency letter format [verify], FINRA Letter of Caution / Examination Finding shape [verify], and broker-dealer / adviser remediation conventions.
- `payments-fintech.md` — Covers OCC fintech / bank-partnership supervisory letter conventions [verify], and CFPB UDAAP supervisory recommendation patterns.

## Cross-cutting overlays needed

- `cyber.md` — Optional, when the issue is a cyber control deficiency. Anchors: NYDFS Part 500 §500.3, §500.5, §500.7; FFIEC IT booklet.
- `privacy.md` — Optional, when the issue is a privacy-program deficiency.
- `climate.md` — Not required at v1.
- `conduct.md` — Optional, when the issue concerns customer-facing harm. Anchors: CFPB UDAAP exam manual [verify section]. Severity rationale shifts when customer harm is identifiable.

## Output template named sections

Top of artifact:
- Issue ID and title
- Source (audit engagement ID, exam letter ID, regulator, control test ID, vendor monitoring exception, validation finding)
- Date identified, period covered
- Source posture and confidence label

Body — the CCCE structure plus severity:
- Condition (what was observed; specific, dated, scoped)
- Criteria (the standard or rule the condition is measured against; named source with section)
- Cause (root cause, not surface symptom; tied to control design or operation)
- Effect / impact (financial, customer, regulatory, operational, reputational; quantified where possible)
- Severity rating (low / moderate / high / critical) with rationale
- Population and sample (when issue arose from a sample)
- Linked obligation IDs
- Linked control IDs
- Linked evidence IDs

Remediation:
- Recommended action (declarative; what owner must do)
- Owner (named role)
- Target date
- Closure evidence (what will be inspected to verify closure)
- Interim mitigation (if any)

Tail:
- Evidence gap flag (yes / no)
- Reviewer questions
- Source trace
- Sign-off block

## Structured output fields

Schema: `schemas/issue.schema.json` (existing). Phase 2 should extend with:
- `title` (already present, keep)
- `source` (object): `source_type` (enum: `internal-audit`, `compliance-testing`, `vendor-monitoring`, `model-validation`, `examiner-letter`, `self-identified`, `whistleblower`, `other`), `source_id` (string), `regulator` (string, optional).
- `date_identified`, `period_start`, `period_end` (ISO date strings).
- `population_size` (integer, optional), `sample_size` (integer, optional), `exceptions_observed` (integer, optional).
- `linked_obligation_ids` (array of strings).
- `linked_control_ids` (array of strings).
- `linked_evidence_ids` (array of strings).
- `criteria_source_anchor` (string).
- `closure_evidence` (array of strings).
- `interim_mitigation` (string, optional).
- `severity_rationale` (string).
- `mra_mria_classification` (enum, optional): `MRA`, `MRIA`, `n/a`.
- `confidence_label` (enum).
- `human_review_required` (boolean, always true for severity assignment).

Existing fields kept: `issue_id`, `condition`, `criteria`, `cause`, `impact`, `severity`, `remediation`, `owner`, `target_date`, `evidence_gap`.

## Example scenarios

### Scenario 1: BCBS 239 risk-reporting completeness exception

Input: an internal audit team has tested the monthly market-risk pack against BCBS 239 Principle 4 (completeness) and identified that two material counterparty exposures were excluded from the consolidated view because of a feed timing mismatch.

Output emphasizes:
- Condition is dated and quantified: feed mismatch on three reporting cycles, exposures totaling [amount, supplied by user] omitted.
- Criteria cites BCBS 239 Principle 4 and Principle 7 (accuracy of risk reporting), with the section reference.
- Cause is the feed-orchestration cutoff time, not "human error"; tied to a specific control activity in the data-reconciliation matrix.
- Effect quantifies the under-stated counterparty exposure metric and notes the downstream impact on the executive risk pack.
- Severity is high; rationale ties to materiality threshold, repeated occurrence, and committee-pack consumption.
- Closure evidence: revised feed schedule, two cycles of reconciled output, sign-off by head of market risk reporting.
- MRA / MRIA classification is n/a (internal audit issue, not examiner letter).

### Scenario 2: TPRM critical-vendor SOC 2 finding remediation

Input: vendor monitoring found that a critical fraud-screening vendor's most recent SOC 2 Type II report has a qualified opinion on logical access controls, with no firm-side compensating control documented.

Output emphasizes:
- Condition: SOC 2 Type II qualified opinion on CC6.1 (logical access), reporting period [period], with no documented firm-side compensating control as of [date].
- Criteria: U.S. interagency third-party risk management guidance §III.D ongoing monitoring; firm's third-party policy §[verify].
- Cause: gap in vendor-monitoring control activity — SOC 2 reports are received but not reviewed for qualified opinions against a firm-side compensating-control matrix.
- Effect: residual risk exposure on customer-data access at the vendor; potential consumer-data implication; cyber overlay flagged.
- Severity is high; rationale ties to vendor criticality, customer-data exposure, and absence of compensating control.
- Recommended action: document compensating control or initiate vendor remediation tracking; assign to head of vendor management with a 60-day target.
- Linked obligation IDs reference the TPRM ongoing monitoring obligation; linked control IDs reference the SOC 2 review control.

## Common pitfalls

1. Confusing condition with cause. "The control failed" is not a condition; it is a conclusion. The condition is the dated, scoped, observable state. Phase 2 SKILL.md must reject merged condition-and-cause text.
2. Generic criteria. "Per firm policy" is not a citable criterion. Criteria must name the source (rule, guidance, standard, internal policy with section) and provide an anchor that the reviewer can read.
3. Surface-level cause. "Human error" or "training gap" is rarely the root cause. Phase 2 should require the cause to tie to a specific control design or operation weakness.
4. Severity inflation or deflation. Severity without rationale is a number, not a finding. The severity_rationale field is mandatory and must reference materiality, frequency, customer impact, or regulatory exposure.
5. Closure evidence is the artifact, not an action. "Remediated" is not closure evidence. The closure_evidence field names what will be inspected (e.g., "two consecutive months of reconciled feed output and head-of-reporting sign-off log").
6. Missing MRA / MRIA classification when issue is regulator-sourced. If the issue source is an examiner letter, the classification field must be populated; phase 2 should make this conditional.
