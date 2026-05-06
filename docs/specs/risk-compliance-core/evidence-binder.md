# evidence-binder — spec sheet

Plugin: `risk-compliance-core`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Builds an evidence binder index for a regulatory exam, internal audit, model validation, vendor review, or committee review. Output is an evidence index, one row per artifact, with system-of-record provenance, control coverage, completeness flag, and reviewer sign-off — not a folder of unlabeled screenshots.

Best for:
- Assembling the binder for a horizontal review (exam request list, internal audit fieldwork pack, validation evidence pack, vendor diligence pack, committee evidence pack).
- Reconciling an exam request list against available evidence and surfacing the gaps before the exam window opens.

Not the right tool when:
- The work is producing the underlying evidence (run the source-system report, run the test) — this skill indexes existing evidence.
- The work is drafting a finding from missing evidence (use `issue-writeup`).
- The work is the committee narrative itself (use `risk-reporting/skills/risk-committee-pack`).

Anchored to: BCBS 239 (January 2013) Principles 3, 4, 7 (accuracy, completeness, accuracy of reporting); SR 11-7 §V model documentation expectations [verify section]; FFIEC IT Examination Handbook, Audit booklet (April 2012) §III evidence sufficiency [verify section]; OCC Bulletin 2026-13 §III.D evidence and documentation [verify section]; AICPA AU-C 500 (audit evidence) for the underlying definitional framing of evidence sufficiency and appropriateness [verify section].

## Source anchors

Primary:
- BCBS 239, January 2013. Principles 3 (accuracy and integrity), 4 (completeness), 7 (accuracy of risk reporting). Use for: data-evidence completeness expectations, lineage requirements.
- SR 11-7, April 4, 2011. §V (model validation) and §VI (governance and documentation). Use for: model-validation binder evidence requirements (development data, code, validation tests, ongoing monitoring records). [verify section labels]
- FFIEC IT Examination Handbook, Audit booklet, April 2012. §III (audit programs and procedures), §IV.B (evidence and documentation). Use for: audit-binder evidence sufficiency posture, retention expectations. [verify section labels]
- OCC Bulletin 2026-13, 2026 — refreshed model risk guidance. §III.D documentation expectations [verify]; §III.E independent challenge evidence [verify].
- AICPA AU-C 500, audit evidence — for evidence sufficiency and appropriateness framing referenced by internal audit functions. [verify section labels]

Secondary (overlay only):
- ISO/IEC 42001:2023 §7.5 documented information and §9 performance evaluation, for AI-management-system evidence binders. [verify section labels]
- DORA (Regulation (EU) 2022/2554) Article 28 ICT third-party documentation expectations [verify], when the binder is being assembled for an EU ICT register review.

## Sector overlays needed

- `banking.md` — Covers OCC heightened standards [verify], FFIEC IT booklet retention expectations, supervisory exam request list (RFI) common shape.
- `insurance.md` — Covers NAIC Model Audit Rule §16 [verify] internal-control evidence and ORSA evidence expectations; state DOI exam request shape.
- `capital-markets.md` — Covers SEC Rule 17a-4 / FINRA 4511 [verify] recordkeeping evidence, FINRA Books and Records exam request shape, and SEC OCIE / EXAMS evidence list patterns.
- `payments-fintech.md` — Covers OCC fintech bank-partnership exam evidence patterns [verify] and FDIC-supervised partner-bank evidence requests.

## Cross-cutting overlays needed

- `cyber.md` — Required when the binder covers a cyber-incident or NYDFS Part 500 review. Anchors: NYDFS Part 500 §500.16 incident response, §500.17 reporting; SEC Reg S-K Item 106 [verify] and Form 8-K Item 1.05 disclosure evidence.
- `privacy.md` — Optional, when the binder covers a privacy-program review. Anchors: GLBA Safeguards (16 CFR 314) [verify], state privacy laws.
- `climate.md` — Not required at v1.
- `conduct.md` — Optional, when the binder covers a UDAAP or fair-lending exam. Anchors: CFPB UDAAP exam manual [verify].

## Output template named sections

Top of artifact:
- Binder purpose (regulator exam, audit fieldwork, validation, vendor review, committee)
- Scope (entity, process, period covered, examiner / reviewer)
- Source posture and confidence label
- Request list (when assembled against an exam RFI)

