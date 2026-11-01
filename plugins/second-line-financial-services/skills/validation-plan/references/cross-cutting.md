# cross-cutting

One section per topic. Read only the sections the scope calls for.

## cyber

### Cyber cross-cutting overlay for validation-plan

When the scope record flags `cyber` for the model use case, this overlay adds cyber-specific scope items to the validation plan. AI red-teaming and adversarial robustness overlap substantially with cyber red-teaming; this overlay is where that overlap is named so the validator and the CISO function are reading the same testing surface.

Loaded by: `validation-plan/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NYDFS 23 NYCRR Part 500, especially the third-party-risk, incident-response, and incident-notice provisions (Part 500 governs covered entities; the model is in scope when it sits inside a covered entity's information system or is hosted by a third-party service provider).
- NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024), addressing AI-enabled threats and the entity's own use of AI.
- SEC cyber disclosure rules: 8-K Item 1.05 (material cybersecurity incident disclosure) and Reg S-K Item 106 (cybersecurity risk management, strategy, and governance) where the registrant is public.
- FFIEC IT Examination Handbook, Information Security and Cybersecurity sections, applied to the model's serving environment, change controls, and access controls.
- NIST AI 600-1 (Generative AI Profile) cyber-relevant Measure subcategories: prompt injection (direct and indirect), data poisoning, model extraction, evasion, information security.
- EU AI Act Article 15(5) on resilience to attacks (data poisoning, model poisoning, model evasion, confidentiality attacks, model flaws) for high-risk EU AI systems.

#### What changes for cyber-flagged validation plans

##### 1. Conceptual soundness gains a cyber-architecture review

The plan's conceptual-soundness scope adds a cyber-architecture review subsection: input channels (chat, API, batch, retrieval triggers), prompt-injection robustness posture (tested, untested, vendor-tested), model-supply-chain dependence (foundation-model provider, model-hosting environment, model artefact integrity controls), and tool/agent privileges where applicable. For a traditional ML model the subsection is short (serving environment, model-artefact integrity, access controls); for a GenAI model with tool use or agentic behaviour, it is one of the deeper scope items.

##### 2. Data review flags poisoning and extraction exposure

For models trained or fine-tuned on firm data, the data-review scope adds:

- Training-data integrity controls (provenance, change-detection on training corpora) and the residual exposure to data-poisoning where the controls are partial.
- For RAG-using models, the retrieval corpus is itself a cyber-relevant surface (retrieval-corpus injection is a real attack pattern); access controls, content-validation controls, and refresh integrity model are scoped.
- Training-data extraction risk for models exposing memorised training data through outputs.

##### 3. Robustness scope expands to the AI red-team / cyber red-team overlap

The plan's robustness scope is the operative location for AI red-teaming. Attack classes named in the catalogue (each with method, success criterion, owner):

- Direct prompt injection (single-turn, multi-turn).
- Indirect prompt injection (via retrieved content, via uploaded documents, via tool outputs).
- Jailbreak (adversarial prompting against safety guardrails; vendor-supplied test set plus firm-internal red team).
- RAG corpus poisoning (synthetic injection of malicious content into the retrieval corpus, with retrieval-time scoring tests).
- Model extraction (query-based reconstruction of model behaviour or stolen weights via output interrogation).
- Evasion (input perturbation against classifier or detector models).
- Tool misuse (for agentic systems, attempts to invoke tools beyond their intended boundary, including with elevated privileges).
- Goal hijack (for agentic systems, attempts to redirect the agent's objective via prompt or tool output).
- Supply-chain attack (compromised foundation-model artefact, compromised dependency, compromised vendor-hosted endpoint).
- Confidentiality attack (membership inference, training-data extraction, prompt-template extraction).

For each attack class, vendor-supplied results carry vendor-self-attestation confidence; firm-independent red-team results carry higher confidence and are listed separately. Absence of firm-independent testing is itself a plan-recordable item (it goes to source trace as `[evidence needed]` and to effective-challenge questions, not silently into the plan body).

##### 4. Monitoring scope adds cyber-relevant signals

Monitoring entries the cyber overlay expects, each with the six required fields (metric, threshold, frequency, owner, escalation path, revalidation_trigger):

- Authentication and authorisation anomalies on the model's serving endpoint.
- Prompt-injection detection signals (where the firm has a detection layer; if not, the absence is recorded as an effective-challenge question on the gap).
- Output-anomaly detection (sudden shifts in refusal rate, citation patterns, tool-call patterns are leading indicators of compromise as well as drift).
- Vendor change-of-version signals for foundation-model and serving-environment dependencies; an unannounced version swap is both a cyber signal and a model-risk signal, with `revalidation_trigger = true`.
- Tool-invocation rate and pattern monitoring for GenAI with tool or agent privileges; sudden expansion of tool use is an investigation trigger.
- Retrieval-corpus integrity monitoring (for RAG); change-of-content detection on the retrieval corpus.

Cyber-relevant entries typically escalate to the CISO function in addition to the model owner.

##### 5. Effective challenge gains cyber-tagged questions

Cyber-tagged effective-challenge questions probe specific gaps, not the broad cyber posture:

- The agentic system has tool privileges; what is the tool-boundary control and what is the off-switch criterion if tool-invocation rate or pattern shifts beyond baseline.
- The foundation-model is vendor-opaque; what is the firm's evidence base for adversarial robustness that does not depend on vendor self-attestation.
- The retrieval corpus is firm-controlled but the corpus owner is in a different function from the model owner; what is the change-control loop and what does the validator need to see to consider it adequate.
- The prompt-injection detection layer is novel; what is the validator's confidence in detection precision and recall.
- An unannounced foundation-model version swap is both a model-risk and a cyber event; what is the operational test that the version-monitoring control actually fires.

##### 6. Dependencies expand to cyber functions

The plan's dependencies list adds:

- Information-security red-team capacity and scheduling.
- Vendor evidence (system card, evaluation report, red-team summary) reviewed jointly with the cyber function.
- Detection-layer evidence pack from the firm's cyber detection function.
- For NY footprint, NYDFS Part 500 covered-entity self-assessment and the October 2024 industry letter alignment evidence.

#### Cyber-specific output template additions

- `conceptual_soundness.cyber_architecture_review` — subsection covering input channels, prompt-injection posture, supply-chain dependence, tool/agent privileges.
- `robustness_testing[]` — cyber attack classes from the catalogue above, each with method, success criterion, owner.
- `monitoring[]` — cyber-tagged entries (authentication anomalies, prompt-injection detection, output-anomaly detection, vendor change-of-version, tool-invocation patterns, retrieval-corpus integrity), each with CISO-function escalation path.
- `effective_challenge_questions[]` — cyber-tagged (tool-boundary, vendor-opaque robustness evidence, retrieval-corpus change control, detection-layer confidence, version-monitoring operational test).
- `dependencies[]` — info-security red-team capacity, joint vendor-evidence review, detection-layer evidence pack, NYDFS Part 500 self-assessment evidence where applicable.

#### Common pitfalls in cyber-flagged validation plans

- Treating "vendor pen-tested" or vendor-supplied adversarial-test results as evidence the deployed prompt surface is hardened. The firm's prompt template, retrieval corpus, and tool inventory are firm-side surfaces and need firm-side testing.
- Framing prompt-injection only as a quality issue. It is also a control-evasion path when the model has tool or agent privileges.
- Assuming model isolation when the model has tool or agent privileges. Tool privileges are lateral-movement opportunities; the plan's robustness scope includes tool-misuse and goal-hijack tests explicitly.
- Omitting vendor change-of-version monitoring; a silent foundation-model swap is both a model-risk event and a cyber event.
- Treating the cyber overlay as the CISO's plan. The validation plan is the validator's scope contract; the CISO function is a joint-review and escalation audience, not the owner.
- Listing "red team" as a single robustness entry without enumerating attack classes; the catalogue above is what the validator scopes against, and the plan reads test-by-test.
- Treating EU AI Act Article 15(5) as out of scope for US-only operations; for any high-risk EU AI system that touches EU users or markets, Article 15(5) cyber-resilience evidence is part of Annex IV technical documentation.

## privacy

### Privacy cross-cutting overlay for validation-plan

When the scope record flags `privacy` for the model use case, this overlay adds privacy-specific scope items to the validation plan. The validation plan is not the firm's privacy-impact assessment; the PIA is its own artifact under the firm's privacy program. The plan scopes the privacy-relevant tests and evidence the validator needs, and points to the PIA in source trace.

Loaded by: `validation-plan/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- GLBA Safeguards Rule (16 CFR Part 314) for non-public personal information (NPI) handled by financial institutions.
- CCPA / CPRA (California) and the rolling state-privacy roster (VCDPA Virginia, CTDPA Connecticut, and others following the same general structure).
- HIPAA Privacy and Security Rules (45 CFR Parts 160 and 164) where protected health information is in scope (life and health insurance; healthcare-adjacent fintechs; claims AI).
- GDPR Article 22 (decisions based solely on automated processing, including profiling) and the right to obtain meaningful information about the logic involved.
- EU AI Act Article 27 (fundamental rights impact assessment, FRIA) where the model is a high-risk AI system used by a deployer in scope of the obligation.
- ECOA / Reg B right-to-explanation in adverse-action notices for credit-decisioning models, sitting at the intersection of fair-lending and privacy.

