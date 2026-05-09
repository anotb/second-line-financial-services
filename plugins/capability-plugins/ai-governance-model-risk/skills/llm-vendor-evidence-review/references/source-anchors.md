# Source anchors: llm-vendor-evidence-review

Cited sources this skill anchors to. Each entry names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link. The skill cites these by file path; SKILL.md does not restate excerpts.

A practitioner note before the list: foundation-model vendor evidence-pack review sits across three regulator perspectives. The bank model-risk framing (the joint interagency Revised Guidance, OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026 issued April 2026) supersedes SR 11-7 and SR 21-8 but expressly excludes generative AI and agentic AI from its scope (footnote 3); for foundation-model evidence review of a GenAI use case the bulletin is not the binding hook. The third-party-risk framings (the 2023 interagency third-party guidance, DORA Article 28 for EU-scope entities) carry the entity-level wrapper that surrounds this skill's model-evidence layer. The AI-specific framings (NIST AI RMF and the Generative AI Profile, ISO/IEC 42001, EU AI Act GPAI provisions for in-scope models) are the substantive anchors for the foundation-model evidence questions. Be explicit about which regulator scope is in play in any individual review.

## Primary anchors

### 1. Federal Reserve SR 11-7 / OCC Bulletin 2011-12 — Model Risk Management

- Citation: Board of Governors of the Federal Reserve System, SR 11-7 / OCC Bulletin 2011-12, "Guidance on Model Risk Management" (April 4, 2011), §VI "Vendor and Third-Party Models".
- Excerpt-paraphrase: Where the firm's model risk programme treats a GenAI use case as a model in scope, the third-party-model expectations apply. The firm cannot delegate validation responsibility; the firm should perform appropriate validation activities on vendor models, recognising that proprietary methods may limit the depth of validation evidence available. Vendor documentation should be sufficient to support the firm's own ongoing monitoring and outcomes analysis. Vendor-developed models should receive the same validation rigor as internally developed models, scaled to materiality and complexity.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm — §VI Vendor and Third-Party Models
- Notes: SR 11-7 was the OCC/FRB joint guidance binding on federally regulated banks for over a decade. As of April 17, 2026 it is superseded by the joint interagency Revised Guidance on Model Risk Management (anchor 2). For traditional non-generative third-party models the supersession carries forward; for GenAI foundation-model evidence the 2026 bulletin is out of scope and the binding hook is firm policy informed by the AI-specific frameworks.

### 2. Joint Interagency Revised Guidance on Model Risk Management — OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026

- Citation: Joint Interagency Revised Guidance on Model Risk Management, OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, dated April 17, 2026. The three issuances are the same joint document; supersedes SR 11-7 (2011) and SR 21-8 (2021).
- Excerpt-paraphrase (footnote 3, verbatim): "Generative AI and agentic AI models are novel and rapidly evolving. As such, they are not within the scope of this guidance. ... However, the principles described in this guidance apply to traditional statistical and quantitative models and non-generative, non-agentic AI models." Most relevant to banking organizations with over $30 billion in total assets; non-binding. The bulletin contains no references to NIST publications.
- Link: https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf — guidance text PDF
- Notes: Foundation-model vendors are generative AI by definition and are not within this bulletin's scope. The third-party-model framing of the 2026 bulletin reaches non-generative vendor models only. For foundation-model evidence-pack review, anchor to NIST AI RMF Govern 6.x, NIST AI 600-1 Govern subcategories on third-party considerations, ISO/IEC 42001 §7.4 / §8.x, EU AI Act GPAI provisions where applicable, and the entity-level third-party guidance (anchor 3).

### 3. Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 6, 2023)

- Citation: OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, "Interagency Guidance on Third-Party Relationships: Risk Management" (issued June 6, 2023), sections on Risk Management Life Cycle (planning, due diligence, contract negotiation, ongoing monitoring, termination).
- Excerpt-paraphrase: The interagency guidance sets risk-management expectations for banking organizations engaging third parties, including AI vendors and foundation-model providers. The due-diligence section expects banking organizations to assess the third party's ability to perform the activity, including specialised technical capabilities; vendor evidence on the model itself feeds the technical-capability assessment. The ongoing-monitoring section expects continued attention to material changes affecting the relationship; vendor model-version swaps and new evidence-pack publications fall in scope.
- Link: https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-17.html — Bulletin 2023-17, Risk Management Life Cycle sections
- Notes: Binding for federally regulated banks. The entity-level wrapper for this skill's model-evidence layer; the entity-level diligence sits in `vendor-diligence` in `third-party-operational-resilience`.

