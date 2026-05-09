---
name: prompt-injection-risk
description: |
  Reviews the prompt-injection threat surface for a deployed or near-deployed GenAI use case in a regulated financial-services firm. Catalogues the carriers (system prompt, user input, retrieved content, tool output, agent memory, multi-agent message, multimodal input), the trust posture on each, the tested attack classes, the mitigations in place with evidence, the residual risk with likelihood and impact framing, the production monitoring and detection signals, the incident-response classes with regulator-notification triggers, and the recommended owner actions. Output is a second-line-grade memo a CISO function, AI Governance Lead, MRMO, or AI risk committee can act on.

  Best for:
  - A GenAI assistant or agent is approaching pre-prod and second-line needs an explicit prompt-injection review before the gate.
  - An incident or near-miss in a deployed GenAI system has surfaced a prompt-injection vector and the committee needs a refreshed residual-risk view and notification-trigger evaluation.
  - A pre-exam or pre-cyber-audit motion needs the firm-wide prompt-injection posture documented for a defined population of GenAI use cases.
  - A foundation-model swap or a tool-inventory change has triggered the re-validation flag in change management.

  Not the right tool when:
  - The system has no LLM, no instructions in natural language, and no retrieved or third-party-supplied text in its prompt path; use validation-plan and the standard model-risk skills.
  - The system uses a foundation model only for embedding generation or classification with no instruction-following surface.
  - The work is broader red-teaming across hallucination, bias, and abuse; use validation-plan with the GenAI testing block. This skill is the prompt-injection-only deep-dive.
  - The work is the firm-side governance card for the use case; use model-card-builder. This skill consumes the card and produces the focused memo.
argument-hint: "[use-case ID, model-card record, validation-plan record, vendor red-team report, firm red-team report, IR runbook reference, or scope statement]"
---

# Prompt-injection risk review

A prompt-injection review is the second-line surfacing of one specific risk class in a GenAI deployment: instructions arriving through a content carrier and overriding, redirecting, or extracting from the system. It is not a full GenAI risk review; it is the cyber-and-AI-governance memo that names the threat surface, the testing, the mitigations with evidence, the residual risk with framing, the production signals with thresholds and owners, the incident classes with regulator-notification triggers, and the gaps that need to close.

Prompt injection sits across two regulator perspectives and the artefact has to name which is in play. The cyber-supervision regimes (NYDFS Part 500 with its October 2024 AI cybersecurity industry letter; SEC cybersecurity disclosure for public registrants; the bank computer-security incident notification rule; state Insurance Data Security Model Law) carry binding supervisory expectation in their respective scopes; prompt injection is, in those frames, a cybersecurity risk class with all the access, logging, monitoring, and notification expectations the cyber programme already carries. The AI-specific framings carry the controls vocabulary (NIST AI 600-1 GenAI Profile, OWASP LLM Top 10 with its 2025 numbering for prompt-injection and indirect-injection entries, MITRE ATLAS, NCSC/CISA secure-AI-development guidance); leading practice, voluntary, but the language vendor red-team reports and internal AI-security teams actually use. The bank model-risk regime (the 2026 joint interagency revised guidance) explicitly excludes GenAI and agentic AI; where the firm's model-risk programme treats the use case as a model by analogy, the principles inform but the binding hook is firm policy. Be explicit in the memo about which scope is in play.

The audience reads from three angles at once. The AI Governance Lead owns the artefact and consolidates the analysis. The CISO function is a co-reviewer, not a downstream consumer; for any cyber-flagged review (which is most v1 GenAI reviews) the cyber overlay sits as the primary lens. The MRMO function and the model owner inherit the model-risk seams; the model owner is the source of upstream evidence (model card, validation plan, vendor system card) and the MRMO challenges the residual-risk view.

The memo is a draft until the human reviewer attests. The skill stops short of filing or approving it.

## Ask first

Most of what the review needs is already on the table by the time someone reaches for this skill. A few things to settle before drafting:

- What is the architecture, and where does the review draw its scope. Foundation-model only, RAG, tool use, multi-agent, persistent memory, multimodal ... the answer drives which carriers populate the threat surface and which attack classes are non-optional. If `model-card-builder` has run, the system-description and GenAI-overlay sections of the card name this; consume the card.
- Where is the use case in lifecycle, and what triggered this review. Pre-prod-gate review consumes vendor red-team results and projects the firm-internal coverage gap. In-prod-periodic review consumes production-monitoring evidence. Post-incident review consumes the incident timeline and the IR runbook outputs. Exam-readiness review consolidates across.
- Who is co-reviewing. For most v1 GenAI reviews the CISO function is a co-reviewer; for any use case touching customer-facing communications, consumer compliance is in the room; for AML-touching use cases, the BSA officer is in the room. The reviewer-attestation block names them.
- What sector and cross-cutting overlays load. Banking, insurance, capital markets, or payments-fintech as sector; cyber as the default cross-cutting overlay; privacy and conduct as additional cross-cutting overlays where the scope flags them.

