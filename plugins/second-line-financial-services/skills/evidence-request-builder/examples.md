# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## hmda-lar-data-integrity

### Example: HMDA LAR data-integrity PBC list for the annual compliance-testing cycle

Public-source-derived. No named institution. The shape mirrors the evidence ask a compliance-testing pod fields ahead of an annual HMDA Loan Application Register data-integrity test.

#### Input

- **Test cycle**: annual HMDA LAR data-integrity test, drafting the PBC list ahead of fieldwork.
- **Test plan reference**: pre-fieldwork test plan (test ID `TP-CMP-HMDA-2026-01`) with operating-effectiveness procedures defined: P1 reperformance of selected LAR data points against source documents per sample, P2 LAR-to-LOS reconciliation at the population level, P3 demographic-firewall reperformance.
- **Sampling memo reference**: `SM-CMP-HMDA-2026-01` from `control-sampling`. 60 LAR records, stratified by action-taken type.
- **Engagement scope supplied**: institution = state member bank; primary regulators = FRB, CFPB, state DFI; persona = compliance-testing manager (reviewer); source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlay = conduct (consumer-facing), privacy not loaded (no GLBA Safeguards touch).
- **Period under test**: calendar year LAR.

#### Output sketch

The skill produces a PBC evidence request list. Headlines:

- **Header** — evidence request list ID `ER-CMP-HMDA-2026-01`, test ID `TP-CMP-HMDA-2026-01`, control ID for the HMDA data-integrity control, obligation IDs for Reg C 12 CFR 1003.4 [verify subsection] data points and 12 CFR 1003.5 [verify subsection] reporting, period covered (calendar year), preparer role (compliance-testing analyst), reviewer role (compliance-testing manager), source posture public-plus-firm-policy-plus-evidence, escalation path (testing manager, then chief compliance officer), confidence label high.
- **Request summary** — 12 requests, due-date span aligned to the four-week fieldwork window, owner roles spread across LAR preparer, loan-operations data-quality lead, demographic-firewall control owner, and AUS configuration owner.
- **Request rows (representative)**:
  - `R001` — control objective: LAR data-point completeness and accuracy per sample. Criterion source: Reg C §1003.4 [verify subsection] data-point definitions. Artifact: LAR record extract for the 60 sampled LEI-loan-IDs with all 110 reportable data points, format CSV with named columns matching the FFIEC HMDA Filing Instructions Guide [verify edition] field labels (no screenshots accepted). System of record: LAR generation system. Owner role: LAR preparer. Due date: fieldwork day 5. Reliance: original-system-output. Sensitivity: confidential (NPI on borrower fields). Status: open.
  - `R002` — control objective: source-document support for sampled LAR records. Criterion source: Reg C §1003.4 [verify subsection]. Artifact: underlying loan-application file per sample ID (URLA, AUS findings, rate-lock confirmation, settlement statement, lien-position evidence). Format PDF (one bundle per sample). System of record: loan origination system, document repository. Owner role: loan operations file-pull lead. Due date: fieldwork day 10. Reliance: original-system-output. Sensitivity: confidential. Status: open.
  - `R003` — control objective: AUS configuration evidence supporting the AUS findings reliance. Criterion source: firm AUS reliance policy section, FFIEC HMDA Filing Instructions Guide [verify edition]. Artifact: AUS configuration export covering the period's underwriting rule set. Format system-export (CSV or PDF as the AUS supports). System of record: AUS (vendor). Owner role: AUS configuration owner. Due date: fieldwork day 7. Reliance: vendor-supplied (drives reliance test note in the workpaper). Sensitivity: internal. Status: open.
  - `R004` — control objective: ECOA monitoring data flow integrity. Criterion source: Reg B §1002.13 [verify subsection]. Artifact: demographic-information form per sample plus the front-end-to-back-end flow log. Format PDF (forms) plus CSV (flow log). System of record: loan origination system, demographic data store. Owner role: demographic-firewall control owner. Due date: fieldwork day 8. Reliance: original-system-output. Sensitivity: confidential. Status: open.
  - `R005` — control objective: demographic firewall structural enforcement. Criterion source: Reg B §1002.5(b) [verify subsection], firm fair-lending policy section. Artifact: production-environment role-based access entitlement extract for any role with read-or-write access to demographic information at underwriting. Format system-export CSV. System of record: IAM (Okta, Azure AD, or named equivalent). Owner role: IAM operations lead. Due date: fieldwork day 5. Reliance: original-system-output. Sensitivity: internal. Status: open.
  - `R006` — control objective: rate-spread calculation queue integrity (repeat-issue area from prior cycle). Criterion source: Reg C §1003.4(a)(12) [verify subsection], FFIEC HMDA Filing Instructions Guide rate-spread methodology [verify edition]. Artifact: rate-spread calculation log for the period with input fields and output spread per sample. Format CSV. System of record: rate-spread calculation engine. Owner role: pricing operations lead. Due date: fieldwork day 7. Reliance: original-system-output. Sensitivity: internal. Status: open.
  - `R007` — control objective: LAR-to-LOS population reconciliation evidence. Criterion source: firm LAR data-quality policy section. Artifact: quarterly LAR data-quality reconciliation log for the period. Format PDF (signed by the data-quality lead). System of record: loan-operations reconciliation log. Owner role: loan-operations data-quality lead. Due date: fieldwork day 3. Reliance: management-prepared (drives completeness-and-accuracy check). Sensitivity: internal. Status: open.
  - `R008` — control objective: prior-cycle LAR resubmission evidence. Criterion source: FFIEC HMDA resubmission threshold guidance [verify FFIEC edition], firm HMDA resubmission policy section. Artifact: prior-year resubmission log including resubmitted records, the resubmission rationale, and the regulator-acknowledgement evidence (where applicable). Format PDF. System of record: regulatory-reporting log. Owner role: regulatory-reporting manager. Due date: fieldwork day 5. Reliance: original-system-output. Sensitivity: confidential. Status: open.
  - Additional rows (R009-R012) cover preapproval-program disclosures, lien-position evidence on selected samples, loan-officer credentials per sample, and the AUS findings export per sample.