#### What changes for privacy-flagged validation plans

##### 1. Data review gains a privacy-classification subsection

Each data source in scope of validation carries a privacy classification: NPI under GLBA, PHI under HIPAA, PCI cardholder data, customer-supplied prompts, public, confidential. For foundation-model training data, firm visibility is typically limited to vendor system-card statements; record at vendor-self-attestation confidence and do not extend vendor claims to cover the firm's deployed prompt surface (the most common error).

A specific subsection covers the prompt surface for GenAI: where prompt content is stored, retention period, whether prompts are used for any vendor-side training or evaluation, the BAA or DPA posture with the model vendor, and the firm-side controls preventing prompt content from flowing into vendor training. Lawful-basis-for-processing is a data-section field where a state or international privacy law in operating footprint requires it.

##### 2. Outcomes analysis adds privacy-specific tests

Privacy-specific tests in scope:

- PII / NPI memorisation: query the model for known training records (or known retrieval entries) and measure leakage rate.
- Training-data extraction: structured prompts attempting to reconstruct training samples; measure reconstruction precision.
- Cross-customer retrieval (for RAG): test queries from one customer context that should not surface another customer's content; measure leak rate.
- PHI-leak (HIPAA contexts): output sampling for PHI elements not in the input or in scope of the use case.
- Prompt-template extraction: query-based attempts to surface the system prompt or retrieval prompt; measure extraction rate.