### 4. NIST AI RMF 1.0 — Govern 6 (Third-Party Considerations)

- Citation: NIST, "Artificial Intelligence Risk Management Framework (AI RMF 1.0)" (January 2023), Govern 6 "Policies, processes, and procedures for the oversight of third parties' development, use, and integration of AI" — subcategories Govern 6.1 (third-party risk policies and procedures) and Govern 6.2 (contingencies for third-party AI risks).
- Excerpt-paraphrase: Organisations are expected to have policies and procedures for managing third-party AI risks, including risks arising from the development, deployment, and use of AI systems by third parties. The framework names the need for documented vendor risk-management procedures, contingency planning for third-party AI failures, and lifecycle attention to third-party AI from procurement through retirement.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — AI RMF 1.0, Govern 6 section
- Notes: Voluntary, not binding. The leading-practice anchor most second-line AI governance functions cite for third-party AI considerations. Maps to ISO/IEC 42001 §7.4 and §8.x.

### 5. NIST AI 600-1 — Generative AI Profile

- Citation: NIST AI 600-1, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (July 2024), Govern subcategories on third-party considerations and Manage subcategories on third-party risks for foundation-model dependence [verify exact subcategory numbering for the foundation-model and vendor-evidence entries].
- Excerpt-paraphrase: The Generative AI Profile extends the NIST AI RMF for GenAI-specific concerns. The Govern function carries guidance on third-party considerations specific to foundation-model providers, including system-card review and content-provenance expectations. The Manage function carries guidance on third-party risk management for GenAI, including monitoring for upstream changes that affect deployment and incident-disclosure expectations from vendors. The profile treats foundation-model dependence as a third-party-risk concern with named documentation expectations.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Generative AI Profile (NIST AI 600-1), Govern and Manage sections [verify subcategory numbering for foundation-model and vendor-evidence-specific entries]
- Notes: Voluntary, not binding. The most current leading-practice anchor for GenAI third-party considerations as of the skill's authoring. Subcategory numbering carries `[verify section]` flags pending second-pass confirmation.

### 6. ISO/IEC 42001:2023 — Artificial Intelligence Management System

- Citation: ISO/IEC 42001:2023 "Information technology — Artificial intelligence — Management system", §7.4 "Communication" (including supplier-side communication obligations), §8.1 "Operational planning and control", §8.3 "AI system lifecycle controls", and Annex A controls relevant to supplier and third-party AI [verify Annex A control IDs].
- Excerpt-paraphrase: ISO/IEC 42001 sets management-system expectations for AI, including supplier and third-party-AI controls. The communication section (§7.4) carries expectations on supplier-side information flows; the lifecycle section (§8.3) carries expectations on lifecycle controls including third-party AI evidence and ongoing monitoring. The Annex A controls include items relevant to third-party AI risk assessment, supplier monitoring, and supplier-incident handling.
- Link: https://www.iso.org/standard/42001 — ISO/IEC 42001:2023 §7.4, §8.1, §8.3, Annex A
- Notes: Voluntary/certifiable. Firms pursuing certification use this anchor as the AI management-system frame for supplier and third-party AI.

### 7. EU AI Act — Articles 51 to 55 (General-Purpose AI Models)

