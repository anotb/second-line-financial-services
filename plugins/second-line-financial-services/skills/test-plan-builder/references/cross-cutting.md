# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay — test-plan-builder

Loaded when `scope.cross_cutting_overlay_set` includes `conduct`, when the test addresses consumer-facing controls (UDAAP, fair-lending, sales-practices, complaint-handling), or when customer-harm framing matters separately from the technical control conclusion. Supplements `references/source-anchors.md`.

#### Test-plan conventions for conduct-relevant testing

Conduct-relevant test plans carry a consumer-harm read distinct from the substantive control read. Two conventions matter:

- **Customer-harm framing is a separate conclusion lens that the plan sets up at planning time.** A control can be operating effectively as designed and still produce customer harm if the design embeds an unfair, deceptive, or abusive feature. The plan names the substantive control conclusion (effective / partially effective / not effective) and a separate consumer-harm read where applicable. The conduct overlay does not collapse the two reads.
- **Disclosure-content testing requires the production version.** Disclosure test plans target the disseminated disclosure (customer-facing) rather than the master template. Test-environment disclosures and pre-production disclosures are not the population; the plan defines population as the disclosure as the customer received it, by sample of customer interactions, and names the production-extract source.

#### Conduct-supervisory anchors (load by reference; do not restate)

