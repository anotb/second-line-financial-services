# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — regulatory-impact-assessment

When the scope flags banking and the rule under assessment touches OCC, FRB, FDIC, or NCUA-supervised entities (or state-chartered banks under shared examination authority), load this overlay alongside `references/source-anchors.md`. The overlay carries the regulator-specific scoping conventions, threshold tier semantics, named-policy and named-control patterns, and the strategy-lens posture for the federal banking agencies.

#### Institution-type scoping conventions

Federal banking impact assessments turn on chartering, primary federal regulator, and tier categorisation:

- **National banks and federal savings associations** are OCC-supervised. Scope reads against OCC bulletins, the Comptroller's Handbook, and 12 CFR Parts 1 through 195 [verify subpart and section per assessment].
- **State member banks and bank holding companies (BHCs)** are FRB-supervised. Scope reads against SR letters and 12 CFR Parts 200 through 270 [verify subpart and section].
- **State non-member banks and FDIC-insured state savings associations** are FDIC-supervised. Scope reads against FILs and 12 CFR Parts 300 through 391 [verify subpart and section].
- **Federally insured credit unions** are NCUA-supervised. Scope reads against NCUA Letters to Credit Unions and 12 CFR Parts 700 through 799 [verify subpart and section].
- **Foreign banking organisations (FBOs) with US operations** are FRB-supervised at the consolidated level under the Enhanced Prudential Standards (Regulation YY, 12 CFR Part 252) [verify subpart], with the US branches' day-to-day supervision often shared with OCC or state regulators.

When the rule applies inter-agency (the June 2023 third-party-risk guidance, the heightened standards), the assessment cites all three or four agencies in the source-identification block.

#### Threshold tier semantics

The assessment's threshold determination reads against the federal banking tier framework:

- **Heightened Standards**: 12 CFR Part 30 Appendix B applies to insured national banks, federal savings associations, and federal branches with average total consolidated assets of $50B or more (parallel under Part 30 Appendix D for FRB and FDIC supervised entities) [verify subsection]. The Heightened Standards drive the second-line authority, board governance, and risk-management framework expectations the assessment reads against for in-scope rule changes.
- **FRB tailoring framework**: Categories I through IV under 12 CFR Part 252 [verify section] tier capital, liquidity, stress-testing, and resolution-planning expectations by asset size and complexity. A Category I firm absorbs a rule differently from a Category III firm; the assessment cites the firm's category and the corresponding tier expectations.
- **CFPB direct supervision threshold**: $10B in total assets for depository institutions (CFPB has direct supervisory authority for $10B+ banks and for non-bank consumer-finance providers). The assessment reads CFPB-rule scope against this threshold for bank-side applicability.
- **Community banks**: Generally below $10B in total assets, with FDIC, OCC Midsize and Community Bank Supervision, or FRB community-bank supervision as primary; the assessment reads against community-bank tailoring (e.g., the FDIC's community-bank-tailored expectations on operational resilience, BSA-AML proportionality).

#### Named-policy and named-control patterns

Federal banking impact assessments routinely touch the named-policy areas below; the policy-impact section typically references one or more:

- **Risk Governance Framework** under Heightened Standards Appendix B II.B [verify subsection].
- **Compliance Risk Management Programme** under OCC, FRB, FDIC supervisory guidance and the FFIEC Compliance Manual.
- **Third-Party Risk Management Policy** anchored on the June 2023 interagency guidance.
- **Information Security Programme** anchored on the GLBA Safeguards Rule, 12 CFR Part 30 Appendix B (security guidelines), and the FFIEC IT Examination Handbook.
- **Model Risk Management Policy** anchored on the joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026), which superseded SR 11-7 / OCC Bulletin 2011-12 (April 4, 2011) and SR 21-8 (April 9, 2021). GenAI and agentic AI are explicitly out of scope of the joint guidance; AI scope for those models routes to NIST AI RMF / NIST AI 600-1 / EU AI Act.
- **BSA-AML Programme** anchored on the FFIEC BSA/AML Examination Manual, 31 CFR Chapter X, and the AMLA 2020 implementation rules.
- **Fair-Lending Programme** anchored on Reg B (12 CFR Part 1002), Reg C (12 CFR Part 1003), and the FFIEC Interagency Fair Lending Examination Procedures.
- **Operational Resilience Programme** anchored on the FFIEC Business Continuity Management booklet and the FRB / OCC / FDIC operational-resilience papers (Sound Practices to Strengthen Operational Resilience; the 2020 paper) [verify publication date].
- **Capital Adequacy Process and ICAAP** anchored on 12 CFR Part 217 (FRB) and parallel OCC / FDIC subparts [verify subpart] for Category I-IV firms.
- **CCAR / DFAST stress-testing programme** for Category I-IV firms [verify regulation citation].
- **Recovery and Resolution Plans** for Category I-II firms under 12 CFR Parts 243, 381 [verify section].

The assessment's policy-impact section names the policy area, the expected change type, and the rationale; the skill does not draft policy language.

#### Reporting-impact patterns

Federal banking reporting touches:

- **Call Report (FFIEC 031, 041, 051)** schedules. Rule changes affecting balance-sheet classification, loan-segment reporting, fair-value reporting, or liquidity reporting drive Call Report schedule changes.
- **FR Y-9C, FR Y-9LP, FR Y-14A/Q/M** for BHCs. Tier-specific reporting expectations [verify form numbers].
- **HMDA LAR (Reg C)** for institutions meeting the HMDA threshold. https://www.consumerfinance.gov/data-research/hmda/ .
- **CRA Performance Evaluations** under 12 CFR Part 25 / 228 / 345 [verify subpart] and the 2023 interagency CRA modernisation final rule [verify implementation date and section].
- **CFPB 1071 Small Business Lending Register** under 12 CFR 1002.107 [verify subsection], phased by origination tier.
- **Suspicious Activity Reports (SAR)** and Currency Transaction Reports (CTR) under 31 CFR 1010, 1020 [verify subsection].