- Citation: Regulation (EU) 2024/1689 (EU AI Act), Articles 51 to 55, covering classification of general-purpose AI models, obligations of providers of GPAI models, GPAI models with systemic risk, codes of practice, and information requirements [verify article-by-article phasing dates and AI Office implementing acts at SKILL.md write time].
- Excerpt-paraphrase: Articles 51 to 55 set obligations for providers of general-purpose AI models, including documentation requirements (technical documentation, training-content summary, copyright-policy disclosures), information-sharing with downstream deployers, and additional obligations for GPAI models with systemic risk (model evaluations, adversarial testing, serious-incident reporting, cybersecurity protection). The information-sharing obligation supports downstream deployer compliance work; the GPAI-with-systemic-risk obligations support the depth of evidence available for high-impact deployments.
- Link: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 — Articles 51, 52, 53, 54, 55 [verify exact phasing dates and AI Office implementing acts current as of write time]
- Notes: Binding for in-EU-scope deployments. For non-EU-scope deployments, the GPAI provisions are informational reference and a directional indicator of converged international practice on foundation-model evidence expectations. The AI Office Code of Practice on General-Purpose AI is the voluntary instrument for demonstrating Article 53 compliance; published with signatory list. Adherence does not displace the underlying obligation, but for vendor evidence-pack review the signatory status and the vendor's adherence claims against the Code's measures are themselves evidence asks. GPAI provider obligations applied from 2 August 2025 under Article 113. Cite current effective dates and the published Code version at write time.

### 8. NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024)

- Citation: New York Department of Financial Services, "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks" (October 16, 2024), addressing AI-related cybersecurity risks including third-party AI service-provider security under 23 NYCRR §500.11 [verify section reference for third-party AI passages].
- Excerpt-paraphrase: NYDFS-covered entities under Part 500 are expected to address AI-related cybersecurity risks within their existing cybersecurity programmes. The letter calls out third-party AI service-provider security as an extension of existing §500.11 obligations: covered entities should evaluate the cybersecurity practices of AI vendors and address AI-specific risks through their third-party service-provider security programmes. The letter does not create new rules; it signals supervisory expectation for how Part 500 is applied to AI vendors.
- Link: https://www.dfs.ny.gov/industry-guidance/industry-letters — Industry Letter October 16, 2024 [verify section reference]
- Notes: Binding for NYDFS-covered entities (state-chartered banks, insurers, money transmitters, virtual currency businesses operating in NY). For entities outside NYDFS scope, this is industry-practice reference. Carried in the cyber cross-cutting overlay.

### 9. SOC 2 Trust Service Criteria and ISO/IEC 27001 (third-party attestation form-factors)

- Citation: AICPA Trust Service Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy (2017 Trust Services Criteria, with subsequent updates) [verify current edition]; ISO/IEC 27001:2022, "Information security, cybersecurity and privacy protection — Information security management systems — Requirements", Annex A controls.
- Excerpt-paraphrase: SOC 2 Type II reports are independent-auditor attestations covering the operating effectiveness of controls relevant to one or more Trust Service Criteria over a defined period. ISO/IEC 27001 certificates with the Statement of Applicability indicate certification to the information-security management-system standard with the specific Annex A controls in scope. Both are the third-party attestation form-factors most foundation-model vendors offer for security-posture evidence; the firm reviews the report (not just the opinion) for scope, relevant criteria, sub-service organisation considerations, and complementary user-entity controls.
- Link: https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc — SOC 2 Trust Service Criteria sections; https://www.iso.org/standard/27001 — ISO/IEC 27001:2022 Annex A controls section [verify section]
- Notes: Both are voluntary/audit-issued. The firm's CISO function reads the report for substantive content; the AI Governance Lead surfaces the key findings into the security-posture criterion. SOC 2 is the form-factor in US-centric procurement; ISO/IEC 27001 is the form-factor in EU and APAC.

### 10. Public foundation-model provider system cards and model cards (form-factor reference)

- Citation: Anthropic, OpenAI, Google, and Meta system and model cards covering model release notes, intended use, evaluation results, dangerous-capability evaluations, red-team summaries, training-data disclosures, and known limitations. Examples include Anthropic Claude system cards, OpenAI GPT-4 / GPT-4o / o-series system cards, Google Gemini model cards, Meta Llama responsible-use guides.
- Excerpt-paraphrase: Public foundation-model provider system and model cards are the form-factor in which foundation-model vendors publish the evidence this skill reviews. They typically cover intended-use scope, training-data posture (at varying depth), evaluation methodology and results, dangerous-capability evaluations, red-team summaries (often partial), known limitations and failure modes, and content-provenance posture. They are vendor self-attestation; they do not test the firm's prompt template, retrieval corpus, tool inventory, or downstream decisioning.
- Link: https://www.anthropic.com/news (search for system card releases); https://openai.com/safety; https://ai.google.dev/responsible (Gemini); https://ai.meta.com/responsible-ai/ (Llama) — system-card and model-card pattern reference, evaluation and limitations sections [verify section]
- Notes: Form-factor reference only. The skill does not endorse specific vendors. Vendor results land in the review at vendor-self-attestation confidence and never substitute for firm-side testing of the deployed system.

