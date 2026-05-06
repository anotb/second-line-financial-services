# Cyber cross-cutting overlay — test-plan-builder

Loaded when `engagement-scope.cross_cutting_overlay_set` includes `cyber`, when the test addresses IAM controls, data-protection controls, or NYDFS Part 500-mandated areas, or when the firm is a Covered Entity under 23 NYCRR Part 500. Supplements `references/source-anchors.md`.

## Test-plan conventions for cyber control testing

Cyber control test plans carry methodology distinct from financial-control test planning:

- **Sample design follows population behaviour, not transaction count.** Access-recertification populations stratify by privilege tier (standard / privileged / service / break-glass), data sensitivity, and recertifier role. Vulnerability-management populations stratify by severity and asset criticality. The plan's population-and-sampling-reference section restates the stratification decision and the rationale.
- **Tolerable rate is severity-driven for zero-tolerable populations.** Privileged-access populations, sanctions-screening populations, and customer-funds-segregation populations typically carry a zero-tolerable rate. The plan names the zero-tolerable subset and the severity-driven aggregation read so the workpaper later does not collapse it into the overall rate.
- **Reperformance is the standard procedure for technical controls.** Where the plan calls for reperformance (re-running an entitlement query, re-validating a scan finding, re-reading an alert), the plan names the production-access prerequisite and the alternative procedure when production access is not available to the second-line tester (system-generated extract with extract-integrity check).
- **Extract-integrity check is a planned procedure, not a fieldwork afterthought.** IAM entitlement extracts, vulnerability-scan output, and SIEM logs run at different times produce different populations; the plan names the extract date, the extract-source role, and the independent count the workpaper will reconcile against.

## Cyber-supervisory anchors (load by reference; do not restate)

- **NYDFS 23 NYCRR Part 500.7 — Access Privileges and Management** [verify subsection labels against the latest amendment]. Periodic review of access privileges; risk-based authentication exceptions require senior-officer certification. https://www.dfs.ny.gov/industry_guidance/cybersecurity .
- **NYDFS 23 NYCRR Part 500** generally — §500.3 cybersecurity policy, §500.4 CISO, §500.5 vulnerability management, §500.7 access privileges, §500.9 risk assessment, §500.11 third-party service-provider security, §500.13 asset management and data retention, §500.14 monitoring and training, §500.15 encryption, §500.16 incident response and business continuity, §500.17 notices, §500.19 exemptions [verify subsection labels].
- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section]. https://ithandbook.ffiec.gov/it-booklets/information-security.aspx [verify URL].
- **NIST SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations** (January 2022) [verify section labels for assessment objectives, methods, and assessment objects]. https://csrc.nist.gov/pubs/sp/800/53/a/r5/final .
- **NIST Cybersecurity Framework 2.0** (February 2024) [verify version number and category labels]. Used as a control-categorisation anchor when the firm has mapped controls to CSF categories. https://www.nist.gov/cyberframework .
- **CISA Zero Trust Maturity Model 2.0** (April 2023) [verify version and pillar labels]. Used where the IAM test plan scope includes zero-trust posture. https://www.cisa.gov/zero-trust-maturity-model .
- **SEC Reg S-K Item 106 — Cybersecurity Risk Management, Strategy, and Governance disclosure** [verify Item number and current effective date]. Cyber-disclosure-process testing scope where the firm is a registrant. https://www.ecfr.gov/current/title-17/chapter-II/part-229/section-229.106 [verify URL].

## Cyber-control-area test-plan notes

### Access-recertification testing (Part 500.7-relevant)

- Test-plan conventions: criteria section names §500.7 [verify subsection] (least privilege, periodic review) and the firm's IAM control standard; population is the recertification packets due in the period; sample stratified by privilege tier (standard / privileged / service); design procedures cover the attestation form structure (does the form support per-entitlement attestation or only per-system blanket approval), the campaign workflow, and the HR-IAM integration architecture; operating procedures cover per-packet attestation reperformance, IAM-system reperformance for revocations, and HR-IAM feed reconciliation for terminated employees.
- Privileged-access subset: zero tolerable rate; aggregation is severity-driven, not rate-driven; the plan names the privileged sub-sample size and the rationale for any expansion to full enumeration.

### Vulnerability-management testing (Part 500.5-relevant)

- Test-plan conventions: criteria section names §500.5 [verify subsection] and the firm's vulnerability-management standard; population is the vulnerabilities identified in the period; sample stratified by severity and asset criticality; design procedures cover the scan-tool configuration and coverage; operating procedures cover scan cadence, MTTR by severity, and the exception-register integrity (tracked exceptions versus exceptions that have aged out without remediation or formal acceptance).

### Pen-test and red-team evidence reliance

- Test-plan conventions: external pen-test or red-team reports are third-party-assurance evidence; the plan's reliance posture covers the testing scope, the testing date, the finding-status as of report date, and the firm's remediation tracking. Reliance on a pen-test summary without the full report is partial evidence; the plan's limitations section names the constraint.

### Incident-response testing (Part 500.16-relevant)

- Test-plan conventions: criteria section names §500.16 [verify subsection] and the firm's IR plan; population is the incidents and tabletop exercises in the period; design procedures cover the IR plan adequacy review; operating procedures cover tabletop evidence (tabletop date, scenario, participants by role, observations, action items, action-item closure) by sample.

### Logging and monitoring testing (Part 500.14-relevant)

- Test-plan conventions: SIEM-coverage test plans read the asset register against the SIEM-log-source register by sample (missing log sources are exceptions on the design dimension); alert-disposition test plans cover alert sample by category with the disposition rationale and the closure timeline against the firm's policy clock.

### Encryption testing (Part 500.15-relevant)

- Test-plan conventions: encryption-at-rest and encryption-in-transit test plans read the configuration against the firm's standard by asset sample; key-management test plans read key-rotation evidence and customer-managed-key posture (where applicable). Unencrypted exceptions tracked via the exception register are read against the senior-officer approval requirement under §500.15(b) [verify].

### Annual certification (Part 500.17(b)-relevant)

- Test-plan conventions: testing that supports the annual certification reads against the §500.17(b) requirements; findings during the certification period that touch certifiable elements (control failures, material gaps) are flagged in the plan limitations as items the senior-officer certification preparer must consider, not items the plan concludes on. The plan does not certify; the senior officer certifies.

## Cross-link to NIST SP 800-53A documentation conventions

Where the firm has adopted NIST SP 800-53 control families and SP 800-53A assessment methodology, the plan restates the assessment objective, the assessment method (examine, interview, test) per procedure, and the assessment objects (specifications, mechanisms, activities, individuals) sampled. The plan names the SP 800-53 control number per criterion for traceability into the firm's POAM (Plan of Action and Milestones) where one is maintained.

## Audience and tone

A test plan drafted for the firm's CISO and the cyber-risk committee reads heavier on technical detail, expected procedure depth, and the populations the cycle will fully enumerate versus sample. A plan drafted with an upcoming NYDFS examination in mind reads heavier on Part 500 subsection citation, the §500.17(b) certification posture, and the CISO-attested elements the cycle is designed to support. A plan drafted for internal-audit reliance reads heavier on the evidence reliance and the system-of-record extract-integrity posture set out as planned procedures.
