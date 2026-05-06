# ai-use-case-intake — Phase 1 spec sheet

Date: 2026-05-06
Plugin: ai-governance-model-risk
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Turns a first-line AI use case description into a structured intake record that downstream second-line workflows (tiering, model card, validation plan, pre-prod review) can consume. Captures purpose, intended users, data sources, vendor and model dependencies, autonomy level, decision impact, human oversight points, and proposed review gates. The intake is the front door for everything else in this plugin.

Best for:
- A first-line owner has proposed an AI or model use case and second-line needs a single intake record before tier and review gate decisions.
- An AI inventory refresh requires consistent intake metadata across in-flight, in-production, and decommissioned use cases.

Not the right tool when:
- The use case is already intaked and the question is its risk tier (use ai-risk-tiering).
- The use case has already cleared intake and tiering and the next artifact is the model card (use model-card-builder).
- The work is procurement-stage diligence on an AI vendor before any internal use case exists (use vendor-diligence in third-party-operational-resilience with the AI vendor mode).

Anchored to: NIST AI RMF 1.0 Govern 1.6 and Map 1.1 to 1.6 (use case context, intended purpose, deployment setting); ISO/IEC 42001:2023 §6.1.2 and §8.1 (AI system impact assessment, operational planning); SR 11-7 §III (model definition and inventory); OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026) [verify section on inventory scope and AI inclusion]; EU AI Act (Regulation (EU) 2024/1689) Article 6 and Annex III (high-risk classification trigger fields).

## Source anchors

- SR 11-7 (FRB SR 11-7 / OCC 2011-12, supervisory guidance on model risk management) §III — model definition; model inventory expectations.
- OCC Bulletin 2026-13 (revised interagency model risk guidance, 2026) [verify section] — inclusion of AI/ML and generative AI within model definition; intake and inventory expectations.
- FDIC FIL on revised interagency model risk management guidance, 2026 [verify section] — parallel inventory and intake expectations.
- NIST AI RMF 1.0 Govern 1.6 (inventory), Map 1.1 to 1.6 (context, intended purpose, system categorization).
- NIST AI RMF Generative AI Profile (NIST AI 600-1) Govern 1.6, Map 1.1 — GenAI-specific intake metadata (foundation model dependence, prompt/RAG architecture, autonomy).
- ISO/IEC 42001:2023 §6.1.2 (AI system impact assessment), §7.5 (documented information), §8.1 (operational planning).
- EU AI Act (Regulation (EU) 2024/1689) Article 6 (high-risk classification), Annex III (high-risk use cases) — fields needed at intake to support later triage.
- NYDFS Industry Letter on Cybersecurity Risks Arising from AI (October 2024) [verify section] — intake fields covering AI-enabled threat surface and AI-touching data.

## Sector overlays needed

- `references/sector-overlays/banking.md` — credit decisioning, deposit operations, fraud and AML AI; intake fields for model owner unit, regulator overlap (OCC, FRB, FDIC, CFPB), CCAR/DFAST overlap.
- `references/sector-overlays/insurance.md` — pricing and underwriting AI, claims AI; intake fields for state insurance department exposure (NAIC Model Bulletin on the Use of AI Systems by Insurers, 2023), policyholder impact.
- `references/sector-overlays/capital-markets.md` — execution algos, surveillance models, research AI; intake fields for SEC/FINRA exposure, MAR/MiFID II overlap where applicable.
- `references/sector-overlays/payments-fintech.md` — onboarding AI, transaction monitoring AI; intake fields for sponsor bank relationship, BSA program coverage.

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — NYDFS October 2024 AI cybersecurity letter, NIST AI 600-1 Manage 2.7 (prompt injection); intake fields for AI-enabled threat surface (training-data poisoning exposure, prompt injection exposure, deepfake/social-engineering exposure).
- `references/cross-cutting/privacy.md` — GLBA Safeguards Rule, state privacy laws; intake fields for personal information categories, consumer notice posture, sensitive attributes used in model.
- `references/cross-cutting/conduct.md` — intake fields capturing customer-facing impact, fairness exposure, complaint surface.

Climate not applicable.

## Output template named sections

