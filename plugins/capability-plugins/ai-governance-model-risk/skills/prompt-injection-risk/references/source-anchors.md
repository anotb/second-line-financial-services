# Source anchors: prompt-injection-risk

Cited sources this skill anchors to. Each entry names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link. The skill cites these by file path; SKILL.md does not restate excerpts.

A practitioner note before the list: prompt injection sits across two regulator perspectives. The cyber framings (NYDFS, SEC cyber disclosure, FFIEC) carry binding supervisory expectation in their respective scopes. The AI-specific framings (NIST AI 600-1, OWASP LLM Top 10, MITRE ATLAS, NCSC AI guidance) are leading-practice references; they are not, in themselves, binding regulation. The model-risk framing (SR 11-7, OCC 2026-13) applies to GenAI as model-risk extension where the bank's own model risk program treats the GenAI use case as in scope. Be explicit about which regulator scope is in play in any individual review.

## Primary anchors

### 1. NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024)

- Citation: New York Department of Financial Services, "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks" (October 16, 2024), [verify section] on AI-enabled threats including prompt injection, data poisoning, social engineering, and the entity's own use of AI.
- Excerpt-paraphrase: Covered entities under 23 NYCRR Part 500 are expected to address AI-related cybersecurity risks within their existing cybersecurity programs. The letter calls out AI-enabled social engineering and deepfakes as external threats, and prompt injection, data poisoning, and model-supply-chain risks as risks arising from the entity's own deployment of AI. Existing Part 500 obligations on risk assessment, third-party service-provider security, multi-factor authentication, monitoring, and incident response apply to the AI surface. The letter does not create new rules; it signals supervisory expectation for how Part 500 is applied to AI.
- Link: https://www.dfs.ny.gov/industry-guidance/industry-letters — Industry Letter October 16, 2024 [verify section]
- Notes: Binding for NYDFS-covered entities (state-chartered banks, insurers, money transmitters, virtual currency businesses operating in NY). For entities outside NYDFS scope, this is industry-practice reference and a directional indicator of where state-cyber supervisors are heading. The accompanying 23 NYCRR Part 500 sections that bite for prompt-injection events are §500.9 (risk assessment), §500.11 (third-party service provider security), §500.16 (incident response and business-continuity plan), and §500.17(a) (notice to superintendent on cybersecurity events meeting the 72-hour notice criteria).

### 2. NIST AI 600-1 — Generative AI Profile

- Citation: NIST AI 600-1, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (July 2024), Manage and Measure subcategories on prompt-injection mitigation, downstream-impact management, and third-party considerations [verify exact subcategory numbering].
- Excerpt-paraphrase: The Generative AI Profile extends the NIST AI RMF for GenAI-specific concerns. The profile names prompt injection as a recurring risk class and sets out actions in the Manage function (mitigation selection and deployment) and the Measure function (testing approach for adversarial inputs including prompt-injection variants). It treats foundation-model dependence as a third-party-risk concern under Govern, with implications for the firm's ability to monitor for upstream changes that affect the prompt-injection posture.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Generative AI Profile (NIST AI 600-1), Manage and Measure section [verify subcategory numbering for the prompt-injection-specific entries]
- Notes: NIST AI RMF and the GenAI Profile are voluntary, not binding. They are the leading-practice anchor most second-line AI governance functions cite when framing the prompt-injection threat surface. The CSF 2.0 mapping and the Profile's worked examples are useful for cross-referencing existing cyber control framings to AI-specific risk classes.

### 3. OWASP Top 10 for Large Language Model Applications

- Citation: OWASP Top 10 for LLM Applications [verify edition; v1.1 published 2023, v2.0 in development as of 2025], LLM01 Prompt Injection (direct and indirect), LLM02 Insecure Output Handling, LLM03 Training Data Poisoning, LLM06 Sensitive Information Disclosure, LLM07 Insecure Plugin Design, LLM08 Excessive Agency.
- Excerpt-paraphrase: LLM01 is the top-ranked risk class and is the canonical taxonomy for prompt injection in the practitioner community. It distinguishes direct injection (the user crafts a prompt that overrides the system instruction) from indirect injection (instructions arrive through a content carrier that the LLM consumes, e.g., a retrieved document, a tool output, a multimodal input). Adjacent entries cover related vectors: LLM02 covers downstream consequences when the LLM's output is consumed without sanitisation, LLM06 covers exfiltration of sensitive content from the system prompt or training data, LLM07 covers tool/plugin design weaknesses that magnify injection impact, LLM08 covers excessive agency where the LLM has the authority to take consequential actions.
- Link: https://owasp.org/www-project-top-10-for-large-language-model-applications/ — Top 10 list, LLM01 section, current edition [verify version at SKILL.md write time]
- Notes: OWASP is not a regulator. The taxonomy is industry-practice and is the vocabulary most commonly used in vendor red-team reports, third-party assessments, and internal AI-security programmes. It is not, by itself, binding on a regulated firm; it is the framing the second-line review uses to organise the threat surface and tested attack classes.

