# cross-cutting

One section per topic. Read only the sections the scope calls for.

## cyber

### Cyber cross-cutting overlay — evidence-request-builder

Loaded when `scope.cross_cutting_overlay_set` includes `cyber`, when the test addresses IAM controls, data-protection controls, or NYDFS Part 500-mandated areas, or when the firm is a Covered Entity under 23 NYCRR Part 500. Supplements `references/source-anchors.md`.

#### Request-list conventions for cyber control testing

Cyber control testing PBC lists carry methodology distinct from financial-control testing:

- **Sample design follows population behaviour, not transaction count.** Access-recertification populations stratify by privilege tier (standard / privileged / service / break-glass), data sensitivity, and recertifier role. Vulnerability-management populations stratify by severity and asset criticality. The request list reflects the stratification by sample reference per row.
- **System-of-record extracts carry an extract date.** IAM entitlement extracts, vulnerability-scan output, and SIEM logs run at different times produce different populations; the request names the extract cutoff date and the run-by role expectation. The workpaper later applies the extract-integrity check.
- **Reperformance-source requests draw the production environment.** Where the test plan calls for reperformance against the production environment (re-running an entitlement query, re-validating a scan finding, re-reading an alert disposition), the request names production scope rather than a test-environment scope. Test-environment evidence does not satisfy production-control reperformance.
- **Privileged-access requests carry restricted sensitivity by default.** Privileged accounts, service accounts with elevated rights, and break-glass accounts are restricted-classification rows; the sensitivity column drives downstream handling and routing.

#### Cyber-supervisory anchors (load by reference; do not restate)

- **NYDFS 23 NYCRR Part 500.7 — Access Privileges and Management** [verify subsection labels against the latest amendment]. Periodic review of access privileges; risk-based-authentication-exemption certification. https://www.dfs.ny.gov/industry_guidance/cybersecurity .
- **NYDFS 23 NYCRR Part 500** generally — §500.3 cybersecurity policy, §500.4 CISO, §500.5 vulnerability management, §500.7 access privileges, §500.9 risk assessment, §500.11 third-party service-provider security, §500.13 asset management and data retention, §500.14 monitoring and training, §500.15 encryption, §500.16 incident response and business continuity, §500.17 notices, §500.19 exemptions [verify subsection labels].
- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section]. https://ithandbook.ffiec.gov/it-booklets/information-security.aspx [verify URL].
- **NIST SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations** (January 2022) [verify section labels for assessment objectives, methods, and assessment objects]. https://csrc.nist.gov/pubs/sp/800/53/a/r5/final .
- **NIST Cybersecurity Framework 2.0** (February 2024) [verify version number and category labels]. https://www.nist.gov/cyberframework .
- **CISA Zero Trust Maturity Model 2.0** (April 2023) [verify version and pillar labels]. https://www.cisa.gov/zero-trust-maturity-model .

#### Cyber-control-area request notes

##### Access-recertification testing (Part 500.7-relevant)

- Request conventions: per-sample recertification packet PDF (entitlement list reviewed, recertifier per-entitlement attestation or blanket attestation, timestamps); IAM entitlement extract CSV per sampled user as of the recertification cutoff date; revocation-ticket evidence per removed entitlement; HR-IAM termination-feed reconciliation extract for the period (full population, not sample); SoD exception log extract; privileged-access review packet (separate quarterly artifact, requested separately and the workpaper covers the methodology overlap question); IAM-system change log for the period (rules out silent intra-period entitlement reshape); annual-certification working-paper section covering §500.7. Privileged-account requests are restricted-classification.

##### Vulnerability-management testing (Part 500.5-relevant)

- Request conventions: vulnerability-scan output for the period CSV per scan run (asset, vulnerability, severity, scan date, remediation status); per-sample remediation evidence (ticket, fix evidence, retest evidence); exception-register extract for accepted-risk vulnerabilities (with senior-officer approval evidence); scan-coverage evidence (asset register joined to scan-coverage register). Penetration-test reports and red-team reports are third-party-assurance class; the request notes the testing scope, date, and finding-status as of report date.

