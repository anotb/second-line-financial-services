# Source anchors: board-ai-risk-pack

Cited regulatory sources this skill anchors to. Every primary anchor names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link.

The skill cites these by file path. SKILL.md does not restate excerpts.

## Primary anchors

### 1. NIST AI Risk Management Framework 1.0 — Govern function

- Citation: National Institute of Standards and Technology, AI Risk Management Framework 1.0 (January 2023), Govern function, subcategories Govern 1.x (organisational governance and policies), Govern 4.x (accountability structures, roles, and responsibilities), Govern 6.x (third-party considerations), Govern 5.x (consultation and engagement with affected communities).
- Excerpt-paraphrase: The Govern function establishes that a culture of risk management is cultivated and present, that AI risk management is integrated and supported across the organization, that organizational structures, roles, and responsibilities related to AI risk management are clear, and that issues related to third-party AI are addressed. The board AI risk pack is the standing instrument by which the AI risk committee discharges its responsibilities under Govern 1.x and Govern 4.x; the vendor exposure section anchors to Govern 6.x; the policy and framework changes section anchors to Govern 1.x organisational policies.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Govern function section, Govern 1.x, 4.x, 6.x subcategories
- Notes: NIST AI RMF 1.0 is voluntary, not binding; it is the dominant framing US firms use for AI governance maturity narrative. The bank model-risk bulletin (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026) excludes generative AI and agentic AI from its scope, so for those use cases NIST is the substantive anchor. Subcategory numbering verified against NIST AI RMF 1.0 publication.

### 2. NIST AI 600-1 — Generative AI Profile

- Citation: NIST AI 600-1, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (July 2024), Govern, Map, Measure, and Manage subcategories specific to GenAI [verify exact Govern and Manage subcategory numbering at pack-write time].
- Excerpt-paraphrase: NIST AI 600-1 extends the AI RMF for GenAI-specific risks: confabulation, dangerous or violent content, data privacy, environmental impacts, harmful bias, human-AI configuration, information integrity, information security, intellectual property, obscene content, value chain and component integration. The GenAI program status section of the pack anchors to this profile; the foundation-model and AI vendor exposure section anchors to value-chain and component-integration subcategories; the incident classification taxonomy aligns to the named risk categories.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Generative AI Profile (NIST AI 600-1) [verify section]
- Notes: Subcategory numbering confirmed at pack-write time; verification flag carried until the published profile section refs are pinned.

### 3. Joint Interagency Revised Guidance on Model Risk Management — OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026

- Citation: Joint Interagency Revised Guidance on Model Risk Management, OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, dated April 17, 2026. The three issuances are the same joint document; supersedes SR 11-7 (2011) and SR 21-8 (2021).
- Excerpt-paraphrase (footnote 3, verbatim): "Generative AI and agentic AI models are novel and rapidly evolving. As such, they are not within the scope of this guidance. ... However, the principles described in this guidance apply to traditional statistical and quantitative models and non-generative, non-agentic AI models." Most relevant to banking organizations with over $30 billion in total assets; non-binding.
- Link: https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf — guidance text PDF
- Notes: For traditional models in the firm's inventory and the model performance trends section, this is the current anchor at federally regulated banks. For GenAI and agentic use cases (which dominate the GenAI program status and foundation-model exposure sections of this pack) the bulletin is out of scope; those sections anchor to NIST AI RMF, NIST AI 600-1, ISO/IEC 42001, NAIC Bulletin (insurers), NYDFS October 2024 letter, and the EU AI Act where applicable.

### 4. Federal Reserve SR 11-7 — Guidance on Model Risk Management, §II and §III (superseded; cited for historical framing only)

