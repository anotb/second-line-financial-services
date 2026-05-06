# ai-risk-tiering — Phase 1 spec sheet

Date: 2026-05-06
Plugin: ai-governance-model-risk
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Assigns a risk tier to an AI or model use case using a defensible, multi-factor rubric. Consumes the intake record and produces a tier with reasons, the named gates that the tier triggers, and the validation depth the tier requires. The tier is the routing decision for the rest of model risk and AI governance.

Best for:
- An intake record exists and second-line needs to set the tier before deciding validation depth, monitoring frequency, and committee path.
- A periodic re-tiering exercise on the AI inventory after a change in use case scope, autonomy, customer exposure, or vendor.

Not the right tool when:
- The use case has not been intaked yet (use ai-use-case-intake first).
- The question is whether the use case is high-risk under the EU AI Act specifically (use ai-act-triage; the AI Act has a regulation-driven classification, not a firm-defined rubric).
- The question is the validation plan itself, not the tier (use validation-plan).

Anchored to: SR 11-7 §IV (model risk rating); OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026) [verify section on risk rating and tiering]; NIST AI RMF 1.0 Map 5.1 (impact assessment), Measure 2.6 (risk levels); NIST AI RMF Generative AI Profile (NIST AI 600-1) Map 1.1, Measure 2.6; ISO/IEC 42001:2023 §6.1.2 (AI system impact assessment).

## Source anchors

- SR 11-7 §IV — model risk rating, materiality, and risk-based supervision principle.
- OCC Bulletin 2026-13 (revised interagency model risk guidance, 2026) [verify section] — risk-rating expectations, AI/ML inclusion, tier-driven validation depth.
- FDIC FIL on revised interagency model risk management guidance, 2026 [verify section] — parallel risk-rating expectations.
- NIST AI RMF 1.0 Map 5.1 (impact assessment), Measure 2.6 (risk levels and tolerances).
- NIST AI RMF Generative AI Profile (NIST AI 600-1) Map 1.1 (use case context for GenAI), Measure 2.6 (risk levels for GenAI specifically).
- ISO/IEC 42001:2023 §6.1.2 (AI system impact assessment).
- EU AI Act Article 6 and Annex III (informational only — formal AI Act classification belongs to ai-act-triage; flag overlap at tier 1 / high-risk).
- NYDFS Industry Letter on Cybersecurity Risks Arising from AI (October 2024) [verify section] — cyber materiality factors that should weight up the tier.

## Sector overlays needed

- `references/sector-overlays/banking.md` — credit, AML, fraud, deposit operations tiering nuances; CCAR/DFAST and OCC HSL list materiality.
- `references/sector-overlays/insurance.md` — pricing and underwriting tier weighting, claims AI tiering; NAIC Model Bulletin on Use of AI Systems by Insurers, 2023 framing.
- `references/sector-overlays/capital-markets.md` — execution algo, market-making, surveillance tiering; SEC Rule 15c3-5 (market access) and FINRA supervisory expectations as weight-up factors.
- `references/sector-overlays/payments-fintech.md` — onboarding, transaction monitoring, decisioning tiering; sponsor bank relationship as a weight-up factor.

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — NYDFS October 2024 AI cyber letter; tier-up factors for prompt injection exposure, training data poisoning exposure, and AI-enabled social engineering exposure.
- `references/cross-cutting/privacy.md` — tier-up factors for processing of regulated NPI, sensitive consumer data, biometric data.
- `references/cross-cutting/conduct.md` — tier-up factors for customer-binding decisions, fairness exposure, complaint vector.

Climate not applicable.

## Output template named sections

1. Use case reference and version
2. Tier decision (tier 1 / 2 / 3 / 4)
3. Tiering rubric scoring with per-factor justification
4. Triggered gates (validation depth, monitoring frequency, committee route, vendor diligence depth)
5. Sector and cross-cutting overlay flags
6. Re-tiering triggers (named events that force a re-look)
7. Open questions and dissent
8. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `use_case_id` | string | Links to intake record. |
| `tier` | enum | `tier_1`, `tier_2`, `tier_3`, `tier_4`. |
| `tier_rationale` | string | Two to four sentences, regulator-readable. |
| `factors` | array of objects | Each: factor name, score, weight, justification, source reference. |
| `triggered_gates` | array of objects | Gate name, owner, frequency, stop condition. |
| `validation_depth` | enum | `full`, `targeted`, `light_touch`, `monitor_only`. |
| `monitoring_frequency` | enum | `monthly`, `quarterly`, `semi_annual`, `annual`. |
| `committee_route` | string | Named committee that owns approval. |
| `re_tiering_triggers` | array of strings | Named events that require re-tiering. |
| `overlay_flags` | array of strings | Sector and cross-cutting overlays applied. |
| `dissent` | array of objects | Reviewer, position, basis. |
| `source_trace` | array of objects | Claim, source, evidence reference, confidence label. |

## Example scenarios (public-source-derived, anonymous)

1. A US national bank intaked a generative AI assistant for KYC analysts that drafts narrative for periodic refresh files using internal customer data and OFAC list metadata. Tiering surfaces: customer-binding indirectly (analyst review remains, but at scale the human review may not be effective), regulated NPI in retrieval, AML control surface (FFIEC BSA/AML manual exposure), foundation model vendor dependency, NYDFS cyber exposure. Tier proposed at tier 1 with gates: full validation, quarterly monitoring of grounding and refusal behavior, AI risk committee approval before any expansion to non-KYC narrative.

2. A capital markets broker-dealer intaked a research summarization assistant restricted to public earnings transcripts and analyst notes, output for internal use only. Tiering surfaces: no customer-binding, no regulated NPI, foundation model vendor dependency, research conduct exposure, MAR/Reg AC adjacency. Tier proposed at tier 3 with gates: targeted validation focused on hallucination and fabrication, semi-annual monitoring, model risk team approval (no committee escalation required), with re-tiering trigger if output is ever published externally or used in client-facing materials.

## Common pitfalls

1. Tiering rubric collapses to a single dominant factor (usually customer impact) and ignores cyber, conduct, and concentration. Mitigation: require all named factors to be scored, with `n/a` justified, not blank.
2. Tier inflation or deflation by sponsor pressure. The sponsor wants tier 3 to skip validation depth. Mitigation: dissent field is required when tier disagrees with sponsor proposal; AI risk committee secretary signs the dissent line.
3. Re-tiering triggers are defined and forgotten. The use case grows beyond its tier without re-tiering. Mitigation: re-tiering triggers must include named events with monitoring owners, not just dates.
4. GenAI-specific factors (foundation model swap risk, prompt injection exposure, RAG corpus drift) are missing from a rubric designed for pre-GenAI ML. Mitigation: reference NIST AI 600-1 Measure 2.6 and ensure GenAI factor block is present.
5. Tier 1 set by reflex for anything customer-facing. Tier 1 then becomes meaningless because everything is tier 1. Mitigation: tier 1 reserved for customer-binding decisions or material financial impact; require justification against named threshold.
