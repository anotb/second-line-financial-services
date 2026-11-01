# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Sector overlay: banking

Loads when `sector_overlay_set` includes `banking`. Carries large-bank supervisory-finding terminology context, heightened-standards severity flavour, and the BSA/AML and consumer-compliance exception conventions that shape classification and severity calibration in bank-side compliance testing.

#### Supervisory-finding terminology context

Bank examiners use a structured ladder for supervisory findings: matter-requiring-attention, matter-requiring-immediate-attention, formal enforcement action. Federal Reserve, OCC, and FDIC each carry their own variants; large banks are typically in scope of more than one. The firm does not invent a regulator-issued matter; it drafts its own exceptions in the same shape so its records align with examiner vocabulary.

What this means for the register:

- An exception severity-ranked `critical` should be readable in the shape an examiner would expect to see for a matter-requiring-immediate-attention candidate (clearly stated condition, criterion with section reference, dated, scoped, with quantified effect where possible). The register itself carries internal severity, not an examiner classification.
- A repeat-issue flag with a prior issue ID raises the supervisory-finding-eligibility read. Repeat exceptions on the same control or population are the classic pattern that converts a matter-requiring-attention into something heavier on the next exam cycle.
- Exception conditions and effects that touch board-reported metrics or consolidated risk reporting carry escalated severity rationale (the supervisory expectation is that board-reported information is reliable). [verify the exact framing in current Federal Reserve and OCC guidance.]

The firm's escalation playbook is the firm's; this overlay does not substitute for it. The handoff to issue write-up populates fields the firm uses to ladder its own internal escalation, and `issue-writeup` carries the matter-requiring-attention / matter-requiring-immediate-attention classification field where the source is examiner-issued.

#### Heightened-standards severity flavour

For large insured national banks within scope of 12 CFR Part 30 Appendix D, the three-lines-of-defense structure is part of the supervisory expectation rather than a methodology preference. [verify section labels.]

Exception classification carries this:

- A control-failure exception in the front-line that the independent risk-management function did not surface earlier in the lifecycle reads with different severity than the same exception caught earlier. The severity rationale field names the second-line and internal-audit roles in the chain.
- Risk-governance-framework exceptions (limits framework, risk-appetite reporting, board-level risk reporting) carry the heightened-standards framing; the criterion field cites Appendix D with a section reference.

#### BSA/AML exception conventions

BSA/AML testing produces a distinctive set of exception patterns: customer-due-diligence file completeness, beneficial-ownership documentation, currency-transaction reporting accuracy, suspicious-activity-report timing, OFAC sanctions-screening hits clearance. The criterion is typically the BSA/AML rule with a section reference (31 CFR Chapter X) and the FFIEC BSA/AML examination manual section. [verify rule and manual sections per the current edition.]

Classification calls for the BSA/AML population:

- A missing CDD document where the customer relationship was nonetheless onboarded with required risk rating in the system reads as `evidence-gap`, severity moderates against frequency and customer risk tier.
- A late SAR filing reads as `control-failure` with timing being the load-bearing fact; severity calibration uses the SAR-timing rule's deadlines, not the firm's internal SLA.
- A sanctions-screening hit not cleared within the firm's escalation SLA reads as `control-failure`, severity scales with the watch-list source and the customer relationship type. Critical when the hit is on a primary sanctions list.

Conduct-overlay loading is automatic when the BSA/AML population includes consumer-facing accounts.

#### Consumer-compliance exception conventions

Consumer-compliance testing covers Reg E (electronic fund transfer error resolution), Reg Z (truth in lending), Reg B (equal credit opportunity), Reg DD (truth in savings), HMDA (home mortgage disclosure), Reg X (RESPA), and the CFPB UDAAP frame. [verify CFR citations per current editions.]

Classification calls:

- Timing-rule deviations (Reg E provisional credit, error resolution finals, Reg X disclosure timing) read as `control-failure`, severity calibrated against the regulatory deadline and the consumer-impact pattern.
- HMDA LAR data accuracy deviations split between `data-integrity` (system of record disagrees with the LAR submission) and `control-failure` (the source data was wrong).
- UDAAP-touching exceptions load the conduct cross-cutting overlay; the severity rationale field carries customer-harm framing distinct from the technical control deviation.

#### Sponsor-bank programme overlay (intersection with payments-fintech)

Bank-as-a-service / sponsor-bank engagements are bank-side; they often load alongside `payments-fintech.md` because the controls under test span the bank's oversight machinery and the fintech partner's operational execution. Exception classification here often turns on whether the deviation is in the bank's oversight control (sponsor-bank-side `control-failure` or `design-gap`) or in the partner's execution that the bank's oversight should have caught (still classified at the bank's control, not the partner's, because the bank is the testing subject). [verify the relevant interagency third-party guidance section labels.]