#### Strategy-lens posture for federal banking

The federal banking strategy lens has identifiable patterns:

- **Industry-association alignment**: BPI for large banks; ABA for the broader bank trade-association posture; ICBA for community banks; NAFCU for credit unions. The assessment names which association(s) the firm is engaged with on the rule.
- **Comment-letter convention**: Bank comment letters typically run through the BPI or ABA committee structure first, then the firm signs as a member or files its own. Coordination with the trade-association draft is standard; firm-direct comment letters are reserved for items where the firm's posture diverges from industry consensus or where the firm wants to make a specific record.
- **Supervisor meeting convention**: Federal banking agencies hold pre-comment meetings with supervised institutions on significant rulemakings. The CRO chief of staff or head of regulatory affairs runs the meeting; counsel attends; the head of the business affected provides the substantive read.
- **Examiner-posture-shift signal**: Speeches by the OCC Comptroller, FRB Chair or Vice Chair for Supervision, FDIC Chair, and the Director of the CFPB are read for examiner-posture signal; the assessment cites the specific speech URL and date when the signal is the trigger for the impact read.
- **Escalation triggers**: For federally supervised banks, a high-impact rule (cost-to-comply over $50M, multi-policy refresh, multi-control-objective change, board-reporting expectation) typically escalates to the board risk committee for the regulatory-strategy posture. A Heightened-Standards firm carries an additional gate: the chief risk officer's independent risk management view feeds the board's read.

#### Cost-to-comply patterns

Federal banking cost-to-comply reads typically calibrate against:

- **OMB Circular A-4 RIAs** published in the federal banking agencies' adopting releases for significant rules (the "Effects of the Rule" section).
- **Peer-firm benchmark**: where peer-firm cost reads are available through trade-association working groups or public disclosures, the firm calibrates against them.
- **Vendor-quote ranges**: for technology and vendor remediation costs, the assessment uses indicative vendor-quote ranges as the basis.
- **Prior-project benchmarks**: the firm's prior-project cost-to-comply reads (e.g., the firm's CECL implementation cost as a benchmark for a new accounting-rule impact) feed indicative ranges.

Agency cost estimates routinely diverge from firm-side reads. The assessment names the divergence and the basis; the federal banking strategy lens often picks up that divergence as a comment-letter input.

#### When to escalate beyond regulatory-change-committee

For federal banking, the escalation triggers below typically fire:

- **CRO**: any rule with a Heightened-Standards Risk Governance Framework implication; any rule introducing a new annual board-attestation expectation.
- **General counsel**: any rule with a litigation-posture implication (judicial review pending; a vacatur or stay affecting the effective date); any rule requiring counsel to set the comment-letter signature posture.
- **Executive committee**: any rule with a cost-to-comply read over $50M one-time or $20M run-rate (illustrative threshold; firm-specific thresholds in `references/firm-overlay.md`).
- **Board risk committee**: any rule introducing a new board-committee-reporting expectation; any rule under a Heightened-Standards Risk Governance Framework category; any consent-order-pattern theme that names a peer institution under the same primary regulator.
- **Full board**: any rule with strategic-business-model implications (e.g., the Basel III Endgame final rule's capital implications for affected firms); any rule with a board-attestation expectation.

The escalation triggers are firm-specific; the overlay names the pattern, and `references/firm-overlay.md` overrides with firm-specific thresholds.

## capital-markets

### Capital markets sector overlay — regulatory-impact-assessment

When the scope flags capital markets and the rule touches SEC-registered investment advisers, registered funds, broker-dealers, transfer agents, exchanges, ATSs, or FINRA members, load this overlay alongside `references/source-anchors.md`. The overlay carries the SEC adopting-release mechanics, FINRA rule-filing alignment under SEC Rule 19b-4, the AUM-and-activity threshold mechanics, IAA Rule 206(4)-7 implications, and the strategy-lens posture for SEC and FINRA engagements.

#### Institution-type scoping conventions

Capital-markets impact assessments turn on registration status, regulator, and activity:

- **SEC-registered investment advisers** under the Investment Advisers Act of 1940. Scope reads against the IAA and 17 CFR Part 275; the registered-adviser AUM threshold (generally $100M federal-registration; below that, state registration) determines federal-versus-state primary regulator.
- **Registered investment companies (mutual funds, ETFs, closed-end funds)** under the Investment Company Act of 1940 and 17 CFR Part 270.
- **Broker-dealers** under the Securities Exchange Act of 1934, 17 CFR Parts 240 and 242, and FINRA membership.
- **Transfer agents** registered under §17A of the Exchange Act, 17 CFR Part 240 §§240.17Ad-1 through 240.17Ad-22 [verify subsection].
- **Exchanges and ATSs** under Regulation ATS and the Exchange Act.
- **Municipal advisors** under the Municipal Securities Rulemaking Board (MSRB) framework.
- **Security-based swap dealers** under §15F of the Exchange Act and Title VII of Dodd-Frank.

When the rule applies across registration categories (a cyber-disclosure rule that hits both registered advisers and registered funds), the assessment names each registration in the source-identification block.

#### Threshold and tier mechanics

The assessment's threshold determination reads against the SEC and FINRA tier mechanics:

- **Adviser federal-registration threshold**: $100M AUM generally [verify exact threshold and exceptions]. Below the threshold, advisers register with state regulators.
- **Large adviser AUM thresholds**: certain rules (e.g., the SEC's private-fund-adviser rule, the cybersecurity disclosure rule) tier expectations by AUM and by client type [verify rule-specific thresholds].
- **Fund-registration thresholds**: registered investment companies tier reporting and disclosure expectations by net asset value, by share class, and by investor type.
- **Broker-dealer net-capital tiers**: under SEC Rule 15c3-1 (17 CFR §240.15c3-1) [verify subsection], net-capital thresholds determine the firm's permissible activity scope.
- **FINRA member tiering**: FINRA Rule 4517 [verify] and member-specific examination tiering set the firm's examination cycle.

#### Named-policy and named-control patterns

Capital-markets impact assessments routinely touch the named-policy areas below; the policy-impact section typically references one or more:

- **IAA Rule 206(4)-7 Compliance Programme** (17 CFR §275.206(4)-7) [verify subsection]: the adviser's annual review of its compliance programme; the assessment's policy-impact section often anchors on the annual review's scope.
- **Marketing Rule programme** under IAA Rule 206(4)-1 (17 CFR §275.206(4)-1) [verify subsection]: advertising and solicitation procedures; performance-presentation review; testimonials and endorsements policy.
- **Custody Rule programme** under IAA Rule 206(4)-2 (17 CFR §275.206(4)-2) [verify subsection]: client-asset custody safeguards; surprise-examination procedure (where applicable).
- **Books and Records programme** under IAA Rule 204-2 (17 CFR §275.204-2) and Exchange Act Rule 17a-3 / 17a-4 [verify subsection]: record-creation and record-retention; the 2024 SEC and CFTC enforcement pattern on off-channel communications has driven a substantial control-objective refresh.
- **Cybersecurity Programme** under SEC and FINRA expectations (17 CFR Part 248 Reg S-P; the SEC adopted cyber rule for advisers and funds when applicable; FINRA Rule 4370 [verify subsection]).
- **Anti-Money Laundering Programme** under FinCEN rules (31 CFR 1010 / 1023 / 1024 / 1026) [verify subsection], Bank Secrecy Act application to broker-dealers and to investment advisers (the 2024 final rule extending AML obligations to certain investment advisers) [verify rule citation and effective date].
- **Best Execution programme** under FINRA Rule 5310, MSRB Rule G-18 [verify], and the SEC's order-handling and best-execution expectations.
- **Suitability and Care Obligations programme** under FINRA Rule 2111 (suitability), Reg BI (17 CFR §240.15l-1) [verify subsection] for broker-dealer customer-care, and the IAA fiduciary-duty interpretation [verify Release IA-5248].
- **Fund Liquidity Risk Management programme** under Investment Company Act Rule 22e-4 (17 CFR §270.22e-4) [verify subsection].

The assessment's policy-impact section names the policy area, the expected change type, and the rationale; the skill does not draft policy language.

#### Reporting-impact patterns

Capital-markets reporting touches:

- **Form ADV (Parts 1A, 2A, 2B, Part 3 / Form CRS)** for investment advisers. Annual amendments and other-than-annual amendments under Rule 204-1 [verify subsection].
- **Form N-1A, N-2, N-3, N-4, N-CSR, N-PORT, N-LIQUID** for registered investment companies. Specific form changes follow specific rule changes.
- **Form 10-K Item 1.05** (cyber incident disclosure) for public companies under the SEC cyber rule (17 CFR 229.106 and Form 8-K Item 1.05) [verify section].
- **FOCUS Reports** for broker-dealers under SEC Rule 17a-5 [verify subsection].
- **Form CRS** for advisers and broker-dealers serving retail investors under Reg BI [verify rule citation].
- **MSRB Form G-32, G-37, G-45** for municipal-securities-related activity [verify form citations].
- **CFTC Form CPO-PQR / CTA-PR** for commodity pool operators and commodity trading advisors that are also SEC-registered.

#### SEC adopting-release and FINRA filing mechanics

Capital-markets impact assessments turn on a specific publication chain:

- The SEC issues a proposing release (in the Federal Register, with a release number, e.g., Release No. 33-XXXXX, IA-XXXXX, 34-XXXXX, IC-XXXXX). The release carries the agency's cost-and-benefit analysis under OMB Circular A-4 (the "Economic Analysis" section in the release).
- A comment period follows (typically 60 days, sometimes longer for complex rulemakings).
- The SEC issues an adopting release with the final rule. The adopting release contains the substantive analysis the impact assessment reads against, including responses to comments and the agency's revised cost-and-benefit analysis.
- For FINRA-rule changes, FINRA files a proposed rule change with the SEC under Section 19(b)(1) of the Exchange Act and SEC Rule 19b-4 (17 CFR §240.19b-4) [verify subsection]. The SEC publishes the FINRA filing for comment in the Federal Register; the SEC approves, disapproves, or institutes proceedings.
- Effective dates for SEC final rules are typically 60 days after Federal Register publication, with compliance dates often deferred (12 to 24 months for substantive operational rules).

The assessment's source-identification block carries the release number, the FR citation, the publication date, the effective date, and the compliance dates by phase.

#### Strategy-lens posture for SEC and FINRA engagements

The capital-markets strategy lens has identifiable patterns:

- **Industry-association alignment**: SIFMA for broker-dealers and large advisers; ICI for fund-side; IAA for the smaller-and-medium adviser side; the Managed Funds Association for hedge-fund advisers; the SEC IAC and FINRA committees for industry input.
- **Comment-letter convention**: Adviser, fund, and broker-dealer comment letters typically run through the trade-association committee structure first; the firm signs as a member, files its own letter, or both. The comment file is itself part of the rulemaking record and is read by the agency in the adopting release.
- **Supervisor meeting convention**: SEC Division of Investment Management, Division of Trading and Markets, and Division of Examinations hold pre-comment meetings with registrants and industry associations on significant rulemakings. FINRA holds rule-filing-stakeholder meetings as well.
- **Examiner-posture-shift signal**: Speeches by the SEC Chair, the Commissioners, the Division Directors, and the Director of FINRA are read for examiner-posture signal. The Division of Examinations annual examination priorities letter is the operative annual signal; the assessment reads the most recent priorities letter for the strategy lens.
- **Comment-letter timing**: The SEC comment-period close date drives the firm's internal timeline; comment letters typically run through compliance, legal, and business-head review, with sign-off by the chief compliance officer for advisers and the chief legal officer for broker-dealers. For fund-board-related rules, the fund board's read feeds the comment letter.
- **Escalation triggers**: For SEC-registered firms, a high-impact rule typically escalates to the chief compliance officer (advisers), the chief legal officer (broker-dealers), and the head of the business affected. Fund-board-related rules escalate to the fund board for the strategy posture. The board of the adviser or broker-dealer receives the escalated read for items with cost-to-comply over a firm-set threshold or with strategic-business-model implications.

#### Cost-to-comply patterns

Capital-markets cost-to-comply reads typically calibrate against:

- **SEC Economic Analysis** in the adopting release. The SEC's analysis often presents low-cost and high-cost ranges; the firm's read calibrates against the agency's range and names where the firm-side estimate diverges.
- **Trade-association cost-survey data**: SIFMA, ICI, and IAA periodically publish industry-average cost-to-comply reads on significant rules. The firm's read calibrates against the trade-association data with firm-specific adjustments.
- **Prior-rule benchmarks**: the firm's prior cost-to-comply on Reg BI implementation, marketing-rule implementation, or custody-rule amendments serves as a benchmark for new-rule reads.
- **Vendor-quote ranges**: third-party compliance-platform and recordkeeping-platform vendor quotes feed indicative ranges.

Agency cost estimates routinely diverge from firm-side reads, particularly for buy-side firms where the agency's cost ranges have historically underestimated implementation costs in some rule categories. The assessment names the divergence and the basis.

#### When to escalate beyond regulatory-change-committee

For SEC-registered and FINRA-member firms, the escalation triggers below typically fire:

- **Chief compliance officer (advisers)**: any rule with an IAA Rule 206(4)-7 annual-review-scope implication.
- **Chief legal officer (broker-dealers)**: any rule with a Reg BI implication or with an off-channel-communications enforcement-pattern implication.
- **Fund board**: any rule with a fund-board-oversight implication (Rule 18f-4 for derivatives; Rule 22e-4 for liquidity; Rule 38a-1 for compliance programmes; Rule 17a-9 for affiliate transactions).
- **Executive committee**: any rule with a cost-to-comply read over a firm-specific threshold; any rule with a strategic-business-model implication.
- **Board of the adviser or broker-dealer**: any rule with a board-reporting expectation (Reg BI, the SEC cyber rule for public-company filers, the SEC custody rule amendments).

The escalation triggers are firm-specific; the overlay names the pattern, and `references/firm-overlay.md` overrides with firm-specific thresholds.

## insurance

### Insurance sector overlay — regulatory-impact-assessment

When the scope flags insurance and the rule (or NAIC model law, or state DOI bulletin, or NYDFS Industry Letter, or federal-level insurance-related rule such as a Federal Insurance Office report or HHS-CMS rule for health insurance) touches insurers or affiliated entities, load this overlay alongside `references/source-anchors.md`. The overlay carries the NAIC model-law adoption mechanics, state DOI variance, NYDFS overlays, and the strategy-lens posture for state-DOI-led examination cycles.

#### Institution-type and regulatory-frame scoping

Insurance impact assessments turn on legal-entity type, line of business, and state-of-domicile:

- **Life and annuity insurers** under state insurance codes; NAIC Suitability in Annuity Transactions Model Regulation (#275) [verify section]; state-by-state adoption variance.
- **Property and casualty insurers** under state insurance codes; market-conduct examination cycles run by state DOIs.
- **Health insurers** under state insurance codes plus federal frameworks (ACA market-stabilisation rules, ERISA where applicable, HIPAA, MHPAEA).
- **Reinsurers** under state insurance codes plus the Bilateral Agreement / Covered Agreement regime for credit for reinsurance.
- **Captive insurers** under state captive statutes (Vermont, South Carolina, Hawaii, others) [verify state captive code].
- **Insurance holding company systems** under NAIC Insurance Holding Company System Regulatory Act (#440) [verify section] and state adoption.
- **Producers (agents and brokers)** under state producer-licensing statutes; state-by-state variance.

The insurance regulatory frame is primarily state-level. Federal-level frameworks apply for specific topics (Federal Insurance Office reporting; ACA; ERISA; HIPAA; OFAC; FCRA application to insurance underwriting; sanctions; Treasury terrorism-risk-insurance reauthorisation cycles).

#### Threshold and tier semantics

The assessment's threshold determination reads against insurance-specific tier mechanics:

- **NAIC RBC tiers** (Risk-Based Capital): the firm's RBC level (Total Adjusted Capital ratio) drives the regulatory-action tier the firm sits in (No Action; Company Action; Regulatory Action; Authorized Control; Mandatory Control). The assessment cites the tier and the corresponding regulatory-action expectations.
- **NAIC IRIS ratios**: the Insurance Regulatory Information System ratios drive the firm's examination-priority categorisation.
- **Group capital calculation (GCC)**: the NAIC group capital framework drives consolidated-supervision expectations for insurance holding company systems.
- **Domestic and non-domestic state license**: the assessment reads state-by-state license footprint to scope state-specific rule applicability. A non-domestic license carries the host-state's rule scope; a domestic license carries the domestic-state's primary supervisory authority.
- **NYDFS Part 500 covered-entity scope**: NYDFS-licensed insurance entities meet the Part 500 covered-entity definition; the assessment reads cyber-rule scope against this.
- **NAIC Insurance Data Security Model Law (#668)** adoption: the model-law adoption status by state determines which state-specific cyber-data-security rule the firm is subject to. https://content.naic.org/cipr-topics/cybersecurity .

#### Named-policy and named-control patterns

Insurance impact assessments routinely touch the named-policy areas below; the policy-impact section typically references one or more:

- **Enterprise Risk Management Programme** under NAIC ORSA Model Act (#505) [verify section] and NAIC Risk Management and Own Risk and Solvency Assessment Model Act state adoption.
- **Underwriting Programme** anchored on state-specific underwriting rules and NAIC Unfair Trade Practices Act (#880) [verify section].
- **Claims-Handling Programme** anchored on state-specific claims-handling regulations and NAIC Unfair Claims Settlement Practices Act (#900) [verify section].
- **Market Conduct Programme** anchored on the NAIC Market Conduct Examiners Handbook and state DOI examination expectations.
- **Insurance Holding Company Filings** under Form A (acquisition of control), Form B (registration), Form C (changes), Form D (extraordinary transactions), and Form F (enterprise risk report) [verify state adoption of the model holding-company act].
- **Producer Licensing and Conduct Programme** anchored on state producer-licensing statutes.
- **Anti-Fraud Programme** anchored on NAIC Insurance Fraud Prevention Model Act (#680) [verify section] and state adoption.
- **Cybersecurity Programme** anchored on NAIC Insurance Data Security Model Law (#668) and NYDFS 23 NYCRR Part 500 where applicable.
- **AI Use in Underwriting and Claims** anchored on the NAIC Model Bulletin on the Use of AI Systems by Insurers (December 2023) [verify section] and state adoption (Colorado SB 21-169 and Reg 10-1-1; New York DFS Circular Letter on the use of external consumer data and information sources in underwriting and the related Insurance Circular Letter; California; Connecticut and others) [verify state-specific bulletins].
- **Privacy and Data Protection Programme** anchored on the GLBA Privacy Rule, state insurance privacy statutes, and HIPAA where the firm touches PHI.

The assessment's policy-impact section names the policy area, the expected change type, and the rationale; the skill does not draft policy language.

#### Reporting-impact patterns

Insurance reporting touches:

- **NAIC Annual Statement** (Statutory Annual Statement; Quarterly Statements). State-by-state filing with the home state and NAIC-state filings.
- **ORSA Summary Report** annually under NAIC ORSA Model Act state adoption.
- **NAIC RBC Report** annually with the Statutory Annual Statement.
- **Form B Holding Company Registration** (annual) and Form F Enterprise Risk Report (annual) for insurance holding company systems.
- **NAIC Market Conduct Annual Statement** (MCAS) for life, annuity, P&C, and health lines [verify line-of-business scope].
- **State-DOI rate, form, and rule filings** under SERFF (System for Electronic Rates and Form Filing) [verify state-specific filing convention].
- **Federal filings** where applicable: Form 5500 for ERISA-covered group health plans; HHS-CMS filings for ACA-market participation; FIO filings; Treasury TRIA filings for terrorism-risk-insurance writers.

#### NAIC model-law adoption mechanics

Insurance impact assessments turn on a state-by-state adoption pattern:

- The NAIC adopts a model law at a NAIC member meeting, with Plenary approval following committee adoption.
- States individually consider the model law for adoption, with state-specific drafting variance. Some states adopt the model law verbatim; some adopt with amendments; some decline to adopt.
- A model law's "effective date" at the NAIC level is the NAIC adoption date, not a state-level effective date. The firm's compliance obligation runs from the state-level effective date, which can lag the NAIC adoption by months or years.
- State adoption status is tracked on the NAIC website (model-law-tracking page, https://content.naic.org/) [verify URL].
- Some NAIC frameworks rely on accreditation: the NAIC Accreditation Standards require accredited states to enact certain model laws within a set period. Non-accredited states still receive non-domestic-state oversight pressure to adopt.

The assessment's effective-date posture for insurance rules names the NAIC adoption date, the state-by-state adoption status (where the firm is licensed), and the firm's effective-date read state-by-state. A single rule can have a different effective date in every state the firm is licensed in.

#### NYDFS overlay

NYDFS is the most-active state-level insurance supervisor and the source of multiple Industry Letters that drive cross-state convention:

- **NYDFS Insurance Circular Letters**: topic-specific letters that shape NYDFS examination posture and often signal cross-state convention. https://www.dfs.ny.gov/industry_guidance/circular_letters .
- **NYDFS Cybersecurity Requirements (Part 500)**: covered insurers fall under Part 500 alongside other DFS-supervised financial-services companies.
- **NYDFS AI in Insurance Industry Letter** (and the related Circular Letter on the use of external consumer data and information sources in underwriting and pricing) [verify date and section]: the operative NYDFS posture on AI and external-data use in insurance underwriting.
- **NYDFS Climate Risk Industry Letter** (and the climate-risk-management framework for insurers) [verify date and section]: NYDFS climate-risk expectations for licensed insurers.

#### Strategy-lens posture for state-DOI engagements

The insurance strategy lens has identifiable patterns:

- **Industry-association alignment**: ACLI for life and annuity; APCIA (American Property Casualty Insurance Association) for P&C; AHIP for health; NAMIC (National Association of Mutual Insurance Companies) for mutual P&C; NAIFA (insurance and financial advisors). The assessment names which association(s) the firm is engaged with on the rule.
- **NAIC Working Group engagement**: the firm engages with the NAIC working group considering the model law (e.g., the Innovation, Cybersecurity and Technology (H) Committee for AI and cyber; the Property and Casualty Insurance (C) Committee for P&C topics). Engagement is via trade-association seat or as a public commenter.
- **State-DOI engagement**: the firm engages with the home-state DOI on the strategy posture for state-specific bulletins and on the state's adoption stance for NAIC model laws. NYDFS, California DOI, Connecticut DOI, Texas DOI, Florida DOI, and Illinois DOI are routine engagement targets.
- **Examiner-posture-shift signal**: NYDFS Industry Letters, California DOI bulletins, the NAIC's Quarterly Bulletin, and the National Council of Insurance Legislators (NCOIL) model-law actions signal examiner-posture shifts.
- **Federal-level engagement**: where the rule touches federal frameworks (FIO, HHS-CMS, Treasury, OFAC, federal AI rulemaking), the firm's federal engagement runs in parallel.
- **Escalation triggers**: For state-DOI-led rules, escalation typically runs to the chief compliance officer for the line of business (life, P&C, health), the head of underwriting, and the head of claims. For NAIC-model-law-driven rules with multi-state rollout, escalation to the executive committee is standard for cost-to-comply over a firm-set threshold. Holding-company-act-driven rules (Form A, Form F) escalate to the general counsel and the chief financial officer.

#### Cost-to-comply patterns

Insurance cost-to-comply reads typically calibrate against:

- **NAIC fiscal-impact estimates** in the model-law drafting record (where prepared) [verify drafting record availability].
- **State-DOI bulletin economic-impact statements** where the state has prepared one (variable by state).
- **Trade-association cost-survey data**: ACLI, APCIA, AHIP periodically publish industry-average cost-to-comply reads.
- **Prior-rule benchmarks**: the firm's prior cost-to-comply on principle-based reserving (PBR) implementation, AML programme stand-up for insurers, ORSA implementation, or the Insurance Data Security Model Law adoption serves as a benchmark.
- **State-by-state cumulative cost**: a single NAIC model law adopted state-by-state with drafting variance carries cumulative state-by-state implementation cost; the assessment reads that cumulative cost rather than a single-state cost.

#### When to escalate beyond regulatory-change-committee

For insurance, the escalation triggers below typically fire:

- **Chief compliance officer (per line of business)**: any rule with a market-conduct-examination-cycle implication or an underwriting-or-claims-rule implication.
- **General counsel**: any rule with an insurance-holding-company-act implication; any rule requiring counsel to set the trade-association coordination posture.
- **Chief financial officer / chief actuary**: any rule with a reserving, RBC, or capital-treatment implication.
- **Executive committee**: any rule with a multi-state rollout and cumulative cost-to-comply over a firm-set threshold; any rule with a strategic-business-model implication (a reserving change for a line of business; a capital-charge change).
- **Board risk committee**: any rule with an ORSA-implication; any rule with a cyber-data-security-policy refresh expectation; any rule with an AI-use-in-underwriting-or-claims implication.
- **Full board**: any rule with strategic-business-model implications across multiple lines or states.

The escalation triggers are firm-specific; the overlay names the pattern, and `references/firm-overlay.md` overrides with firm-specific thresholds.

## payments-fintech

### Payments and fintech sector overlay — regulatory-impact-assessment

When the scope flags payments or fintech and the rule touches non-bank consumer-finance providers, money transmitters, payment processors, prepaid issuers, BNPL providers, crypto-asset firms, neobanks operating under sponsor-bank arrangements, or bank-fintech partnerships, load this overlay alongside `references/source-anchors.md`. The overlay carries the CFPB larger-participant authority, the state-money-transmitter overlay, the bank-fintech partnership posture, and the strategy-lens posture for non-bank engagement.

#### Institution-type and regulatory-frame scoping

Payments and fintech impact assessments turn on legal-entity type, activity, partnership structure, and licensing footprint:

- **Non-bank consumer-finance providers** (mortgage servicers, debt collectors, payday lenders, BNPL providers, larger participants in consumer-financial-product markets) under CFPB direct supervision per the larger-participant rule (12 CFR Part 1090; the November 2024 final rule designating larger participants of digital consumer payment applications has been the subject of post-publication challenge and CFPB reconsideration since 2025 — verify current operative status). The CFPB BNPL interpretive rule (May 2024) was **nullified by Pub. L. 119-11 (May 9, 2025); historical only**.
- **State-licensed money transmitters** under state money-transmitter statutes (state-by-state). The Conference of State Bank Supervisors (CSBS) Money Transmitter Modernization Act / Money Services Business Model Act is the harmonisation vehicle, with state-by-state adoption variance.
- **Federally registered MSBs** under FinCEN registration (31 CFR 1022) [verify subsection].
- **Sponsor-bank-arrangement fintechs**: a non-bank fintech offering a banking-like product (deposit account, debit card, payments capability) under a sponsor-bank's charter. The sponsor-bank carries the regulatory exposure; the fintech operates under contract.
- **Neobanks**: digital-only fintechs offering banking-like products, typically under sponsor-bank arrangements (very few have direct charters).
- **Payment processors and acquirers** under card-network rules (Visa, Mastercard, AmEx, Discover) and state money-transmission rules where applicable.
- **Prepaid card issuers** under Reg E (12 CFR Part 1005) [verify subsection], state money-transmission rules where applicable, and CFPB rules for prepaid accounts (12 CFR Part 1005 Subpart A) [verify subsection].
- **Crypto-asset firms** under federal frameworks (FinCEN MSB registration, SEC, CFTC depending on the asset's classification) and state-by-state money-transmitter and BitLicense-type rules.
- **Lending fintechs** under federal consumer-credit rules (TILA, Reg Z; ECOA, Reg B; FCRA; FDCPA) and state lending licensing rules.

#### Threshold and tier semantics

The assessment's threshold determination reads against payments-and-fintech tier mechanics:

- **CFPB larger-participant thresholds**: the CFPB's larger-participant rule (12 CFR Part 1090) [verify subpart and section] sets activity-volume thresholds that bring non-bank firms under direct CFPB supervision (e.g., consumer reporting, debt collection, student loan servicing, automobile financing, international money transmission, and digital consumer payment applications under the November 2024 final rule — verify current operative status given post-2024 challenge and CFPB reconsideration). BNPL is currently outside the named larger-participant markets; the CFPB BNPL interpretive rule was **nullified by Pub. L. 119-11 (May 9, 2025); historical only**.
- **State money-transmitter licensing thresholds**: state-by-state money-transmitter statutes set activity-volume and net-worth thresholds for licensure.
- **FinCEN MSB registration thresholds**: 31 CFR 1010.100(ff) [verify subsection] sets the MSB definition; firms meeting the definition register with FinCEN.
- **Sponsor-bank tier**: sponsor-bank capital, asset size, and primary regulator drive the bank-side regulatory exposure that flows to the fintech under the partnership.
- **Card-network volume tiers**: Visa, Mastercard, and AmEx tier merchants and processors by transaction volume; tier-specific compliance expectations apply (PCI DSS Level 1 through 4).

#### Named-policy and named-control patterns

Payments-and-fintech impact assessments routinely touch the named-policy areas below; the policy-impact section typically references one or more:

- **BSA-AML Programme** for the firm's MSB or money-transmitter scope under FinCEN rules (31 CFR 1022) and state requirements.
- **OFAC Sanctions Programme** for the firm's payments and customer-onboarding scope.
- **Reg E Programme** for consumer-error-resolution, provisional-credit, and unauthorised-EFT handling under 12 CFR Part 1005.
- **Reg Z Programme** for credit-card, BNPL-where-applicable, and lending disclosures under 12 CFR Part 1026. (Reg Z applicability to Pay-in-Four BNPL is now an open question on the regulatory text; the CFPB BNPL interpretive rule was **nullified by Pub. L. 119-11 (May 9, 2025); historical only**.)
- **TILA-RESPA Integrated Disclosure (TRID) Programme** for mortgage lenders.
- **FCRA Programme** for adverse-action, credit-reporting, and dispute handling.
- **FDCPA Programme** for collection activities (where applicable).
- **State Money Transmitter Licensing Programme**: state-by-state license maintenance, surety-bond compliance, net-worth covenants, consumer-protection rules.
- **Sponsor-Bank Partnership Programme** with the bank-side allocation pattern: which obligations the bank retains, which the fintech operates, and which are jointly executed. The June 2023 interagency third-party-risk guidance is the operative bank-side framework for the partnership.
- **Customer Identification Programme (CIP)** under 31 CFR 1020 (for bank partners) or 31 CFR 1022 (for the MSB) [verify subsection].
- **Cybersecurity Programme** anchored on PCI DSS, NYDFS Part 500 for NYDFS-licensed entities, and FFIEC IT Handbook expectations flowed down through sponsor-bank contracts.
- **Privacy Programme** anchored on the GLBA Privacy Rule, the GLBA Safeguards Rule, state privacy laws (CCPA / CPRA), and CFPB consumer-financial-data rules.
- **Dispute-Handling and Complaint-Management Programme** anchored on Reg E, Reg Z, CFPB complaint-tracking expectations, and card-network dispute rules.
- **Open Banking and Data Sharing Programme** under CFPB Section 1033 (12 CFR Part 1033). **§1033 compliance dates stayed as of October 29, 2025; CFPB-initiated reconsideration with ANPR** — verify current docket status before sequencing the programme against tier-based compliance dates.

The assessment's policy-impact section names the policy area, the expected change type, and the rationale; the skill does not draft policy language.

#### Reporting-impact patterns

Payments-and-fintech reporting touches:

- **FinCEN SAR and CTR** under 31 CFR 1022 (for MSBs), 1020 (for bank partners), 1023 (for broker-dealers in money-services activity).
- **State money-transmitter reports**: quarterly call reports, annual financial reports, transaction-volume reports under state statutes.
- **CFPB complaint-database reporting**: CFPB-supervised firms respond to consumer complaints in the CFPB consumer complaint database with response timing and documentation expectations.
- **Card-network operator reports**: chargeback ratios, fraud ratios, dispute-volume reports under network rules.
- **Prepaid card disclosures** under 12 CFR Part 1005 [verify subsection].
- **Section 1033 data-access reporting** under the CFPB open-banking rule (**compliance dates stayed October 29, 2025; CFPB reconsideration with ANPR** — verify before relying on rule-text reporting cadences).
- **Sponsor-bank-issued reports**: the sponsor-bank's regulatory reports cover the bank-fintech-partnership program-level data; the fintech's contributions feed those reports.

#### Sponsor-bank partnership posture

Bank-fintech partnerships carry a bank-side and fintech-side regulatory exposure pattern:

- **Bank-side allocation**: under the June 2023 interagency third-party-risk guidance, the sponsor-bank retains primary regulatory exposure for the partnership. The fintech operates under contract; the bank's regulator examines the fintech's operations through the bank's third-party-risk-management framework. Recent enforcement actions against sponsor banks (2023-2024) have raised the bar on bank-side oversight expectations, particularly around BSA-AML programme effectiveness, consumer-protection-rule adherence, and operational resilience.
- **Fintech-side direct exposure**: where the fintech holds direct CFPB supervision under the larger-participant rule, holds state money-transmitter licenses, or operates as an FinCEN-registered MSB, the fintech carries direct regulatory exposure for those frameworks alongside the sponsor-bank partnership.
- **Partnership documentation**: the master service agreement, the BSA-AML programme allocation, the consumer-protection-rule allocation, the data-handling allocation, and the exit-plan documentation are the operative partnership artifacts. Rule changes routinely require partnership-document refresh.
- **Sponsor-bank concentration risk**: where multiple sponsor-bank arrangements implicate similar customer bases or payment flows, the bank-side concentration-risk read drives partnership-portfolio decisions. A new rule that disproportionately affects sponsor-bank-arrangement fintechs (e.g., an AML rule expansion, a Section 1071 expansion to non-bank lenders under bank partnership) carries portfolio-level escalation.

#### Strategy-lens posture for CFPB and state engagements

The payments-and-fintech strategy lens has identifiable patterns:

- **Industry-association alignment**: Financial Technology Association (FTA), American Fintech Council (AFC), Money Transmission Regulators Association (state-side), Financial Innovation Now (FIN) for payments and tech-sector engagement. Larger card networks engage through their own channels; merchant payments through the Merchant Risk Council; BNPL through trade-association working groups.
- **CFPB engagement convention**: the CFPB holds public listening sessions on significant rulemakings; non-bank firms engage through trade-association channels and as direct commenters. The CFPB's RFI (Request for Information) cycle precedes some rulemakings; the assessment reads RFI responses for industry posture signal.
- **State-by-state engagement**: state money-transmitter regulators engage through CSBS and through state-specific bulletins. The Money Transmission Modernization Act is the state-harmonisation vehicle; state-by-state adoption progresses unevenly.
- **Examiner-posture-shift signal**: CFPB Director speeches, CFPB Supervisory Highlights, OCC and FRB and FDIC interagency communications on bank-fintech partnerships, and NYDFS Industry Letters drive examiner-posture signal.
- **Sponsor-bank coordination**: where the rule affects the bank-fintech partnership, the fintech and the sponsor-bank coordinate the strategy posture. Comment letters on bank-fintech-partnership topics often run through both bank-side and fintech-side trade associations.
- **Escalation triggers**: For non-bank-supervised firms, escalation typically runs to the chief compliance officer, the head of legal, and the head of the partnership programme. For sponsor-bank-arrangement fintechs, the sponsor-bank's regulatory-affairs lead is a parallel escalation point. Items with state-by-state cumulative-cost implications or with sponsor-bank-partnership renegotiation implications escalate to the executive committee.

#### Cost-to-comply patterns

Payments-and-fintech cost-to-comply reads typically calibrate against:

- **CFPB Economic Analysis** in the rule's adopting release (the CFPB prepares cost-and-benefit analyses under OMB Circular A-4).
- **State-by-state cumulative cost** for state-money-transmitter rule changes.
- **Trade-association cost-survey data**: FTA, AFC, MRA periodically publish cost-to-comply reads.
- **Prior-rule benchmarks**: the firm's prior cost-to-comply on prepaid-account-rule implementation, debt-collection-rule implementation (Reg F), or Section 1033 implementation serves as a benchmark.
- **Sponsor-bank contract pass-through**: where the rule increases the sponsor-bank's compliance burden, the bank's contractual pass-through to the fintech is a cost-to-comply input.

#### When to escalate beyond regulatory-change-committee

For payments-and-fintech, the escalation triggers below typically fire:

- **Chief compliance officer**: any rule with a CFPB direct-supervision-scope implication; any rule with a state-money-transmitter-license implication.
- **Head of legal**: any rule requiring partnership-document refresh (master service agreement, programme agreement); any rule with a state-by-state legal-research implication.
- **Head of the partnership programme (sponsor-bank-arrangement fintechs)**: any rule affecting the bank-fintech-partnership allocation pattern.
- **Executive committee**: any rule with multi-state cumulative-cost implications; any rule with a strategic-product-decision implication (de-risk a product line, exit a state, restructure a partnership).
- **Board (where applicable for the fintech)**: any rule with strategic-business-model implications; any consent-order-pattern theme that names a peer fintech under similar product or partnership structure.

The escalation triggers are firm-specific; the overlay names the pattern, and `references/firm-overlay.md` overrides with firm-specific thresholds.
