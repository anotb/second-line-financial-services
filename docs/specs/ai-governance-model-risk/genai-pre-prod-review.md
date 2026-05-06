# genai-pre-prod-review — Phase 1 spec sheet

Date: 2026-05-06
Plugin: ai-governance-model-risk
Phase: 1 (per-skill scoping; no SKILL.md content)
Status: NEW for v1 (GenAI expansion).

## Activation-tuned description

Pre-production gate review for a GenAI use case before initial release or material expansion. Pulls together the upstream artifacts (intake, tier, model card, validation plan results, prompt-injection review where applicable, RAG evaluation where applicable, vendor evidence review where applicable) and produces a go / hold / no-go recommendation with conditions, named gates, and owners. The document a senior risk officer or AI risk committee secretary signs into the meeting.

Best for:
- A GenAI use case is at the pre-prod gate and second-line needs the gate-review memo with a clear recommendation.
- A material expansion of an existing GenAI deployment (new user population, new tool, new corpus) needs a re-gate.
- A regulator pre-meet or exam request is asking for the gate package on a named GenAI use case.

Not the right tool when:
- The use case has not produced its upstream artifacts yet (drive intake, tier, model card, validation plan, prompt-injection, RAG-evaluation, vendor-evidence as applicable first).
- The use case is non-generative ML (use validation-plan with the standard model-risk close-out flow; this skill is GenAI-specific).
- The artifact required is the executive committee pre-read (use board-ai-risk-pack; this skill is the pre-prod gate review, not the committee summary).

Anchored to: SR 11-7 §III to V (governance, validation, controls applied at the pre-prod gate); OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026) [verify section on pre-implementation review]; NIST AI RMF 1.0 Map function and Manage 1.x (managing risks at deployment); NIST AI RMF Generative AI Profile (NIST AI 600-1) Map and Manage subcategories specific to GenAI; ISO/IEC 42001:2023 §8.x (operational controls and AI system lifecycle); EU AI Act Article 9 (risk management), Article 13 (transparency to deployers), Article 14 (human oversight), Article 26 (deployer obligations) where applicable.

## Source anchors

- SR 11-7 §III (governance, policies, controls), §IV (model risk rating), §V (validation, monitoring, controls) — the pre-prod gate exercises all three.
- OCC Bulletin 2026-13 (revised interagency model risk guidance, 2026) [verify section] — refreshed pre-implementation expectations including AI/ML and GenAI inclusion.
- FDIC FIL on revised interagency model risk management guidance, 2026 [verify section] — parallel pre-implementation expectations.
- NIST AI RMF 1.0 Map 5.1 (impact assessment), Manage 1.1 to 1.4 (managing risks at deployment), Manage 4.1 (deployment monitoring).
- NIST AI RMF Generative AI Profile (NIST AI 600-1) — Map and Manage subcategories specific to GenAI deployment readiness (foundation model dependencies, content provenance, hallucination posture, harmful content mitigation, dangerous capability containment) [verify exact subcategory numbering].
- ISO/IEC 42001:2023 §8.1 (operational planning), §8.3 (AI system lifecycle), §9.x (performance evaluation).
- EU AI Act Article 9 (risk management system), Article 13 (transparency for high-risk AI), Article 14 (human oversight), Article 15 (accuracy, robustness, cybersecurity), Article 26 (deployer obligations) — where the use case is a high-risk EU AI system.
- NYDFS Industry Letter on Cybersecurity Risks Arising from AI (October 2024) — pre-prod gate cyber expectations for covered entities.
- US Treasury Department report on Managing Artificial Intelligence-Specific Cybersecurity Risks in the Financial Services Sector (March 2024) [verify exact title and date] — informational reference for sector-specific pre-prod expectations.

## Sector overlays needed

- `references/sector-overlays/banking.md` — pre-prod gate expectations for banking GenAI (KYC assistants, RM assistants, compliance assistants); regulator overlap with OCC, FRB, FDIC pre-implementation review.
- `references/sector-overlays/insurance.md` — pre-prod gate expectations for insurance GenAI (claims assistants, underwriting assistants); NAIC Model Bulletin alignment, state department expectations.
- `references/sector-overlays/capital-markets.md` — pre-prod gate expectations for capital markets GenAI (research, surveillance, analyst assistants); SEC, FINRA, MAR adjacency.
- `references/sector-overlays/payments-fintech.md` — pre-prod gate expectations for payments and fintech GenAI; sponsor bank gate alignment.

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — NYDFS October 2024 alignment; pre-prod cyber gate items (identity, logging, IR readiness, prompt-injection posture).
- `references/cross-cutting/privacy.md` — pre-prod privacy gate items (data minimisation, retention, regulated NPI / PHI handling, consumer notice posture).
- `references/cross-cutting/conduct.md` — pre-prod conduct gate items (fairness, harmful content posture, complaint readiness).

