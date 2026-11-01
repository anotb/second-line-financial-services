# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## control-test-binder

### Example: control-test evidence binder for an SR 11-7 model validation

Public-source-derived. No named institution. The shape mirrors a common pattern: an in-house model risk team assembles the evidence binder for the annual revalidation of an internal credit-decisioning model, working from SR 11-7, OCC Bulletin 2026-13, and the firm's MRM policy.

#### Input

- **Binder purpose**: model-validation.
- **Scope**: revalidation of an internal credit-decisioning model used in second-look review of declined small-business-loan applications. Period covered: 2025-04-01 to 2026-03-31.
- **Reviewer**: head of model validation (2-line); the binder is being assembled by a 1.5-line model risk reporting analyst on the model owner's team.
- **Engagement scope supplied**: institution = state member bank; primary regulators = FRB, state DFI; persona = head of MRM; source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlays = none for this binder (cyber, privacy, conduct not in scope of the validation cycle).
- **Inputs already on file**: prior validation report (2025); ongoing-monitoring dashboard extracts; the firm's MRM retention schedule; the firm's model inventory record for the model.

#### Output sketch

The skill produces an evidence binder. Headlines:

- **Scope and binder purpose** — model-validation, 12-month period, head-of-MRV reviewer; source posture allows direct extracts from the model risk system of record (MRMS) and the credit-decisioning platform.
- **Request list** — populated from the head-of-MRV's evidence ask for the revalidation cycle: model documentation set, development-data extract, validation re-runs, ongoing-monitoring outputs, outcomes analysis, benchmarking against an external dataset, exception register, change log. Each item carries a status (`met`, `partial`, `gap`, `not-applicable`, `deferred`).
- **Evidence index, grouped by SR 11-7 §V validation activity**:
  - *Conceptual soundness*: model documentation v3.2 (`policy-version`, system of record = MRMS); design memo v2.0 (`management-memo` paired with the design-decision sign-off log from MRMS).
  - *Process verification*: code repository snapshot (`system-extract`, system of record = internal Git enterprise); training script run log (`system-extract`).
  - *Outcomes analysis*: development-data extract (`system-extract`, system of record = data warehouse Snowflake); validation re-run output (`system-extract`); back-test comparison (`test-workpaper`).
  - *Ongoing monitoring*: monthly monitoring dashboard exports for the period (`system-extract`, system of record = MRMS monitoring module); breach alerts (`incident-record`); response actions (`sign-off-log`).
  - *Benchmarking*: external dataset benchmark for the most recent vintage — **gap**.
- **Provenance concerns** — one row flagged: the development-data extract for the 2024 vintage was manually copied from a deprecated reporting tool to a spreadsheet during a system migration; reproducibility is `false` and the row's `completeness_flag` is `partial`. Reviewer questions surface the issue.
- **Evidence gaps** — benchmarking against the external dataset is missing for the most recent vintage; prior-cycle monitoring records are present but the firm's MRM retention schedule calls for seven years and current evidence runs back five.
- **Evidence by control** — the firm's three model-risk controls (independent validation, ongoing monitoring, change management) each carry the supporting evidence rows and a sufficiency call. Independent validation is `complete`; ongoing monitoring is `partial` (benchmarking gap); change management is `complete`.
- **Reviewer questions** — does the spreadsheet-extract row meet MRM's reproducibility expectation, or should the row be reclassified as `management-assertion` until the data warehouse re-pull is run? Should the binder hold open until the external benchmarking gap closes, or proceed with the gap explicitly noted?
- **Confidence label**: `medium`. Posture is high but the benchmarking gap and the provenance issue on the 2024 vintage extract pull confidence down.
- **Sign-off**: blank. The binder is a draft until the head of MRV signs.

The binder is the evidence index, not the validation conclusion. The validation report consumes the binder; the validator decides.

#### Why this scenario matters