1. Use case identifier and version
2. Sponsor and accountable owner (first-line)
3. Business purpose and target outcome
4. Intended users and decision points
5. Decision impact (customer, financial, regulatory, operational)
6. Autonomy level (human-in-the-loop, human-on-the-loop, fully automated)
7. Model and AI architecture (in-house, vendor, foundation model, RAG, agentic)
8. Data sources and data sensitivity
9. Vendor and third-party dependencies
10. Regulatory exposure flags (US, EU, sector)
11. Proposed risk tier (preliminary)
12. Proposed review gates and human oversight points
13. Open questions for second-line follow-up
14. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `use_case_id` | string | Canonical ID for the use case (links to inventory). |
| `use_case_name` | string | Short human-readable name. |
| `business_unit` | string | Sponsor unit. |
| `accountable_owner` | string | First-line owner name and role (placeholder where unknown). |
| `purpose_statement` | string | One paragraph, plain language. |
| `intended_users` | array of strings | Internal staff, customers, third parties, agentic callers. |
| `decision_impact` | object | Sub-fields: customer_impact, financial_impact, regulatory_impact, operational_impact (each enum: none/low/medium/high). |
| `autonomy_level` | enum | `human_in_loop`, `human_on_loop`, `fully_automated`, `agentic_with_tool_use`. |
| `architecture` | object | Sub-fields: model_type (traditional, ML, foundation_model, agentic), deployment (in_house, vendor_api, on_prem), uses_rag (bool), uses_tools (bool). |
| `vendor_dependencies` | array of objects | Vendor name, role (model provider, hosting, data), criticality. |
| `data_sources` | array of objects | Source name, sensitivity (public, internal, confidential, regulated_PI, regulated_NPI), purpose (training, retrieval, evaluation). |
| `regulatory_flags` | array of strings | Tags such as `OCC_2026-13`, `EU_AI_Act_Annex_III`, `NYDFS_Part_500`, `CFPB_adverse_action`. |
| `preliminary_tier` | enum | `tier_1` to `tier_4`, plus `unclassified`. |
| `review_gates` | array of objects | Gate name, criteria, required reviewer, stop condition. |
| `open_questions` | array of strings | Each tagged with which downstream skill needs the answer. |
| `source_trace` | array of objects | Claim, source, evidence reference, confidence label. |

## Example scenarios (public-source-derived, anonymous)

1. Mid-size US bank wants to deploy a foundation-model-based assistant for relationship managers to draft client-meeting prep notes from internal CRM data and recent public earnings calls. Intake captures: customer-facing exposure indirectly (RM uses output, not customer), foundation model vendor dependency, RAG over internal CRM and external earnings transcripts, autonomy human-in-the-loop, regulatory flags for OCC 2026-13 model definition, NYDFS Part 500 cyber, GLBA on customer info that may surface in retrieval. Preliminary tier proposed at tier 2 pending tiering skill review.

2. Regional life insurer is piloting an ML-based mortality risk score for underwriting acceleration. Intake captures: customer-facing decision (binding, with adverse action implications via state insurance fairness rules and NAIC Model Bulletin on Use of AI Systems by Insurers, 2023), in-house model trained on third-party clinical and prescription data, no foundation model, autonomy human-in-the-loop with auto-accept threshold for low-risk applicants. Regulatory flags for state insurance departments, NAIC Model Bulletin, ECOA-equivalent fairness expectations. Preliminary tier proposed at tier 1 pending tiering skill review.

## Common pitfalls

1. Intake captures the system as built today and misses the planned roadmap. Tier and gates set on a moving target. Mitigation: required field for "next twelve-month change plan" with named owner.
2. Autonomy level recorded as "human-in-the-loop" because there is a button somewhere, even though the human review is rubber-stamped at scale. Mitigation: require evidence of effective human oversight (NIST Map 3.5, EU AI Act Article 14) at intake or flag as open question.
3. Foundation model dependency missed because the use case is described as "an internal AI tool". Mitigation: required field for foundation model identity and version, including pinned versus floating.
4. Data sensitivity recorded at the source level, not the field level. A "CRM extract" intake hides regulated NPI inside an otherwise internal data source. Mitigation: require field-level sensitivity tagging for any source flagged regulated.
5. Intake is treated as a one-time form, not a living record. Drifts within a quarter. Mitigation: required `last_reviewed_date` and `next_review_due` with link to the change plan field.
