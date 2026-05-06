# attestation-pack — spec sheet

Plugin: `risk-reporting`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Assembles a management attestation pack: scope statement, control inventory, evidence index, owner certifications, exceptions and remediation, reviewer questions, and the signature block. Output is the named-section pack a control owner, head of compliance, internal audit lead, or external assessor can take into the certification meeting after qualified review.

Best for:
- Producing the periodic management attestation pack underpinning a formal certification (SOX 404 sub-certification at process-owner level, FFIEC self-assessment, vendor-management attestation, BCBS 239 self-assessment attestation, SOC 1 / SOC 2 management assertion package).
- Refreshing the attestation pack ahead of an external assessor field visit (SOC auditor, internal audit, regulator-engaged third-party).
- Producing the attestation evidence binder for a regulator response that requires named-control-by-named-control evidence.
- Standing up the first attestation pack for a new process or product (where no prior pack exists).

Not the right tool when:
- The artifact is the underlying risk-control matrix (use `risk-compliance-core/skills/control-matrix`; the attestation pack consumes it).
- The artifact is an issue write-up for an exception identified during attestation (use `risk-compliance-core/skills/issue-writeup`).
- The artifact is a single control test workpaper (use `compliance-testing/skills/control-test-workpaper`).
- The artifact is a management response to a regulator finding (use `management-response`).
- The work is the SEC executive certification (CEO / CFO certifications under Section 302 / 906) — that is a securities-counsel-led artifact, not a second-line attestation pack. This skill produces the process-owner sub-certifications that ladder up to the executive certification.

Anchored to: COSO Internal Control – Integrated Framework (2013) for the control-attestation framing; SOX Sections 302 and 404 sub-certification structures (process-owner level); PCAOB AS 2201 (Audit of Internal Control over Financial Reporting Integrated with an Audit of Financial Statements) [verify pin cite]; AICPA SSAE 18 / SOC 1 and SOC 2 (management assertion expectations); BCBS 239 (January 2013) Principle 1 (governance) for risk-data attestation; U.S. interagency third-party risk management guidance (June 2023) §III.D for vendor-attestation expectations; OCC Heightened Standards 12 CFR Part 30 Appendix D §IV [verify section] for board-level attestation linkage.

## Source anchors

Primary:
- COSO Internal Control – Integrated Framework, 2013. Components to cite: Control Environment, Risk Assessment, Control Activities, Information and Communication, Monitoring Activities. Use for: framing control-by-control attestation against the COSO components the firm has adopted.
- SOX Section 302 (corporate responsibility for financial reports) and Section 404 (management assessment of internal controls). Use for: the structural backbone of process-owner sub-certifications that ladder to CEO/CFO certifications.
- PCAOB AS 2201 — Audit of Internal Control Over Financial Reporting Integrated with an Audit of Financial Statements (formerly AS 5). Sections to cite: paragraphs on management's responsibility, control identification, and evidence. [verify pin cites.] Use for: framing what attestation evidence the external auditor will expect.
- AICPA SSAE 18 / AT-C 320 (SOC 1) and AT-C 105 / 205 (SOC 2). Use for: management assertion structure when the attestation pack supports a SOC report.
- BCBS 239, Principle 1 (governance). Use for: the risk-data attestation use case (Head of Risk Reporting attesting to data quality and report integrity).
- U.S. interagency third-party risk management guidance, final June 2023. Section III.D (ongoing monitoring). Use for: vendor-management attestation use case (vendor manager attesting to ongoing-monitoring evidence).
- OCC Heightened Standards 12 CFR Part 30 Appendix D §IV [verify section labels]. Use for: large-bank attestation linkage from process-owner up to the board's risk governance framework.

Secondary (overlay only):
- COBIT 2019 — for IT-control attestation framing where the firm uses COBIT as its IT governance framework.
- NIST Cybersecurity Framework 2.0 (February 2024) [verify version] — for cyber-control attestation against the framework's functions and categories.