## Sector and other secondary anchors

### 11. NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)

- Citation: National Association of Insurance Commissioners, "Model Bulletin: Use of Artificial Intelligence Systems by Insurers" (adopted December 4, 2023), AIS Programme elements including third-party AI accountability, testing and validation, monitoring, and documentation.
- Excerpt-paraphrase: The Bulletin's AIS Programme elements include third-party AI accountability: insurers are expected to address vendor AI within their AIS Programme with named accountability, vendor risk-management procedures, evidence on testing and validation, and monitoring. The vendor evidence-pack review feeds the third-party-AI accountability and testing-and-validation elements.
- Link: https://content.naic.org/sites/default/files/inline-files/2023-12-4%20Model%20Bulletin_Adopted_0.pdf — Model Bulletin and AIS Programme elements
- Notes: Insurance sector overlay anchor. NAIC Bulletin is a model bulletin; binding only to the extent state DOIs adopt it. Carried in the insurance sector overlay.

### 12. FFIEC IT Examination Handbook — Information Security and Architecture, Infrastructure, and Operations booklets

- Citation: FFIEC Information Technology Examination Handbook, Information Security booklet (current edition) and Architecture, Infrastructure, and Operations booklet (June 2021), sections on application security, third-party risk, change management [verify section reference for AI-system-specific guidance].
- Excerpt-paraphrase: The FFIEC IT Handbook sets supervisory expectations for IT and information security at federally supervised financial institutions. AI vendors are examined under existing application-security, third-party-risk, and change-management framings; AI-specific sections are evolving across the booklets.
- Link: https://ithandbook.ffiec.gov — Information Security booklet and AIO booklet [verify section]
- Notes: Banking sector overlay anchor.

### 13. SEC Cybersecurity Disclosure Rules — 8-K Item 1.05 and Reg S-K Item 106

- Citation: 17 CFR 229.106 (Reg S-K Item 106, "Cybersecurity"); 17 CFR 249.308 (Form 8-K, Item 1.05, "Material Cybersecurity Incidents") (rules adopted July 26, 2023; effective dates phased).
- Excerpt-paraphrase: Public registrants must disclose material cybersecurity incidents on Form 8-K within four business days of materiality determination (Item 1.05) and disclose cybersecurity risk-management, strategy, and governance annually under Item 106. A vendor-AI cybersecurity incident contributing to a material incident triggers the obligation. The vendor evidence-pack review supports the firm's materiality assessment by documenting incident-disclosure history and cyber posture.
- Link: https://www.sec.gov/rules/final/2023/33-11216.pdf — Final Rule, July 2023, Sections II.A.1 and II.B.1
- Notes: Cyber cross-cutting overlay anchor for SEC-registered entities.

### 14. GLBA Safeguards Rule (16 CFR Part 314)

- Citation: 16 CFR Part 314, FTC Standards for Safeguarding Customer Information (Safeguards Rule), as amended December 2021, with notification provisions added October 2023 effective May 2024 (16 CFR §314.5(d)).
- Excerpt-paraphrase: Financial institutions in scope of the Safeguards Rule must implement an information security programme and notify the FTC of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers. Vendor-AI events involving customer NPI may meet the notification threshold.
- Link: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 — 16 CFR §314.5(d)
- Notes: Privacy and cyber cross-cutting overlay anchor for non-bank financial institutions in FTC scope.

### 15. SEC Investment Advisers Act Rule 206(4)-1 (Marketing Rule) and Rule 204-2 (Books and Records)

