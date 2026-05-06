# Source anchors: agentic-ai-controls

Cited sources this skill anchors to. Each entry names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link. The skill cites these by file path; SKILL.md does not restate excerpts.

A practitioner note before the list: agentic AI sits across three regulator perspectives at once. The model-risk framing (SR 11-7, OCC Bulletin 2026-13) applies where the firm's model risk programme treats the agent as in scope, which it should for any agent making consequential decisions. The cyber framing (NYDFS Part 500, the October 2024 AI Industry Letter, SEC 8-K Item 1.05, FFIEC IT Handbook, the 36-hour banking computer-security incident notification rule, state Insurance Data Security Model Law) carries binding supervisory expectation in their respective scopes. The human-oversight framing (EU AI Act Article 14 for in-scope deployments, sector consumer-protection regimes, fair-claims-settlement standards in insurance) sets the bar for what "human in the loop" has to mean in practice. The AI-specific practitioner framings (NIST AI 600-1, OWASP LLM Top 10, MITRE ATLAS, NCSC AI guidance) are leading practice; they are not, in themselves, binding regulation. Be explicit about which scopes are in play in any individual review.

## Primary anchors

### 1. NIST AI Risk Management Framework 1.0

- Citation: NIST AI 100-1, "Artificial Intelligence Risk Management Framework (AI RMF 1.0)" (January 2023), Govern function (especially Govern 1.x organisational policies, Govern 4.x accountability and roles, Govern 6.x third-party considerations) and Manage function (especially Manage 1.x risk identification and prioritisation, Manage 2.x risk treatment, Manage 4.x deployment, monitoring, and incident response).
- Excerpt-paraphrase: The AI RMF organises AI risk management around four functions (Govern, Map, Measure, Manage) with subcategories that map to lifecycle activities. For agentic deployments the Govern subcategories on accountability, roles, and policies set the organisational scaffold; Manage 4.x (deployment monitoring, incident handling, recovery and decommissioning) sets the operational expectations the agentic-controls review surfaces. The framework is voluntary and process-focused; it does not prescribe specific controls.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — AI RMF 1.0, Govern and Manage function sections [verify subcategory numbering]
- Notes: Voluntary, not binding. The leading-practice anchor most second-line AI governance functions cite for the organisational scaffold.

### 2. NIST AI 600-1 — Generative AI Profile

- Citation: NIST AI 600-1, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (July 2024), Manage and Measure subcategories on prompt-injection mitigation (Manage 2.7), downstream-impact management (Manage 2.8), incident handling (Manage 4.1), and third-party considerations under Govern [verify exact subcategory numbering].
- Excerpt-paraphrase: The Generative AI Profile extends the NIST AI RMF for GenAI-specific concerns, including agentic configurations. Manage 2.7 names prompt injection as a recurring risk class with mitigation expectations; Manage 2.8 covers downstream impact when GenAI outputs feed into deployed systems (which is exactly the agentic case where outputs become tool-call arguments); Manage 4.1 covers incident handling. Govern subcategories address foundation-model dependence as a third-party-risk concern with implications for the firm's ability to monitor for upstream changes that affect agent behaviour.
- Link: https://www.nist.gov/itl/ai-risk-management-framework — Generative AI Profile (NIST AI 600-1), Manage and Measure section [verify subcategory numbering]
- Notes: Voluntary, not binding. The leading-practice anchor for the GenAI-specific risk classes including the agentic seam.

### 3. SR 11-7 / OCC Bulletin 2011-12 — Model Risk Management (applied to agentic AI)

- Citation: Board of Governors of the Federal Reserve System, SR 11-7 / OCC Bulletin 2011-12, "Guidance on Model Risk Management" (April 4, 2011), §IV "Model Validation" (independent review, conceptual soundness, ongoing monitoring, outcomes analysis) and §V "Model Documentation".
- Excerpt-paraphrase: Where the firm's model risk programme treats an agentic AI use case as a model in scope of SR 11-7, the validation expectations apply: independent review of the planner-executor design, conceptual soundness of the tool-selection and authority logic, ongoing monitoring of outcomes (including tool-call patterns and human-oversight effectiveness), and outcomes analysis. SR 11-7 does not name agentic AI by term; the connection is made by interpreting the validation and controls expectations against the agentic configuration. The 2026 interagency revision (OCC Bulletin 2026-13, see anchor 4) refreshes this for AI/ML and agentic configurations explicitly.
- Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm — §IV Model Validation, §V Model Documentation
- Notes: Binding on federally regulated banks. The applicability to agentic AI is a firm-by-firm interpretation; many firms now treat in-scope agentic use cases as models for the purposes of the model risk programme.

