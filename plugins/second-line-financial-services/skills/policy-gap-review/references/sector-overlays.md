# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — policy-gap-review

Loads when the scope `sector_overlay_set` includes `banking`. Binds policy gap reviews to bank-supervisory expectations on the firm's policy framework.

#### Supervisory frame

US bank examiners (OCC, FRB, FDIC) read policies as evidence of the firm's governance posture. The policy is rarely the sole evidence for any control rating, but a policy gap is a finding the supervisor will probe in fieldwork because it is the cheapest finding to issue: the policy text is the artefact, the benchmark text is the source, the gap reads itself. Policy refreshes ahead of examination cycles are routine; the gap matrix is the reviewer's sequencing tool.

State-member banks share supervision between the FRB and the state banking department; policy gap reviews may need to evidence both supervisor's frames. National banks and federal savings associations sit with the OCC. State non-member banks sit with the FDIC and the state.

#### Heightened standards architecture

For OCC large-bank populations covered by 12 CFR Part 30 Appendix D, the matrix benchmarks the firm's risk-governance policy and the suite of risk-type policies against the heightened-standards framework:

- The risk governance framework (RGF) policy. Standards II and III set expectations on the framework's content (risk taxonomy, risk-appetite linkage, three-lines-of-defense roles, board oversight architecture).
- The risk-appetite-statement (RAS) policy. Standard III.E expects the RAS to set quantitative limits and qualitative tolerances aligned with the strategic plan; gap-matrix rows on RAS-policy content are common in pre-2014 RAS policies that have not been refreshed.
- The strategic plan policy. Standard III.D expects a comprehensive written strategic plan covering at least three years.
- Independent-risk-management coverage policies. Standard IV expects the second-line function to be independent, sufficiently resourced, and have authority that the firm-wide policy makes explicit.
- Front-line-unit responsibilities policy. Standard IV.A expects the front-line unit to assess and address risks; gap rows fire on policies that delegate risk responsibility entirely to the second line.

Heightened-standards rows do not appear in policy gap reviews for non-Heightened-Standards banks; the scope's institution profile drives the inclusion.

#### OCC Bulletin 2014-39 framing

OCC Bulletin 2014-39 (Risk Governance for Banks) is the prudential supervisor's expectations document on policy-framework content for covered banks. The matrix benchmarks against the bulletin's expectations on:

- Board approval cadence and documentation.
- Policy-version control and document-management hygiene.
- Policy-to-RAS linkage and breach-and-escalation protocols.
- Policy ownership at the named-role level.

A policy gap matrix for a covered bank that does not benchmark against 2014-39 expectations is incomplete; the supervisor reads with the bulletin in hand.

#### Consumer-compliance and CRA triggers

When the policy in scope is a lending or consumer-facing policy, three banking-specific benchmark families enter:

- **Fair-lending and ECOA / Reg B** — adverse-action notice content (12 CFR §1002.9), prohibited-basis monitoring policy expectations, exception-and-override review policy expectations, comparator-file analysis policy expectations where the firm runs them. Comment 9(b)(2)-3 of the Official Staff Commentary requires the cited reasons to relate to and accurately describe the factors actually considered or scored, and is the operative anchor for adverse-action notices on AI/algorithmic decisioning. (CFPB Circular 2022-03, which restated this point for complex algorithms, was **withdrawn May 12, 2025; historical only**.) ML-decisioning policies remain a frequent gap site.
- **CRA** — for banks subject to CRA, the matrix benchmarks against CRA performance evaluation policy expectations, assessment-area policy expectations, and small-business / small-farm / community-development data accuracy policy expectations. The scope of CRA expectations varies by the bank's CRA size category.
- **HMDA** — Reg C policy expectations on data accuracy, scrubbing and validation, LAR submission and resubmission. The FFIEC HMDA Examiner Transmittal sets the supervisory expectations on data-quality controls and policy-framework anchoring.
- **Section 1071** — Reg B Subpart B (12 CFR Part 1002, Subpart B) small-business data collection policy expectations. **§1071 revised final rule, May 1, 2026: 1,000 covered transactions; effective June 30, 2026; compliance January 1, 2028** — supersedes the 2023 tiered phase-in schedule. The matrix benchmarks against the revised rule and against the firm's covered-FI status.

