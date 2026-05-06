# Source anchors: genai-pre-prod-review

Cited sources this skill anchors to. Each entry names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link. The skill cites these by file path; SKILL.md does not restate excerpts.

A practitioner note before the list: the GenAI pre-prod gate review pulls together upstream artefacts (intake, tier, model card, validation-plan results, prompt-injection review, RAG evaluation, vendor evidence review where applicable) and produces a gate decision. The source coverage therefore comes through the upstream skills as well as the model-risk and AI-governance anchors named here. For sector-specific and cross-cutting anchors, see the loaded overlay files.

## Primary anchors

### 1. Federal Reserve SR 11-7 / OCC Bulletin 2011-12 — Model Risk Management

- Citation: Board of Governors of the Federal Reserve System, SR 11-7 / OCC Bulletin 2011-12, "Guidance on Model Risk Management" (April 4, 2011), §III "Governance, Policies, and Controls", §IV "Model Validation", §V "Model Documentation".
- Excerpt-paraphrase: SR 11-7 §III sets the supervisory expectation that banks have governance, policies, and controls covering model risk including roles for model owners, validators, and senior management. §IV sets the validation expectations (independent review, conceptual soundness, ongoing monitoring, outcomes analysis) and includes the effective challenge expectation (validators with sufficient stature, knowledge, and incentive to challenge the model). §V sets documentation expectations covering model design, data, performance, controls, and limitations. The pre-prod gate exercises all three: it confirms the governance set is in place, validates that validation has produced the expected evidence, and confirms documentation is current. Where the firm's model risk programme treats a GenAI use case as in scope of SR 11-7, the gate review applies these expectations to the GenAI artefact set.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm — §III, §IV, §V
- Notes: Binding on federally regulated banks. Applicability to GenAI is a firm-by-firm interpretation; many firms now treat in-scope GenAI use cases as models for the purposes of the model risk programme. The 2026 interagency revision (anchor 2) refreshes this for AI/ML and GenAI explicitly.

### 2. OCC Bulletin 2026-13 — Revised Interagency Model Risk Management Guidance

- Citation: OCC Bulletin 2026-13, "Revised Interagency Guidance on Model Risk Management" (issued 2026 by OCC; FDIC and Federal Reserve parallel issuances expected) [verify section on pre-implementation review and AI/ML scope].
- Excerpt-paraphrase: The revised guidance refreshes SR 11-7 documentation, validation, and governance expectations to incorporate AI/ML and generative-AI use cases including foundation-model dependence, retrieval-augmented generation, tool use, and agentic configurations. Pre-implementation review expectations include the gate-review motion as a component of the governance and controls set.
- Link: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html — Bulletin 2026-13 [verify section]
- Notes: Confirm published bulletin section numbering at SKILL.md write time. Until verified, the SKILL.md and gate-review memo do not over-claim binding language on pre-implementation review from this bulletin.

### 3. FDIC FIL on Revised Interagency Model Risk Management Guidance, 2026

- Citation: FDIC Financial Institution Letter on the Revised Interagency Model Risk Management Guidance (2026 parallel issuance) [verify FIL number and section].
- Excerpt-paraphrase: FDIC parallel issuance to OCC Bulletin 2026-13 setting equivalent expectations for FDIC-supervised institutions. Pre-implementation review expectations align with the OCC bulletin.
- Link: https://www.fdic.gov/news/financial-institution-letters/ — [verify FIL number and section]
- Notes: Confirm published FIL number and section at SKILL.md write time.

### 4. Federal Reserve SR Letter on Revised Interagency Model Risk Management Guidance, 2026

- Citation: Federal Reserve SR Letter on the Revised Interagency Model Risk Management Guidance (2026 parallel issuance) [verify SR number and section].
- Excerpt-paraphrase: Federal Reserve parallel issuance to OCC Bulletin 2026-13 setting equivalent expectations for FRB-supervised holding companies and state-member banks. Pre-implementation review expectations align with the OCC bulletin.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/ — [verify SR number and section]
- Notes: Confirm published SR letter number and section at SKILL.md write time.

