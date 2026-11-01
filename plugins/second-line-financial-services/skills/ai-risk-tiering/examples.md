# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## credit-decisioning-tier

### Example: tiering decision for an in-house consumer credit-decisioning ML model

Public-source-derived. No named institution. Patterns drawn from Reg B §1002.9 (adverse action specificity; CFPB Circulars 2022-03 and 2023-03 informed earlier framing but were withdrawn May 12, 2025; the obligation survives on the regulation and Staff Commentary) and SR 11-7 §IV materiality framing.

#### Input description

A US bank holding company has intaked a refresh of an existing gradient-boosted classifier for consumer auto-loan underwriting in the indirect dealer channel. The intake record names the use case as customer-binding (the model is the principal driver of the credit decision in the indirect channel), regulated NPI in inputs, US-only operating footprint, vendor-supplied bureau data feed but firm-built model. The sponsor (head of consumer lending) has proposed tier-2 to keep validation depth manageable.

Engagement scope provided by `scoping`:
- Institution type: bank holding company, mid-cap, primary regulators OCC and CFPB.
- Persona: head of model risk, second line.
- Sector overlay set: banking. Cross-cutting overlays: privacy (regulated NPI under GLBA), conduct (consumer-credit decisioning, ECOA / Reg B reach).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.

#### Output sketch

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

#### Why this scenario matters

- It exercises the dominant-factor discipline. Customer impact, regulatory impact, and conduct exposure all score high. The tier decision rests on three factors, not one; an inflation by reflex (everything customer-facing is tier-1) is replaced by a defended decision against named factors.
- It exercises the dissent block. The sponsor's tier-2 proposal is recorded and overridden with basis. This is the mechanism that prevents tier deflation by sponsor pressure.
- It exercises the re-tiering triggers as named events with monitoring owners, not just dates. The state-footprint and adverse-action-method triggers are exactly the ones that historically move a model out of its tier without a re-look.
- It exercises the AI Act overlap routing. US-only footprint today; flagged for re-look if EU operations open; not double-routed to ai-act-triage.
- It is the routing decision for downstream skills: model-card-builder gets `tier-1` and produces a deep card; validation-plan gets `validation_depth = full`; agentic-ai-controls is not invoked (no autonomous behaviour); board-ai-risk-pack consumes the tier and gates.

## genai-internal-tool-tier

### Example: tiering decision for an internal-use GenAI research summariser at a broker-dealer

Public-source-derived. No named institution. Patterns drawn from NIST AI 600-1 Generative AI Profile (Map 1.1, Measure 2.6), public model and system card precedents from frontier labs as a documentation form factor, and the SEC Marketing Rule and books-and-records rule frame for adviser/BD AI use.

#### Input description

A US broker-dealer has intaked a GenAI research-summarisation assistant for internal analyst use. The assistant ingests public earnings transcripts and the firm's own published research notes and produces structured summaries for the equity research desk. Output is internal only; no client-facing surface today. Vendor-hosted foundation model with version pinning, RAG over the firm's research note corpus and a vendor-supplied transcript corpus. No tools; no agentic behaviour; advisory-only. Sponsor (head of equity research) proposed tier-3.

Engagement scope provided by `scoping`:
- Institution type: broker-dealer (also dual-registered investment adviser), primary regulators SEC and FINRA.
- Persona: AI Governance Lead, second line, reporting to CCO.
- Sector overlay set: capital-markets. Cross-cutting overlays: cyber (vendor-hosted foundation model is a supply-chain surface), conduct (research integrity and Reg AC adjacency).
- Source posture: public-plus-firm-policy.

#### Output sketch

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

#### Why this scenario matters

- It exercises the GenAI factor block. Foundation-model dependence, hallucination, citation fabrication, vendor swap, RAG corpus drift are scored explicitly. NIST AI 600-1 Measure 2.6 is the anchor; the tier rubric does not collapse to a pre-GenAI shape.
- It exercises the customer-impact-low + regulatory-adjacency-medium combination. Customer impact is the dominant tier-1 trigger when present; here it is absent and the tier holds at tier-3 despite regulatory adjacency.
- It exercises the re-tiering trigger discipline. Incorporation into client-facing material, scope expansion, tool addition, and a vendor swap are each named events with monitoring owners. The tier is defensible at the time of decision and re-defensible when scope grows.
- It exercises the no-dissent path. Sponsor proposal is accepted; the dissent block is empty rather than padded.
- It is the routing decision for downstream skills: model-card-builder gets `tier-3` and compresses sections accordingly; validation-plan gets `validation_depth = targeted`; agentic-ai-controls is not invoked (advisory only); llm-vendor-evidence-review is invoked at light-touch depth.