- **Not-applicable items**:
  - Pre-period LAR records — out of period; the LAR is calendar-year scoped.
  - Small-business loans — out of scope under HMDA; covered separately under the Section 1071 testing cycle (12 CFR Part 1002 Subpart B; **§1071 revised final rule, May 1, 2026: 1,000 covered transactions; effective June 30, 2026; compliance January 1, 2028** — supersedes the 2023 tiered schedule) under test plan `TP-CMP-1071-2026-01`.
  - SAR content for any sampled customer — restricted access; the LAR data-integrity test does not inspect SAR content. SAR-decision testing is a separate cycle with its own access-control posture.
- **Limitations** — the request list addresses the calendar year only; demographic-firewall evidence is point-in-time at the testing date and does not cover the prior period; reliance on vendor AUS configuration evidence carries a separate completeness check via R003.
- **Reviewer questions** — one reviewer question for pre-fielding sign-off: whether the demographic-firewall entitlement extract (R005) should also pull the test environment for comparison, given that the firm's demographic-firewall control has historically been tested only against production. Routed to the testing manager.
- **Confidence label** — high.

The list is a spreadsheet artifact; render it via the `xlsx` skill in `document-skills`.

#### Why this scenario matters

- **Boundary check on artifact specificity** — every request names the artifact concretely (CSV with named columns, PDF bundle per sample, role-based entitlement extract for a specific role-set), not "all relevant LAR documents".
- **Boundary check on reliance classification** — vendor-supplied (AUS configuration) and management-prepared (data-quality reconciliation log) evidence are flagged so the workpaper applies the right reliance test.
- **Boundary check on the not-applicable section** — small-business loans, pre-period records, and SAR content are explicitly out, with the rationale and the separate cycle named where applicable. Avoids re-ask in next year's cycle.
- **Boundary check on criterion-per-row** — each row names a single criterion source (regulation section, policy section, or methodology). Where the criterion stack is complex, the request was split rather than collapsed.
- **Boundary check on format specificity** — CSV asks name expected columns; "screenshot" is not accepted on data-integrity tests.

