# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Cross-cutting overlay: conduct — obligation-mapping

Loaded when the scope includes `conduct` in `cross_cutting_overlay_set`, or when the source being mapped is conduct-anchored. Adds conduct-specific source labels and obligation patterns when the register scopes consumer-facing decisions, marketing, complaints, or fair-treatment processes. Does not change the row spine.

Conduct sits where consumer compliance, fair-lending, market-conduct, and product-governance overlap. The register often loads conduct alongside privacy when the process touches consumer decisioning, alongside `payments-fintech` when the product is a consumer payment, and alongside `insurance` when the engagement covers insurance market-conduct.

#### Sources the register may cite

##### CFPB and federal consumer-finance conduct

- Dodd-Frank Act §§1031, 1036 (UDAAP); CFPB UDAAP Examination Procedures (current edition of the CFPB Supervision and Examination Manual UDAAP module).
  - Use for: unfair, deceptive, abusive acts and practices obligations across consumer-financial-product processes; the register cites the manual section and the underlying statutory authority.
  - Link: https://www.consumerfinance.gov/compliance/supervision-examinations/

- Equal Credit Opportunity Act (ECOA), 15 U.S.C. §1691 et seq.; Reg B, 12 CFR Part 1002.
  - §1002.4 (general rules), §1002.5 (information about applicants), §1002.7 (rules concerning extensions of credit), §1002.9 (notifications), §1002.13 (information for monitoring purposes), §1002.14 (rules on appraisals).
  - Use for: fair-lending obligations including adverse-action notification, monitoring-information collection, and §1002.7 spousal-signature rules.
  - Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1002

- Fair Housing Act, 42 U.S.C. §3601 et seq. and HUD's implementing regulations (24 CFR Part 100).
  - Use for: housing-related fair-lending obligations on dwelling-secured credit.

- Home Mortgage Disclosure Act; Reg C, 12 CFR Part 1003.
  - Use for: HMDA reporting obligations on covered institutions; the register cites the §1003.x reporting and recordkeeping sections.

- CFPB Section 1071, 12 CFR 1002.107 et seq.
  - Use for: small-business-lending data collection conduct obligations; pair with the §1002.108 firewall conduct row.

- Servicemembers Civil Relief Act and Military Lending Act (32 CFR Part 232).
  - Use for: military-borrower conduct obligations.

- Real Estate Settlement Procedures Act (RESPA), 12 CFR Part 1024.
  - §1024.7 (Loan Estimate via §1026.19(e)), §1024.17 (escrow accounts), §1024.30 et seq. (servicing).
  - Use for: mortgage-settlement and servicing conduct obligations.

- Fair Debt Collection Practices Act, 15 U.S.C. §1692 et seq.; Reg F, 12 CFR Part 1006.
  - Use for: third-party debt-collection conduct obligations.

##### Capital-markets conduct

- Reg BI (Best Interest), 17 CFR §240.15l-1.
  - Care, conflict-of-interest, disclosure, and compliance obligations on broker-dealers serving retail customers.
  - Use for: retail-investor conduct obligations.

- IAA fiduciary duty (interpretation in IAA SEC Release 5248).
  - Use for: investment-adviser fiduciary conduct obligations on retail clients.

- FINRA Rule 2010 (standards of commercial honor) and FINRA Rule 2111 (suitability).
  - Use for: FINRA-imposed conduct obligations.

##### Insurance conduct

