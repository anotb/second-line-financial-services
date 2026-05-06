# evidence-request-builder — spec sheet

Plugin: `compliance-testing`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Drafts an evidence request list (sometimes called a PBC — provided-by-client — list, or evidence ask list) for a control test or examination. Each request line names the control objective being tested, the criterion the evidence supports, the artifact requested, the requested format, the system of record, the owner role, and the due date. Output is a numbered, traceable request list a first-line owner can fulfill and a reviewer can tie back to the test plan.

Best for:
- A compliance-testing or audit team has scoped a test and is preparing the evidence ask before fieldwork begins.
- A second-line reviewer is preparing for an examination and needs to anticipate the regulator's evidence asks against current control coverage.
- A QA reviewer is building a re-perform list to redo a workpaper because the original evidence trail was thin.

Not the right tool when:
- The test scope and procedures have not been written (use `test-plan-builder` first; this skill consumes its procedures).
- Evidence is in hand and the work is documenting test results (use `workpaper-drafter`).
- The work is QAing a completed workpaper for evidence sufficiency (use `qa-workpaper`).

Anchored to: IIA Performance Standard 2310 (Identifying Information) [verify section]; AICPA AU-C 500, Audit Evidence [verify paragraph]; FFIEC IT Examination Handbook, Audit booklet (April 2012) §IV (audit testing) and §V (audit communication) [verify section]; SR 08-8 (Federal Reserve, Compliance Risk Management Programs, October 2008) [verify section]; CFPB Compliance Management System Review Procedures [verify section]; OCC PPM 5310-3 [verify exact reference and date].

## Source anchors

Primary:
- IIA International Professional Practices Framework — Standard 2310 (Identifying Information). Use for: framing evidence sufficiency, reliability, and relevance in internal-audit-led testing. [verify section labels against current IPPF release]
- AICPA AU-C 500, Audit Evidence. Use for: methodology anchor on appropriate audit evidence (relevance and reliability), evidence from external sources, evidence about completeness. AU-C 500 is an external-audit standard; in second-line practice it is borrowed for methodology rigor. [verify paragraph references]
- FFIEC IT Examination Handbook, Audit booklet, April 2012, §IV (audit testing) and §V (audit communication). Use for: evidence-request hygiene in financial-services testing. [verify section labels]
- SR 08-8 (Federal Reserve, Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles, October 16, 2008). Use for: expectations on evidence collection in a compliance risk management program. [verify section labels]
- CFPB Compliance Management System Review Procedures (current Supervision and Examination Manual edition). Use for: CMS-context evidence ask conventions. [verify section labels]

Secondary (overlay only):
- COSO 2013 Internal Control — Integrated Framework, Principle 13 (Uses Relevant Information) and Principle 14 (Communicates Internally). [verify principle reference]
- OCC PPM 5310-3 (compliance management systems for OCC-supervised banks). [verify exact reference and current effective date]

## Sector overlays needed

- `banking.md` — Bank evidence conventions for compliance and consumer-protection testing (HMDA LAR pulls, Reg DD/Reg E disclosure samples, complaint-management evidence under CFPB CMS exam manual [verify section]).
- `insurance.md` — Claim-file evidence asks (state DOI market-conduct conventions [verify]); policy-file underwriting evidence; rate-filing supporting evidence.
- `capital-markets.md` — Order-blotter pulls, FINRA 4511 / SEC 17a-4 recordkeeping evidence [verify]; trade-surveillance log asks; communications-supervision evidence under FINRA 3110 [verify].
- `payments-fintech.md` — Sponsor-bank oversight evidence asks (third-party reporting packs under interagency TPRM 2023 §III.D [verify]); Reg E error-resolution case-file asks; payments operations reconciliations.

## Cross-cutting overlays needed

- `cyber.md` — Required when the test scopes cyber controls. Anchors: FFIEC IT booklet evidence conventions, NYDFS Part 500 §500.5 / §500.7 evidence types, NIST SP 800-53 control-evidence types [verify]. Common artifacts: vulnerability scans, access recertification packets, penetration-test reports, incident-response runbooks.
- `privacy.md` — Optional, for evidence asks tied to GLBA Safeguards Rule (16 CFR 314.4) [verify] or state privacy law testing.
- `climate.md` — Not required at v1.
- `conduct.md` — Optional, for UDAAP-related evidence asks (call recordings, complaint files, marketing-claim review records [verify CFPB UDAAP manual section]).

## Output template named sections

1. Scope and source posture
   - Test ID, related control ID, related obligation ID, jurisdiction, period under test, source posture.
2. Request summary
   - Number of requests, due dates, owner roles, escalation path.
3. Evidence request lines (numbered, one row per item)
   - Request ID
   - Control objective
   - Criterion (named source: rule, policy section, methodology)
   - Artifact requested (specific, not "all relevant documents")
   - Format requested (PDF, CSV with named columns, screenshot with timestamp, signed memo)
   - System of record / source location
   - Owner role
   - Due date
   - Population reference (sample ID or full-population pointer)
   - Reliance: original / vendor-supplied / management-prepared (drives reliability assessment)
   - Status placeholder (open / received / re-asked / closed)