- Citation: Board of Governors of the Federal Reserve System, Supervision and Regulation Letter SR 11-7 / OCC Bulletin 2011-12, "Guidance on Model Risk Management" (April 4, 2011), §II "Overview of Model Risk Management" and §III "Model Risk Governance".
- Excerpt-paraphrase: §II framed board and senior-management responsibilities for model risk. §III set governance, policies, and controls expectations including the role of an oversight committee, written policies, internal standards, periodic reporting, and the model inventory. As of April 17, 2026 it is superseded by the joint interagency Revised Guidance on Model Risk Management (anchor 3) for federally regulated banks; SR 21-8 is also superseded.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm — sections §II and §III
- Notes: Superseded for binding purposes by OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026 as of April 17 2026. Cite for historical framing only.

### 5. ISO/IEC 42001:2023 — Artificial Intelligence Management System

- Citation: ISO/IEC 42001:2023 "Information technology — Artificial intelligence — Management system", §5.1 "Leadership and commitment", §6.2 "AI objectives and planning to achieve them", §9.3 "Management review".
- Excerpt-paraphrase: §5.1 sets leadership and commitment expectations including establishment of the AI policy and AI objectives, integration of the AI management system into business processes, and assignment of roles and responsibilities. §6.2 requires AI objectives that are measurable, monitored, and updated. §9.3 requires top management to review the AI management system at planned intervals to ensure continuing suitability, adequacy, and effectiveness, with named inputs and outputs. The board AI risk pack is one of the standing inputs to §9.3 management review for firms operating an AI management system, with the AI governance maturity posture section the bridge between pack and management review.
- Link: https://www.iso.org/standard/42001 — ISO/IEC 42001:2023 §5.1, §6.2, §9.3
- Notes: ISO/IEC 42001 is voluntary/certifiable; firms pursuing certification consume this anchor as the AI management-system frame. The §9.3 management-review inputs and outputs list is the authoritative checklist for the maturity section content.

### 6. NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)

- Citation: National Association of Insurance Commissioners, "Model Bulletin: Use of Artificial Intelligence Systems by Insurers" (adopted December 4, 2023), Sections 1-4 (general expectations) and the AIS Program elements (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness).
- Excerpt-paraphrase: Insurers using AI systems are expected to adopt and implement an AIS Program addressing the named elements. The committee reporting expectation is that insurers maintain documentation supporting the AIS Program and report appropriately to senior management and the board on AI program status, AI use case inventory, testing and validation outcomes, and third-party AI oversight. The insurance-sector overlay of the board AI risk pack is structured around the AIS Program elements; the AI governance maturity section in insurance packs maps each element to current posture.
- Link: https://content.naic.org/sites/default/files/inline-files/2023-12-4%20Model%20Bulletin_Adopted_0.pdf — Model Bulletin Sections 1-4 and AIS Program elements
- Notes: NAIC Bulletin is a model bulletin; binding only to the extent state DOIs adopt it. State adoption tracker maintained by the NAIC AI Working Group is the public reference for binding-status confirmation per jurisdiction.

### 7. NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024)

- Citation: NYDFS Industry Letter, "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks" (October 16, 2024), [verify section] on board-level AI cyber posture, AI-enabled threats (deepfake, social engineering), prompt-injection-related risks, and the firm's own use of AI as a cyber surface.
- Excerpt-paraphrase: Covered entities under 23 NYCRR Part 500 are expected to address AI-related cybersecurity risks in their cybersecurity program, including threats enabled by AI (deepfakes, AI-aided social engineering, AI-aided phishing), risks from the firm's own use of AI (prompt injection, data exposure through AI systems, vendor concentration on AI providers), and the board oversight responsibility for the cybersecurity program covers AI-related risk. The board AI risk pack carries the cyber cross-cutting overlay content for NY-footprint firms with NYDFS as a primary regulator.
- Link: https://www.dfs.ny.gov/industry-guidance/industry-letters — Industry Letter October 16, 2024 [verify section]
- Notes: Cyber cross-cutting overlay anchor; relevant to the foundation-model concentration narrative and the prompt-injection signal in the GenAI program status section.