## troubleshooting

### Troubleshooting: ai-risk-tiering

Recurring failure modes when a tier decision looks complete but is not. The decider attestation should catch these; the rubric review should preempt them.

#### The rubric collapses to a single dominant factor

Symptom: every factor scored, but only `customer_impact` carries the rationale. Cyber, conduct, vendor-dependence, and concentration are scored `low` or `n/a` without justification. The tier rationale reads as a one-factor argument.

Why it happens: customer impact is the easiest factor to assess and the loudest. The other factors require pulling on threads (vendor evidence, concentration analysis, NYDFS exposure) that take longer to investigate.

Fix: require all named factors to be scored, with `n/a` justified, not blank. The decider attestation block does not clear when more than one factor is unjustifiably `n/a`. The schema enforces it; the reviewer reads it.

#### Tier inflation or deflation by sponsor pressure

Symptom: the sponsor wants a lower tier to skip validation depth, or a higher tier to look serious. The tier matches the sponsor's proposal without dissent recorded; the rationale leans on factors that were not the actual driver.

Why it happens: the tier decision reads as a negotiation instead of a defended judgement. Common when the model risk team and the sponsor sit close together; less common when second-line owns the artefact.

Fix: dissent field is required when tier disagrees with sponsor proposal. AI risk committee secretary signs the dissent line at tier-1 and tier-2; the second-line reviewer signs at tier-3 and tier-4. An empty dissent block is fine; an inflated tier without a defending rationale is not.

#### Re-tiering triggers are dates instead of events

Symptom: the re-tiering trigger block reads "annual review" or "Q4 reassessment" as the only entries. The use case grows beyond its tier between review dates without anyone noticing.

Why it happens: annual review feels like the safe default; named events take more thought to enumerate.

Fix: each re-tiering trigger names an event with a monitoring owner and a detection method. Dates are refresh cadences, not triggers. Sector-overlay re-tiering triggers are loaded from the matching overlay file; cross-cutting overlay triggers from the cross-cutting file. Empty or date-only trigger blocks fail the decider attestation.

#### GenAI factor block is missing on a GenAI use case

Symptom: tier rubric uses pre-GenAI factor language; foundation-model dependence, RAG corpus drift, prompt-injection exposure, autonomy uplift via tool use are all absent or all `n/a` without justification.

Why it happens: the rubric was built for traditional ML; the GenAI fields look optional and the decider ticks the boxes that exist. Common at first-tier-on-GenAI-use-case stage; less common after the firm has tiered a few.

Fix: when the use case is GenAI (foundation model, RAG, or tools), the GenAI overlay block fires. Reference NIST AI 600-1 Map 1.1 and Measure 2.6 in the rubric explicitly. The schema's `genai_specific` factor is required to be scored; the source trace points at the vendor system card and the firm-side evaluation evidence separately.

#### Tier-1 set by reflex for anything customer-facing

Symptom: every customer-facing use case is tier-1; tier-1 becomes the default and loses meaning. Validation depth, monitoring frequency, and committee path get applied uniformly across the inventory; the firm spends tier-1 resources on tier-3 use cases.

