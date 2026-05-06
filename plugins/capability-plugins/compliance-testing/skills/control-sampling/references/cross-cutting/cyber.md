# Cyber cross-cutting overlay — control-sampling

Loaded when `engagement-scope.cross_cutting_overlay_set` includes `cyber`, when the test addresses IAM controls, vulnerability management, data-protection controls, or covered-entity-cybersecurity-mandated areas, or when the firm is a Covered Entity under a state cybersecurity regime (e.g., NYDFS 23 NYCRR Part 500). Supplements `references/source-anchors.md`.

## Population definition conventions for cyber control sampling

Cyber control testing populations carry definitions distinct from financial-control testing:

- **Population items are tickets, alerts, identities, packets, scans, or configurations — not transactions.** Vulnerability remediation tickets closed in the period; SIEM alerts triaged in the period; entitled identities active during the period; recertification packets generated in the period; vulnerability-scan runs during the period; configuration-baseline drift events during the period. The memo names the population in items the sample can draw from.
- **Identities are not packets.** A single user can have multiple recertification packets across roles; a single packet can address multiple entitlements. The memo names which is the population (typically packets for recertification testing; typically identities for terminated-user testing).
- **Extract integrity matters more than transaction-system reconciliation.** IAM entitlement extracts, vulnerability-scan output, and SIEM logs run at different times produce different populations. The memo names the extract date, the run-by role, and the completeness check (entitlement count reconciled to the IAM platform's user count; scan output reconciled to the asset-register asset count; alert count reconciled to the SIEM rule-firing log).
- **Service accounts and break-glass identities are typically excluded from standard recertification populations and sampled separately.** The memo names the exclusion and the separate sample where applicable.

## Cyber-supervisory anchors (load by reference; do not restate)

- **NYDFS 23 NYCRR Part 500.7 — Access Privileges and Management** [verify subsection labels against the latest amendment]. The standard anchor for access-recertification sampling at NYDFS Covered Entities. https://www.dfs.ny.gov/industry_guidance/cybersecurity .
- **NYDFS 23 NYCRR Part 500.5 — Vulnerability Management** [verify subsection labels]. Vulnerability ticket and remediation populations. https://www.dfs.ny.gov/industry_guidance/cybersecurity .
- **NYDFS 23 NYCRR Part 500** generally — §500.3 cybersecurity policy, §500.4 CISO, §500.9 risk assessment, §500.11 third-party service-provider security, §500.13 asset management and data retention, §500.14 monitoring and training, §500.15 encryption, §500.16 incident response and business continuity, §500.17 notices [verify subsection labels].
- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section]. https://ithandbook.ffiec.gov/it-booklets/information-security.aspx [verify URL].
- **NIST SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations** (January 2022) [verify section labels]. The methodology anchor for assessment-object selection: specifications, mechanisms, activities, and individuals as sampling targets. https://csrc.nist.gov/pubs/sp/800/53/a/r5/final .
- **NIST Cybersecurity Framework 2.0** (February 2024) [verify version number and category labels]. Used as a control-categorisation anchor for sampling scope. https://www.nist.gov/cyberframework .

## Cyber-control-area sampling notes

### Access-recertification sampling (Part 500.7-relevant)

- Sampling conventions: population is recertification packets generated in the period (not entitled users). Stratification by privilege tier (standard, privileged, service, break-glass), data sensitivity (PII-handling, restricted, confidential, public), and recertifier role (line manager, application owner, segregation-of-duties reviewer). Privileged-access tolerable rate is typically zero per firm policy. Terminated-employee testing pulls a separate population (HR-IAM feed reconciliation events for terminations during the period) and typically expands from sample to full population because the privileged-not-revoked-after-termination scenario carries asymmetric impact. Judgmental-sample floor often references regulator-handbook appendix conventions (FFIEC IT booklet) and the firm's IT-GCC methodology.

### Vulnerability-management sampling (Part 500.5-relevant)

- Sampling conventions: population is vulnerability tickets opened or closed in the period, depending on the test objective. Stratification by severity (critical, high, medium, low), asset criticality (tier-1 production, tier-2 production, non-production), and asset class (infrastructure, application, endpoint, cloud). MTTR tests sample closed tickets with stratification by severity and the firm's policy clock. Exception-register testing pulls a separate population (tracked exceptions during the period) and tests for exceptions that have aged out without remediation or formal acceptance.

### Pen-test and red-team evidence reliance

- Sampling conventions: external pen-test or red-team report findings are themselves a population. Sampling samples reported findings with stratification by severity and asset coverage; the test reads finding-status against the firm's remediation tracking. The pen-test report is third-party-assurance evidence; the population is the firm's remediation actions, not the testing the third party performed.

### Incident-response sampling (Part 500.16-relevant)

- Sampling conventions: tabletop testing evidence (tabletop-events during the period) and live-incident response evidence (incidents during the period, where applicable) form separate populations. Tabletop-events sampling stratifies by scenario type and participant scope. Live-incident sampling reads against the firm's incident-response plan timeline.

### Logging and monitoring sampling (Part 500.14-relevant)

- Sampling conventions: SIEM-coverage testing population is the asset register, sampled against the SIEM-log-source register; missing log sources are exceptions on the design dimension. Alert-disposition sampling pulls alerts triaged in the period with stratification by category and disposition (true-positive, false-positive, escalated, suppressed). Tolerable rates for missed-true-positive testing on calibrated control sets are typically near-zero.

### Encryption sampling (Part 500.15-relevant)

- Sampling conventions: encryption-at-rest and encryption-in-transit testing samples assets with stratification by asset class and data sensitivity. Key-management testing samples key-rotation events with stratification by key category. Unencrypted exceptions tracked via the exception register are sampled against the senior-officer approval requirement under §500.15(b) [verify].

### Annual certification (Part 500.17(b)-relevant)

- Sampling conventions: testing that supports the senior-officer annual certification samples evidence aligned to the §500.17(b) certification scope; the population definition references the certification-period boundary, and the sample design reads heavy on the criteria that drive certifiable elements.

## NIST SP 800-53A assessment-object sampling

Where the firm has adopted NIST SP 800-53 control families and SP 800-53A assessment methodology, the sampling memo names the assessment objects under sample (specifications, mechanisms, activities, individuals) per control family. Each object class typically carries its own population and stratification:

- Specifications: documented policies and procedures in force during the period.
- Mechanisms: hardware, software, firmware components active in the period.
- Activities: events that occurred during the period (logins, scans, alerts, reviews).
- Individuals: identities or roles in the assessed scope.

## Audience and tone

A sampling memo drafted for the firm's CISO and the cyber-risk committee reads heavier on technical-population definitions and remediation-tracking populations. A memo drafted with an upcoming NYDFS examination in mind reads heavier on Part 500 subsection citations, the §500.17(b) certification posture as context for tolerable-rate setting, and the CISO-attested elements. A memo drafted for internal-audit reliance reads heavier on the SP 800-53A assessment-object selection rationale and the extract-integrity posture for IAM, vulnerability, and SIEM populations.
