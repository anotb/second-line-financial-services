# Source anchors: ai-risk-tiering

Cited regulatory sources this skill anchors to. Every primary anchor names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link.

The skill cites these by file path. SKILL.md does not restate excerpts.

## Primary anchors

### 1. Federal Reserve SR 11-7 — Guidance on Model Risk Management

- Citation: Board of Governors of the Federal Reserve System, Supervision and Regulation Letter SR 11-7 / OCC Bulletin 2011-12, "Guidance on Model Risk Management" (April 4, 2011), §III "Overview of Model Risk Management" and §IV "Model Development, Implementation, and Use" — the materiality and risk-rating framing.
- Excerpt-paraphrase: §III sets the risk-based principle: "the rigor and sophistication of validation should be commensurate with the bank's overall use of models, the complexity and materiality of its models, and the size and complexity of the bank's operations." §IV reinforces that materiality factors (model purpose, decision influence, financial exposure, complexity, uncertainty, vendor dependence) drive the depth of model risk management practice. The tier produced by this skill is the firm-side artefact that operationalises that risk-based principle.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm — §III and §IV
- Notes: SR 11-7 was the OCC/FRB joint guidance binding on federally regulated banks for over a decade. As of April 17, 2026 it is superseded by the joint interagency Revised Guidance on Model Risk Management (anchor 2). Materiality factors listed in SR 11-7 remain the spine of the rubric in this skill. Specific tier names (tier-1 through tier-4) and quantitative cutoffs are firm policy, not SR 11-7.

### 2. Joint Interagency Revised Guidance on Model Risk Management — OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026

- Citation: Joint Interagency Revised Guidance on Model Risk Management, OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, dated April 17, 2026. The three issuances are the same joint document; supersedes SR 11-7 (2011) and SR 21-8 (2021).
- Excerpt-paraphrase (footnote 3, verbatim): "Generative AI and agentic AI models are novel and rapidly evolving. As such, they are not within the scope of this guidance. ... However, the principles described in this guidance apply to traditional statistical and quantitative models and non-generative, non-agentic AI models." Most relevant to banking organizations with over $30 billion in total assets; non-binding. The bulletin contains no references to NIST publications.
- Link: https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf — guidance text PDF
- Notes: For traditional models in the firm's tiering rubric, this bulletin carries materiality and proportionality framing forward from SR 11-7 for federally regulated banks. For GenAI and agentic use cases the bulletin is out of scope; the GenAI-specific factor in the rubric anchors to NIST AI 600-1, ISO/IEC 42001, and the cyber and conduct overlays. Tier names and quantitative cutoffs remain firm policy.

### 3. NIST AI Risk Management Framework 1.0 — Map function

- Citation: National Institute of Standards and Technology, AI Risk Management Framework 1.0 (January 2023), Map function (Map 1.1 context establishment, Map 5.1 impact assessment), Measure function (Measure 2.6 risk levels and tolerances).
- Excerpt-paraphrase: Map 1.1 establishes context for the AI system including intended purpose, stakeholders, and operational setting. Map 5.1 calls for impact assessment that considers benefits, harms, and affected groups. Measure 2.6 covers setting risk levels and tolerances against the firm's risk appetite. The tier produced by this skill is the firm-side artefact that records the Map 5.1 impact assessment outcome and the Measure 2.6 risk-level placement.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Map function section (Map 1.1, Map 5.1) and Measure function section (Measure 2.6)
- Notes: NIST AI RMF 1.0 is voluntary, not binding; it is the framing the skill uses where SR 11-7 or sector-specific anchors do not apply directly. Tier names and cutoffs remain firm policy.

### 4. NIST AI 600-1 — Generative AI Profile

- Citation: NIST AI 600-1, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (July 2024), Map 1.1 (use case context for GenAI), Measure 2.6 (risk levels for GenAI specifically) [verify exact Measure subcategory numbering at decision-write time].
- Excerpt-paraphrase: NIST AI 600-1 extends the AI RMF for GenAI-specific concerns including data provenance, hallucination, content provenance, prompt-injection exposure, training-data poisoning, and synthetic-content risk. The tiering rubric's GenAI-specific factor (foundation-model dependence, RAG corpus drift, hallucination exposure, autonomy uplift via tool use) aligns to Map 1.1 and Measure 2.6 in this profile.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Generative AI Profile (NIST AI 600-1), Map 1.1 section and Measure 2.6 section [verify section]
- Notes: Subcategory numbering confirmed at decision-write time; spec sheet flags the verification.

### 5. EU AI Act — Article 6 and Annex III (high-risk classification)