## capital-markets

### Sector overlay: capital-markets

Loads when `sector_overlay_set` includes `capital-markets`. Carries supervision-rule exception treatment for broker-dealer and investment-adviser testing, and enforcement-style language hygiene.

#### Broker-dealer supervision exception treatment

Broker-dealer testing operates against FINRA supervision rules: FINRA Rule 3110 (supervision), Rule 3120 (supervisory control system), Rule 3130 (annual certification of compliance and supervisory processes). [verify the current rule text; FINRA periodically issues regulatory notices that update the supervisory expectations.]

What this means for the register:

- A supervisory-review deviation (sales-practice review, communications review, OBA / outside-business-activity attestation) reads as `control-failure` or `design-gap` depending on whether the review process exists but missed the item (`control-failure`) or the supervisory system itself does not require the review the criterion expects (`design-gap`).
- A trade-surveillance alert that was not adjudicated within the firm's documented timeframe reads as `control-failure`, severity scales with the alert tier and the volume of unadjudicated alerts.
- An annual-certification gap (Rule 3130) reads as `design-gap` if the certification process itself does not address the criterion the test surfaced; reads as `evidence-gap` if the process did address it but the artifact does not show it.

#### Investment-adviser compliance-program exception treatment

Adviser testing operates against the Advisers Act compliance-program rule (Rule 206(4)-7) and the related code-of-ethics rule (Rule 204A-1). [verify rule citations and current SEC interpretive guidance.]

Classification calls:

- A compliance-program annual review deviation (no documented review, scope of review did not cover a material risk) reads as `design-gap` when the program design did not address the risk and as `control-failure` when the design did but the review missed it.
- A code-of-ethics violation (personal securities transaction not reported, late reporting, unapproved transaction) reads as `control-failure`; severity calibration references the access-person designation and the violation pattern.
- A custody-rule (Rule 206(4)-2) deviation reads with elevated severity because the custody framework itself is the supervisory bar; the criterion field cites the rule with a section reference.

#### SEC EXAMS examination posture