### 8. EU AI Act — Article 9 (risk management system) and Article 26 (deployer obligations)

- Citation: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 9 "Risk management system" and Article 26 "Obligations of deployers of high-risk AI systems".
- Excerpt-paraphrase: Article 9 requires providers of high-risk AI systems to establish, implement, document, and maintain a risk management system as a continuous iterative process planned and run throughout the entire lifecycle. Article 26 sets deployer obligations including monitoring the operation of the high-risk AI system on the basis of the instructions for use, informing the provider when serious incidents are observed, and keeping logs. The board AI risk pack is the standing committee instrument by which deployers in scope evidence Article 26 monitoring and incident-notification posture; for in-house high-risk providers, the pack is also the standing input to the Article 9 risk-management-system review.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 9 and Article 26
- Notes: Applies to firms with EU-deployer or EU-provider exposure; phasing dates and AI Office guidance are evolving. The deployer-versus-provider distinction governs which of Article 9 or Article 26 obligations apply; cross-link to `ai-act-triage`.

### 9. BCBS 239 — Principles for Effective Risk Data Aggregation and Risk Reporting

- Citation: Basel Committee on Banking Supervision, "Principles for effective risk data aggregation and risk reporting" (BCBS 239, January 2013), Principles 7-11 (risk reporting practices), Principle 3 (data accuracy and integrity).
- Excerpt-paraphrase: BCBS 239 sets data aggregation and risk reporting principles for global and domestic systemically important banks. Principles 7-11 cover accuracy, comprehensiveness, clarity and usefulness, frequency, and distribution of risk reports. Principle 3 covers data accuracy and integrity. The data confidence label on the AI inventory aggregation in the board pack is BCBS 239-anchored for firms in scope (G-SIB, D-SIB) and is leading practice for any firm aggregating AI inventory data through enterprise data infrastructure.
- Link: https://www.bis.org/publ/bcbs239.htm — Principles 3, 7-11
- Notes: BCBS 239 applies directly to G-SIBs and is national-supervisor-extended to D-SIBs in many jurisdictions. The AI inventory completeness statement in the appendix uses the BCBS 239 voice (known limitations, restatements) where the firm is in scope.

## Secondary anchors (sector and cross-cutting)

### 10. OCC Heightened Standards (12 CFR Part 30 Appendix D) — board oversight of risk-governance framework

- Citation: 12 CFR Part 30 Appendix D, "OCC Guidelines Establishing Heightened Standards for Certain Large Insured National Banks, Insured Federal Savings Associations, and Insured Federal Branches", Section II "Risk Governance Framework" and Section III "Board of Directors".
- Excerpt-paraphrase: The Heightened Standards apply to OCC-supervised banks meeting an asset-size threshold. Section II requires a written risk governance framework with named components; Section III sets board responsibilities for oversight of the framework, the risk appetite statement, and the chief risk executive. AI risk management sits within the operational and model risk components of the framework; the board AI risk pack is one of the standing instruments for board oversight of AI risk under Section III.
- Link: https://www.ecfr.gov/current/title-12/chapter-I/part-30 — 12 CFR Part 30 Appendix D Section II and Section III
- Notes: Banking sector overlay anchor; reach is OCC large-bank only.

### 11. Federal Reserve SR 12-17 — Consolidated Supervision Framework for Large Financial Institutions

- Citation: Federal Reserve Supervision and Regulation Letter SR 12-17 (December 17, 2012), "Consolidated Supervision Framework for Large Financial Institutions", expectations for board and senior management oversight including risk management and internal controls.
- Excerpt-paraphrase: SR 12-17 sets the FRB framework for consolidated supervision of large financial institutions, including board responsibility to oversee risk management practices, the maintenance of an effective independent risk-management function, and the management of issues including supervisory matters requiring attention. The board AI risk pack's regulator and exam interactions section consumes the SR 12-17 framing for the over-age MRA / MRIA management expectation.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1217.htm — SR 12-17
- Notes: Banking sector overlay anchor; reach is FRB large-financial-institution.

