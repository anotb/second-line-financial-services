# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay for attestation-pack

When the scope record flags `conduct` for the attestation pack, this overlay sets the conduct-attestation content for named pack sections. Conduct attestations surface at firms with consumer-facing businesses (sales-practices attestations, fair-lending self-assessments, suitability and best-interest attestations).

Loaded by: `attestation-pack/SKILL.md` when `scope.cross_cutting_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- FINRA supervisory rules: Rule 3110 (supervision), Rule 3120 (supervisory control), Rule 3130 (CEO certification), Rule 2111 (suitability), Rule 2090 (KYC).
- SEC Regulation Best Interest (17 CFR §240.15l-1) and Form CRS (17 CFR §240.17a-14) for broker-dealers.
- Investment Advisers Act Rule 204A-1 (Code of Ethics) and Rule 206(4)-7 (compliance).
- Equal Credit Opportunity Act (Regulation B, 12 CFR Part 1002) and Fair Housing Act for fair-lending attestation.
- CFPB UDAAP authority under Sections 1031 and 1036 of the Consumer Financial Protection Act.
- HMDA reporting under Regulation C (12 CFR Part 1003) for fair-lending data attestation.

#### What changes for conduct-flagged attestation packs

##### 1. FINRA Rule 3130 CEO certification

For FINRA member firms, Rule 3130 requires the CEO to certify annually that the firm has processes in place to establish, maintain, review, test, and modify policies and procedures reasonably designed to achieve compliance with applicable securities laws. The attestation pack supporting Rule 3130 typically:

- Anchors the assertion text to Rule 3130(b) explicitly.
- Carries process-owner and CCO sub-certifications on each substantive compliance area (supervision, suitability, KYC, anti-money-laundering, books and records, regulatory reporting).
- Surfaces the Rule 3120 supervisory-control report as an evidence-index entry.
- Carries CEO sign-off (this is the executive certification at the broker-dealer level).

##### 2. Reg BI and Form CRS attestation

For broker-dealers in scope of Regulation Best Interest, attestations on Reg BI compliance frequently surface as part of the annual compliance review or as a discrete artifact. The attestation pack typically:

- Anchors to Reg BI's four obligations (disclosure, care, conflict of interest, compliance) explicitly.
- Carries process-owner sub-certifications on each obligation.
- Surfaces Form CRS filing and delivery process attestations.

##### 3. Fair-lending self-assessment

For lenders subject to ECOA (Reg B) and the Fair Housing Act, fair-lending self-assessments are recurring attestations frequently consumed by examiners and by the firm's board. The attestation pack typically:

- Anchors to ECOA / Reg B and to the firm's fair-lending policy.
- Covers the underwriting, pricing, marketing, servicing, and loss-mitigation phases.
- Carries the most recent statistical analysis (HMDA-data analysis where applicable; comparative-file review results) as evidence-index entries.
- Surfaces any disparate-treatment or disparate-impact findings as exceptions with linked issues.
- Carries Head of Fair Lending or CCO sign-off and routes to the board.

##### 4. Sales-practices and suitability attestation

For broker-dealers and investment advisers, sales-practices and suitability attestations surface periodically (annually or quarterly depending on firm policy). The attestation pack typically:

- Covers the suitability-determination process, the supervisory review structure, and the exception-handling flow.
- Surfaces sample-test results from the supervisory review as evidence-index entries.
- Reflects findings from the most recent independent-testing exercise.
- Carries CCO sign-off.

##### 5. UDAAP attestation linkages

For consumer-finance firms supervised by the CFPB (or state-level analogs), UDAAP-program attestations frequently surface. The attestation pack typically:

- Covers the UDAAP risk assessment, the complaint-handling process, the marketing review process, and the third-party oversight (UDAAP risk extends to service providers under Section 1031).
- Surfaces complaint trends and root-cause analysis as evidence-index entries.
- Reflects any consent orders, MRAs, or regulatory findings on UDAAP topics as current or prior-period exceptions.

##### 6. Sign-off and review machinery

Conduct attestation packs typically include the Chief Compliance Officer, the Head of Fair Lending (where the firm has one), the General Counsel, the Chief Audit Executive, and the CEO or business-unit head at the executive layer. Routing depends on the artifact: Rule 3130 to FINRA-relevant senior management; fair-lending self-assessments to the board (typically Audit Committee or a dedicated Fair Lending Committee); UDAAP attestations to CCO and the board's risk or audit committee.

#### Verification flags

- FINRA Rule 3130(b) — confirm current text and any FINRA-issued guidance.
- Reg BI — confirm any SEC staff guidance updates at pack-write time.
- Reg B / ECOA — confirm any CFPB rulemaking updates affecting fair-lending data collection or analysis.

## cyber

### Cyber cross-cutting overlay for attestation-pack

When the scope record flags `cyber` for the attestation pack, this overlay sets the cyber-control-attestation content for named pack sections. Cyber-control attestations are a frequent use case (annual CISO certifications, NYDFS Form B, AOC for card-handling, CSF-aligned program attestations); the overlay lands as content in the pack rather than as background reading.

Loaded by: `attestation-pack/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NYDFS 23 NYCRR Part 500, especially §500.17(b) (annual notice of compliance, post-Second-Amendment Form B). Verify section labels at pack-write time.
- NIST Cybersecurity Framework 2.0 (February 2024) for governance and risk-management framing.
- FFIEC IT Examination Handbook (Information Security and Cybersecurity sections) for federally supervised banking organisations.
- PCI DSS v4.0 / v4.0.1 Attestation of Compliance for card-handling entities.
- NAIC Insurance Data Security Model Law (Model #668) for state-licensed insurers in adopting jurisdictions.

#### What changes for cyber-flagged attestation packs

##### 1. Annual CISO certification structure

For NYDFS-covered entities, §500.17(b) (post-Second-Amendment) requires an annual written notice of compliance signed by the CISO and the highest-ranking executive (Form B) or a written acknowledgement of non-compliance. The attestation pack supporting Form B typically:

- Anchors the assertion text to §500.17(b) explicitly.
- Organises the control inventory by Part 500 section requirements (cybersecurity program, governance, access controls, incident response, multi-factor authentication, training, third-party service providers, and the asset-class-specific requirements at §500.7, §500.12, §500.14, §500.15).
- Surfaces non-compliance items as exceptions with the acknowledgement-of-non-compliance route documented where the firm cannot certify full compliance.
- Carries CISO and highest-ranking executive sign-off; legal review by GC office.

For non-NYDFS-covered entities, the parallel content uses the firm's CISO reporting structure under the relevant regulator's expectations (FFIEC for banks; SEC Reg S-P for advisers, BDs, transfer agents; NAIC Model #668 for state-licensed insurers in adopting jurisdictions).

##### 2. NIST CSF 2.0 control-inventory framing

Where the firm uses NIST CSF 2.0 as the cyber-control framework framing, the attestation pack control inventory organises by the six functions (Govern, Identify, Protect, Detect, Respond, Recover) rather than by lifecycle or by regulator subsection. The Govern function (added in CSF 2.0) covers organisational policies, roles and responsibilities, risk-management strategy, supply-chain risk, and policies and procedures; the Govern function attestation typically includes board-oversight evidence and the firm's risk-tolerance setting.

##### 3. PCI DSS Attestation of Compliance

For card-handling entities, the AOC is itself the attestation pack output. The skill structures the underlying control inventory by the twelve PCI DSS requirements at v4.0 / v4.0.1, surfaces the cardholder-data environment (CDE) boundary in the scope statement, and carries the QSA assessment as an evidence-index entry where applicable. The PCI DSS v4.0 transition (v3.2.1 retired March 31, 2024) may surface as exceptions for the new authentication and cryptographic requirements where firm-side implementation is in transition.

##### 4. Vendor-cyber posture as evidence

Cyber attestations frequently rely on vendor SOC 2 Type II reports as evidence for outsourced control coverage. The standard SOC-report-reliance discipline applies: review carve-outs, identify CUECs, and provide CUEC-level evidence at the user firm. A cyber attestation that cites vendor SOC reports without the CUEC-level evidence is the failure mode the troubleshooting file calls out.

##### 5. CISO-program independence and resourcing

NYDFS §500.4 (CISO designation) and analogous regulatory expectations require CISO independence and resourcing. The attestation pack typically includes:

- A statement on CISO reporting line and independence from the business units the CISO oversees.
- A statement on cyber-program resourcing (budget, headcount, technology investment trend) as an evidence-index entry rather than in the assertion text.
- Material organisational changes affecting CISO independence in the period as a current-period exception or as a forward-looking item.

##### 6. Sign-off and review machinery

Cyber attestation packs typically include the CISO (signer for Form B and CISO-program assertions), the highest-ranking executive (co-signer for Form B; CEO or equivalent), the General Counsel (legal review), the Chief Audit Executive's information-security relationship lead (witness or independent-review role), and the board's risk or audit committee chair (acknowledgement of receipt for the annual cyber report).

#### Verification flags

- NYDFS Part 500 §500.17(b) Form B requirements — verify post-Second-Amendment text and any DFS-issued FAQs at pack-write time.
- PCI DSS version — verify v4.0 vs v4.0.1 and current AOC form.
- NIST CSF 2.0 — confirm function and category mapping if the firm has adopted a tailored crosswalk.
- NAIC Model #668 adoption — verify state-by-state for insurance carriers in scope.

## privacy

### Privacy cross-cutting overlay for attestation-pack

When the scope record flags `privacy` for the attestation pack, this overlay sets the privacy-attestation content for named pack sections. Privacy-control attestations surface where the scoped process touches consumer financial information; the GLBA Safeguards Rule annual report is the recurring use case for nonbank financial institutions in scope.

Loaded by: `attestation-pack/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- GLBA Safeguards Rule, 16 CFR §314.4(g) (annual report to board) for FTC-regulated nonbank financial institutions. Verify section labels post-2021/2023 amendments.
- GLBA Privacy Rule (Regulation P, 12 CFR Part 1016 for CFPB-supervised; 16 CFR Part 313 for FTC-supervised) for consumer privacy notice obligations.
- Consumer Financial Protection Bureau information-security expectations under UDAAP authorities.
- State privacy laws where applicable (CCPA/CPRA, CDPA, CTDPA, others; verify the firm's footprint at pack-write time).

#### What changes for privacy-flagged attestation packs

##### 1. GLBA Safeguards Rule annual report

For nonbank financial institutions in FTC-supervised scope, §314.4(g) requires the qualified individual (CISO-equivalent) to report at least annually in writing to the board or governing body on the information-security program. The annual report covers:

- Overall status of the information-security program and compliance with the Safeguards Rule.
- Risk assessment results and any changes since the prior assessment.
- Service-provider arrangements and oversight.
- Testing and monitoring results.
- Security events and the firm's response.
- Recommendations for changes to the program.

The attestation pack supporting the §314.4(g) report typically:

- Anchors the assertion text to §314.4(g) explicitly.
- Organises the control inventory by Safeguards Rule elements (designation of qualified individual; risk assessment; access controls; encryption; multi-factor authentication; secure disposal; change management; incident response; service-provider oversight; training).
- Surfaces security events under §314.4(j) (the 2023 amendment's breach-notification requirement) where applicable.
- Carries qualified-individual sign-off and routes to the board or governing body.

##### 2. Banking-organisation privacy attestation

For banking organisations supervised by the federal banking agencies, the parallel privacy-attestation content sits within the broader information-security program attestation under FFIEC IT Examination Handbook expectations. The attestation pack typically integrates the privacy elements (consumer privacy notice accuracy, opt-out processes, third-party-sharing oversight under Reg P) into the broader information-security program rather than as a standalone artifact.

##### 3. State-privacy-law attestation linkages

Where the firm operates in states with comprehensive privacy laws (CCPA/CPRA in California; VCDPA in Virginia; CTDPA in Connecticut; others), state-privacy-law obligations surface in the attestation. These typically include:

- Consumer-rights-handling processes (right to know, right to delete, right to opt out of sale or sharing).
- Data-protection assessments (DPAs) where the law requires them.
- Sensitive-data-processing controls.
- Service-provider contractual flow-downs.

State privacy laws do not generally require a regulator-filed attestation, but firm-policy attestation frequently covers them. The attestation pack treats state-privacy-law obligations as control-inventory rows rather than as a separate artifact.

##### 4. Material-event linkage

Privacy-related security events that meet the §314.4(j) threshold (Safeguards Rule), the SEC Reg S-P customer-notification threshold, the HIPAA Breach Notification Rule threshold, or state breach-notification thresholds surface as exceptions in the attestation period. The pack typically:

- Lists each event with the regulator-notification status, the customer-notification status, and the linked issue ID.
- Carries the firm's response and remediation status.
- Reflects any material findings in the assertion text as a carve-out where the response is incomplete.

##### 5. Sign-off and review machinery

Privacy attestation packs typically include the qualified individual (CISO-equivalent for Safeguards Rule), the Chief Privacy Officer (where the firm has one), the General Counsel (legal review), the Chief Compliance Officer, and the board or governing body as the recipient of the annual report.

#### Verification flags

- GLBA Safeguards Rule §314.4(g) and §314.4(j) — verify post-2021/2023 amendments.
- State privacy laws — verify the firm's footprint and the in-force compliance dates at pack-write time.
- HIPAA Breach Notification Rule applicability — verify entity classification (covered entity, business associate) where health-information processing is in scope.
