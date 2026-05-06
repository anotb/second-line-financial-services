# prompt-injection-risk — Phase 1 spec sheet

Date: 2026-05-06
Plugin: ai-governance-model-risk
Phase: 1 (per-skill scoping; no SKILL.md content)
Status: NEW for v1 (GenAI expansion).

## Activation-tuned description

Reviews the prompt-injection threat surface for a deployed or near-deployed GenAI use case. Catalogues the carriers (system prompt, user input, retrieved content, tool output, agent memory), enumerates the tested attack classes, lists the mitigations in place, and states the residual risk and the monitoring and detection coverage. Output is a second-line-grade memo a CISO, head of AI risk, or AI risk committee can act on.

Best for:
- A GenAI assistant or agent is approaching pre-prod and second-line needs an explicit prompt-injection review.
- An incident or near-miss in a GenAI deployment has surfaced a prompt-injection vector and the committee needs an updated residual-risk view.
- A pre-exam or pre-cyber-audit motion needs the firm-wide prompt-injection posture documented for a defined population of GenAI use cases.

Not the right tool when:
- The system has no LLM, no instructions in natural language, and no retrieved or third-party-supplied text in its prompt path (use validation-plan and the standard model-risk skills).
- The system uses a foundation model only for embedding generation or classification with no instruction-following surface.
- The work is broader red-teaming across hallucination, bias, and abuse (use validation-plan with the GenAI testing block; this skill is the prompt-injection-only deep-dive).

Anchored to: NIST AI RMF Generative AI Profile (NIST AI 600-1) Manage 2.7 (prompt-injection mitigations) and Measure 2.7 (prompt-injection testing); OWASP Top 10 for LLM Applications (LLM01 Prompt Injection, LLM02 Insecure Output Handling, LLM07 Insecure Plugin Design, LLM08 Excessive Agency) [verify edition]; MITRE ATLAS framework (TA0043 reconnaissance, TA0011 command and control, TA0040 impact in the AI context, with prompt-injection-relevant techniques) [verify exact taxonomy]; NCSC guidelines for secure AI system development [verify date]; NYDFS Industry Letter on Cybersecurity Risks Arising from AI (October 2024).

## Source anchors

- NIST AI RMF Generative AI Profile (NIST AI 600-1) — Manage 2.7 (prompt-injection mitigation expectations), Measure 2.7 (testing approach), Manage 2.8 (downstream impact), Govern 6.1 (third-party considerations including foundation models) [verify exact subcategory numbering].
- OWASP Top 10 for LLM Applications [verify edition] — LLM01 Prompt Injection (direct and indirect), LLM02 Insecure Output Handling, LLM03 Training Data Poisoning, LLM06 Sensitive Information Disclosure, LLM07 Insecure Plugin Design, LLM08 Excessive Agency.
- MITRE ATLAS — adversarial threat taxonomy applicable to LLM-based systems [verify exact technique IDs for prompt injection / jailbreak / evasion].
- NCSC guidelines for secure AI system development [verify date] — design and operational expectations including secure-by-design considerations for prompt injection.
- NYDFS Industry Letter on Cybersecurity Risks Arising from AI (October 2024) — prompt injection and AI-enabled threats called out as supervisory expectations for covered entities.
- NIST SP 800-53 (informational) — security controls referenced for logging, monitoring, identity, and access in AI systems.
- ISO/IEC 42001:2023 §8.3 (AI system lifecycle controls).
- Public Anthropic, OpenAI, Google system cards — used as a pattern reference for how foundation-model providers describe injection-relevant testing and mitigations (no firm-specific facts copied).

## Sector overlays needed

- `references/sector-overlays/banking.md` — banker-assistant and KYC-assistant injection surfaces (customer chat history, ingested documents, AML alert narratives); regulator overlap with FFIEC IT booklet on emerging tech [verify].
- `references/sector-overlays/insurance.md` — claims-summary and underwriting assistants; injection surface includes scanned correspondence, medical records, third-party adjuster notes; NAIC Model Bulletin alignment.
- `references/sector-overlays/capital-markets.md` — research and surveillance assistants; injection surface includes ingested news, social media, transcripts; MAR / Reg AC adjacency.
- `references/sector-overlays/payments-fintech.md` — onboarding and dispute-handling assistants; injection surface includes customer-supplied evidence and merchant correspondence.

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — primary overlay. NYDFS October 2024 alignment. Maps prompt-injection threats to existing cyber control frame (identity, logging, detection, IR).
- `references/cross-cutting/privacy.md` — injection-driven exfiltration of PII or NPI as a privacy event class.
- `references/cross-cutting/conduct.md` — injection-driven customer-facing harm (offensive output, false promises, off-label financial advice).

