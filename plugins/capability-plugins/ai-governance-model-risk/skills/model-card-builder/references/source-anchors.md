# Source anchors: model-card-builder

Cited regulatory sources this skill anchors to. Every primary anchor names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link.

The skill body cites these by file path; this file carries the citations.

A practitioner note before the list: the model-risk anchors and the AI-specific anchors are distinct and load against different parts of the card. The 2026 joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026) covers the model-card baseline for traditional statistical or quantitative models in scope of bank model-risk programs. It supersedes SR 11-7 (2011) and SR 21-8 (the 2021 BSA/AML model-risk interagency statement). It is most relevant to banking organizations with total assets over $30 billion and is non-binding (does not set forth enforceable standards). Footnote 3 of the joint guidance text expressly excludes generative AI and agentic AI from its scope; for the GenAI overlay in this card (foundation-model dependence, RAG corpus, tool use, prompt-injection robustness, content provenance, autonomy-level uplift) the binding anchors are the AI-specific frameworks (NIST AI RMF, NIST AI 600-1, ISO/IEC 42001) and the sector and cross-cutting overlays (NAIC AI Bulletin, NYDFS October 2024 letter, EU AI Act where applicable). The 2026 joint guidance does not reference NIST AI RMF or NIST AI 600-1; those are separate, voluntary, non-bank-supervisory frameworks. Be explicit about which scope is in play in any individual card.

## Primary anchors

### 1. Joint Interagency Revised Guidance on Model Risk Management (2026)

- Citation: OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, "Revised Guidance on Model Risk Management" (April 17, 2026). One joint document with three bibliographic anchors. Supersedes SR 11-7 (2011) and SR 21-8 (the 2021 BSA/AML model-risk interagency statement); FDIC rescinded FIL-22-2017 and FIL-27-2021 in parallel.
- Excerpt-paraphrase: Section II defines an in-scope model as "a complex quantitative method, system, or approach that applies statistical, economic, or financial theories to process input data into quantitative estimates," and explicitly excludes "simple arithmetic calculations, such as those found within spreadsheets, as well as deterministic rule-based processes and software where there are no statistical, economic, or financial theories underpinning their design or use." Footnote 3 excludes generative AI and agentic AI: "Generative AI and agentic AI models are novel and rapidly evolving. As such, they are not within the scope of this guidance. Nonetheless, a banking organization's risk management and governance practices should guide the determination of appropriate governance and controls for any tools, processes, or systems not covered in this document. However, the principles described in this guidance apply to traditional statistical and quantitative models and non-generative, non-agentic AI models." Section II clarifies the guidance "is expected to be most relevant to banking organizations with over $30 billion in total assets" and is non-binding ("non-compliance with this guidance will not result in supervisory criticism" since it does "not set forth enforceable standards or prescriptive requirements"). The model card produced by this skill is the firm-side documentation artifact aligned to the principles articulated in the joint guidance for in-scope traditional models.
- Link: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf (joint guidance PDF, 12 pages); https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm; https://www.fdic.gov/news/financial-institution-letters/2026/agencies-revise-interagency-model-risk-management-guidance
- Notes: Anchor for traditional model-risk framing in covered banking organizations. The joint guidance does not reference NIST AI RMF, NIST AI 600-1, or any other NIST publication (a `grep` of the 12-page PDF returns zero NIST matches). Do not cite this bulletin for GenAI, RAG, tool-use, or agentic-AI documentation expectations; for those, route to the AI-specific anchors (NIST AI RMF, NIST AI 600-1, ISO/IEC 42001) and sector and cross-cutting overlays. Where the firm is below the $30B materiality threshold or is not a bank, the guidance is referenced as a leading-practice anchor only, not as a controlling standard. The supersession of SR 21-8 is consequential for AML monitoring cards that previously cited it; the new joint guidance covers BSA/AML model use under its general principles but stops short of bank-AML-specific prescription.

### 3. NIST AI Risk Management Framework 1.0

- Citation: National Institute of Standards and Technology, AI Risk Management Framework 1.0 (January 2023), Map function (Map 1.1, Map 2.x), Measure function (Measure 2.x), Manage function (Manage 3.x).
- Excerpt-paraphrase: Map 1.1 covers establishing context for the AI system including intended purpose; Map 2.1 covers categorisation and classification. Measure 2.x covers performance, robustness, fairness, and explainability metrics for the system, including segment-level reporting. Manage 3.x covers deployment monitoring and risk-response. The card's intended-use, performance, robustness/fairness, and monitoring sections align to these subcategories.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Map function and Measure function subcategories cited in section 2 above
- Notes: NIST AI RMF 1.0 is voluntary, not binding; it is the NIST framing the card uses where SR 11-7 or sector-specific anchors do not apply directly.