### 5. NIST AI Risk Management Framework 1.0

- Citation: NIST AI 100-1, "Artificial Intelligence Risk Management Framework (AI RMF 1.0)" (January 2023), Map function (Map 1.x to Map 5.x including Map 5.1 impact assessment), Manage function (Manage 1.1 to 1.4 managing risks at deployment, Manage 4.1 deployment monitoring).
- Excerpt-paraphrase: The AI RMF describes the Map function (context, categorisation, assessment of AI-related risks) and the Manage function (allocating risk-management resources, prioritising risks, responding to risks, and decommissioning). Map 5.1 covers impact assessment on individuals, groups, and society. Manage 1.1 to 1.4 cover the actions taken at deployment to manage residual risks. Manage 4.1 covers monitoring of deployed AI systems. The pre-prod gate review is the moment the firm consolidates the Map output, confirms the Manage actions are in place, and signs the deployment readiness against the Manage 4.1 monitoring expectation.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — AI RMF 1.0 Map function (Map 5.1 section) and Manage function (Manage 1.x and 4.1 sections)
- Notes: Voluntary, not binding. The most-cited leading-practice reference for AI governance.

### 6. NIST AI 600-1 — Generative AI Profile

- Citation: NIST AI 600-1, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (July 2024), Map and Manage subcategories specific to GenAI deployment readiness [verify exact subcategory numbering for foundation-model dependencies, content provenance, hallucination posture, harmful content mitigation, dangerous capability containment].
- Excerpt-paraphrase: The Generative AI Profile extends the NIST AI RMF for GenAI-specific concerns. It names risk classes that the pre-prod gate review must consider: foundation-model dependencies (third-party-risk under Govern), content provenance, hallucination posture, harmful-content mitigation, dangerous-capability containment, and prompt-injection threat surface. It sets actions under Manage and Measure for managing those risks at deployment.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Generative AI Profile (NIST AI 600-1), Map and Manage subcategory section [verify section]
- Notes: Voluntary. The leading-practice anchor for GenAI-specific gate review considerations.

### 7. ISO/IEC 42001:2023 — Artificial Intelligence Management System

- Citation: ISO/IEC 42001:2023 "Information technology — Artificial intelligence — Management system", §8.1 "Operational planning and control", §8.3 "AI system lifecycle controls", §9.x "Performance evaluation" [verify §9.x sub-clause numbers].
- Excerpt-paraphrase: ISO/IEC 42001 sets management-system expectations for AI including operational planning and control (§8.1), AI system lifecycle controls covering risk assessment, design, deployment, operation, and decommissioning (§8.3), and performance evaluation expectations (§9.x). The pre-prod gate sits inside the §8.3 lifecycle expectation as the deployment-readiness review.
- Link: https://www.iso.org/standard/42001 — ISO/IEC 42001:2023 §8.1, §8.3, §9.x
- Notes: Voluntary / certifiable. Firms pursuing certification cite this anchor as the AI management-system frame.

### 8. EU AI Act — Article 9 (risk management system)

- Citation: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 9 "Risk management system" (text adopted June 2024, entered into force August 2024, phased application).
- Excerpt-paraphrase: Article 9 requires high-risk AI systems to have a risk-management system established, implemented, documented, and maintained as a continuous iterative process throughout the entire lifecycle, requiring regular systematic review and updating. Includes identification and analysis of known and reasonably foreseeable risks; estimation and evaluation of risks; adoption of risk-management measures. The pre-prod gate is the deployment-readiness checkpoint inside this iterative process where the use case is in scope of the EU AI Act as a high-risk system.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 9
- Notes: Binding for AI systems placed on the EU market or affecting persons in the EU, where in scope as high-risk. The financial-services use cases most likely to fall in scope are creditworthiness assessment (Annex III, point 5(b)) and life-and-health insurance risk assessment and pricing (Annex III, point 5(c)).

