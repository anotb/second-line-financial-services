# Source anchors: fair-lending-test-plan

Cited regulatory sources this skill anchors to. Every primary anchor names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link.

The skill cites these by file path. SKILL.md does not restate excerpts.

## Primary anchors

### 1. Equal Credit Opportunity Act (ECOA)

- Citation: Equal Credit Opportunity Act, 15 U.S.C. §1691 (general prohibition on discrimination in credit transactions); §1691(a) prohibited bases; §1691(d) adverse action notice requirement.
- Excerpt-paraphrase: It is unlawful for any creditor to discriminate against any applicant with respect to any aspect of a credit transaction on the basis of race, color, religion, national origin, sex or marital status, or age (provided the applicant has the capacity to contract); because all or part of the applicant's income derives from any public-assistance program; or because the applicant has in good faith exercised any right under the Consumer Credit Protection Act. The prohibition reaches the entire credit transaction, including marketing, underwriting, pricing, servicing, and adverse action.
- Link: https://www.ecfr.gov/current/title-15/chapter-41/subchapter-IV/section-1691 — §1691(a) prohibited bases
- Notes: ECOA reaches every creditor; the implementing regulation (Regulation B) carries the operational detail.

### 2. Regulation B — 12 CFR Part 1002

- Citation: Regulation B, 12 CFR Part 1002 (CFPB-administered): §1002.4 (general rules), §1002.5 (rules concerning requests for information), §1002.6 (rules concerning evaluation of applications, including the effects-test framing), §1002.7 (rules concerning extensions of credit), §1002.9 (notifications including adverse action), §1002.13 (information for monitoring purposes for dwelling-secured credit).
- Excerpt-paraphrase: §1002.6(a) addresses use of information and contains the effects-test framing under which a creditor's facially neutral practice may violate ECOA where it has a disparate impact and is not justified by business necessity; §1002.6(b) lists specific rules on use of information including age, public-assistance income, and other items. §1002.9 sets the form, content, and timing of adverse action notices; the specific reasons must be the actual principal reasons for the adverse action. §1002.13 covers collection of monitoring information for credit secured by a dwelling.
- Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1002 — Regulation B sections cited above
- Notes: §1002.6 effects-test framing is the core anchor for disparate-impact testing of model features and policies; §1002.9 anchors the adverse-action posture for any AI/ML model in the test perimeter.

### 3. Fair Housing Act (FHA)

- Citation: Fair Housing Act, 42 U.S.C. §3601 to §3619: §3604 (discrimination in the sale or rental of housing and other prohibited practices), §3605 (discrimination in residential real estate-related transactions), §3606 (discrimination in the provision of brokerage services), §3608 (administration; affirmatively further fair housing).
- Excerpt-paraphrase: §3605 prohibits any person or entity whose business includes engaging in residential real estate-related transactions to discriminate against any person in making available such a transaction, or in the terms or conditions of such a transaction, because of race, color, religion, sex, handicap, familial status, or national origin. The transaction definition includes the making or purchasing of loans secured by residential real estate.
- Link: https://www.law.cornell.edu/uscode/text/42/chapter-45/subchapter-I — §3605 residential real-estate transactions
- Notes: FHA reaches dwelling-secured lending and overlaps ECOA on race, national origin, sex, and (uniquely on the FHA side) handicap and familial status.

### 4. HUD Disparate Impact Rule — 24 CFR §100.500

- Citation: HUD regulation implementing the Fair Housing Act discriminatory-effects standard, 24 CFR §100.500 (current text following the 2023 reinstated rule).
- Excerpt-paraphrase: A practice has a discriminatory effect where it actually or predictably results in a disparate impact on a group of persons or creates, increases, reinforces, or perpetuates segregated housing patterns because of a protected characteristic. The rule sets a burden-shifting framework: plaintiff or charging party shows discriminatory effect; defendant shows the challenged practice is necessary to achieve one or more substantial, legitimate, nondiscriminatory interests; plaintiff or charging party then shows the interests could be served by another practice with less discriminatory effect.
- Link: https://www.ecfr.gov/current/title-24/subtitle-B/chapter-I/subchapter-A/part-100/subpart-G/section-100.500 — 24 CFR §100.500 burden-shifting framework
- Notes: The discriminatory-effects rule is the FHA-side anchor for disparate-impact testing and for less-discriminatory-alternative search. Reinstated by HUD in 2023 after revision and litigation history.