### 4. NIST AI 600-1 — Generative AI Profile

- Citation: NIST AI 600-1, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (July 2024), Map and Measure subcategories specific to GenAI [verify exact Measure subcategory numbering at SKILL.md write time].
- Excerpt-paraphrase: NIST AI 600-1 extends the AI RMF for generative-AI-specific concerns including data provenance, hallucination, content provenance, prompt-injection exposure, and synthetic-content risk. The card's GenAI overlay (foundation-model dependence, RAG corpus, prompt-injection robustness, content provenance) aligns to Map and Measure subcategories in this profile.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Generative AI Profile (NIST AI 600-1), Map 1.1 section and Measure 2.x section subcategories [verify section]
- Notes: Subcategory numbering confirmed at SKILL.md write time; spec sheet flags the verification.

### 5. ISO/IEC 42001:2023 — Artificial Intelligence Management System

- Citation: ISO/IEC 42001:2023 "Information technology — Artificial intelligence — Management system", §7.5 "Documented information" and §8.1 "Operational planning and control".
- Excerpt-paraphrase: §7.5 sets out documentation expectations for an AI management system, covering creation, control, retention, and protection of documented information. §8.1 covers operational planning and control of AI processes. The model card is the documented information for an in-scope AI use case under §7.5.
- Link: https://www.iso.org/standard/42001 — ISO/IEC 42001:2023 §7.5 Documented information
- Notes: ISO/IEC 42001 is voluntary/certifiable; firms pursuing certification use this anchor as the AI management-system frame.

### 6. EU AI Act — Article 11 and Annex IV

- Citation: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 11 "Technical documentation" and Annex IV "Technical documentation referred to in Article 11(1)".
- Excerpt-paraphrase: Article 11 requires providers of high-risk AI systems to draw up technical documentation before placing the system on the market or putting it into service; the documentation must contain at least the elements set out in Annex IV. Annex IV enumerates intended purpose, version, hardware and software description, data requirements, training methodology, testing, performance metrics, post-market monitoring plan, and human-oversight design.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 11 and Annex IV
- Notes: The model card produced by `model-card-builder` is the firm-side governance artifact and overlaps in content with Annex IV technical documentation. For FS use cases that fall under EU AI Act high-risk (e.g., creditworthiness assessment, life and health insurance pricing), the firm-side card supports the Annex IV obligation but does not, by itself, satisfy it. The deployer-versus-provider distinction governs which of Article 11 or Article 26 obligations apply; cross-link to `ai-act-triage`.

## Secondary anchors (sector and cross-cutting)

### 7. CFPB Circular 2022-03 — Adverse action notification requirements when using AI or complex algorithms

- Citation: CFPB Circular 2022-03 (May 26, 2022), "Adverse action notification requirements in connection with credit decisions based on complex algorithms".
- Excerpt-paraphrase: Creditors using complex algorithms must still provide a statement of specific reasons to applicants against whom adverse action is taken; the complexity of the model is not a defence to the specificity requirement under ECOA / Regulation B (15 USC §1691; 12 CFR §1002.9).
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/ — Circular §1 and §2
- Notes: Banking sector overlay anchor; consumer-credit decisioning model cards must address adverse action notice generation in controls and sign-off questions.

### 8. CFPB Circular 2023-03 — Adverse action notices and the use of sample reason codes

- Citation: CFPB Circular 2023-03 (September 19, 2023), "Adverse action notification requirements and the proper use of the CFPB's sample forms".
- Excerpt-paraphrase: Creditors cannot rely on illegitimate reasons, including reasons not actually relied upon in the adverse decision. Reasons given in the adverse action notice must be the actual principal reasons for the adverse action, even when sample reason codes are used. Applies under ECOA / Regulation B §1002.9.
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2023-03-adverse-action-notification-requirements-and-the-proper-use-of-the-cfpbs-sample-forms-provided-in-regulation-b/ — Circular section "Required Information"
- Notes: Banking sector overlay anchor; complements Circular 2022-03.

### 9. NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)