### 12. SEC Investment Advisers Act Rule 206(4)-7 — Compliance program rule

- Citation: 17 CFR 275.206(4)-7 (Compliance procedures and practices).
- Excerpt-paraphrase: Investment advisers must adopt and implement written policies and procedures reasonably designed to prevent violation of the IAA, conduct an annual review of those policies and procedures, and designate a chief compliance officer. The annual review is a standing input to the AI risk committee at adviser firms; AI use cases supporting advisory recommendations or client communications are in scope of the program.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 — 17 CFR §275.206(4)-7
- Notes: Capital-markets sector overlay anchor.

### 13. SEC Investment Advisers Act Rule 206(4)-1 — Marketing Rule

- Citation: 17 CFR 275.206(4)-1 ("Investment Adviser Marketing").
- Excerpt-paraphrase: Marketing communications by investment advisers, including those generated or assisted by AI, are subject to general prohibitions, performance-presentation rules, and testimonial/endorsement requirements. AI-generated client communications fall within scope where they meet the definition of an advertisement. The capital-markets sector overlay of the board AI risk pack carries the Marketing Rule scope statement on AI-generated client communications.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 — 17 CFR §275.206(4)-1
- Notes: Capital-markets sector overlay anchor.

### 14. NYDFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024)

- Citation: NYDFS Insurance Circular Letter on the Use of Artificial Intelligence Systems and External Consumer Data and Information Sources in Insurance Underwriting and Pricing (January 17, 2024), [verify section] on governance, fairness testing, disclosure, and consumer recourse.
- Excerpt-paraphrase: The Circular Letter sets governance, fairness testing, disclosure, and consumer-recourse expectations for life-insurance underwriting and pricing using AI and ECDIS. Insurers are expected to maintain documentation supporting the use of each AI/ECDIS element and report on AIS Program status to senior management. The insurance-sector overlay of the board AI risk pack carries the NY-footprint life-insurance writer framing.
- Link: https://www.dfs.ny.gov/industry-guidance/circular-letters — Insurance Circular Letter (January 2024) [verify section]
- Notes: Insurance sector overlay anchor for NY footprint.

### 15. Colorado Division of Insurance regulation implementing SB 21-169 (life-insurance underwriting)

- Citation: Colorado Division of Insurance, regulation implementing SB 21-169 (governance and risk management of ECDIS and predictive models in life-insurance underwriting) [verify regulation number and effective date].
- Excerpt-paraphrase: Carriers using ECDIS or predictive models in life-insurance underwriting in Colorado must implement a governance and risk-management framework, including a written policy, testing for unfair discrimination, consumer disclosure, and recourse. The committee reporting expectation is that the framework's status and testing outcomes are reported to the board or designated committee. The insurance-sector overlay of the board AI risk pack carries the CO life-insurance writer framing.
- Link: https://doi.colorado.gov/insurance-products/life-insurance/algorithm-and-predictive-model-governance — CO regulation [verify section]
- Notes: Insurance sector overlay anchor for CO footprint.

### 16. CFPB Circular 2022-03 — Adverse action notification requirements when using AI or complex algorithms

- Citation: CFPB Circular 2022-03 (May 26, 2022), "Adverse action notification requirements in connection with credit decisions based on complex algorithms".
- Excerpt-paraphrase: Creditors using complex algorithms must still provide a statement of specific reasons to applicants against whom adverse action is taken; the complexity of the model is not a defence to the specificity requirement under ECOA / Regulation B (15 USC §1691; 12 CFR §1002.9). The conduct cross-cutting overlay of the board AI risk pack carries the adverse action notice posture for consumer-credit AI use cases.
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/ — Circular Section 1 and Section 2
- Notes: Conduct cross-cutting overlay anchor; complaint trend by AI-touched product is the standing committee data point.