When the scope record is supplied, the skill consumes it for institution, persona, source posture, sector and cross-cutting overlays, lifecycle stage, and architecture flags. Otherwise it asks the practitioner the few facts it needs, and source posture sets what the memo can assert at high confidence and what carries `[evidence needed]`.

## How the memo gets filled in

The memo has the same spine across architectures. The order below is the dependency chain a senior practitioner walks; sections without dependencies fill in as evidence arrives.

Tier and architecture drive depth, so consume the model card and the scope record before deciding how heavy any section sits. Threat-surface enumeration must happen before tested-attack-class selection, because the attack classes that apply depend on the carriers the system actually has. Mitigation evidence must be in hand before residual-risk framing, because residual risk is the gap between the attack classes and the mitigations that hold them down.

**Review metadata** names the reviewer role, the review stage (pre-prod-gate, in-prod-periodic, post-incident, exam-readiness), the date, and the upstream artefact IDs (scope, model card, validation plan). Reviewer roles are functions, never named individuals.

**Use case reference and architecture summary** lands the architecture facts that drive every other section: foundation-model provider and version pinning posture, RAG corpora with retrieval scoping rules, tool inventory with autonomy level, multi-agent topology, memory mode, modalities. A pointer to the model card's system description is preferable to restating; the prompt-injection memo is not the place to re-derive architecture.

**Threat surface** enumerates the carriers the system has and assigns trust posture and trust basis on each. Every carrier the system actually has appears as a row, even if the trust posture is "trusted"; carriers not in the system are explicit "not applicable" rather than omitted (the omission would otherwise read as oversight). The trust basis is the load-bearing column. "Trusted because firm-controlled" differs from "trusted because authenticated" differs from "trusted because schema-validated upstream"; the basis is what fails first when the assumption changes.

**Tested attack classes** record what was tested, by whom, with what dataset reference, against what success criterion, with what result. The baseline attack-class set for a typical text-only RAG-using system is direct system-prompt override, indirect injection in retrieved content, exfiltration of system-prompt content, and jailbreak. For tool-using or agentic systems add tool hijack, agent redirect, and multi-agent message injection. For multimodal systems add multimodal injection per modality. For systems with persistent memory add memory poisoning. Vendor red-team results are recorded explicitly as vendor-tested; firm-internal red-team coverage gaps land as `[evidence needed]` and route to recommended actions.

**Mitigations** list each control with type, owner, evidence pointer, and whether the mitigation was exercised in any tested attack. A mitigation without an evidence pointer is policy, not a control. A mitigation listed but not exercised in any tested attack is recorded as `exercised_in_test = no` and routed to recommended actions; do not treat it as coverage.

**Residual risk** names each concrete residual risk with likelihood, impact, basis, accepted owner role, accepted date, and review cadence. "Low" without a basis is opinion. Cross-reference any partial or fail result in the tested-attacks table to a residual-risk row; an unaccepted partial result is itself a finding.

**Monitoring and detection** list each production signal with all five fields: signal, threshold (in firm policy units), frequency, owner (function), escalation path (named committee, officer, or process). The baseline signal set for a typical GenAI system is refusal rate, output-filter trip rate, anomalous output length (exfiltration leading indicator), and foundation-model version monitoring. RAG-using systems add retrieval-source audit and citation-precision sampling. Tool-using or agentic systems add tool-invocation rate and pattern, inter-agent message structured-output trip rate, and cross-scope tool query anomaly. Persistent-memory systems add memory-content sampling.

**Incident response** names each incident class, the procedure pointer, the regulator-notification trigger that applies, and the off-switch criterion. The off-switch is the operational decision the runbook turns on; if there is no off-switch, that is itself a critical-severity recommended action. Regulator-notification triggers come from the firm's existing cyber-incident regimes (NYDFS 72-hour notice, SEC 8-K Item 1.05 for public registrants, GLBA Safeguards notification, state breach laws, the bank 36-hour computer-security incident rule, sector-specific notification regimes); the sector and cross-cutting overlays carry the named triggers per scope.

**Recommended owner actions** name each gap with owner role (function), deadline, severity, and any depends-on. Severity is the second-line judgement, not the owner's. Critical-severity items typically block pre-prod sign-off. The standard recommended-action item that fires for any architecture depending on a third-party foundation model is the foundation-model swap re-validation flag in change management.

**Source trace and confidence** records every material claim, its source, the evidence pointer, and a confidence label. Vendor red-team results carry vendor-self-attestation confidence (typically low to medium); firm-internal red-team results carry higher confidence. Do not collapse vendor and firm evidence into one line. Items without evidence carry `[evidence needed]` and route to recommended actions.