#### BSA / AML triggers

When the policy in scope is a BSA, AML, OFAC/sanctions, or financial-crime policy, the matrix benchmarks against:

- The four pillars (board-approved BSA program, designated BSA officer, training, independent testing) — explicit in the FFIEC BSA/AML Examination Manual.
- CDD / EDD policy expectations under FinCEN's CDD Rule (31 CFR §1010.230). Beneficial-ownership policy expectations are the most-cited 2018-onwards gap for legacy AML policies that pre-date the rule.
- SAR-filing policy expectations (timeliness, supervisory review, narrative quality) under 31 CFR §1020.320. SAR confidentiality under 31 USC §5318(g) constrains how the policy describes filing decisions; gap rows fire when the policy improperly references SAR contents in non-SAR sections.
- CTR policy expectations under 31 CFR §1010.310.
- OFAC sanctions screening policy expectations (the OFAC Framework for Compliance Commitments, May 2019).

The BSA/AML policy gap review is sometimes scoped as its own engagement; the matrix can carry a separate `review_id` cross-referenced to the parent enterprise policy gap review.

#### Sign-off and review-gate norms

Bank-side policy gap reviews are reviewed by a named role keyed to the matrix scope: the BSA officer for BSA/AML policies, the chief compliance officer for consumer-compliance policies, the chief risk officer (or the head of model risk under SR 11-7 / 2026-13 matrices) for risk-management policies, the chief credit officer for credit-risk policies, the CISO for cybersecurity policies. The compliance committee or the relevant board committee tables the recommended edits at the cadence the firm's framework requires.

#### Anchors used by this overlay

- 12 CFR Part 30 Appendix D — OCC Heightened Standards [verify section labels].
- OCC Bulletin 2014-39 — Risk Governance for Banks [verify section labels].
- FFIEC BSA/AML Examination Manual — current edition [verify chapter and section labels].
- 31 CFR §1010.230 — FinCEN Customer Due Diligence Rule.
- 31 CFR §1010.310 — FinCEN CTR rule.
- 31 CFR §1020.320 — FinCEN SAR rule for banks.
- 31 USC §5318(g) — SAR confidentiality.
- 12 CFR Part 1002 — Regulation B (ECOA implementation), including §1002.9 adverse-action notices.
- 12 CFR Part 1002 Subpart B — Section 1071 small-business data collection (**§1071 revised final rule, May 1, 2026: 1,000 transactions; effective June 30, 2026; compliance January 1, 2028** — supersedes the 2023 tiered schedule).
- 12 CFR Part 1003 — Regulation C (HMDA implementation).
- 12 CFR Part 25 / Part 228 / Part 345 — CRA implementing regulations (OCC / FRB / FDIC).
- CFPB Circular 2022-03 — Adverse Action Notice Requirements in Connection with Credit Decisions Based on Complex Algorithms (**withdrawn May 12, 2025; historical only**; Reg B §1002.9 and Comment 9(b)(2)-3 carry the obligation).
- OFAC Framework for OFAC Compliance Commitments (May 2019).

## capital-markets

### Capital markets sector overlay — policy-gap-review

Loads when the scope `sector_overlay_set` includes `capital-markets`. Binds policy gap reviews to capital-markets-supervisory expectations on the firm's compliance and supervisory policy framework.

#### Supervisory frame

Capital markets is federally supervised by the SEC for investment advisers (under the Investment Advisers Act of 1940), broker-dealers (under the Securities Exchange Act of 1934), and registered investment companies (under the Investment Company Act of 1940). FINRA self-regulates broker-dealers under a layer of FINRA rules that operate in parallel with SEC rules. State supervision applies for state-registered advisers and for broker-dealer agents.

