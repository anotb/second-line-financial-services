# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay — qa-workpaper

Loaded when `scope.cross_cutting_overlay_set` includes `conduct`, when the QA review covers a workpaper that sampled a consumer-impact population, or when the underlying control test touches a UDAAP-relevant area. Supplements `references/source-anchors.md`.

#### Why conduct QA carries distinct conventions

Conduct workpapers fail QA on conclusion-language hygiene more often than other workpapers. The recurring patterns:

- **Legal-violation framing in conclusions.** A workpaper concluding "the firm engaged in unfair or deceptive practices under Dodd-Frank §1031" or "the bank did not comply with Reg E §1005.11(c)" is a QA finding regardless of the underlying evidence; that conclusion is for legal counsel and the regulator, not the second-line workpaper.
- **Customer-harm framing collapsed into technical control conclusion.** A control may operate effectively at the technical dimension while customer harm is identifiable from the population (e.g., the dispute-resolution control operated within the timing clocks, but the population shows customers were charged fees during the investigation period that the firm should have reversed). The QA reviewer challenges whether customer-harm framing is carried separately from control-effectiveness framing.
- **UDAAP-relevant findings without the customer-impact analysis.** UDAAP exam procedures examine customer impact distinct from technical compliance; a workpaper concluding on a UDAAP-relevant control without the customer-impact analysis is a recurring deficiency.

#### QA conventions for conduct-relevant workpapers

- **Conclusion-language rewrite.** The QA reviewer rewrites legal-violation framing to control-effectiveness framing and elevates the legal question to legal counsel and the head of regulatory affairs as a separate routing, not a conclusion in the workpaper.
- **Customer-harm framing carried separately.** The QA reviewer confirms the workpaper carries a separate customer-harm read where the population shows identifiable harm, distinct from the control-effectiveness conclusion.
- **UDAAP-relevant tests carry the abusive-prong consideration.** Dodd-Frank §1031 includes the "abusive" prong distinct from FTC Act §5 unfair-or-deceptive prongs. The QA reviewer confirms UDAAP-relevant workpapers consider all three prongs (unfair, deceptive, abusive) where applicable, not just the unfair-or-deceptive subset.

#### Conduct-supervisory anchors (load by reference; do not restate)

