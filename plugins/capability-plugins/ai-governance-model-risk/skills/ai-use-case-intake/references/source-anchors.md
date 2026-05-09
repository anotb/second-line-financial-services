# Source anchors: ai-use-case-intake

Cited regulatory sources this skill anchors to. Every primary anchor names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link.

The skill cites these by file path. SKILL.md does not restate excerpts.

## Primary anchors

### 1. NIST AI Risk Management Framework 1.0 — Govern and Map functions

- Citation: National Institute of Standards and Technology, AI Risk Management Framework 1.0 (NIST AI 100-1, January 2023), Govern 1.6 (inventory of AI systems) and Map 1.1 to Map 1.6 (context, intended purpose, system categorization, capabilities, deployment setting, risks and benefits).
- Excerpt-paraphrase: Govern 1.6 calls for the organisation to establish and maintain an inventory of AI systems with sufficient detail to support risk management. Map 1.1 establishes context for the AI system including intended purpose, stakeholders, and operational setting; Map 1.4 names capabilities and uses; Map 1.6 establishes risks and benefits with affected groups identified. The intake record produced by this skill operationalises the Govern 1.6 inventory entry and supplies the Map 1.1 to 1.6 context that downstream tier and impact-assessment work relies on.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Govern function section (Govern 1.6) and Map function section (Map 1.1 through Map 1.6)
- Notes: NIST AI RMF 1.0 is voluntary, not binding; it is the framing the skill uses where SR 11-7 or sector-specific anchors do not apply directly. The AI inventory is the artefact regulators most-frequently ask to see when they ask "show me your AI use cases."

### 2. NIST AI 600-1 — Generative AI Profile

- Citation: NIST AI 600-1, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (July 2024), Govern 1.6 (GenAI inventory considerations) and Map 1.1 (use case context for GenAI) [verify exact subcategory numbering at decision-write time].
- Excerpt-paraphrase: NIST AI 600-1 extends the AI RMF for GenAI-specific concerns including data provenance, hallucination, content provenance, prompt-injection exposure, training-data poisoning, and synthetic-content risk. The GenAI overlay block in this skill (foundation-model identity and pinning posture, RAG corpus and refresh cadence, tool inventory, autonomy uplift) aligns to Govern 1.6 and Map 1.1 in this profile.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Generative AI Profile (NIST AI 600-1) [verify section]
- Notes: Subcategory numbering confirmed at decision-write time; phase-1 spec sheet flags the verification.

### 3. ISO/IEC 42001:2023 — AI management system

- Citation: ISO/IEC 42001:2023 "Information technology — Artificial intelligence — Management system", §6.1.2 "AI system impact assessment", §7.5 "Documented information", §8.1 "Operational planning and control".
- Excerpt-paraphrase: §6.1.2 requires the organisation to perform an impact assessment of the AI system on individuals, groups of individuals, and societies, considering intended use, foreseeable misuse, and the operational context. §7.5 requires documented information sufficient to support the AI management system. §8.1 covers operational planning and control of AI systems, including changes. The intake record produced by this skill is the documented-information artefact under §7.5 that feeds the §6.1.2 impact assessment.
- Link: https://www.iso.org/standard/42001 — ISO/IEC 42001:2023 §6.1.2, §7.5, §8.1
- Notes: ISO/IEC 42001 is voluntary and certifiable; firms pursuing certification use this anchor as the AI management-system frame.

### 4. SR 11-7 — Guidance on Model Risk Management

- Citation: Board of Governors of the Federal Reserve System, Supervision and Regulation Letter SR 11-7 / OCC Bulletin 2011-12, "Guidance on Model Risk Management" (April 4, 2011), §III "Overview of Model Risk Management" — the model definition and inventory expectations.
- Excerpt-paraphrase: §III defines a model as "a quantitative method, system, or approach that applies statistical, economic, financial, or mathematical theories, techniques, and assumptions to process input data into quantitative estimates" and calls for a comprehensive inventory of models with their use, status, and validation history. The intake record produced by this skill is the entry an AI or model use case takes in that inventory; the §III definition is the gate for whether a use case is in scope of model risk management at all.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm — §III
- Notes: SR 11-7 was the OCC/FRB joint guidance binding on federally regulated banks for over a decade. As of April 17, 2026 it is superseded by the joint interagency Revised Guidance on Model Risk Management (anchor 5). For traditional models the intake's model-risk inventory entry now anchors there; for GenAI and agentic use cases the bulletin is out of scope and the intake record's role is to capture the use case for the firm's broader AI inventory, anchored in NIST AI RMF (anchor 1).

### 5. Joint Interagency Revised Guidance on Model Risk Management — OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026