Why it happens: tier-1 feels safe; the cost of over-tiering is hidden (everyone's time) while the cost of under-tiering is loud (an exam finding).

Fix: tier-1 is reserved for customer-binding decisions or material financial impact; the rationale names the threshold. Customer-facing alone is not a tier-1 trigger; an internal-use GenAI assistant is not tier-1 even if it interacts with customer-data inputs. The decider attestation challenges any tier-1 designation that does not clear the named-threshold test.

#### AI Act overlap is set to true reflexively or missed entirely

Symptom: every use case is routed to `ai-act-triage` regardless of EU footprint, or no use case is routed even when a US adviser serves EU professional clients.

Why it happens: the AI Act is unfamiliar to US-only practitioners, who either over-route as a hedge or under-route from absence of EU client volume.

Fix: the `ai_act_category` factor records the category-by-category Annex III check, not a single yes/no. EU footprint includes EU establishment, EU customer base, EU client base for an adviser, or EU branch reinsurance; the rubric flags the routing trigger when any of those is in scope. Where US-only and no EU exposure, the factor records `n/a` with footprint as the rationale and a re-tiering trigger if footprint changes.

#### Sector overlay loaded but ignored

Symptom: insurance pricing model tiered without NAIC #880 unfair-discrimination framing; banking AML model tiered without FFIEC manual exposure; capital-markets surveillance model tiered without Rule 15c3-5 overlap; payments-fintech AI tiered without sponsor-bank reach.

Why it happens: the sector overlay file exists in `references/sector-overlays.md` but the decider treated it as background reading.

Fix: when the scope names a sector, the matching overlay's elevation factors and triggered gates land in the tier decision. Sign-off questions probe the sector items. If the overlay is loaded but the tier decision has no overlay-specific content, the loader did not run; rerun with the overlay reference in scope.

#### Cross-cutting overlay (cyber, privacy, conduct) is collapsed into the capability rubric

Symptom: cyber exposure scored `low` because "no customer-facing surface", missing the tool-use uplift; privacy scored against training data only, missing the prompt surface; conduct scored only on direct customer impact, missing the indirect path through analyst recommendations or marketing material.

Why it happens: the capability rubric has cyber, data sensitivity, and conduct as named factors; the cross-cutting overlay reads as duplicative.

Fix: the cross-cutting overlay tells the rubric what counts as high, medium, low for the named factor. Cyber, privacy, and conduct are scored once; the overlay is the scoring guide. Where the overlay is loaded but the score reads as if the overlay were absent, the decider re-reads the overlay and re-scores.

#### Vendor-dependence scored against contract, not against operational reality

Symptom: vendor-dependence scored `low` because "version pinning is in the contract"; in operational reality the vendor swaps the underlying model with a notice period the firm cannot meet, or pinning applies to the API endpoint but not to the model behaviour.

Why it happens: the contract is the easiest evidence; operational evidence (vendor change-of-version notice posture, pinning verification) requires asking the vendor and reading the notice channel.

Fix: vendor-dependence scoring reads the operational posture, not just the contract. Version pinning in contract without an audited notice channel reads as medium dependence, not low. Vendor-supplied adversarial-test results (vendor self-attestation) read as medium evidence at most; firm-independent evaluation reads as higher confidence. The source trace records both separately.

#### Tier and gates do not match firm policy

Symptom: tier-1 with no AI risk committee approval gate; tier-3 with full validation gate; tier-4 with quarterly monitoring. The default tier-to-gate mapping in the template is treated as advisory and overridden without rationale.

Why it happens: the firm's policy defines the mapping; the template's defaults are illustrative and the decider conflated the two.

Fix: where firm policy supplies the tier-to-gate mapping in `references/firm-overlay.md`, the firm policy wins and the template's defaults yield. Where firm policy does not yet exist, the template's defaults are the starting point and any deviation requires rationale in the dissent block. The tier-to-gate mapping is policy, not judgement.

#### Source trace omits the regulatory citation

Symptom: tier-1 designation citing "ECOA reach" or "FFIEC manual exposure" without a section reference or link. The decider's reading of the regulation is on the table; the regulatory citation is not.

Why it happens: the citations live in `references/source-anchors.md` and the decider treated the rationale text as self-supporting.

Fix: every regulatory claim in the tier rationale carries a source-anchor pointer. The source trace block enforces the discipline. Where the citation carries `[verify section]`, the flag carries forward into the tier decision; do not invent.

#### Re-tiering trigger ownership is left unassigned

Symptom: triggers named with detection methods but no owner; or owner listed as "TBD" or as a named individual.

Why it happens: triggers cross functions (vendor management owns vendor change-of-version notice, regulatory change owns horizon scan, AI governance owns scope changes), and the decider leaves the owner blank rather than chasing across functions.

Fix: each trigger names a function as owner, never a named individual. Where the owner spans functions (vendor management with CISO function, for example), both functions are named. Triggers without owners fail the decider attestation; chasing the owner across functions is part of the work.

#### ORSA materiality (insurance) or stress-testing inclusion (banking) is missed

Symptom: insurance use case tiered as tier-2 with ORSA materiality un-checked; banking use case tiered without CCAR/DFAST pedigree where the model is in fact in scope.

Why it happens: ORSA and CCAR/DFAST owners sit elsewhere in the firm; the tier decider does not have the inventory in front of them.

Fix: insurance tier decisions check ORSA-materiality-thresh; banking tier decisions check stress-testing-inscope. Both are sector-overlay-loaded and required to be scored. Where the answer is unknown at tier-decision time, the open-questions block carries the item with a named owner and a due date before pre-prod gate.