- Citation: National Association of Insurance Commissioners, "Model Bulletin: Use of Artificial Intelligence Systems by Insurers" (adopted December 4, 2023), Sections 1-4 (general expectations), AIS Program elements (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness).
- Excerpt-paraphrase: Insurers using AI systems are expected to adopt and implement an AIS Program addressing the named elements. Documentation includes a detailed AI use-case inventory with intended use, data sources, performance, and oversight; the model card is the documentation artifact for individual AI use cases.
- Link: https://content.naic.org/sites/default/files/inline-files/2023-12-4%20Model%20Bulletin_Adopted_0.pdf — Model Bulletin Sections 1-4 and AIS Program elements
- Notes: NAIC Bulletin is a model bulletin; binding only to the extent state DOIs adopt it. State adoption tracker maintained by the NAIC AI Working Group is the public reference for binding-status confirmation per jurisdiction.

### 10. New York Department of Financial Services Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024)

- Citation: NYDFS Insurance Circular Letter on the Use of Artificial Intelligence Systems and External Consumer Data and Information Sources in Insurance Underwriting and Pricing (January 17, 2024), [verify section] on governance, fairness testing, disclosure, consumer recourse.
- Excerpt-paraphrase: The Circular Letter sets governance, fairness testing, disclosure, and consumer-recourse expectations for life-insurance underwriting and pricing using AI and ECDIS. Insurers are expected to maintain documentation supporting the use of each AI/ECDIS element.
- Link: https://www.dfs.ny.gov/industry-guidance/circular-letters — Insurance Circular Letter (January 2024) [verify exact section]
- Notes: Insurance sector overlay anchor for NY footprint.

### 11. Colorado Division of Insurance regulation implementing SB 21-169 (life-insurance underwriting)

- Citation: Colorado Division of Insurance, regulation implementing SB 21-169 (governance and risk management of ECDIS and predictive models in life-insurance underwriting) [verify regulation number and effective date].
- Excerpt-paraphrase: Carriers using ECDIS or predictive models in life-insurance underwriting in Colorado must implement a governance and risk-management framework, including a written policy, testing for unfair discrimination, consumer disclosure, and recourse. The model card supports the documentation element.
- Link: https://doi.colorado.gov/insurance-products/life-insurance/algorithm-and-predictive-model-governance — CO regulation [verify section]
- Notes: Insurance sector overlay anchor for CO footprint.

### 12. NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024)

- Citation: NYDFS Industry Letter, "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks" (October 16, 2024), [verify section] on AI-related cyber threats including AI-enabled social engineering, deepfakes, and prompt-injection-related risks.
- Excerpt-paraphrase: Covered entities under 23 NYCRR Part 500 are expected to address AI-related cybersecurity risks in their cybersecurity program, including AI-enabled threats and risks from the entity's own use of AI. The model card carries cyber section evidence for a GenAI use case in NY footprint.
- Link: https://www.dfs.ny.gov/industry-guidance/industry-letters — Industry Letter October 2024 [verify section]
- Notes: Cyber cross-cutting overlay anchor; relevant to the GenAI customer-support example in this skill.

### 13. OCC Heightened Standards (12 CFR Part 30 Appendix D)

- Citation: 12 CFR Part 30 Appendix D, "OCC Guidelines Establishing Heightened Standards for Certain Large Insured National Banks, Insured Federal Savings Associations, and Insured Federal Branches".
- Excerpt-paraphrase: The Heightened Standards apply to OCC-supervised banks meeting an asset-size threshold. They establish minimum standards for risk-governance frameworks, including independent risk management, board composition and oversight, risk-appetite statements, and chief risk-executive responsibilities. Models in scope of risk-appetite statements connect to the model card via tier and inventory references.
- Link: https://www.ecfr.gov/current/title-12/chapter-I/part-30 — 12 CFR Part 30 Appendix D
- Notes: Banking sector overlay anchor; reach is OCC large-bank only.

### 14. FFIEC BSA/AML Examination Manual

- Citation: FFIEC Bank Secrecy Act/Anti-Money Laundering Examination Manual (current edition), sections on transaction monitoring, customer risk rating, and SAR filing [verify section reference].
- Excerpt-paraphrase: The manual sets supervisory expectations for BSA/AML programs including model risk for transaction-monitoring and customer-risk-rating systems. Model documentation is a component of the program; threshold tuning, above-the-line / below-the-line testing, and model performance evidence are recurring exam topics.
- Link: https://bsaaml.ffiec.gov/manual — Examination Manual section on Transaction Monitoring [verify section]
- Notes: Banking and payments-fintech sector overlay anchor.

