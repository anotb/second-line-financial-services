# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — control-matrix

Loads when the scope `sector_overlay_set` includes `banking`. Binds matrix construction to bank-supervisory expectations.

#### Supervisory frame

US bank examiners (OCC, FRB, FDIC) read control matrices line-by-line during safety-and-soundness, BSA/AML, and consumer-compliance examinations. The matrix is rarely the sole evidence for a control rating, but it is the navigation device that organises everything else (policies, procedures, sample testing, exception logs, committee minutes). A matrix that an examiner cannot follow row-by-row is a finding waiting to happen.

State-member banks share supervision between the FRB and the state banking department; the matrix may need to evidence both supervisor's frames. National banks and federal savings associations sit with the OCC. State non-member banks sit with the FDIC and the state. The matrix author knows which constellation applies.

#### Heightened standards architecture

For OCC large-bank populations covered by 12 CFR Part 30 Appendix D, the matrix carries rows for:

- The CRO independence model (named role, reporting line to the board risk committee, dual reporting if the firm uses it).
- The risk governance framework documentation (current version, approval history, board attestation).
- The risk-appetite-statement controls (board approval, breach-and-escalation framework, KRI alignment).
- The limits framework (front-line-unit, line-of-business, and aggregate limits, breach-and-escalation evidence).
- The independent-risk-management coverage map (what the second line independently challenges, what is read-only oversight, what is co-developed).

These rows do not appear in matrices for non-Heightened-Standards banks; the scope's institution profile drives the inclusion.

#### FFIEC IT booklet integration

When the matrix scopes a process touching information systems (most do), the FFIEC IT Examination Handbook booklets frame the technology-control rows. Information Security booklet (governance, logical access, change management); Audit booklet (independence and audit-program design); Outsourcing Technology Services / Third-Party booklets (where the technology service is provided by a third party). The cyber cross-cutting overlay is the substantive content; this sector overlay simply confirms the FFIEC frame is the bank-side reading.

#### Consumer-compliance and CRA triggers

When the matrix scopes a lending process, two banking-specific control families enter:

- **Fair-lending and ECOA / Reg B controls** — adverse-action notice content and timing (12 CFR §1002.9), prohibited-basis monitoring, exception-and-override review, comparator-file analysis where the firm performs it. The CFPB and the prudential supervisor both probe these.
- **CRA controls** — for banks subject to CRA, the matrix carries rows on CRA performance evaluation evidence, assessment-area controls, and small-business / small-farm / community-development data accuracy. The scope of CRA controls varies by the bank's CRA size category.
- **HMDA controls** — data accuracy, scrubbing and validation, LAR submission and resubmission controls. HMDA is Reg C; the matrix references the rule and the FFIEC HMDA Examiner Transmittal.

Consumer-compliance rows live in their own matrix block under a CMS lens (board-and-management oversight, compliance program, complaint response, compliance audit), keyed to the CFPB CMS framing.

#### BSA / AML controls

When the matrix scopes a process where BSA applies (which is most customer-facing processes at most banks), the matrix carries rows for:

- The four pillars (board-approved BSA program, designated BSA officer, training, independent testing).
- CDD / EDD controls under FinCEN's Customer Due Diligence Rule (31 CFR §1010.230).
- Transaction-monitoring scenario-tuning and disposition controls.
- SAR-filing controls (timeliness, supervisory review, narrative quality), with the SAR filing itself excluded from the matrix evidence (SAR confidentiality under 31 USC §5318(g) prohibits documenting that a SAR was filed).
- CTR controls.
- OFAC / sanctions screening controls.

The BSA / AML control block is sometimes sufficiently large that it carries its own matrix (separate `matrix_id`) cross-referenced to the parent.

#### Recordkeeping and retention

- Bank Service Company Act, 12 USC §1867(c): examiner-access expectations for third-party-provided services. Vendor-control rows reference the contract clause that gives the examiner access; if the clause is missing, the matrix surfaces a coverage gap.
- 12 CFR Part 1010 (FinCEN BSA recordkeeping): five-year retention floor for BSA records. The evidence-pointer expected window respects the five-year floor.

#### Sign-off and review-gate norms

Bank-side matrices are reviewed by a named role keyed to the matrix scope: the BSA officer for BSA matrices, the chief compliance officer for consumer-compliance matrices, the chief risk officer (or the head of model risk under SR 11-7 matrices) for risk matrices, the chief credit officer for credit-risk matrices. Internal-audit reviews the matrix as part of its own scoping and references it in the audit workpapers; internal audit does not own the matrix.

