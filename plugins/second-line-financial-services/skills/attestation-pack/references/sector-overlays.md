# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for attestation-pack

When the scope record names sector `banking`, this overlay adds banking-specific structure and content expectations to the attestation pack. Where there is conflict between capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `attestation-pack/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, BHC, FBO with US operations).

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for banking attestation packs

##### 1. SOX 404 attestation framework with COSO 2013

Public BHCs and SLHCs run management's annual ICFR assessment under SOX §404 against COSO 2013. The attestation pack for a process-owner or function-head sub-certification anchors to the COSO components in the control inventory, surfaces deficiencies (control deficiency, significant deficiency, material weakness) per the SEC and PCAOB definitions, and feeds the executive certification under §302 / §906. The skill produces the sub-certification, not the executive certification; the executive certification is securities-counsel-led.

##### 2. Heightened Standards risk-governance framework attestation linkage

For OCC-supervised covered banks, 12 CFR Part 30 Appendix D Section IV requires the board (or its risk committee) to review and approve the Risk Governance Framework. Process-owner and function-head sub-certifications under the firm's certification framework typically ladder up to the board attestation that the framework is in place and operating; the attestation pack supports that ladder. The sub-certification chain (`sub_certification_chain[]` in the schema) reflects the ladder explicitly.

##### 3. Vendor-management attestation under interagency third-party guidance

The vendor-management attestation use case anchors to the interagency third-party risk management guidance (June 2023), particularly Section III.D (Ongoing Monitoring) and Section III.E (Termination). For each critical third-party relationship, the attestation pack carries:

- Vendor identification (anonymised in shareable artifacts) and criticality tier per the firm's tiering framework.
- Lifecycle-stage organisation of the control inventory (planning, due diligence, contract, ongoing monitoring, termination).
- SOC report reliance evidenced with carve-out review and CUEC-level evidence at the user firm; SOC report alone is not sufficient evidence under the user-firm attestation.
- Exit-test record (where exit testing is in scope under the firm's policy).
- Concentration analysis where the vendor sits at a sector-concentration threshold.

A vendor attestation that cites the SOC report without the CUEC-level evidence or without the carve-out review is the failure mode the troubleshooting file calls out.

##### 4. BCBS 239 risk-data attestation

The risk-data attestation use case (Head of Risk Reporting attesting to data quality and report integrity) anchors to BCBS 239 Principle 1 (Governance). For G-SIBs and other in-scope firms, the attestation typically:

- Organises the control inventory by BCBS 239 principle group (overarching governance: Principles 1-2; aggregation: Principles 3-6; reporting: Principles 7-11; supervisory and remediation: Principles 12-14).
- Consumes the most recent self-assessment (produced by `bcbs239-gap-assessment`) as a primary evidence-index entry.
- Reflects current Top-5 priority gaps as exceptions in the current period.
- Feeds the regulatory-capital-reporting attestation chain where the firm files Y-14, Y-9, FFIEC 031/041, and similar regulatory reports.

For SSM-supervised institutions or US-IHC subsidiaries of SSM groups, the ECB Guide on effective risk data aggregation and risk reporting (May 2024 final) raises the bar incrementally; the overlay carries that distinction when the scope flags both jurisdictions.

##### 5. Y-14 / Y-9 attestation chain

The regulatory-capital-reporting attestation chain at large BHCs typically includes:

- Sub-certifications from process owners on each in-scope reporting line (credit risk, market risk, operational risk, capital, liquidity).
- Function-head sub-certification from the Head of Risk Reporting.
- Function-head sub-certification from the Head of Regulatory Reporting on the report-production process and reconciliation to source.
- CFO-level certification on the financial-statement linkage.

The attestation pack supports each layer; the executive Y-14 attestation itself is owned by the CFO function and is out of scope for this skill.

##### 6. CRA, BSA, and consumer-compliance attestations

BSA officer annual certification (firm-policy artifact, often required by board policy or by examination expectation) is a recurring use case. The attestation pack typically covers:

- The BSA program elements per 31 CFR Part 1020 (internal controls, training, independent testing, BSA Officer designation).
- Fifth Pillar (CDD Rule) elements.
- Sanctions-program elements where the BSA Officer also serves as the OFAC compliance lead.
- Findings from the most recent independent testing and any open MRA or MRIA on AML or sanctions topics.

CRA self-assessments and consumer-compliance attestations follow analogous patterns.

##### 7. Sign-off and review machinery

For OCC-supervised covered banks, the named reviewers on a sub-certification pack typically include the function head's direct manager (one ladder up), the Head of Internal Audit's relationship lead for the function, and the General Counsel's office. For process-owner sub-certifications, the function head is the principal reviewer.

For BHCs, the Board Audit Committee receives the annual SOX 404 management report; the executive certification under §302 / §906 is filed with the SEC by the CEO and CFO with securities-counsel review.

#### What the overlay leaves to the SKILL workflow

This overlay names the banking-specific anchors and use cases. It does not replicate the workflow steps. The SKILL.md walks the order of work; the overlay tells the SKILL which assertion shape, which evidence categories, and which sign-off ladder apply.

## capital-markets

### Capital-markets sector overlay for attestation-pack

When the scope record names sector `capital-markets`, this overlay adds capital-markets-specific structure and content expectations. Where there is conflict between capability defaults and this overlay, the overlay governs the capital-markets-sector elements.

Loaded by: `attestation-pack/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type is a registered investment adviser, broker-dealer, registered fund, transfer agent, or other capital-markets-registered entity.

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for capital-markets attestation packs