Depth flexes with tier and audience. A pre-prod-gate review for a tier-2 customer-support assistant compresses to one or two pages of substance; a tier-1 agentic system review with cyber overlay can run long and dense. Empty named sections are not acceptable, but compression is.

## Sector and cross-cutting overlays

When the scope names a sector (banking, insurance, capital markets, payments-fintech), load the matching `references/sector-overlays/<sector>.md`. Each overlay carries sector-specific carriers, mitigations, monitoring signals, regulator-notification triggers, and co-reviewer expectations. The overlay's named additions land in the memo; treating the overlay as background reading is the failure mode.

The cyber cross-cutting overlay should be considered the default for v1 GenAI reviews. Prompt injection is, in NYDFS framing, a cybersecurity risk class; the CISO function co-reviews and co-decides on residual-risk acceptance. The overlay carries the cyber-side mitigations expected (authentication, audit logging, network controls, secrets handling, supply-chain controls, IR runbook integration), the cyber-tagged monitoring signals (authentication anomalies, tool-invocation patterns, output-anomaly detection), and the regulator-notification triggers most likely to apply.

The privacy and conduct cross-cutting overlays load when the scope flags them: privacy where the use case handles NPI, PHI, or other regulated personal data with potential for injection-driven exfiltration; conduct where the use case generates or assists customer-facing communications with potential for UDAAP, Marketing Rule, or fiduciary-lens exposure. Climate is not applicable.

Load only the overlays the scope names. Gold-plating with overlays the engagement does not implicate adds noise without challenge value.

## Quality bar

The memo is only credible when these hold:

- Every material claim cites a source. Unsupported items carry `[evidence needed]` and route to recommended actions, not silently into the memo body.
- Evidence is separated from inference. Vendor red-team results are not the same line as firm-internal red-team results; vendor self-attestation confidence is recorded explicitly.
- No fabricated regulatory facts. Unknown section references carry `[verify section]` in the source-anchors file (not in the memo body).
- Trust basis populates on every threat-surface row. "Trusted, no controls" without a basis fails the review.
- Mitigations without evidence pointers route to recommended actions. They do not count as coverage.
- Residual risk carries likelihood, impact, and basis. Rating without basis is opinion.
- Monitoring entries carry all five fields (signal, threshold, frequency, owner, escalation path).
- Incident response entries name regulator-notification triggers per the loaded overlays. Off-switch criteria on cyber-relevant classes are non-optional.
- Foundation-model swap re-validation is a non-optional recommended action for any architecture depending on a third-party foundation model.
- No named institutions outside finalised public enforcement actions; examples are anonymised and public-source-derived.
- Reviewer roles are functions, never named individuals.
- The memo is a draft until the human reviewer attests. The skill does not file the memo, post to the AI risk committee, or trigger an IR runbook.

## Adaptation

Tier drives depth. Lifecycle stage drives which sections lean heavy (pre-prod-gate emphasises tested attacks and mitigations; in-prod-periodic emphasises monitoring and residual risk; post-incident emphasises incident response and recommended actions). Audience drives tone (working group is plain, committee is structured, examiner response is formal, board distillation pulls residual risk and recommended actions to the front). Sector and cross-cutting overlays load from the scope. Source posture sets what the memo can assert at high confidence and what carries `[evidence needed]`. Where firm-specific policy or taxonomy applies, it lives in `references/firm-overlay.md` (consumed when present) and never in the memo directly.

## Output

Default to drafting the memo against `templates/default-output.md`. Render as Word for committee or CISO review, or another format the audience asks for. Produce the structured record at `schemas/prompt-injection-review.schema.json` when downstream consumers (`genai-pre-prod-review`, `board-ai-risk-pack`, `ai-governance-reviewer`, the firm cyber IR chain) need it. The reviewer-attestation block is filled by the human reviewer (AI Governance Lead with CISO function for cyber-flagged reviews; co-acceptors per sector overlay where applicable); the memo is filed only after.

Downstream consumers: `genai-pre-prod-review` consumes the structured object for the gate decision; `board-ai-risk-pack` pulls the residual-risk summary, the recommended-actions list, and material incident-response triggers; the `ai-governance-reviewer` agent pulls the structured object for second-line challenge; the firm cyber IR chain consumes the incident-response section as input to runbook design and IR drill scope. The schema is the input contract for those consumers; additive changes only.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded from scope.
- `references/cross-cutting/cyber.md` — cyber overlay, the default cross-cutting overlay for v1 GenAI reviews.
- `references/firm-overlay.md` — firm policy, taxonomy, named owners (consumed when present).
- `templates/default-output.md` — memo template.
- `schemas/prompt-injection-review.schema.json` — structured-output contract.
- `examples/` — anonymised public-source-derived scenarios (customer-support assistant; agentic research assistant).
- `TROUBLESHOOTING.md` — recurring defects.