#### Anchors used by this overlay

- 12 CFR Part 30 Appendix D — OCC Heightened Standards [verify section labels].
- FFIEC IT Examination Handbook (Information Security, Audit, Outsourcing Technology Services booklets) [verify booklet revision dates].
- 12 CFR Part 1002 — Regulation B (ECOA implementation).
- 12 CFR Part 1003 — Regulation C (HMDA implementation).
- 12 CFR Part 25 / Part 228 / Part 345 — CRA implementing regulations (OCC / FRB / FDIC).
- 31 CFR §1010.230 — FinCEN Customer Due Diligence Rule.
- 31 CFR §1020 series — FinCEN bank-specific BSA rules.
- 31 USC §5318(g) — SAR confidentiality.
- 12 USC §1867(c) — Bank Service Company Act examiner access.
- CFPB Supervision and Examination Manual — CMS chapter [verify section labels].

## capital-markets

### Capital-markets sector overlay — control-matrix

Loads when the scope `sector_overlay_set` includes `capital-markets`. Binds matrix construction to SEC, FINRA, and CFTC examination expectations for broker-dealers, investment advisers, registered funds, and futures-market participants.

#### Supervisory frame

SEC Division of Examinations and FINRA Member Supervision examine against named rule references; the matrix is read against the rule, not against a paraphrase. The rule citation in the obligation-source column is the navigation device for both the firm and the examiner. CFTC and NFA examinations follow a similar pattern for futures and swaps participants.

The character of the matrix differs by registration:

- **Broker-dealer matrices** anchor on FINRA supervision (Rule 3110), books-and-records (SEA §17(a) / Rules 17a-3 / 17a-4 / FINRA 4511), AML (FINRA 3310), communications (FINRA 2210), and the suitability and best-interest framework (FINRA 2111 / Reg BI).
- **Investment adviser matrices** anchor on the Advisers Act compliance program rule (Rule 206(4)-7) and its annual-review evidence, the custody rule (206(4)-2), the marketing rule (206(4)-1), and recordkeeping (Rule 204-2).
- **Registered fund matrices** anchor on the Investment Company Act compliance program rule (Rule 38a-1) and the fund's CCO report to the board.
- **CFTC-registrant matrices** anchor on the relevant Part 23 (swap dealers), Part 30 (foreign futures intermediaries), and Part 4 (commodity pool operators) controls.

#### Annual-review machinery (advisers and funds)

Adviser matrices are bound to the annual-review cycle under Rule 206(4)-7. The matrix supports the CCO's annual-review report; testing rows in the matrix document the CCO-led testing for the year, the deficiencies identified, and the remediation evidence. Fund matrices serve the same function under Rule 38a-1, with the CCO reporting to the fund board at least annually.

The annual-review character drives matrix cadence: a broker-dealer matrix may be refreshed only on supervisory or material-change triggers, while an adviser matrix is expected to refresh annually with documented testing.

#### Books-and-records controls

The recordkeeping rules are sharp and the matrix cites them precisely:

- 17 CFR §240.17a-3 — record creation requirements (broker-dealers).
- 17 CFR §240.17a-4 — record retention; most categories six years (first two readily accessible). The 2022 amendment introduced an electronic-recordkeeping audit-trail option as an alternative to write-once-read-many storage.
- FINRA Rule 4511 — general books-and-records retention, six years unless a specific rule sets a different period.
- 17 CFR §275.204-2 — Investment Advisers Act recordkeeping; most records five years (first two on-premises).
- 17 CFR §1.31 — CFTC recordkeeping; five years from creation, with electronic-storage standards.

Matrices for processes touching records under these rules carry retention-control rows; the evidence pointer's expected retention window respects the rule, not the firm's policy summary of the rule.

#### Marketing and communications controls

Broker-dealer matrices for communications-with-the-public processes carry FINRA 2210 controls (principal review, filing requirements for member-firm-prepared retail communications, recordkeeping). Adviser matrices carry Rule 206(4)-1 (the marketing rule) controls: testimonial and endorsement evidence, performance-presentation controls (gross-and-net, time-period, hypothetical-performance disclosures), and review-and-recordkeeping controls.

#### Best-interest and suitability controls

