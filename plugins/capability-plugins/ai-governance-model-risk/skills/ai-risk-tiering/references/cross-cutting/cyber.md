# Cyber cross-cutting overlay for ai-risk-tiering

When the engagement-scope record flags `cyber` for the use case, this overlay supplies the cyber-specific factors that weight up the tier and the named triggers that force a re-tier when the cyber posture changes. It does not replace the firm's information-security risk assessment; it is the tiering-side surfacing of cyber considerations that a second-line reviewer (and an examiner under NYDFS Part 500 or the FFIEC IT Handbook) will look for.

Loaded by: `ai-risk-tiering/SKILL.md` when `engagement_scope.cross_cutting_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 16, 2024) — covered entities under 23 NYCRR Part 500 are expected to address AI-related cybersecurity risks, including AI-enabled threats and risks from the entity's own use of AI.
- NIST AI 600-1 (Generative AI Profile) Manage subcategories on prompt injection, training-data poisoning, model extraction, and content provenance.
- OWASP Top 10 for LLM Applications and MITRE ATLAS as the threat taxonomies that anchor the cyber factor scoring.
- FFIEC IT Examination Handbook, Information Security and Cybersecurity sections, applied to the model's serving environment, change controls, and access controls.

## Cyber-specific scoring guidance

The capability rubric scores `cyber_exposure` once. The overlay tells the rubric what counts as high, medium, low for this factor:

- **High** — any of: GenAI use case with tool or agent privileges; customer-supplied prompt content that can carry adversarial instructions; foundation-model dependence with no firm-side adversarial testing; retrieval corpus accessible to multiple business lines without strong scoping; covered entity under NYDFS Part 500 with the use case in the NY footprint and no firm-side red-team evidence.
- **Medium** — any of: foundation-model dependence with vendor-supplied adversarial-test results only (vendor self-attestation, no firm-independent testing); RAG over firm-controlled corpora with controlled access; advisory-only with human-in-the-loop on outputs; serving environment isolated and version-pinned but unmonitored for unannounced version swaps.
- **Low** — traditional ML on firm-internal data, no foundation-model dependence, no customer-facing surface, no tool or agent privileges, internal serving environment with monitored change control.

The cyber score is dominant where the use case is GenAI with tool privileges or with a customer-facing prompt surface; otherwise it is contributing.

## Cyber-specific re-tiering triggers

Add to the re-tiering trigger block when `cross_cutting_set` includes `cyber`:

- Vendor change-of-version notice on a foundation model or model-serving platform. Owner: vendor management with CISO function. Detection: vendor change-of-version notice channel.
- Tool or agent-privilege expansion on a GenAI use case. Owner: AI governance with CISO function. Detection: change-management notice.
- New input channel that exposes the model to customer-supplied content (chat, email ingestion, document upload). Owner: AI governance with CISO function. Detection: change-management notice.
- Detected prompt-injection event or retrieval-corpus-injection event. Owner: CISO function with model owner. Detection: detection-layer alerting plus post-incident review.
- Footprint change into a NYDFS Part 500 covered jurisdiction, or material change to NYDFS Part 500 expectations. Owner: regulatory change function with CISO function. Detection: regulatory horizon scan.

## Common pitfalls in cyber-flagged tiering

- Treating "vendor pen-tested" or vendor adversarial-test results as evidence the deployed prompt surface is hardened. The firm's prompt template, retrieval corpus, and tool inventory are firm-side surfaces; the cyber score is set against firm-side evidence, not vendor self-attestation.
- Underweighting cyber exposure on a tier-3 internal-only GenAI use case. Internal-only does not eliminate cyber exposure when the use case has tool privileges, retrieval-corpus access across business lines, or vendor-hosted infrastructure.
- Treating prompt injection as a quality issue rather than a control-evasion path. When the use case has tool or agent privileges, prompt injection becomes a lateral-movement opportunity and the cyber score reflects that.
- Failing to flag NYDFS Part 500 covered-entity status. The October 2024 NYDFS Industry Letter on AI cybersecurity is a current expectation, not a future one; tier-up factors apply at the time of the tiering decision.
