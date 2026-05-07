# Cyber cross-cutting overlay — qa-workpaper

Loaded when `engagement-scope.cross_cutting_overlay_set` includes `cyber`, when the QA review covers a workpaper addressing IAM controls, data-protection controls, vulnerability-management controls, or NYDFS Part 500-mandated areas, or when the firm is a Covered Entity under 23 NYCRR Part 500. Supplements `references/source-anchors.md`.

## Why cyber QA carries distinct conventions

Cyber control workpapers fail QA on evidence-reliability more often than financial-control workpapers. The recurring patterns:

- **Vendor-supplied scan results cited as evidence without firm-side reliance assessment.** A workpaper that cites a vendor's SaaS-platform scan output as evidence of vulnerability remediation without documenting the firm's reliance test (scan scope, scan recency, vendor's CUEC posture, the firm's independent verification of remediation on critical findings) is an evidence-reliability deficiency.
- **Screenshot-only access reviews.** A workpaper that documents access-recertification with screenshots of the IAM tool's recertification screen, without a system-of-record entitlement extract reperformed against the screenshot, is an evidence-reliability deficiency. Screenshots are ephemeral and operator-controlled; they do not substitute for an extract.
- **Production-versus-test environment evidence reliance.** Cyber control testing where the preparer cited the test environment as evidence of production posture is a structural finding. The QA reviewer challenges environment-provenance on every cyber evidence item.
- **Privileged-access tolerable-rate floor of zero.** Most firm policies set zero tolerance for privileged-access exceptions; the QA reviewer challenges severity ratings that do not reflect the floor.

## QA conventions for cyber control workpapers

- **Sample-design QA.** The QA reviewer confirms sample stratification by privilege tier (standard / privileged / service / break-glass), data sensitivity, and recertifier role for access-recertification workpapers; by severity and asset criticality for vulnerability-management workpapers; and by alert category for SIEM alert-disposition workpapers.
- **System-of-record evidence integrity QA.** The QA reviewer confirms IAM entitlement extracts, vulnerability-scan output, and SIEM logs name the extract date, the run-by role, and the completeness check against an independent system count.
- **Reperformance QA.** Where the test plan called for reperformance, the QA reviewer reperforms a small subsample of the entitlement query, the scan-finding validation, or the alert disposition; QA reperform is the most credible QA dimension for cyber workpapers.

## Cyber-supervisory anchors (load by reference; do not restate)

- **NYDFS 23 NYCRR Part 500.7 — Access Privileges and Management** [verify subsection labels against the latest amendment]. https://www.dfs.ny.gov/industry_guidance/cybersecurity .
- **NYDFS 23 NYCRR Part 500** generally — §500.3 cybersecurity policy, §500.4 CISO, §500.5 vulnerability management, §500.7 access privileges, §500.9 risk assessment, §500.11 third-party service-provider security, §500.13 asset management and data retention, §500.14 monitoring and training, §500.15 encryption, §500.16 incident response and business continuity, §500.17 notices, §500.19 exemptions [verify subsection labels].
- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section]. https://ithandbook.ffiec.gov/it-booklets/information-security.aspx [verify URL].
- **NIST SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations** (January 2022) [verify section labels for assessment objectives, methods, and assessment objects]. https://csrc.nist.gov/pubs/sp/800/53/a/r5/final .
- **NIST Cybersecurity Framework 2.0** (February 2024) [verify version number and category labels]. Used as a control-categorisation anchor when the firm has mapped testing scope to CSF categories. https://www.nist.gov/cyberframework .

## Cyber-control-area QA notes

### Access-recertification testing — QA scope items

- QA conventions: the QA reviewer reperforms entitlement queries for a small subsample of the privileged tier; confirms HR-IAM feed reconciliation evidence for terminated employees is documented (terminations typically expanded from sample to full population); confirms the attestation form supports per-entitlement attestation versus blanket approval (a blanket-approval form is a design-effectiveness QA finding even when operating effectiveness is high). Privileged-access exceptions trigger issue elevation regardless of overall sample deviation rate.

### Vulnerability-management testing — QA scope items

- QA conventions: the QA reviewer confirms scan-frequency cadence reperformance, MTTR-by-severity calculation against the firm's policy clocks, and exception-register testing as a separate procedure (tracked exceptions versus exceptions that have aged out without remediation or formal acceptance). Reliance on vendor scan output without firm reperformance on critical findings is the recurring deficiency.

### Pen-test and red-team evidence reliance — QA scope items

- QA conventions: the QA reviewer confirms reliance on a pen-test or red-team report carries the testing scope, testing date, finding-status as of report date, and the firm's remediation tracking. Reliance on a pen-test summary without the full report is partial evidence; the QA reviewer flags this as a limitation, not as substitute evidence.

### Incident-response testing — QA scope items

- QA conventions: the QA reviewer confirms tabletop-testing evidence (date, scenario, participants by role, observations, action-item closure tracking) is sampled, and that the workpaper distinguishes design (the IR plan) from operating (the tabletop output and closure of action items).

### SIEM logging and alert-disposition testing — QA scope items

- QA conventions: the QA reviewer confirms SIEM-coverage testing reads the asset register against the SIEM-log-source register by sample (missing log sources are design-dimension exceptions); confirms alert-disposition testing reads the alert sample by category with the disposition rationale and the closure timeline against the firm's policy clock.

### Encryption testing — QA scope items

- QA conventions: the QA reviewer confirms encryption-at-rest and encryption-in-transit testing reads the configuration against the firm's standard by asset sample, and that key-management testing reads the key-rotation evidence and customer-managed-key posture (where applicable). Unencrypted exceptions tracked via the exception register are read against the senior-officer approval requirement under §500.15(b) [verify].

### Annual certification scope — QA scope items

- QA conventions: where the workpaper supports the §500.17(b) annual certification, the QA reviewer reads heavier on certification-scope items, evidence-reliability dimensions, and reviewer-separation evidence. Findings during the certification period that touch certifiable elements are flagged in the QA review note as items the senior-officer certification preparer must consider; the workpaper does not certify, and neither does the QA review.

## Cross-link to NIST SP 800-53A documentation conventions

Where the firm has adopted NIST SP 800-53 control families and SP 800-53A assessment methodology, the QA reviewer confirms the workpaper restates the assessment objective, the assessment method (examine, interview, test) per procedure, and the assessment objects (specifications, mechanisms, activities, individuals) sampled. The QA review note's deficiency findings map to the SP 800-53 control number for traceability into the firm's POAM (Plan of Action and Milestones) where one is maintained.

## Audience and tone

A QA review note drafted for the firm's CISO or cyber-risk committee reads heavier on the technical evidence-reliability dimensions and the reperformance posture. A QA note drafted with an upcoming NYDFS examination in mind reads heavier on the Part 500 subsection citation, the §500.17(b) certification posture, and the CISO-attested elements. A QA note for internal-audit reliance reads heavier on the system-of-record extract-integrity posture and the reviewer-separation evidence.