SEC EXAMS deficiency letters and the related risk-alert publications shape what severity calibration the firm carries on testing exceptions in advance of a likely exam. [verify the current calendar-year EXAMS examination priorities and the risk-alert publications relevant to the firm's business model.]

Exception classification reads against EXAMS priorities:

- A deviation in an area called out in the current EXAMS priorities carries elevated severity rationale; the rationale field names the priority area.
- Repeat exceptions in priority areas raise the supervisory-finding-eligibility read meaningfully.

#### Enforcement-style language hygiene

Capital-markets testing carries an additional discipline because the surrounding enforcement environment uses precise language for legal violations. The register concludes on control effectiveness and exception classification, not on legal violation. "The firm violated Rule X" is not register language; "the control did not operate as designed for the [population] during the period, the criterion being Rule X" is.

The handoff to issue write-up follows the same discipline: the recommendation seed names the control or process change, not the legal conclusion. Legal-violation determinations are for legal counsel and regulator-led proceedings, not for second-line testing artifacts.

## insurance

### Sector overlay: insurance

Loads when `sector_overlay_set` includes `insurance`. Carries state-DOI market-conduct exception conventions and the model-audit-rule severity framing for ICFR-relevant findings.

#### State DOI market-conduct exception conventions

State insurance departments examine market-conduct practices on a multi-state or single-state basis, working from the NAIC Market Regulation Handbook and state-specific examination procedures. [verify the current NAIC Market Regulation Handbook edition and the state-specific procedure references for the entity's domicile and material states.]

What this means for the register:

- Exception classification on market-conduct testing populations (claims handling timing, producer licensing, advertising compliance, complaint handling, underwriting discrimination, replacement-of-policy practices) reads against the NAIC handbook standards and the relevant state-specific timing rules.
- A claims-timing deviation reads as `control-failure` with the state-specific prompt-pay-rule deadline as the load-bearing fact.
- A producer-licensing deviation reads as `control-failure` or `data-integrity` depending on whether the producer was unlicensed in the state at the time of the transaction (control-failure) or the producer was licensed but the licensing record in the firm system was stale (data-integrity).
- A complaint-handling deviation that surfaces a UDAAP-analogue pattern (state insurance unfair-trade-practices acts) loads the conduct cross-cutting overlay; the severity rationale carries consumer-harm framing.

The handoff to issue write-up populates fields the firm's market-conduct response register consumes; severity calibration uses the firm's published thresholds where they exist and the state-specific examination procedure's severity hierarchy where they do not.

#### NAIC Model Audit Rule severity framing for ICFR-relevant findings

Insurer ICFR-over-financial-reporting testing operates against the NAIC Model Audit Rule (Model #205) framework for insurers above the audit-exemption threshold. [verify Model #205 current revision date and the state adoption status for the entity's domicile.]

ICFR-relevant exception classification:

- A material-weakness candidate reads at `critical` severity. The severity rationale references both the dollar materiality threshold and the qualitative-materiality factors (regulatory exposure, ORSA-impact, board-reported figure exposure).
- A significant-deficiency candidate reads at `high` severity.
- A control-deficiency that is neither carries lower severity but the rationale still references the insurer's own materiality framework and the auditor's analogous evaluation under AU-C 265.

Where the test was scoped to support an ORSA filing or a Form B / Form F filing under the NAIC Insurance Holding Company System Regulatory Act, the criterion field cites the NAIC model and the state-specific adoption with a section reference. [verify the holding-company-act references for the entity's lead-state regulator.]

#### Captive-insurer and reinsurance considerations

For captive insurers and reinsurance arrangements, the regulatory regime varies by domicile (Vermont, Bermuda, Cayman, others). Exception classification follows the applicable domicile's exam manual and the relevant accreditation standard. [verify the domicile-specific exam manual sections.] The register notes the regulatory regime explicitly in the criterion field; do not import US state-DOI conventions wholesale into a non-US captive register.

## payments-fintech

### Sector overlay: payments-fintech

Loads when `sector_overlay_set` includes `payments-fintech`. Carries sponsor-bank oversight exception conventions and Reg E error-resolution exception treatment.

#### Sponsor-bank oversight exception conventions

Bank-as-a-service / sponsor-bank programmes carry exception patterns that span the bank's oversight machinery and the fintech partner's operational execution. The interagency third-party-relationships guidance (June 6, 2023, OCC / FRB / FDIC) sets the supervisory expectation. [verify section labels under the published guidance.]

What this means for the register:

- The testing subject is the bank's oversight control, not the fintech partner's operational control. Classification reads against the bank-side criterion, even when the underlying observable condition was at the partner.
- A partner-side execution gap that the bank's oversight control did not surface reads as `control-failure` at the bank's oversight control. The severity rationale names the partner-side condition, the oversight criterion, and the gap in the bank's monitoring or escalation process.
- A partner-side execution gap that the bank's oversight control did surface and escalate reads as `closed-at-exception` on the bank's oversight, with the partner-side issue tracked in the firm's vendor-monitoring register (a separate artifact).
- A design-gap in the bank's oversight programme (no monitoring control exists for a partner risk the third-party guidance expects to be monitored) reads as `design-gap`, severity calibrated against the partner's criticality tier.

The handoff to issue write-up populates fields the bank's third-party-risk issue ladder consumes; severity calibration carries the partner criticality and the supervisory expectation that critical-vendor oversight is heightened.

#### Reg E error-resolution exception treatment

Reg E (12 CFR 1005, Subpart A) error-resolution testing produces a high-volume exception population in payments and consumer-facing fintech. [verify current section labels at 12 CFR 1005.11 for error resolution and §1005.6 for liability.]

Classification calls:

- Provisional-credit timing deviations (the rule sets a 10-business-day deadline for provisional credit when the institution cannot complete investigation within that window) read as `control-failure` with timing as the load-bearing fact. Severity calibrates against frequency and the dollar pattern.
- Error-resolution-final-determination timing deviations read similarly; the rule sets a 45-day deadline (90 days for new accounts and certain transaction types). [verify the current deadline structure.]
- Investigation-quality deviations (no documented investigation steps, conclusion not supported by the investigation record) read as `evidence-gap` when the system shows the investigation occurred and as `control-failure` when there is no system or file record of the investigation at all.
- Liability-determination deviations (consumer assessed liability beyond the rule's caps, liability assessed without the conditions the rule requires) read as `control-failure`, severity calibrated against the liability amount and the consumer-harm pattern.

Conduct cross-cutting overlay loads automatically when the Reg E population is consumer-facing.

#### Money-transmitter exception treatment

Money-transmitter testing carries state-by-state regulatory variation. [verify the relevant state money-transmitter act sections for the states where the entity is licensed.] Exception classification reads against the state-specific obligations the test was scoped to; the criterion field cites the state-specific rule with a section reference. The severity rationale field names the state-specific examination posture where it differs from federal expectations.

#### Card-network and processor exception patterns

For testing scoped to card-network rules (Visa Core Rules, Mastercard Rules) or processor-side reconciliation controls, the criterion is typically the network rule with a rule-section reference and the firm's contractual obligation under the network agreement. [verify the network rule edition.] These are typically `control-failure` or `data-integrity` exceptions rather than `design-gap`; the design is the network's, not the firm's. The severity rationale field names the network-side fining or chargeback exposure.