- **CFPB UDAAP Examination Procedures** (CFPB Supervision and Examination Manual, UDAAP module) [verify section labels]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **Dodd-Frank §1031 (12 USC §5531) and §1036 (12 USC §5536)** — UDAAP authority. The "abusive" prong is statutorily distinct from FTC Act §5 unfair or deceptive prongs; test plans covering abusive-act analysis cite §1031(d) directly. https://www.law.cornell.edu/uscode/text/12/5531 .
- **FTC Act §5 (15 USC §45)** — unfair or deceptive acts or practices. Applies to non-bank firms outside CFPB authority and to bank holding companies via FRB authority. https://www.law.cornell.edu/uscode/text/15/45 .
- **CFPB compliance bulletins on consumer-harm framing** [verify specific bulletin numbers and dates]. https://www.consumerfinance.gov/compliance/supervisory-guidance/ .
- **Reg B / ECOA — 12 CFR Part 1002**, especially §1002.4 (general rule against discrimination) and §1002.6 (rules concerning evaluation of applications) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- **Fair Housing Act (42 USC §3601 et seq.)** for housing-related credit testing. https://www.law.cornell.edu/uscode/text/42/3601 .
- **Servicemembers Civil Relief Act (50 USC §3901 et seq.)** for SCRA-relevant testing. https://www.law.cornell.edu/uscode/text/50/3901 .
- **NAIC Unfair Trade Practices Act (Model #880) and Unfair Claims Settlement Practices Act (Model #900)** [verify model numbers and state-by-state adoption]. State-adopted versions cite the state statute primarily.
- **FINRA Rule 2010 (Standards of Commercial Honor) and Rule 2111 (Suitability)** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/2010 .
- **SR 11-7 — Supervisory Guidance on Model Risk Management** (Federal Reserve / OCC Bulletin 2011-12, April 4, 2011) [verify section labels]. Referenced when the test plan addresses model-driven consumer-impact controls (e.g., AI-driven underwriting decisioning). https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm .

#### Conduct-control-area test-plan notes

##### UDAAP testing

- Test-plan conventions: criteria section cites the relevant CFPB bulletin or the Dodd-Frank §1031 / §1036 statutory text; population includes consumer-facing materials (disclosures, marketing, fee schedules, dispute responses, account-servicing communications), customer-experience evidence (call recordings, chat transcripts, app screen flows), and complaint-pattern evidence. The substantive control conclusion is on whether the firm's UDAAP control framework is operating; the consumer-harm read is whether observed practices show a substantive UDAAP risk regardless of control framework effectiveness.
- The "abusive" prong testing under §1031(d) reads against the four statutory tests (material interference with ability to understand a term or condition; taking unreasonable advantage of lack of understanding; taking unreasonable advantage of inability to protect interests; taking unreasonable advantage of reasonable reliance on a covered person to act in the consumer's interest) [verify exact statutory language]. The plan does not pre-judge the legal test; it surfaces evidence relevant to the test for legal review.

##### Fair-lending testing (ECOA, FHA)

- Test-plan conventions: fair-lending test plans cover underwriting (disparate-treatment file review, comparative-file analysis), pricing (overage and underage analysis, spread distribution by prohibited basis), redlining (geography distribution), marketing (channel and language coverage), and steering (product-mix distribution). Disparate-impact analysis is statistical; the plan carries the model design, the variables included and excluded, and the limitations.
- The plan restates the prohibited bases (race, colour, religion, national origin, sex, marital status, age, public-assistance income, exercise of a right under the CCPA, ECOA-protected activity) [verify Reg B §1002.2(z)] and the protected classes under FHA where applicable.

##### Sales-practices testing (broker-dealer suitability and recommendation)

- Test-plan conventions: suitability test plans under FINRA Rule 2111 cover the recommendation, the customer profile, and the rationale by sample; Reg BI test plans for retail customers cover the Care Obligation, Conflict of Interest Obligation, and Disclosure Obligation evidence. Customer-impact framing covers commission-overweight recommendations, complex-product placements with retail customers, and compensation-driven product-mix distortion.

##### Complaint-handling testing

- Test-plan conventions: complaint-handling test plans cover complaint intake, classification, investigation, response, root-cause analysis, and trend reporting. Reg E §1005.11 error-resolution overlaps with complaint testing where the complaint is also a §1005.11 dispute; the plan tracks both regulatory clocks. Complaint-pattern review feeds the consumer-harm read independent of control-framework effectiveness.

##### Insurance unfair-trade-practices and unfair-claims-settlement testing

- Test-plan conventions: state-adopted UTPA and UCSPA test plans cover the state-specific definitions of unfair practices; multi-state plans carry state-by-state variance. Claims-handling timing test plans cover the state-statutory clocks (acknowledgement, investigation, decision, payment) by sample.

#### Customer-harm framing in the plan's pass and fail criteria

The plan's pass and fail criteria, when the conduct overlay is loaded, can carry an additional read: the substantive control criterion plus a consumer-harm signal criterion ("consumer-harm signal observed: yes / no / inconclusive" with rationale). This signal read is not a legal conclusion (legal conclusions sit with counsel); it is the testing-program's surfacing of evidence relevant to the legal-conduct dimension. The plan's reviewer-questions section flags any anticipated consumer-harm signal for legal review distinct from control-framework remediation.

#### Distinctness from technical control conclusion

A test plan covering a fee-disclosure control may set up a substantive procedure on whether the disclosure is delivered as designed (a control-effectiveness read) and a separate procedure on whether the disclosure as designed is unclear, misleading, or abusive (a consumer-harm read). The two reads sit side by side; the plan does not collapse them. Issue-writeup downstream may produce two issues (a control-effectiveness finding and a consumer-harm finding) from the same workpaper.

#### Audience and tone

A test plan drafted for the firm's CCO and the conduct-risk committee reads heavier on the consumer-harm read, complaint-pattern evidence, and the customer-experience evidence the cycle will inspect. A plan drafted with an upcoming CFPB exam in mind reads heavier on UDAAP module references, complaint-handling evidence, and customer-experience evidence (call recordings, chat transcripts). A plan drafted for fund-board reporting on adviser conduct reads heavier on suitability and Reg BI evidence with the customer-base distribution as context.

## cyber

### Cyber cross-cutting overlay — test-plan-builder

Loaded when `scope.cross_cutting_overlay_set` includes `cyber`, when the test addresses IAM controls, data-protection controls, or NYDFS Part 500-mandated areas, or when the firm is a Covered Entity under 23 NYCRR Part 500. Supplements `references/source-anchors.md`.

#### Test-plan conventions for cyber control testing

Cyber control test plans carry methodology distinct from financial-control test planning:

- **Sample design follows population behaviour, not transaction count.** Access-recertification populations stratify by privilege tier (standard / privileged / service / break-glass), data sensitivity, and recertifier role. Vulnerability-management populations stratify by severity and asset criticality. The plan's population-and-sampling-reference section restates the stratification decision and the rationale.
- **Tolerable rate is severity-driven for zero-tolerable populations.** Privileged-access populations, sanctions-screening populations, and customer-funds-segregation populations typically carry a zero-tolerable rate. The plan names the zero-tolerable subset and the severity-driven aggregation read so the workpaper later does not collapse it into the overall rate.
- **Reperformance is the standard procedure for technical controls.** Where the plan calls for reperformance (re-running an entitlement query, re-validating a scan finding, re-reading an alert), the plan names the production-access prerequisite and the alternative procedure when production access is not available to the second-line tester (system-generated extract with extract-integrity check).
- **Extract-integrity check is a planned procedure, not a fieldwork afterthought.** IAM entitlement extracts, vulnerability-scan output, and SIEM logs run at different times produce different populations; the plan names the extract date, the extract-source role, and the independent count the workpaper will reconcile against.

#### Cyber-supervisory anchors (load by reference; do not restate)

- **NYDFS 23 NYCRR Part 500.7 — Access Privileges and Management** [verify subsection labels against the latest amendment]. Periodic review of access privileges; risk-based authentication exceptions require senior-officer certification. https://www.dfs.ny.gov/industry_guidance/cybersecurity .
- **NYDFS 23 NYCRR Part 500** generally — §500.3 cybersecurity policy, §500.4 CISO, §500.5 vulnerability management, §500.7 access privileges, §500.9 risk assessment, §500.11 third-party service-provider security, §500.13 asset management and data retention, §500.14 monitoring and training, §500.15 encryption, §500.16 incident response and business continuity, §500.17 notices, §500.19 exemptions [verify subsection labels].
- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section]. https://ithandbook.ffiec.gov/it-booklets/information-security.aspx [verify URL].
- **NIST SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations** (January 2022) [verify section labels for assessment objectives, methods, and assessment objects]. https://csrc.nist.gov/pubs/sp/800/53/a/r5/final .
- **NIST Cybersecurity Framework 2.0** (February 2024) [verify version number and category labels]. Used as a control-categorisation anchor when the firm has mapped controls to CSF categories. https://www.nist.gov/cyberframework .
- **CISA Zero Trust Maturity Model 2.0** (April 2023) [verify version and pillar labels]. Used where the IAM test plan scope includes zero-trust posture. https://www.cisa.gov/zero-trust-maturity-model .
- **SEC Reg S-K Item 106 — Cybersecurity Risk Management, Strategy, and Governance disclosure** [verify Item number and current effective date]. Cyber-disclosure-process testing scope where the firm is a registrant. https://www.ecfr.gov/current/title-17/chapter-II/part-229/section-229.106 [verify URL].

#### Cyber-control-area test-plan notes

##### Access-recertification testing (Part 500.7-relevant)

- Test-plan conventions: criteria section names §500.7 [verify subsection] (least privilege, periodic review) and the firm's IAM control standard; population is the recertification packets due in the period; sample stratified by privilege tier (standard / privileged / service); design procedures cover the attestation form structure (does the form support per-entitlement attestation or only per-system blanket approval), the campaign workflow, and the HR-IAM integration architecture; operating procedures cover per-packet attestation reperformance, IAM-system reperformance for revocations, and HR-IAM feed reconciliation for terminated employees.
- Privileged-access subset: zero tolerable rate; aggregation is severity-driven, not rate-driven; the plan names the privileged sub-sample size and the rationale for any expansion to full enumeration.

##### Vulnerability-management testing (Part 500.5-relevant)

- Test-plan conventions: criteria section names §500.5 [verify subsection] and the firm's vulnerability-management standard; population is the vulnerabilities identified in the period; sample stratified by severity and asset criticality; design procedures cover the scan-tool configuration and coverage; operating procedures cover scan cadence, MTTR by severity, and the exception-register integrity (tracked exceptions versus exceptions that have aged out without remediation or formal acceptance).

##### Pen-test and red-team evidence reliance

- Test-plan conventions: external pen-test or red-team reports are third-party-assurance evidence; the plan's reliance posture covers the testing scope, the testing date, the finding-status as of report date, and the firm's remediation tracking. Reliance on a pen-test summary without the full report is partial evidence; the plan's limitations section names the constraint.

##### Incident-response testing (Part 500.16-relevant)

- Test-plan conventions: criteria section names §500.16 [verify subsection] and the firm's IR plan; population is the incidents and tabletop exercises in the period; design procedures cover the IR plan adequacy review; operating procedures cover tabletop evidence (tabletop date, scenario, participants by role, observations, action items, action-item closure) by sample.

##### Logging and monitoring testing (Part 500.14-relevant)

- Test-plan conventions: SIEM-coverage test plans read the asset register against the SIEM-log-source register by sample (missing log sources are exceptions on the design dimension); alert-disposition test plans cover alert sample by category with the disposition rationale and the closure timeline against the firm's policy clock.

##### Encryption testing (Part 500.15-relevant)

- Test-plan conventions: encryption-at-rest and encryption-in-transit test plans read the configuration against the firm's standard by asset sample; key-management test plans read key-rotation evidence and customer-managed-key posture (where applicable). Unencrypted exceptions tracked via the exception register are read against the senior-officer approval requirement under §500.15(b) [verify].

##### Annual certification (Part 500.17(b)-relevant)

- Test-plan conventions: testing that supports the annual certification reads against the §500.17(b) requirements; findings during the certification period that touch certifiable elements (control failures, material gaps) are flagged in the plan limitations as items the senior-officer certification preparer must consider, not items the plan concludes on. The plan does not certify; the senior officer certifies.

#### Cross-link to NIST SP 800-53A documentation conventions

Where the firm has adopted NIST SP 800-53 control families and SP 800-53A assessment methodology, the plan restates the assessment objective, the assessment method (examine, interview, test) per procedure, and the assessment objects (specifications, mechanisms, activities, individuals) sampled. The plan names the SP 800-53 control number per criterion for traceability into the firm's POAM (Plan of Action and Milestones) where one is maintained.

#### Audience and tone

A test plan drafted for the firm's CISO and the cyber-risk committee reads heavier on technical detail, expected procedure depth, and the populations the cycle will fully enumerate versus sample. A plan drafted with an upcoming NYDFS examination in mind reads heavier on Part 500 subsection citation, the §500.17(b) certification posture, and the CISO-attested elements the cycle is designed to support. A plan drafted for internal-audit reliance reads heavier on the evidence reliance and the system-of-record extract-integrity posture set out as planned procedures.
