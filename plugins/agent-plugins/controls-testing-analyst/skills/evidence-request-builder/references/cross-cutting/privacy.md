# Privacy cross-cutting overlay — evidence-request-builder

Loaded when `engagement-scope.cross_cutting_overlay_set` includes `privacy`, or when the request list will pull artifacts containing NPI, PHI, PCI, or other regulated personal data. The overlay sets the privacy posture on individual rows and on the request list as a whole, and bears on what the request list may legitimately ask for and how the artifact moves once received.

## Why privacy belongs in the request list

Evidence frequently is personal data. Sample claim files carry NPI and may carry PHI. Customer prompts to AI systems carry whatever the customer typed. Adverse-action notice samples carry NPI. Reg E case files carry NPI. Complaint logs carry NPI and sometimes PHI. The request list cannot ask for that evidence without applying the firm's privacy controls, and the request list must be able to evidence its own privacy posture for downstream regulator scrutiny.

The discipline is: classify each row's `sensitivity` honestly at request time (not on receipt), name the lawful basis for the request in the row's `notes` where the basis is non-obvious, redact at the row level where redaction is the firm's standard and the request can be satisfied with redacted form, and segregate restricted rows from lower-classification rows in shared review folders.

## Specific regimes

- **GLBA Safeguards Rule** — 16 CFR Part 314 (FTC) for non-bank financial institutions; functional regulator equivalents for banks (interagency Safeguards rule, e.g., 12 CFR Part 30 Appendix B for OCC-supervised banks) [verify reference]. Bears on requests touching the firm's information-security program and on the firm's posture for sharing NPI evidence with second-line testers.
- **HIPAA** — 45 CFR Part 160 and Part 164. Where PHI may appear in narratives or files (medical-pay claims, life and health underwriting, certain disability evidence), the request list evidences the firm's BAA chain and the minimum-necessary handling. Restricted classification by default; HIPAA Privacy Rule §164.502(b) [verify subsection] minimum-necessary standard bears on whether a request for full claim-file PDFs is justified or whether a redacted form satisfies the test objective.
- **State privacy laws** — California (CCPA/CPRA), Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), Texas, Florida, and others as adopted. Right-to-delete and right-to-correct request fulfilment evidence is itself sometimes the testing artifact; the request list cites the state statute and the firm's response register.
- **FCRA / FACTA** — when consumer-report data appears in evidence (adverse-action samples, fraud-investigation files), FCRA disposal rules (16 CFR Part 682) and the FTC Red Flags Rule apply. The request list notes consumer-report-data presence and the access posture.
- **Reg S-P / Reg S-ID** — for SEC-registered entities, customer-information handling. Bears on requests for customer files at advisers and broker-dealers.
- **GDPR / UK GDPR** — for engagements involving EU/EEA data subjects, Article 5 principles (purpose limitation, data minimisation) bear on what evidence the request list may legitimately ask for; Article 28 governs processor relationships when third-party reviewers handle the evidence.
- **NYDFS 23 NYCRR Part 500** — overlaps with cyber overlay; §500.13 asset management and data retention bears on retention posture for evidence after the testing closes.

## Implications for request-list construction

- **Row-level sensitivity classification at request time.** A request list that defaults every row to `internal` is not honest. Classify when the request is drafted; the workpaper later confirms or escalates the classification on receipt.
- **Minimum-necessary per request.** Each request asks for the minimum evidence the test objective needs. A request for "the full claim file PDF" when the test objective is timing-only should be reshaped to ask for the claim-event log; the full file is a separate request only if the test objective needs the file content. Bears especially on PHI and NPI under HIPAA minimum-necessary and GLBA Safeguards.
- **Redaction posture per request.** Some requests can be satisfied with redacted artifacts (account numbers redacted to last-4, SSN redacted entirely, customer name pseudonymised by sample ID). The request list names the redaction expectation in the artifact description; the workpaper later confirms the firm's redaction was applied.
- **Source-of-record provenance bears on privacy.** A screenshot of NPI taken on a personal device is a privacy incident, not just a provenance concern. The request specifies that the artifact must come from the system-of-record extract or a corporate-managed environment; the workpaper later applies the device-class check.
- **Custodian-role for restricted rows.** Where the request asks for restricted-classification artifacts, the owner-role on the request includes a privacy-aware role (privacy officer, data protection officer, HIPAA privacy officer) for sign-off in addition to the operational owner.
- **Retention after testing.** When the cycle closes, the artifacts requested may themselves carry retention obligations under the firm's records-retention schedule. The request list does not control retention; the closure binder (`evidence-binder` in `risk-compliance-core`) carries the retention posture into the lifecycle.
- **SAR content carries a separate access posture.** SAR content access is restricted to authorised reviewers under 31 CFR §1020.320 [verify subsection] and bears on whether the second-line testing program can request SAR content directly. The request list typically asks for the case-management file with SAR content access controlled by the BSA officer's process; SAR-decision testing is a separate cycle with its own access-control posture.
- **Customer prompts and outputs in AI testing.** Where the test addresses an AI system, customer prompts are NPI by default; the request list classifies sensitivity, names the de-identification posture, and asks for the firm's prompt-and-output logging configuration evidence rather than restating customer content.

## Anchors used by this overlay

- 16 CFR Part 314 — FTC Safeguards Rule.
- 12 CFR Part 30 Appendix B — Interagency Guidelines Establishing Information Security Standards (for OCC-supervised banks) [verify reference and current applicability].
- 45 CFR Parts 160 and 164 — HIPAA Privacy and Security Rules; §164.502(b) minimum-necessary [verify subsection].
- 16 CFR Part 682 — FCRA disposal rule.
- CCPA / CPRA — Cal. Civ. Code §1798.100 et seq.
- Reg S-P — 17 CFR §248.30; SEC 2024 Reg S-P amendments incident-notification provisions [verify subsection].
- Reg S-ID — 17 CFR §248.201-202.
- GDPR — Regulation (EU) 2016/679, Articles 5 and 28.
- UK GDPR — Data Protection Act 2018.
- 31 CFR §1020.320 — SAR confidentiality [verify subsection].
- NYDFS 23 NYCRR §500.13 — asset management and data retention [verify subsection].
