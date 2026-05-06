# Source anchors: validation-plan

Cited regulatory sources this skill anchors to. Each primary anchor names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link.

The skill cites these by file path. SKILL.md does not restate excerpts.

## Primary anchors

### 1. Federal Reserve SR 11-7 / OCC Bulletin 2011-12 — Guidance on Model Risk Management

- Citation: Board of Governors of the Federal Reserve System, Supervision and Regulation Letter SR 11-7 / OCC Bulletin 2011-12, "Guidance on Model Risk Management" (April 4, 2011), §III "Model Development, Implementation, and Use", §IV "Model Validation", §V "Governance, Policies, and Controls".
- Excerpt-paraphrase: §IV sets out the three pillars of model validation: (a) evaluation of conceptual soundness, including developmental evidence; (b) ongoing monitoring, including process verification and benchmarking; (c) outcomes analysis, including back-testing. Validation activities should be commensurate with the model's potential impact and the firm's overall use of the model. §IV.5 sets the effective challenge expectation: validation work is performed by parties with sufficient stature, knowledge, and incentive to challenge the model. §V sets governance, documentation, and inventory expectations that the validation plan operates within.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm — SR 11-7 §III, §IV (validation), §V
- Notes: SR 11-7 is the OCC/FRB joint guidance; binding on federally regulated banks. For non-bank registrants, SR 11-7 is referenced as a leading-practice anchor rather than a binding rule. The validation plan produced by this skill is the validator-side scope contract that operationalises §IV.

### 2. OCC Bulletin 2026-13 — Revised Interagency Model Risk Management Guidance (2026)

- Citation: OCC Bulletin 2026-13, "Revised Interagency Guidance on Model Risk Management" (issued 2026 by OCC; FDIC parallel FIL and Federal Reserve parallel SR letter expected) [verify section on validation depth, AI/ML extension, and effective challenge].
- Excerpt-paraphrase: The revised guidance refreshes SR 11-7 to incorporate AI/ML and generative-AI use cases, including foundation-model dependence, retrieval-augmented generation (RAG), tool use, and agentic configurations. Validation depth is set commensurate with model impact; the three pillars (conceptual soundness, ongoing monitoring, outcomes analysis) carry forward with extensions for vendor-opaque foundation models (vendor evidence review substitutes for theory replication where the model is not auditable internally).
- Link: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html — Bulletin 2026-13 [verify section]
- Notes: Plan-writer flag — confirm published bulletin section numbering at plan-write time. The phase-1 spec sheet records `[verify section]` and the SKILL.md does not over-claim binding language until verified.

### 3. FDIC FIL on Revised Interagency Model Risk Management Guidance (2026)

- Citation: FDIC FIL on revised interagency model risk management guidance (issued 2026) [verify exact FIL number and section].
- Excerpt-paraphrase: Parallel issuance to OCC Bulletin 2026-13. Validation expectations for FDIC-supervised institutions follow the interagency text with FDIC-specific supervisory framing.
- Link: https://www.fdic.gov/news/financial-institution-letters/2026/agencies-revise-interagency-model-risk-management-guidance — FDIC FIL [verify section]
- Notes: Plan-writer flag — confirm the FIL number and any FDIC-specific elaboration at plan-write time.

### 4. NIST AI Risk Management Framework 1.0 — Measure function

- Citation: National Institute of Standards and Technology, AI Risk Management Framework 1.0 (January 2023), Measure function, subcategories Measure 1.1 to Measure 4.3, with primary validation-relevant subcategories at Measure 2.1 (validity and reliability), Measure 2.5 (safety), Measure 2.6 (security and resilience), Measure 2.7 (accountability and transparency), Measure 2.8 (explainability and interpretability), Measure 2.9 (privacy enhancement), Measure 2.10 (fairness with harmful bias managed), Measure 2.11 (environmental impact), Measure 2.12 (information integrity), Measure 2.13 (information security).
- Excerpt-paraphrase: The Measure function defines testable AI-system properties and recommends segment-level and disaggregated reporting where the system has differential impact across groups or contexts. The validation plan's outcomes-analysis, robustness, fairness, and explainability scope items align to Measure 2.x subcategories.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Measure function section, Measure 2.x subcategories
- Notes: NIST AI RMF is voluntary, not binding; it is the NIST framing the plan uses where SR 11-7 or sector-specific anchors do not apply directly.

