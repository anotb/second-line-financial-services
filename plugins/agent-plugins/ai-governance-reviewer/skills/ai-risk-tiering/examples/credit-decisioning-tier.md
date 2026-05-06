# Example: tiering decision for an in-house consumer credit-decisioning ML model

Public-source-derived. No named institution. Patterns drawn from CFPB Circular 2022-03 (adverse action notification requirements when using AI or complex algorithms), CFPB Circular 2023-03, and SR 11-7 §IV materiality framing.

## Input description

A US bank holding company has intaked a refresh of an existing gradient-boosted classifier for consumer auto-loan underwriting in the indirect dealer channel. The intake record names the use case as customer-binding (the model is the principal driver of the credit decision in the indirect channel), regulated NPI in inputs, US-only operating footprint, vendor-supplied bureau data feed but firm-built model. The sponsor (head of consumer lending) has proposed tier-2 to keep validation depth manageable.

Engagement scope provided by `engagement-scoping`:
- Institution type: bank holding company, mid-cap, primary regulators OCC and CFPB.
- Persona: head of model risk, second line.
- Sector overlay set: banking. Cross-cutting overlays: privacy (regulated NPI under GLBA), conduct (consumer-credit decisioning, ECOA / Reg B reach).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.

## Output sketch

Tier decision: **tier-1**.

Tier rationale (regulator-readable): the use case is customer-binding (model output is the principal driver of an adverse-action-eligible credit decision in the indirect channel) with material financial exposure (auto-loan portfolio in the multi-billion range) and direct ECOA / Reg B and CFPB reach. The Heightened Standards risk-appetite framework reaches the model. Sponsor proposed tier-2; second line dissents and books tier-1.

Per-factor scoring (abbreviated):

| Factor | Score | Weight | Notes |
|---|---|---|---|
| customer_impact | high | dominant | Customer-binding adverse action, indirect channel scale. |
| financial_impact | high | contributing | Multi-billion portfolio, loss-given-default sensitivity. |
| regulatory_impact | high | dominant | ECOA / Reg B; CFPB Circulars 2022-03 and 2023-03 on AI adverse action; OCC primary regulator. |
| ai_act_category | n/a | secondary | US-only footprint; flagged for monitoring if EU operations open. |
| autonomy_level | medium | contributing | Decisioning is automated, with override workflow but at scale override is rare. |
| data_sensitivity | high | contributing | GLBA NPI, bureau attributes, application form data. |
| model_concentration | medium | contributing | Single decisioning model in indirect channel; no challenger in production. |
| vendor_dependence | low | secondary | Vendor bureau data only; model is firm-built. |
| cyber_exposure | low | secondary | No customer-facing surface; serving environment internal. |
| conduct_exposure | high | dominant | Customer-binding, ECOA-relevant disparate-impact exposure, complaint vector. |
| genai_specific | n/a | secondary | Traditional ML; no foundation model, no RAG, no tools. |
| sector_specific | high | contributing | OCC Heightened Standards, ECOA / Reg B, FCRA adverse action. |

Triggered gates:
- Full validation (independent), owner: model risk validation, frequency: pre-prod and annual.
- AI risk committee approval at tier-1, owner: AI risk committee secretary, frequency: one-time and on material change.
- Pre-prod gate, owner: head of model risk, frequency: one-time.
- Quarterly monitoring pack to model risk committee, owner: model owner with consumer compliance for complaint and adverse-action-quality content.

Validation depth: full. Monitoring frequency: quarterly.
Committee route: AI risk committee with model risk committee technical review.

Re-tiering triggers:
- Expansion to direct-to-consumer channel (current scope is indirect only). Owner: head of consumer lending. Detection: change-management notice.
- Material change in adverse-action notice generation method. Owner: consumer compliance. Detection: change-management notice plus quarterly monitoring pack.
- Performance breach for two consecutive quarters on segment-level approval-rate disparity. Owner: model owner. Detection: monitoring pack.
- Regulatory change to ECOA / Reg B adverse action standard, including any new CFPB Circular on algorithmic credit decisioning. Owner: regulatory change function. Detection: regulatory horizon scan.

Overlay flags: banking, privacy, conduct.

AI Act overlap: false; routed_to_ai_act_triage = false (no EU operations). Flagged for re-look if footprint changes.

Dissent: model risk dissents from sponsor's tier-2 proposal. Basis: customer-binding decisioning at this scale is tier-1 under firm policy; sponsor's tier-2 framing rests on the override workflow as a control, but override rates are below 3% portfolio-wide and override does not change the binding character of the initial decision. Recorded; AI risk committee secretary signs the dissent line.

Open questions:
- The new state-footprint expansion (three states added in the refresh) lacks adequate training coverage. Tier holds at tier-1; the open question is whether the segment-flag fires reliably at decision time and whether the open-state-footprint posture warrants temporary monitor-only treatment for those three states. Owner: model owner; due before pre-prod gate.

Source trace:
- Use case is customer-binding — intake record §intended-use, high confidence.
- Multi-billion portfolio scale — finance system pull, high confidence.
- ECOA / Reg B reach — public regulatory citation (CFPB Circulars), high confidence.
- Sponsor proposal of tier-2 — sponsor email of YYYY-MM-DD, high confidence.
- Override rate < 3% — monitoring pack 2025-Q4, high confidence.

## Why this scenario matters

- It exercises the dominant-factor discipline. Customer impact, regulatory impact, and conduct exposure all score high. The tier decision rests on three factors, not one; an inflation by reflex (everything customer-facing is tier-1) is replaced by a defended decision against named factors.
- It exercises the dissent block. The sponsor's tier-2 proposal is recorded and overridden with basis. This is the mechanism that prevents tier deflation by sponsor pressure.
- It exercises the re-tiering triggers as named events with monitoring owners, not just dates. The state-footprint and adverse-action-method triggers are exactly the ones that historically move a model out of its tier without a re-look.
- It exercises the AI Act overlap routing. US-only footprint today; flagged for re-look if EU operations open; not double-routed to ai-act-triage.
- It is the routing decision for downstream skills: model-card-builder gets `tier-1` and produces a deep card; validation-plan gets `validation_depth = full`; agentic-ai-controls is not invoked (no autonomous behaviour); board-ai-risk-pack consumes the tier and gates.