### 9. EU AI Act — Article 13 (transparency to deployers)

- Citation: Regulation (EU) 2024/1689, Article 13 "Transparency and provision of information to deployers".
- Excerpt-paraphrase: Article 13 requires high-risk AI systems to be designed and developed so that operation is sufficiently transparent to enable deployers to interpret the system's output and use it appropriately. Includes requirement for instructions for use containing information including the system's intended purpose, accuracy, robustness, cybersecurity, expected lifetime, and any foreseeable changes that could affect performance. The deployer-side gate review consumes the provider-supplied transparency artefacts as input.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 13
- Notes: Binding for high-risk AI systems in the EU.

### 10. EU AI Act — Article 14 (human oversight)

- Citation: Regulation (EU) 2024/1689, Article 14 "Human oversight".
- Excerpt-paraphrase: Article 14 requires high-risk AI systems to be designed and developed in such a way that they can be effectively overseen by natural persons during the period the AI system is in use. Human oversight aims to prevent or minimise risks to health, safety, or fundamental rights. Includes capabilities for the natural persons to understand the system's capacities and limitations, to remain aware of automation bias, to interpret the output, to decide not to use it, and to intervene or interrupt. The pre-prod gate's human-oversight section maps directly to Article 14 expectations where the use case is in scope.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 14
- Notes: Binding for high-risk AI systems in the EU.

### 11. EU AI Act — Article 26 (deployer obligations)

- Citation: Regulation (EU) 2024/1689, Article 26 "Obligations of deployers of high-risk AI systems".
- Excerpt-paraphrase: Article 26 sets obligations on deployers including using the system in accordance with the instructions for use, ensuring human oversight per Article 14, monitoring operation and informing providers of risks and serious incidents, keeping logs, performing data protection impact assessments where applicable, and informing affected workers and natural persons subject to the system. The deployer-side pre-prod gate review is the moment the firm confirms the deployer-obligation set is in place before initial use.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 26
- Notes: Binding for deployers of high-risk AI systems in the EU. The financial-services entity acting as deployer is in scope where the use case is high-risk.

### 12. EU AI Act — Article 15 (accuracy, robustness, cybersecurity)

- Citation: Regulation (EU) 2024/1689, Article 15 "Accuracy, robustness and cybersecurity".
- Excerpt-paraphrase: Article 15 requires high-risk AI systems to achieve appropriate levels of accuracy, robustness, and cybersecurity, and to perform consistently throughout the lifecycle. Includes resilience to errors, faults, or inconsistencies, and resilience to attempts by unauthorised third parties to alter use, output, or performance through exploitation of vulnerabilities (which covers prompt injection and adversarial attacks).
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 15
- Notes: Binding for high-risk AI systems in the EU. The robustness and cybersecurity expectations in Article 15 read alongside the validation-plan robustness scope and the prompt-injection review residual risk.

### 13. NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024)

- Citation: New York Department of Financial Services, "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks" (October 16, 2024), [verify section] on AI-enabled threats and the entity's own use of AI.
- Excerpt-paraphrase: Covered entities under 23 NYCRR Part 500 are expected to address AI-related cybersecurity risks within their existing cybersecurity programmes. The pre-prod gate cyber items (identity, logging, IR readiness, prompt-injection posture) are part of how the firm's existing Part 500 obligations apply to AI deployments. Existing Part 500 obligations on risk assessment, third-party service-provider security, multi-factor authentication, monitoring, and incident response apply to the AI surface.
- Link: https://www.dfs.ny.gov/industry-guidance/industry-letters — Industry Letter October 16, 2024 [verify section]
- Notes: Binding for NYDFS-covered entities. For entities outside NYDFS scope, this is industry-practice reference and a directional indicator of where state-cyber supervisors are heading.