## Sector overlays needed

- `banking.md` — Covers FFIEC IT booklet attestation expectations (information security program attestation), OCC Heightened Standards attestation linkage, and the Federal Reserve's Y-14 / FR Y-9 reporting attestation expectations [verify].
- `insurance.md` — Covers NAIC Model Audit Rule (Model #205) [verify section] internal-control-over-financial-reporting attestation expectations for insurers, ORSA management assertion expectations.
- `capital-markets.md` — Covers SEC Rule 17a-5 financial responsibility attestation [verify section], FINRA 3120/3130 supervisory and CEO certifications.
- `payments-fintech.md` — Covers PCI DSS attestation of compliance (AOC) expectations, OCC bank-partnership attestation linkage where the fintech is a sponsor-bank partner.

## Cross-cutting overlays needed

- `cyber.md` — Optional, frequently invoked. Cyber-control attestations are a major use case; the overlay covers NIST CSF 2.0 attestation framing, NYDFS Part 500 §500.17(b) annual CISO certification (Form B) [verify after Part 500 amendments], and PCI DSS AOC structure.
- `climate.md` — Not required at v1. Climate attestations are emerging (e.g., financed-emissions data attestation) but are not yet a stable artifact.
- `privacy.md` — Optional. Privacy-control attestations (GLBA Safeguards Rule 16 CFR 314.4(g) annual report) [verify section] appear where the scoped process touches consumer financial information.
- `conduct.md` — Optional. Conduct attestations (sales-practices attestations under FINRA, fair-lending self-attestations) appear at firms with consumer-facing businesses.

## Output template named sections

Top of artifact:
- Cover: attestation period, scope (process / product / function / legal entity), attesting role, attestation type (sub-certification under SOX 302/404 / SOC 1 management assertion / SOC 2 management assertion / FFIEC self-assessment / vendor-management / BCBS 239 risk-data / cyber annual / privacy annual / other), assertion language version, source posture
- Executive summary (5 bullets, attesting role's voice)

Body:
- Scope statement (the precise boundary being attested: which processes, which systems, which legal entities, which time period)
- Source criteria (the framework or rule against which the attestation is made)
- Control inventory (the named controls in scope, sourced from the upstream control matrix; one row per control)
- Evidence index (one row per piece of evidence supporting the attestation: what it is, where it sits, who produced it, period covered)
- Exceptions identified (controls that did not operate as designed in the period, or where evidence is insufficient; severity and remediation)
- Compensating controls (where exceptions exist, the compensating control narrative)
- Remediation status (open issues from prior period, current-period status, owner, target date)
- Reviewer questions (questions the attesting role expects from internal audit, external assessor, or regulator)

Tail:
- Assertion language (the actual attestation text the attesting role signs)
- Sign-off block (attesting role, name field for human signature, date, witness if required)
- Source trace per material claim
- Confidence label (high / medium / low / unknown)
- Human-review gates and recommended owner actions

## Structured output fields

Schema to add in phase 2: `attestation-pack.schema.json`. Reuses `control.schema.json` (existing) for control-inventory rows and `issue.schema.json` (existing) for exception linkage.

Wrapper object:
- `attestation_id`: string. Stable ID.
- `attestation_period`: object. `start` (ISO date), `end` (ISO date).
- `scope`: object. `processes` (array of strings), `systems` (array of strings), `legal_entities` (array of strings).
- `attesting_role`: string. Role title (e.g., "Head of Vendor Management"; "Head of Risk Reporting"; "CISO"; "Process Owner — Wholesale Credit Risk").
- `attestation_type`: enum. `sox-sub-certification` / `soc1-management-assertion` / `soc2-management-assertion` / `ffiec-self-assessment` / `vendor-management` / `bcbs239-risk-data` / `cyber-annual` / `privacy-annual` / `other`.
- `assertion_language_version`: string.
- `source_posture`: enum. `public-only` / `firm-policy-overlay` / `mixed`.
- `source_criteria`: array of strings (e.g., `COSO 2013`, `PCAOB AS 2201`, `AICPA SSAE 18 AT-C 320`, `BCBS 239 Principle 1`).
- `control_inventory`: array of objects, each conforming to `control.schema.json` extended with `attestation_period_design_effectiveness` (enum: effective / partially-effective / not-effective / not-tested) and `attestation_period_operating_effectiveness` (same enum).
- `evidence_index`: array of objects with `evidence_id`, `description`, `evidence_type` (enum: system-output / report / sign-off-log / minutes / policy / external-assessor-output / sample-test-result / reconciliation), `system_of_record` (string), `period_covered` (object with start and end ISO dates), `produced_by` (role), `linked_control_ids` (array of strings).
- `exceptions`: array of objects with `exception_id`, `linked_control_id`, `description`, `severity` (enum: low / medium / high / critical), `compensating_control_description` (string or null), `linked_issue_id` (foreign key to `issue.schema.json`), `status` (enum: open / remediated / accepted-risk / pending-review).
- `prior_period_remediation_status`: array of objects with `prior_issue_id`, `current_status`, `evidence_pointer`.
- `reviewer_questions`: array of strings.
- `assertion_text`: string. The actual attestation language signed.
- `signed_by_role`: string. (The signature itself is out of scope for the structured output; the role and date are captured.)
- `signed_date`: string or null. ISO date.
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `human_review_required`: boolean. Always true for v1.

## Example scenarios

### Scenario 1: Vendor-management attestation pack for a critical third-party fraud-screening service

Input: the second-line vendor-management function is producing the annual attestation pack for a critical third-party fraud-screening service used in card transactions. The attesting role is the Head of Vendor Management; the attestation supports the firm's third-party-risk reporting to the Risk Committee and feeds the OCC continuous-monitoring discussion. Source posture: U.S. interagency third-party risk management guidance (June 2023), the firm's third-party policy, and the firm's vendor-management framework. The attestation period is the prior calendar year.

Output emphasizes:
- Scope statement names the vendor (anonymized as "Vendor V"), the service (real-time card-transaction fraud screening), the system integration points, and the legal-entity perimeter.
- Control inventory pulls 14 controls from the upstream vendor-management control matrix, organized by lifecycle stage (planning / due diligence / contract / ongoing monitoring / termination).
- Evidence index lists 31 pieces of evidence: most recent SOC 2 Type II report (with carve-outs noted), quarterly KRI reviews, contract amendments, ongoing-monitoring meeting minutes, exit-test record, financial-condition reviews, regulatory-watch updates.
- Exceptions: two open exceptions. Exception 1: the most recent SOC 2 Type II carries a control gap on logical access reviews (linked to ISS-2025-0418); compensating control narrative covers the firm's quarterly access-recertification overlay. Exception 2: the vendor outage in Q2 2025 (linked to ME-2025-Q2-003 and to the kri-commentary block on OPS-001) demonstrated insufficient resilience; remediation is in progress (dual-vendor architecture review at Q3).
- Prior-period remediation: three prior-period issues, all remediated; evidence pointers cite the closure memos.
- Reviewer questions: anticipates OCC continuous-monitoring questions on dual-vendor architecture, exit-plan testing cadence, and whether the firm has a contingency for a sustained vendor outage.
- Assertion language is the firm's standard vendor-management attestation text, version 4.2.
- Confidence label: medium. Two open exceptions, one with active remediation and one pending Q3 architecture review.
- Human review required: yes; the pack goes to the Head of Operational Risk and the General Counsel before the Risk Committee.

### Scenario 2: BCBS 239 risk-data attestation pack from the Head of Risk Reporting

Input: the Head of Risk Reporting is producing the annual BCBS 239 risk-data attestation pack supporting the firm's most recent self-assessment (consuming the `bcbs239-gap-assessment` output). The attestation underpins the data-confidence label in the Risk Committee pack and the Y-14 attestation chain. Source posture: BCBS 239 Principle 1 (governance), the firm's risk-data policy, the firm's data-quality framework, and the most recent self-assessment.

Output emphasizes:
- Scope statement names the legal-entity perimeter (top-tier US BHC plus the IHC under Y-14 reporting), the systems in scope (the credit-loss data warehouse, the market-risk source systems, the operational-risk loss database, the regulatory-reporting layer), and the time period.
- Control inventory pulls 22 controls from the upstream risk-data control matrix, organized by BCBS 239 principle group (overarching governance, aggregation, reporting).
- Evidence index includes data-quality framework reports, reconciliation logs (between source systems and the regulatory-reporting layer), data-lineage documentation, the most recent BCBS 239 self-assessment, internal-audit reports on risk data, and the risk-data committee minutes.
- Exceptions: three open exceptions. Exception 1: Principle 6 (adaptability) — ad-hoc stress aggregation capability is 5 business days versus an internal target of 48 hours (linked to the gap-assessment Top-5 priority gap). Exception 2: Principle 2 (architecture) — manual reconciliation between two market-risk source systems persists (linked to ISS-2025-0301). Exception 3: Principle 3 (accuracy) — the operational-risk loss database carries a known understatement of small-event losses below the $50k threshold; investigation ongoing.
- Compensating controls: for Exception 1, the firm runs pre-computed stress aggregations weekly to reduce the risk of a 5-business-day delay during a stress event. For Exception 2, daily reconciliation reviews with documented sign-off. For Exception 3, the threshold-based exclusion is explicit in committee-pack commentary.
- Reviewer questions: anticipates internal-audit questions on whether the compensating control for Exception 1 actually mitigates the underlying gap, and FRB horizontal-review questions on the manual reconciliation in Exception 2.
- Assertion language is the firm's BCBS 239 risk-data attestation text, version 2.1.
- Confidence label: medium (three open exceptions, one of them in scope of an upcoming horizontal review).
- Human review required: yes; the pack goes to the CDO, the CRO, and the Audit Committee.

## Common pitfalls

1. Attestation as ceremony. The attestation is a sworn assertion, not a procedural step. Phase 2 must require named exceptions where exceptions exist (a clean attestation with material open issues elsewhere is a frequent regulator finding).
2. Evidence index by reference. "All evidence is on the SharePoint" is not an evidence index. Phase 2 must require one row per piece of evidence with system of record, period covered, and producer role.
3. Compensating-control hand-waving. Where an exception has a compensating control, the compensating control must be named, evidenced, and linked to the in-scope control. Phase 2 must reject `compensating_control_description` that does not name a discrete control.
4. Stale assertion language. Firms often roll forward assertion language without checking the underlying source criteria for changes. Phase 2 must require the assertion-language version and a year-over-year change check; if SSAE / PCAOB / SOX criteria have updated, the pack must reflect it.
5. Process-owner sub-certifications confused with executive certifications. Process-owner sub-certifications under SOX ladder up to the CEO/CFO 302/906 certifications; this skill produces the sub-certification, not the executive certification. Phase 2 must explicitly scope to the sub-certification level and route executive-certification work to securities counsel.
6. Vendor SOC report taken at face value. SOC 2 reports are management assertions of the service organization, not of the user firm. Where the attestation pack relies on a vendor SOC report, the user firm must (a) review carve-outs, (b) review complementary user entity controls (CUECs), and (c) attest to the operation of CUECs at the user firm. Phase 2 must include CUEC-level evidence in the evidence index when a SOC report is cited.
7. Prior-period remediation skipped. Phase 2 must require year-over-year remediation status; prior exceptions that have not been remediated by the current attestation are reportable and must appear in the current-period exceptions section.
8. Confidence-label inflation. The confidence label here reflects the strength of the evidence base, not the substantive control posture. A `high` confidence label requires complete evidence index coverage; phase 2 must reject `high` where any in-scope control has missing evidence.
