# Source anchors: ai-act-triage

Cited regulatory sources this skill anchors to. Every primary anchor names the source, the section reference (or `[verify section]` flag), a one-paragraph excerpt or paraphrase of the relevant content, and the link.

The skill cites these by file path. SKILL.md does not restate excerpts.

## Primary anchors

### 1. EU AI Act — Regulation (EU) 2024/1689

- Citation: Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence and amending Regulations (EC) No 300/2008, (EU) No 167/2013, (EU) No 168/2013, (EU) 2018/858, (EU) 2018/1139 and (EU) 2019/2144 and Directives 2014/90/EU, (EU) 2016/797 and (EU) 2020/1828 (Artificial Intelligence Act). Published in the Official Journal of the European Union on 12 July 2024.
- Excerpt-paraphrase: The Regulation lays down harmonised rules on the placing on the market, putting into service, and use of AI systems in the Union; prohibitions on certain AI practices; specific requirements for high-risk AI systems and obligations for operators of those systems; harmonised transparency rules for certain AI systems; rules on the placing on the market of general-purpose AI models; rules on market monitoring, market surveillance, governance, and enforcement; and measures to support innovation. The Regulation is the operative source for every section anchor below.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj section: full text including all Articles and Annexes
- Notes: Citations below reference articles, annexes, and recitals from this Regulation. The published consolidated text in the Official Journal is the authoritative version.

### 2. AI Act Article 3 — Definitions

- Citation: Regulation (EU) 2024/1689, Article 3 "Definitions".
- Excerpt-paraphrase: Article 3 sets the definitions used across the Regulation, including AI system (Article 3(1)), provider (Article 3(3)), deployer (Article 3(4)), importer (Article 3(6)), distributor (Article 3(7)), authorised representative (Article 3(5)), placing on the market (Article 3(9)), putting into service (Article 3(11)), substantial modification (Article 3(23)), general-purpose AI model (Article 3(63)), general-purpose AI system (Article 3(66)), and biometric categorisation (Article 3(40)). The triage's operator-role determination relies on the Article 3 definitions.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 3)
- Notes: Provider versus deployer distinction is the load-bearing call for in-house-built versus vendor-supplied systems. Article 25 governs flips between roles for substantial modifications.

### 3. AI Act Article 5 — Prohibited AI practices

- Citation: Regulation (EU) 2024/1689, Article 5 "Prohibited AI practices".
- Excerpt-paraphrase: Article 5 prohibits the placing on the market, putting into service, or use of certain AI practices, including: subliminal techniques beyond a person's consciousness or purposefully manipulative or deceptive techniques with the objective or effect of materially distorting behaviour (5(1)(a)); exploitation of vulnerabilities (5(1)(b)); social scoring (5(1)(c)); criminal-offence risk-assessment of natural persons solely based on profiling (5(1)(d)); untargeted scraping of facial images for facial-recognition databases (5(1)(e)); emotion-inference in workplaces or education institutions outside narrow exceptions (5(1)(f)); biometric categorisation by sensitive attributes outside narrow exceptions (5(1)(g)); real-time remote biometric identification in publicly accessible spaces for law-enforcement outside narrow exceptions (5(1)(h)). Article 5 prohibitions apply from 2 February 2025 per Article 113.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 5)
- Notes: The Article 5 screen is run on the record for every triage; each sub-practice is screened individually even where the answer is "does not apply".

### 4. AI Act Article 6 — Classification rules for high-risk AI systems

- Citation: Regulation (EU) 2024/1689, Article 6 "Classification rules for high-risk AI systems".
- Excerpt-paraphrase: Article 6(1) classifies as high-risk an AI system that is intended to be used as a safety component of a product, or is itself a product, covered by Union harmonisation legislation listed in Annex I, where the product is required to undergo a third-party conformity assessment. Article 6(2) classifies as high-risk the AI systems listed in Annex III. Article 6(3) provides a derogation: an AI system referred to in Annex III is not considered high-risk where it does not pose a significant risk of harm to the health, safety, or fundamental rights of natural persons, including by not materially influencing the outcome of decision-making, in any of four narrowly defined situations (narrow procedural task; improving the result of a previously completed human activity; detecting decision-making patterns or deviations without replacing human assessment; preparatory task to an assessment relevant to the use cases listed in Annex III). Article 6(3) does not apply where the AI system performs profiling of natural persons.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 6)
- Notes: The derogation under Article 6(3) is narrow; the triage records the analysis when invoked and routes to legal.