### 4. OCC Bulletin 2026-13 — Revised Interagency Model Risk Management Guidance

- Citation: OCC Bulletin 2026-13, "Revised Interagency Guidance on Model Risk Management" (issued 2026 by OCC; FDIC and Federal Reserve parallel issuances expected) [verify section on agentic AI, tool-use, and adversarial robustness].
- Excerpt-paraphrase: The revised guidance refreshes SR 11-7 documentation, validation, and ongoing-monitoring expectations to incorporate AI/ML and generative-AI use cases including foundation-model dependence, retrieval-augmented generation, tool use, and agentic configurations. Adversarial robustness (including prompt injection and tool-misuse for agentic configurations) and human-oversight effectiveness sit within the validation expectations.
- Link: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html — Bulletin 2026-13 [verify section]
- Notes: Confirm published bulletin section numbering at SKILL.md write time and at memo-write time. Until verified, the SKILL.md and the review artifact do not over-claim binding language on agentic-specific expectations from this bulletin.

### 5. EU AI Act — Regulation (EU) 2024/1689, Article 14 (human oversight)

- Citation: Regulation (EU) 2024/1689 of the European Parliament and of the Council on Artificial Intelligence (the AI Act), Article 14 "Human oversight"; supplementary references to Article 9 (risk management system), Article 13 (transparency and provision of information to deployers), and Article 26 (obligations of deployers of high-risk AI systems).
- Excerpt-paraphrase: Article 14 requires high-risk AI systems to be designed and developed such that they can be effectively overseen by natural persons during the period the system is in use. The article specifies that oversight measures must enable persons to understand the relevant capacities and limitations, remain aware of automation bias, correctly interpret outputs, decide not to use or disregard outputs, and intervene or interrupt the system through a "stop" button or similar procedure. For agentic deployments in scope of the AI Act, this is the load-bearing legal anchor for the human-oversight section of the agentic-controls review.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj — Article 14
- Notes: Binding on providers and deployers of high-risk AI systems with EU nexus. Out-of-scope use cases inherit the framing by analogy. The Article 14 four-eyes and stop-button requirements are the bar for "effective oversight" everywhere.

### 6. ISO/IEC 42001:2023 — Artificial Intelligence Management System

- Citation: ISO/IEC 42001:2023 "Information technology — Artificial intelligence — Management system", §8.1 (operational planning and control), §8.2 (AI system impact assessment), §8.3 (AI system lifecycle controls), and Annex A controls relevant to AI security, oversight, and adversarial robustness [verify Annex A control IDs].
- Excerpt-paraphrase: ISO/IEC 42001 sets management-system expectations for AI, including lifecycle controls covering risk assessment, design, deployment, operation, and decommissioning. Annex A controls cover items relevant to agentic AI security (input validation, output controls, monitoring, oversight points, supplier controls) that map to the agentic-controls mitigation set.
- Link: https://www.iso.org/standard/42001 — ISO/IEC 42001:2023 §8.x and Annex A
- Notes: Voluntary / certifiable. Firms pursuing certification use this anchor as the AI management-system frame.

### 7. NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024)

- Citation: New York Department of Financial Services, "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks" (October 16, 2024), [verify section] on AI-enabled threats including prompt injection, data poisoning, social engineering, and the entity's own use of AI.
- Excerpt-paraphrase: Covered entities under 23 NYCRR Part 500 are expected to address AI-related cybersecurity risks within their existing cybersecurity programs. The letter calls out AI-enabled social engineering and deepfakes as external threats, and prompt injection, data poisoning, and model-supply-chain risks as risks arising from the entity's own deployment of AI. For agentic deployments, the letter's framing applies to the agent's serving environment, the tool-invocation surface, and the foundation-model supply chain. Existing Part 500 obligations on risk assessment (§500.9), third-party service-provider security (§500.11), incident response (§500.16), audit-trail (§500.6), and notice to superintendent (§500.17(a)) apply to the agentic surface.
- Link: https://www.dfs.ny.gov/industry-guidance/industry-letters — Industry Letter October 16, 2024 [verify section]
- Notes: Binding for NYDFS-covered entities. For entities outside NYDFS scope, this is industry-practice reference and a directional indicator of where state-cyber supervisors are heading.