For each test, the success criterion is in firm-policy units (zero leaks, leak rate at or below threshold) and the owner is named.

##### 3. Robustness scope adds privacy-relevant adversarial tests

Privacy-relevant adversarial tests overlap with the cyber overlay but have privacy-specific framing:

- Membership-inference attack on training-data privacy.
- Prompt-injection on indirect content (uploaded documents, retrieved content) attempting to extract NPI/PHI from the prompt context.
- Differential-privacy guarantees check (where the firm asserts DP; verify the assertion).

##### 4. Monitoring scope adds privacy signals

Privacy monitoring entries, each with the six required fields:

- PII/NPI leak detection on outputs (sampling cadence, threshold, owner: privacy office in coordination with model owner, escalation: CPO, revalidation trigger: any leak above threshold).
- Cross-customer retrieval audit (for RAG; continuous if feasible, escalation: information security and privacy office).
- Customer-rights-request processing for the model's outputs (right to know, right to delete, right to opt out of automated decisioning where applicable); turnaround time as a metric.
- Privacy-incident detection on the model's processing surface; integration with the firm's incident-response function.

##### 5. Effective challenge gains privacy-tagged questions

Privacy-tagged effective-challenge questions probe concrete gaps:

- The PIA was completed at design; what evidence supports that the deployed system matches the PIA assumptions.
- The vendor BAA / DPA covers the model service; what is the firm's evidence that prompt content does not flow into vendor training or evaluation.
- For an automated-decisioning use case in EU footprint, what is the firm's process for the right to obtain meaningful information about the logic involved (GDPR Article 22).
- For a credit-decisioning model, what is the SHAP / reason-code-mapped adverse-action notice generation method, and how does it satisfy the principal-reasons standard under Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary.
- For a GenAI model with NPI/PHI in the prompt context, what is the firm's leak-detection cadence and what is the off-switch criterion.

