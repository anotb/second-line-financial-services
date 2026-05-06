# Cyber cross-cutting overlay for ai-use-case-intake

When the engagement-scope record flags `cyber` for the use case, this overlay supplies the cyber-specific intake fields and the named flags that route into downstream tier and pre-prod work. It does not replace the firm's information-security risk assessment; it is the intake-side surfacing of cyber considerations a second-line reviewer (and an examiner under NYDFS Part 500 or the FFIEC IT Handbook) will look for.

Loaded by: `ai-use-case-intake/SKILL.md` when `engagement_scope.cross_cutting_set` includes `cyber`. Source-anchored in `references/source-anchors.md`.

## Source basis

- NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 16, 2024) — covered entities under 23 NYCRR Part 500 expected to address AI-related cybersecurity risks, including AI-enabled threats and risks from the entity's own use of AI.
- 23 NYCRR Part 500 (Second Amendment) — covered-entity cybersecurity program expectations.
- NIST AI 600-1 (Generative AI Profile) Manage subcategories on prompt injection, training-data poisoning, model extraction, content provenance.
- OWASP Top 10 for LLM Applications and MITRE ATLAS as the threat taxonomies that anchor the AI-cyber intake fields.
- FFIEC IT Examination Handbook, Information Security and Cybersecurity sections, applied to the model's serving environment, change controls, and access controls.

## Cyber-specific intake fields

In addition to the capability intake spine, the cyber overlay adds the following:

- AI-enabled threat surface (the entity's exposure to AI-enhanced phishing, deepfake-driven social engineering, AI-driven credential stuffing). Fielded as a one-paragraph narrative with named exposures.
- The entity's own AI use risk surface (prompt injection, training-data poisoning, model extraction, supply-chain dependence on a foundation-model vendor, RAG-corpus poisoning, content-provenance posture). Fielded as a checklist with each exposure scored exposed / not exposed / unclear.
- NYDFS Part 500 covered-entity status. Fielded as a boolean with the operating-state footprint that triggers the status.
- Foundation-model vendor change-of-version posture (pinned, floating with notice, rolling without notice). Captured as part of the architecture block but cyber-relevant because rolling-without-notice is a supply-chain surface.
- Adversarial-test posture (vendor-supplied adversarial-test results only, firm-independent red-team evidence, none). Vendor self-attestation alone is not evidence the firm has tested its own deployed prompt surface, retrieval corpus, or tool inventory.

## Cyber-specific regulatory flags

When the cyber overlay is loaded, the intake's regulatory-flags table picks up:

- `NYDFS_Part_500` (where the firm is a covered entity in the NY footprint) with routing to `ai-risk-tiering`.
- `NYDFS_AI_letter_2024` (where any of the named AI-enabled threats or own-AI-use risks apply) with routing to `ai-risk-tiering`, `prompt-injection-risk`, and `genai-pre-prod-review`.
- A general flag for the firm's information-security policy where applicable (for non-NYDFS firms; FFIEC IT Handbook reach for federally regulated banks).

## Cyber-specific open questions for downstream skills

The intake routes the following open questions when relevant:

- For `prompt-injection-risk`: where is the prompt surface, what controls limit prompt-injection exposure, what evidence does the firm have of red-team testing of the deployed prompt surface (not just vendor self-attestation).
- For `rag-evaluation-review`: what is the retrieval-corpus access control, what is the corpus refresh and provenance evidence, what is the firm's posture on retrieval-corpus poisoning detection.
- For `validation-plan`: how is foundation-model version monitoring instrumented, how is the firm notified of vendor change-of-version, what is the regression-test posture on vendor change.
- For `agentic-ai-controls`: where the use case has tool privileges, what limits the tool-action scope, what is the circuit-breaker posture if the tool is used outside its boundary.
- For `vendor-diligence`: what is the foundation-model vendor's evidence pack on supply-chain integrity, model-extraction defences, and incident-response cooperation.

## Common pitfalls in cyber-flagged intake

- Treating "vendor pen-tested" or vendor adversarial-test results as evidence the deployed prompt surface is hardened. The firm's prompt template, retrieval corpus, and tool inventory are firm-side surfaces; the intake captures evidence at the firm level, not vendor self-attestation.
- Recording an internal-only GenAI use case as low cyber-exposure. Internal-only does not eliminate cyber exposure when the use case has tool privileges, retrieval-corpus access across business lines, or vendor-hosted infrastructure.
- Treating prompt injection as a quality issue rather than a control-evasion path. When the use case has tool or agent privileges, prompt injection becomes a lateral-movement opportunity and the intake's autonomy-level and tool-inventory blocks need to reflect that.
- Failing to flag NYDFS Part 500 covered-entity status. The October 2024 NYDFS Industry Letter on AI cybersecurity is a current expectation; the flag belongs in intake regardless of which downstream skill picks it up.
- Recording the foundation-model pinning posture as "floating" without naming the vendor change-of-version notice channel. "Floating with notice" is a different posture from "rolling without notice" and the intake distinguishes them.