### 5. AI Act Annex I — Union harmonisation legislation

- Citation: Regulation (EU) 2024/1689, Annex I "List of Union harmonisation legislation".
- Excerpt-paraphrase: Annex I lists Union harmonisation legislation referenced in Article 6(1) (Section A, requiring third-party conformity assessment) and other Union harmonisation legislation (Section B). Financial-services products are not in the Annex I lists; the Annex I high-risk route is rarely the route for FS use cases. The triage records the screen running and the typical conclusion (Annex I not invoked).
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 6(1) reference; Annex I list)
- Notes: For FS use cases, Annex III is the operative high-risk route under Article 6(2).

### 6. AI Act Annex III — High-risk AI systems referred to in Article 6(2)

- Citation: Regulation (EU) 2024/1689, Annex III "High-risk AI systems referred to in Article 6(2)".
- Excerpt-paraphrase: Annex III lists the eight categories of high-risk AI systems under Article 6(2): biometrics (point 1); critical infrastructure (point 2); education and vocational training (point 3); employment, workers' management, and access to self-employment (point 4); access to and enjoyment of essential private services and essential public services and benefits (point 5, including 5(a) public-assistance benefits, 5(b) creditworthiness and credit scoring of natural persons with the fraud-detection carve-out, 5(c) life and health insurance risk-assessment and pricing, 5(d) emergency dispatch); law enforcement (point 6); migration, asylum, and border-control management (point 7); administration of justice and democratic processes (point 8). For financial services, the load-bearing rows are 5(b) for credit decisioning and 5(c) for life and health insurance pricing.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj Article 6(2) reference; Annex III list
- Notes: The triage walks every Annex III row on the record and cites the row when applicable.

### 7. AI Act Article 9 — Risk management system

- Citation: Regulation (EU) 2024/1689, Article 9 "Risk management system".
- Excerpt-paraphrase: Providers of high-risk AI systems must establish, implement, document, and maintain a risk management system across the system's lifecycle. The system identifies and analyses known and reasonably foreseeable risks; estimates and evaluates risks that may emerge in intended use and reasonably foreseeable misuse; evaluates risks based on post-market monitoring; and adopts targeted risk-management measures. Risk-management measures include design and development controls, mitigation, and provision of information.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 9)
- Notes: Article 9 is provider-side; deployer-side risk-management is Article 26. The triage records both.

### 8. AI Act Article 10 — Data and data governance

- Citation: Regulation (EU) 2024/1689, Article 10 "Data and data governance".
- Excerpt-paraphrase: Training, validation, and testing data sets used in high-risk AI systems must meet quality criteria including relevant design choices; data collection processes; data preparation operations; assumptions about the information the data is supposed to measure and represent; assessment of availability, quantity, and suitability; examination of possible biases reasonably foreseeable to affect health and safety, fundamental rights, or to lead to prohibited discrimination; appropriate measures to detect, prevent, and mitigate such biases; and identification of relevant data gaps. Where strictly necessary for bias monitoring, special categories of personal data may be processed under appropriate safeguards (Article 10(5)).
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 10)
- Notes: Article 10 reach is broader than the GDPR DPIA reach; the triage records the delta.

### 9. AI Act Article 11 and Annex IV — Technical documentation