### 5. HMDA / Regulation C — 12 CFR Part 1003

- Citation: Home Mortgage Disclosure Act and Regulation C, 12 CFR Part 1003 (CFPB-administered). §1003.4 (compilation of reportable data); §1003.5 (disclosure and reporting); Appendix A (data points).
- Excerpt-paraphrase: Covered institutions report Loan/Application Register (LAR) data points including action taken, applicant demographic information (ethnicity, race, sex), income, loan purpose, occupancy, lien status, AUS recommendation, denial reasons, rate spread, and points-and-fees for HMDA-reportable transactions. The LAR is the principal data source for mortgage fair-lending statistical analysis.
- Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1003 — 12 CFR Part 1003 §1003.4 and Appendix A data points
- Notes: HMDA self-reported demographics anchor mortgage fair-lending tests; Reg C also establishes peer-aggregate data that supports comparator-set construction in redlining tests.

### 6. FFIEC Interagency Fair Lending Examination Procedures

- Citation: Federal Financial Institutions Examination Council, Interagency Fair Lending Examination Procedures (current edition; FFIEC distributes the manual on behalf of FRB, OCC, FDIC, NCUA) [verify edition date].
- Excerpt-paraphrase: The procedures set the supervisory methodology for fair-lending examination including risk assessment, scoping, comparative file review (matched-pair design), statistical analysis (including regression for underwriting and pricing), redlining analysis, and steering analysis. The procedures define risk factors, focal points, and the comparator-construction approach examiners use; second-line test plans typically anchor methodology to the same procedures.
- Link: https://www.ffiec.gov/pdf/fairlend.pdf — Interagency Fair Lending Examination Procedures, Part I (Risk Assessment) and Part II (Examination Procedures) [verify section]
- Notes: The procedures are not a binding rule on the institution; they describe how examiners examine. The institution's own test plan inherits the methodology because that is the methodology it will be examined against.

### 7. CFPB Fair Lending Report (annual report to Congress)

- Citation: Consumer Financial Protection Bureau, Fair Lending Report (annual; most recent edition) [verify edition year].
- Excerpt-paraphrase: The annual fair-lending report sets out the bureau's supervision and enforcement priorities, focal product lines, and emerging-issue posture. Recent editions have addressed mortgage redlining, indirect auto, small-business lending under Section 1071, algorithmic discrimination, and digital marketing of consumer credit.
- Link: https://www.consumerfinance.gov/data-research/research-reports/fair-lending-reports/ — CFPB Fair Lending Reports, supervisory-priorities section [verify section]
- Notes: The report is a supervisory-priority signal, not a rule. Test-plan scope often references the most recent report's focal items.

### 8. CFPB Circular 2022-03 — Adverse action and complex algorithms

- Citation: CFPB Circular 2022-03 (May 26, 2022), "Adverse action notification requirements in connection with credit decisions based on complex algorithms".
- Excerpt-paraphrase: Creditors using complex algorithms must still provide a statement of specific reasons to applicants against whom adverse action is taken; the complexity of the model is not a defence to the specificity requirement under ECOA / Regulation B (15 USC §1691; 12 CFR §1002.9). The circular addresses a recurring industry posture that black-box models exempt the creditor from the specificity obligation; the bureau's position is that they do not.
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/ — Circular sections "Question Presented" and "Response"
- Notes: Test plans that include AI/ML models in the underwriting perimeter consume this circular as part of the framing for adverse-action sampling and for the model-feature-review test type.

### 9. CFPB Circular 2023-03 — Adverse action notices and sample reason codes

