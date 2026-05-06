# Example: tiering decision for an internal-use GenAI research summariser at a broker-dealer

Public-source-derived. No named institution. Patterns drawn from NIST AI 600-1 Generative AI Profile (Map 1.1, Measure 2.6), public model and system card precedents from frontier labs as a documentation form factor, and the SEC Marketing Rule and books-and-records rule frame for adviser/BD AI use.

## Input description

A US broker-dealer has intaked a GenAI research-summarisation assistant for internal analyst use. The assistant ingests public earnings transcripts and the firm's own published research notes and produces structured summaries for the equity research desk. Output is internal only; no client-facing surface today. Vendor-hosted foundation model with version pinning, RAG over the firm's research note corpus and a vendor-supplied transcript corpus. No tools; no agentic behaviour; advisory-only. Sponsor (head of equity research) proposed tier-3.

Engagement scope provided by `engagement-scoping`:
- Institution type: broker-dealer (also dual-registered investment adviser), primary regulators SEC and FINRA.
- Persona: AI Governance Lead, second line, reporting to CCO.
- Sector overlay set: capital-markets. Cross-cutting overlays: cyber (vendor-hosted foundation model is a supply-chain surface), conduct (research integrity and Reg AC adjacency).
- Source posture: public-plus-firm-policy.

## Output sketch

Tier decision: **tier-3**.

Tier rationale (regulator-readable): use case is internal-only with no customer-binding output, no regulated NPI in inputs (public transcripts plus internal research notes), and no autonomous behaviour. Foundation-model dependence and Reg AC / Marketing Rule adjacency are the elevating factors; the tier holds at tier-3 with a hard re-tiering trigger if any output reaches a client-facing surface or is incorporated into a published research note without independent analyst review.

Per-factor scoring (abbreviated):

| Factor | Score | Weight | Notes |
|---|---|---|---|
| customer_impact | low | secondary | Internal use only; no customer-binding output. |
| financial_impact | low | secondary | Productivity tool; no balance-sheet or fee impact. |
| regulatory_impact | medium | contributing | SEC Marketing Rule reach if any output published; Rule 204-2 / 17a-4 books-and-records reach if output supports a recommendation; Reg AC research independence framing. |
| ai_act_category | n/a | secondary | US-only footprint; no EU client base for the relevant business line. |
| autonomy_level | low | secondary | Advisory only; analyst review between summary and any onward use. |
| data_sensitivity | low | secondary | Public transcripts plus internal research notes (confidential business data). No NPI. |
| model_concentration | low | secondary | Single use case, narrow scope. |
| vendor_dependence | medium | contributing | Vendor-hosted foundation model with version pinning; firm has change-of-version notice but model behaviour is partially outside firm control. |
| cyber_exposure | medium | contributing | Vendor supply-chain surface; prompt-injection from transcript content; NYDFS Part 500 reach for NY-licensed entity. |
| conduct_exposure | medium | contributing | Research integrity (Reg AC); MAR-adjacency on any forward-looking content; analyst-conduct posture. |
| genai_specific | medium | dominant | Foundation model, RAG, hallucination and citation-fabrication exposure. NIST AI 600-1 Measure 2.6 profile. |
| sector_specific | medium | contributing | Marketing Rule reach if any client-facing path opens; books-and-records reach. |

Triggered gates:
- Targeted validation focused on hallucination, citation precision, and refusal behaviour. Owner: model risk team. Frequency: pre-prod and semi-annual.
- AI governance lead approval (no AI risk committee escalation required at tier-3 under firm policy). Owner: AI Governance Lead. Frequency: one-time and on material change.
- Pre-prod gate. Owner: AI Governance Lead. Frequency: one-time.
- Vendor diligence light-touch (foundation-model vendor evidence review). Owner: vendor management with AI governance. Frequency: one-time and on vendor swap.

Validation depth: targeted. Monitoring frequency: semi-annual.
Committee route: AI Governance Lead with notification to model risk committee.

Re-tiering triggers:
- Output is incorporated into any client-facing material (research note published externally, marketing material, RFP response, client letter). Owner: head of equity research with CCO. Detection: change-management notice and quarterly Marketing Rule reach review.
- Input scope expands to non-public material (e.g., management commentary not yet public). Owner: research compliance. Detection: change-management notice.
- Vendor model swap or material version change. Owner: vendor management. Detection: vendor change-of-version notice.
- RAG corpus scope change (e.g., addition of trader chat archives, expert-network notes, alternative-data sources). Owner: AI Governance Lead. Detection: change-management notice.
- Any tool added to the assistant (e.g., trade-history retrieval, position-data lookup). Owner: AI Governance Lead. Detection: change-management notice.
- SEC final action on the predictive-data-analytics rulemaking, where in scope. Owner: regulatory change function. Detection: regulatory horizon scan.

Overlay flags: capital-markets, cyber, conduct.

AI Act overlap: false; routed_to_ai_act_triage = false. Flagged for re-look if EU client base added.

Dissent: none. Sponsor proposal of tier-3 is accepted.

Open questions:
- Books-and-records posture for AI-generated summaries that an analyst used in the formation of a recommendation is unsettled inside the firm. Owner: CCO and head of equity research; due before pre-prod gate. Tier holds at tier-3; the question affects controls and monitoring scope rather than the tier itself.

Source trace:
- Use case is internal-only — intake record §intended-use, high confidence.
- No regulated NPI in inputs — intake record §data sources, high confidence.
- Foundation-model dependence and version pinning — vendor-evidence pack and contract addendum, medium confidence (vendor-self-attestation).
- Marketing Rule reach posture — firm research compliance memo, medium confidence (memo is current but the published-output boundary is not yet operationalised as a control).
- NYDFS Part 500 reach — NY licensure, high confidence.

## Why this scenario matters

- It exercises the GenAI factor block. Foundation-model dependence, hallucination, citation fabrication, vendor swap, RAG corpus drift are scored explicitly. NIST AI 600-1 Measure 2.6 is the anchor; the tier rubric does not collapse to a pre-GenAI shape.
- It exercises the customer-impact-low + regulatory-adjacency-medium combination. Customer impact is the dominant tier-1 trigger when present; here it is absent and the tier holds at tier-3 despite regulatory adjacency.
- It exercises the re-tiering trigger discipline. Incorporation into client-facing material, scope expansion, tool addition, and a vendor swap are each named events with monitoring owners. The tier is defensible at the time of decision and re-defensible when scope grows.
- It exercises the no-dissent path. Sponsor proposal is accepted; the dissent block is empty rather than padded.
- It is the routing decision for downstream skills: model-card-builder gets `tier-3` and compresses sections accordingly; validation-plan gets `validation_depth = targeted`; agentic-ai-controls is not invoked (advisory only); llm-vendor-evidence-review is invoked at light-touch depth.