- **CFPB UDAAP Examination Procedures** (CFPB Supervision and Examination Manual, UDAAP module) [verify section labels]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **Dodd-Frank §1031 (12 USC §5531) and §1036 (12 USC §5536)** — UDAAP authority. https://www.law.cornell.edu/uscode/text/12/5531 .
- **FTC Act §5 (15 USC §45)** — unfair or deceptive practices authority for institutions outside CFPB's direct UDAAP authority. https://www.law.cornell.edu/uscode/text/15/45 .
- **Interagency Policy Statement on Discrimination in Lending** [verify exact title and date for the most recent statement applicable to the firm's regulator constellation]. Used as the framing anchor when the underlying test touches fair-lending posture.

#### Conduct-relevant control-area QA notes

##### Reg E error-resolution conclusion language — QA scope items

- The QA reviewer rewrites "the bank did not comply with Reg E §1005.11(c)" to "the dispute-resolution control did not operate within the §1005.11(c) timing clock for the [population] sample during the period". The legal-violation question routes to legal counsel separately.

##### Complaint-handling testing — QA scope items

- The QA reviewer confirms the workpaper carries a customer-harm read distinct from the control-effectiveness read. Complaint-handling controls may operate at the technical dimension (acknowledgement, routing, response timing) while the population shows resolution outcomes that warrant customer-impact analysis (refunds, account corrections, restitution).

##### Fee-disclosure and fee-application testing — QA scope items

- The QA reviewer confirms fee-disclosure testing carries the regulatory-model redline and the noted deviations as control-effectiveness findings; fee-application testing carries the customer-harm dimension where unauthorised or mistakenly-applied fees are identified in the sample. The customer-harm dimension is distinct from the technical fee-disclosure conclusion.

##### Marketing-practices and disclosure testing — QA scope items

- The QA reviewer confirms marketing-practices testing carries the deceptive-prong consideration distinct from the unfair-prong; reliance on the firm's marketing-review approval evidence does not substitute for sampling marketing materials against the disclosure rules.

##### Fair-lending and disparate-impact testing — QA scope items

- The QA reviewer confirms fair-lending testing distinguishes statistical disparities (which warrant further analysis) from disparate-treatment findings (which require evidence of intent or a substantially-similar-applicant comparison). The QA reviewer challenges any conclusion drifting toward "the firm engaged in disparate-treatment discrimination" without the underlying evidence; statistical-disparity findings route to the head of fair lending and legal counsel separately.

#### Audience and tone

A QA review note drafted with an upcoming CFPB or DOJ exam in mind reads heaviest on conclusion-language hygiene, the customer-harm framing, and the UDAAP all-three-prongs consideration. A QA note for in-cycle testing-program closure reads operationally with the same dimensions but lighter on the examiner-prep posture. The conclusion-language rewrite is the most-recurring intervention; firms with strong conduct posture build the rewrite into the testing-template default rather than relying on the QA reviewer to catch it every cycle.

## cyber

### Cyber cross-cutting overlay — qa-workpaper

Loaded when `scope.cross_cutting_overlay_set` includes `cyber`, when the QA review covers a workpaper addressing IAM controls, data-protection controls, vulnerability-management controls, or NYDFS Part 500-mandated areas, or when the firm is a Covered Entity under 23 NYCRR Part 500. Supplements `references/source-anchors.md`.

#### Why cyber QA carries distinct conventions

Cyber control workpapers fail QA on evidence-reliability more often than financial-control workpapers. The recurring patterns:

- **Vendor-supplied scan results cited as evidence without firm-side reliance assessment.** A workpaper that cites a vendor's SaaS-platform scan output as evidence of vulnerability remediation without documenting the firm's reliance test (scan scope, scan recency, vendor's CUEC posture, the firm's independent verification of remediation on critical findings) is an evidence-reliability deficiency.
- **Screenshot-only access reviews.** A workpaper that documents access-recertification with screenshots of the IAM tool's recertification screen, without a system-of-record entitlement extract reperformed against the screenshot, is an evidence-reliability deficiency. Screenshots are ephemeral and operator-controlled; they do not substitute for an extract.
- **Production-versus-test environment evidence reliance.** Cyber control testing where the preparer cited the test environment as evidence of production posture is a structural finding. The QA reviewer challenges environment-provenance on every cyber evidence item.
- **Privileged-access tolerable-rate floor of zero.** Most firm policies set zero tolerance for privileged-access exceptions; the QA reviewer challenges severity ratings that do not reflect the floor.

#### QA conventions for cyber control workpapers

- **Sample-design QA.** The QA reviewer confirms sample stratification by privilege tier (standard / privileged / service / break-glass), data sensitivity, and recertifier role for access-recertification workpapers; by severity and asset criticality for vulnerability-management workpapers; and by alert category for SIEM alert-disposition workpapers.
- **System-of-record evidence integrity QA.** The QA reviewer confirms IAM entitlement extracts, vulnerability-scan output, and SIEM logs name the extract date, the run-by role, and the completeness check against an independent system count.
- **Reperformance QA.** Where the test plan called for reperformance, the QA reviewer reperforms a small subsample of the entitlement query, the scan-finding validation, or the alert disposition; QA reperform is the most credible QA dimension for cyber workpapers.

#### Cyber-supervisory anchors (load by reference; do not restate)

- **NYDFS 23 NYCRR Part 500.7 — Access Privileges and Management** [verify subsection labels against the latest amendment]. https://www.dfs.ny.gov/industry_guidance/cybersecurity .
- **NYDFS 23 NYCRR Part 500** generally — §500.3 cybersecurity policy, §500.4 CISO, §500.5 vulnerability management, §500.7 access privileges, §500.9 risk assessment, §500.11 third-party service-provider security, §500.13 asset management and data retention, §500.14 monitoring and training, §500.15 encryption, §500.16 incident response and business continuity, §500.17 notices, §500.19 exemptions [verify subsection labels].
- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section]. https://ithandbook.ffiec.gov/it-booklets/information-security.aspx [verify URL].
- **NIST SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations** (January 2022) [verify section labels for assessment objectives, methods, and assessment objects]. https://csrc.nist.gov/pubs/sp/800/53/a/r5/final .
- **NIST Cybersecurity Framework 2.0** (February 2024) [verify version number and category labels]. Used as a control-categorisation anchor when the firm has mapped testing scope to CSF categories. https://www.nist.gov/cyberframework .

