# Insurance sector overlay — evidence-request-builder

Loaded when `engagement-scope.sector_overlay_set` includes `insurance` or when the test addresses NAIC, state DOI, or federal insurance rules. Supplements `references/source-anchors.md`.

## Request-list conventions insurance testing programs apply

Insurance testing PBC lists carry conventions distinct from bank consumer-compliance:

- **Claim-file and policy-file evidence is per-file PDF.** A claim-file ask is the full file (FNOL, adjuster notes, coverage analysis, payment record, denial letter where applicable, complaint correspondence where applicable) per claim ID. A policy-file ask is the underwriting file per policy ID (application, underwriter notes, rate calculation, supporting documentation, declaration page). System-of-record naming matters: claim-management system, policy-administration system, agency-management system.
- **Rate-filing testing requests the SERFF filing.** Rate-and-form-filing testing draws the actual SERFF (System for Electronic Rate and Form Filing) filing record per state-product, the supporting actuarial memorandum, and the state DOI approval order or disposition. SERFF tracking number is the natural request key.
- **Market-conduct evidence follows the NAIC Market Conduct Examiners Handbook conventions.** State DOI market-conduct examinations use standardised request-list shapes the NAIC handbook codifies; second-line testing programs in scope of upcoming market-conduct exams should align the request-list shape so the workpaper file reads against the examiner's expectation.
- **Complaint-handling evidence draws the consumer-complaint log plus per-complaint files.** Complaint logs are CSV exports from the complaint-management system with named columns (complaint ID, intake date, source, line of business, complaint type, resolution date, resolution outcome). Per-sample complaint files are PDF bundles.
- **Producer-licensing evidence draws state-licensing and appointment evidence.** Producer-licensing testing requests the licensing register (state, license type, effective date, appointment status) plus per-sample state license verification (NIPR or state DOI lookup).

## Insurance-supervisory anchors (load by reference; do not restate)

- **NAIC Annual Financial Reporting Model Regulation (Model Audit Rule, Model #205)** [verify section references for the ICFR-relevant evidence-request conventions]. https://content.naic.org/cipr-topics/topic-naic-model-laws-and-regulations [verify URL].
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number and section labels]. https://content.naic.org/cipr-topics/own-risk-and-solvency-assessment-orsa .
- **NAIC Market Conduct Examiners Handbook** (current edition) [verify section labels for state DOI market-conduct request conventions]. https://content.naic.org/cmte_d_mceh.htm [verify URL].
- **NAIC Insurance Data Security Model Law (Model #668)** [verify section labels for cybersecurity event-reporting and program-evidence requests]. https://content.naic.org/cipr-topics/insurance-data-security-model-law .
- **State unfair claims settlement practices statutes** (state by state) — testing requests carry the state-adopted statute citation; the NAIC Unfair Claims Settlement Practices Model Act (Model #900) [verify model number] is the methodology anchor where the state adopted the model.

## Insurance-control-area request notes

### Claims-handling testing (state UCSPA, NAIC Market Conduct Examiners Handbook)

- Request conventions: per-sample claim file PDF bundle (FNOL, adjuster notes, coverage analysis, payment record, denial letter where applicable, customer correspondence). Claim-handling timing requests the claim-system event log (intake date, acknowledgement date, decision date, payment date) per sample. Complaint-correspondence routing testing requests the complaint-management-system extract joined to the claim file by claim ID. Reliance test notes apply where the claim file is management-prepared at the adjuster level (subject to supervisor review trace).

### Underwriting-file testing (NAIC Market Conduct Examiners Handbook)

- Request conventions: per-sample policy file PDF bundle (application, underwriter notes, rate calculation, supporting documentation, declaration page, any subsequent endorsements). Underwriting-decision testing also requests the underwriter-decision audit trail from the policy-administration system. Rating-tier-assignment testing requests the rating-engine input/output log per sample.

### Rate-and-form-filing testing

- Request conventions: SERFF filing record per state-product (filing PDF, supporting documentation, actuarial memorandum, state DOI disposition or approval letter). State-by-state filing register is a CSV export from the firm's filing-tracking system (or from SERFF directly). Use-and-file states versus prior-approval states have different evidence shapes; the request list distinguishes by state.

### Producer-licensing and appointment testing

- Request conventions: producer-licensing register CSV (NPN, name-as-licensed, state, license type, license effective and expiration dates, appointment status, line-of-authority) from the agency-management system; per-sample state license verification (NIPR or state DOI). Continuing-education compliance testing requests the producer's CE-credit register from the firm's CE-tracking system or from NAIC ProducerCheck.

### Privacy and data-security testing under Model #668

- Request conventions: information-security program evidence (program documents, risk-assessment evidence, incident-response evidence, third-party assurance for vendors handling NPI). Cybersecurity event reporting requests the firm's event log for the period with the §4(B) [verify subsection] notification timing per event.

### ORSA testing

- Request conventions: ORSA Summary Report draft for the period, ORSA risk-assessment supporting evidence, and the board-or-board-committee approval of the ORSA Summary Report. ORSA evidence is typically connector-aware reliance because the ORSA Summary Report itself is a privileged regulator-only filing and evidence access posture matters.

## Audience and tone

A request list drafted ahead of an upcoming state DOI market-conduct exam reads aligned to the NAIC Market Conduct Examiners Handbook standardised data calls. A request list drafted for the firm's internal periodic testing of claim-handling reads operationally with the same evidence shape. Where the firm is multi-state, the request list distinguishes state-specific evidence (state-adopted statute citation) from federal-or-NAIC-model evidence.