### 5. NIST AI 600-1 — Generative AI Profile

- Citation: NIST AI 600-1, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (July 2024), Measure subcategories specific to GenAI risks including CBRN information / capabilities (Measure 2.x), confabulation / hallucination, dangerous or violent recommendations, data privacy, environmental impacts, harmful bias, human-AI configuration, information integrity, information security, intellectual property, obscene / degrading / abusive content, value chain and component integration [verify exact subcategory numbering at plan-write time].
- Excerpt-paraphrase: NIST AI 600-1 extends the AI RMF for generative-AI-specific concerns. The validation plan's GenAI-specific outcomes-analysis tests (faithfulness, citation precision, refusal rate, hallucination rate) and robustness tests (direct prompt injection, indirect prompt injection on retrieved content, jailbreak, RAG poisoning, model extraction) align to Measure subcategories in this profile.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Generative AI Profile (NIST AI 600-1), Measure section subcategories [verify section]
- Notes: Subcategory numbering confirmed at plan-write time; spec sheet flags the verification.

### 6. ISO/IEC 42001:2023 — Artificial Intelligence Management System

- Citation: ISO/IEC 42001:2023 "Information technology — Artificial intelligence — Management system", §9.1 "Monitoring, measurement, analysis and evaluation", §9.2 "Internal audit", §9.3 "Management review".
- Excerpt-paraphrase: §9.1 sets the management-system expectation for monitoring AI processes and evaluating their performance against defined criteria. §9.2 covers internal audit of the AI management system. §9.3 covers management review. The validation plan's ongoing-monitoring scope and the validator's reporting cadence operate within §9.1; effective challenge sits adjacent to §9.2.
- Link: https://www.iso.org/standard/42001 — ISO/IEC 42001:2023 §9 (monitoring, measurement, analysis, evaluation; internal audit; management review)
- Notes: ISO/IEC 42001 is voluntary / certifiable. Firms pursuing certification use this anchor as the AI management-system frame.

### 7. EU AI Act — Article 9 Risk Management System and Annex IV Technical Documentation

- Citation: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 9 "Risk management system" and Annex IV "Technical documentation referred to in Article 11(1)".
- Excerpt-paraphrase: Article 9 requires providers of high-risk AI systems to establish, implement, document, and maintain a risk management system as a continuous iterative process planned and run throughout the entire lifecycle of the high-risk AI system, requiring regular systematic review and updating. Article 9(2) lists steps including identification and analysis of known and reasonably foreseeable risks, estimation and evaluation of risks that may emerge under intended use and reasonably foreseeable misuse, evaluation of other risks based on data from the post-market monitoring system, and adoption of risk management measures. Annex IV (referenced via Article 11) requires technical documentation including testing performed, validation procedures, performance metrics, and the post-market monitoring plan.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 9 (risk management system) and Annex IV (technical documentation)
- Notes: For FS use cases that fall under EU AI Act high-risk (e.g., creditworthiness assessment per Annex III; life and health insurance pricing per Annex III), the validation plan supports Article 9 risk-management evidence and Annex IV technical-documentation elements. Provider-versus-deployer distinction governs which obligations apply directly. Cross-link to `ai-act-triage` for scoping.

### 8. EU AI Act — Article 15 Accuracy, Robustness, and Cybersecurity

- Citation: Regulation (EU) 2024/1689, Article 15 "Accuracy, robustness and cybersecurity".
- Excerpt-paraphrase: Article 15 requires high-risk AI systems to be designed and developed to achieve appropriate levels of accuracy, robustness, and cybersecurity, and to perform consistently in those respects throughout their lifecycle. Article 15(4) addresses resilience to errors, faults, and inconsistencies; Article 15(5) addresses resilience to attempts by unauthorised third parties to alter use, outputs, or performance through exploiting system vulnerabilities, including measures to prevent, detect, respond to, resolve, and control attacks (data poisoning, model poisoning, model evasion, confidentiality attacks, model flaws).
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 15 (accuracy, robustness, cybersecurity)
- Notes: The plan's robustness, adversarial, and stress-testing scope aligns to Article 15. Where the model is a high-risk EU AI system, Article 15 evidence is part of the Annex IV technical-documentation set.

