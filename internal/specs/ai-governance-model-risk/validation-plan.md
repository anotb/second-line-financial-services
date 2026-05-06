# validation-plan — Phase 1 spec sheet

Date: 2026-05-06
Plugin: ai-governance-model-risk
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Drafts a validation plan for an AI or model use case, sized to its tier. Names the conceptual soundness work, the data and design review, the outcomes analysis, the ongoing monitoring scope, and the effective challenge questions. Output is the contract between the validator and the model owner before testing starts.

Best for:
- A use case has cleared intake and tiering and validation is the next step before pre-prod or production approval.
- An annual revalidation cycle requires a tailored plan for an in-production model rather than a copy-paste of last year's plan.
- A new vendor or foundation model is being swapped into an existing use case and the revalidation plan needs to scope the delta.

Not the right tool when:
- Validation has already executed and the work is the validation report write-up (use the report skill in the validation agent plugin in phase 3, not this plan-stage skill).
- The use case has not been intaked or tiered (use ai-use-case-intake or ai-risk-tiering).
- The artifact required is the full pre-prod gate review across people, process, and technology controls (use genai-pre-prod-review for GenAI; this plan is the validator-side scope only).

Anchored to: SR 11-7 §V (validation activities: conceptual soundness, ongoing monitoring, outcomes analysis); OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026) [verify section on validation depth and effective challenge]; NIST AI RMF 1.0 Measure function (Measure 2.1 to 2.13); NIST AI RMF Generative AI Profile (NIST AI 600-1) Measure subcategories on hallucination, harmful content, and information integrity; ISO/IEC 42001:2023 §9.1 (monitoring, measurement, analysis, evaluation).

## Source anchors

- SR 11-7 §V — three validation pillars: conceptual soundness; ongoing monitoring; outcomes analysis. Effective challenge expectations.
- OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026) [verify section] — refreshed validation depth tiers, AI/ML inclusion, GenAI applicability.
- FDIC FIL on revised interagency model risk management guidance, 2026 [verify section] — parallel validation expectations.
- NIST AI RMF 1.0 Measure 2.1 to 2.13 — testable properties (validity, reliability, safety, security and resilience, accountability and transparency, explainability and interpretability, privacy, fairness with harmful bias managed, environmental impact).
- NIST AI RMF Generative AI Profile (NIST AI 600-1) Measure subcategories — GenAI-specific testable properties (Measure 1.1 hallucination/confabulation, Measure 2.7 prompt injection, Measure 2.9 information integrity, Measure 2.11 harmful content, Measure 2.12 dangerous capabilities, Measure 2.13 information security) [verify exact numbering].
- ISO/IEC 42001:2023 §9.1 (monitoring), §9.2 (internal audit), §9.3 (management review).
- EU AI Act Article 9 (risk management), Article 15 (accuracy, robustness, cybersecurity) — used where the model is a high-risk EU AI system.

## Sector overlays needed

- `references/sector-overlays/banking.md` — credit model validation tests (KS, AUC, segment performance, override analysis, bureau-data dependence); AML/fraud model validation (above-threshold review, productivity, tuning re-baseline).
- `references/sector-overlays/insurance.md` — pricing and underwriting validation (segmental loss ratios, indication-vs-charged, NAIC Model Bulletin alignment); claims AI validation (faithfulness, fairness across geographies and demographics).
- `references/sector-overlays/capital-markets.md` — execution algo validation (slippage, market impact, kill-switch testing; SEC Rule 15c3-5 alignment); surveillance model validation (precision/recall, alert quality).
- `references/sector-overlays/payments-fintech.md` — transaction monitoring validation; onboarding decisioning validation under sponsor bank framework.

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — validation tests for prompt injection, data poisoning, model extraction; alignment with NYDFS October 2024 AI cyber letter.
- `references/cross-cutting/privacy.md` — validation tests for PII memorisation, training-data leak, retrieval over inappropriate corpora.
- `references/cross-cutting/conduct.md` — validation tests for fairness, harmful content, customer impact.

Climate not applicable.

## Output template named sections

