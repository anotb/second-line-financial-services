# Source anchors: rag-evaluation-review

Cited sources this skill anchors to. Each entry names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link. The skill cites these by file path; SKILL.md does not restate excerpts.

A practitioner note before the list. RAG evaluation sits at a particular intersection: model-risk validation expectations apply (where the firm's model risk programme treats the GenAI use case as in scope), and the broader AI-management framings apply, but the operational metric vocabulary in widest use (the RAGAS-style families: faithfulness, answer relevance, context precision, context recall) is **industry practice, not binding regulator language**. No US financial-services regulator names "RAGAS" or specifies particular RAG metric formulas in published guidance. The skill treats these metric families as the practitioner-standard framing for grounding evaluation, with the explicit caveat that any equivalent named framework or in-house equivalent is acceptable as long as the metric semantics are documented. Be explicit in the review about which expectations carry binding regulator language and which carry industry-practice weight.

## Primary anchors

### 1. Federal Reserve SR 11-7 / OCC Bulletin 2011-12 — Model Risk Management

- Citation: Board of Governors of the Federal Reserve System, SR 11-7 / OCC Bulletin 2011-12, "Guidance on Model Risk Management" (April 4, 2011), §V "Model Validation" with focus on the data-review and outcomes-analysis pillars applied to retrieval corpora and grounding outputs.
- Excerpt-paraphrase: SR 11-7 sets the federal supervisory expectation on model validation including independent review, conceptual soundness assessment, ongoing monitoring, and outcomes analysis. The data-review pillar applied to a RAG system covers the retrieval corpus: source quality, fitness for the intended use, freshness, coverage, and provenance. The outcomes-analysis pillar applied to a RAG system covers the grounding outputs: how well the system's outputs match the intended-purpose target, with attention to both Type-I and Type-II error patterns. SR 11-7 does not name "RAG" or "grounding evaluation" as terms; the connection is made by interpreting the validation expectations against the RAG architecture.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm — §V Model Validation
- Notes: Superseded for binding purposes by OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026 as of April 17 2026 (anchor 2). The substantive applicability to RAG systems is by analogy at firm policy level; the 2026 bulletin text excludes GenAI from scope.

### 2. Joint Interagency Revised Guidance on Model Risk Management — OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026

- Citation: Joint Interagency Revised Guidance on Model Risk Management, OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, dated April 17, 2026. The three issuances are the same joint document; supersedes SR 11-7 (2011) and SR 21-8 (2021).
- Excerpt-paraphrase (footnote 3, verbatim): "Generative AI and agentic AI models are novel and rapidly evolving. As such, they are not within the scope of this guidance. ... However, the principles described in this guidance apply to traditional statistical and quantitative models and non-generative, non-agentic AI models." Most relevant to banking organizations with over $30 billion in total assets; non-binding.
- Link: https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf — guidance text PDF
- Notes: A RAG system is generative AI and is not within this bulletin's scope. Cite the bulletin only for traditional-model framing (e.g., a non-generative classifier in a routing layer). For the substantive RAG-evaluation anchors, see NIST AI 600-1 (anchor 3), ISO/IEC 42001 (anchor 4), and the sector and cross-cutting overlays.

### 3. NIST AI RMF — Generative AI Profile (NIST AI 600-1)

- Citation: NIST AI 600-1, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (July 2024). Relevant subcategories include Measure 2.9 (information integrity, including provenance and verifiability), Measure 1.1 (hallucination/confabulation), Manage 4.1 (deployment monitoring), and Govern 6.1 (third-party considerations) [verify exact subcategory numbering].
- Excerpt-paraphrase: The Generative AI Profile extends the NIST AI RMF for GenAI-specific concerns. Information integrity (Measure 2.9) covers provenance and verifiability, which maps directly to the corpus-fitness and citation-precision elements of a RAG evaluation. Confabulation/hallucination (Measure 1.1) is named explicitly; the GenAI Profile recommends measurement and monitoring for confabulation rate. Deployment monitoring (Manage 4.1) covers the production-monitoring expectations. Third-party considerations (Govern 6.1) cover the foundation-model and vendor dependencies.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Generative AI Profile (NIST AI 600-1), Measure and Manage section [verify section] for subcategory numbering
- Notes: NIST AI RMF and the GenAI Profile are voluntary, not binding. They are the leading-practice anchor most second-line AI governance functions cite when framing grounding evaluation. The Profile names hallucination and information integrity as risks but does not specify particular metric formulas; the metric-family selection is left to the firm.

### 4. ISO/IEC 42001:2023 — Artificial Intelligence Management System

- Citation: ISO/IEC 42001:2023 "Information technology — Artificial intelligence — Management system", §8.1 "Operational planning and control", §9.1 "Monitoring, measurement, analysis and evaluation", and Annex A controls relevant to AI lifecycle including data quality and operational performance [verify Annex A control IDs].
- Excerpt-paraphrase: ISO/IEC 42001 sets management-system expectations for AI. Operational planning and control (§8.1) covers the controls applied during the operation of an AI system, including data inputs and processing. Monitoring and measurement (§9.1) covers the ongoing measurement of system performance against defined criteria. The Annex A controls include items relevant to data quality, performance monitoring, and risk treatment.
- Link: https://www.iso.org/standard/42001 — ISO/IEC 42001:2023 §8.1, §9.1 and Annex A
- Notes: Voluntary/certifiable. Firms pursuing certification use this anchor as the AI management-system frame.

### 5. EU AI Act Article 10 — Data and Data Governance

- Citation: Regulation (EU) 2024/1689 (EU AI Act), Article 10, "Data and data governance", with applicability to high-risk AI systems per Article 6 and Annex III.
- Excerpt-paraphrase: Article 10 sets requirements for training, validation, and testing data sets used in high-risk AI systems: relevant, sufficiently representative, free of errors, complete with regard to the intended purpose, with consideration for the geographical, behavioural, contextual, or functional setting. Although Article 10 is framed for training data, the data-governance principles (relevance, representativeness, completeness for the intended purpose) apply by analogy to retrieval corpora in a high-risk RAG system.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Regulation (EU) 2024/1689, Article 10
- Notes: Binding for high-risk AI systems with EU touch. The high-risk classification is the gating question; many FS use cases sit in the high-risk class under Annex III (Annex III items 5(b) credit-decisioning and 5(c) creditworthiness assessment apply to many bank and adviser use cases). Where the EU AI Act is in scope, the corpus-fitness framing in this skill aligns to Article 10 expectations.

## Industry-practice metric framework references (informational)

### 6. Industry-practice grounding-evaluation metric families (RAGAS-style)

- Citation: Industry-practice grounding-evaluation metric families commonly referenced as RAGAS-style: faithfulness (claim is entailed by retrieved context), answer relevance (response addresses the query), context precision (retrieved context contains content supporting the claim), context recall (retrieved context is sufficient to support the claim). The RAGAS framework (Es, Shahul et al., open-source library) is one named implementation; equivalent named frameworks include TruLens, DeepEval, and various in-house pipelines.
- Excerpt-paraphrase: These metric families are the practitioner-community standard for RAG evaluation as of 2024-2026. They are not specified in any US financial-services regulator's published guidance. The metric semantics differ across implementations; in particular, "citation precision" in some implementations measures whether the output contains a citation marker, and in other implementations measures whether the cited document section supports the claim. The latter definition is the meaningful one for second-line review purposes.
- Link: https://docs.ragas.io/ — RAGAS reference implementation, metrics section (open source), and equivalent framework documentation
- Notes: Industry-practice reference, **not binding regulation**. The skill treats this family as the practitioner-standard vocabulary for grounding evaluation. Any equivalent named framework or in-house equivalent is acceptable as long as the metric semantics are documented in the review (the `metric_definition` field carries the documentation). The skill does not endorse any specific framework; it requires that the metric semantics be explicit and that citation precision in particular be defined as supports-the-claim, not contains-a-marker.

## Sector and other secondary anchors

### 7. FFIEC IT Examination Handbook — Information Security and AIO booklets

- Citation: FFIEC Information Technology Examination Handbook, Information Security booklet (current edition) and Architecture, Infrastructure, and Operations booklet (June 2021), sections on data integrity, application security, third-party risk, change management [verify section reference for data-integrity guidance].
- Excerpt-paraphrase: The FFIEC IT Handbook sets supervisory expectations for IT and information security at federally supervised financial institutions including data-integrity controls on data sources used by applications. Retrieval corpora in a RAG system are data sources in the FFIEC framing; the integrity, access-control, and change-management expectations apply.
- Link: https://ithandbook.ffiec.gov — Information Security booklet and AIO booklet [verify section]
- Notes: Banking sector overlay anchor.

### 8. NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)

- Citation: National Association of Insurance Commissioners, "Model Bulletin: Use of Artificial Intelligence Systems by Insurers" (adopted December 4, 2023), AIS Program elements including risk management, testing-and-validation, third-party AI accountability, monitoring, and documentation.
- Excerpt-paraphrase: Insurers using AI systems are expected to adopt and implement an AIS Program addressing the named elements. The testing-and-validation element covers ongoing performance monitoring and the documentation element covers traceability. RAG-specific evaluation work feeds these elements; the documentation element supports the regulatory examination posture.
- Link: https://content.naic.org/sites/default/files/inline-files/2023-12-4%20Model%20Bulletin_Adopted_0.pdf — Model Bulletin and AIS Program elements
- Notes: Insurance sector overlay anchor. NAIC Bulletin is a model bulletin; binding only to the extent state DOIs adopt it. The state-adoption tracker maintained by the NAIC AI Working Group is the public reference for binding-status confirmation per jurisdiction.

### 9. SEC Investment Advisers Act Rule 206(4)-1 (Marketing Rule) and Rule 204-2 (Books and Records)

- Citation: 17 CFR §275.206(4)-1 (Investment Adviser Marketing) and 17 CFR §275.204-2 (Books and Records).
- Excerpt-paraphrase: AI-generated client-facing content from a registered investment adviser is subject to the Marketing Rule's general prohibitions and the books-and-records preservation. Where the RAG system feeds adviser-facing client content, the grounding-quality outputs (and the residual risk on grounding failures) are inputs to the firm's Marketing Rule compliance posture and to the records-retention posture.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 — 17 CFR §275.206(4)-1
- Notes: Capital-markets sector overlay anchor.

### 10. NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024)

- Citation: New York Department of Financial Services, "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks" (October 16, 2024) [verify section] on AI-related cybersecurity risks including model-supply-chain considerations relevant to retrieval-platform and foundation-model dependencies.
- Excerpt-paraphrase: Covered entities under 23 NYCRR Part 500 are expected to address AI-related cybersecurity risks within their existing cybersecurity programs. The letter signals supervisory expectation for how Part 500 obligations on third-party service-provider security and incident response apply to AI deployments. For a RAG system, the corpus access-control framing and the retrieval-platform supply-chain framing connect to the cyber overlay.
- Link: https://www.dfs.ny.gov/industry-guidance/industry-letters — Industry Letter October 16, 2024 [verify section]
- Notes: Cyber cross-cutting overlay anchor; pointer to `prompt-injection-risk/references/source-anchors.md` for the full NYDFS framing.

### 11. GLBA Safeguards Rule (16 CFR Part 314)

- Citation: 16 CFR Part 314, FTC Standards for Safeguarding Customer Information (Safeguards Rule), as amended December 2021, with notification provisions added October 2023 effective May 2024 (16 CFR §314.5(d)).
- Excerpt-paraphrase: Financial institutions in scope of the Safeguards Rule must implement an information security program and, since May 2024, must notify the FTC of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers. A confirmed cross-scope leakage event from a RAG system involving customer NPI may meet the notification threshold.
- Link: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 — 16 CFR §314.5(d)
- Notes: Privacy cross-cutting overlay anchor; relevant for non-bank financial institutions in FTC scope.

### 12. HIPAA Privacy Rule and Security Rule

- Citation: 45 CFR Part 164 Subpart E (Privacy Rule, Use and Disclosure including minimum-necessary at §164.502(b)) and 45 CFR Part 164 Subpart C (Security Rule, technical safeguards at §164.312).
- Excerpt-paraphrase: HIPAA-covered entities and business associates handling PHI are subject to minimum-necessary requirements on use and disclosure (Privacy Rule) and to technical safeguards including access controls, audit controls, integrity, and transmission security (Security Rule). For a RAG system retrieving over PHI corpora, retrieval-side scoping is the operational mechanism for minimum-necessary; technical safeguards apply to the retrieval-platform and the audit-logging programme.
- Link: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164 — 45 CFR §164.502(b) and §164.312
- Notes: Insurance sector overlay anchor (life/health insurer claims-summary use cases) and privacy cross-cutting overlay anchor where PHI is in the corpus.

### 13. CFPB UDAAP framework

- Citation: Dodd-Frank Wall Street Reform and Consumer Protection Act, §1031 (prohibition on unfair, deceptive, or abusive acts or practices) and §1036 (CFPB enforcement authority); CFPB Consumer Financial Protection Circulars on UDAAP including circulars on chatbots and AI in consumer finance.
- Excerpt-paraphrase: The CFPB enforces the UDAAP framework for consumer-facing financial services. Inaccurate AI-generated communications (deception by inaccurate statement) are within UDAAP scope. The grounding-quality outputs and the residual risk on grounding failures are inputs to the firm's UDAAP exposure posture for any customer-facing use case.
- Link: https://www.consumerfinance.gov/compliance/circulars/ — CFPB Circulars index section, including circulars on chatbot supervision in consumer finance
- Notes: Conduct cross-cutting overlay anchor.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at SKILL.md write time and at memo-write time:

- OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026 — verbatim GenAI/agentic scope exclusion confirmed against the OCC PDF (footnote 3). The three issuances are the same joint document, not parallels. RAG systems are generative AI and out of scope of this bulletin; for binding RAG-evaluation expectations there is no current US bank-supervisory anchor — anchor to NIST AI 600-1, ISO/IEC 42001, and overlays.
- NIST AI 600-1 — confirm exact subcategory numbering for Measure 2.9 (information integrity), Measure 1.1 (hallucination/confabulation), Manage 4.1 (deployment monitoring), and Govern 6.1 (third-party considerations).
- ISO/IEC 42001:2023 — confirm Annex A control IDs relevant to data quality, performance monitoring, and risk treatment.
- FFIEC IT Examination Handbook — confirm section reference for data-integrity guidance applicable to retrieval-corpus controls.
- NYDFS Industry Letter on AI cybersecurity (October 2024) — confirm exact section reference for AI-deployment supply-chain passages.

Where verification is incomplete, the SKILL.md cites with the `[verify section]` flag carried forward; do not invent.

## Industry-practice framing reminder

The RAGAS-style metric families (faithfulness, answer relevance, context precision, context recall, citation precision when defined as supports-the-claim, refusal rate on a labelled out-of-scope set) are the practitioner-standard vocabulary for grounding evaluation. They are **not specified in any US financial-services regulator's published guidance**. Any equivalent named framework or in-house equivalent is acceptable provided the metric semantics are documented. The skill does not over-claim binding regulator language for these metrics; the substantive anchors are the AI-specific frameworks (NIST AI 600-1 Measure 2.9 information integrity and Measure 1.1 confabulation, ISO/IEC 42001 §8.1 / §9.1) applied to RAG by analogy. The bank model-risk bulletin (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026) excludes generative AI from scope and is not the binding hook for RAG evaluation.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy, named owners, and named metric framework via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. An advisory firm shipping a client-specific overlay does the same thing under a separate overlay file.