- Citation: 17 CFR 275.206(4)-1 (Investment Adviser Marketing) and 17 CFR 275.204-2 (Books and Records).
- Excerpt-paraphrase: AI-generated client-facing content from a registered investment adviser is subject to the Marketing Rule's general prohibitions and books-and-records preservation. Vendor evidence on output-control posture supports the firm's compliance assessment.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 — 17 CFR §275.206(4)-1; https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.204-2 — 17 CFR §275.204-2
- Notes: Capital-markets sector overlay anchor.

### 16. CFPB Circular on AI-driven adverse-action notices

- Citation: Consumer Financial Protection Bureau, Circular on the use of complex algorithms in adverse-action notices [verify circular number and date as of SKILL.md write time], addressing the use of AI and complex algorithms in credit and other consumer-financial-services decisioning.
- Excerpt-paraphrase: The CFPB has stated that the use of AI or complex algorithms does not relieve consumer-financial-services entities of the obligation to provide accurate, specific reason codes in adverse-action notices under ECOA / Regulation B. Vendor evidence on output-explanation-depth and refusal-around-determinative-statements supports the firm's adverse-action-notice compliance assessment.
- Link: https://www.consumerfinance.gov/compliance/circulars/ — CFPB Circulars index, AI/algorithm-relevant circular section [verify section]
- Notes: Conduct cross-cutting overlay anchor for CFPB-scope entities.

### 17. NIST SP 800-53 Rev. 5 (referenced for cyber-side control mapping)

- Citation: NIST Special Publication 800-53 Rev. 5, "Security and Privacy Controls for Information Systems and Organizations" (September 2020), control families AC, AU, IR, SI, SR.
- Excerpt-paraphrase: SP 800-53 is the federal control catalogue. It is referenced not as a primary AI anchor but as the underlying control framework for the cyber-side of vendor evidence: identity and access controls (AC), audit logging (AU), incident response (IR), system and information integrity (SI), supply-chain controls (SR).
- Link: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final — NIST SP 800-53 Rev. 5, control families section
- Notes: Cyber cross-cutting overlay anchor.

### 18. DORA — Article 28 (Critical ICT Third-Party Service Providers)

- Citation: Regulation (EU) 2022/2554 (Digital Operational Resilience Act), Article 28 "General principles" governing ICT third-party-service-provider arrangements [verify article and recital references applicable to AI-vendor arrangements].
- Excerpt-paraphrase: DORA sets requirements for EU financial entities engaging ICT third-party service providers, including AI vendors providing ICT-services. Article 28 covers risk-management requirements throughout the lifecycle of the arrangement; related articles cover contractual provisions, register of information, exit strategies, and oversight of critical ICT third-party service providers.
- Link: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554 — Article 28 [verify exact article and paragraph references]
- Notes: Binding for EU-supervised financial entities. Entity-level wrapper for EU-scope deployments; sits alongside the US interagency third-party guidance in `vendor-diligence`. Loaded conditionally where scope flags EU-jurisdictional in-scope.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at SKILL.md write time and at review-write time:

- OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026 — verbatim GenAI/agentic scope exclusion confirmed against the OCC PDF (footnote 3). The three issuances are the same joint document, not parallels. Foundation-model vendors are out of scope of this bulletin.
- NIST AI 600-1 — confirm exact Govern and Manage subcategory numbering for the foundation-model and vendor-evidence-specific entries.
- ISO/IEC 42001:2023 — confirm Annex A control IDs relevant to supplier and third-party AI.
- EU AI Act Articles 51 to 55 — confirm phasing dates, AI Office Code of Practice status, and AI Office implementing acts current as of write time.
- NYDFS Industry Letter on AI cybersecurity (October 2024) — confirm exact section reference for the third-party-AI passages.
- SOC 2 Trust Services Criteria — confirm current edition.
- FFIEC IT Examination Handbook — confirm section reference for AI-system-specific guidance where it exists.
- CFPB Circular on AI-driven adverse-action notices — confirm exact circular number and date.
- DORA Article 28 — confirm exact article and paragraph references applicable to AI-vendor arrangements.

Where verification is incomplete, the SKILL.md cites with the `[verify section]` flag carried forward; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy, and named owners via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. An advisory firm shipping a client-specific overlay does the same thing under a separate overlay file.