Broker-dealer matrices for retail-account processes carry Reg BI (17 CFR §240.15l-1) controls: care, disclosure, conflict-of-interest, and compliance obligations. Adviser matrices for retail-account processes carry the fiduciary-duty framework (SEC Interpretation Regarding Standard of Conduct for Investment Advisers, June 2019) and Form CRS controls.

#### AML controls

FINRA 3310 sets the broker-dealer AML program elements; the matrix carries rows for the four pillars and for the FinCEN CDD Rule (31 CFR §1010.230) integration. Where the broker-dealer is part of a bank holding company, the matrix may inherit transaction-monitoring controls from the bank's BSA program; the inheritance and the firewall between the two are themselves matrix-recordable.

#### Sign-off and review-gate norms

Adviser matrices are signed by the CCO (named under Rule 206(4)-7); fund matrices by the fund CCO under Rule 38a-1. Broker-dealer matrices for supervisory-program processes are signed by the principal-supervisor designated under FINRA 3110; broker-dealer AML matrices by the AML compliance officer designated under FINRA 3310. CFTC-registrant matrices are signed by the chief compliance officer designated under the relevant Part regulation.

#### Anchors used by this overlay

- 17 CFR §240.15l-1 — Regulation Best Interest.
- 17 CFR §240.17a-3 and §240.17a-4 — broker-dealer recordkeeping.
- 17 CFR §275.204-2 — Investment Advisers Act recordkeeping.
- 17 CFR §275.206(4)-7 — Advisers Act compliance program rule.
- 17 CFR §275.206(4)-1 — Advisers Act marketing rule.
- 17 CFR §275.206(4)-2 — Advisers Act custody rule.
- 17 CFR §270.38a-1 — Investment Company Act fund compliance program rule.
- 17 CFR §1.31 — CFTC recordkeeping.
- FINRA Rule 2111 — suitability.
- FINRA Rule 2210 — communications with the public.
- FINRA Rule 3110 — supervision.
- FINRA Rule 3310 — AML compliance program.
- FINRA Rule 4511 — books and records, general retention.
- 31 CFR §1010.230 — FinCEN Customer Due Diligence Rule (applies to broker-dealers as covered financial institutions).

## insurance

### Insurance sector overlay — control-matrix

Loads when the scope `sector_overlay_set` includes `insurance`. Binds matrix construction to state-DOI and NAIC-framework expectations.

#### Supervisory frame

State Departments of Insurance run market-conduct examinations (claims-handling, underwriting, rating, marketing, producer licensing) and financial examinations (solvency, reserves, reinsurance, corporate governance) under state law and the NAIC handbooks. Multistate examinations are coordinated under the NAIC framework with a lead state. The matrix is read by the examiner-in-charge during fieldwork; the binding-state version of the standard governs where state-specific amendments diverge from the NAIC model.

NAIC accreditation drives a baseline set of standards across adopting states. Most insurance-side matrices anchor on the NAIC model for the substantive control objective and reference the adopting-state rule for enforcement.

#### Internal-control reporting (Model Audit Rule)