### 4. MITRE ATLAS — Adversarial Threat Landscape for AI Systems

- Citation: MITRE ATLAS, the adversarial-threat knowledge base for AI systems (modeled after MITRE ATT&CK), tactics and techniques covering reconnaissance, initial access, ML attack staging, evasion, exfiltration, and impact in AI-system contexts [verify exact technique IDs for prompt-injection-relevant entries].
- Excerpt-paraphrase: ATLAS catalogues adversarial tactics and techniques against AI systems with case studies drawn from public incidents and red-team disclosures. Prompt-injection-relevant techniques sit across initial access (e.g., LLM Prompt Injection technique), ML attack staging (e.g., LLM Jailbreak), evasion (e.g., Evade ML Model), and impact (e.g., External Harms, System Misuse for External Effect). The case studies are useful for grounding likelihood ratings in observed incident patterns rather than abstract assessment.
- Link: https://atlas.mitre.org/ — ATLAS matrix, case studies section [verify technique IDs at SKILL.md write time]
- Notes: ATLAS is industry-practice reference. It is the most widely used adversarial-threat taxonomy in AI red-teaming and is the cyber-team-friendly framing of what OWASP calls LLM01.

### 5. NCSC Guidelines for Secure AI System Development

- Citation: National Cyber Security Centre (UK) and Cybersecurity and Infrastructure Security Agency (US), "Guidelines for Secure AI System Development" (November 2023) [verify date and section references], joint guidance signed by 18 international cybersecurity agencies.
- Excerpt-paraphrase: The guidelines set secure-by-design expectations across the AI system lifecycle: secure design (threat modelling for AI-specific risks including prompt injection), secure development (supply-chain considerations for foundation models and components), secure deployment (operational controls for monitoring and incident response), secure operation and maintenance (lifecycle management of model updates). Prompt injection is named explicitly as a design consideration; the guidance recommends treating model inputs as untrusted by default.
- Link: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development — NCSC and CISA joint guidelines (November 2023) [verify exact section reference for prompt-injection guidance]
- Notes: Industry-practice reference. The guidelines are not binding; they carry weight because they are signed by US, UK, EU, and Asia-Pacific cybersecurity agencies and represent a converged international view.

### 6. Federal Reserve SR 11-7 / OCC Bulletin 2011-12 — Model Risk Management (applied to GenAI)

- Citation: Board of Governors of the Federal Reserve System, SR 11-7 / OCC Bulletin 2011-12, "Guidance on Model Risk Management" (April 4, 2011), §IV "Model Validation" and §V "Model Documentation".
- Excerpt-paraphrase: Where the firm's model risk program treats a GenAI use case as a model in scope of SR 11-7, the validation expectations apply: independent review, conceptual soundness, ongoing monitoring, and outcomes analysis. The prompt-injection review is the model-risk-side surfacing of the adversarial robustness component of validation. SR 11-7 does not name prompt injection by term; the connection is made by interpreting the validation expectations against the GenAI threat surface.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm — §IV Model Validation
- Notes: Binding on federally regulated banks. The applicability of SR 11-7 to GenAI is a firm-by-firm interpretation; many firms now treat in-scope GenAI use cases as models for the purposes of the model risk program. The 2026 interagency revision (OCC Bulletin 2026-13, see anchor 7) refreshes this for AI/ML and GenAI explicitly.

### 7. OCC Bulletin 2026-13 — Revised Interagency Model Risk Management Guidance

- Citation: OCC Bulletin 2026-13, "Revised Interagency Guidance on Model Risk Management" (issued 2026 by OCC; FDIC and Federal Reserve parallel issuances expected) [verify section on adversarial robustness and AI/ML scope].
- Excerpt-paraphrase: The revised guidance refreshes SR 11-7 documentation and validation expectations to incorporate AI/ML and generative-AI use cases, including foundation-model dependence, retrieval-augmented generation, tool use, and agentic configurations. Adversarial robustness (including prompt injection for GenAI) sits within the validation expectations.
- Link: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html — Bulletin 2026-13 [verify section]
- Notes: Confirm published bulletin section numbering at SKILL.md write time. Until verified, the SKILL.md and review memo do not over-claim binding language on adversarial robustness from this bulletin.