### 8. MITRE ATLAS — Adversarial Threat Landscape for AI Systems

- Citation: MITRE ATLAS, the adversarial-threat knowledge base for AI systems (modeled after MITRE ATT&CK), tactics and techniques covering reconnaissance, initial access, ML attack staging, evasion, exfiltration, and impact in AI-system contexts [verify exact technique IDs for agentic-relevant entries including LLM Plugin Compromise and LLM Prompt Injection].
- Excerpt-paraphrase: ATLAS catalogues adversarial tactics and techniques against AI systems with case studies drawn from public incidents and red-team disclosures. Agentic-relevant techniques sit across initial access (LLM Prompt Injection), ML attack staging (LLM Jailbreak), execution (LLM Plugin Compromise, where the term "plugin" maps to the tool-use surface), and impact (External Harms, System Misuse for External Effect). The case studies are useful for grounding likelihood ratings in observed incident patterns rather than abstract assessment.
- Link: https://atlas.mitre.org/ — ATLAS matrix, case studies section [verify technique IDs at SKILL.md write time]
- Notes: Industry-practice reference. The most widely used adversarial-threat taxonomy in AI red-teaming and the cyber-team-friendly framing of the agentic threat surface.

### 9. OWASP Top 10 for Large Language Model Applications

- Citation: OWASP Top 10 for LLM Applications [verify edition; v1.1 published 2023, v2.0 in development as of 2025], with particular relevance for agentic systems on LLM01 Prompt Injection (direct and indirect), LLM02 Insecure Output Handling, LLM06 Sensitive Information Disclosure, LLM07 Insecure Plugin / Tool Design, LLM08 Excessive Agency.
- Excerpt-paraphrase: LLM07 (Insecure Plugin / Tool Design) and LLM08 (Excessive Agency) are the two entries that bite hardest for agentic systems. LLM07 covers tool-design weaknesses that magnify injection impact (broad permissions, weak input validation, unauthenticated tool calls). LLM08 covers excessive agency, where the LLM has authority to take consequential actions and where the per-action guardrails do not catch the chained-action outcome (the canonical agentic failure mode). LLM01 and LLM02 carry the prompt-injection and output-handling framings used elsewhere in the review.
- Link: https://owasp.org/www-project-top-10-for-large-language-model-applications/ — Top 10 list, LLM07 and LLM08 sections, current edition [verify version at SKILL.md write time]
- Notes: OWASP is not a regulator. The taxonomy is industry-practice and the vocabulary most commonly used in vendor red-team reports and internal AI-security programmes for agentic systems.

### 10. NCSC Guidelines for Secure AI System Development

- Citation: National Cyber Security Centre (UK) and Cybersecurity and Infrastructure Security Agency (US), "Guidelines for Secure AI System Development" (November 2023) [verify date and section references], joint guidance signed by 18 international cybersecurity agencies.
- Excerpt-paraphrase: The guidelines set secure-by-design expectations across the AI system lifecycle: secure design (threat modelling for AI-specific risks including prompt injection and tool-misuse), secure development (supply-chain considerations for foundation models and components), secure deployment (operational controls for monitoring and incident response), secure operation and maintenance. Prompt injection and untrusted-input handling are named explicitly; the guidance recommends treating model inputs and tool outputs as untrusted by default.
- Link: https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development — NCSC and CISA joint guidelines (November 2023) [verify exact section reference]
- Notes: Industry-practice reference. Not binding; carries weight because of the multi-agency international signatory list.

### 11. SEC Cybersecurity Disclosure Rules — 8-K Item 1.05 and Reg S-K Item 106

- Citation: 17 CFR 229.106 (Reg S-K Item 106, "Cybersecurity"); 17 CFR 249.308 (Form 8-K, Item 1.05, "Material Cybersecurity Incidents") (rules adopted July 26, 2023; effective dates phased).
- Excerpt-paraphrase: Public registrants must disclose material cybersecurity incidents on Form 8-K within four business days of materiality determination (Item 1.05) and must disclose cybersecurity risk management, strategy, and governance annually under Item 106. Where an agentic-AI tool-misuse event causes or contributes to a material cybersecurity incident (data exfiltration, unauthorised actions taken via tool privileges, third-party-service compromise), the 8-K disclosure obligation applies. The agentic-controls review supports the firm's materiality assessment by documenting the threat surface, the residual risk, the kill-switch posture, and the incident-response posture.
- Link: https://www.sec.gov/rules/final/2023/33-11216.pdf — Final Rule, July 2023, Sections II.A.1 (Item 1.05) and II.B.1 (Item 106)
- Notes: Binding on SEC public registrants. The materiality assessment under 8-K Item 1.05 is the registrant's; the agentic-controls review is one input.