### 14. US Treasury Department Report on Managing Artificial Intelligence-Specific Cybersecurity Risks in the Financial Services Sector (March 2024)

- Citation: US Department of the Treasury, "Managing Artificial Intelligence-Specific Cybersecurity Risks in the Financial Services Sector" (March 2024) [verify exact title and date].
- Excerpt-paraphrase: Treasury report describing AI-specific cybersecurity risks observed in the financial services sector and recommended practices. Informational reference for the cyber overlay's pre-prod gate considerations on AI-specific cyber risks.
- Link: https://home.treasury.gov/system/files/136/Managing-Artificial-Intelligence-Specific-Cybersecurity-Risks-In-The-Financial-Services-Sector.pdf — Treasury report (March 2024), recommended-practices section [verify section]
- Notes: Informational, not binding. Useful as a sector-specific reference alongside the cyber overlay.

### 15. Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 6, 2023)

- Citation: OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, "Interagency Guidance on Third-Party Relationships: Risk Management" (issued June 6, 2023).
- Excerpt-paraphrase: The interagency guidance sets risk-management expectations for banking organizations engaging third parties, including AI vendors and foundation-model providers. The pre-prod gate's foundation-model dependency posture and swap-revalidation policy items align with the guidance's risk-management lifecycle: due diligence, contracting (notice and audit rights for change-of-version notice), ongoing monitoring (vendor change-of-version notice and re-validation flag).
- Link: https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-17.html — Bulletin 2023-17 sections on Risk Management Life Cycle
- Notes: Binding on banking organizations. Loaded via the banking sector overlay.

## Sector and other secondary anchors

### 16. NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)

- Citation: National Association of Insurance Commissioners, "Model Bulletin: Use of Artificial Intelligence Systems by Insurers" (adopted December 4, 2023), AIS Program elements including risk management, testing and validation, third-party AI accountability, monitoring, and documentation.
- Excerpt-paraphrase: Insurers using AI systems are expected to adopt and implement an AIS Program addressing the named elements. The pre-prod gate is the deployment-readiness moment where AIS Program documentation, third-party AI accountability, and monitoring expectations consolidate; the gate review records AIS Program element status by state where applicable.
- Link: https://content.naic.org/sites/default/files/inline-files/2023-12-4%20Model%20Bulletin_Adopted_0.pdf — Model Bulletin and AIS Program elements
- Notes: Binding only to the extent state DOIs adopt it. Loaded via the insurance sector overlay.

### 17. SEC Cybersecurity Disclosure Rules — 8-K Item 1.05 and Reg S-K Item 106

- Citation: 17 CFR 229.106 (Reg S-K Item 106, "Cybersecurity"); 17 CFR 249.308 (Form 8-K, Item 1.05, "Material Cybersecurity Incidents") (rules adopted July 26, 2023).
- Excerpt-paraphrase: Public registrants must disclose material cybersecurity incidents on Form 8-K within four business days of materiality determination (Item 1.05) and must disclose cybersecurity risk-management, strategy, and governance annually under Item 106. Where a GenAI use case has cyber-relevant incident potential, the pre-prod gate's incident-response readiness section evaluates the 8-K Item 1.05 trigger as part of the regulator-notification trigger list.
- Link: https://www.sec.gov/rules/final/2023/33-11216.pdf — Final Rule, July 2023, Sections II.A.1 and II.B.1
- Notes: Binding on SEC public registrants. Loaded via the cyber cross-cutting overlay.

### 18. 36-hour banking computer-security incident notification rule