### 15. SEC Rule 15c3-5 — Market Access Rule

- Citation: 17 CFR 240.15c3-5 ("Risk management controls for brokers or dealers with market access").
- Excerpt-paraphrase: Brokers and dealers with market access must establish, document, and maintain a system of risk management controls and supervisory procedures designed to manage financial and regulatory risks of market access. Where execution algorithms or trading models drive routing or order-placement decisions, controls under Rule 15c3-5 apply to the model.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.15c3-5 — 17 CFR §240.15c3-5
- Notes: Capital-markets sector overlay anchor.

### 16. SEC Investment Advisers Act Rule 206(4)-7 — Compliance program rule

- Citation: 17 CFR 275.206(4)-7 (Compliance procedures and practices).
- Excerpt-paraphrase: Investment advisers must adopt and implement written policies and procedures reasonably designed to prevent violation of the IAA, conduct annual review, and designate a chief compliance officer. Models supporting advisory recommendations are within the program; the annual review is a recurring re-validation cadence trigger for the model card.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 — 17 CFR §275.206(4)-7
- Notes: Capital-markets sector overlay anchor.

### 17. SEC Investment Advisers Act Rule 206(4)-1 — Marketing Rule

- Citation: 17 CFR 275.206(4)-1 ("Investment Adviser Marketing").
- Excerpt-paraphrase: Marketing communications by investment advisers, including those generated or assisted by AI, are subject to general prohibitions, performance-presentation rules, and testimonial/endorsement requirements. AI-generated client communications fall within scope where they meet the definition of an advertisement.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 — 17 CFR §275.206(4)-1
- Notes: Capital-markets sector overlay anchor for AI-generated client content.

### 18. SEC Adviser Books-and-Records Rule 204-2 / BD Rules 17a-3 and 17a-4

- Citation: 17 CFR 275.204-2 (Books and records to be maintained by investment advisers); 17 CFR 240.17a-3 and 17 CFR 240.17a-4 (Records to be made and preserved by certain exchange members, brokers, and dealers).
- Excerpt-paraphrase: Books-and-records rules require advisers and BDs to make and preserve records supporting their recommendations and trading decisions. AI-generated content supporting a recommendation or decision falls within the records-preservation scope.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.204-2 — 17 CFR §275.204-2 and §240.17a-3
- Notes: Capital-markets sector overlay anchor.

### 19. Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 6, 2023)

- Citation: OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, "Interagency Guidance on Third-Party Relationships: Risk Management" (issued June 6, 2023).
- Excerpt-paraphrase: The interagency guidance sets risk-management expectations for banking organizations engaging third parties, including fintech and AI vendors. Where a sponsor-bank arrangement involves third-party-developed models, the bank retains accountability for model risk; the model card carries the bank-side ownership and oversight statements.
- Link: https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-17.html — Bulletin 2023-17 sections on Risk Management Life Cycle
- Notes: Payments-fintech sector overlay anchor.

### 20. Public model and system card precedents (form-factor reference only)

- Citation: Public model and system cards from Anthropic (Claude system cards), OpenAI (GPT system cards), and Google (Gemini cards) are referenced as a documentation pattern, not as a source of facts to be copied.
- Excerpt-paraphrase: Frontier-lab system cards establish a documentation form factor for foundation models including intended use, training data summary, evaluation results, limitations, and safety mitigations. The firm-side model card consumes vendor system cards as evidence (at vendor-self-attestation confidence) but does not copy vendor facts as firm assertions.
- Link: https://www.anthropic.com/news/claude-system-card — system card pattern reference, intended-use section and limitations section; https://openai.com/safety — system card pattern reference, evaluation section
- Notes: Form-factor reference only; no firm-specific content is asserted from these sources. Vendor evidence is recorded with confidence labels per the source-trace section of the card.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at SKILL.md write time and at card-write time:

- NIST AI 600-1 — confirm exact Measure subcategory numbering for the GenAI elements cited.
- NYDFS Insurance Circular Letter (January 2024) — confirm section reference.
- Colorado Division of Insurance regulation implementing SB 21-169 — confirm regulation number and effective date.
- NYDFS Industry Letter on AI cybersecurity (October 2024) — confirm section reference.
- FFIEC BSA/AML Examination Manual — confirm section reference for transaction-monitoring model expectations.

Where verification is incomplete, the SKILL.md cites with the `[verify section]` flag carried forward; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy, and named owners via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. An advisory firm shipping a client-specific overlay does the same thing under a separate overlay file.