- Citation: Regulation (EU) 2024/1689, Article 11 "Technical documentation" and Annex IV "Technical documentation referred to in Article 11(1)".
- Excerpt-paraphrase: Article 11 requires providers of high-risk AI systems to draw up technical documentation before placing the system on the market or putting it into service; the documentation must contain at least the elements set out in Annex IV. Annex IV enumerates: (1) general description of the AI system including intended purpose, version, hardware and software; (2) detailed description including methodology, training data, validation and testing, capabilities and limitations, foreseeable unintended outcomes; (3) detailed information about monitoring, functioning, and control; (4) description of the appropriateness of the performance metrics; (5) detailed description of the risk management system; (6) description of relevant changes; (7) list of harmonised standards applied; (8) declaration of conformity; (9) detailed description of the post-market monitoring plan.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 11 and Annex IV)
- Notes: The firm-side model card produced by `model-card-builder` overlaps with Annex IV but does not by itself satisfy the Annex IV obligation; the triage records the deltas.

### 10. AI Act Article 13 — Transparency and provision of information to deployers

- Citation: Regulation (EU) 2024/1689, Article 13 "Transparency and provision of information to deployers".
- Excerpt-paraphrase: Providers of high-risk AI systems must design and develop the systems so that their operation is sufficiently transparent to enable deployers to interpret outputs and use them appropriately. Instructions for use must accompany the system, including the provider's identity; characteristics, capabilities, and limitations; performance metrics including accuracy, robustness, and cybersecurity; foreseeable circumstances that may lead to risks; technical capabilities relevant to outputs; specifications for input data; and human-oversight measures.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 13)
- Notes: Article 13 is provider-side; the triage records the obligation when the firm is the provider.

### 11. AI Act Article 14 — Human oversight

- Citation: Regulation (EU) 2024/1689, Article 14 "Human oversight".
- Excerpt-paraphrase: High-risk AI systems must be designed and developed in such a way that they can be effectively overseen by natural persons during the period in which the AI system is in use. Human oversight measures must enable the natural persons to understand the relevant capacities and limitations; remain aware of automation bias; correctly interpret the output; decide not to use the system or otherwise disregard, override, or reverse the output; and intervene in the operation or interrupt the system through a stop button or similar.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 14)
- Notes: Article 14 is provider-design; deployer-operation of the oversight is Article 26. The triage records both halves.

### 12. AI Act Article 15 — Accuracy, robustness, and cybersecurity

- Citation: Regulation (EU) 2024/1689, Article 15 "Accuracy, robustness, and cybersecurity".
- Excerpt-paraphrase: High-risk AI systems must be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle. Levels of accuracy and the relevant accuracy metrics are declared in the instructions for use. Resilience addresses errors, faults, and inconsistencies that may occur in the system itself or in the environment, including through redundancy and fail-safe plans. Cybersecurity addresses attacks attempting to alter use, outputs, or performance, including through measures to prevent, detect, respond to, resolve, and control attacks.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 15)
- Notes: Article 15 cybersecurity reach interacts with NIS2 (Directive (EU) 2022/2555) and DORA (Regulation (EU) 2022/2554) for financial entities; cross-link to `cyber.md` overlay.

### 13. AI Act Article 22 — Authorised representative

- Citation: Regulation (EU) 2024/1689, Article 22 "Authorised representatives of providers of high-risk AI systems".
- Excerpt-paraphrase: Providers established in third countries must, prior to making their AI systems available on the Union market, appoint by written mandate an authorised representative established in the Union. The authorised representative performs tasks specified in the mandate received from the provider, including verifying that the provider has drawn up the EU declaration of conformity and the technical documentation, keeping at the disposal of competent authorities the documentation, and cooperating with competent authorities. Article 22 reaches third-country providers regardless of EU establishment.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 22)
- Notes: Load-bearing for US firms providing high-risk AI systems used in the EU without an EU establishment.

### 14. AI Act Article 25 — Responsibilities along the AI value chain