## Secondary anchors (sector and cross-cutting)

### 9. OCC Heightened Standards (12 CFR Part 30 Appendix D)

- Citation: 12 CFR Part 30 Appendix D, "OCC Guidelines Establishing Heightened Standards for Certain Large Insured National Banks, Insured Federal Savings Associations, and Insured Federal Branches".
- Excerpt-paraphrase: Heightened Standards apply to OCC-supervised banks meeting an asset-size threshold; they establish minimum standards for risk-governance frameworks, including independent risk management and risk-appetite statements. Tier-1 models in scope of the risk-appetite statement carry an independence expectation on the validator function.
- Link: https://www.ecfr.gov/current/title-12/chapter-I/part-30 — 12 CFR Part 30 Appendix D
- Notes: Banking sector overlay anchor; reach is OCC large-bank only.

### 10. CFPB Circular 2022-03 — Adverse action notification with complex algorithms

- Citation: CFPB Circular 2022-03 (May 26, 2022), "Adverse action notification requirements in connection with credit decisions based on complex algorithms".
- Excerpt-paraphrase: Creditors using complex algorithms must still provide a statement of specific reasons to applicants against whom adverse action is taken; complexity of the model is not a defence to the specificity requirement under ECOA / Regulation B (15 USC §1691; 12 CFR §1002.9).
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/ — Circular sections 1 and 2
- Notes: Banking sector overlay anchor; consumer-credit decisioning models include adverse-action-reason quality in the validation plan's explainability scope.

### 11. CFPB Circular 2023-03 — Adverse action notices and the use of sample reason codes

- Citation: CFPB Circular 2023-03 (September 19, 2023), "Adverse action notification requirements and the proper use of the CFPB's sample forms".
- Excerpt-paraphrase: Creditors cannot rely on illegitimate reasons; reasons given in the adverse action notice must be the actual principal reasons for the adverse action, even when sample reason codes are used (12 CFR §1002.9).
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2023-03-adverse-action-notification-requirements-and-the-proper-use-of-the-cfpbs-sample-forms-provided-in-regulation-b/ — Circular section "Required Information"
- Notes: Banking sector overlay anchor; complements Circular 2022-03.

### 12. NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)

- Citation: National Association of Insurance Commissioners, "Model Bulletin: Use of Artificial Intelligence Systems by Insurers" (adopted December 4, 2023), Sections 1-4 and AIS Program elements (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness).
- Excerpt-paraphrase: Insurers using AI systems are expected to adopt and implement an AIS Program addressing the named elements, including testing and validation. The validation plan operationalises the testing and validation elements for an individual AI use case in a carrier setting.
- Link: https://content.naic.org/sites/default/files/inline-files/2023-12-4%20Model%20Bulletin_Adopted_0.pdf — Model Bulletin Sections 1-4 and AIS Program elements
- Notes: Insurance sector overlay anchor. The Bulletin is a model bulletin; binding only to the extent state DOIs adopt it.

### 13. NYDFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024)

- Citation: NYDFS Insurance Circular Letter on the Use of Artificial Intelligence Systems and External Consumer Data and Information Sources in Insurance Underwriting and Pricing (January 17, 2024), [verify section] on governance, fairness testing, disclosure, and consumer recourse.
- Excerpt-paraphrase: The Circular Letter sets governance, fairness testing, disclosure, and consumer-recourse expectations for life-insurance underwriting and pricing using AI and ECDIS. Validation plans for in-scope models in NY footprint extend fairness scope to the unfair-discrimination framing under state insurance code.
- Link: https://www.dfs.ny.gov/industry-guidance/circular-letters — Insurance Circular Letter (January 2024) [verify exact section]
- Notes: Insurance sector overlay anchor for NY footprint.

### 14. Colorado Division of Insurance regulation implementing SB 21-169

- Citation: Colorado Division of Insurance, regulation implementing SB 21-169 (governance and risk management of ECDIS and predictive models in life-insurance underwriting) [verify regulation number and effective date].
- Excerpt-paraphrase: Carriers using ECDIS or predictive models in life-insurance underwriting in Colorado must implement a governance and risk-management framework, including testing for unfair discrimination. Validation plan scope extends to ECDIS provenance and unfair-discrimination testing for in-scope models.
- Link: https://doi.colorado.gov/insurance-products/life-insurance/algorithm-and-predictive-model-governance — CO regulation [verify section]
- Notes: Insurance sector overlay anchor for CO footprint.