Climate not applicable.

## Output template named sections

1. Use case reference and architecture summary
2. Threat surface (carriers and trust posture for each: system prompt, user input, retrieved content, tool output, agent memory, multi-agent message)
3. Tested attack classes (named, with method, dataset or red-team reference, success criterion, result)
4. Mitigations in place (input filtering, output filtering, retrieval source vetting, tool boundary, structured output enforcement, content provenance, refusals)
5. Residual risk (named, with likelihood and impact framing, accepted-risk owners)
6. Monitoring and detection (signals captured in production, thresholds, owners, escalation)
7. Incident response (incident classes, named procedures, regulator-notification triggers)
8. Recommended owner actions (gaps to close, deadlines)
9. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `use_case_id` | string | Links to intake record. |
| `architecture_summary` | object | Sub-fields: foundation_model, uses_rag, uses_tools, multi_agent, memory. |
| `threat_surface` | array of objects | Each: carrier (system_prompt/user_input/retrieved_content/tool_output/memory/multi_agent_message), trust_posture, controls_at_carrier. |
| `tested_attacks` | array of objects | Each: attack_class, method (direct/indirect/jailbreak/exfiltration/tool_hijack/agent_redirect), dataset_ref, success_criterion, result, residual. |
| `mitigations` | array of objects | Each: mitigation, type (input_filter/output_filter/source_vetting/tool_boundary/structured_output/refusal/provenance), evidence. |
| `residual_risk` | array of objects | Each: risk, likelihood, impact, accepted_owner, accepted_date. |
| `monitoring_detection` | array of objects | Each: signal, threshold, owner, escalation_path. |
| `incident_response` | array of objects | Each: incident_class, procedure, regulator_notification_trigger. |
| `recommended_actions` | array of objects | Each: gap, owner, deadline, severity. |
| `source_trace` | array of objects | Claim, source, evidence reference, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. A US bank deploys a GenAI assistant for relationship managers that retrieves over an internal CRM and recent public earnings transcripts. Prompt-injection review identifies indirect injection in transcript retrieval as the highest-likelihood vector (transcript text is third-party-controlled). Tested attacks: direct system-prompt override, indirect injection in transcript, exfiltration of system-prompt content, retrieval-poisoning via crafted public material. Mitigations in place: retrieval-source vetting limited to a fixed list of transcript providers, output-filtering refusal of any output containing internal CRM identifiers when the user is unauthenticated, structured-output enforcement on summaries. Residual risk: a determined adversary publishing crafted earnings-call transcripts could redirect the assistant; likelihood low, impact medium. Monitoring: refusal-rate, output-filter trip rate, anomalous summary length. Recommended actions: add per-source provenance tag to retrieved content, drill IR procedure quarterly.

2. A regional life insurer pilots a GenAI claims-summary assistant operating over scanned correspondence and PHI documents. Prompt-injection review identifies indirect injection via scanned correspondence (where a claimant or a third party could embed instructions) as the highest-likelihood vector. Tested attacks: direct prompt override in adjuster query, indirect injection in scanned correspondence to extract PHI on unrelated claimants, jailbreak to bypass refusal of medical-advice queries, tool-hijack attempt (no tools enabled, so n/a). Mitigations: PHI access scoped per claim file, OCR step normalises and strips suspicious patterns, output-filter refuses any output mentioning a non-current claim ID, no tool calls available. Residual risk: a rare crafted correspondence could surface a small amount of in-claim-file content out of context to the adjuster; likelihood low, impact low. Monitoring: refusal-rate, output-filter trip rate, sampling of summaries against ground truth. Recommended actions: add immutable audit log retention beyond the platform default, drill IR procedure with the privacy officer.

## Common pitfalls

1. The review focuses only on direct injection (the user typing "ignore previous instructions") and skips indirect injection in retrieved or tool-supplied content. Indirect injection is the more common practical vector. Mitigation: required carrier-by-carrier coverage in the threat surface block.
2. The mitigations list lists tools without evidence that they are configured and exercised. Output-filtering is named, but no one knows what the regex set actually contains. Mitigation: each mitigation entry requires an evidence reference (config link, test report, change record).
3. Residual risk recorded as "low" without likelihood and impact framing. Becomes opinion. Mitigation: required likelihood and impact fields with one-line basis.
4. Monitoring lists signals without thresholds or owners. The signal exists in a dashboard nobody reads. Mitigation: each monitoring entry requires threshold, owner, and escalation.
5. Foundation-model swap risk ignored. The provider updates the model and the residual-risk view is now stale. Mitigation: required `foundation_model_swap_revalidation` flag in recommended actions when the architecture depends on a third-party foundation model.