Policy gap reviews in capital markets typically benchmark against the federal rules that explicitly impose written-policy or written-procedure obligations.

#### Investment Advisers Act framework

##### SEC Rule 206(4)-7 — Compliance Procedures and Practices

Anchor: 17 CFR §275.206(4)-7. The rule requires registered advisers to adopt and implement written policies and procedures reasonably designed to prevent violation of the Advisers Act, designate a Chief Compliance Officer, and review the adequacy of the policies annually. The matrix benchmarks an adviser's compliance policy framework against the rule and against the SEC EXAMS published examination priorities for the year. [verify the most-recent EXAMS priorities document.]

What the gap review picks up: legacy adviser policies that pre-date specific risk areas the SEC has subsequently flagged in EXAMS priorities (e.g., the Marketing Rule under amended Rule 206(4)-1, custody under Rule 206(4)-2, sustainability-related disclosures, off-channel communications, AI-system use in advisory decisioning).

##### SEC Marketing Rule — Rule 206(4)-1 (amended, effective November 2022)

Anchor: 17 CFR §275.206(4)-1. The amended rule replaced the prior advertising and cash-solicitation rules with a single principles-based marketing framework. Policy gap matrices for adviser marketing-review policies benchmark against the rule's seven prohibitions and the testimonial / endorsement / third-party-rating provisions. Frequent gap site for advisers that did not refresh marketing policy after the November 2022 compliance date.

##### SEC Custody Rule — Rule 206(4)-2

Anchor: 17 CFR §275.206(4)-2. Policy expectations on the segregation of client assets, qualified custodian use, surprise verifications, and the audit-exception alternative. The SEC has signalled rulemaking to expand custody to all client assets (the proposed Safeguarding Rule); the matrix benchmarks against the rule in force at the engagement's effective date.

#### Investment Company Act framework

##### SEC Rule 38a-1 — Compliance Procedures and Practices of Investment Companies

Anchor: 17 CFR §270.38a-1. Imposes written-compliance-policy and CCO designation expectations on registered investment companies (mutual funds, ETFs, closed-end funds). The fund-level CCO designation is parallel to but distinct from the adviser-level CCO designation under Rule 206(4)-7; fund-board oversight is a key feature. The matrix benchmarks fund compliance policies against Rule 38a-1 and against any applicable disclosure-rule policies (Rule 18f-4 derivatives, Rule 22e-4 liquidity risk management, Rule 30e-3 shareholder reports). [verify the operative numbering for any post-2020 amendments to the named rules.]

#### Broker-dealer framework

##### FINRA Rule 3110 — Supervision

Anchor: FINRA Rule 3110(a) supervisory system, 3110(b) written supervisory procedures, 3110(c) internal inspections, 3110(d) transaction review and investigation, 3110(e) qualifications investigated. The matrix benchmarks broker-dealer supervisory policies against the rule's content elements. [verify any sub-rule amendments since the consolidation of NASD Rules 3010 and 3012 into FINRA Rule 3110.]

##### FINRA Rule 4511 — General Books and Records

Anchor: FINRA Rule 4511 read with SEC Rules 17a-3 and 17a-4 (recordkeeping under the Exchange Act). Policy expectations on books-and-records, retention periods, and the post-2022 amendment to Rule 17a-4 on the electronic-storage standard. The matrix benchmarks recordkeeping policies against the rules in force at the engagement's effective date.

##### SEC Rule 15c3-5 — Market Access

Anchor: 17 CFR §240.15c3-5. Policy expectations on broker-dealers providing market access; pre-trade financial and regulatory risk-management controls. Frequent gap site for legacy market-access policies that have not been refreshed after the equity-options expansion of the rule's reach in subsequent SEC interpretive guidance.

#### EXAMS examination priorities