- Citation: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 6 "Classification rules for high-risk AI systems" and Annex III "High-risk AI systems referred to in Article 6(2)".
- Excerpt-paraphrase: Article 6(1) classifies as high-risk any AI system that is itself a safety component of a product covered by Union harmonisation legislation listed in Annex I, or is itself such a product, where conformity assessment by a third party is required. Article 6(2) deems high-risk the AI systems listed in Annex III. Annex III enumerates the eight categories most relevant to FS: biometric identification and categorisation; critical infrastructure; education; employment; essential private services and public services and benefits, including creditworthiness assessment of natural persons (Annex III §5(b)) and risk assessment and pricing in life and health insurance (Annex III §5(c)); law enforcement; migration; administration of justice and democratic processes.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 6 and Annex III §5(b), §5(c)
- Notes: The formal AI Act classification is owned by `ai-act-triage`. This skill flags Annex III overlap as a routing trigger and elevates the tier where the use case is in scope. Annex III §5(b) creditworthiness and §5(c) life-and-health insurance pricing are the most-frequent FS triggers; Annex III §1 biometric identification is the next.

### 6. ISO/IEC 42001:2023 — AI system impact assessment

- Citation: ISO/IEC 42001:2023 "Information technology — Artificial intelligence — Management system", §6.1.2 "AI system impact assessment".
- Excerpt-paraphrase: §6.1.2 requires the organisation to perform an impact assessment of the AI system on individuals, groups of individuals, and societies, considering intended use, foreseeable misuse, and the operational context. The tier produced by this skill consumes the impact-assessment output and records the firm's risk-level placement.
- Link: https://www.iso.org/standard/42001 — ISO/IEC 42001:2023 §6.1.2
- Notes: ISO/IEC 42001 is voluntary/certifiable; firms pursuing certification use this anchor as the AI management-system frame.

## Secondary anchors (sector and cross-cutting)

### 7. NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)

- Citation: National Association of Insurance Commissioners, "Model Bulletin: Use of Artificial Intelligence Systems by Insurers" (adopted December 4, 2023), Sections 1-4 (general expectations) and AIS Program elements (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness).
- Excerpt-paraphrase: Insurers using AI systems are expected to adopt and implement an AIS Program proportionate to the use case's potential to harm consumers. The Bulletin frames a graduated expectation: greater oversight where AI affects consumers in eligibility, premium, claims, or coverage; lighter touch where the use case is back-office. The tier rubric uses "potential to harm consumers" as the spine of the insurance overlay's tier-elevation logic, not a different test.
- Link: https://content.naic.org/sites/default/files/inline-files/2023-12-4%20Model%20Bulletin_Adopted_0.pdf — Model Bulletin Sections 1-4 and AIS Program elements
- Notes: NAIC Bulletin is a model bulletin; binding only to the extent state DOIs adopt it. State adoption tracker maintained by the NAIC AI Working Group is the public reference for binding-status confirmation per jurisdiction.

### 8. Colorado Division of Insurance regulation implementing SB 21-169

- Citation: Colorado Division of Insurance, regulation implementing SB 21-169 (governance and risk management of External Consumer Data and Information Sources and predictive models in life-insurance underwriting) [verify regulation number and effective date].
- Excerpt-paraphrase: Carriers using ECDIS or predictive models in life-insurance underwriting in Colorado must implement a governance and risk-management framework, including a written policy, testing for unfair discrimination, consumer disclosure, and recourse. The tier rubric reads CO operating footprint as a tier-elevation factor for life-underwriting AI in scope of the regulation.
- Link: https://doi.colorado.gov/insurance-products/life-insurance/algorithm-and-predictive-model-governance — CO regulation [verify section]
- Notes: Insurance sector overlay anchor for CO footprint; risk-categorisation reads from the regulation's scope (life-insurance underwriting using ECDIS or predictive models).

### 9. New York DFS Insurance Circular Letter on AI and ECDIS (January 2024)

- Citation: NYDFS Insurance Circular Letter on the Use of Artificial Intelligence Systems and External Consumer Data and Information Sources in Insurance Underwriting and Pricing (January 17, 2024), [verify section] on governance, fairness testing, disclosure, and consumer recourse.
- Excerpt-paraphrase: The Circular Letter sets governance, fairness testing, disclosure, and consumer-recourse expectations for life-insurance underwriting and pricing using AI and ECDIS in NY. The tier rubric reads NY operating footprint as a tier-elevation factor for in-scope underwriting and pricing AI.
- Link: https://www.dfs.ny.gov/industry-guidance/circular-letters — Insurance Circular Letter (January 2024) [verify exact section]
- Notes: Insurance sector overlay anchor for NY footprint.

### 10. NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024)