### 15. NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024)

- Citation: NYDFS Industry Letter, "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks" (October 16, 2024), [verify section] on AI-related cyber threats including AI-enabled social engineering, deepfakes, and prompt-injection-related risks.
- Excerpt-paraphrase: Covered entities under 23 NYCRR Part 500 are expected to address AI-related cybersecurity risks in their cybersecurity program. The validation plan's robustness and adversarial scope for GenAI in NY footprint aligns to this industry letter.
- Link: https://www.dfs.ny.gov/industry-guidance/industry-letters — Industry Letter October 2024 [verify section]
- Notes: Cyber cross-cutting overlay anchor.

### 16. SEC Rule 15c3-5 — Market Access Rule

- Citation: 17 CFR 240.15c3-5 ("Risk management controls for brokers or dealers with market access").
- Excerpt-paraphrase: Brokers and dealers with market access must establish, document, and maintain a system of risk management controls and supervisory procedures designed to manage financial and regulatory risks of market access. Validation of execution algorithms or trading models in scope of market access includes testing of pre-trade risk controls (financial and regulatory).
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.15c3-5 — 17 CFR §240.15c3-5
- Notes: Capital-markets sector overlay anchor for execution algos and order-routing models.

### 17. SEC Investment Advisers Act Rule 206(4)-7 — Compliance program rule

- Citation: 17 CFR 275.206(4)-7 (Compliance procedures and practices).
- Excerpt-paraphrase: Investment advisers must adopt and implement written policies and procedures reasonably designed to prevent violation of the IAA, conduct an annual review, and designate a chief compliance officer. The annual review is a recurring re-validation cadence trigger for adviser models in scope.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 — 17 CFR §275.206(4)-7
- Notes: Capital-markets sector overlay anchor.

### 18. FFIEC BSA/AML Examination Manual

- Citation: FFIEC Bank Secrecy Act / Anti-Money Laundering Examination Manual (current edition), sections on transaction monitoring, customer risk rating, and SAR filing [verify section reference for transaction-monitoring model expectations].
- Excerpt-paraphrase: The manual sets supervisory expectations for BSA/AML programs including model risk for transaction-monitoring and customer-risk-rating systems. Above-the-line / below-the-line testing, threshold tuning, and productivity testing are recurring exam topics that validation plans for AML models scope explicitly.
- Link: https://bsaaml.ffiec.gov/manual — Examination Manual section on Transaction Monitoring [verify section]
- Notes: Banking and payments-fintech sector overlay anchor.

### 19. NACHA Operating Rules — Third-Party Sender risk management

- Citation: NACHA Operating Rules (current edition), Third-Party Sender registration, risk-management, and return-rate-monitoring rules [verify rule citations and current threshold values].
- Excerpt-paraphrase: ODFIs are expected to monitor Originator (and Third-Party Sender) return rates against NACHA thresholds (administrative-return, overall-return, unauthorized-return). Validation of return-rate-driven monitoring models scopes against the current threshold table and the firm's ODFI risk-management framework.
- Link: https://www.nacha.org/rules — NACHA Operating Rules (paywalled; current edition; specific sections to be confirmed against the firm's licensed copy)
- Notes: Payments-fintech sector overlay anchor. NACHA rulebook is paywalled; cite at plan-write time against the firm's licensed copy.

### 20. Joint OCC, FRB, FDIC Interagency Guidance on Third-Party Relationships (June 6, 2023) and OCC/FRB/FDIC Joint Statement on Bank-Fintech Arrangements (July 25, 2024)

- Citation: OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, "Interagency Guidance on Third-Party Relationships: Risk Management" (issued June 6, 2023); OCC / FRB / FDIC Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services (July 25, 2024) [verify exact title and date].
- Excerpt-paraphrase: The interagency guidance sets risk-management expectations for banking organizations engaging third parties, including fintech and AI vendors. The 2024 joint statement specifically addresses bank-fintech deposit-product arrangements. The validation plan for a sponsor-bank-program model identifies the bank-side accountability for model risk; the fintech does not absolve the bank of validation expectations.
- Link: https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-17.html — Bulletin 2023-17 §III "Risk Management Life Cycle"; https://www.fdic.gov/news/financial-institution-letters/2024 — Joint Statement on Bank-Fintech Arrangements [verify exact bulletin]
- Notes: Payments-fintech sector overlay anchor.