- Citation: CFPB Circular 2023-03 (September 19, 2023), "Adverse action notification requirements and the proper use of the CFPB's sample forms provided in Regulation B".
- Excerpt-paraphrase: Creditors cannot rely on illegitimate reasons in adverse action notices, including reasons not actually relied upon in the adverse decision. Reasons given must be the actual principal reasons for the adverse action, even when sample reason codes are used. The circular reinforces and extends the 2022-03 position for AI/ML and complex models.
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2023-03-adverse-action-notification-requirements-and-the-proper-use-of-the-cfpbs-sample-forms-provided-in-regulation-b/ — Circular section "Required Information"
- Notes: Anchors the LDA-search expectation for any AI/ML model in scope; the bureau's framing is that creditors using complex models actively look for less-discriminatory alternatives and document the search.

### 10. Joint Statement on Enforcement of Civil Rights, Fair Lending, Fair Housing, and Consumer Financial Protection Laws (April 2023)

- Citation: Joint Statement issued April 25, 2023 by the Consumer Financial Protection Bureau, the Civil Rights Division of the Department of Justice, the Federal Trade Commission, and the Equal Employment Opportunity Commission, "Joint Statement on Enforcement Efforts Against Discrimination and Bias in Automated Systems".
- Excerpt-paraphrase: The four agencies confirm that existing legal authorities apply to the use of automated systems and innovative new technologies, including in the consumer financial-services context. Discrimination and bias in automated systems are enforceable under the agencies' existing statutes; novel technology is not a defence.
- Link: https://www.consumerfinance.gov/about-us/newsroom/cfpb-federal-partners-confirm-automated-systems-advanced-technology-not-an-excuse-for-lawbreaking-behavior/ — Joint Statement text, signatories section
- Notes: Anchors the algorithmic-discrimination framing across ECOA, FHA, FCRA, FTC Act §5, and Title VII for the FS perimeter.

### 11. HUD guidance on AI / algorithmic underwriting

- Citation: HUD Office of Fair Housing and Equal Opportunity guidance on artificial-intelligence underwriting and tenant-screening, including the May 2024 guidance "Guidance on Application of the Fair Housing Act to the Screening of Applicants for Rental Housing" and prior FHEO communications addressing algorithmic underwriting in residential lending [verify exact title and date].
- Excerpt-paraphrase: HUD has issued a series of FHEO communications addressing algorithmic underwriting, automated valuation, and tenant-screening tools, restating that the FHA's prohibitions apply to model-driven decisions and that the discriminatory-effects framework under 24 CFR §100.500 reaches algorithmic underwriting practices.
- Link: https://www.hud.gov/program_offices/fair_housing_equal_opp — HUD FHEO guidance index [verify exact section]
- Notes: HUD has issued multiple post-2023 FHEO communications; verify the exact title and date for the citation in any given test plan.

### 12. CFPB UDAAP — Examination Manual

- Citation: CFPB Supervision and Examination Manual, UDAAP module (current edition) [verify edition date].
- Excerpt-paraphrase: The UDAAP module sets out the bureau's framework for unfair, deceptive, or abusive acts or practices under sections 1031 and 1036 of the Consumer Financial Protection Act. The framework defines the elements of each prong (unfairness: substantial injury, not reasonably avoidable, not outweighed by benefits; deception: material misrepresentation; abusiveness: interference with the ability to understand, taking unreasonable advantage), and is applied alongside fair-lending review where consumer-outcome themes overlap discrimination themes.
- Link: https://www.consumerfinance.gov/compliance/supervision-examinations/ — CFPB Supervision and Examination Manual, UDAAP module section [verify section]
- Notes: UDAAP overlaps fair-lending review on themes such as marketing claims, dark patterns, and steering. See `references/cross-cutting/conduct.md`.

### 13. DOJ Combatting Redlining Initiative