##### 1. Fund CCO annual report under Rule 38a-1

For registered investment companies, Rule 38a-1 under the Investment Company Act of 1940 requires the fund CCO to provide a written report at least annually to the fund board addressing the operation of the fund's compliance policies and procedures, material changes since the prior report, and material compliance matters since the prior report. The attestation pack supporting the report typically:

- Covers the fund-complex-level compliance program elements and the per-fund tailoring.
- Surfaces material compliance matters with linked issues and remediation status.
- Anchors to Rule 38a-1 explicitly in the assertion text.
- Carries fund CCO sign-off and routes to the board (typically via the fund board's Audit Committee or a dedicated Compliance Committee).

The fund CCO is the named signer; this is fund-board-level, not adviser-level.

##### 2. Adviser CCO annual review under Rule 206(4)-7

For registered investment advisers, Rule 206(4)-7 under the Investment Advisers Act of 1940 requires the adviser CCO to conduct an annual review of the adequacy of the adviser's compliance policies and procedures and the effectiveness of their implementation. The annual review is not a regulator-filed report but typically generates an internal attestation pack reviewed by the firm's senior management and (for many firms) the board or governing body. The attestation pack typically:

- Covers the firm-level compliance program elements (Code of Ethics under Rule 204A-1, advertising, custody, books and records, marketing, privacy).
- Reflects findings from the annual review with linked remediation.
- Anchors to Rule 206(4)-7 explicitly.
- Carries adviser CCO sign-off and routes to senior management.

The adviser-level attestation and the fund-CCO attestation are distinct artifacts even where the same firm serves as adviser to registered funds. This skill produces both as separate pack instances.

##### 3. Broker-dealer Rule 17a-5 annual report

For registered broker-dealers, Rule 17a-5 (17 CFR §240.17a-5) requires annual filing including (depending on broker-dealer category) a financial-responsibility report and either a compliance report or an exemption report. The compliance report includes management assertions on compliance with the financial-responsibility rules (Rule 15c3-1 net capital, Rule 15c3-3 customer-protection, books-and-records requirements). The attestation pack typically:

- Carries process-owner sub-certifications on net-capital computation, customer-protection segregation, and books-and-records integrity.
- Anchors to the specific financial-responsibility rules in the assertion text.
- Coordinates with the PCAOB AS 3105 auditor on the audit of the financial reports.

##### 4. FINRA 3120 / 3130 supervisory and CEO certifications

FINRA Rule 3120 requires a written report on the supervisory system to senior management at least annually. FINRA Rule 3130 requires the CEO to certify annually that the member firm has processes in place to establish, maintain, review, test, and modify policies and procedures reasonably designed to achieve compliance with applicable securities laws. The attestation pack supporting Rule 3130 typically:

- Anchors to Rule 3130(b) explicitly.
- Surfaces the Rule 3120 report content as an evidence-index entry.
- Carries CEO sign-off (this is the executive certification at the broker-dealer level; the skill produces the CCO and CCO-equivalent sub-certifications that ladder to the CEO certification).

##### 5. Form ADV and Form CRS attestation chain

While not formal attestation packs in their own right, Form ADV and Form CRS filings carry implicit attestations. The annual amendment cycle generates internal attestation work supporting the filing accuracy; the attestation pack for the underlying compliance program is consumed as evidence.

##### 6. Sign-off and review machinery

Capital-markets attestation packs typically include the General Counsel's office (with securities counsel for executive-certification-adjacent work), the Chief Compliance Officer (for both adviser and fund CCO depending on the entity), the Chief Audit Executive, and the CFO and CEO at the function-head and executive layers respectively. Fund-board attestations route to the fund board (typically Audit Committee or dedicated Compliance Committee); adviser attestations route to senior management; broker-dealer attestations route to the firm's governing body and (for certain reports) to FINRA and the SEC.

#### What the overlay leaves to the SKILL workflow

This overlay names the capital-markets-specific anchors and use cases. It does not replicate the workflow steps.

## insurance

### Insurance sector overlay for attestation-pack

When the scope record names sector `insurance`, this overlay adds insurance-specific structure and content expectations. Where there is conflict between capability defaults and this overlay, the overlay governs the insurance-sector elements.

Loaded by: `attestation-pack/SKILL.md` when `scope.sector_overlay_set` includes `insurance`, or when the institution type is an insurer or insurance group.

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for insurance attestation packs

##### 1. NAIC Model Audit Rule (Model #205) ICFR attestation

For insurers above the premium threshold (conventionally $500 million single insurer or $1 billion insurance group, with state-by-state variation), Model #205 Section 16 requires an annual management report of internal control over financial reporting filed with the domiciliary-state insurance department. The structure parallels SOX §404:

- Management assertion on the design and operating effectiveness of ICFR over financial-statement preparation.
- Identification of material weaknesses.
- Sub-certifications from process owners (claims, underwriting, reserving, investments, reinsurance, statutory reporting) feeding the function-head sub-certification feeding the CFO-level assertion.
- External-auditor attestation on the management assertion (where the carrier is in scope of the auditor-attestation requirement).

The attestation pack typically covers the function-head and process-owner layers; the CFO-level assertion is owned by the CFO function with auditor coordination.

##### 2. ORSA management assertion (Model #505)

For insurers in scope of the Risk Management and Own Risk and Solvency Assessment Model Act (#505), the annual ORSA Summary Report carries an implicit management assertion on the risk-management framework and the own-risk-and-solvency assessment. The attestation pack supporting the ORSA Summary Report typically:

- Maps the control inventory to ORSA Summary Report Section 1 (Description of the Insurer's Risk Management Framework), Section 2 (Insurer's Assessment of Risk Exposure), and Section 3 (Group Risk Capital and Prospective Solvency Assessment).
- Carries CRO sub-certification on the risk-management framework.
- Carries Chief Actuary sub-certification on the prospective solvency assessment and capital projections.
- Carries CFO sub-certification on the group risk capital and the financial-statement linkage.

##### 3. Statutory accounting and SAP attestation

Beyond GAAP-based ICFR under Model #205, statutory accounting principles (SAP) carry their own attestation expectations through the Annual Statement and the actuarial opinion. The attestation pack for statutory reporting typically:

- Anchors to the NAIC Accounting Practices and Procedures Manual.
- Carries process-owner sub-certifications on each Schedule of the Annual Statement (Schedule F reinsurance recoverables, Schedule D investments, Schedule P loss reserves where applicable).
- Coordinates with the appointed actuary on the actuarial opinion (which is a separate attestation under Section 5 of the actuarial opinion model regulation).

##### 4. Cyber attestation under NAIC Insurance Data Security Model Law (#668)

For state-licensed insurers in jurisdictions that have adopted Model #668 (state-by-state adoption), the annual notice of compliance signed by the senior officer is a recurring attestation. The cyber overlay (`references/cross-cutting.md#cyber`) carries the substantive content; the insurance overlay reflects that for insurers, Model #668 is the parallel to NYDFS Part 500 §500.17(b) for non-NYDFS-licensed carriers.

##### 5. Sign-off and review machinery

Insurance attestation packs typically include the appointed actuary as a named reviewer on actuarial-opinion-adjacent attestations, the General Counsel for legal review, the Chief Audit Executive for internal-audit perspective, and the CFO and CRO at the function-head layer. The board Audit Committee receives the annual Model #205 report; the lead state insurance department receives the ORSA Summary Report and (where applicable) the Model #205 management report.

#### What the overlay leaves to the SKILL workflow

This overlay names the insurance-specific anchors and use cases. It does not replicate the workflow steps.

## payments-fintech

### Payments-fintech sector overlay for attestation-pack

When the scope record names sector `payments-fintech`, this overlay adds payments and fintech-specific structure and content expectations. Where there is conflict between capability defaults and this overlay, the overlay governs the payments-fintech-sector elements.

Loaded by: `attestation-pack/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type is a money services business, payment processor, card network participant, or fintech in a sponsor-bank-partnership arrangement.

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for payments-fintech attestation packs

##### 1. PCI DSS Attestation of Compliance (AOC)

Card-handling entities (merchants, service providers, payment processors) attest annually to PCI DSS compliance via the Attestation of Compliance form. Level 1 merchants and service providers complete the AOC validated by a Qualified Security Assessor; lower-volume entities use a Self-Assessment Questionnaire. The attestation pack typically:

- Organises the control inventory by the twelve PCI DSS requirements (current version v4.0 / v4.0.1; verify at pack-write time).
- Surfaces in-scope cardholder-data environment (CDE) boundaries explicitly.
- Carries the QSA assessment as an evidence-index entry where applicable.
- Anchors to the AOC form structure and to PCI DSS v4.0 / v4.0.1 explicitly.
- Routes to the merchant acquirer or the card brands per the brand's compliance program (Visa, Mastercard, AMEX, Discover, JCB).

PCI DSS v3.2.1 retired March 31, 2024; v4.0 in force with v4.0.1 minor revisions. The new authentication and cryptographic requirements at v4.0 may surface as exceptions where firm-side implementation is in transition.

##### 2. Sponsor-bank-partnership attestation linkage

For fintech entities in sponsor-bank-partnership arrangements (BaaS, deposit programs, credit-product partnerships), the sponsor bank is the regulated entity and the fintech operates under contractual flow-down of the sponsor bank's regulatory expectations. The attestation pack for the fintech typically:

- Anchors to the contractual flow-down terms from the sponsor bank's third-party-risk-management requirements.
- Carries process-owner sub-certifications on the operational controls the sponsor bank's third-party oversight tests against (KYC, transaction monitoring, complaint handling, dispute resolution under Reg E or Reg Z, fair-lending screening for credit products).
- Feeds the sponsor bank's vendor-management attestation as a vendor-side input.

The sponsor bank is in scope of the federal banking agencies' interagency third-party risk management guidance (June 2023); the fintech-side attestation supports the bank-side oversight rather than substituting for it.

##### 3. State money transmitter and MSB attestation

For state-licensed money transmitters and FinCEN-registered MSBs, attestation expectations vary by state and by FinCEN registration category. Common elements include:

- BSA program attestation under 31 CFR Part 1022 (MSB rule), including the Section 314(a) and (b) processes.
- State surety-bond and net-worth maintenance attestations per the licensing state's requirements.
- Money Transmitter Modernization Act (MTMA) compliance attestations in states that have adopted MTMA.

##### 4. Operational resilience attestation under Regulation E and Regulation Z

For payments and consumer-finance products, attestations on Reg E (electronic fund transfers, error resolution, prepaid accounts) and Reg Z (truth in lending, credit cards) compliance are standing obligations. The attestation pack typically:

- Carries process-owner sub-certifications on dispute resolution, provisional credit, error resolution timing.
- Surfaces metrics on dispute volumes, average resolution time, and aging against the Reg E ten-business-day clock.
- Anchors to the relevant subparts of Reg E (12 CFR Part 1005) and Reg Z (12 CFR Part 1026) explicitly in the assertion text.

##### 5. Sign-off and review machinery

Payments-fintech attestation packs typically include the General Counsel, the Chief Compliance Officer, the BSA Officer, the CTO or CISO (for technical-control attestations such as PCI DSS), and the CEO at the executive layer. For sponsor-bank partnerships, the pack typically routes to the sponsor bank's vendor-management function as a deliverable to the partnership; the sponsor bank's own attestation chain consumes it.

#### What the overlay leaves to the SKILL workflow

This overlay names the payments-fintech-specific anchors and use cases. It does not replicate the workflow steps.