#### Cyber-control-area QA notes

##### Access-recertification testing — QA scope items

- QA conventions: the QA reviewer reperforms entitlement queries for a small subsample of the privileged tier; confirms HR-IAM feed reconciliation evidence for terminated employees is documented (terminations typically expanded from sample to full population); confirms the attestation form supports per-entitlement attestation versus blanket approval (a blanket-approval form is a design-effectiveness QA finding even when operating effectiveness is high). Privileged-access exceptions trigger issue elevation regardless of overall sample deviation rate.

##### Vulnerability-management testing — QA scope items

- QA conventions: the QA reviewer confirms scan-frequency cadence reperformance, MTTR-by-severity calculation against the firm's policy clocks, and exception-register testing as a separate procedure (tracked exceptions versus exceptions that have aged out without remediation or formal acceptance). Reliance on vendor scan output without firm reperformance on critical findings is the recurring deficiency.

##### Pen-test and red-team evidence reliance — QA scope items

- QA conventions: the QA reviewer confirms reliance on a pen-test or red-team report carries the testing scope, testing date, finding-status as of report date, and the firm's remediation tracking. Reliance on a pen-test summary without the full report is partial evidence; the QA reviewer flags this as a limitation, not as substitute evidence.

##### Incident-response testing — QA scope items

- QA conventions: the QA reviewer confirms tabletop-testing evidence (date, scenario, participants by role, observations, action-item closure tracking) is sampled, and that the workpaper distinguishes design (the IR plan) from operating (the tabletop output and closure of action items).

##### SIEM logging and alert-disposition testing — QA scope items

- QA conventions: the QA reviewer confirms SIEM-coverage testing reads the asset register against the SIEM-log-source register by sample (missing log sources are design-dimension exceptions); confirms alert-disposition testing reads the alert sample by category with the disposition rationale and the closure timeline against the firm's policy clock.

##### Encryption testing — QA scope items

- QA conventions: the QA reviewer confirms encryption-at-rest and encryption-in-transit testing reads the configuration against the firm's standard by asset sample, and that key-management testing reads the key-rotation evidence and customer-managed-key posture (where applicable). Unencrypted exceptions tracked via the exception register are read against the senior-officer approval requirement under §500.15(b) [verify].

##### Annual certification scope — QA scope items

- QA conventions: where the workpaper supports the §500.17(b) annual certification, the QA reviewer reads heavier on certification-scope items, evidence-reliability dimensions, and reviewer-separation evidence. Findings during the certification period that touch certifiable elements are flagged in the QA review note as items the senior-officer certification preparer must consider; the workpaper does not certify, and neither does the QA review.

#### Cross-link to NIST SP 800-53A documentation conventions

Where the firm has adopted NIST SP 800-53 control families and SP 800-53A assessment methodology, the QA reviewer confirms the workpaper restates the assessment objective, the assessment method (examine, interview, test) per procedure, and the assessment objects (specifications, mechanisms, activities, individuals) sampled. The QA review note's deficiency findings map to the SP 800-53 control number for traceability into the firm's POAM (Plan of Action and Milestones) where one is maintained.

#### Audience and tone

A QA review note drafted for the firm's CISO or cyber-risk committee reads heavier on the technical evidence-reliability dimensions and the reperformance posture. A QA note drafted with an upcoming NYDFS examination in mind reads heavier on the Part 500 subsection citation, the §500.17(b) certification posture, and the CISO-attested elements. A QA note for internal-audit reliance reads heavier on the system-of-record extract-integrity posture and the reviewer-separation evidence.