- Citation: Joint Interagency Revised Guidance on Model Risk Management, OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, dated April 17, 2026. The three issuances are the same joint document; supersedes SR 11-7 (2011) and SR 21-8 (2021).
- Excerpt-paraphrase (footnote 3, verbatim): "Generative AI and agentic AI models are novel and rapidly evolving. As such, they are not within the scope of this guidance. ... However, the principles described in this guidance apply to traditional statistical and quantitative models and non-generative, non-agentic AI models." Most relevant to banking organizations with over $30 billion in total assets; non-binding. The bulletin contains no references to NIST publications.
- Link: https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf — guidance text PDF
- Notes: Cite this anchor for the inventory entry of a traditional model in scope at a federally regulated bank. For GenAI and agentic use cases the bulletin is out of scope; the intake's GenAI architecture fields (foundation-model identity, RAG corpora, tool inventory, autonomy posture) anchor to NIST AI 600-1, ISO/IEC 42001, and the cross-cutting cyber overlay rather than this bulletin.

### 6. EU AI Act — Article 6 and Annex III (high-risk classification)

- Citation: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 6 "Classification rules for high-risk AI systems" and Annex III "High-risk AI systems referred to in Article 6(2)".
- Excerpt-paraphrase: Article 6(1) classifies as high-risk any AI system that is itself a safety component of a product covered by Union harmonisation legislation listed in Annex I, or is itself such a product, where conformity assessment by a third party is required. Article 6(2) deems high-risk the AI systems listed in Annex III. Annex III enumerates the eight categories most relevant to FS: biometric identification and categorisation; critical infrastructure; education; employment; essential private services and public services and benefits, including creditworthiness assessment of natural persons (Annex III §5(b)) and risk assessment and pricing in life and health insurance (Annex III §5(c)); law enforcement; migration; administration of justice and democratic processes. The intake record captures the fields needed at intake to support the formal AI Act classification owned by `ai-act-triage`.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 6 and Annex III §5(b), §5(c)
- Notes: The formal AI Act classification is owned by `ai-act-triage`. Intake captures the fields and flags Annex III overlap for routing.

### 7. EU AI Act — Article 17 (quality management for high-risk providers)

- Citation: Regulation (EU) 2024/1689, Article 17 "Quality management system" — providers of high-risk AI systems are required to put in place a quality management system that includes documented information on the design, development, monitoring, post-market plan, and reporting of serious incidents.
- Excerpt-paraphrase: Article 17 requires providers of high-risk AI systems to put in place a documented quality management system covering strategies for regulatory compliance, design and design-control techniques, development and quality-control techniques, examination and verification procedures, technical specifications, data management, risk management, the post-market monitoring system, procedures for serious-incident reporting, communication with regulators and notified bodies, recordkeeping, and resource management. Where the firm is a provider of a high-risk AI system, the intake record is the documented inventory entry that feeds the Article 17 quality management system.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 17
- Notes: Most US financial-services firms are deployers, not providers, of high-risk AI systems for AI Act purposes; the Article 17 reach applies most directly to firms that build their own high-risk AI systems for in-house use or sale. The deployer obligations under Articles 26 and 27 carry separately.

### 8. NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024)

- Citation: NYDFS Industry Letter, "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks" (October 16, 2024), [verify section] on AI-related cyber threats and on the entity's own AI use.
- Excerpt-paraphrase: Covered entities under 23 NYCRR Part 500 are expected to address AI-related cybersecurity risks in their cybersecurity program, including AI-enabled threats (deepfake-driven social engineering, AI-enhanced phishing) and risks from the entity's own use of AI (prompt injection, training-data poisoning, model extraction). Intake fields capturing AI-enabled threat surface and the entity's AI use feed the Part 500 risk-assessment chain.
- Link: https://www.dfs.ny.gov/industry-guidance/industry-letters — Industry Letter October 2024 [verify section]
- Notes: Cyber cross-cutting overlay anchor; cited from `references/cross-cutting/cyber.md`.

## Secondary anchors (sector and cross-cutting)

### 9. NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)

- Citation: National Association of Insurance Commissioners, "Model Bulletin: Use of Artificial Intelligence Systems by Insurers" (adopted December 4, 2023), Sections 1-4 (general expectations) and AIS Program elements (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness).
- Excerpt-paraphrase: Insurers using AI systems are expected to adopt and implement an AIS Program proportionate to the use case's potential to harm consumers. The intake record's regulatory-flags and decision-impact fields feed the AIS Program element status; the intake captures the fields needed to set the AIS Program proportionality at later stages.
- Link: https://content.naic.org/sites/default/files/inline-files/2023-12-4%20Model%20Bulletin_Adopted_0.pdf — Model Bulletin Sections 1-4 and AIS Program elements
- Notes: NAIC Bulletin is a model bulletin; binding only to the extent state DOIs adopt it. State adoption tracker maintained by the NAIC AI Working Group is the public reference for binding-status confirmation per jurisdiction.