The SEC Division of Examinations publishes annual examination priorities. The matrix references the priorities for the engagement's effective year as a benchmark for emerging-area policy expectations the SEC has telegraphed it will probe. Policy gap rows often surface where firm policy lags the EXAMS priorities document.

#### Sign-off and review-gate norms

Capital-markets-side policy gap reviews are reviewed by the CCO (always, under Rules 206(4)-7 and 38a-1), with the chief legal officer, the chief operating officer, or the chief risk officer concurring as the matter scope requires. Fund-board oversight is required for fund compliance policies under Rule 38a-1; the matrix surfaces fund-board-tabling expectations explicitly when fund policies are in scope.

#### Anchors used by this overlay

- 17 CFR §275.206(4)-7 — Advisers Act Compliance Rule.
- 17 CFR §275.206(4)-1 — Advisers Act Marketing Rule (amended November 2022).
- 17 CFR §275.206(4)-2 — Advisers Act Custody Rule.
- 17 CFR §270.38a-1 — Investment Company Act Compliance Rule.
- 17 CFR §270.18f-4 — Investment Company Act derivatives risk management.
- 17 CFR §270.22e-4 — Investment Company Act liquidity risk management.
- 17 CFR §240.17a-3 — broker-dealer recordkeeping.
- 17 CFR §240.17a-4 — broker-dealer record retention (amended 2022).
- 17 CFR §240.15c3-5 — broker-dealer market access.
- FINRA Rule 3110 — Supervision [verify sub-rule amendments].
- FINRA Rule 4511 — General Books and Records.
- SEC Division of Examinations priorities — current year [verify operative document].

## insurance

### Insurance sector overlay — policy-gap-review

Loads when the scope `sector_overlay_set` includes `insurance`. Binds policy gap reviews to insurance-supervisory expectations on the firm's policy framework.

#### Supervisory frame

Insurance is state-supervised in the US, with the National Association of Insurance Commissioners (NAIC) coordinating model laws and accreditation standards. State Departments of Insurance (DOIs) examine on the licensed state's adopted code; the NAIC model laws are adopted with state-by-state variation. A policy gap matrix for an insurance entity benchmarks against the NAIC model when the firm anchors there and against the operative state code where the licensed state has diverged.

The federal interplay is narrow but real: Federal Insurance Office (FIO) covers monitoring; Treasury / OFAC sanctions apply; the SEC supervises insurance-affiliated investment advisers and broker-dealers under separate frameworks (those run on the capital-markets overlay).

#### NAIC Model Audit Rule (MAR)

When the policy in scope is a financial-reporting, internal-audit, or internal-control policy, the matrix benchmarks against NAIC Model #205 (Annual Financial Reporting Model Regulation, the Model Audit Rule). MAR §16 covers the management report on internal control over financial reporting for in-scope insurers (typically those above the premium-volume threshold the rule names). Policy gap rows on MAR §16 are common for insurers whose ICFR policy frameworks were designed pre-MAR-2010 and have not been refreshed for the operative reporting cadence. [verify section labels against the most-recent NAIC model adoption.]

#### ORSA policy expectations

NAIC's Risk Management and Own Risk and Solvency Assessment Model Act (ORSA) imposes policy-framework expectations on covered insurers (typically above the premium-volume threshold). The matrix benchmarks the firm's ERM policy and the ORSA-summary-report policy against:

- The risk identification and prioritisation framework.
- The risk-tolerance statement and the linkage to the strategic plan.
- The risk-management policies covering each material risk category.
- The economic-capital and prospective solvency-assessment methodology.
- The board oversight of the ERM framework and the ORSA process.

A policy gap matrix for an ORSA-covered insurer that does not benchmark the ERM policy against the ORSA framework is incomplete; the state DOI reads ORSA submissions with the framework expectations in hand.

#### Market conduct and conduct-of-business

When the policy in scope is a market-conduct, sales-practice, claims-handling, or producer-supervision policy, the matrix benchmarks against:

- The NAIC Market Conduct Examiners Handbook (as adopted in the operative state code).
- State unfair claims practices acts (typically modelled on NAIC #900, with state variation).
- Producer licensing and supervision expectations (NAIC Producer Licensing Model Act #218).
- Suitability standards for annuities (NAIC Model #275) and life insurance, including the post-2020 best-interest amendments adopted by most states.
- Claims handling and timing standards (state-specific; the rule citation in the matrix is the operative state code).

#### Cybersecurity and data security

NAIC Model #668 (Insurance Data Security Model Law) imposes cybersecurity-program expectations on licensed insurers. State adoption varies; states that have adopted it (a growing list since 2017) impose policy-framework expectations on the firm's information security policy that overlap with NYDFS Part 500 for NYDFS-licensed entities. The cyber cross-cutting overlay loads in parallel where cybersecurity is in scope.

#### Sign-off and review-gate norms

Insurance-side policy gap reviews are reviewed by a named role keyed to the matrix scope: the chief actuary for actuarial policies, the chief compliance officer for market-conduct policies, the chief risk officer for ERM and ORSA policies, the CISO for cybersecurity policies, the chief claims officer for claims-handling policies. The audit committee or the operative board committee tables the recommended edits at the cadence the firm's framework requires; ORSA-related changes are tabled with board oversight per the ORSA model act.

#### Anchors used by this overlay

- NAIC Model #205 — Annual Financial Reporting Model Regulation (Model Audit Rule), §16 ICFR management report [verify section labels].
- NAIC Model #505 — Risk Management and Own Risk and Solvency Assessment Model Act [verify section labels].
- NAIC Market Conduct Examiners Handbook — current edition [verify chapter labels].
- NAIC Model #900 — Unfair Claims Settlement Practices Act [verify state-by-state adoption].
- NAIC Model #218 — Producer Licensing Model Act [verify state adoption].
- NAIC Model #275 — Suitability in Annuity Transactions Model Regulation [verify post-2020 best-interest amendment adoption].
- NAIC Model #668 — Insurance Data Security Model Law [verify state-by-state adoption].
- State unfair claims practices acts — operative state code where the licensed state has diverged from the NAIC model.

## payments-fintech

### Payments and fintech sector overlay — policy-gap-review

Loads when the scope `sector_overlay_set` includes `payments-fintech`. Binds policy gap reviews to payments-and-fintech-supervisory expectations on the firm's policy framework.

#### Supervisory frame

Payments and fintech sit across a complex supervisory mesh. Bank-sponsored fintech arrangements run on the sponsor bank's prudential supervisor (OCC, FRB, FDIC) and the bank-side TPRM frame; the fintech itself may be a state-licensed money transmitter, a registered investment adviser, a broker-dealer, or none of the above depending on the activity. The CFPB has direct supervisory authority over banks above $10B and over named non-banks for specific markets; UDAAP authority extends to all consumer-financial-services providers. State financial regulators license money transmitters (licensing patterns vary by state) and supervise consumer protection.

Policy gap reviews in payments-and-fintech benchmark against the bank-side and consumer-side rules in force, with the matrix surfacing the seam between the bank's policies (which the bank's supervisor reads) and the fintech's policies (which various supervisors read depending on the activity).

#### OCC fintech bank-partnership expectations

The OCC has issued multiple statements on bank-fintech partnerships, including the 2024 final third-party risk management guide for community banks (joint with FRB and FDIC), supervisory observations from the OCC's Office of the Comptroller, and the OCC's articulated expectation that the sponsor bank cannot delegate compliance accountability to the fintech partner. The matrix benchmarks bank-side TPRM and bank-fintech-program policies against:

- Sponsor-bank-side accountability for consumer protection (UDAAP, Reg E, Reg Z, Reg DD where applicable).
- BSA/AML accountability, including SAR/CTR responsibilities under the bank's BSA program.
- Information security responsibilities under the bank's cybersecurity policy.
- Customer complaint-handling responsibilities.
- Data sharing and customer-data ownership boundaries (Reg P, Reg S-P, GLBA).

Frequent gap site for sponsor-bank policies that delegated too much to the fintech partner without retaining named accountability points; OCC supervisory letters have surfaced this pattern repeatedly since 2022.

#### CFPB consumer-compliance expectations

When the policy in scope governs a consumer-facing payment, deposit, prepaid, or credit product, the matrix benchmarks against:

- **Reg E** — 12 CFR Part 1005, electronic fund transfers, including the Prepaid Accounts Rule (effective 2019).
- **Reg Z** — 12 CFR Part 1026, Truth in Lending, including credit-card provisions.
- **Reg DD** — 12 CFR Part 1030, Truth in Savings.
- **CFPB UDAAP exam manual** — for any consumer-facing policy.
- **CFPB Section 1033 (open banking)** — 12 CFR Part 1033, the personal financial data rights rule (final October 2024). **Compliance dates stayed as of October 29, 2025; CFPB-initiated reconsideration with ANPR** — verify current docket status before treating phased compliance dates as firm. The matrix benchmarks against the rule text and the firm's data-provider posture.

The Reg E provisional-credit obligations on dispute timing are a frequent gap site for fintech policies that adopted abbreviated timing windows that do not meet the rule.

#### State money-transmission licensing

When the firm operates as a state-licensed money transmitter, the matrix benchmarks against the operative state codes. The Conference of State Bank Supervisors (CSBS) Money Transmitter Modernization Act has been adopted by a growing list of states since 2021 and harmonises some core requirements; the matrix references the operative state's adopted version. State consumer protection acts impose additional policy expectations beyond the MTL.

#### FFIEC BSA/AML for non-bank money services businesses

When the firm is a money services business (MSB) registered with FinCEN, the matrix benchmarks against:

- 31 CFR §1022 series — FinCEN MSB rules.
- The FFIEC BSA/AML Examination Manual's MSB-specific sections.
- FinCEN's CDD Rule (31 CFR §1010.230) including the beneficial-ownership requirements.
- OFAC sanctions screening expectations.

#### Sponsor-bank-fintech allocation patterns

Policy gap matrices on bank-fintech program policies surface the allocation of compliance accountability between the bank and the fintech as a recurring matrix dimension. The matrix carries a `cross_policy_interactions` block that names the fintech's parallel policy and the contractual allocation document (the bank-fintech program agreement) so the reader can route the cross-policy fix to the right co-owner. The matrix does not assume the contract is itself sufficient evidence of compliance; the contract is benchmark input, not closure.

#### Sign-off and review-gate norms

Payments-and-fintech policy gap reviews are reviewed by the CCO (consumer-compliance), the BSA officer (BSA/AML), the chief risk officer (TPRM and operational risk), and the chief legal officer (state-licensing and contractual allocation). Where the firm is a sponsor bank, the bank's compliance committee tables material recommended edits; where the firm is a fintech, the fintech's risk and compliance committee tables, and the bank partner's policy team is informed via the program-management seam.

#### Anchors used by this overlay

- Interagency Guidance on Third-Party Relationships (June 2023) — for sponsor-bank-side TPRM benchmarks.
- 2024 community-bank third-party risk management guide (interagency).
- OCC Bulletin 2013-29 (legacy) and successor 2023 guidance — for sponsor-bank-side TPRM history.
- 12 CFR Part 1005 — Regulation E [verify post-2019 Prepaid Rule amendments].
- 12 CFR Part 1026 — Regulation Z [verify section labels for credit-card provisions].
- 12 CFR Part 1030 — Regulation DD.
- 12 CFR Part 1033 — Personal Financial Data Rights Rule (final October 2024) [verify phase-in tier dates].
- 31 CFR §1022 series — FinCEN MSB rules.
- 31 CFR §1010.230 — FinCEN Customer Due Diligence Rule.
- CSBS Money Transmitter Modernization Act — operative state-by-state adoption.
- CFPB UDAAP Examination Manual — current edition.