### 21. GLBA Safeguards Rule (16 CFR Part 314)

- Citation: 16 CFR Part 314 (Standards for Safeguarding Customer Information), as amended (2021 Final Rule, 2023 amendments on incident notification).
- Excerpt-paraphrase: Financial institutions must develop, implement, and maintain a comprehensive information-security program with administrative, technical, and physical safeguards for non-public personal information (NPI). Validation of models that process NPI scopes against the firm's safeguards-program controls and against memorisation / leak risk where the model is generative.
- Link: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 — 16 CFR Part 314
- Notes: Privacy cross-cutting overlay anchor.

### 22. HIPAA Privacy and Security Rules

- Citation: 45 CFR Parts 160 and 164 — HIPAA Privacy Rule (Subpart E of Part 164) and Security Rule (Subpart C of Part 164).
- Excerpt-paraphrase: Covered entities and business associates handling protected health information (PHI) must implement Privacy Rule and Security Rule controls. For models processing PHI, the validation plan scopes against minimum-necessary access, BAA coverage on any vendor handling PHI, and PHI-leak risk in generative outputs.
- Link: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164 — 45 CFR Part 164 Subparts C and E
- Notes: Privacy cross-cutting overlay anchor; insurance and healthcare-fintech contexts.

### 23. GDPR Article 22 — Automated individual decision-making

- Citation: Regulation (EU) 2016/679 (General Data Protection Regulation), Article 22 (decisions based solely on automated processing, including profiling).
- Excerpt-paraphrase: Article 22 grants data subjects the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects or similarly significant effects, with limited exceptions; where exceptions apply, the controller must implement suitable measures including the right to obtain meaningful information about the logic involved.
- Link: https://eur-lex.europa.eu/eli/reg/2016/679/oj — Article 22
- Notes: Privacy cross-cutting overlay anchor where EU customers are in operating footprint; the validation plan scopes meaningful-information-about-logic evidence.

### 24. Public model and system card precedents (form-factor reference only)

- Citation: Public model and system cards from Anthropic (Claude system cards), OpenAI (GPT system cards), and Google (Gemini cards); referenced as a documentation pattern for vendor-evidence review, not as a source of facts to be copied.
- Excerpt-paraphrase: Frontier-lab system cards establish a documentation form factor for foundation models including intended use, training data summary, evaluation results, limitations, and safety mitigations. The validation plan's `vendor_model_card_review` scope item enumerates which vendor evidence is in scope (system card, evaluation report, red-team summary).
- Link: https://www.anthropic.com/news/claude-system-card — system card pattern reference, evaluation section; https://openai.com/safety — system card pattern reference, limitations section
- Notes: Form-factor reference only; vendor evidence carries vendor-self-attestation confidence in source trace.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at plan-write time:

- OCC Bulletin 2026-13 — confirm published section numbering for validation depth, AI/ML extension, and effective challenge.
- FDIC FIL parallel issuance to OCC Bulletin 2026-13 — confirm number and section.
- FRB SR letter parallel issuance to OCC Bulletin 2026-13 — confirm number and section.
- NIST AI 600-1 — confirm exact Measure subcategory numbering for the GenAI elements cited (hallucination/confabulation, prompt injection, information integrity, harmful content, dangerous capabilities, information security).
- NYDFS Insurance Circular Letter (January 2024) — confirm section reference.
- Colorado Division of Insurance regulation implementing SB 21-169 — confirm regulation number and effective date.
- NYDFS Industry Letter on AI cybersecurity (October 2024) — confirm section reference.
- FFIEC BSA/AML Examination Manual — confirm section reference for transaction-monitoring model expectations.
- NACHA Operating Rules — confirm current Third-Party Sender rule citations and current threshold values against the firm's licensed copy.
- OCC/FRB/FDIC Joint Statement on Bank-Fintech Arrangements (July 2024) — confirm exact title, date, and bulletin numbers.

Where verification is incomplete, the SKILL.md cites with `[verify section]` carried forward in this file only; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy, and named owners via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. An advisory firm shipping a client-specific overlay does the same thing under a separate overlay file.
