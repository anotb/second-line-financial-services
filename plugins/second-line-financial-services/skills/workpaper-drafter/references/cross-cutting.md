# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay — workpaper-drafter

Loaded when `scope.cross_cutting_overlay_set` includes `conduct`, when the test addresses consumer-facing controls (UDAAP, fair-lending, sales-practices, complaint-handling), or when customer-harm framing matters separately from the technical control conclusion. Supplements `references/source-anchors.md`.

#### Workpaper conventions for conduct-relevant testing

Conduct-relevant testing workpapers carry a consumer-harm read distinct from the substantive control read. Two conventions matter:

- **Customer-harm framing is a separate conclusion lens.** A control can be operating effectively as designed and still produce customer harm if the design embeds an unfair, deceptive, or abusive feature. The workpaper carries the substantive control conclusion (effective / partially effective / not effective) and a separate consumer-harm read where applicable. The conduct overlay does not collapse the two reads.
- **Disclosure-content testing requires the production version.** Disclosure testing reads the disseminated disclosure (customer-facing) rather than the master template. Test-environment disclosures and pre-production disclosures are not the population; the workpaper population is the disclosure as the customer received it, by sample of customer interactions.

#### Conduct-supervisory anchors (load by reference; do not restate)

- **CFPB UDAAP Examination Procedures** (CFPB Supervision and Examination Manual, UDAAP module) [verify section labels]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **Dodd-Frank §1031 (12 USC §5531) and §1036 (12 USC §5536)** — UDAAP authority. The "abusive" prong is statutorily distinct from FTC Act §5 unfair or deceptive prongs; testing workpapers covering abusive-act analysis cite §1031(d) directly. https://www.law.cornell.edu/uscode/text/12/5531 .
- **FTC Act §5 (15 USC §45)** — unfair or deceptive acts or practices. Applies to non-bank firms outside CFPB authority and to bank holding companies via FRB authority. https://www.law.cornell.edu/uscode/text/15/45 .
- **CFPB compliance bulletins on consumer-harm framing** [verify specific bulletin numbers and dates]. https://www.consumerfinance.gov/compliance/supervisory-guidance/ .
- **Reg B / ECOA — 12 CFR Part 1002**, especially §1002.4 (general rule against discrimination) and §1002.6 (rules concerning evaluation of applications) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- **Fair Housing Act (42 USC §3601 et seq.)** for housing-related credit testing. https://www.law.cornell.edu/uscode/text/42/3601 .
- **Servicemembers Civil Relief Act (50 USC §3901 et seq.)** for SCRA-relevant testing. https://www.law.cornell.edu/uscode/text/50/3901 .
- **NAIC Unfair Trade Practices Act (Model #880) and Unfair Claims Settlement Practices Act (Model #900)** [verify model numbers and state-by-state adoption]. State-adopted versions cite the state statute primarily.
- **FINRA Rule 2010 (Standards of Commercial Honor) and Rule 2111 (Suitability)** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/2010 .

#### Conduct-control-area workpaper notes

##### UDAAP testing

- Workpaper conventions: UDAAP testing reads consumer-facing materials (disclosures, marketing, fee schedules, dispute responses, account-servicing communications), customer-experience evidence (call recordings, chat transcripts, app screen flows), and complaint-pattern evidence (complaint-management system extracts, theme analysis). The substantive control conclusion is on whether the firm's UDAAP control framework is operating; the consumer-harm read is whether observed practices show a substantive UDAAP risk regardless of control framework effectiveness.
- The "abusive" prong testing under §1031(d) reads against the four statutory tests (material interference with ability to understand a term or condition; taking unreasonable advantage of lack of understanding; taking unreasonable advantage of inability to protect interests; taking unreasonable advantage of reasonable reliance on a covered person to act in the consumer's interest) [verify exact statutory language]. The workpaper does not pre-judge the legal test; it surfaces evidence relevant to the test for legal review.

##### Fair-lending testing (ECOA, FHA)

- Workpaper conventions: fair-lending testing covers underwriting (disparate-treatment file review, comparative-file analysis), pricing (overage and underage analysis, spread distribution by prohibited basis), redlining (geography distribution), marketing (channel and language coverage), and steering (product-mix distribution). Disparate-impact analysis is statistical; the workpaper carries the model used, the variables included and excluded, and the limitations.
- The workpaper restates the prohibited bases (race, colour, religion, national origin, sex, marital status, age, public-assistance income, exercise of a right under the CCPA, ECOA-protected activity) [verify Reg B §1002.2(z)] and the protected classes under FHA where applicable.

##### Sales-practices testing (broker-dealer suitability and recommendation)

- Workpaper conventions: suitability testing under FINRA Rule 2111 reads the recommendation, the customer profile, and the rationale by sample; Reg BI testing for retail customers reads the Care Obligation, Conflict of Interest Obligation, and Disclosure Obligation evidence. Customer-impact framing covers commission-overweight recommendations, complex-product placements with retail customers, and compensation-driven product-mix distortion.

##### Complaint-handling testing

- Workpaper conventions: complaint-handling testing reads complaint intake, classification, investigation, response, root-cause analysis, and trend reporting. Reg E §1005.11 error-resolution overlaps with complaint testing where the complaint is also a §1005.11 dispute; the workpaper tracks both regulatory clocks. Complaint-pattern review feeds the consumer-harm read independent of control-framework effectiveness.

##### Insurance unfair-trade-practices and unfair-claims-settlement testing

- Workpaper conventions: state-adopted UTPA and UCSPA testing reads the state-specific definitions of unfair practices; multi-state tests carry state-by-state variance. Claims-handling timing testing reads the state-statutory clocks (acknowledgement, investigation, decision, payment) by sample.

#### Customer-harm framing in the conclusion

The workpaper conclusion section, when the conduct overlay is loaded, can carry an additional read: "consumer-harm signal observed: [yes / no / inconclusive]" with rationale. This read is not a legal conclusion (legal conclusions sit with counsel); it is the testing-program's surfacing of evidence relevant to the legal-conduct dimension. The reviewer questions section flags any consumer-harm signal for legal review distinct from control-framework remediation.

#### Distinctness from technical control conclusion

A workpaper covering a fee-disclosure control may conclude that the disclosure control is operating effectively (the disclosure is delivered as designed) and separately surface a consumer-harm signal that the disclosure as designed is unclear, misleading, or abusive. The two conclusions sit side by side; the workpaper does not collapse them. Issue-writeup downstream may produce two issues (a control-effectiveness finding and a consumer-harm finding) from the same workpaper.

#### Audience and tone

A workpaper drafted for the firm's CCO and the conduct-risk committee reads heavier on the consumer-harm read and the complaint-pattern evidence. A workpaper drafted with an upcoming CFPB exam in mind reads heavier on UDAAP module references, complaint-handling evidence, and customer-experience evidence (call recordings, chat transcripts). A workpaper drafted for fund-board reporting on adviser conduct reads heavier on suitability and Reg BI evidence with the customer-base distribution as context.

## cyber

### Cyber cross-cutting overlay — workpaper-drafter

Loaded when `scope.cross_cutting_overlay_set` includes `cyber`, when the test addresses IAM controls, data-protection controls, or NYDFS Part 500-mandated areas, or when the firm is a Covered Entity under 23 NYCRR Part 500. Supplements `references/source-anchors.md`.

#### Workpaper conventions for cyber control testing

Cyber control testing workpapers carry methodology distinct from financial-control testing:

- **Sample design follows population behaviour, not transaction count.** Access-recertification populations stratify by privilege tier (standard / privileged / service / break-glass), data sensitivity, and recertifier role. Vulnerability-management populations stratify by severity and asset criticality. The sample-design rationale in the workpaper restates the stratification decision.
- **System-of-record evidence carries an extract-integrity check.** IAM entitlement extracts, vulnerability-scan output, and SIEM logs run at different times produce different populations; the workpaper names the extract date, the run-by role, and what the preparer did to confirm completeness against an independent system count.
- **Reperformance is the standard procedure for technical controls.** Where the test plan calls for reperformance (re-running an entitlement query, re-validating a scan finding, re-reading an alert), the workpaper notes preparer access to the production environment versus reliance on a system-generated extract; production-access evidence is stronger but rarely available to second-line testers.

#### Cyber-supervisory anchors (load by reference; do not restate)

- **NYDFS 23 NYCRR Part 500.7 — Access Privileges and Management** [verify subsection labels against the latest amendment]. Periodic review of access privileges; risk-based authentication exceptions require senior-officer certification. https://www.dfs.ny.gov/industry_guidance/cybersecurity .
- **NYDFS 23 NYCRR Part 500** generally — §500.3 cybersecurity policy, §500.4 CISO, §500.5 vulnerability management, §500.7 access privileges, §500.9 risk assessment, §500.11 third-party service-provider security, §500.13 asset management and data retention, §500.14 monitoring and training, §500.15 encryption, §500.16 incident response and business continuity, §500.17 notices, §500.19 exemptions [verify subsection labels].
- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section]. https://ithandbook.ffiec.gov/it-booklets/information-security.aspx [verify URL].
- **NIST SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations** (January 2022) [verify section labels for assessment objectives, methods, and assessment objects]. https://csrc.nist.gov/pubs/sp/800/53/a/r5/final .
- **NIST Cybersecurity Framework 2.0** (February 2024) [verify version number and category labels]. Used as a control-categorisation anchor for testing scope set against firm-mapped CSF categories. https://www.nist.gov/cyberframework .
- **CISA Zero Trust Maturity Model 2.0** (April 2023) [verify version and pillar labels]. Used where the firm's IAM testing scope includes zero-trust posture. https://www.cisa.gov/zero-trust-maturity-model .

#### Cyber-control-area workpaper notes

##### Access-recertification testing (Part 500.7-relevant)

- Workpaper conventions: sample design stratified by privilege tier; reperformance against IAM extract; HR-IAM feed reconciliation for terminated employees with separate sample (terminations typically expand from sample to full population because the privileged-not-revoked-after-termination scenario carries asymmetric impact); attestation form review reads whether the form supports per-entitlement attestation versus blanket approval (a blanket-approval form is a design exception even when operating effectiveness is high).
- Privileged-access testing has a tolerable rate of zero in most firm policies; the workpaper aggregation makes that explicit and any privileged exception triggers the issue elevation regardless of overall sample deviation rate.

##### Vulnerability-management testing (Part 500.5-relevant)

- Workpaper conventions: sample design stratified by severity and asset criticality; the procedure tests cadence (scan frequency), MTTR by severity, and exception-register integrity (tracked exceptions versus exceptions that have aged out without remediation or formal acceptance). Exception-register testing is its own sub-procedure; the workpaper carries it as a separate procedure ID.

##### Pen-test and red-team evidence reliance

- Workpaper conventions: external pen-test or red-team reports are third-party-assurance evidence; the reliance test note covers the testing scope, the testing date, the finding-status as of report date, and the firm's remediation tracking. Reliance on a pen-test summary without the full report is partial evidence; the workpaper notes the limitation.

##### Incident-response testing (Part 500.16-relevant)

- Workpaper conventions: tabletop testing evidence (tabletop date, scenario, participants by role, observations, action items, action-item closure tracking) is read by sample of past tabletops; the workpaper distinguishes design (the IR plan) from operating (the tabletop output and closure of action items).

##### Logging and monitoring testing (Part 500.14-relevant)

- Workpaper conventions: SIEM-coverage testing reads the asset register against the SIEM-log-source register by sample; missing log sources are exceptions on the design dimension. Alert-disposition testing reads alert sample by category with the disposition rationale and the closure timeline against the firm's policy clock.

##### Encryption testing (Part 500.15-relevant)

- Workpaper conventions: encryption-at-rest and encryption-in-transit testing reads the configuration against the firm's standard by asset sample; key-management testing reads the key-rotation evidence and the customer-managed-key posture (where applicable). Unencrypted exceptions tracked via the exception register are read against the senior-officer approval requirement under §500.15(b) [verify].

##### Annual certification (Part 500.17(b)-relevant)

- Workpaper conventions: testing that supports the annual certification reads the certification scope against the §500.17(b) requirements; findings during the certification period that touch certifiable elements (control failures, material gaps) are flagged in the workpaper limitations as items the senior-officer certification preparer must consider, not items the workpaper concludes on. The workpaper does not certify; the senior officer certifies.

#### Cross-link to NIST SP 800-53A documentation conventions

Where the firm has adopted NIST SP 800-53 control families and SP 800-53A assessment methodology, the workpaper restates the assessment objective, the assessment method (examine, interview, test) per procedure, and the assessment objects (specifications, mechanisms, activities, individuals) sampled. The workpaper aggregation maps observed exceptions to the SP 800-53 control number for traceability into the firm's POAM (Plan of Action and Milestones) where one is maintained.

#### Audience and tone

A workpaper drafted for the firm's CISO and the cyber-risk committee reads heavier on technical detail and remediation tracking. A workpaper drafted with an upcoming NYDFS examination in mind reads heavier on Part 500 subsection citation, the §500.17(b) certification posture, and the CISO-attested elements. A workpaper drafted for internal-audit reliance reads heavier on the evidence reliance and the system-of-record extract-integrity posture.