- Citation: Regulation (EU) 2024/1689, Article 25 "Responsibilities along the AI value chain".
- Excerpt-paraphrase: Any distributor, importer, deployer, or other third party becomes a provider of a high-risk AI system and is subject to provider obligations under Article 16 in any of the following circumstances: (a) they put their name or trademark on a high-risk AI system already placed on the market; (b) they make a substantial modification to a high-risk AI system already placed on the market in such a way that it remains a high-risk AI system; (c) they modify the intended purpose of an AI system, including a general-purpose AI system, that has not been classified as high-risk in such a way that the AI system concerned becomes a high-risk AI system. The original provider is no longer considered the provider for the purposes of the Regulation in those circumstances.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 25)
- Notes: Article 25 governs flips into provider role for fine-tuning and substantial modification. Common in firm-side adaptation of vendor LLMs.

### 15. AI Act Article 26 — Obligations of deployers of high-risk AI systems

- Citation: Regulation (EU) 2024/1689, Article 26 "Obligations of deployers of high-risk AI systems".
- Excerpt-paraphrase: Deployers of high-risk AI systems must take appropriate technical and organisational measures to ensure they use such systems in accordance with the instructions for use; assign human oversight to natural persons with the necessary competence, training, and authority; ensure input data is relevant and sufficiently representative; monitor operation; keep automatically generated logs for at least six months; inform the provider, distributor, or relevant market surveillance authority where they have reasons to consider use leads to a risk; comply with registration obligations under Article 49; carry out fundamental rights impact assessment under Article 27 where applicable; cooperate with competent authorities.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 26)
- Notes: Deployer obligations are substantive even where the firm is not the provider. Common pitfall: assuming "the vendor handles it".

### 16. AI Act Article 27 — Fundamental rights impact assessment

- Citation: Regulation (EU) 2024/1689, Article 27 "Fundamental rights impact assessment for high-risk AI systems".
- Excerpt-paraphrase: Before deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in critical infrastructure, deployers that are bodies governed by public law or are private entities providing public services (Article 27(1)(a)), and deployers of high-risk AI systems referred to in Annex III(5)(b) (creditworthiness) and Annex III(5)(c) (life and health insurance) (Article 27(1)(b)), must perform a fundamental rights impact assessment. The assessment includes a description of the deployer's processes; the period of time and frequency; the categories of natural persons and groups likely to be affected; the specific risks of harm; the measures to be taken upon materialisation of those risks; the governance arrangements including human oversight; and the complaints-handling arrangements.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 27)
- Notes: FRIA is in addition to the GDPR DPIA, not in lieu of. The triage carries the FRIA-vs-DPIA reconciliation note.

### 17. AI Act Article 49 — Registration

- Citation: Regulation (EU) 2024/1689, Article 49 "Registration" and Annex VIII "Information to be submitted upon the registration of high-risk AI systems".
- Excerpt-paraphrase: Before placing on the market or putting into service a high-risk AI system listed in Annex III (other than Annex III(2) critical infrastructure), the provider or, where applicable, the authorised representative, must register themselves and their system in the EU database referred to in Article 71. Deployers that are public authorities or Union institutions, bodies, offices, or agencies, or persons acting on their behalf, must also register the use. Annex VIII enumerates the registration content.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 49 and Annex VIII)
- Notes: Registration is a pre-deployment gate for high-risk systems.

### 18. AI Act Article 50 — Transparency obligations

- Citation: Regulation (EU) 2024/1689, Article 50 "Transparency obligations for providers and deployers of certain AI systems".
- Excerpt-paraphrase: Article 50(1): providers must ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed they are interacting with an AI system, unless this is obvious from the circumstances. Article 50(2): providers of AI systems generating synthetic audio, image, video, or text content must ensure outputs are marked in a machine-readable format and detectable as artificially generated or manipulated. Article 50(3): deployers of an emotion-recognition system or biometric-categorisation system must inform natural persons exposed thereto of the operation; deployers of deepfake AI systems must disclose the artificial generation. Article 50(4): deployers of an AI system that generates or manipulates text published with the purpose of informing the public on matters of public interest must disclose the artificial generation. Article 50(5): exemptions for law-enforcement and certain artistic uses.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 50)
- Notes: The triage screens each sub-obligation individually. Common landing zone for client-facing GenAI.