### 8. SEC Cybersecurity Disclosure Rules — 8-K Item 1.05 and Reg S-K Item 106

- Citation: 17 CFR 229.106 (Reg S-K Item 106, "Cybersecurity"); 17 CFR 249.308 (Form 8-K, Item 1.05, "Material Cybersecurity Incidents") (rules adopted July 26, 2023; effective dates phased).
- Excerpt-paraphrase: Public registrants must disclose material cybersecurity incidents on Form 8-K within four business days of materiality determination (Item 1.05) and must disclose cybersecurity risk management, strategy, and governance annually under Item 106. Where a prompt-injection event causes or contributes to a material cybersecurity incident (data exfiltration, unauthorised actions taken via tool privileges, third-party-service compromise), the 8-K disclosure obligation applies. The prompt-injection review supports the firm's materiality assessment by documenting the threat surface, the residual risk, and the response posture.
- Link: https://www.sec.gov/rules/final/2023/33-11216.pdf — Final Rule, July 2023, Sections II.A.1 and II.B.1
- Notes: Binding on SEC public registrants. The materiality assessment under 8-K Item 1.05 is the registrant's; the prompt-injection review is one input.

### 9. NIST SP 800-53 — Security and Privacy Controls (referenced for AI control mapping)

- Citation: NIST Special Publication 800-53 Rev. 5, "Security and Privacy Controls for Information Systems and Organizations" (September 2020), control families AC (Access Control), AU (Audit and Accountability), IR (Incident Response), SI (System and Information Integrity), SR (Supply Chain Risk Management).
- Excerpt-paraphrase: SP 800-53 is the federal control catalogue. It is referenced in this skill not as a primary AI anchor but as the underlying control framework for the cyber-side mitigations a prompt-injection review records: identity and access controls on the model's serving endpoint (AC family), audit logging of model invocations and retrievals (AU family), incident-response procedures (IR family), input validation and output filtering as system-integrity controls (SI family), and foundation-model and tool-supply-chain controls (SR family).
- Link: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final — NIST SP 800-53 Rev. 5, control families section (AC, AU, IR, SI, SR)
- Notes: SP 800-53 is binding for federal information systems; for FS firms it is informational and is the cyber team's vocabulary for control mapping.

### 10. ISO/IEC 42001:2023 — Artificial Intelligence Management System

- Citation: ISO/IEC 42001:2023 "Information technology — Artificial intelligence — Management system", §8.3 "AI system lifecycle controls" and Annex A controls relevant to AI security and adversarial robustness [verify Annex A control IDs].
- Excerpt-paraphrase: ISO/IEC 42001 sets management-system expectations for AI, including lifecycle controls covering risk assessment, design, deployment, operation, and decommissioning. The Annex A controls include items relevant to AI security (input validation, output controls, monitoring) that map to the prompt-injection mitigation set.
- Link: https://www.iso.org/standard/42001 — ISO/IEC 42001:2023 §8.3 and Annex A
- Notes: Voluntary/certifiable. Firms pursuing certification use this anchor as the AI management-system frame.

### 11. Public foundation-model provider system cards (form-factor reference)

- Citation: Anthropic, OpenAI, Google, and Meta system and model cards covering safety evaluations including prompt-injection and jailbreak testing. Examples include Anthropic Claude system cards, OpenAI GPT-4 and o-series system cards, Google Gemini model cards, Meta Llama responsible-use guides.
- Excerpt-paraphrase: Foundation-model provider system cards describe the vendor's adversarial testing approach, including prompt-injection variants tested, jailbreak resistance benchmarks, and refusal-behaviour calibration. They are vendor self-attestation; they do not test the firm's prompt template, retrieval corpus, or tool inventory.
- Link: https://www.anthropic.com/news/claude-system-card and https://openai.com/safety — vendor system-card pattern reference, evaluation section and limitations section
- Notes: Form-factor reference only. Vendor results land in the review at vendor-self-attestation confidence and never substitute for firm-side testing of the deployed system.

## Sector and other secondary anchors

### 12. FFIEC IT Examination Handbook — Information Security and Architecture, Infrastructure, and Operations booklets

- Citation: FFIEC Information Technology Examination Handbook, Information Security booklet (current edition) and Architecture, Infrastructure, and Operations booklet (June 2021), sections on application security, third-party risk, change management [verify section reference for AI-system-specific guidance].
- Excerpt-paraphrase: The FFIEC IT Handbook sets supervisory expectations for IT and information security at federally supervised financial institutions. The handbook does not yet have AI-specific sections in all booklets; AI systems are examined under the existing application-security, third-party-risk, and change-management framings. Prompt injection is examined as part of application security and input validation.
- Link: https://ithandbook.ffiec.gov — Information Security booklet and AIO booklet [verify section]
- Notes: Banking sector overlay anchor. FFIEC is the inter-agency examination council; member-agency exam manuals (OCC, FRB, FDIC, NCUA, CFPB) align to the booklets.

