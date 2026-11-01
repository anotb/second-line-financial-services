# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay — control-sampling

Loaded when `scope.cross_cutting_overlay_set` includes `conduct`, when the test addresses consumer-facing controls (UDAAP, fair-lending, sales-practices, complaint-handling), or when stratification by customer segment matters separately from the technical control conclusion. Supplements `references/source-anchors.md`.

#### Population definition conventions for conduct-relevant sampling

Conduct-relevant sampling carries population conventions distinct from substantive-control sampling:

- **Populations are customer interactions, not transactions.** Disclosure-delivery events to customers in the period; complaints received in the period; customer-service calls handled in the period; sales recommendations made in the period; account-servicing communications sent in the period. The customer-experience artifact is the population item.
- **The disclosure population is the disseminated disclosure, not the master template.** Test-environment disclosures and pre-production disclosures are not the population; the population is the disclosure as the customer received it.
- **Complaint populations stratify by intake channel because routing differences embed risk.** DOI-routed, regulator-routed (CFPB consumer complaint database), social-media-escalation, branch-walk-in, call-centre, and direct-to-online routes carry different risk profiles and resolution clocks.
- **Call recordings and chat transcripts are populations in their own right.** Sampling pulls customer interactions with stratification by call type and disposition. Access controls on the recording library may constrain the sample (the memo names the access-control posture and any sample-size constraint that flows from it).

#### Conduct-supervisory anchors (load by reference; do not restate)