### 10. Colorado Division of Insurance regulation implementing SB 21-169

- Citation: Colorado Division of Insurance, regulation implementing SB 21-169 (governance and risk management of External Consumer Data and Information Sources and predictive models in life-insurance underwriting) [verify regulation number and effective date].
- Excerpt-paraphrase: Carriers using ECDIS or predictive models in life-insurance underwriting in Colorado must implement a governance and risk-management framework, including a written policy, testing for unfair discrimination, consumer disclosure, and recourse. Intake fields capturing data source provenance (ECDIS use), Colorado operating footprint, and consumer-recourse posture feed the regulation's governance chain.
- Link: https://doi.colorado.gov/insurance-products/life-insurance/algorithm-and-predictive-model-governance — CO regulation [verify section]
- Notes: Insurance sector overlay anchor for CO footprint.

### 11. NYDFS Insurance Circular Letter on AI and ECDIS (January 2024)

- Citation: NYDFS Insurance Circular Letter on the Use of Artificial Intelligence Systems and External Consumer Data and Information Sources in Insurance Underwriting and Pricing (January 17, 2024), [verify section] on governance, fairness testing, disclosure, and consumer recourse.
- Excerpt-paraphrase: The Circular Letter sets governance, fairness testing, disclosure, and consumer-recourse expectations for life-insurance underwriting and pricing using AI and ECDIS in NY. Intake captures NY operating footprint, ECDIS use, and consumer-recourse posture.
- Link: https://www.dfs.ny.gov/industry-guidance/circular-letters — Insurance Circular Letter (January 2024) [verify exact section]
- Notes: Insurance sector overlay anchor for NY footprint.

### 12. CFPB Circular 2022-03 — Adverse action notification when using complex algorithms

- Citation: CFPB Circular 2022-03 (May 26, 2022), "Adverse action notification requirements in connection with credit decisions based on complex algorithms".
- Excerpt-paraphrase: Creditors using complex algorithms must still provide a statement of specific reasons to applicants against whom adverse action is taken; the complexity of the model is not a defence to the specificity requirement under ECOA / Regulation B (15 USC §1691; 12 CFR §1002.9). Intake fields capturing customer-binding decision posture, adverse-action implications, and consumer-recourse channel feed the conduct flag.
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/ — Circular section "Required Information" referencing 15 USC §1691 and 12 CFR §1002.9
- Notes: Banking and consumer-compliance overlay anchor; cited from the conduct cross-cutting overlay where present, and from the banking sector overlay.

### 13. SEC Investment Advisers Act Rule 206(4)-1 — Marketing Rule

- Citation: 17 CFR §275.206(4)-1 (Investment Adviser Marketing Rule).
- Excerpt-paraphrase: The Marketing Rule reaches AI-generated client communications and AI-generated performance presentations; the rule's general prohibitions apply to any communication that meets the definition of "advertisement," and the testimonial/endorsement, hypothetical-performance, and predecessor-performance provisions apply on top. Intake captures whether AI output reaches client-facing material, which determines Marketing Rule reach.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 — 17 CFR §275.206(4)-1
- Notes: Capital-markets sector overlay anchor.

### 14. SEC and BD books-and-records rules (Rule 204-2; Rules 17a-3 and 17a-4)

- Citation: 17 CFR §275.204-2 (Books and records to be maintained by investment advisers); 17 CFR §240.17a-3 and 17 CFR §240.17a-4 (Records to be made and preserved by certain exchange members, brokers, and dealers).
- Excerpt-paraphrase: Books-and-records rules require advisers and BDs to make and preserve records supporting recommendations and trading decisions. AI-generated content supporting a recommendation or decision falls within preservation scope; intake captures the preservation posture as a regulatory flag.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.204-2 — 17 CFR §275.204-2 ; https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-3 — 17 CFR §240.17a-3
- Notes: Capital-markets sector overlay anchor.

### 15. FFIEC BSA/AML Examination Manual

- Citation: FFIEC Bank Secrecy Act/Anti-Money Laundering Examination Manual (current edition), sections on transaction monitoring, customer risk rating, and SAR governance [verify section reference].
- Excerpt-paraphrase: The manual sets supervisory expectations for BSA/AML programs including model risk for transaction-monitoring and customer-risk-rating systems. Intake captures BSA/AML reach as a regulatory flag and identifies whether the use case touches SAR-workflow integration.
- Link: https://bsaaml.ffiec.gov/manual — Examination Manual [verify section]
- Notes: Banking and payments-fintech sector overlay anchor.

### 16. Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 6, 2023)