##### Logging and monitoring testing (Part 500.14-relevant)

- Request conventions: SIEM log-source register extract; alert sample with disposition rationale, disposer role, closure timeline; SIEM-coverage testing extract joining the asset register to the log-source register (missing log sources are surfaced); on-call rotation evidence for the period.

##### Encryption testing (Part 500.15-relevant)

- Request conventions: per-asset encryption-configuration evidence (encryption-at-rest configuration screenshot or system export, encryption-in-transit configuration evidence); key-management evidence (key-rotation log per key); customer-managed-key posture evidence where applicable; unencrypted-exception register for the period with senior-officer approval evidence per §500.15(b) [verify].

##### Incident-response testing (Part 500.16-relevant)

- Request conventions: per-sample tabletop evidence (date, scenario, participants by role, observations, action items, action-item closure tracking); IR-runbook current version; IR-runbook revision log for the period; per-incident-of-record file (incident timeline, containment evidence, recovery evidence, post-incident review, regulatory-notification evidence per §500.17(a) where applicable).

##### Pen-test and red-team evidence reliance

- Request conventions: full report (not summary), with the testing scope, methodology, finding-status as of report date; the firm's response evidence to the findings (acceptance, remediation, retest); engagement letter or scope-of-work for the testing (for reliance test note on the testing's scope).

##### Annual certification (Part 500.17(b)-relevant)

- Request conventions: certification working-paper file for the most recent certification cycle, including the §500.17(b) supporting evidence per requirement element; certification-period exception-and-remediation log; CISO review-and-attestation evidence on the certification preparation.

#### Cross-link to NIST SP 800-53A documentation conventions

Where the firm has adopted NIST SP 800-53 control families and SP 800-53A assessment methodology, the request list aligns to the assessment objects (specifications, mechanisms, activities, individuals); per control under test, the request asks for evidence covering the SP 800-53A assessment objects and the firm's POAM (Plan of Action and Milestones) entries where applicable.

#### Audience and tone

A request list drafted with an upcoming NYDFS examination in mind reads heavier on Part 500 subsection citation, the §500.17(b) certification-evidence trail, and the CISO-attested elements. A request list drafted for the firm's CISO and the cyber-risk committee reads heavier on technical detail and remediation tracking. A request list drafted for internal-audit reliance reads heavier on the system-of-record extract-integrity posture and the reperformance-source distinction (production versus test environment).

## privacy

### Privacy cross-cutting overlay — evidence-request-builder

Loaded when `scope.cross_cutting_overlay_set` includes `privacy`, or when the request list will pull artifacts containing NPI, PHI, PCI, or other regulated personal data. The overlay sets the privacy posture on individual rows and on the request list as a whole, and bears on what the request list may legitimately ask for and how the artifact moves once received.

#### Why privacy belongs in the request list

Evidence frequently is personal data. Sample claim files carry NPI and may carry PHI. Customer prompts to AI systems carry whatever the customer typed. Adverse-action notice samples carry NPI. Reg E case files carry NPI. Complaint logs carry NPI and sometimes PHI. The request list cannot ask for that evidence without applying the firm's privacy controls, and the request list must be able to evidence its own privacy posture for downstream regulator scrutiny.

The discipline is: classify each row's `sensitivity` honestly at request time (not on receipt), name the lawful basis for the request in the row's `notes` where the basis is non-obvious, redact at the row level where redaction is the firm's standard and the request can be satisfied with redacted form, and segregate restricted rows from lower-classification rows in shared review folders.

#### Specific regimes