- NAIC Suitability in Annuity Transactions Model Regulation (Model #275) and state best-interest adoptions (NY Reg 187, Iowa best-interest amendments, others).
  - Use for: annuity sales conduct obligations.
  - Link: https://content.naic.org/

- NAIC Unfair Trade Practices Act (Model #880) and state adoptions.
  - Use for: insurance unfair-trade-practice obligations.

##### Complaint handling as conduct

- CFPB Complaint Handling expectations within the CMS framework.
  - Use for: complaint-intake, response, root-cause, and reporting obligations on CFPB-supervised firms.

- Functional-regulator complaint-handling expectations (OCC, FDIC, FRB consumer-affairs procedures).
  - Use for: bank-supervised complaint-handling obligations.

#### Obligation patterns the practitioner expects to find

- **UDAAP obligations as design and conduct rows.** UDAAP risk attaches to product features and to operational practices; the register surfaces both kinds of rows (a fee-disclosure UDAAP row is a design row; an unauthorized-charge handling UDAAP row is a conduct row).
- **Adverse-action obligations across credit and insurance.** ECOA §1002.9 adverse action, FCRA §615 adverse-action notice, and state insurance adverse-underwriting notification obligations each impose distinct content and timing.
- **Suitability and best-interest rows.** Reg BI care obligation, IAA fiduciary duty, FINRA 2111 suitability, NAIC best-interest annuity rules. The register surfaces them as separate rows even when the same retail customer interaction triggers more than one.
- **Disclosure-timing rows.** RESPA Loan Estimate timing, TILA §1026.19 timing, ECOA §1002.9(a)(1) adverse-action 30-day window, Reg E §1005.7 prior-to-first-EFT timing. Each is a distinct row.
- **Complaint-handling rows.** Intake within X days, root-cause analysis, response to consumer, regulator-reporting where required (CFPB consumer-complaint database for CFPB-supervised firms, NYDFS Reg 218 [verify] for NYDFS insurance).
- **Servicing and collection conduct rows.** RESPA Subpart C servicing obligations, Reg F debt-collection limits, Mortgage Servicing Rules call requirements.

#### What does not belong here

- Information-security obligations. Those go to the cyber overlay.
- Privacy notices and data-subject rights. Those go to the privacy overlay (notice content overlaps with conduct disclosure obligations; surface both rows with cross-references rather than collapsing).
- Internal firm policy and taxonomy. That goes in `references/firm-overlay.md`.

## cyber

### Cross-cutting overlay: cyber — obligation-mapping

Loaded when the scope includes `cyber` in `cross_cutting_overlay_set`, or when the source being mapped is cyber-anchored. Adds cyber-specific source labels and obligation patterns the practitioner expects to find when the register scopes information-security or cybersecurity processes. Does not change the row spine.

The cyber overlay is the most-loaded cross-cutting overlay in this skill: most material processes touch information systems, and most multi-source registers carry at least one cyber-anchored row.

#### Sources the register may cite

##### State-issued cyber rules

- NYDFS 23 NYCRR Part 500 — Cybersecurity Requirements for Financial Services Companies (effective March 2017; amended November 2023).
  - §500.2 (cybersecurity program), §500.3 (cybersecurity policy), §500.4 (CISO), §500.5 (vulnerability management), §500.7 (access privileges), §500.9 (risk assessment), §500.11 (third-party service-provider security policy), §500.13 (asset management), §500.14 (training and monitoring), §500.16 (incident response and BCDR), §500.17 (notice of cybersecurity event).
  - Use for: NYDFS-covered entities; the register cites the precise §500.x section per row and notes covered-entity tier under the November 2023 amendment.
  - Link: https://www.dfs.ny.gov/industry_guidance/cybersecurity

##### Federal cyber rules

- SEC cybersecurity disclosure rules (2023, 17 CFR Part 229 and Part 232).
  - Reg S-K Item 106 (cyber risk management, strategy, and governance disclosure).
  - Form 8-K Item 1.05 (material cybersecurity incident disclosure within four business days of materiality determination).
  - Use for: issuer-side cybersecurity disclosure obligations on registered companies; cross-load with `capital-markets` if the engagement includes issuer reporting.
  - Link: https://www.sec.gov/rules/final/2023/33-11216.pdf

##### Federal supervisory expectations

- FFIEC Information Security booklet (September 2016; under current revision).
  - §II (governance), §III (risk identification and assessment), §IV (mitigation), §V (security operations), §VI (testing), §VII (incident response), §VIII (resilience). [verify section labels against currently posted edition.]
  - Use for: bank-supervised information-security obligations; the booklet is supervisory expectation rather than rule, and the register notes that distinction in the source-trace.
  - Link: https://ithandbook.ffiec.gov/it-booklets/information-security/

- Interagency Guidelines Establishing Information Security Standards (12 CFR Part 30 Appendix B / Part 208 Appendix D / Part 364 Appendix B).
  - §III (information security program), §III.C (assess risk), §III.D (manage and control risk).
  - Use for: bank-supervised information-security-program obligations under GLBA §501(b) implementation.

- Computer-Security Incident Notification Rule for banking organizations (12 CFR Part 53 OCC / Part 225 Appendix N FRB / Part 304 FDIC), effective May 2022.
  - 36-hour notification obligation to the primary federal regulator following determination of a notification incident.
  - Use for: incident-notification obligations on supervised banking organizations.
  - Link: https://www.ecfr.gov/current/title-12/chapter-I/part-53

- FFIEC Authentication and Access to Financial Institution Services and Systems guidance (August 2021).
  - Use for: customer-authentication and access-control obligations.

##### EU cyber and ICT

- DORA — Regulation (EU) 2022/2554. Articles 5-14 (ICT risk management framework), Articles 17-23 (ICT-related incident management, classification, reporting), Articles 24-27 (digital operational resilience testing), Articles 28-30 (ICT third-party risk).
  - Use for: EU-anchored cybersecurity and ICT obligations; the register cites the named article on each row.
  - Link: https://eur-lex.europa.eu/eli/reg/2022/2554/oj

##### Privacy adjacents (when scope edges into privacy)

- GLBA Safeguards Rule (FTC, 16 CFR §314.4 elements; functional regulator equivalents for bank-supervised institutions).
  - Use for: information-security-program elements when the privacy overlay is also loaded.

#### Obligation patterns the practitioner expects to find

- **Section-precise rows.** NYDFS Part 500 obligations extract at the §500.x level; mapping a single Part 500 obligation to "the program in general" loses the rule. The register cites the section.
- **Tier-dependent applicability.** Part 500 amendments introduced covered-entity tiers; the row's applicability column carries the tier reasoning.
- **Incident-notification obligations as their own rows.** The 36-hour banking incident notification, NYDFS §500.17, SEC Form 8-K Item 1.05, and DORA Article 19 incident-classification windows all extract as separate rows because the trigger, recipient, and timing differ. The register does not collapse them.
- **Third-party cyber obligations.** NYDFS §500.11, the Interagency Guidelines third-party expectations, and DORA Article 28 each impose distinct third-party security obligations; the register surfaces them rather than rolling them into a generic "vendor security" row.
- **Authentication and customer-protection cyber overlap.** FFIEC authentication guidance interacts with Reg E error-resolution and unauthorized-transfer obligations; the register treats these as separate but cross-referenced rows.

#### What does not belong here

- Bank capital and credit obligations. Cyber overlay is for information-security obligations; load `banking` for capital and credit.
- Privacy obligations beyond information security (notice and choice, data-subject rights, advertising-data use). Load the privacy cross-cutting overlay for those.
- Internal firm policy, security-control library, or specific control procedures. Those go in `references/firm-overlay.md` or in control-matrix output, not in the obligation register.

## privacy

### Cross-cutting overlay: privacy — obligation-mapping

Loaded when the scope includes `privacy` in `cross_cutting_overlay_set`, or when the source being mapped is privacy-anchored. Adds privacy-specific source labels and obligation patterns when the register scopes processes that touch nonpublic personal information, consumer financial information, or other regulated personal data. Does not change the row spine.

The privacy overlap with cyber is real but distinct: cyber covers information-security obligations on the system, privacy covers obligations on the data and the consumer relationship. Both overlays often load together; each carries its own rows.

#### Sources the register may cite

##### Federal financial-services privacy

- Gramm-Leach-Bliley Act privacy provisions, 15 U.S.C. §6801 et seq., implemented through:
  - CFPB Reg P, 12 CFR Part 1016. §1016.4 (initial privacy notice), §1016.5 (annual notice), §1016.10 (limits on disclosure to nonaffiliated third parties), §1016.13 (exception for service providers), §1016.15 (other exceptions).
  - FTC Privacy Rule (16 CFR Part 313) for non-bank financial institutions under FTC jurisdiction.
  - Functional-regulator equivalents (12 CFR Part 332 FDIC, 12 CFR Part 216 FRB, 12 CFR Part 1016 CFPB).
  - Use for: notice obligations, opt-out obligations, third-party-sharing limits.
  - Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1016

- GLBA Safeguards Rule (FTC, 16 CFR Part 314 amended 2021/2023). §314.4 (information security program elements including encryption, MFA, vendor oversight). [verify section labels against current edition.]
  - Use for: information-security-program obligations under privacy framing; cross-load with cyber overlay where the engagement also covers cyber.
  - Link: https://www.ftc.gov/legal-library/browse/rules/safeguards-rule

- Fair Credit Reporting Act, 15 U.S.C. §1681 et seq.; Reg V, 12 CFR Part 1022.
  - §1022.20 (FCRA accuracy and integrity), §1022.40 (Affiliate Marketing Rule), §1022.80 (Disposal Rule), §1022.90 (Address Discrepancy Rule), §1022.123 (Identity Theft Red Flags Rule).
  - Use for: consumer-report-related privacy obligations; the Disposal Rule and Red Flags Rule are the most-cited rows.
  - Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1022

##### State privacy laws

- California Consumer Privacy Act / California Privacy Rights Act (Cal. Civ. Code §1798.100 et seq., as amended by CPRA).
  - §1798.100 (right to know), §1798.105 (right to delete), §1798.106 (right to correct), §1798.110 (right to access), §1798.120 (right to opt out of sale or sharing), §1798.121 (right to limit use of sensitive personal information).
  - Use for: California-resident-data obligations; covered businesses determined by §1798.140 thresholds.
  - Note: financial-information exemption under §1798.145(e) for data subject to GLBA; the exemption has limits, particularly for breach-notification obligations and pixel-tracking guidance.
  - Link: https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CIV&title=1.81.5

- Other state privacy laws. Virginia VCDPA (Va. Code §59.1-575 et seq.), Colorado CPA, Connecticut CTDPA, Utah UCPA, Texas TDPSA, and the additional state laws enacting in 2024-2026.
  - The register names each state where the entity has covered residents and notes the GLBA-data exemption posture per state.

##### Health and other adjacents

- HIPAA for health-affiliated financial entities (45 CFR Parts 160, 162, 164).
  - Use for: PHI obligations on health insurers, FSAs, HSAs administered by financial institutions.

- Children's Online Privacy Protection Act, 16 CFR Part 312.
  - Use for: COPPA obligations where the financial institution offers a child-directed service.

##### EU and UK privacy

- General Data Protection Regulation (Regulation (EU) 2016/679).
  - Articles 5 (principles), 6 (lawfulness of processing), 13-14 (information to data subjects), 17 (erasure), 28 (processor obligations), 30 (records of processing), 32 (security of processing), 33-34 (breach notification).
  - Use for: EU-personal-data obligations; the register names the controller and processor relationships per row.

- UK GDPR and Data Protection Act 2018.
  - Equivalent obligation set with UK-specific implementation.

#### Obligation patterns the practitioner expects to find

- **Notice and choice rows.** GLBA Reg P initial and annual notices; CCPA notice-at-collection; GDPR Articles 13-14 information requirements. Each is a distinct obligation row with its own trigger and content requirement.
- **Data-subject-rights rows.** CCPA rights, GDPR Articles 15-22 rights, and FCRA dispute and access rights extract as separate rows because the response timeline and substantive scope differ.
- **Third-party data-sharing rows.** GLBA §1016.10 disclosure limits, CCPA opt-out-of-sale-or-sharing, and GDPR Article 28 processor terms each impose distinct third-party-related obligations.
- **Breach- and incident-notification rows.** State breach-notification laws (covering both financial and non-financial data depending on exemption posture), GDPR Articles 33-34, NYDFS §500.17, the federal banking 36-hour rule. Each row names the trigger, recipient, and window.
- **Records-of-processing and assessment rows.** GDPR Article 30 records, CCPA risk-assessment provisions [verify under CPRA regulations], and GLBA Safeguards Rule §314.4(d) risk-assessment requirements.
- **Sensitive-data and special-category rows.** CPRA sensitive personal information (§1798.121), GDPR Article 9 special categories. The register surfaces these as their own rows because the lawful-processing or use-limitation analysis is distinct.

#### What does not belong here

- Information-security control specifics. Those belong in cyber overlay rows or in control-matrix output. Privacy overlay covers what data must be protected and disclosed; cyber overlay covers how the system protects it.
- Marketing-conduct obligations beyond data-driven marketing. Those go to the conduct cross-cutting overlay.
- Internal firm policy and taxonomy. That goes in `references/firm-overlay.md`.