- Citation: U.S. Department of Justice, Combatting Redlining Initiative (announced October 22, 2021); subsequent public consent orders and complaints filed jointly with CFPB, OCC, and state AGs (2021 to current).
- Excerpt-paraphrase: The DOJ initiative addresses lending discrimination on the basis of race, ethnicity, and national origin, focusing on redlining patterns: lenders that avoid providing credit to majority-minority areas. Public consent orders set comparator-MSA selection patterns, peer-set construction, marketing-distribution evidence, and remedial-program design templates that subsequent test plans treat as reference patterns.
- Link: https://www.justice.gov/crt/combating-redlining-initiative — initiative overview section and case index
- Notes: Public consent orders are the empirical reference for redlining test scoping; the worked example in `examples/mortgage-redlining-test.md` derives its structural pattern from this body.

### 14. BISG methodology

- Citation: Consumer Financial Protection Bureau, "Using publicly available information to proxy for unidentified race and ethnicity: A methodology and assessment" (Summer 2014; subsequent CFPB technical updates) [verify current methodology document].
- Excerpt-paraphrase: The Bayesian Improved Surname Geocoding (BISG) method combines census-derived geographic distribution of race and ethnicity with surname-derived priors to produce a probability distribution over race and ethnicity for an individual whose race and ethnicity are not self-reported. The CFPB methodology paper documents the construction, accuracy, and known limitations including geographic and surname-distribution variation.
- Link: https://files.consumerfinance.gov/f/201409_cfpb_report_proxy-methodology.pdf — CFPB BISG methodology paper (Summer 2014), methodology section
- Notes: BISG is the dominant proxy method for non-mortgage consumer credit; mortgage fair-lending continues to use HMDA self-reported demographics where available. Test plans should record the proxy method per test and the proxy-uncertainty handling.

### 15. ECOA Reg B §1002.13 — Information for monitoring purposes

- Citation: 12 CFR §1002.13 ("Information for monitoring purposes"), addressing collection of applicant ethnicity, race, sex, marital status, and age for credit primarily for the purchase or refinancing of a principal residence secured by such dwelling.
- Excerpt-paraphrase: Creditors that receive applications for credit primarily for the purchase or refinancing of a dwelling occupied or to be occupied by the applicant as a principal residence must request the listed monitoring information; collection rules and the form of request are set in the section. The monitoring data feeds the test population for dwelling-secured fair-lending review.
- Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1002/section-1002.13 — 12 CFR §1002.13
- Notes: Anchors the demographic-data inputs for mortgage tests; non-dwelling-secured credit relies on proxy methods (BISG) where self-reported demographics are not collected.

### 16. CFPB Section 1071 small-business data rule (Regulation B subpart B)

- Citation: CFPB Final Rule on Small Business Lending under the Equal Credit Opportunity Act (Section 1071 of the Dodd-Frank Act), implementing 12 CFR §1002.101 to §1002.114.
- Excerpt-paraphrase: Covered financial institutions must compile, maintain, and submit data on credit applications by small businesses, including data on the protected demographic characteristics of the principal owners (race, ethnicity, sex). The rule extends a HMDA-style data infrastructure to the small-business credit perimeter; fair-lending test plans for in-scope small-business products consume the §1071 data once collected.
- Link: https://www.consumerfinance.gov/rules-policy/final-rules/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b/ — final rule, Subpart B sections §1002.101 to §1002.114
- Notes: §1071 readiness is a separate skill; this skill consumes §1071 data once it exists for in-scope products. Compliance dates and tier phase-in are subject to ongoing litigation; verify operative effective date at plan time.

## Secondary anchors (sector and cross-cutting)

### 17. Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 2023)

- Citation: OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, "Interagency Guidance on Third-Party Relationships: Risk Management" (issued June 6, 2023).
- Excerpt-paraphrase: The interagency guidance sets risk-management expectations for banking organizations engaging third parties, including fintech and AI vendors. Where a sponsor-bank arrangement involves third-party-developed underwriting or marketing models, the bank retains accountability; fair-lending second-line review duties allocate per the program agreement and the bank's own fair-lending program.
- Link: https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-17.html — Bulletin 2023-17
- Notes: Payments-fintech sector overlay anchor; relevant where the test plan covers a sponsor-bank fintech program.