- **GLBA Safeguards Rule** — 16 CFR Part 314 (FTC) for non-bank financial institutions; functional regulator equivalents for banks (interagency Safeguards rule, e.g., 12 CFR Part 30 Appendix B for OCC-supervised banks) [verify reference]. Bears on requests touching the firm's information-security program and on the firm's posture for sharing NPI evidence with second-line testers.
- **HIPAA** — 45 CFR Part 160 and Part 164. Where PHI may appear in narratives or files (medical-pay claims, life and health underwriting, certain disability evidence), the request list evidences the firm's BAA chain and the minimum-necessary handling. Restricted classification by default; HIPAA Privacy Rule §164.502(b) [verify subsection] minimum-necessary standard bears on whether a request for full claim-file PDFs is justified or whether a redacted form satisfies the test objective.
- **State privacy laws** — California (CCPA/CPRA), Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), Texas, Florida, and others as adopted. Right-to-delete and right-to-correct request fulfilment evidence is itself sometimes the testing artifact; the request list cites the state statute and the firm's response register.
- **FCRA / FACTA** — when consumer-report data appears in evidence (adverse-action samples, fraud-investigation files), FCRA disposal rules (16 CFR Part 682) and the FTC Red Flags Rule apply. The request list notes consumer-report-data presence and the access posture.
- **Reg S-P / Reg S-ID** — for SEC-registered entities, customer-information handling. Bears on requests for customer files at advisers and broker-dealers.
- **GDPR / UK GDPR** — for engagements involving EU/EEA data subjects, Article 5 principles (purpose limitation, data minimisation) bear on what evidence the request list may legitimately ask for; Article 28 governs processor relationships when third-party reviewers handle the evidence.
- **NYDFS 23 NYCRR Part 500** — overlaps with cyber overlay; §500.13 asset management and data retention bears on retention posture for evidence after the testing closes.

#### Implications for request-list construction

- **Row-level sensitivity classification at request time.** A request list that defaults every row to `internal` is not honest. Classify when the request is drafted; the workpaper later confirms or escalates the classification on receipt.
- **Minimum-necessary per request.** Each request asks for the minimum evidence the test objective needs. A request for "the full claim file PDF" when the test objective is timing-only should be reshaped to ask for the claim-event log; the full file is a separate request only if the test objective needs the file content. Bears especially on PHI and NPI under HIPAA minimum-necessary and GLBA Safeguards.
- **Redaction posture per request.** Some requests can be satisfied with redacted artifacts (account numbers redacted to last-4, SSN redacted entirely, customer name pseudonymised by sample ID). The request list names the redaction expectation in the artifact description; the workpaper later confirms the firm's redaction was applied.
- **Source-of-record provenance bears on privacy.** A screenshot of NPI taken on a personal device is a privacy incident, not just a provenance concern. The request specifies that the artifact must come from the system-of-record extract or a corporate-managed environment; the workpaper later applies the device-class check.
- **Custodian-role for restricted rows.** Where the request asks for restricted-classification artifacts, the owner-role on the request includes a privacy-aware role (privacy officer, data protection officer, HIPAA privacy officer) for sign-off in addition to the operational owner.
- **Retention after testing.** When the cycle closes, the artifacts requested may themselves carry retention obligations under the firm's records-retention schedule. The request list does not control retention; the closure binder (`evidence-binder` in `risk-compliance-core`) carries the retention posture into the lifecycle.
- **SAR content carries a separate access posture.** SAR content access is restricted to authorised reviewers under 31 CFR §1020.320 [verify subsection] and bears on whether the second-line testing program can request SAR content directly. The request list typically asks for the case-management file with SAR content access controlled by the BSA officer's process; SAR-decision testing is a separate cycle with its own access-control posture.
- **Customer prompts and outputs in AI testing.** Where the test addresses an AI system, customer prompts are NPI by default; the request list classifies sensitivity, names the de-identification posture, and asks for the firm's prompt-and-output logging configuration evidence rather than restating customer content.

#### Anchors used by this overlay

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