For insurers above the premium threshold under the NAIC Model Audit Rule (Model #205), §16 sets internal-control-over-financial-reporting expectations comparable to SOX 404 for non-accelerated filers. Matrices for ICFR-in-scope financial-reporting processes carry rows that the firm's external auditor will read against; the matrix taxonomy aligns to the COSO 2013 components by default, with the firm's MAR §16 attestation as the downstream artifact.

#### ORSA controls

Insurers in ORSA-adopting states file an annual ORSA Summary Report under the NAIC Risk Management and ORSA Model Act (Model #505). The matrix supporting an ORSA program covers: governance and risk-culture controls, the firm's risk-and-capital integration controls, the stress-testing and scenario-analysis controls, and the board-and-committee review controls. ORSA is principle-based; the matrix carries firm-side responses tied to each ORSA section, not a recital of the model act.

#### Market-conduct controls

When the matrix scopes a claims, underwriting, rating, marketing, or producer-licensing process, the relevant NAIC handbook (Market Conduct Examiners Handbook) frames the control rows. Specific control families:

- **Claims-handling controls** — timeliness (Unfair Claims Settlement Practices Act, NAIC Model #900, as adopted), reserve adequacy at first notice of loss, claim-investigation documentation, denial-letter content, complaint-trigger flags. State-specific timing thresholds drive the operating-effectiveness measurement.
- **Underwriting and rating controls** — actuarial-justification documentation, rate-filing controls (where state law requires prior approval), nondiscrimination controls (where state law prohibits specific risk factors), and underwriting-judgment override review.
- **Suitability and replacement controls (life and annuities)** — NAIC Suitability in Annuity Transactions Model Regulation (Model #275) controls, replacement controls (NAIC Model #613), and best-interest-standard controls in adopting states.
- **Producer-licensing controls** — appointment, termination, continuing-education tracking, and §501 "knowledge of cause for termination" reporting.
- **Privacy notice controls** — NAIC Insurance Information and Privacy Protection Act (Model #672), GLBA-aligned.

#### Financial-examination controls

When the matrix scopes a process that is examined under the Financial Condition Examiners Handbook, the control rows align to the handbook's risk-focused framework: identification of inherent risk in the process, identification of mitigating controls, evaluation of control design and operating effectiveness, and conclusion on residual risk. The matrix is the firm-side evidence of the second step (mitigating controls) and the third step (effectiveness).

#### Holding-company controls

For insurance groups under the NAIC Insurance Holding Company System Regulatory Act (Model #440) and Regulation (Model #450), the matrix may scope holding-company-level oversight controls: Form B and Form F filing controls, intercompany-transaction approval controls, and group-wide enterprise-risk-management controls keyed to ORSA.

#### Sign-off and review-gate norms

Market-conduct matrices are reviewed by the chief compliance officer; financial-exam matrices by the chief financial officer or chief risk officer; ICFR matrices by the controller or chief accounting officer with sign-off from the audit committee. ORSA matrices are reviewed by the CRO and tabled at the board risk committee.

#### Anchors used by this overlay

- NAIC Model Audit Rule (Model #205) §16 — internal control over financial reporting [verify section].
- NAIC Risk Management and ORSA Model Act (Model #505) [verify section labels].
- NAIC Market Conduct Examiners Handbook [verify section labels].
- NAIC Financial Condition Examiners Handbook [verify section labels].
- NAIC Unfair Claims Settlement Practices Act (Model #900) [verify state-specific adoption].
- NAIC Suitability in Annuity Transactions Model Regulation (Model #275) [verify section labels].
- NAIC Insurance Holding Company System Regulatory Act (Model #440) and Regulation (Model #450) [verify section labels].
- NAIC Insurance Information and Privacy Protection Act (Model #672).
- State adopting statutes and bulletins — verify per binding state.

## payments-fintech

### Payments and fintech sector overlay — control-matrix

Loads when the scope `sector_overlay_set` includes `payments-fintech`. Binds matrix construction to bank-partnership, money-transmitter, and payment-network supervisory expectations.

#### Supervisory frame

The supervisory map for fintechs splits by structure:

- **Direct-chartered fintech bank** — supervised under the bank overlay (use `banking.md` instead of or in addition to this file). The matrix is read by the bank's primary federal regulator and any state.
- **Sponsor-bank-partnership fintech** — examined indirectly through the sponsor bank under the interagency third-party guidance (June 2023). The matrix may need to evidence the partner-bank-side controls and the fintech-side controls; the scope names which side the matrix represents. The OCC's bank-partnership posture has tightened since 2023 and matrix rows for sponsor-bank oversight controls are increasingly examiner-probed.
- **Non-bank fintech with state money-transmitter licenses** — examined state-by-state under the NMLS framework. The matrix is read by state DFS examiners; common-state coordination via the NMLS State Coordinating Committee for multistate exams.
- **Card-network participant** — additional rule-set from network operating rules (Visa, Mastercard, Discover, Amex), PCI DSS, and (for MSBs) FinCEN.
- **CFPB larger-participant** — larger-participant rules under Dodd-Frank §1024 extend CFPB direct examination to fintechs above the size threshold for the relevant market (general-purpose consumer reporting, consumer-debt collection, student-loan servicing, international money transfer, automobile financing, larger-participant general-use prepaid card).

#### Sponsor-bank-relationship controls

Where the matrix scopes a sponsor-bank-partnership process, the rows split between bank-side oversight controls and fintech-side operating controls:

Bank-side oversight controls (bank's TPRM matrix on this fintech):
- Criticality-determination control.
- Initial and ongoing due-diligence controls.
- Contract-clause controls (right to audit, examiner access via 12 USC §1867(c), data ownership, exit, BSA cooperation).
- Ongoing-monitoring controls (KRI review, complaint review, BSA-program oversight, periodic on-site or virtual reviews).
- Termination and exit-plan controls.

Fintech-side operating controls (fintech's own matrix):
- BSA program controls (where MSB-registered): four pillars, transaction monitoring, SAR filing, CTR.
- Reg E error-resolution controls (12 CFR §1005.11): timing (10 days for provisional credit, 45 or 90 days for resolution), notice content, recordkeeping (two-year retention).
- Reg Z disclosure controls for credit products (12 CFR §1026): TILA disclosures, periodic-statement controls, billing-error resolution.
- UDAAP controls: marketing-claim review, complaint-trigger response, fee-disclosure controls.
- Complaint-handling controls: intake, categorisation, response, root-cause review.
- PCI DSS attestation controls (where card data is handled): annual SAQ or ROC, QSA findings remediation, scope-creep monitoring.

#### Money-transmitter-license controls

When the matrix scopes a state money-transmitter-licensed activity, the row set covers:

- Licensing maintenance controls: NMLS filings, state-specific reporting, surety-bond maintenance.
- Permissible-investment controls: state-specific permissible-investments rules, the matching to outstanding obligations, and the periodic attestation.
- Customer-fund safeguarding controls: segregation of customer funds, daily-reconciliation controls.
- BSA controls per the FinCEN MSB rules (31 CFR §1022 series).
- State-specific reporting controls (e.g., CDFI reporting, CRA-equivalent reporting for state-chartered MSBs in adopting states).

The Conference of State Bank Supervisors' Money Services Businesses Model Money Transmission Modernization Act (MTMA) is gradually adopted; check the binding-state version.

#### Network and PCI controls

Card-network participants carry network-rule controls separate from regulator controls. The matrix may include rows for:

- Chargeback and dispute controls (network-specific timing and documentation rules).
- Tokenisation and authorisation controls (network-specific vault and token-service-provider relationships).
- PCI DSS v4.0 controls — the matrix references the firm's SAQ or ROC and the QSA's findings; the granular PCI control set typically lives in the firm's PCI-program documentation rather than the regulator-facing matrix.

#### CFPB direct supervision

For larger-participant fintechs and for fintechs the CFPB has elected to supervise under §1024(a)(1)(C) (risk-based supervision), the matrix is read against the CFPB Supervision and Examination Manual chapters that apply. CMS pillars (board and management oversight, compliance program, complaint response, compliance audit) anchor the matrix; product-specific chapters drive substantive control rows.

#### Recordkeeping and retention

- 31 CFR §1010.430 — FinCEN general recordkeeping (five-year floor for BSA records).
- 31 CFR §1022 series — MSB-specific FinCEN rules.
- 12 CFR §1005 — Reg E (two-year retention for error-resolution records).
- 12 CFR §1026 — Reg Z (two-year retention for credit-disclosure evidence).
- PCI DSS v4.0 — log retention typically one year online with three months immediately available; varies by control.
- State-specific retention varies; common pattern is the longer of three years or state-specific window.

#### Sign-off and review-gate norms

Sponsor-bank matrices for fintech-partnership oversight are signed by the bank's BSA officer or chief compliance officer. Fintech-side matrices are signed by the fintech's BSA officer (where MSB-registered), CCO, or both depending on scope. Network-rule matrices are signed by the head of payments operations.

For BaaS arrangements specifically, the matrix may need to evidence both sides; the scope record names which side this matrix represents.

#### Anchors used by this overlay

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023).
- 31 CFR §1010.430 — FinCEN general recordkeeping.
- 31 CFR §1022 series — MSB-specific FinCEN rules.
- 31 CFR §1010.230 — FinCEN Customer Due Diligence Rule.
- 12 CFR §1005 — Reg E (Electronic Fund Transfers Act implementation).
- 12 CFR §1026 — Reg Z (Truth in Lending Act implementation).
- Dodd-Frank Act §1024 — CFPB supervisory authority over larger participants.
- 12 USC §1867(c) — Bank Service Company Act examiner access (operative for sponsor-bank fintech relationships).
- PCI DSS v4.0 — current version of the Payment Card Industry Data Security Standard.
- CSBS Money Services Businesses Model Money Transmission Modernization Act [verify state-specific adoption].