- Citation: 12 CFR Part 53 (OCC), 12 CFR Part 225 Subpart N (FRB), 12 CFR Part 304 (FDIC) — "Computer-Security Incident Notification" (final rule effective May 1, 2022).
- Excerpt-paraphrase: Banking organizations must notify their primary federal regulator within 36 hours of determining that a notification incident has occurred (a cybersecurity event that materially disrupts or degrades, or is reasonably likely to materially disrupt or degrade, the bank's ability to deliver services). Pre-prod gate's incident-response readiness evaluates this trigger for GenAI events causing material disruption to bank operations.
- Link: https://www.occ.gov/news-issuances/federal-register/2021/86fr66424.pdf — Final Rule, November 2021, notification-incident definition section
- Notes: Binding on federally regulated banks. Loaded via the banking sector overlay.

### 19. GLBA Safeguards Rule (16 CFR Part 314)

- Citation: 16 CFR Part 314, FTC Standards for Safeguarding Customer Information (Safeguards Rule), as amended December 2021, with notification provisions added October 2023 effective May 2024 (16 CFR §314.5(d)).
- Excerpt-paraphrase: Financial institutions in scope of the Safeguards Rule must implement an information-security programme and notify the FTC of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers. Pre-prod gate's incident-response readiness evaluates the §314.5(d) trigger for GenAI events involving NPI exfiltration where applicable.
- Link: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 — 16 CFR §314.5(d)
- Notes: Binding for non-bank financial institutions in FTC scope. Loaded via the privacy cross-cutting overlay.

### 20. HIPAA Breach Notification Rule (45 CFR §§164.400-414)

- Citation: 45 CFR §§164.400-414, HIPAA Breach Notification Rule.
- Excerpt-paraphrase: Covered entities and business associates must notify affected individuals, the Secretary of HHS, and in some cases the media, following discovery of a breach of unsecured protected health information. Pre-prod gate's incident-response readiness evaluates this trigger for GenAI events involving PHI exfiltration where the use case is in scope of HIPAA.
- Link: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D — 45 CFR §§164.400-414
- Notes: Binding on HIPAA covered entities and business associates. Loaded via the privacy cross-cutting overlay (and the insurance sector overlay where the carrier handles PHI).

### 21. Public foundation-model provider system cards (form-factor reference)

- Citation: Anthropic, OpenAI, Google, and Meta system and model cards covering safety evaluations, deployment recommendations, and use-policy considerations. Examples include Anthropic Claude system cards, OpenAI GPT-4 and o-series system cards, Google Gemini model cards, Meta Llama responsible-use guides.
- Excerpt-paraphrase: Foundation-model provider system cards describe the vendor's evaluation approach, intended use, limitations, and recommended deployment considerations. They are vendor self-attestation; they do not test the firm's prompt template, retrieval corpus, tool inventory, or downstream use case. The pre-prod gate review consumes vendor system cards through the `llm-vendor-evidence-review` upstream artefact.
- Link: https://www.anthropic.com/news/claude-system-card and https://openai.com/safety — vendor system-card pattern reference, evaluations section and limitations section
- Notes: Form-factor reference only. Vendor results land at vendor-self-attestation confidence and never substitute for firm-side gate evidence.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at SKILL.md write time and at gate-review write time:

- OCC Bulletin 2026-13 — confirm published section numbering on pre-implementation review and AI/ML scope.
- FDIC FIL parallel issuance — confirm FIL number and section.
- Federal Reserve SR letter parallel issuance — confirm SR number and section.
- NIST AI 600-1 — confirm exact Map and Manage subcategory numbering for the pre-prod-gate-relevant entries (foundation-model dependencies, content provenance, hallucination posture, harmful-content mitigation, dangerous-capability containment).
- ISO/IEC 42001:2023 §9.x — confirm sub-clause numbering for performance-evaluation expectations.
- NYDFS Industry Letter on AI cybersecurity (October 2024) — confirm exact section reference for the relevant passages.
- US Treasury Department report on AI-Specific Cybersecurity Risks — confirm exact title and date.

Where verification is incomplete, the SKILL.md cites with the `[verify section]` flag carried forward; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy, and named owners via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. An advisory firm shipping a client-specific overlay does the same thing under a separate overlay file.