- **Practitioner trick line**: "screenshot is not evidence; the system-of-record link is." The benchmarking row could have been a screenshot of an external-dataset query result; the binder requires a paired `system_of_record_link` (the dataset query plus the run log) before the row counts as `complete`. The binder downgrades a confident-looking screenshot to `partial` if the link is missing.
- **Boundary check on evidence-class**: the design memo is a `management-memo` (an assertion), not source evidence. Pairing it with the sign-off log from MRMS makes the design-decision auditable; without the pairing, the memo is one person's claim.
- **Boundary check on retention**: the firm's MRM retention schedule (seven years) is the binding internal expectation; the binder surfaces the two-year shortfall as a gap even though SR 11-7 itself does not specify a duration.
- **Boundary check on provenance**: the spreadsheet extract is a real-world failure mode. The binder does not silently treat it as evidence; it carries the provenance concern and lets the reviewer call it.
- **Boundary check on the request list**: every request-list item maps to evidence rows or appears in the gaps section. A request list with silent omissions is unauditable.

#### Anchors

- SR 11-7 / OCC Bulletin 2011-12 (April 4, 2011), §V Model Documentation.
- OCC Bulletin 2026-13, Revised Interagency Guidance on Model Risk Management, model-documentation refresh [verify section].
- AICPA AU-C 500, audit evidence — sufficiency and appropriateness framing carried by internal audit functions [verify section].
- IIA International Standards 2310 (Identifying Information) and 2410 (Communicating Results) [verify section labels].

See `references/source-anchors.md` for full citations.

## exam-response-binder

### Example: exam-response evidence binder for a state-DOI market-conduct exam

Public-source-derived. No named institution. The shape mirrors a common pattern: a P&C insurer's compliance team assembles the evidence binder for a state Department of Insurance market-conduct examination focused on claims-handling timeliness and unfair claims-settlement practices.

#### Input

- **Binder purpose**: regulator-exam.
- **Scope**: state-DOI market-conduct exam, claims-handling segment. Period covered: 2024-01-01 to 2025-12-31.
- **Reviewer**: examiner-in-charge (external); internal sponsor is the chief compliance officer; the binder is being assembled by a market-conduct compliance manager.
- **Engagement scope supplied**: institution = P&C insurer, state-licensed; primary regulators = state DOI (lead), NAIC accreditation framework background; persona = chief compliance officer; source posture = public-plus-firm-policy-plus-evidence; sector overlay = insurance; cross-cutting overlays = privacy (claims data carries NPI and PHI on first-party medical-payments coverage), conduct (unfair-claims-practices and bad-faith exposure).
- **Inputs already on file**: examiner request list issued at exam open (47 items); claims-platform extracts; complaint log; state DOI complaint correspondence; the firm's claims handbook and procedure versions in force during the period; sample workpapers from the firm's prior internal market-conduct review.

#### Output sketch

The skill produces an evidence binder. Headlines:

- **Scope and binder purpose** — regulator-exam, 24-month period, examiner-in-charge reviewer; source posture supports direct extracts from the claims platform (Guidewire ClaimCenter is the named system of record) and the complaint-management system.
- **Request list** — all 47 examiner items captured verbatim. Status reconciled: 38 `met`, 5 `partial`, 3 `gap`, 1 `not-applicable` (a request for a product line the firm does not write in the state).
- **Evidence index, sample rows**:
  - Claims-handling timeliness extract for the period (`system-extract`, system of record = Guidewire ClaimCenter, period = 2024-01-01 to 2025-12-31, `provenance.reproducible = true`).
  - Sample of 60 claim files selected by the firm's internal sampling protocol (`sample-workpaper`, system of record = the same, paired with the sampling-method memo as a `management-memo`).
  - Complaint log for the period (`system-extract`, system of record = complaint-management system).
  - State DOI complaint correspondence (`regulatory-correspondence`, sensitivity = `restricted`).
  - Claims handbook v6.1 and v6.2 in force during the period (`policy-version`, system of record = policy-management system).
  - Adjuster training records (`training-record`, system of record = LMS).
  - Three signed-attestation rows from claims operations leadership, paired with the underlying staffing reports (`signed-attestation` plus `system-extract`).