### 17. Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 6, 2023)

- Citation: OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, "Interagency Guidance on Third-Party Relationships: Risk Management" (issued June 6, 2023), Risk Management Life Cycle sections.
- Excerpt-paraphrase: The interagency guidance sets risk-management expectations for banking organizations engaging third parties, including fintech and AI vendors. The guidance covers planning, due diligence and third-party selection, contract negotiation, ongoing monitoring, and termination. The vendor exposure section of the board AI risk pack consumes the interagency guidance framing for foundation-model providers, evaluation vendors, RAG infrastructure providers, and agent platforms; the payments-fintech sector overlay carries sponsor-bank framing.
- Link: https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-17.html — Bulletin 2023-17 Risk Management Life Cycle
- Notes: Banking and payments-fintech sector overlay anchor.

### 18. FRB SR 19-3 — Compliance and Operational Risk Management Programs

- Citation: Federal Reserve Supervision and Regulation Letter SR 19-3 (February 26, 2019), "Compliance and Operational Risk Management Programs at Large Financial Institutions"; relates to FRB tailoring framework expectations.
- Excerpt-paraphrase: SR 19-3 sets framework expectations for compliance and operational risk management at large financial institutions including board and senior management oversight, independent compliance and operational risk management functions, and reporting. AI use cases in scope of the firm's compliance or operational risk taxonomies surface here; the board AI risk pack consumes SR 19-3 framing for the regulator interactions and AI governance maturity sections.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1903.htm — SR 19-3
- Notes: Banking sector overlay anchor.

### 19. FINRA — AI guidance and supervision framework expectations

- Citation: FINRA, "Artificial Intelligence in the Securities Industry" (2020 report) and subsequent FINRA notices on AI supervision expectations [verify exact notice numbers and dates at pack-write time].
- Excerpt-paraphrase: FINRA expects member firms to apply existing supervisory and risk-management frameworks to AI applications in the securities business, including supervision of AI-generated communications, oversight of AI-driven trading and surveillance systems, and recordkeeping for AI-supported decisions. The capital-markets sector overlay of the board AI risk pack consumes the FINRA framing for broker-dealer AI use cases.
- Link: https://www.finra.org/rules-guidance/key-topics/fintech/artificial-intelligence — FINRA AI guidance section [verify section]
- Notes: Capital-markets sector overlay anchor; specific FINRA notices on AI verified at pack-write time.

### 20. SEC Adviser Books-and-Records Rule 204-2

- Citation: 17 CFR 275.204-2 (Books and records to be maintained by investment advisers).
- Excerpt-paraphrase: Books-and-records rules require advisers to make and preserve records supporting their recommendations and advisory activities. AI-generated content supporting a recommendation or client communication falls within the records-preservation scope. The capital-markets sector overlay of the board AI risk pack carries the books-and-records posture for AI-generated content under the program.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.204-2 — 17 CFR §275.204-2
- Notes: Capital-markets sector overlay anchor.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at pack-write time:

- OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026 — verbatim GenAI/agentic scope exclusion confirmed against the OCC PDF (footnote 3). The three issuances are the same joint document, not parallels. SR 11-7 and SR 21-8 are confirmed superseded as of April 17 2026.
- NIST AI 600-1 — confirm exact Govern and Manage subcategory numbering for the GenAI elements cited.
- NYDFS Industry Letter on AI cybersecurity (October 2024) — confirm section reference for board-oversight language.
- NYDFS Insurance Circular Letter (January 2024) — confirm section reference.
- Colorado Division of Insurance regulation implementing SB 21-169 — confirm regulation number and effective date.
- FINRA AI notices — confirm exact notice numbers and dates relied on.

Where verification is incomplete, the SKILL.md cites with the `[verify section]` flag carried forward in this file; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy, named owners, threshold values, and committee charter via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. An advisory firm shipping a client-specific overlay does the same thing under a separate overlay file.
