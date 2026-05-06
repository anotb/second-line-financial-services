# model-card-builder — Phase 1 spec sheet

Date: 2026-05-06
Plugin: ai-governance-model-risk
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Drafts a model card for an AI or model use case in a financial-services firm. The model card is the canonical second-line artifact summarising intended use, training and reference data, performance, limitations and known failure modes, monitoring plan, controls, and sign-off questions. Single source of truth for governance committees, validators, internal audit, and exam responses.

Best for:
- A first-line owner has proposed an AI use case and second-line needs the model card before a tier decision or pre-prod gate.
- A model risk team is refreshing model cards as part of an annual model inventory exercise.
- A new vendor model is replacing an existing model and the card needs to be updated to reflect the swap.

Not the right tool when:
- The use case has not been intaked yet (use ai-use-case-intake first).
- Validation testing has not run and there are no performance results to summarise (use validation-plan; the model card consumes its outputs).
- The artifact required is the technical documentation file under EU AI Act Annex IV — that is the provider-side documentation set, not the firm-side model card. (Use ai-act-triage to scope Annex IV deltas; the model card sits alongside but does not replace Annex IV.)

Anchored to: SR 11-7 §V (model documentation expectations); OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026) [verify section on model documentation]; NIST AI RMF 1.0 Map and Measure functions; NIST AI RMF Generative AI Profile (NIST AI 600-1) Map 1.1 and Measure 2.x; ISO/IEC 42001:2023 §7.5 (documented information).

## Source anchors

- SR 11-7 §V — model documentation: scope, theory and design, data, testing, performance, limitations, change control.
- OCC Bulletin 2026-13 (revised interagency model risk guidance, 2026) [verify section] — refreshed documentation expectations including AI/ML and GenAI inclusion.
- FDIC FIL on revised interagency model risk management guidance, 2026 [verify section] — parallel documentation expectations.
- NIST AI RMF 1.0 Map 1.1 (intended purpose and context), Map 2.1 (system categorisation), Measure 2.x (performance metrics, robustness, fairness, explainability), Manage 3.x (deployment monitoring).
- NIST AI RMF Generative AI Profile (NIST AI 600-1) Map and Measure subcategories specific to GenAI (data provenance, hallucination metrics, content provenance).
- ISO/IEC 42001:2023 §7.5 (documented information), §8.1 (operational planning).
- EU AI Act Article 11 and Annex IV — informational reference; firm-side card is distinct from provider Annex IV.
- Public model and system card precedents from frontier labs (Anthropic Claude system cards, OpenAI system cards, Google Gemini cards) used as a documentation pattern reference (no firm-specific facts copied; pattern only).

## Sector overlays needed

- `references/sector-overlays/banking.md` — fields for credit decisioning model cards (regulator, ECOA/Reg B adverse action surface, CCAR/DFAST overlap), AML/fraud model cards (FFIEC manual exposure).
- `references/sector-overlays/insurance.md` — fields for pricing and underwriting model cards (NAIC Model Bulletin on Use of AI Systems by Insurers, 2023, state insurance fairness rules), claims AI model cards.
- `references/sector-overlays/capital-markets.md` — fields for execution algo model cards (SEC Rule 15c3-5 controls, FINRA supervisory expectations), surveillance model cards.
- `references/sector-overlays/payments-fintech.md` — fields for transaction monitoring and onboarding decisioning cards.

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — model card cyber section: training data integrity controls, model serving environment, prompt injection exposure for GenAI cards, NYDFS AI cyber letter (October 2024) alignment.
- `references/cross-cutting/privacy.md` — model card data section: regulated NPI use, GLBA Safeguards alignment, retention.
- `references/cross-cutting/conduct.md` — model card limitations section: known fairness exposures, complaint surface, customer-impact framing.

Climate not applicable.

## Output template named sections