- **Evidence by finding** — populated for two open issues from the firm's prior internal review: an issue on first-contact letter timeliness (remediation evidence shows the letter-template change and the post-change timeliness metrics) and an issue on adjuster-training completion (remediation evidence shows the catch-up training records and revised quarterly attestation).
- **Provenance concerns** — one row flagged: a screenshot of the examiner's prior on-site question log, taken from the examiner portal during a working session, is in the binder for context. The `system_of_record_link` is the examiner portal record ID; the provenance concern notes that the firm cannot reproduce a portal screenshot if access changes.
- **Evidence gaps** — three items: an aged inventory of claims open more than 90 days at year-end 2024 (firm's reporting was rebuilt mid-period and the prior view is not reproducible), the staffing-ratio analysis the examiner asked for at the segment-by-line level (firm has the totals but not the segmentation), and the evidence of a bad-faith-handling training module the examiner expected (firm covers the topic in the broader claims-ethics module but not as a discrete module).
- **Evidence by control** — the firm's claims-timeliness control, complaint-handling control, and adjuster-training control each carry the supporting rows and a sufficiency call.
- **Custodian register** — claims operations director (claims-handling rows), complaint manager (complaint rows), HR L&D manager (training rows), compliance manager (policy and procedure rows). Compliance director signs the binder.
- **Reviewer questions** — should the screenshot row be removed before the binder is filed (provenance concern), or kept with the explicit caveat? Does the bad-faith-training gap warrant supplementary evidence (sample handling files showing the practice) or a remediation commitment with a deadline?
- **Confidence label**: `medium`. Posture is high and most rows are reproducible; the gaps and the screenshot pull confidence down.
- **Sign-off**: blank. The binder is a draft until the chief compliance officer signs and the examiner-in-charge accepts.

The binder is the index that the examiner works against; the firm does not take a litigation or settlement position from this artifact.

#### Why this scenario matters

- **Practitioner trick line**: "a management memo is not a substitute for a system extract." The signed-attestation rows from claims-operations leadership pair with the underlying staffing reports; without the pairing, the binder would be carrying assertions as evidence.
- **Practitioner trick line**: "the examiner's request list is the binder's spine." Every request maps to evidence rows or to the gaps section; silent omissions are what trigger the supplementary-request loop the firm is trying to avoid.
- **Boundary check on sensitivity**: state DOI correspondence is `restricted` (regulator-confidential); the binder must not co-mingle restricted and lower-classification rows in shared review folders.
- **Boundary check on the screenshot rule**: the portal screenshot is in the binder because the examiner's question log lives in the examiner-controlled system, not in a firm-controlled system of record. The binder is honest about the provenance limit; it does not pretend the screenshot is reproducible firm-side evidence.
- **Boundary check on cross-overlays**: privacy applies (claims data, NPI and PHI in medical-pay segments), conduct applies (unfair-claims-practices statute). Both overlays load; the binder cites the relevant state UDAP and the NAIC Model Unfair Claims Settlement Practices Act anchors in the source trace.
- **Boundary check on the gap-versus-finding distinction**: a gap in the binder is not yet a finding. The examiner may treat it as one; the binder's job is to surface it honestly with an owner and a target close. The skill stops at the draft binder; the response posture is decided by counsel and the CCO.

#### Anchors

- NAIC Model Audit Rule (Model #205), §16 internal control over financial reporting [verify section].
- NAIC Market Conduct Examiners Handbook, claims-handling examination standards [verify section].
- State Unfair Claims Settlement Practices Act (NAIC Model #900) [verify state-specific adoption].
- AICPA AU-C 500, audit evidence — sufficiency and appropriateness framing.
- IIA International Standards 2310 and 2410 [verify section labels].

See `references/source-anchors.md` for full citations.

## troubleshooting

### Troubleshooting: evidence-binder

The binder is a reconciliation surface, not a folder. When it fails (the regulator's request list does not square with what the binder shows, the reviewer cannot tell what supports what, the audit working paper review bounces it back), the cause is almost always one of the recurring defects below. Practitioner trick line that captures the discipline: a screenshot is not evidence; the system-of-record link is.

#### 1. The binder is a folder of unlabeled screenshots

**Symptom**: Reviewer or examiner asks "where did this come from", and the answer is "from the system" without a system-of-record name, an extract method, or a date the extract was taken. The binder reads as a screenshot dump rather than an indexed evidence pack.

**Why it happens**: The team treated the binder as storage rather than as an index. Screenshots were captured in the moment without recording provenance, then dropped into a SharePoint folder named after the exam.

**Resolution**:
- Every row carries `system_of_record` (a named system, not "internal database"), `provenance.extract_method`, `provenance.extracted_by` (a named role), and `provenance.extracted_at` (an ISO datetime).
- A screenshot is a row attribute, not a row in itself. The row records what the screenshot shows; the screenshot is an attachment that proves the screen state. The system-of-record reference is the actual evidence.
- If the system of record cannot be named, the row is not evidence yet. It belongs in `evidence_gaps` until the source is identified.

#### 2. The request list and the evidence index do not reconcile

**Symptom**: Examiner or audit lead reviews the binder and finds RFI items that have no corresponding evidence row, or evidence rows that do not map to any RFI item. Both directions of the gap are common.

**Why it happens**: The binder was assembled by walking the evidence the team already had rather than by walking the request list. The mapping was never built explicitly.

**Resolution**:
- Build the binder from the request list outward. Each `request_list` item gets either a populated `evidence_items` row (or rows) or a populated `evidence_gaps` row. No request item ends in limbo.
- Evidence rows that do not map to a request item belong in their own section (often a "supplementary evidence" group) with an explanation of why they are in the binder. Otherwise they are noise to the reviewer.
- The reconciliation is itself a deliverable. A clean binder with `request_list` populated, every item resolved, and gaps named is more credible than a fat binder with no reconciliation.

#### 3. The custodian field is set to a team

**Symptom**: Custodian column reads "Compliance" or "Risk" or "Operations" across many rows. When the binder is challenged on a specific row, no individual is accountable for the integrity of that piece of evidence.

**Why it happens**: The team set the field to a team name as a default. The role-level discipline was not enforced.

**Resolution**:
- Custodian is a named role accountable for the integrity of that evidence (Head of Model Risk Reporting, BSA Officer, Director of Vendor Management, Lead Underwriting Auditor). Not a team name. Not a person name (the role outlasts the person).
- The custodian is the role the reviewer goes back to with questions. If the role does not exist or does not have the standing to answer, the row's provenance is weaker than it appears.
- For multi-source evidence (e.g., a reconciliation that pulls from two systems), name a primary custodian and reference the contributing roles in the description.

#### 4. Period coverage is stale

**Symptom**: Evidence rows have `date_generated` six months before the period under review, or `period_start` / `period_end` that do not align to the supervisory or audit window. The reviewer rejects the row on timeliness grounds.

**Why it happens**: Stock evidence (last quarter's BCBS 239 lineage report, last year's vendor-tier list) was carried into the binder without checking that the dates fit the current scope.

**Resolution**:
- Set `period_start` and `period_end` against the engagement's actual window, not against the date the evidence was first generated. Re-pull stock evidence when the period has moved.
- For evidence that does not have a period (a policy version, a contract, a charter), `date_generated` and `period_covered` collapse into the effective-date and effective-period of the document. Capture the document version explicitly.
- Where the supervisory window is short but the underlying recordkeeping floor is longer (BSA: five years; broker-dealer books and records: three to six years depending on rule), the binder's row-level metadata respects the floor even if the engagement window is shorter.

#### 5. Assertions are mixed with evidence

**Symptom**: A management memo asserting "controls are operating effectively as of period end" appears in the evidence index alongside system extracts and test results, with no flag distinguishing the two.

**Why it happens**: The team did not draw the line between evidence (something that exists in the world and can be inspected) and assertion (something a person or function says). Both are useful; they are not the same.

**Resolution**:
- Use `evidence_type` honestly. A management memo is `attestation` or `other`, not `system report` or `sample workpaper`.
- For attestation rows, the description names who attested, on what basis, and against what underlying evidence (which other binder rows). An attestation that does not point at underlying evidence is an opinion, not testimony.
- The reviewer can choose to credit an attestation; they cannot credit an attestation dressed up as a system extract.

#### 6. The binder cannot be re-pulled

**Symptom**: A year later, the binder is referenced in a regulator follow-up or an internal-audit replay. The team cannot reproduce the evidence because the source systems have changed, the queries were not preserved, or the extract method was undocumented.

**Why it happens**: Provenance was captured as a snapshot, not as a method. The binder records what was extracted but not how to extract the same thing again.

**Resolution**:
- For system-extract rows, `provenance.extract_method` names the query, the report ID, the dashboard ID, or the file path that produces the extract. Where a SQL query was hand-written, the query text is attached. Where a vendor system produced the report, the report name and report parameters are recorded.
- For ad-hoc extracts (a one-off pull from a system that does not have a standing report), the binder flags this in the provenance description and the gap section notes the operational risk of non-reproducibility.
- The replay test is the discipline: another team member, six months later, with the binder in hand, should be able to re-pull every system-extract row.

#### 7. Privacy posture is set to "internal" by default

**Symptom**: Every row carries `sensitivity: internal` regardless of content. The binder includes NPI samples, PHI narratives, or restricted-classification material at the same posture as a published policy. When the binder is shared with external counsel or a regulator, the firm has no row-level control.

**Why it happens**: The team did not load the privacy overlay when the binder warranted it, or loaded it but did not apply row-level classification.

**Resolution**:
- Load `references/cross-cutting.md#privacy` whenever the binder may carry NPI, PHI, PCI, or other regulated personal data. The overlay is mandatory by content, not optional by preference.
- Classify rows honestly. Sample claim files with NPI are `confidential` or `restricted`, not `internal`. Materiality memos under legal privilege are `restricted`. Public policies are `public`.
- Sensitivity drives downstream handling: redaction, segregation, distribution-list control. A binder that defaults every row to `internal` cannot support any of that.

#### 8. Gaps are hidden

**Symptom**: The binder reads clean (no rows in `evidence_gaps`) but the reviewer or examiner finds gaps anyway. The team's claim that the binder is complete collapses on inspection.

**Why it happens**: Gaps were filled with weak evidence to avoid an empty `evidence_gaps` section, or the gap analysis was never run because a clean binder felt better.

**Resolution**:
- Every `request_list` item that is not unambiguously met by an `evidence_items` row generates an `evidence_gaps` row. Partial coverage is partial; mark it.
- A binder with named gaps and a remediation plan is stronger than a binder with hidden gaps. Reviewers credit honesty about gaps; they discount binders that claim completeness and do not survive scrutiny.
- The completeness flag on a row (`complete`, `partial`, `gap`) is the row-level analogue. Rows flagged `partial` accumulate; if too many rows are partial, the binder summary acknowledges the cumulative weakness.

#### 9. The binder is signed by a function rather than a role

**Symptom**: The sign-off block reads "Reviewed by Compliance" with no named role. When the binder is later challenged, no individual function head is on record as accountable for the binder's integrity.

**Why it happens**: The sign-off was treated as a courtesy line rather than as the accountability act it is.

**Resolution**:
- The reviewer is a named role (Chief Compliance Officer, Chief Risk Officer, Audit Director, Head of Model Risk, Head of TPRM). The sign-off captures the role, the date, and any caveats the reviewer wants on record.
- Multiple roles may sign for different sections. A model-validation binder may carry the head of model risk for §V evidence and the model owner for the development-data extract section.
- The sign-off block is the contract between the binder and the audience. Without it, the binder is a draft.

#### 10. The skill is invoked when the work is upstream

**Symptom**: The team called evidence-binder when the actual work was generating the evidence (running the source-system report, executing the test, drafting the memo). The binder produced is empty or tautological because there is no evidence to index yet.

**Why it happens**: The team conflated "we need an evidence pack" with "we need to build the evidence." Different work, different skills.

**Resolution**:
- The "Not the right tool when" section of the SKILL.md is the contract. Producing the underlying evidence is upstream of this skill; this skill indexes existing evidence.
- If the team needs the evidence built, the upstream work belongs in the source-system team, the testing function, or the relevant control-owner team. Evidence-binder catches the artifacts those teams produce.
- For drafting findings from missing evidence, hand off to `issue-writeup`. For committee narratives, hand off to `risk-committee-pack`. The binder is the source of truth those skills consume; it is not the narrative they produce.