Body — the index itself, one row per evidence item, with these named columns:
- Evidence ID
- Evidence type (system report, screenshot, sign-off log, sample workpaper, policy version, contract, training record, attestation, meeting minutes, other)
- Description
- System of record (named system, not "internal database")
- Date generated
- Period covered
- Linked obligation IDs
- Linked control IDs
- Linked issue IDs (if remediation evidence)
- Custodian (named role)
- Sensitivity (public, internal, confidential, restricted)
- Provenance trail (extract method, who pulled, when)
- Completeness flag (complete, partial, gap)
- Reviewer sign-off

Tail of artifact:
- Evidence gaps (request items with no evidence)
- Provenance concerns (items where source-of-record is unclear)
- Recommended owner actions
- Source trace and confidence label
- Sign-off block

## Structured output fields

Wrapper object:
- `binder_id`: string.
- `binder_purpose`: enum. `regulator-exam`, `internal-audit`, `model-validation`, `vendor-review`, `committee-pack`, `other`.
- `scope`: object. `entity`, `process`, `period_start`, `period_end`, `reviewer` (all string).
- `request_list`: array of objects with `request_id` (string), `request_text` (string), `status` (enum: `met`, `partial`, `gap`).
- `evidence_items`: array of evidence-item objects.
- `evidence_gaps`: array of objects with `request_id` and `gap_description`.
- `confidence_label`: enum.
- `reviewer_questions`: array of strings.
- `human_review_required`: boolean. Always true.

Evidence-item object (new schema, phase 2 should add as `schemas/evidence.schema.json`):
- `evidence_id`: string.
- `evidence_type`: enum.
- `description`: string.
- `system_of_record`: string.
- `date_generated`: string (ISO date).
- `period_start`, `period_end`: strings.
- `linked_obligation_ids`: array of strings.
- `linked_control_ids`: array of strings.
- `linked_issue_ids`: array of strings.
- `custodian`: string (role).
- `sensitivity`: enum (`public`, `internal`, `confidential`, `restricted`).
- `provenance`: object with `extract_method` (string), `extracted_by` (string, role), `extracted_at` (string, ISO datetime).
- `completeness_flag`: enum (`complete`, `partial`, `gap`).
- `reviewer_signoff`: object with `reviewer` (string, role), `signed_at` (string, ISO datetime), `comments` (string).

## Example scenarios

### Scenario 1: SR 11-7 model validation evidence pack

Input: model risk team is preparing the validation evidence pack for an internal credit-decisioning model up for annual revalidation. Source posture is SR 11-7 plus OCC 2026-13 plus the firm's MRM policy.

Output emphasizes:
- Evidence index rows grouped by SR 11-7 §V validation activity (conceptual soundness, ongoing monitoring outcomes, outcomes analysis, benchmarking).
- System-of-record column distinguishes development data extracts (date-stamped, lineage-traced) from validation re-runs.
- Provenance column flags one row where extract method is "manually copied to spreadsheet" — completeness flag is partial.
- Evidence gaps section flags missing benchmarking against an external dataset for the most recent vintage.
- Confidence label medium; reviewer questions ask whether the prior validation cycle's monitoring records were retained per the firm's MRM retention schedule.

### Scenario 2: SEC cyber 8-K disclosure-readiness binder

Input: a registrant's CISO and disclosure committee are assembling the evidence binder for the next 8-K Item 1.05 readiness review. Source posture is SEC cyber rules plus the firm's incident-response policy.

Output emphasizes:
- Evidence index rows grouped by disclosure-decision step (incident intake, materiality assessment, disclosure committee review, board notification, draft 8-K language).
- Cyber overlay applied: incident-timeline source-system reference, materiality memo with named author and date, legal review log.
- Provenance trail names the SIEM / ticketing system pulling the timeline.
- Sensitivity flagged on the materiality memo as restricted (legal-privileged).
- Evidence gaps section flags absence of a board-notification log for the most recent tabletop exercise.

## Common pitfalls

1. Treating a screenshot as evidence without the underlying system-of-record link. A screenshot proves something was visible on a screen, not that the underlying record exists, is current, or matches the population. Every screenshot row needs a paired system-of-record reference.
2. Mixing evidence and assertions. A management memo asserting "controls are operating effectively" is an assertion, not evidence. The binder must either capture both with explicit type tags or omit the assertion.
3. Stale period coverage. Evidence pulled six months before the period under review fails the timeliness test. The period_start / period_end fields exist to make this catchable.
4. Custodian set to a team. "Compliance" is not a custodian. The custodian field is a named role accountable for the evidence's integrity (e.g., Head of Model Risk Reporting).
5. Hidden gaps. Phase 2 must enforce that every request_list item is matched to evidence_items or surfaced in evidence_gaps. A clean binder with no gaps and no request_list reconciliation is unauditable.