- Citation: NYDFS Industry Letter, "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks" (October 16, 2024), [verify section] on AI-related cyber threats.
- Excerpt-paraphrase: Covered entities under 23 NYCRR Part 500 are expected to address AI-related cybersecurity risks in their cybersecurity program, including AI-enabled threats (deepfake-driven social engineering) and risks from the entity's own use of AI (prompt injection, training-data poisoning, model extraction). Tier-up factors apply at the time of the tiering decision; this is a current expectation, not a future one.
- Link: https://www.dfs.ny.gov/industry-guidance/industry-letters — Industry Letter October 2024 [verify section]
- Notes: Cyber cross-cutting overlay anchor; cited from `references/cross-cutting/cyber.md`.

### 11. CFPB Circular 2022-03 — Adverse action notification when using complex algorithms (withdrawn May 12, 2025; historical only)

- Citation: CFPB Circular 2022-03 (May 26, 2022), "Adverse action notification requirements in connection with credit decisions based on complex algorithms". **Withdrawn May 12, 2025; historical only.** Reg B §1002.9 continues to apply on its own terms.
- Excerpt-paraphrase: Creditors using complex algorithms must still provide a statement of specific reasons to applicants against whom adverse action is taken; the complexity of the model is not a defence to the specificity requirement under ECOA / Regulation B (15 USC §1691; 12 CFR §1002.9). The tier rubric reads any consumer-credit decisioning AI as customer-binding for tiering purposes; the conduct factor scores high on the strength of Reg B itself, not the withdrawn circular.
- Link: https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/ — Circular section "Required Information" referencing 15 USC §1691 and 12 CFR §1002.9 [historical reference]
- Notes: Banking and consumer-compliance overlay anchor; cited from the conduct cross-cutting overlay where present, and from the banking sector overlay.

### 12. OCC Heightened Standards (12 CFR Part 30 Appendix D)

- Citation: 12 CFR Part 30 Appendix D, "OCC Guidelines Establishing Heightened Standards for Certain Large Insured National Banks, Insured Federal Savings Associations, and Insured Federal Branches".
- Excerpt-paraphrase: The Heightened Standards apply to OCC-supervised banks meeting an asset-size threshold. They establish minimum standards for risk-governance frameworks including risk-appetite statements that name model risk. Tier-1 models in scope of an in-scope bank typically appear in the risk-appetite statement; the tier decision references the firm's appetite-statement classification.
- Link: https://www.ecfr.gov/current/title-12/chapter-I/part-30 — 12 CFR Part 30 Appendix D
- Notes: Banking sector overlay anchor; reach is OCC large-bank only.

### 13. FFIEC BSA/AML Examination Manual

- Citation: FFIEC Bank Secrecy Act/Anti-Money Laundering Examination Manual (current edition), sections on transaction monitoring, customer risk rating, and SAR governance [verify section reference].
- Excerpt-paraphrase: The manual sets supervisory expectations for BSA/AML programs including model risk for transaction-monitoring and customer-risk-rating systems. The tier rubric reads any AML, sanctions-screening, or fraud-decision AI as regulator-facing under the manual; threshold tuning and SAR-workflow integration drive the tier toward higher scoring on regulatory and conduct factors.
- Link: https://bsaaml.ffiec.gov/manual — Examination Manual [verify section]
- Notes: Banking and payments-fintech sector overlay anchor.

### 14. SEC Rule 15c3-5 — Market Access Rule

- Citation: 17 CFR 240.15c3-5 ("Risk management controls for brokers or dealers with market access").
- Excerpt-paraphrase: Brokers and dealers with market access must establish, document, and maintain risk-management controls and supervisory procedures designed to manage financial and regulatory risks of market access. Where execution algorithms or trading models drive routing or order-placement decisions, the tier rubric reads the model as an in-scope control under the rule and elevates the regulatory factor accordingly.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.15c3-5 — 17 CFR §240.15c3-5
- Notes: Capital-markets sector overlay anchor.

### 15. SEC Investment Advisers Act Rule 206(4)-7 and Rule 206(4)-1

- Citation: 17 CFR 275.206(4)-7 (Compliance procedures); 17 CFR 275.206(4)-1 (Investment Adviser Marketing).
- Excerpt-paraphrase: Rule 206(4)-7 requires advisers to adopt and implement written compliance policies; the annual review is a recurring re-tiering trigger where the use case scope has changed. Rule 206(4)-1 reaches AI-generated client communications and AI-generated performance presentations; the tier rubric reads any client-facing GenAI as Marketing-Rule-implicating where output reaches clients or prospective clients.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 — 17 CFR §275.206(4)-7 ; https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 — 17 CFR §275.206(4)-1
- Notes: Capital-markets sector overlay anchor.

### 16. SEC and BD Books-and-Records Rules (Rule 204-2; Rules 17a-3 and 17a-4)

