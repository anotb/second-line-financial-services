# Cyber cross-cutting overlay for validation-plan

When the scope record flags `cyber` for the model use case, this overlay adds cyber-specific scope items to the validation plan. AI red-teaming and adversarial robustness overlap substantially with cyber red-teaming; this overlay is where that overlap is named so the validator and the CISO function are reading the same testing surface.

Loaded by: `validation-plan/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- NYDFS 23 NYCRR Part 500, especially the third-party-risk, incident-response, and incident-notice provisions (Part 500 governs covered entities; the model is in scope when it sits inside a covered entity's information system or is hosted by a third-party service provider).
- NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024), addressing AI-enabled threats and the entity's own use of AI.
- SEC cyber disclosure rules: 8-K Item 1.05 (material cybersecurity incident disclosure) and Reg S-K Item 106 (cybersecurity risk management, strategy, and governance) where the registrant is public.
- FFIEC IT Examination Handbook, Information Security and Cybersecurity sections, applied to the model's serving environment, change controls, and access controls.
- NIST AI 600-1 (Generative AI Profile) cyber-relevant Measure subcategories: prompt injection (direct and indirect), data poisoning, model extraction, evasion, information security.
- EU AI Act Article 15(5) on resilience to attacks (data poisoning, model poisoning, model evasion, confidentiality attacks, model flaws) for high-risk EU AI systems.

## What changes for cyber-flagged validation plans

### 1. Conceptual soundness gains a cyber-architecture review

The plan's conceptual-soundness scope adds a cyber-architecture review subsection: input channels (chat, API, batch, retrieval triggers), prompt-injection robustness posture (tested, untested, vendor-tested), model-supply-chain dependence (foundation-model provider, model-hosting environment, model artefact integrity controls), and tool/agent privileges where applicable. For a traditional ML model the subsection is short (serving environment, model-artefact integrity, access controls); for a GenAI model with tool use or agentic behaviour, it is one of the deeper scope items.

### 2. Data review flags poisoning and extraction exposure

For models trained or fine-tuned on firm data, the data-review scope adds:

- Training-data integrity controls (provenance, change-detection on training corpora) and the residual exposure to data-poisoning where the controls are partial.
- For RAG-using models, the retrieval corpus is itself a cyber-relevant surface (retrieval-corpus injection is a real attack pattern); access controls, content-validation controls, and refresh integrity model are scoped.
- Training-data extraction risk for models exposing memorised training data through outputs.

### 3. Robustness scope expands to the AI red-team / cyber red-team overlap

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

### 4. Monitoring scope adds cyber-relevant signals

Monitoring entries the cyber overlay expects, each with the six required fields (metric, threshold, frequency, owner, escalation path, revalidation_trigger):

- Authentication and authorisation anomalies on the model's serving endpoint.
- Prompt-injection detection signals (where the firm has a detection layer; if not, the absence is recorded as an effective-challenge question on the gap).
- Output-anomaly detection (sudden shifts in refusal rate, citation patterns, tool-call patterns are leading indicators of compromise as well as drift).
- Vendor change-of-version signals for foundation-model and serving-environment dependencies; an unannounced version swap is both a cyber signal and a model-risk signal, with `revalidation_trigger = true`.
- Tool-invocation rate and pattern monitoring for GenAI with tool or agent privileges; sudden expansion of tool use is an investigation trigger.
- Retrieval-corpus integrity monitoring (for RAG); change-of-content detection on the retrieval corpus.

Cyber-relevant entries typically escalate to the CISO function in addition to the model owner.

### 5. Effective challenge gains cyber-tagged questions

Cyber-tagged effective-challenge questions probe specific gaps, not the broad cyber posture:

- The agentic system has tool privileges; what is the tool-boundary control and what is the off-switch criterion if tool-invocation rate or pattern shifts beyond baseline.
- The foundation-model is vendor-opaque; what is the firm's evidence base for adversarial robustness that does not depend on vendor self-attestation.
- The retrieval corpus is firm-controlled but the corpus owner is in a different function from the model owner; what is the change-control loop and what does the validator need to see to consider it adequate.
- The prompt-injection detection layer is novel; what is the validator's confidence in detection precision and recall.
- An unannounced foundation-model version swap is both a model-risk and a cyber event; what is the operational test that the version-monitoring control actually fires.

### 6. Dependencies expand to cyber functions

The plan's dependencies list adds:

- Information-security red-team capacity and scheduling.
- Vendor evidence (system card, evaluation report, red-team summary) reviewed jointly with the cyber function.
- Detection-layer evidence pack from the firm's cyber detection function.
- For NY footprint, NYDFS Part 500 covered-entity self-assessment and the October 2024 industry letter alignment evidence.

## Cyber-specific output template additions

- `conceptual_soundness.cyber_architecture_review` — subsection covering input channels, prompt-injection posture, supply-chain dependence, tool/agent privileges.
- `robustness_testing[]` — cyber attack classes from the catalogue above, each with method, success criterion, owner.
- `monitoring[]` — cyber-tagged entries (authentication anomalies, prompt-injection detection, output-anomaly detection, vendor change-of-version, tool-invocation patterns, retrieval-corpus integrity), each with CISO-function escalation path.
- `effective_challenge_questions[]` — cyber-tagged (tool-boundary, vendor-opaque robustness evidence, retrieval-corpus change control, detection-layer confidence, version-monitoring operational test).
- `dependencies[]` — info-security red-team capacity, joint vendor-evidence review, detection-layer evidence pack, NYDFS Part 500 self-assessment evidence where applicable.

## Common pitfalls in cyber-flagged validation plans

- Treating "vendor pen-tested" or vendor-supplied adversarial-test results as evidence the deployed prompt surface is hardened. The firm's prompt template, retrieval corpus, and tool inventory are firm-side surfaces and need firm-side testing.
- Framing prompt-injection only as a quality issue. It is also a control-evasion path when the model has tool or agent privileges.
- Assuming model isolation when the model has tool or agent privileges. Tool privileges are lateral-movement opportunities; the plan's robustness scope includes tool-misuse and goal-hijack tests explicitly.
- Omitting vendor change-of-version monitoring; a silent foundation-model swap is both a model-risk event and a cyber event.
- Treating the cyber overlay as the CISO's plan. The validation plan is the validator's scope contract; the CISO function is a joint-review and escalation audience, not the owner.
- Listing "red team" as a single robustness entry without enumerating attack classes; the catalogue above is what the validator scopes against, and the plan reads test-by-test.
- Treating EU AI Act Article 15(5) as out of scope for US-only operations; for any high-risk EU AI system that touches EU users or markets, Article 15(5) cyber-resilience evidence is part of Annex IV technical documentation.