### 12. Banking computer-security incident notification rule (12 CFR Part 53 / Part 225 / Part 304)

- Citation: 12 CFR Part 53 (OCC), 12 CFR Part 225 Subpart M (FRB), 12 CFR Part 304 Subpart C (FDIC), "Computer-Security Incident Notification Requirements for Banking Organizations and Their Bank Service Providers" (effective May 1, 2022), with the 36-hour notification requirement for "notification incidents".
- Excerpt-paraphrase: Banking organisations and their bank service providers must notify the primary federal regulator within 36 hours of determining a "notification incident" has occurred (a computer-security incident that has materially disrupted or degraded, or is reasonably likely to materially disrupt or degrade, the banking organisation's ability to deliver services). Agentic-AI tool-misuse events that meet this threshold trigger the rule; the agentic-controls review supports the determination by documenting the kill-switch posture, the blast-radius framing, and the incident classes.
- Link: https://www.federalregister.gov/documents/2021/11/23/2021-25510 — Final Rule November 2021, 36-hour notification section, effective May 2022
- Notes: Binding on bank-affiliated entities and their bank service providers in the US. Distinct from NYDFS §500.17(a) and from SEC 8-K Item 1.05; can trigger concurrently.

### 13. NIST SP 800-53 Rev. 5 — Security and Privacy Controls (referenced for agentic control mapping)

- Citation: NIST Special Publication 800-53 Rev. 5, "Security and Privacy Controls for Information Systems and Organizations" (September 2020), control families AC (Access Control), AU (Audit and Accountability), IR (Incident Response), SI (System and Information Integrity), SR (Supply Chain Risk Management), SC (System and Communications Protection).
- Excerpt-paraphrase: SP 800-53 is the federal control catalogue. It is referenced in this skill not as a primary AI anchor but as the underlying control framework for the cyber-side mitigations an agentic-controls review records: identity and access controls on the agent's service account (AC family), audit logging of agent invocations, tool calls, and oversight events (AU family), incident-response procedures including kill-switch and rollback (IR family), input validation and output filtering as system-integrity controls (SI family), foundation-model and tool-supply-chain controls (SR family), sandbox and execution-environment controls (SC family).
- Link: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final — NIST SP 800-53 Rev. 5, control-family sections AC, AU, IR, SI, SR, SC
- Notes: SP 800-53 is binding for federal information systems; for FS firms it is informational and is the cyber team's vocabulary for control mapping.

### 14. SEC Rule 15c3-5 — Market Access Rule

- Citation: 17 CFR 240.15c3-5, "Risk Management Controls for Brokers or Dealers with Market Access" (Rule 15c3-5).
- Excerpt-paraphrase: Brokers or dealers with market access (or providing market access to others) must implement risk-management controls and supervisory procedures reasonably designed to manage the financial, regulatory, and other risks of market access activity. Pre-trade controls include credit and capital thresholds, erroneous-order prevention, regulatory-compliance checks; post-trade controls include surveillance and immediate access to a "kill switch". For any agentic AI with order-routing, position-actioning, or order-management interaction, Rule 15c3-5 is the load-bearing capital-markets anchor.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.15c3-5 — 17 CFR §240.15c3-5
- Notes: Capital-markets sector overlay anchor. Binding on broker-dealers with market access.

## Sector and other secondary anchors

### 15. NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)

- Citation: National Association of Insurance Commissioners, "Model Bulletin: Use of Artificial Intelligence Systems by Insurers" (adopted December 4, 2023), AIS Program elements covering governance, risk management, testing and validation, third-party AI accountability, monitoring, and documentation.
- Excerpt-paraphrase: Insurers using AI systems are expected to adopt and implement an AIS Program addressing the named elements. For agentic deployments in claims handling, FNOL intake, agent / producer co-pilot, and policyholder-facing actuation, AIS Program element-by-element coverage applies; the carrier remains accountable for vendor-supplied AI used on its policies. Adversarial-robustness considerations including tool-misuse sit within testing and validation; documentation expectations apply.
- Link: https://content.naic.org/sites/default/files/inline-files/2023-12-4%20Model%20Bulletin_Adopted_0.pdf — Model Bulletin and AIS Program elements
- Notes: Insurance sector overlay anchor. NAIC Bulletin is a model bulletin; binding only to the extent state DOIs adopt it. The state-adoption tracker maintained by the NAIC AI Working Group is the public reference for binding-status confirmation per jurisdiction.

### 16. NAIC Unfair Trade Practices Act (Model #880) and state Unfair Claims Settlement Practices Acts

- Citation: NAIC Unfair Trade Practices Act, Model Regulation #880, including the unfair-claims-settlement provisions adopted by most states as a state Unfair Claims Settlement Practices Act (UCSPA) [verify model-act section numbering and per-state adoption].
- Excerpt-paraphrase: The Unfair Trade Practices Act and state UCSPAs set the fair-claims-settlement standards governing acknowledgment timing, investigation reasonableness, prompt and reasoned denial, communication, and documentation. The standards apply regardless of who or what produces the claims decision. An agentic claims-AI system cannot move the standard; the controls review must record how the agent and its human-oversight design satisfy the named requirements (acknowledgment within state-defined timing, reasoned-denial drafting reviewable by a human, complaint flow, supervisor-override path, audit trail, denial-letter human review).
- Link: https://content.naic.org/cipr-topics/unfair-trade-practices — NAIC Unfair Trade Practices Act resources [verify model-act section numbering]
- Notes: Insurance sector overlay anchor (claims-AI overlay specifically). Binding via state adoption; the per-state UCSPA is the operative regulation in each jurisdiction.

### 17. NAIC Insurance Data Security Model Law (Model #668)

- Citation: NAIC Insurance Data Security Model Law, Model Regulation #668, §4 information security program requirements including §4.F third-party service-provider obligations.
- Excerpt-paraphrase: Insurers and their licensees must maintain an information security program; §4.F requires due diligence on third-party service providers, written contractual obligations on data security, and ongoing monitoring. Where a TPA, claims administrator, or other vendor runs an agentic system on the carrier's policies, the §4.F obligations attach; the carrier remains accountable.
- Link: https://content.naic.org/sites/default/files/inline-files/MDL-668.pdf — Model #668 §4.F
- Notes: Insurance overlay anchor. Adoption is state-by-state; the NAIC adoption tracker is the per-state reference.

### 18. NYDFS Insurance Circular Letter on AI / ECDIS in Insurance Underwriting and Pricing (January 2024)

- Citation: New York Department of Financial Services, "Use of Artificial Intelligence Systems and External Consumer Data and Information Sources in Insurance Underwriting and Pricing", Insurance Circular Letter No. 7 (January 17, 2024) [verify circular-letter number].
- Excerpt-paraphrase: NY-licensed insurers using AI systems and external consumer data and information sources (ECDIS) in life-insurance underwriting and pricing must implement governance, risk management, testing, fairness assessment, transparency, disclosure, and consumer-recourse processes per the letter. For agentic systems in NY-licensed life-carrier underwriting scope, the letter's expectations apply; the agentic-controls review references this anchor when the engagement scope places it in.
- Link: https://www.dfs.ny.gov/industry-guidance/circular-letters — Insurance Circular Letter 2024-7 [verify section] and circular-letter number
- Notes: Insurance overlay anchor for NY-licensed life carriers. Binding within scope.

### 19. Colorado Division of Insurance regulation implementing SB 21-169

- Citation: Colorado Division of Insurance, "Governance and Risk Management Framework Requirements for Life Insurers' Use of External Consumer Data and Information Sources, Algorithms, and Predictive Models", Regulation 10-1-1 (effective November 14, 2023) [verify regulation number].
- Excerpt-paraphrase: Life insurers operating in Colorado must implement a documented governance and risk-management framework for the use of ECDIS, algorithms, and predictive models, including testing for unfair discrimination, consumer disclosure, and consumer-recourse processes. For agentic systems in CO life-carrier underwriting scope, the regulation applies; the controls review references this anchor when the engagement scope places it in.
- Link: https://doi.colorado.gov/announcements/colorado-division-of-insurance-final-adopted-algorithm-and-predictive-model-governance — final adopted regulation [verify section] and regulation number
- Notes: Insurance overlay anchor for CO life carriers. Binding within scope.

### 20. HIPAA Privacy Rule and Security Rule

- Citation: HIPAA Privacy Rule (45 CFR Part 164 Subparts A and E), HIPAA Security Rule (45 CFR Part 164 Subpart C), Breach Notification Rule (45 CFR §§164.400-414).
- Excerpt-paraphrase: Covered entities and business associates handling protected health information must comply with the Privacy Rule (use and disclosure rules, minimum-necessary, individual rights), the Security Rule (administrative, physical, technical safeguards), and the Breach Notification Rule (notification to individuals, HHS, and in some cases the media following discovery of a breach of unsecured PHI). For agentic systems in health-claims AI, life-and-health underwriting AI using prescription-history or medical data, or any other PHI-touching flow, HIPAA applies to the agent and to its vendor.
- Link: https://www.hhs.gov/hipaa/for-professionals/privacy/index.html and https://www.hhs.gov/hipaa/for-professionals/security/index.html — HIPAA Privacy Rule sections (45 CFR Part 164 Subparts A and E) and Security Rule sections (45 CFR Part 164 Subpart C)
- Notes: Insurance and healthcare-finance overlay anchor. Binding on covered entities and business associates.

### 21. FFIEC IT Examination Handbook — Information Security and AIO booklets

- Citation: FFIEC Information Technology Examination Handbook, Information Security booklet (current edition) and Architecture, Infrastructure, and Operations booklet (June 2021), sections on application security, third-party risk, change management, and operations [verify section reference for agentic-system-specific guidance].
- Excerpt-paraphrase: The FFIEC IT Handbook sets supervisory expectations for IT and information security at federally supervised financial institutions. The handbook does not yet have AI-specific sections in all booklets; agentic systems are examined under the existing application-security, third-party-risk, change-management, and operations framings. Tool-use, identity, and external-system actuation are examined under existing framings.
- Link: https://ithandbook.ffiec.gov — Information Security booklet and AIO booklet [verify section]
- Notes: Banking sector overlay anchor.

### 22. Joint OCC, FRB, and FDIC Interagency Guidance on Third-Party Relationships (June 6, 2023)

- Citation: OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, "Interagency Guidance on Third-Party Relationships: Risk Management" (issued June 6, 2023).
- Excerpt-paraphrase: The interagency guidance sets risk-management expectations for banking organisations engaging third parties, including AI vendors and foundation-model providers. For agentic systems built on or integrated with vendor-supplied components, the third-party risk-management lifecycle applies: due diligence, contracting (notice and audit rights for adversarial-robustness testing and tool-design changes), ongoing monitoring (vendor change-of-version notice, tool-inventory changes).
- Link: https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-17.html — Bulletin 2023-17, Risk Management Life Cycle sections
- Notes: Banking and payments-fintech sector overlay anchor.

### 23. FINRA Rule 3110 — Supervision

- Citation: FINRA Rule 3110, "Supervision".
- Excerpt-paraphrase: Member firms must establish and maintain a system to supervise the activities of each associated person that is reasonably designed to achieve compliance with applicable securities laws and regulations and FINRA rules. For agentic systems used in capital-markets workflows (research, surveillance assistance, advisor co-pilots, order-management actuation), Rule 3110 supervisory expectations apply; the human-oversight design must reflect the supervisory bar.
- Link: https://www.finra.org/rules-guidance/rulebooks/finra-rules/3110 — FINRA Rule 3110
- Notes: Capital-markets sector overlay anchor. Binding on FINRA member firms.

### 24. SEC Investment Advisers Act Rule 206(4)-1 (Marketing Rule)

- Citation: 17 CFR 275.206(4)-1, Investment Adviser Marketing Rule.
- Excerpt-paraphrase: AI-generated client-facing content from a registered investment adviser is subject to the Marketing Rule's general prohibitions and books-and-records preservation. An agentic system that drafts or sends client communications without effective human oversight creates Marketing Rule exposure; the controls review captures the oversight design and the books-and-records integration.
- Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 — 17 CFR §275.206(4)-1
- Notes: Capital-markets sector overlay anchor.

### 25. CFPB UDAAP framings and Consumer Financial Protection Act §1031 / §1036

- Citation: Consumer Financial Protection Act of 2010 §§1031 and 1036 (12 USC §§5531 and 5536), prohibiting unfair, deceptive, or abusive acts or practices in connection with consumer financial products or services.
- Excerpt-paraphrase: For agentic systems with customer-facing actuation in consumer-financial contexts (consumer-banking, consumer-lending, deposit servicing, payments to consumers), CFPB UDAAP framings apply to the agent's outputs and actions. The controls review captures the conduct-overlay seam: complaint-rate and complaint-code drift as conduct signals, customer-impact escalation triggers, customer-recourse posture.
- Link: https://www.consumerfinance.gov/compliance/supervisory-guidance/ — CFPB UDAAP guidance, supervisory bulletin section [verify section]
- Notes: Consumer-finance overlay anchor. Loaded via the conduct cross-cutting overlay.

### 26. GLBA Safeguards Rule (16 CFR Part 314)

- Citation: 16 CFR Part 314, FTC Standards for Safeguarding Customer Information (Safeguards Rule), as amended December 2021, with notification provisions added October 2023 effective May 2024 (16 CFR §314.5(d)).
- Excerpt-paraphrase: Financial institutions in scope of the Safeguards Rule must implement an information security program and, since May 2024, must notify the FTC of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers. An agentic-AI tool-misuse event involving customer NPI may meet the notification threshold.
- Link: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 — 16 CFR §314.5(d)
- Notes: Privacy cross-cutting overlay anchor; relevant for non-bank financial institutions in FTC scope.

### 27. Public foundation-model provider system cards (form-factor reference)

- Citation: Anthropic, OpenAI, Google, and Meta system and model cards covering safety evaluations including tool-use, agentic-configuration, and excessive-agency testing where described. Examples include Anthropic Claude system cards (which discuss agentic safety), OpenAI GPT-4 and o-series system cards, Google Gemini model cards, Meta Llama responsible-use guides.
- Excerpt-paraphrase: Foundation-model provider system cards describe the vendor's adversarial-testing approach, including (where covered) tool-use evaluations and agentic configurations. They are vendor self-attestation; they do not test the firm's tool inventory, the firm's authority logic, or the firm's oversight design.
- Link: https://www.anthropic.com/news/claude-system-card and https://openai.com/safety — vendor system-card pattern reference, evaluation section and limitations section
- Notes: Form-factor reference only. Vendor results land in the review at vendor-self-attestation confidence and never substitute for firm-side testing of the deployed agent.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at SKILL.md write time and at memo-write time:

- NIST AI 600-1 — confirm exact Manage and Measure subcategory numbering for the Manage 2.7, 2.8, 4.1 references.
- OCC Bulletin 2026-13 — confirm published section numbering on agentic AI, tool-use, and adversarial robustness.
- FDIC and Federal Reserve parallel issuances to OCC Bulletin 2026-13 — confirm number and section.
- NYDFS Industry Letter on AI cybersecurity (October 2024) — confirm exact section reference for the prompt-injection and tool-use passages.
- ISO/IEC 42001:2023 — confirm Annex A control IDs relevant to agentic-AI controls including oversight, supplier, and AI-system-specific entries.
- MITRE ATLAS — confirm exact technique IDs for the agentic-relevant entries including LLM Plugin Compromise, LLM Prompt Injection, and any newly added agentic technique entries.
- OWASP Top 10 for LLM Applications — confirm current edition (v1.1 vs v2.0 etc.) and the exact LLM07 / LLM08 framing at write time.
- NCSC Guidelines for Secure AI System Development — confirm exact section reference for the tool-use and untrusted-input guidance.
- FFIEC IT Examination Handbook — confirm section reference for AI-system-specific guidance where it exists.
- NAIC #880 — confirm current section numbering for the unfair-claims-settlement provisions.
- NAIC Insurance Data Security Model Law (Model #668) — confirm §4.F numbering and current text.
- NYDFS Insurance Circular Letter (January 2024) — confirm circular-letter number.
- Colorado SB 21-169 implementing regulation — confirm regulation number (Regulation 10-1-1 or current).
- State Insurance Data Security Model Law adoption per state — verify per-state adoption status against the NAIC adoption tracker.
- 12 CFR Part 53 / Part 225 / Part 304 — confirm the current 36-hour banking computer-security incident notification rule sections.

Where verification is incomplete, the SKILL.md cites with the `[verify section]` flag carried forward; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy, and named owners via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. An advisory firm shipping a client-specific overlay does the same thing under a separate overlay file.