- Citation: 17 CFR 275.204-2 (Books and records to be maintained by investment advisers); 17 CFR 240.17a-3 and 17 CFR 240.17a-4 (Records to be made and preserved by certain exchange members, brokers, and dealers).
- Excerpt-paraphrase: Books-and-records rules require advisers and BDs to make and preserve records supporting recommendations and trading decisions. AI-generated content supporting a recommendation or decision falls within preservation scope; the tier rubric flags books-and-records reach as a contributing factor on the regulatory factor where the model output is preservable.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.204-2 — 17 CFR §275.204-2 ; https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-3 — 17 CFR §240.17a-3
- Notes: Capital-markets sector overlay anchor.

### 17. Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 6, 2023)

- Citation: OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, "Interagency Guidance on Third-Party Relationships: Risk Management" (issued June 6, 2023).
- Excerpt-paraphrase: The interagency guidance sets risk-management expectations for banking organisations engaging third parties, including fintech and AI vendors. Where a sponsor-bank arrangement involves third-party-developed models, the bank retains accountability for model risk; the tier rubric elevates the vendor-dependence factor in sponsor-bank configurations.
- Link: https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-17.html — Bulletin 2023-17
- Notes: Payments-fintech and banking overlay anchor.

### 18. OCC, FRB, and FDIC Joint Statement on Bank-Fintech Arrangements (July 25, 2024)

- Citation: OCC / FRB / FDIC Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services (July 25, 2024) [verify exact date and title].
- Excerpt-paraphrase: The joint statement is operative for sponsor-bank programs and addresses end-customer reconciliation, FBO subledger posture, and deposit-insurance representation review. The tier rubric reads sponsor-bank arrangements as elevating the regulatory and concentration factors when the AI use case sits in the program operator's stack.
- Link: https://www.fdic.gov/news/financial-institution-letters — July 2024 Joint Statement section on bank-fintech deposit arrangements [verify exact citation]
- Notes: Payments-fintech overlay anchor. Cite alongside OCC Bulletin 2023-17 for sponsor-bank tiering.

### 19. NYDFS 23 NYCRR Part 500 (Cybersecurity Regulation)

- Citation: 23 NYCRR Part 500 ("Cybersecurity Requirements for Financial Services Companies"), as amended through the Second Amendment (effective November 2023; further compliance dates phased in through 2025).
- Excerpt-paraphrase: Covered entities must maintain a cybersecurity program based on a risk assessment, including governance, access controls, monitoring, incident response, and third-party risk management. The 2024 NYDFS Industry Letter on AI extends Part 500 to AI-specific risks. The tier rubric reads NY-licensed covered-entity status as a tier-up factor on the cyber factor when AI is in scope.
- Link: https://www.dfs.ny.gov/industry/cybersecurity — 23 NYCRR Part 500 sections on cybersecurity program governance
- Notes: Cyber cross-cutting overlay anchor.

### 20. GLBA Safeguards Rule and HIPAA Privacy/Security Rules

- Citation: 16 CFR Part 314 (FTC Safeguards Rule under Gramm-Leach-Bliley Act); 45 CFR Part 160 and Part 164 (HIPAA Privacy and Security Rules).
- Excerpt-paraphrase: GLBA Safeguards Rule applies to non-public personal information held by financial institutions; HIPAA applies to protected health information held by covered entities and business associates. The tier rubric reads NPI in inputs, training data, or retrieval corpus as a tier-up factor on the data-sensitivity factor; PHI reads as a higher tier-up.
- Link: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 — 16 CFR Part 314 ; https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C — 45 CFR Subchapter C (HIPAA Privacy and Security Rule sections)
- Notes: Privacy cross-cutting overlay anchor.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at decision-write time:

- OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026 — verbatim GenAI/agentic scope exclusion confirmed against the OCC PDF (footnote 3). The three issuances are the same joint document, not parallels. SR 11-7 and SR 21-8 are confirmed superseded as of April 17 2026.
- NIST AI 600-1 — confirm exact Measure subcategory numbering for the GenAI elements cited.
- NYDFS Insurance Circular Letter (January 2024) — confirm section reference.
- Colorado Division of Insurance regulation implementing SB 21-169 — confirm regulation number and effective date.
- NYDFS Industry Letter on AI cybersecurity (October 2024) — confirm section reference.
- FFIEC BSA/AML Examination Manual — confirm section reference for transaction-monitoring model expectations.
- OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 25, 2024) — confirm exact title, date, and operative status against the date of analysis.

Where verification is incomplete, the tiering record cites with the `[verify section]` flag carried forward; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy (specific tier names, quantitative cutoffs, named committees, named owners), and validation-depth mapping via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. Tier names and cutoffs are firm policy; the source anchors set the materiality factors that drive the tier, not the tier values.