##### 6. Dependencies add privacy functions

The plan's dependencies list adds:

- Privacy office review of the data classification and the PIA.
- BAA / DPA evidence for any vendor handling NPI/PHI.
- Customer-rights workflow integration evidence (for jurisdictions with right-to-know / right-to-delete obligations).
- For EU footprint, GDPR Article 22 right-to-explanation evidence and (where applicable) Article 27 FRIA.

#### Privacy-specific output template additions

- `data_review.privacy_classification` — per-data-source classification (NPI, PHI, PCI, customer-supplied prompts, public, confidential).
- `data_review.prompt_surface` — for GenAI, retention, vendor-side training posture, BAA / DPA reference, redaction posture.
- `data_review.lawful_basis_for_processing` — where a state or international privacy law requires it.
- `outcomes_analysis[]` — PII/NPI memorisation, training-data extraction, cross-customer retrieval, PHI-leak, prompt-template extraction tests.
- `robustness_testing[]` — membership-inference, indirect-prompt-injection-for-NPI/PHI-extraction, differential-privacy verification where asserted.
- `monitoring[]` — PII/NPI leak detection, cross-customer retrieval audit, customer-rights-request processing turnaround, privacy-incident detection.
- `effective_challenge_questions[]` — privacy-tagged (PIA conformance, vendor BAA/DPA evidence, GDPR Article 22 right-to-explanation, ECOA adverse-action method, NPI/PHI leak-detection cadence).
- `dependencies[]` — privacy office review, BAA/DPA evidence, customer-rights workflow integration, FRIA evidence where applicable.

#### Common pitfalls in privacy-flagged validation plans

- Classifying foundation-model training data without addressing in-context customer prompts. The prompt surface is where customer NPI/PHI most often enters a GenAI use case; vendor system-card statements about training-data privacy do not extend to the firm's deployed prompt surface.
- Treating a vendor's data-processing posture as covering the firm; the firm's BAA (HIPAA) or DPA (GDPR / state privacy) is the firm's evidence, not the vendor's marketing.
- Assuming a HIPAA business-associate agreement with the LLM vendor exists when it does not; PHI flowing into a non-BAA-covered model is a recordable issue, not a plan-body assertion of HIPAA coverage.
- Defaulting to "this is anonymous" without actually anonymising prompts in the leak test. PII redaction is a control with evidence; the claim without the control is a plan-recordable issue.
- Omitting the customer-rights workflow validation for an automated-decisioning use case; right to know, right to delete, and (where applicable) right to opt out of automated decisioning are workflow obligations that the plan's monitoring scope should test.
- Carrying the PIA conclusion into the plan as if it were the validator's privacy-program output. The plan points to the PIA in source trace; the PIA itself is the privacy-program artifact.
- Setting the cross-customer retrieval test as a one-time pre-prod test only; for RAG architectures, this is an ongoing-monitoring item, not just a pre-prod gate item.
