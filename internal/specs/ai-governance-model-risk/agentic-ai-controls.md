# agentic-ai-controls — Phase 1 spec sheet

Date: 2026-05-06
Plugin: ai-governance-model-risk
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Reviews and proposes controls for an agentic AI use case (an AI system that selects actions, calls tools, or operates with autonomy beyond single-turn generation). Output names the agent's scope and authority, the tool inventory and permission boundary, the human oversight points, the kill-switch and rollback procedures, and the residual risk. Designed for second-line review of agents that book actions in real systems, not chat-only assistants.

Best for:
- A first-line owner has built or is building an agentic system that calls tools, reads from systems of record, or executes actions, and second-line needs control coverage before pre-prod or expansion.
- A previously deployed assistant is being upgraded with tool-use, retrieval, or multi-step planning, and the controls and gates need to be revisited.
- An enterprise-wide review of agentic deployments needs a consistent control inventory across sponsoring units.

Not the right tool when:
- The system is a retrieval-augmented chat assistant with no tool calls and no actuation (use rag-evaluation-review and the model card).
- The work is the use-case intake or risk tier itself (use ai-use-case-intake or ai-risk-tiering).
- The system is a vendor-hosted agentic product still in procurement (use vendor-diligence in third-party-operational-resilience with the AI vendor mode; this skill assumes a deployment review on a system the firm is operating).

Anchored to: NIST AI RMF 1.0 Govern 4.x and Manage 4.x; NIST AI RMF Generative AI Profile (NIST AI 600-1) Manage 2.7 (prompt injection), Manage 2.8 (downstream impact in deployed systems), Manage 4.1 (incident handling); SR 11-7 §IV-V applied to agentic systems; OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026) [verify section]; ISO/IEC 42001:2023 §8.x (operational controls); NYDFS Industry Letter on Cybersecurity Risks Arising from AI (October 2024); MITRE ATLAS framework (informational).

## Source anchors

- NIST AI RMF 1.0 Govern 4.1 to 4.3 (organisational accountability and roles), Manage 1.x (managing AI risks), Manage 4.x (deployment monitoring and incident response).
- NIST AI RMF Generative AI Profile (NIST AI 600-1) — Manage 2.7 (prompt injection mitigations), Manage 2.8 (downstream impact in deployed systems), Manage 3.x (third-party considerations including foundation model providers), Manage 4.1 (incident handling) [verify exact numbering].
- SR 11-7 §IV (model risk management framework) and §V (validation, monitoring, controls) — applied to agentic systems where the agent itself is a model under the framework.
- OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026) [verify section on agentic AI and tool-use].
- ISO/IEC 42001:2023 §8.1 (operational planning), §8.2 (AI system impact assessment), §8.3 (AI system lifecycle controls).
- NYDFS Industry Letter on Cybersecurity Risks Arising from AI (October 2024) — covers prompt injection, deepfakes, and AI-enabled threats to deployed systems.
- MITRE ATLAS — adversarial threat catalogue for AI systems (informational reference for attack class enumeration).
- NCSC guidelines for secure AI system development [verify date] — informational reference for design controls.
- OWASP Top 10 for LLM Applications [verify edition] — informational reference for application-level threats including LLM07 insecure plugin design and LLM08 excessive agency.

## Sector overlays needed

- `references/sector-overlays/banking.md` — agentic operations in deposit servicing, payments initiation, fraud response; controls for booking-system actuation, dual-authorisation requirements.
- `references/sector-overlays/insurance.md` — agentic claims-handling actuation (automated payment, policy endorsement); state insurance fairness and consumer protection alignment; NAIC Model Bulletin on Use of AI Systems by Insurers, 2023. (NOTE: claims-ai-controls absorbed into this skill; the insurance overlay is required.)
- `references/sector-overlays/capital-markets.md` — agentic order-routing or position-actioning; SEC Rule 15c3-5 market-access controls, kill-switch expectations, FINRA supervisory controls.
- `references/sector-overlays/payments-fintech.md` — agentic onboarding and transaction-handling actuation; sponsor bank controls.

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — NYDFS October 2024 AI cyber letter alignment; tool-use threat surface; identity and access management for agent service accounts; logging and tamper resistance.
- `references/cross-cutting/privacy.md` — agent access scope to regulated data; retention of agent traces.
- `references/cross-cutting/conduct.md` — customer-impact actuation (account holds, benefit decisions, communications); fairness and complaint surface.

Climate not applicable.

## Output template named sections