Climate not applicable.

## Output template named sections

1. Gate metadata (use case ID, gate type, requested date, recommended decision date)
2. Recommended decision (go / go-with-conditions / hold / no-go), with one-paragraph rationale
3. Upstream artifact roll-up (status of intake, tier, model card, validation plan results, prompt-injection review, RAG evaluation, vendor evidence review; with last-updated dates and links)
4. Open conditions and named gates (what must close before go, with owners and SLAs)
5. Residual risk summary (top 3-5 named risks with likelihood, impact, accepted-risk owners)
6. Monitoring readiness (signals live before go-live, sampling cadence, escalation path)
7. Incident response readiness (procedures, regulator-notification triggers, drilled state)
8. Human oversight design (decision points, sampling expectation, evidence of effective oversight)
9. Foundation-model dependency posture (provider, version, swap-revalidation policy)
10. Sector and cross-cutting overlay sign-offs (named owners with status)
11. Sign-off block (named reviewers, dates, dissent if any)
12. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `gate_id` | string | Canonical gate ID. |
| `use_case_id` | string | Links to intake record. |
| `gate_type` | enum | `initial_release`, `material_expansion`, `recurring_revalidation`, `regulatory_response`. |
| `recommended_decision` | enum | `go`, `go_with_conditions`, `hold`, `no_go`. |
| `decision_rationale` | string | One paragraph, regulator-readable. |
| `upstream_artifacts` | array of objects | Each: artifact, status (current/stale/missing), last_updated, link. |
| `open_conditions` | array of objects | Each: condition, owner, SLA, severity. |
| `residual_risk` | array of objects | Each: risk, likelihood, impact, accepted_owner. |
| `monitoring_readiness` | array of objects | Each: signal, live_before_golive (bool), owner, escalation. |
| `ir_readiness` | object | Sub-fields: procedures_documented, last_drilled, regulator_notification_triggers. |
| `human_oversight` | object | Sub-fields: decision_points, sampling_expectation, effective_oversight_evidence. |
| `foundation_model_posture` | object | Sub-fields: provider, model, version, swap_policy. |
| `overlay_signoffs` | array of objects | Each: overlay (sector or cross-cutting), owner, status. |
| `signoff` | array of objects | Each: reviewer, role, date, position (signed/dissent), basis. |
| `source_trace` | array of objects | Claim, source, evidence reference, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. A US national bank's tier-1 GenAI assistant for KYC analysts is at initial-release pre-prod. Review pulls together: intake (current), tier (tier 1, current), model card (current), validation plan results (full validation with effective challenge questions resolved), prompt-injection review (residual risk medium with monitoring in place), RAG evaluation (faithfulness above threshold, citation precision above threshold), vendor evidence review (foundation model provider system card current, swap-revalidation policy documented). Recommended decision: go-with-conditions. Open conditions: drill IR procedure once before go-live; pin foundation model version for the first 90 days; weekly committee escalation on faithfulness sampling for the first 60 days. Sign-off includes AI risk committee secretary, model risk lead, head of cyber, head of compliance.

2. A regional life insurer's tier-2 GenAI claims summarisation assistant is at material-expansion pre-prod (expanding from one regional office to nationwide). Review pulls together: intake (refreshed), tier (re-tiered tier 2, current), model card (refreshed), validation plan results (targeted validation focused on cross-regional faithfulness and refusal posture), prompt-injection review (refreshed; indirect injection in scanned correspondence remains primary residual), RAG evaluation (refreshed; cross-claim leakage scoping retested), vendor evidence review (current). Recommended decision: hold. Open conditions: PHI cross-claim audit log retention extended to required state-by-state minima before go; complaint-channel readiness documented per state; AI risk committee secretary unsigned pending state-level sign-off from compliance.

## Common pitfalls

1. Gate review is performed without one or more upstream artifacts. The reviewer signs into a partial picture. Mitigation: required artifact-status block; any artifact `stale` or `missing` blocks `go` recommendation by policy.
2. Conditions are listed without owners or SLAs. Become forever-open. Mitigation: each open condition requires owner, SLA, and severity; missing fields fail the quality check.
3. Foundation-model posture is documented but the swap-revalidation policy is silent. The provider swaps the model post go-live and the firm has no agreed playbook. Mitigation: required `swap_policy` field with explicit revalidation trigger.
4. Sign-off is a single name. The committee assumes broader sign-off than exists. Mitigation: sign-off block requires named reviewers across model risk, cyber, compliance, and (where applicable) privacy and consumer-conduct.
5. The decision is "go" with a long list of conditions equivalent to "no-go in disguise". Mitigation: when conditions are material, the recommended decision is `go_with_conditions` or `hold`, not `go`; the rationale must state which conditions are blocking versus tracking.