### 19. AI Act Articles 51 to 55 — General-purpose AI models

- Citation: Regulation (EU) 2024/1689, Articles 51 "Classification rules for general-purpose AI models", 52 "Procedure", 53 "Obligations for providers of general-purpose AI models", 54 "Authorised representatives of providers of general-purpose AI models", 55 "Obligations for providers of general-purpose AI models with systemic risk".
- Excerpt-paraphrase: Article 51 classifies a general-purpose AI model as having systemic risk where it has high-impact capabilities (presumed where the cumulative training compute exceeds 10^25 FLOPs) or where the Commission designates it. Article 53 obligations on providers of GPAI models include drawing up and keeping up to date technical documentation; making available information and documentation to providers of AI systems intending to integrate the model; putting in place a policy to comply with Union copyright law; drawing up and making publicly available a sufficiently detailed summary of the content used for training. Article 55 obligations for systemic-risk GPAI add model evaluation including adversarial testing; assessment and mitigation of systemic risks; serious-incident reporting; adequate cybersecurity protection.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Articles 51 to 55)
- Notes: GPAI obligations attach to the model provider, not to the deployer. Article 53(1)(d) public summary of training content and Article 53(1)(c) Union copyright policy are deployer-side evidence asks for vendor-LLM-backed deployments.

### 20. AI Act Article 70 — Designation of national competent authorities

- Citation: Regulation (EU) 2024/1689, Article 70 "Designation of national competent authorities and single points of contact".
- Excerpt-paraphrase: Each member state must establish or designate at least one notifying authority and at least one market surveillance authority for the purposes of this Regulation. Member states must designate a single point of contact. The competent authorities must exercise their powers independently, impartially, and without bias. Member-state designation is published and notified to the Commission and the AI Office.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 70)
- Notes: Member-state designation status is consulted at write time; the triage records the named NCA in the operating member state.

### 21. AI Act Article 71 — EU database for high-risk AI systems

- Citation: Regulation (EU) 2024/1689, Article 71 "EU database for high-risk AI systems listed in Annex III".
- Excerpt-paraphrase: The Commission, in collaboration with member states, sets up and maintains an EU database containing the information referred to in Annex VIII for the high-risk AI systems referred to in Article 49. The database is publicly accessible, except for the data referred to in Annex VIII Sections C and D.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 71)
- Notes: Registration into the EU database is the operational artifact for the Article 49 obligation.

### 22. AI Act Article 113 — Entry into force and application

- Citation: Regulation (EU) 2024/1689, Article 113 "Entry into force".
- Excerpt-paraphrase: The Regulation entered into force on 1 August 2024. It applies from 2 August 2026, with the following exceptions: Chapters I (general provisions) and II (prohibited AI practices) apply from 2 February 2025; Chapter III Section 4 (notifying authorities and notified bodies), Chapter V (general-purpose AI models), Chapter VII (governance), Chapter XII (penalties) excluding Article 101 (penalties on providers of general-purpose AI models), and Article 78 (confidentiality) apply from 2 August 2025; Article 6(1) (high-risk classification under Annex I product-safety route) and the corresponding obligations apply from 2 August 2027.
- Link: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Article 113)
- Notes: The triage's `applicable_date` field cites Article 113. Common landmarks: prohibited practices 2 February 2025; GPAI provider obligations 2 August 2025; Annex III high-risk and Article 50 transparency 2 August 2026; Annex I product-safety high-risk 2 August 2027.

## Secondary anchors (governance and soft law)

### 23. EU AI Office Code of Practice on General-Purpose AI