1. Agent metadata (agent ID, version, sponsor, tier, scope date)
2. Agent scope and authority statement (what the agent may do, what it may not do)
3. Architecture (planner/executor model, foundation model, RAG, tool layer, memory, multi-agent topology)
4. Tool inventory (tool name, system of record, action type, permission level, blast radius if misused)
5. Identity and authorisation (agent service account, scoping, secret management, rate limits)
6. Human oversight points (when a human must approve, when a human is notified, when the agent acts autonomously)
7. Guardrails (input filtering, output filtering, refusal behaviour, escalation triggers)
8. Prompt-injection and tool-misuse threat assessment (with named attack classes from MITRE ATLAS / OWASP LLM)
9. Kill switch and rollback (named procedures, owners, RTO)
10. Logging, traceability, and audit (what is logged, retention, who can read)
11. Incident response (incident classes, owners, escalation, regulator-notification path)
12. Residual risk assessment (named risks, mitigations, accepted-risk owners)
13. Recommended owner actions (gaps to close, deadlines)
14. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `agent_id` | string | Canonical agent ID and version. |
| `use_case_id` | string | Links to intake record. |
| `tier` | enum | Tier from ai-risk-tiering. |
| `authority_statement` | object | Sub-fields: in_scope_actions, out_of_scope_actions, geographic_scope, customer_scope. |
| `architecture` | object | Sub-fields: planner_model, foundation_model (provider, version), uses_rag, multi_agent (bool), memory (none/short/long). |
| `tool_inventory` | array of objects | Each: tool_name, system, action_type, permission, blast_radius, owner. |
| `identity_authz` | object | Sub-fields: service_account, scopes, secret_management, rate_limit. |
| `human_oversight` | array of objects | Each: decision, oversight_mode (approve/notify/post-hoc), reviewer, SLA. |
| `guardrails` | array of objects | Each: guardrail, type (input/output/behaviour), evidence. |
| `threat_assessment` | array of objects | Each: attack_class, source (ATLAS/OWASP/NIST 600-1), mitigation, residual. |
| `kill_switch` | object | Sub-fields: procedure, owner, RTO, last_drilled. |
| `logging` | object | Sub-fields: log_content, retention, access_controls, immutability. |
| `incident_response` | array of objects | Each: incident_class, owner, escalation, regulator_notification_trigger. |
| `residual_risk` | array of objects | Each: risk, mitigation, accepted_owner, accepted_date. |
| `recommended_actions` | array of objects | Each: gap, owner, deadline, severity. |
| `source_trace` | array of objects | Claim, source, evidence reference, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. A regional US bank deploys an agentic assistant for customer service representatives that can read account state, place a temporary card lock, schedule a callback, and draft a customer communication. Review captures: scope (representative-initiated only, no autonomous customer-facing actuation), tool inventory (account-read, card-lock-temp, callback-schedule, comm-draft; comm-draft requires representative approve), authority (no funds-movement, no permanent card actions, no fee adjustments), threat assessment (prompt injection via customer chat history, tool-misuse via repeated card-lock for the same customer), kill switch (representative supervisor or platform on-call can disable agent service account in under five minutes), residual risk (slow drift in card-lock-temp call rate post-deployment).

2. A capital markets broker-dealer pilots an agentic research assistant that can pull data from internal price databases and external public-source databases, plot a chart, and propose a draft client note for analyst review. Review captures: scope (analyst-initiated only, no client communication actuation), tool inventory (price-database-read, public-source-fetch, chart-render, note-draft; note-draft is text only with no send), authority (no order-routing, no order-management interaction, no client-list access), threat assessment (indirect prompt injection in fetched public sources, hallucinated data when source returns empty, recency exposure), kill switch (analyst lead can disable agent on the platform), residual risk (note-draft errors that escape analyst review and surface in client materials, MAR/Reg AC adjacency).

## Common pitfalls

1. Authority statement is descriptive prose ("the agent helps representatives serve customers") with no enumeration of what the agent may not do. The boundary becomes operational drift. Mitigation: required out-of-scope actions list with at least three concrete entries.
2. Tool inventory captures tool names but not blast radius. A tool labelled "schedule callback" can also be used to spam every customer in a queue if rate-limited badly. Mitigation: blast-radius field is required for each tool.
3. Human oversight is documented but not effective. Reviewers click through. Mitigation: oversight mode must include SLA and a sampling expectation; agentic decisions with `approve` mode require evidence that the approval is read, not auto-clicked.
4. Kill switch is documented but never drilled. Mitigation: `last_drilled` date required; if older than the tier's drill cadence, flag as gap.
5. Threat assessment lists generic "prompt injection" without naming the attack class or the carrier. Indirect injection via retrieved customer chat history is a different control problem from direct injection in the system prompt. Mitigation: each threat-assessment entry must name attack class and carrier (system prompt, user prompt, retrieved content, tool output, agent memory).