- Citation: OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, "Interagency Guidance on Third-Party Relationships: Risk Management" (issued June 6, 2023).
- Excerpt-paraphrase: The interagency guidance sets risk-management expectations for banking organisations engaging third parties, including fintech and AI vendors. Where the AI use case relies on a third-party model, the intake record captures the vendor dependency and the criticality posture; the AI-vendor scenario mode in `vendor-diligence` consumes the intake field.
- Link: https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-17.html — Bulletin 2023-17
- Notes: Payments-fintech and banking overlay anchor.

### 17. OCC, FRB, and FDIC Joint Statement on Bank-Fintech Arrangements (July 25, 2024)

- Citation: OCC / FRB / FDIC Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services (July 25, 2024) [verify exact date and title].
- Excerpt-paraphrase: The joint statement is operative for sponsor-bank programs and addresses end-customer reconciliation, FBO subledger posture, and deposit-insurance representation review. Intake captures sponsor-bank arrangement posture as a vendor dependency and a regulatory flag.
- Link: https://www.fdic.gov/news/financial-institution-letters — July 2024 Joint Statement section on bank-fintech deposit arrangements [verify exact citation]
- Notes: Payments-fintech overlay anchor.

### 18. NYDFS 23 NYCRR Part 500 (Cybersecurity Regulation)

- Citation: 23 NYCRR Part 500 ("Cybersecurity Requirements for Financial Services Companies"), as amended through the Second Amendment (effective November 2023; further compliance dates phased in through 2025).
- Excerpt-paraphrase: Covered entities must maintain a cybersecurity program based on a risk assessment, including governance, access controls, monitoring, incident response, and third-party risk management. The 2024 NYDFS Industry Letter on AI extends Part 500 to AI-specific risks. Intake captures NY-licensed covered-entity status as a regulatory flag and routes to the cyber overlay.
- Link: https://www.dfs.ny.gov/industry/cybersecurity — 23 NYCRR Part 500 sections on cybersecurity program governance
- Notes: Cyber cross-cutting overlay anchor.

### 19. GLBA Safeguards Rule and HIPAA Privacy/Security Rules

- Citation: 16 CFR Part 314 (FTC Safeguards Rule under Gramm-Leach-Bliley Act); 45 CFR Part 160 and Part 164 (HIPAA Privacy and Security Rules).
- Excerpt-paraphrase: GLBA Safeguards Rule applies to non-public personal information held by financial institutions; HIPAA applies to protected health information held by covered entities and business associates. Intake fields capturing field-level data sensitivity (regulated NPI, regulated PHI) feed the privacy overlay and the data-sensitivity tiering factor.
- Link: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 — 16 CFR Part 314 ; https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C — 45 CFR Subchapter C (HIPAA Privacy and Security Rule sections)
- Notes: Privacy cross-cutting overlay anchor.

### 20. NIST AI RMF Map 3.5 / EU AI Act Article 14 — effective human oversight

- Citation: NIST AI RMF 1.0 Map 3.5 (human factors and oversight); EU AI Act (Regulation (EU) 2024/1689) Article 14 "Human oversight" [verify exact subcategory numbering for Map 3.5].
- Excerpt-paraphrase: Map 3.5 addresses human factors in the AI lifecycle including the operational role of human oversight; Article 14 requires that high-risk AI systems be designed and developed in such a way that they can be effectively overseen by natural persons during the period in which they are in use. Intake captures autonomy level and the evidence of effective human oversight; absence of evidence flags the autonomy level as an open question rather than rubber-stamping the human-in-the-loop label.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Map function (Map 3.5) [verify section] ; https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 14
- Notes: The autonomy-level field in the intake structure is anchored here. The "rubber-stamp at scale" failure mode (button-push approval that does not constitute oversight) is the test the intake field is built against.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at decision-write time:

- OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026 — verbatim GenAI/agentic scope exclusion confirmed against the OCC PDF (footnote 3). The three issuances are the same joint document, not parallels. SR 11-7 and SR 21-8 are confirmed superseded as of April 17 2026.
- NIST AI 600-1 — confirm exact subcategory numbering for the GenAI Govern 1.6 and Map 1.1 references.
- NIST AI RMF Map 3.5 — confirm exact subcategory numbering.
- NYDFS Insurance Circular Letter (January 2024) — confirm section reference.
- Colorado Division of Insurance regulation implementing SB 21-169 — confirm regulation number and effective date.
- NYDFS Industry Letter on AI cybersecurity (October 2024) — confirm section reference.
- FFIEC BSA/AML Examination Manual — confirm section reference for transaction-monitoring model expectations.
- OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 25, 2024) — confirm exact title, date, and operative status against the date of analysis.

Where verification is incomplete, the intake record cites with the `[verify section]` flag carried forward; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy (specific intake field extensions, firm AI inventory schema, named owners), and review-gate machinery via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file.