### 13. NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)

- Citation: National Association of Insurance Commissioners, "Model Bulletin: Use of Artificial Intelligence Systems by Insurers" (adopted December 4, 2023), AIS Program elements including risk management, testing and validation, third-party AI accountability, monitoring, and documentation.
- Excerpt-paraphrase: Insurers using AI systems are expected to adopt and implement an AIS Program addressing the named elements. Adversarial-robustness considerations including prompt injection sit within testing and validation; documentation expectations apply.
- Link: https://content.naic.org/sites/default/files/inline-files/2023-12-4%20Model%20Bulletin_Adopted_0.pdf — Model Bulletin and AIS Program elements
- Notes: Insurance sector overlay anchor. NAIC Bulletin is a model bulletin; binding only to the extent state DOIs adopt it. The state-adoption tracker maintained by the NAIC AI Working Group is the public reference for binding-status confirmation per jurisdiction.

### 14. SEC Investment Advisers Act Rule 206(4)-1 (Marketing Rule) and Rule 204-2 (Books and Records)

- Citation: 17 CFR 275.206(4)-1 (Investment Adviser Marketing) and 17 CFR 275.204-2 (Books and Records).
- Excerpt-paraphrase: AI-generated client-facing content from a registered investment adviser (e.g., a research-assistant draft published to clients) is subject to the Marketing Rule's general prohibitions and books-and-records preservation. A prompt-injection event that leads to misleading AI-generated client communications creates Marketing Rule and books-and-records exposure in addition to the cyber and conduct exposure.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 — 17 CFR §275.206(4)-1
- Notes: Capital-markets sector overlay anchor.

### 15. Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 6, 2023)

- Citation: OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, "Interagency Guidance on Third-Party Relationships: Risk Management" (issued June 6, 2023).
- Excerpt-paraphrase: The interagency guidance sets risk-management expectations for banking organizations engaging third parties, including AI vendors and foundation-model providers. Prompt-injection posture for a vendor-hosted GenAI use case is part of the third-party risk-management lifecycle: due diligence, contracting (notice and audit rights for adversarial-robustness testing), ongoing monitoring (vendor change-of-version notice).
- Link: https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-17.html — Bulletin 2023-17 sections on Risk Management Life Cycle
- Notes: Banking and payments-fintech sector overlay anchor.

### 16. GLBA Safeguards Rule (16 CFR Part 314)

- Citation: 16 CFR Part 314, FTC Standards for Safeguarding Customer Information (Safeguards Rule), as amended December 2021, with notification provisions added October 2023 effective May 2024 (16 CFR §314.5(d)).
- Excerpt-paraphrase: Financial institutions in scope of the Safeguards Rule must implement an information security program and, since May 2024, must notify the FTC of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers. A prompt-injection-driven exfiltration event involving customer NPI may meet the notification threshold.
- Link: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 — 16 CFR §314.5(d)
- Notes: Privacy cross-cutting overlay anchor; relevant for non-bank financial institutions in FTC scope.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at SKILL.md write time and at memo-write time:

- NYDFS Industry Letter on AI cybersecurity (October 2024) — confirm exact section reference for the prompt-injection passages.
- NIST AI 600-1 — confirm exact Manage and Measure subcategory numbering for the prompt-injection-specific entries.
- OWASP Top 10 for LLM Applications — confirm current edition (v1.1 vs v2.0 etc.) at write time.
- MITRE ATLAS — confirm exact technique IDs for the prompt-injection-relevant entries.
- NCSC Guidelines for Secure AI System Development — confirm exact section reference for the prompt-injection guidance.
- OCC Bulletin 2026-13 — confirm published section numbering on adversarial robustness and AI/ML scope.
- FDIC and Federal Reserve parallel issuances to OCC Bulletin 2026-13 — confirm number and section.
- ISO/IEC 42001:2023 — confirm Annex A control IDs relevant to the prompt-injection mitigation set.
- FFIEC IT Examination Handbook — confirm section reference for AI-system-specific guidance where it exists.

Where verification is incomplete, the SKILL.md cites with the `[verify section]` flag carried forward; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy, and named owners via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. An advisory firm shipping a client-specific overlay does the same thing under a separate overlay file.