- Citation: European AI Office, Code of Practice for general-purpose AI models (final version published; see AI Office publication for date and version).
- Excerpt-paraphrase: The Code of Practice is a voluntary instrument facilitating compliance with Article 53 obligations for providers of general-purpose AI models. Signatories commit to specific technical documentation practices, training-content summary practices, and copyright-policy practices. Signature does not displace the underlying obligations under Article 53. Adherence to the Code is a means of demonstrating compliance with the obligations covered by the Code.
- Link: https://digital-strategy.ec.europa.eu/en/policies/ai-code-practice (Code of Practice publication, [verify section])
- Notes: Soft-law reference; the triage records vendor signature status as deployer-side evidence-quality signal. Vendor signature is not a binding compliance attestation.

### 24. EU AI Office Q&A and guidelines

- Citation: European AI Office, Q&A documents and guidelines published from 2024 onwards covering Article 5 prohibitions, Article 6 high-risk classification interpretation, Article 50 transparency, and GPAI-related questions.
- Excerpt-paraphrase: AI Office guidance documents provide non-binding interpretive material on the Regulation's application. Guidance is updated as the AI Office develops its supervisory practice and as member-state implementations come into force.
- Link: https://digital-strategy.ec.europa.eu/en/policies/european-ai-office (AI Office publications, [verify section])
- Notes: Soft-law reference; the triage records guidance citations with the soft-law label and does not collapse them with Regulation citations.

### 25. European Commission AI Pact

- Citation: European Commission, AI Pact, voluntary commitments by industry to begin compliance with the AI Act ahead of phasing dates.
- Excerpt-paraphrase: The AI Pact is a voluntary initiative encouraging providers and deployers to begin implementing AI Act obligations before they apply. Pact participants commit to specific actions including AI governance establishment, identification of high-risk systems, and human-oversight implementation.
- Link: https://digital-strategy.ec.europa.eu/en/policies/ai-pact (AI Pact publication, [verify section])
- Notes: Soft-law reference; participation is recorded for context but does not change the Regulation's binding application.

## Member-state implementation anchors (designation and transposition)

### 26. Member-state competent-authority designations under Article 70

- Citation: Member-state designations of notifying authorities, market surveillance authorities, and single points of contact under AI Act Article 70 [verify designation status per member state at write time].
- Excerpt-paraphrase: Each EU member state designates at least one notifying authority and at least one market surveillance authority for the AI Act. For financial services, member states have variously designated existing financial-supervisor authorities, data-protection authorities, or new dedicated AI authorities. Designation status varies by member state and is published nationally.
- Link: Per member state. Aggregate tracker [verify URL] and individual member-state publications.
- Notes: The triage names the NCA in the operating member state and records the prudential-supervisor coordination posture where designation is split.

### 27. Member-state implementing laws and secondary instruments

- Citation: Member-state implementing measures supplementing the directly applicable Regulation, including administrative-procedure provisions, penalty regimes (within the Article 99 framework), and competent-authority procedural rules [verify per member state at write time].
- Excerpt-paraphrase: Although the AI Act is a directly applicable Regulation, member states adopt implementing measures on procedural elements, penalty calibration within the Article 99 framework, and competent-authority operational rules. Implementation status varies; the triage cites the relevant member-state instrument when the scope names a state of operation.
- Link: Per member state. National official-journals and competent-authority publications.
- Notes: The triage does not assert a member-state-specific obligation without confirming implementation status.

## Verification flags

The following items carry `[verify section]` or `[verify ...]` flags and must be confirmed at write time:

- AI Office Code of Practice on General-Purpose AI — confirm published version and section numbering.
- AI Office Q&A and guidelines — confirm latest publication dates and section references.
- European Commission AI Pact — confirm current publication and signatory list state.
- Member-state competent-authority designations under Article 70 — confirm status per member state in the operating footprint.
- Member-state implementing laws — confirm transposition status and effective dates per member state in the operating footprint.

Where verification is incomplete, the citation carries the `[verify section]` flag forward; do not invent.

## Firm overlay placeholder

A firm using this skill in production overlays its policy, taxonomy, and named owners via `references/firm-overlay.md` (not committed in this repo). The firm overlay does not modify this source-anchors file. An advisory firm shipping a client-specific overlay does the same thing under a separate overlay file.