- **CFPB UDAAP Examination Procedures** (CFPB Supervision and Examination Manual, UDAAP module) [verify section labels]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **Dodd-Frank §1031 (12 USC §5531) and §1036 (12 USC §5536)** — UDAAP authority. The "abusive" prong is statutorily distinct from FTC Act §5 unfair or deceptive prongs. https://www.law.cornell.edu/uscode/text/12/5531 .
- **FTC Act §5 (15 USC §45)** — unfair or deceptive acts or practices. https://www.law.cornell.edu/uscode/text/15/45 .
- **Reg B / ECOA — 12 CFR Part 1002**, especially §1002.4 and §1002.6 [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- **Fair Housing Act (42 USC §3601 et seq.)** for housing-related credit testing. https://www.law.cornell.edu/uscode/text/42/3601 .
- **Servicemembers Civil Relief Act (50 USC §3901 et seq.)** for SCRA-relevant testing. https://www.law.cornell.edu/uscode/text/50/3901 .
- **NAIC Unfair Trade Practices Act (Model #880) and Unfair Claims Settlement Practices Act (Model #900)** [verify model numbers and state-by-state adoption]. State-adopted versions cite the state statute primarily.
- **FINRA Rule 2010 (Standards of Commercial Honor) and Rule 2111 (Suitability)** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/2010 .

#### Conduct-control-area sampling notes

##### UDAAP sampling

- Sampling conventions: UDAAP testing pulls multiple populations because the UDAAP frame covers consumer-facing materials, customer interactions, and complaint patterns. Disclosure-delivery events sample with stratification by disclosure type, channel, and product. Customer-experience populations (call recordings, chat transcripts, app screen flows) sample with stratification by interaction type. Complaint-pattern populations sample with theme and product stratification. Tolerable rates for UDAAP-relevant populations carry the customer-impact frame; the memo names the customer-impact rationale alongside the rate.

##### Fair-lending sampling (ECOA, FHA)

- Sampling conventions: fair-lending sampling carries multiple populations across the lending lifecycle. Underwriting-decision sampling stratifies by product, prohibited basis variable (race, ethnicity, sex, marital status, age), and underwriting outcome; comparative-file analysis pulls matched-pair samples within strata. Pricing sampling stratifies by spread tier and prohibited-basis variable. Redlining analysis samples geographies with stratification by demographic composition. Marketing sampling stratifies by channel and language coverage. Disparate-impact analysis is statistical; the sampling memo carries the model design separately from the population definition.

##### Sales-practices sampling (broker-dealer suitability and Reg BI)

- Sampling conventions: suitability sampling under FINRA Rule 2111 pulls recommendations made in the period with stratification by product complexity, customer type, and registered representative experience. Reg BI testing for retail customers pulls Care, Conflict, Disclosure, and Compliance Obligation evidence by sample. Tolerable rates for high-complexity-with-retail-customer combinations are typically lower per firm methodology because customer-impact framing concentrates risk.

##### Complaint-handling sampling

- Sampling conventions: complaint-handling sampling pulls complaints received in the period with stratification by intake channel, complaint type, product, and resolution outcome. Reg E §1005.11 error-resolution overlap with complaint sampling: where the complaint is also a §1005.11 dispute, the case appears in both populations and the sample-design notes the dual-track tracking. Complaint-pattern review feeds the consumer-harm read independent of control-framework effectiveness; sample design supports the pattern read with theme stratification.

##### Insurance unfair-trade-practices and unfair-claims-settlement sampling

- Sampling conventions: state-adopted UTPA and UCSPA sampling pulls populations against the state-specific statutory definitions. Multi-state samples carry per-state stratification because state-by-state variance drives the operative criterion. Claims-handling timing populations sample against state-statutory clocks (acknowledgement, investigation, decision, payment).

#### Customer-impact framing in stratification

When the conduct overlay is loaded, stratification often carries a customer-impact dimension that is not a technical-control dimension:

- Vulnerable-population segments (servicemembers under SCRA, older customers, limited-English-proficiency customers, customers in financial hardship) get oversampled where firm methodology recognises the elevated impact of control failures on these segments.
- Low-balance or low-income customers in fee-related testing get oversampled because the dollar impact relative to account size concentrates harm.
- High-volume-low-dollar populations (small-amount fee testing, micro-transaction populations) get sampled with attention to the cumulative effect read, not just the per-item read.

The memo names these stratification choices explicitly; oversampling on customer-impact dimensions is a methodology call that a reviewer can challenge or affirm.

#### Audience and tone

A sampling memo drafted for the firm's CCO and the conduct-risk committee reads heavier on the customer-impact stratification rationale and the complaint-pattern populations. A memo drafted with an upcoming CFPB exam in mind reads heavier on UDAAP module references, complaint-handling populations, and customer-experience populations (call recordings, chat transcripts) with attention to the customer-impact frame in tolerable-rate setting. A memo drafted for fund-board reporting on adviser conduct reads heavier on suitability and Reg BI populations with the customer-base distribution as context.

## cyber

### Cyber cross-cutting overlay — control-sampling

Loaded when `scope.cross_cutting_overlay_set` includes `cyber`, when the test addresses IAM controls, vulnerability management, data-protection controls, or covered-entity-cybersecurity-mandated areas, or when the firm is a Covered Entity under a state cybersecurity regime (e.g., NYDFS 23 NYCRR Part 500). Supplements `references/source-anchors.md`.

#### Population definition conventions for cyber control sampling

Cyber control testing populations carry definitions distinct from financial-control testing:

- **Population items are tickets, alerts, identities, packets, scans, or configurations — not transactions.** Vulnerability remediation tickets closed in the period; SIEM alerts triaged in the period; entitled identities active during the period; recertification packets generated in the period; vulnerability-scan runs during the period; configuration-baseline drift events during the period. The memo names the population in items the sample can draw from.
- **Identities are not packets.** A single user can have multiple recertification packets across roles; a single packet can address multiple entitlements. The memo names which is the population (typically packets for recertification testing; typically identities for terminated-user testing).
- **Extract integrity matters more than transaction-system reconciliation.** IAM entitlement extracts, vulnerability-scan output, and SIEM logs run at different times produce different populations. The memo names the extract date, the run-by role, and the completeness check (entitlement count reconciled to the IAM platform's user count; scan output reconciled to the asset-register asset count; alert count reconciled to the SIEM rule-firing log).
- **Service accounts and break-glass identities are typically excluded from standard recertification populations and sampled separately.** The memo names the exclusion and the separate sample where applicable.

#### Cyber-supervisory anchors (load by reference; do not restate)

- **NYDFS 23 NYCRR Part 500.7 — Access Privileges and Management** [verify subsection labels against the latest amendment]. The standard anchor for access-recertification sampling at NYDFS Covered Entities. https://www.dfs.ny.gov/industry_guidance/cybersecurity .
- **NYDFS 23 NYCRR Part 500.5 — Vulnerability Management** [verify subsection labels]. Vulnerability ticket and remediation populations. https://www.dfs.ny.gov/industry_guidance/cybersecurity .
- **NYDFS 23 NYCRR Part 500** generally — §500.3 cybersecurity policy, §500.4 CISO, §500.9 risk assessment, §500.11 third-party service-provider security, §500.13 asset management and data retention, §500.14 monitoring and training, §500.15 encryption, §500.16 incident response and business continuity, §500.17 notices [verify subsection labels].
- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section]. https://ithandbook.ffiec.gov/it-booklets/information-security.aspx [verify URL].
- **NIST SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations** (January 2022) [verify section labels]. The methodology anchor for assessment-object selection: specifications, mechanisms, activities, and individuals as sampling targets. https://csrc.nist.gov/pubs/sp/800/53/a/r5/final .
- **NIST Cybersecurity Framework 2.0** (February 2024) [verify version number and category labels]. Used as a control-categorisation anchor for sampling scope. https://www.nist.gov/cyberframework .

#### Cyber-control-area sampling notes

##### Access-recertification sampling (Part 500.7-relevant)

- Sampling conventions: population is recertification packets generated in the period (not entitled users). Stratification by privilege tier (standard, privileged, service, break-glass), data sensitivity (PII-handling, restricted, confidential, public), and recertifier role (line manager, application owner, segregation-of-duties reviewer). Privileged-access tolerable rate is typically zero per firm policy. Terminated-employee testing pulls a separate population (HR-IAM feed reconciliation events for terminations during the period) and typically expands from sample to full population because the privileged-not-revoked-after-termination scenario carries asymmetric impact. Judgmental-sample floor often references regulator-handbook appendix conventions (FFIEC IT booklet) and the firm's IT-GCC methodology.

##### Vulnerability-management sampling (Part 500.5-relevant)

- Sampling conventions: population is vulnerability tickets opened or closed in the period, depending on the test objective. Stratification by severity (critical, high, medium, low), asset criticality (tier-1 production, tier-2 production, non-production), and asset class (infrastructure, application, endpoint, cloud). MTTR tests sample closed tickets with stratification by severity and the firm's policy clock. Exception-register testing pulls a separate population (tracked exceptions during the period) and tests for exceptions that have aged out without remediation or formal acceptance.

##### Pen-test and red-team evidence reliance

- Sampling conventions: external pen-test or red-team report findings are themselves a population. Sampling samples reported findings with stratification by severity and asset coverage; the test reads finding-status against the firm's remediation tracking. The pen-test report is third-party-assurance evidence; the population is the firm's remediation actions, not the testing the third party performed.

##### Incident-response sampling (Part 500.16-relevant)

- Sampling conventions: tabletop testing evidence (tabletop-events during the period) and live-incident response evidence (incidents during the period, where applicable) form separate populations. Tabletop-events sampling stratifies by scenario type and participant scope. Live-incident sampling reads against the firm's incident-response plan timeline.

##### Logging and monitoring sampling (Part 500.14-relevant)

- Sampling conventions: SIEM-coverage testing population is the asset register, sampled against the SIEM-log-source register; missing log sources are exceptions on the design dimension. Alert-disposition sampling pulls alerts triaged in the period with stratification by category and disposition (true-positive, false-positive, escalated, suppressed). Tolerable rates for missed-true-positive testing on calibrated control sets are typically near-zero.

##### Encryption sampling (Part 500.15-relevant)

- Sampling conventions: encryption-at-rest and encryption-in-transit testing samples assets with stratification by asset class and data sensitivity. Key-management testing samples key-rotation events with stratification by key category. Unencrypted exceptions tracked via the exception register are sampled against the senior-officer approval requirement under §500.15(b) [verify].

##### Annual certification (Part 500.17(b)-relevant)

- Sampling conventions: testing that supports the senior-officer annual certification samples evidence aligned to the §500.17(b) certification scope; the population definition references the certification-period boundary, and the sample design reads heavy on the criteria that drive certifiable elements.

#### NIST SP 800-53A assessment-object sampling

Where the firm has adopted NIST SP 800-53 control families and SP 800-53A assessment methodology, the sampling memo names the assessment objects under sample (specifications, mechanisms, activities, individuals) per control family. Each object class typically carries its own population and stratification:

- Specifications: documented policies and procedures in force during the period.
- Mechanisms: hardware, software, firmware components active in the period.
- Activities: events that occurred during the period (logins, scans, alerts, reviews).
- Individuals: identities or roles in the assessed scope.

#### Audience and tone

A sampling memo drafted for the firm's CISO and the cyber-risk committee reads heavier on technical-population definitions and remediation-tracking populations. A memo drafted with an upcoming NYDFS examination in mind reads heavier on Part 500 subsection citations, the §500.17(b) certification posture as context for tolerable-rate setting, and the CISO-attested elements. A memo drafted for internal-audit reliance reads heavier on the SP 800-53A assessment-object selection rationale and the extract-integrity posture for IAM, vulnerability, and SIEM populations.

## privacy

### Privacy cross-cutting overlay — control-sampling

Loaded when `scope.cross_cutting_overlay_set` includes `privacy`, when the test addresses GLBA Safeguards Rule controls, HIPAA Security Rule controls (where applicable to the entity), or other consumer-financial-information safeguards. Supplements `references/source-anchors.md`.

#### Population definition conventions for privacy-relevant sampling

Privacy-relevant sampling carries population conventions that overlap with cyber-control sampling but with distinct emphases:

- **Populations are data-handling events, access events, or safeguards-program tests.** Customer-information access events in the period; data-flow inventory entries during the period; safeguards-program test events run during the period; vendor data-handling assessments completed in the period.
- **Consumer-financial-information populations carry data-classification stratification.** Restricted, confidential, internal, public; or the firm's equivalent classification scheme. Sampling concentrates on the highest-sensitivity classes.
- **Vendor-data-handling populations follow third-party risk management scope.** The population is vendors handling consumer financial information during the period; sampling stratifies by data sensitivity, vendor tier, and assessment recency.

#### Privacy-supervisory anchors (load by reference; do not restate)

- **GLBA Safeguards Rule, 16 CFR Part 314 as amended** (FTC, December 2021 amendments effective 2023). §314.4 elements of an information security program, including §314.4(d) regular monitoring and testing of safeguards effectiveness, §314.4(e) implementation of safeguards, §314.4(f) overseeing service providers [verify subsection labels]. https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 .
- **GLBA Privacy Rule, 12 CFR Part 1016 (CFPB Reg P)** [verify subsection labels for the privacy-notice and opt-out testing populations]. https://www.ecfr.gov/current/title-12/chapter-X/part-1016 .
- **HIPAA Security Rule (45 CFR Parts 160, 164 Subpart C)** §164.308(a)(8) periodic technical and nontechnical evaluation; §164.312 technical safeguards (access control, audit controls, integrity, transmission security) [verify subsection labels]. Applicable to financial-services entities only when they are a HIPAA Covered Entity or Business Associate (e.g., a health-insurance arm; a benefits-administration affiliate). https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html .
- **State data-privacy laws (CPRA, VCDPA, CPA, CTDPA, UCPA, etc.)** [verify state-by-state coverage and effective dates]. Applicable when the firm processes resident data above the law's threshold; sampling memos for state-privacy testing populations cite the state statute and the firm's adopted-applicability assessment.
- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section]. The IT-control-testing baseline for federally-supervised banks, including data-protection controls. https://ithandbook.ffiec.gov/it-booklets/information-security.aspx [verify URL].

#### Privacy-control-area sampling notes

##### Safeguards-program sampling (16 CFR §314.4(d)-relevant)

- Sampling conventions: safeguards-program testing pulls test-events run during the period (penetration tests, vulnerability assessments, continuous-monitoring outputs). The population is the firm's safeguards-program testing inventory; stratification by safeguards-program element (access controls, encryption, monitoring, incident response, training). Annual or periodic-risk-assessment evidence is itself a population for sampling.

##### Access-control sampling (privacy frame)

- Sampling conventions: privacy-relevant access-control sampling overlaps with the cyber overlay's IAM sampling but adds data-classification stratification. The population is access events to consumer-financial-information assets; sampling stratifies by data classification and access type (read, write, export, transmit). Audit-control sampling reads logging coverage against the data-classification register.

##### Service-provider oversight sampling (16 CFR §314.4(f)-relevant)

- Sampling conventions: vendor-oversight testing pulls vendors handling consumer financial information during the period with stratification by data sensitivity, vendor tier, and assessment recency. The population is vendor relationships in scope; sampling tests due-diligence evidence, contract-clause coverage, and ongoing-monitoring evidence per the firm's TPRM program.

##### Privacy-notice and opt-out sampling (Reg P-relevant)

- Sampling conventions: privacy-notice testing samples notice-delivery events with stratification by channel and product. Opt-out testing samples opt-out elections received during the period with stratification by channel and product, and tests opt-out propagation across affiliated systems.

##### State-privacy-law sampling (where applicable)

- Sampling conventions: state-privacy-law sampling pulls consumer-rights requests received during the period (right to know, right to delete, right to correct, right to opt-out of sale or sharing) with stratification by request type, requestor state, and resolution status. Per-state stratification matters because state-by-state variance in clocks and exemptions drives the operative criterion.

#### Customer-financial-information classification in stratification

When the privacy overlay is loaded, the data-classification scheme drives stratification:

- Population items are mapped to the firm's data-classification scheme; sampling concentrates on restricted-and-confidential classes per firm methodology.
- Where the firm has not formalised a data-classification scheme, the memo names the gap and uses a coarser stratification (consumer-vs-business, PII-handling-vs-not) with the limitation flagged.

#### Audience and tone

A sampling memo drafted for the firm's CISO or Chief Privacy Officer reads heavier on the data-classification stratification rationale and the safeguards-program testing inventory. A memo drafted with an upcoming FTC or state-AG inquiry in mind reads heavier on the §314.4 element citations and the vendor-oversight populations. A memo drafted for state-privacy-law compliance reads heavier on per-state stratification and the consumer-rights-request populations.