#### Anchors

- Reg C — 12 CFR Part 1003 (HMDA), §1003.4 data points and §1003.5 reporting.
- FFIEC HMDA Filing Instructions Guide (current edition) [verify edition].
- Reg B — 12 CFR Part 1002, §1002.5(b) and §1002.13 [verify subsections].
- AICPA AU-C 500, Audit Evidence [verify paragraph].
- IIA Standard on Identifying Information (current Global Internal Audit Standards mapping of prior IPPF 2310) [verify section].

See `references/source-anchors.md` and `references/sector-overlays.md#banking` for full citations.

## nydfs-access-recertification

### Example: NYDFS Part 500 access-recertification PBC list for second-line cyber testing

Public-source-derived. No named institution. The shape mirrors the evidence ask a second-line cyber-risk pod fields ahead of testing the quarterly logical-access recertification control on a critical core-banking application.

#### Input

- **Test cycle**: quarterly access-recertification control test, drafting the PBC list ahead of fieldwork.
- **Test plan reference**: pre-fieldwork test plan (test ID `TP-CYB-AR-2026-Q1`) with operating-effectiveness procedures defined: P1 reperformance of recertification packets against the IAM entitlement extract per sample, P2 reperformance of revocation tickets where access was removed, P3 inspection of the SoD exception log, P4 inspection of the privileged-access review evidence.
- **Sampling memo reference**: `SM-CYB-AR-2026-Q1` from `control-sampling`. 30 recertification packets stratified by privilege tier (standard / privileged), plus 100% on the privileged subset.
- **Engagement scope supplied**: institution = NYDFS-Covered Entity national bank; primary regulators = NYDFS, FRB, OCC; persona = second-line cyber-risk testing manager (reviewer); source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlays = cyber (default-on for IAM and Part 500), privacy (loaded for NPI handling on the sampled user populations).
- **Period under test**: most recent quarter.

#### Output sketch

The skill produces a PBC evidence request list. Headlines:

- **Header** — evidence request list ID `ER-CYB-AR-2026-Q1`, test ID `TP-CYB-AR-2026-Q1`, control ID for the quarterly access-recertification control, obligation IDs for NYDFS 23 NYCRR §500.7 [verify subsection], period covered (quarter), preparer role (cyber-risk-testing analyst), reviewer role (cyber-risk-testing manager), source posture public-plus-firm-policy-plus-evidence, escalation path (cyber-risk-testing manager, then head of second-line cyber risk; IAM operations manager for unresponsive system owners), confidence label medium.
- **Request summary** — 8 requests, due-date span aligned to the three-week fieldwork window, owner roles spread across IAM operations, application owner, recertification-program owner, HR systems lead, and the privileged-access review owner.
- **Request rows (representative)**:
  - `R001` — control objective: recertification packet evidence per sample. Criterion source: NYDFS §500.7(a) [verify subsection] periodic review of access privileges. Artifact: recertification packet PDF per sampled user including the entitlement list reviewed, the recertifier's per-entitlement attestation (or the blanket attestation if that is the form), and the timestamps for review and approval. Format PDF with timestamps visible. System of record: recertification platform (firm-named system). Owner role: recertification-program owner. Due date: fieldwork day 7. Reliance: original-system-output. Sensitivity: confidential (user identity, role data). Status: open.
  - `R002` — control objective: underlying entitlement state at the recertification time. Criterion source: NYDFS §500.7(a) [verify subsection]. Artifact: IAM entitlement extract for the application as of the recertification cutoff date for each sampled user. Format system-export CSV with named columns (user ID, role, entitlement, last-modified date, last-modified-by role, status). System of record: IAM platform. Owner role: IAM operations lead. Due date: fieldwork day 5. Reliance: original-system-output. Sensitivity: confidential. Status: open.
  - `R003` — control objective: revocation evidence where access was removed at recertification. Criterion source: NYDFS §500.7(a) [verify subsection], firm IAM policy section on revocation SLA. Artifact: revocation ticket per removed entitlement (ticket ID, requested date, completed date, requester role, approver role) for the sampled users with revoked entitlements at recertification. Format system-export CSV plus per-ticket PDF. System of record: ticketing system (ServiceNow, Jira, or named equivalent). Owner role: IAM operations lead. Due date: fieldwork day 7. Reliance: original-system-output. Sensitivity: internal. Status: open.
  - `R004` — control objective: HR-IAM termination feed evidence (cross-population check, not in the recertification sample). Criterion source: firm IAM policy section on terminated-employee revocation, NYDFS §500.7(a) [verify subsection]. Artifact: full population of termination events for the quarter with the corresponding IAM revocation timestamp per terminated user. Format system-export CSV. System of record: HR platform plus IAM platform (joined by the firm's standard reconciliation report). Owner role: HR systems lead, joint with IAM operations. Due date: fieldwork day 5. Reliance: original-system-output (joined extract; reliance test note records the join logic). Sensitivity: confidential. Status: open.
  - `R005` — control objective: SoD exception log for the period. Criterion source: firm SoD policy section, NYDFS §500.7 [verify subsection]. Artifact: SoD exception log entries created or open during the period with description, approver role, expected expiry, and current status. Format system-export CSV. System of record: SoD exception register (firm-named system). Owner role: IAM governance lead. Due date: fieldwork day 5. Reliance: original-system-output. Sensitivity: internal. Status: open.
  - `R006` — control objective: privileged-access review evidence for the period (separate quarterly artifact, tested concurrently). Criterion source: NYDFS §500.7 [verify subsection] privileged-access review expectation, firm privileged-access policy section. Artifact: privileged-access review packet for the quarter including the privileged-account inventory at review, the per-account review outcome, and the senior-officer attestation. Format PDF. System of record: privileged-access management (PAM) platform plus the recertification platform. Owner role: privileged-access review owner. Due date: fieldwork day 7. Reliance: original-system-output. Sensitivity: restricted (privileged-account data). Status: open.
  - `R007` — control objective: NYDFS annual certification supporting evidence touching access-management. Criterion source: NYDFS §500.17(b) [verify subsection]. Artifact: the most recent annual certification working-paper section covering §500.7 access management, with the underlying evidence references. Format PDF (signed-memo class). System of record: regulatory-affairs filing repository. Owner role: regulatory-affairs lead. Due date: fieldwork day 3. Reliance: management-prepared (working-paper for certification; drives completeness-and-accuracy check). Sensitivity: confidential. Status: open.
  - `R008` — control objective: IAM-system change log integrity over the period (rules out silent in-period entitlement reshape that would invalidate the recertification baseline). Criterion source: firm change-management policy section, NYDFS §500.7 [verify subsection]. Artifact: IAM-system change log for the period including configuration changes, role-definition changes, and entitlement-set changes with date, requester role, approver role, and change-ticket reference. Format system-export CSV. System of record: IAM platform change log plus change-management ticketing. Owner role: IAM operations lead. Due date: fieldwork day 5. Reliance: original-system-output. Sensitivity: internal. Status: open.
- **Not-applicable items**:
  - Service accounts — excluded by sampling rationale; service-account access governance is tested under a separate control under test plan `TP-CYB-SVC-2026-01` with its own request list.
  - Read-only entitlements on non-sensitive screens — lower-risk tier; tested annually rather than quarterly under test plan `TP-CYB-AR-RO-2026-01`.
  - Break-glass account activations — captured in incident-response testing under test plan `TP-CYB-IR-2026-Q1` rather than the recertification control test.
  - SAR-system access — SAR-system entitlement reviews carry restricted access; tested under a separate cycle by reviewers with the access posture, not under this cycle.
- **Limitations** — the request list addresses the most recent quarter only; the IAM entitlement extract is point-in-time at the recertification cutoff date and does not cover intra-quarter entitlement changes (R008 is the cross-check); reliance on the joined HR-IAM extract for terminations rests on the firm's standard reconciliation logic; the request list does not address the application's data-protection or encryption controls (separate cycles).
- **Reviewer questions** — one reviewer question for pre-fielding sign-off: whether the privileged-access review evidence (R006) should be tested concurrently in this workpaper or routed to a separate workpaper under a paired test plan. Routed to the cyber-risk-testing manager.
- **Confidence label** — medium (the privileged-access review evidence overlap with the recertification control test is a methodology open question; the joined HR-IAM termination extract reliability depends on the firm's reconciliation logic that the workpaper's reliance test note will need to address).

The list is a spreadsheet artifact; render it via the `xlsx` skill in `document-skills`.

#### Why this scenario matters

- **Boundary check on the not-applicable section** — service accounts, read-only entitlements, break-glass activations, and SAR-system access are explicitly out, each with the separate cycle named. Avoids re-ask and avoids drift into adjacent control areas.
- **Boundary check on reliance classification** — the joined HR-IAM extract is original-system-output but the join logic itself is management-prepared methodology; the workpaper's reliance test note will pick that up. The annual-certification working-paper section is management-prepared and flagged accordingly.
- **Boundary check on the IAM change log cross-check (R008)** — without the change log, the recertification baseline could be silently reshaped intra-quarter and the test would miss the change. The change-log request is the cross-check, not a separate procedure.
- **Boundary check on privileged-access review separation** — the reviewer question routes the methodology open question explicitly rather than letting the testing analyst absorb the privileged-access review into the recertification workpaper without sign-off.
- **Boundary check on sensitivity classification** — privileged-account data is restricted, not internal; the sensitivity column drives downstream handling (segregation in shared review folders, distribution-list control).

#### Anchors

- NYDFS 23 NYCRR Part 500 — §500.7 (access privileges and management) [verify subsection], §500.17(b) (annual certification) [verify subsection].
- FFIEC IT Examination Handbook — Information Security booklet [verify edition and section].
- NIST SP 800-53A Rev. 5 — Assessing Security and Privacy Controls (January 2022) [verify section labels].
- AICPA AU-C 500, Audit Evidence [verify paragraph].
- IIA Standard on Identifying Information (current Global Internal Audit Standards mapping of prior IPPF 2310) [verify section].

See `references/source-anchors.md`, `references/cross-cutting.md#cyber`, and `references/cross-cutting.md#privacy` for full citations.

## troubleshooting

### Troubleshooting: evidence-request-builder

Recurring pitfalls. Read before drafting the request list and again before pre-fielding sign-off.

#### Request specificity

##### "Provide all relevant documents"

The artifact description must be specific enough that a reasonable owner can fulfill it without a follow-up call. If the request needs a phone call to clarify, the spec is wrong. CSV asks name expected columns; per-sample asks reference the sample-ID set; per-period asks name the period boundary rule (extracted-as-of date, originated-during period, action-taken-during period). The schema requires `artifact_description`; populate it with the specific artifact, not a category.

##### Asking for the policy as evidence of operating effectiveness

The policy is the criterion (or part of it), not the evidence. Ask for the artifact that shows the policy was followed, not the policy itself. Where the test plan does need the policy as criterion-source evidence, a single criterion-source request is fine; the procedure-evidence requests then ask for the operating evidence (case files, system extracts, attestation packets, reconciliations) that demonstrates the policy in operation.

##### Mixing criteria sources without naming them

A single request row names one criterion source: regulator + section, policy + section, or methodology. If the criterion stack is complex (e.g., a control addresses Reg E §1005.11 plus the firm's expedited-error-resolution policy section plus an external NACHA expectation), split the request into multiple rows. Collapsing multiple criteria into one row makes the workpaper's procedure-to-evidence trace ambiguous.

##### Letting the artifact description carry the criterion

The artifact description names what is requested; the criterion source names why. A row that says "the production disclosure for Reg DD §1030.4 [verify subsection]" is collapsing the two; the disclosure is the artifact (PDF), Reg DD §1030.4 is the criterion source, and the row populates both fields rather than one.

#### Reliance classification

##### Skipping the reliance classification

The reliance classification is the workpaper's prompt to apply the right reliability test. Vendor-supplied evidence (AUS configuration, SOC reports, vendor attestations) and management-prepared evidence (data-quality reconciliation logs, schedules, attestations) carry lower reliability than original system output and require completeness-and-accuracy checks at fieldwork. The schema requires `reliance_classification`; populate it.

##### Defaulting everything to original-system-output

Reliance defaults to original-system-output only when the artifact actually is an original-system extract. A management-prepared schedule reconciling two system extracts is management-prepared, not original. A vendor-produced report on the firm's behalf is vendor-supplied, not original. The reviewer separates the classes structurally; defaulting hides the seams.

##### External-confirmation requests handled as ordinary asks

External-confirmation requests (AU-C 505) carry distinct conventions: the reviewer (not the control owner) controls the request, the response goes to the reviewer (not back through the firm), and the response evidences the recipient's identity. A request flagged `external-confirmation` triggers AU-C 505 conventions in the workpaper; routing the request through the firm's normal PBC process defeats the purpose.

#### Sensitivity classification

##### Defaulting everything to internal

A request list that defaults every row to `internal` cannot support the firm's privacy program or the workpaper's downstream handling discipline. NPI, PHI, PCI, SAR-adjacent content, customer narratives, regulator correspondence carry confidential or restricted, not internal. Classify at request time.

##### Treating SAR content as a normal request

SAR content access is restricted under 31 CFR §1020.320 [verify subsection]. A request for SAR content from a tester without the access posture is a control failure on the request list itself. The standard pattern is to request the case-management file with the BSA officer's sign-off on access posture, or to route SAR-decision testing to a separate cycle with the right access posture; either way, the request list documents the access-control posture rather than restating SAR content.

##### Treating customer prompts in AI testing as internal evidence

Customer prompts to AI systems are NPI by default. The request list classifies sensitivity (typically restricted) and asks for the firm's prompt-and-output logging configuration evidence rather than restating customer content; where customer content is requested for sample-level inspection, the request names the de-identification posture and the access-control routing.

#### Format and source-of-record discipline

##### Accepting screenshots on data-integrity tests

Screenshots are weak evidence on data-integrity tests; they show a screen state at a moment in time without a system-of-record link to replay the data. CSV with named columns from the system of record is the standard for data-integrity testing; specify it in the format and reject screenshots in the format-accepted column. Where a screenshot is the appropriate format (a configuration-screen design-effectiveness procedure), name it explicitly with the timestamp expectation.

##### Naming "internal database" as the system of record

Name the system. LAR generation system, loan origination system, IAM (Okta, Azure AD, named platform), HR platform, ticketing system (ServiceNow, Jira), surveillance archive (Smarsh, Global Relay, Bloomberg Vault), claim-management system, BSA case-management system. Generic labels do not survive the workpaper's reliance test or the closure-binder's provenance check. Where the firm pseudonymises systems in artifacts shared externally, the firm-overlay carries the mapping; the request list names the system.

##### Test-environment evidence offered for production-control reperformance

Reperformance procedures against production controls (demographic firewall, IAM access in production, encryption-at-rest in production) require production-environment evidence. A request that does not specify production scope risks the firm offering test-environment evidence that does not satisfy the procedure. Specify the environment in the artifact description.

#### Population and sample reference

##### Requests without a population reference

A request without a sample-ID set or a full-population pointer is not testable. The workpaper later cannot reconcile what was tested against what was asked. The schema does not require `population_reference` (some requests are population-level by design (the SoD exception log for the period, the IAM-system change log for the period) and reference the period only), but the field is the workpaper's bridge from request to sample-level evidence inspection, so populate it where the request is sample-driven.

##### Asking for the full population when the procedure tests a sample

A request for "the full LAR" when the procedure tests 60 records is over-asking; the firm fields the larger ask, and the workpaper later inspects only the sampled records. Ask for the sampled records (per the sampling memo) plus the population-level reconciliation evidence (which is a separate, smaller request). Over-asking burns the firm's fielding capacity and trains owners to deprioritise testing requests.

##### Asking for the sample when the procedure tests the full population

The inverse: a request for "the 30-record sample" of an exception register when the test is integrity-of-the-register-for-the-period. The full population is the right ask; the procedure inspects the entire register against the firm's exception-log discipline.

#### Boundary discipline

##### Drafting evidence pulls before reviewer sign-off

Pre-fielding sign-off is the discipline equivalent of pre-fieldwork sign-off on the test plan. Fielding requests before the reviewer signs off the request list is a methodology weakness; the firm receives requests that the reviewer has not approved and the testing program loses the audit trail. The reviewer signs the request list before it is fielded; the schema captures both the preparer date and the reviewer date.

##### Treating the request list as a workpaper

The request list documents what was asked and the status. Conclusions on operating effectiveness, design effectiveness, and exceptions live in the workpaper. A request list that carries a "conclusion" column has overstepped; the workpaper consumes the closed request list and writes the conclusion against the inspected evidence.

##### Treating the request list as the closure binder

The request list is the operational ask at fieldwork start. The closure binder (`evidence-binder` in `risk-compliance-core`) is the index of artifacts produced at the end of fieldwork, with provenance and sufficiency calls. The two are different artifacts at different lifecycle points. The closed request list flows into the closure binder; the binder is not the request list with status filled in.

##### Forgetting the not-applicable section

Without the not-applicable section, the next year's reviewer re-asks for items that were intentionally out of scope and wastes the owner's time. Items out of period, items in another cycle's scope, items at a separate population stratum, items at restricted-access posture: name them with the rationale and the covering test ID where applicable. Closing the loop on what was not asked is as load-bearing as closing the loop on what was asked.

##### Inviting the first-line owner to draft the request list

The request list is second-line work product. First-line input is welcome on artifact format and system-of-record naming, but the request list is signed off by the testing reviewer, not the control owner. A request list drafted by the control owner is the methodology equivalent of self-attestation on what evidence the test will see.

#### Engagement-scope and overlay loading

##### Loading the wrong sector overlay

Institution type and the regulator the control was designed for drive the sector overlay. HMDA controls pull banking; an adviser compliance-program control pulls capital-markets; a sponsor-bank end-customer reconciliation control pulls payments-fintech and banking together (dual-overlay loading is normal for sponsor-bank arrangements). Do not collapse to one overlay when the scope says two.

##### Skipping cyber overlay on IAM or Part 500 populations

Cyber overlay is default-on for any control test touching IAM, data-protection, or NYDFS Part 500-mandated areas. Skipping the cyber overlay because the test is "operationally categorised as compliance" misses the §500.7, §500.5, §500.15, and §500.17(b) [verify subsections] frame and the privileged-account sensitivity discipline.

##### Skipping privacy overlay on requests touching NPI/PHI/PCI

Privacy overlay loads whenever the request list will pull artifacts containing NPI, PHI, PCI, or other regulated personal data, regardless of how the scope reads. The overlay drives sensitivity classification, redaction posture, and minimum-necessary discipline at request time.

#### Output discipline

##### Citing without sections

Every regulator citation in the criterion-source field carries a section reference or a `[verify section]` placeholder. URL alone does not pass the source-anchor depth check. Use `references/source-anchors.md` and the loaded overlays for the canonical citation set; do not restate excerpts in the request list body.

##### Marking unsupported claims silently

Use `[evidence needed]` explicitly where a claim (a criterion section, a system-of-record name, a population boundary rule) is not yet evidenced. An inferred claim presented as evidenced is the failure mode that propagates to the workpaper.

##### Closing with too much certainty

The confidence label is `high` only when source posture, criteria maturity, firm-policy maturity for the control area, and prior-cycle history line up. `medium` and `low` are normal where the source posture is below evidence-aware, where the firm policy is the only criterion for a specific value (with no external benchmark), or where the control area is new and prior-cycle history is thin. `unknown` is honest where the firm has not yet resourced the planning input.

##### Filling the reviewer-questions section with questions the preparer answered

A reviewer question is something the preparer cannot resolve and is asking the named reviewer to decide before sign-off. A question the preparer answers in the request list is not a reviewer question; it is a footnote.

##### Rendering the markdown when the deliverable is xlsx

The deliverable is an Excel workbook produced via the `xlsx` skill in `document-skills`. The markdown in `templates/default-output.md` is the content spec, not the artifact. Producing the markdown without rendering the workbook stops short of the deliverable; the xlsx render is the artifact the firm fields.