4. Evidence-not-applicable section
   - Items intentionally not requested with rationale (avoids future re-ask).
5. Reviewer sign-off
   - Reviewer role, reviewer questions, sign-off date placeholder.
6. Source trace and confidence label
   - Anchored standards, firm methodology references, confidence label.

## Structured output fields

Schema: new `evidence-request.schema.json` (Phase 2 to add). Until then, output structures are nested under the test-plan schema.

Wrapper object:
- `request_list_id`: string.
- `test_id`: string. Foreign key into `test-plan.schema.json`.
- `control_id`: string. Foreign key into `control.schema.json`.
- `obligation_id`: string. Foreign key into `obligation.schema.json`.
- `period_start`, `period_end`: string (ISO date).
- `requests`: array of objects, each with:
  - `request_id`: string.
  - `control_objective`: string.
  - `criterion_source`: string (named rule, section, policy reference).
  - `artifact_description`: string.
  - `format_requested`: enum. `pdf` / `csv` / `screenshot` / `system-export` / `signed-memo` / `other`.
  - `system_of_record`: string.
  - `owner_role`: string (role, not person).
  - `due_date`: string (ISO date).
  - `population_reference`: string.
  - `reliance_classification`: enum. `original` / `vendor-supplied` / `management-prepared`.
  - `status`: enum. `open` / `received` / `re-asked` / `closed`.
- `not_applicable_items`: array of objects with `description` and `rationale`.
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `reviewer_questions`: array of strings.
- `human_review_required`: boolean. Always true.

Phase 2 should add `evidence-request.schema.json` and reference it from `test-plan.schema.json` via `evidence_request_list_id`.

## Example scenarios

### Scenario 1: HMDA LAR data-integrity evidence asks for an annual compliance-testing cycle

Input: a mid-size bank's compliance-testing team is preparing the annual HMDA Loan Application Register data-integrity test (Reg C). Sample is 60 LAR records drawn from the bank's 2025 LAR. Source posture is public (Reg C 12 CFR 1003 [verify section] and FFIEC HMDA Filing Instructions Guide [verify edition]) plus the firm's HMDA controls methodology.

Output emphasizes:
- 12 numbered requests covering: LAR record extract per sample ID; underlying loan application file; underwriting decision documentation; rate-lock evidence; AUS findings; loan-officer credentials; ECOA monitoring data form; lien position evidence; preapproval-program disclosures; demographic information firewall evidence; quarterly LAR data-quality review log; the prior-year LAR resubmission log if any.
- Reliance classification flags vendor-supplied AUS reports as such (drives a separate request for the AUS configuration report).
- Format column specifies CSV with named columns for LAR extracts (no screenshots accepted).
- Not-applicable section lists pre-2025 records (out of period) and small-business loans (out of scope; tested separately under Section 1071 [verify 1002.107] testing cycle).
- Confidence label high; reviewer question on whether the demographic firewall evidence ask is sufficient given the Section 1071 implementation overlap.

### Scenario 2: NYDFS Part 500 access-recertification evidence asks for second-line cyber testing

Input: second-line cyber risk is testing the quarterly logical-access recertification control for a critical core-banking application against NYDFS Part 500 §500.7 [verify] and FFIEC IT booklet expectations. Sample is 30 recertification packets from the most recent quarter.

Output emphasizes:
- Eight numbered requests: recertification packet PDF per sample ID; underlying entitlement extract from the IAM system; manager attestation log; revocation tickets where access was removed; segregation-of-duties exception log; privileged-access review evidence (separate quarterly artifact); NYDFS Part 500 annual certification supporting evidence; the IAM-system change log for the period.
- Reliance classification distinguishes IAM-system extracts (original system output) from manager attestations (management-prepared).
- Format specifies system-export CSV for entitlement data; signed-memo for manager attestations; PDF for recertification packets with timestamps visible.
- Not-applicable section: service accounts (excluded by sampling rationale; tested under a separate service-account control); read-only entitlements (lower-risk tier, tested annually).
- Confidence label medium; reviewer question on whether the privileged-access review evidence should be tested concurrently or in a separate workpaper.

## Common pitfalls

1. "Provide all relevant documents" requests. The artifact description must be specific enough that a reasonable owner can fulfill it without a follow-up call. If the request needs a phone call to clarify, the spec is wrong.
2. Asking for the policy as evidence of operating effectiveness. The policy is the criterion (or part of it), not the evidence. Ask for the artifact that shows the policy was followed, not the policy itself.
3. Mixing criteria sources without naming them. A single request line should name one criterion source (rule section, policy section, methodology). If the criterion stack is complex, split the request.
4. Skipping the reliance classification. Vendor-supplied evidence and management-prepared evidence have lower reliability than original system output. The classification is the reviewer's prompt to ask follow-up reliability questions.
5. Using the request list as a workpaper. The request list documents what was asked and the status. Conclusions live in the workpaper.
6. Forgetting the not-applicable section. Without it, the next year's reviewer will re-ask for items that were intentionally out of scope and waste the owner's time.