### 18. SR 11-7 — Guidance on Model Risk Management

- Citation: Federal Reserve SR 11-7 / OCC Bulletin 2011-12, "Guidance on Model Risk Management" (April 4, 2011), §V (Model Documentation) and §VI (Third-Party Models).
- Excerpt-paraphrase: SR 11-7 sets the supervisory expectation for model risk management at federally regulated banks; documentation and validation expectations are the structural anchor for any model in the fair-lending test perimeter. The fair-lending test plan and the model card consume each other's outputs (the card states intended use, fairness method, and limitations; the test plan stresses those statements).
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm — §V and §VI
- Notes: OCC Bulletin 2026-13 refreshes the model risk framework but does not extend it to generative AI, retrieval-augmented generation, tool use, or agentic AI; cite at plan time the operative bulletin per the bank's primary federal regulator. For GenAI / RAG / tool-use / agentic-AI scope, anchor to NIST AI RMF (1.0, January 2023), NIST AI 600-1 (Generative AI Profile, July 2024), and the EU AI Act (Regulation (EU) 2024/1689) where extraterritorial reach applies; the AI / ML overlay block in the plan body cites these directly.

### 19. GLBA Safeguards Rule — 16 CFR Part 314

- Citation: Gramm-Leach-Bliley Act Safeguards Rule, 16 CFR Part 314 (FTC; financial institutions not under primary federal banking regulator supervision); 12 CFR Part 30 Appendix B (OCC parallel for national banks); 12 CFR Part 364 Appendix B (FDIC parallel).
- Excerpt-paraphrase: Financial institutions must maintain a written information security program with administrative, technical, and physical safeguards for non-public personal information. The rule addresses data classification, access controls, and incident response; the program reaches NPI used in fair-lending testing (applicant data, model features, BISG inputs).
- Link: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 — 16 CFR Part 314
- Notes: Privacy cross-cutting overlay anchor; relevant to how applicant data is moved and processed for test execution. See `references/cross-cutting/privacy.md`.

### 20. NAIC Unfair Trade Practices framing (insurance scope boundary)

- Citation: NAIC Unfair Trade Practices Act (Model #880); state-DOI unfair-discrimination statutes implementing the model.
- Excerpt-paraphrase: Insurance underwriting and pricing discrimination is regulated under state-DOI unfair-discrimination statutes, not under ECOA or the FHA (subject to narrow exceptions where insurance products are sold as part of a credit transaction). The vocabulary is "unfair discrimination" rather than "fair lending"; the substantive tests differ (actuarial-justification framing rather than ECOA effects-test framing).
- Link: https://content.naic.org/sites/default/files/MO880.pdf — Model #880, unfair-discrimination section [verify section]
- Notes: Insurance overlay anchor; the fair-lending test plan typically does not extend into insurance products. Where the institution sells credit-protection insurance bundled with a credit product, the credit-side decision is in scope and the insurance-side decision is out of scope.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at SKILL.md write time and at plan-write time:

- FFIEC Interagency Fair Lending Examination Procedures — confirm current edition and date.
- CFPB Fair Lending Report — confirm most recent annual edition cited at plan time.
- HUD FHEO algorithmic-underwriting guidance — confirm exact title and date for the guidance cited at plan time.
- CFPB UDAAP Examination Manual — confirm current edition.
- CFPB BISG methodology — confirm whether subsequent technical updates supersede the Summer 2014 methodology paper.
- CFPB Section 1071 — confirm operative compliance dates per current litigation status.
- NAIC Model #880 — confirm current model edition.

Where verification is incomplete, the SKILL.md cites with the `[verify section]` flag carried forward; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy, and named owners via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. An advisory firm shipping a client-specific overlay does the same thing under a separate overlay file.