1. Plan metadata (model ID, version, tier, validator, scope date)
2. Validation depth (full / targeted / light-touch / monitor-only) with tier-based justification
3. Conceptual soundness scope (theory, design choices, alternatives considered, foundation model selection rationale)
4. Data review scope (training data, evaluation data, retrieval corpora, lineage, fitness for purpose)
5. Performance and outcomes analysis scope (named tests, success criteria, segment cuts)
6. Robustness, adversarial, and stress testing scope (including prompt injection and jailbreak for GenAI)
7. Fairness, explainability, and transparency scope
8. Ongoing monitoring scope (metrics, thresholds, frequency, owners)
9. Effective challenge questions (named, with the model owner's expected response evidence)
10. Dependencies and prerequisites (data access, environment, vendor evidence, foundation model card)
11. Timeline, owner, deliverables
12. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `model_id` | string | Canonical model ID and version. |
| `tier` | enum | Tier from ai-risk-tiering. |
| `validation_depth` | enum | `full`, `targeted`, `light_touch`, `monitor_only`. |
| `conceptual_soundness` | object | Scope items, methods, success criteria. |
| `data_review` | object | Scope items, methods, success criteria. |
| `outcomes_analysis` | array of objects | Each: test name, method, dataset, success criterion, owner. |
| `robustness_testing` | array of objects | Each: attack class, method, success criterion, owner. |
| `fairness_explainability` | array of objects | Each: dimension, method, success criterion. |
| `monitoring` | array of objects | Each: metric, threshold, frequency, owner, escalation_path. |
| `effective_challenge_questions` | array of objects | Each: question, expected_evidence, owner of response. |
| `dependencies` | array of strings | Prerequisites and access needs. |
| `timeline` | object | Start, milestones, end, deliverables. |
| `source_trace` | array of objects | Claim, source, evidence reference, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. Tier-1 in-house consumer-credit underwriting model annual revalidation. Validation depth: full. Conceptual soundness scope: theory, segmentation choice, alternative models considered, override policy. Data review scope: bureau attribute fitness, time-window, exclusions. Outcomes analysis scope: KS, AUC, capture-rate by FICO band and by region, override outcomes versus policy. Fairness scope: ECOA/Reg B disparity testing across protected classes, with disparity ratios reported and explained. Monitoring scope: PSI on inputs, score drift, decisioning-rate drift, complaint-rate drift, monthly cadence. Effective challenge questions: what is the policy on proxies, what is the rationale for the current segmentation cuts, when does the model retire.

2. Tier-2 vendor-hosted GenAI claim-summary assistant initial validation. Validation depth: targeted. Conceptual soundness scope: foundation model selection rationale, RAG architecture review, prompt design review, tool boundary review (no auto-decisioning). Data review scope: claim file documents, retention, retrieval grounding controls. Outcomes analysis scope: faithfulness, citation precision, refusal rate on out-of-scope queries, hallucination rate against held-out claim files. Robustness scope: prompt injection adversarial test against indirect injection in scanned correspondence, jailbreak attempts to extract PHI on unrelated claimants, vendor model-version swap drill. Fairness scope: faithfulness and refusal across regional and demographic claim cohorts. Monitoring scope: faithfulness sampling, refusal rate, prompt-injection signal monitoring, complaint code monitoring. Effective challenge questions: what is the escape path if vendor swaps the underlying foundation model without notice, what is the detection cadence for a slow drift in faithfulness, who owns the kill switch.

## Common pitfalls

1. Validation depth set to "full" by reflex for any tier 1 model without scoping which pillars actually change for an AI/ML model versus a traditional model. Mitigation: depth is set per pillar (CS, OA, OM), not as a single label.
2. Effective challenge questions written as compliance theatre ("does the model meet our policy"). Real effective challenge probes the design choice, the assumption, and the failure mode. Mitigation: each effective-challenge entry must name the design choice or assumption it interrogates.
3. GenAI plans treat the foundation model as a black box and skip conceptual soundness on the vendor model. Validators should review the vendor's published system card and red-team results as part of conceptual soundness, even if they cannot retrain. Mitigation: required `vendor_model_card_review` step where foundation model is third-party.
4. Robustness scope misses the most relevant attack class. For RAG, indirect prompt injection in retrieved content. For agentic, tool misuse and goal hijack. For traditional ML, adversarial input only. Mitigation: attack-class catalogue tied to architecture flags.
5. Monitoring scope copy-pasted from the model card without re-grounding to the validator's perspective. Validator monitoring is what triggers re-validation, not just operational alerts. Mitigation: each monitoring entry has an explicit `revalidation_trigger` flag.
