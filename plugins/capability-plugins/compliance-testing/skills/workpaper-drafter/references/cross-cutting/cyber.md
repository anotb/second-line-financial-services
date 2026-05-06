# Cyber cross-cutting overlay — workpaper-drafter

Loaded when `engagement-scope.cross_cutting_overlay_set` includes `cyber`, when the test addresses IAM controls, data-protection controls, or NYDFS Part 500-mandated areas, or when the firm is a Covered Entity under 23 NYCRR Part 500. Supplements `references/source-anchors.md`.

## Workpaper conventions for cyber control testing

Cyber control testing workpapers carry methodology distinct from financial-control testing:

- **Sample design follows population behaviour, not transaction count.** Access-recertification populations stratify by privilege tier (standard / privileged / service / break-glass), data sensitivity, and recertifier role. Vulnerability-management populations stratify by severity and asset criticality. The sample-design rationale in the workpaper restates the stratification decision.
- **System-of-record evidence carries an extract-integrity check.** IAM entitlement extracts, vulnerability-scan output, and SIEM logs run at different times produce different populations; the workpaper names the extract date, the run-by role, and what the preparer did to confirm completeness against an independent system count.
- **Reperformance is the standard procedure for technical controls.** Where the test plan calls for reperformance (re-running an entitlement query, re-validating a scan finding, re-reading an alert), the workpaper notes preparer access to the production environment versus reliance on a system-generated extract; production-access evidence is stronger but rarely available to second-line testers.

## Cyber-supervisory anchors (load by reference; do not restate)

- **NYDFS 23 NYCRR Part 500.7 — Access Privileges and Management** [verify subsection labels against the latest amendment]. Periodic review of access privileges; risk-based authentication exceptions require senior-officer certification. https://www.dfs.ny.gov/industry_guidance/cybersecurity .
- **NYDFS 23 NYCRR Part 500** generally — §500.3 cybersecurity policy, §500.4 CISO, §500.5 vulnerability management, §500.7 access privileges, §500.9 risk assessment, §500.11 third-party service-provider security, §500.13 asset management and data retention, §500.14 monitoring and training, §500.15 encryption, §500.16 incident response and business continuity, §500.17 notices, §500.19 exemptions [verify subsection labels].
- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section]. https://ithandbook.ffiec.gov/it-booklets/information-security.aspx [verify URL].
- **NIST SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations** (January 2022) [verify section labels for assessment objectives, methods, and assessment objects]. https://csrc.nist.gov/pubs/sp/800/53/a/r5/final .
- **NIST Cybersecurity Framework 2.0** (February 2024) [verify version number and category labels]. Used as a control-categorisation anchor for testing scope set against firm-mapped CSF categories. https://www.nist.gov/cyberframework .
- **CISA Zero Trust Maturity Model 2.0** (April 2023) [verify version and pillar labels]. Used where the firm's IAM testing scope includes zero-trust posture. https://www.cisa.gov/zero-trust-maturity-model .

## Cyber-control-area workpaper notes

### Access-recertification testing (Part 500.7-relevant)

- Workpaper conventions: sample design stratified by privilege tier; reperformance against IAM extract; HR-IAM feed reconciliation for terminated employees with separate sample (terminations typically expand from sample to full population because the privileged-not-revoked-after-termination scenario carries asymmetric impact); attestation form review reads whether the form supports per-entitlement attestation versus blanket approval (a blanket-approval form is a design exception even when operating effectiveness is high).
- Privileged-access testing has a tolerable rate of zero in most firm policies; the workpaper aggregation makes that explicit and any privileged exception triggers the issue elevation regardless of overall sample deviation rate.

### Vulnerability-management testing (Part 500.5-relevant)

- Workpaper conventions: sample design stratified by severity and asset criticality; the procedure tests cadence (scan frequency), MTTR by severity, and exception-register integrity (tracked exceptions versus exceptions that have aged out without remediation or formal acceptance). Exception-register testing is its own sub-procedure; the workpaper carries it as a separate procedure ID.

### Pen-test and red-team evidence reliance

- Workpaper conventions: external pen-test or red-team reports are third-party-assurance evidence; the reliance test note covers the testing scope, the testing date, the finding-status as of report date, and the firm's remediation tracking. Reliance on a pen-test summary without the full report is partial evidence; the workpaper notes the limitation.

### Incident-response testing (Part 500.16-relevant)

- Workpaper conventions: tabletop testing evidence (tabletop date, scenario, participants by role, observations, action items, action-item closure tracking) is read by sample of past tabletops; the workpaper distinguishes design (the IR plan) from operating (the tabletop output and closure of action items).

### Logging and monitoring testing (Part 500.14-relevant)

- Workpaper conventions: SIEM-coverage testing reads the asset register against the SIEM-log-source register by sample; missing log sources are exceptions on the design dimension. Alert-disposition testing reads alert sample by category with the disposition rationale and the closure timeline against the firm's policy clock.

### Encryption testing (Part 500.15-relevant)

- Workpaper conventions: encryption-at-rest and encryption-in-transit testing reads the configuration against the firm's standard by asset sample; key-management testing reads the key-rotation evidence and the customer-managed-key posture (where applicable). Unencrypted exceptions tracked via the exception register are read against the senior-officer approval requirement under §500.15(b) [verify].

### Annual certification (Part 500.17(b)-relevant)

- Workpaper conventions: testing that supports the annual certification reads the certification scope against the §500.17(b) requirements; findings during the certification period that touch certifiable elements (control failures, material gaps) are flagged in the workpaper limitations as items the senior-officer certification preparer must consider, not items the workpaper concludes on. The workpaper does not certify; the senior officer certifies.

## Cross-link to NIST SP 800-53A documentation conventions

Where the firm has adopted NIST SP 800-53 control families and SP 800-53A assessment methodology, the workpaper restates the assessment objective, the assessment method (examine, interview, test) per procedure, and the assessment objects (specifications, mechanisms, activities, individuals) sampled. The workpaper aggregation maps observed exceptions to the SP 800-53 control number for traceability into the firm's POAM (Plan of Action and Milestones) where one is maintained.

## Audience and tone

A workpaper drafted for the firm's CISO and the cyber-risk committee reads heavier on technical detail and remediation tracking. A workpaper drafted with an upcoming NYDFS examination in mind reads heavier on Part 500 subsection citation, the §500.17(b) certification posture, and the CISO-attested elements. A workpaper drafted for internal-audit reliance reads heavier on the evidence reliance and the system-of-record extract-integrity posture.