1. Card metadata (model ID, version, owner, date, tier, classification)
2. Intended use (purpose, scope, intended users, in-scope decisions)
3. Out-of-scope use (explicit non-uses)
4. System description (architecture, components, dependencies, foundation model dependence and version, RAG corpus, tools)
5. Training and reference data (sources, sensitivity, licensing, retention, lineage)
6. Performance summary (named metrics with values, including segment-level results)
7. Robustness and stress testing (named tests with results, including adversarial and prompt injection where applicable)
8. Fairness and explainability (results, methods used, limitations of those methods)
9. Limitations and known failure modes (concrete, with examples)
10. Monitoring plan (metrics, thresholds, frequency, owners, escalation path)
11. Controls (preventive, detective, response; named owners)
12. Change management (change types and re-validation triggers)
13. Sign-off questions (questions a reviewer should ask before approving)
14. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `model_id` | string | Canonical model ID and version. |
| `use_case_id` | string | Links to intake record. |
| `tier` | enum | Tier from ai-risk-tiering. |
| `intended_use` | object | Sub-fields: purpose, intended_users, in_scope_decisions, out_of_scope_decisions. |
| `architecture` | object | Sub-fields: model_type, foundation_model (provider, name, version, pinned_or_floating), uses_rag, rag_corpus, uses_tools, tool_inventory. |
| `data` | array of objects | Each: source, sensitivity, purpose (training/retrieval/eval), licensing, retention, lineage. |
| `performance` | array of objects | Each: metric, value, segment, evaluation set, date, owner. |
| `robustness_tests` | array of objects | Each: test name, method, result, owner, date. |
| `fairness_results` | array of objects | Each: protected dimension, metric, value, disparity assessment. |
| `explainability` | object | Method, scope, limitations. |
| `limitations` | array of strings | Concrete failure modes with example. |
| `monitoring` | array of objects | Each: metric, threshold, frequency, owner, escalation_path. |
| `controls` | array of objects | Each: control, type (preventive/detective/response), owner, evidence_pointer. |
| `change_management` | array of objects | Each: change type, re-validation trigger, approver. |
| `signoff_questions` | array of strings | Reviewer questions, each tagged to a section. |
| `source_trace` | array of objects | Claim, source, evidence reference, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. Mid-size US bank refreshes the model card for an in-house gradient-boosted model used to score consumer auto-loan applications. Card sections: intended use (auto-loan underwriting decisioning, US-only, indirect channel out of scope), data (regulated NPI: bureau attributes, application data; no alternative data), performance (AUC, KS by FICO band, by region), fairness (adverse action coding rate by protected class with disparity ratios, ECOA/Reg B alignment), limitations (thin-file applicants, post-bankruptcy applicants), monitoring (PSI on input features, score drift, decisioning-rate drift, complaint-rate drift), controls (challenger model, override sampling, monthly performance pack), signoff questions (what is the trigger to re-fit, what is the policy for proxy variables identified after deployment).

2. Regional US insurer drafts the first model card for a vendor-hosted GenAI assistant used by claim adjusters to summarise medical records and prior correspondence. Card sections: intended use (claims-handling productivity, no auto-decisioning), architecture (foundation model from named vendor, RAG over claim file documents, no tools), data (PHI under HIPAA, claim file documents, retention bounded to claim lifecycle), performance (faithfulness, citation precision, refusal rate on out-of-scope queries), robustness (prompt injection adversarial test results, jailbreak test results), limitations (assistant cannot cite external statute, recency of records, dialect coverage), monitoring (faithfulness sampling, complaint code monitoring, prompt-injection signal monitoring), controls (human review of all assistant output before any claim communication, log retention, vendor change-of-version notice), signoff questions (what happens if the vendor swaps the underlying model, what is the escape path if a hallucinated medical fact reaches a payment decision).

## Common pitfalls

1. Card fills the template but the "limitations" section is generic platitudes ("model may not generalise to new populations"). A reviewer learns nothing. Mitigation: limitations require concrete failure modes with at least one example each.
2. Performance section reports a single headline metric with no segment-level breakdown. Hides discriminatory or regional underperformance. Mitigation: required segment-level reporting on protected and policy-relevant dimensions, even if performance is acceptable.
3. GenAI cards inherit a structure designed for traditional ML and miss foundation-model dependency, prompt injection, RAG corpus drift, and content provenance. Mitigation: GenAI overlay block is required when architecture flags `foundation_model` or `uses_rag` or `uses_tools`.
4. Monitoring section is a list of metrics with no thresholds, owners, or escalation paths. Monitoring exists on paper, not in the operating cadence. Mitigation: each monitoring entry requires threshold, owner, and escalation path; missing fields fail the quality check.
5. Card is updated only at validation cycles. The system changes underneath it (foundation model swap, RAG corpus expansion, prompt change). Mitigation: change-management table with named re-validation triggers; foundation-model version swap is always a re-validation trigger.
