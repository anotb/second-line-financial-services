# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## credit-decisioning-ml

### Example: model card refresh for an in-house consumer auto-loan decisioning model

Public-source-derived. No named institution. Framing patterns drawn from Reg B §1002.9 (specific reasons for adverse action) and the underlying ECOA / Reg B regulatory text. CFPB Circulars 2022-03 and 2023-03 informed the original framing but were **withdrawn May 12, 2025; historical only**. No firm-specific facts asserted.

#### Input description

A US mid-size bank holding company runs a gradient-boosted classifier to score consumer auto-loan applications in the indirect channel. The model has been in production for 18 months. Annual model inventory exercise is in motion. Card was first written at pre-prod gate; today's task is the refresh ahead of the model risk committee review.

Engagement scope provided by `scoping`:
- Institution type: bank holding company, asset size mid-cap, primary regulators OCC and CFPB.
- Persona: model risk validator, second line, reporting to the head of model risk.
- Sector overlay set: banking. Cross-cutting overlays: privacy (regulated NPI), conduct (consumer credit decisioning).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2 (material, customer-facing, ECOA/Reg B exposure, not enterprise-defining).

#### Output sketch

Card sections produced (abbreviated):

- **Card metadata** — model ID `auto-uw-gbm-v3.2`; tier-2; lifecycle stage prod; second-line reviewer named in the scope record.
- **Intended use** — auto-loan underwriting decisioning, US-only, indirect dealer channel only. Out of scope: refinance, lease, direct-to-consumer, pre-approval marketing scoring.
- **System description** — gradient-boosted decision tree on bureau attributes plus application data; no foundation model, no RAG, no tools. Production on internal model serving platform v4.
- **Training and reference data** — bureau attributes from named bureau (regulated NPI, GLBA in scope), application form data (regulated NPI), no alternative data, no social media data. Training window 2022-01 to 2024-12. Excluded fields: ZIP proxies for protected class flagged in 2024 fair-lending review (lineage cited in source trace).
- **Performance summary** — AUC overall and by FICO band, by state, by indirect dealer segment. Deployed-environment metrics from monthly performance pack, not lab-only. Approval rate by FICO band reported alongside.
- **Robustness and stress testing** — out-of-time backtest, recession scenario backtest using internal stress framework, dealer-segment robustness test.
- **Fairness and explainability** — adverse action coding rate by ECOA protected class, disparity ratios calculated per the firm's fair-lending test plan, explainability via SHAP at decision level for adverse action notice generation. Method limitations recorded (SHAP for non-linear interaction effects).
- **Limitations and known failure modes** — concrete list:
  - Thin-file applicants (fewer than three bureau tradelines): model undermargined, override rate elevated. Example: 2025-Q2 monitoring showed override rate of 14% on thin-file segment versus 3% portfolio average.
  - Post-bankruptcy applicants in the 24-to-48-month window: model treats as high-risk despite recovery patterns; second-look process required.
  - Out-of-state applicants in three named states with thin training coverage: AUC drop measured, segment-flag fires at decision time.
- **Monitoring plan** — PSI on top input features (threshold 0.25, monthly, owner: model owner, escalation to MRMO at breach); score drift (KS against reference distribution, threshold per firm policy); decisioning-rate drift (state-level and dealer-level, monthly); complaint-rate drift (CFPB complaint database plus internal complaint feed, monthly, owner: consumer compliance, escalation to fair lending committee at breach). Each entry has threshold, owner, and escalation path filled.
- **Controls** — challenger model in shadow mode (preventive, owner: model owner); 5% random override sampling for second-line review (detective, owner: validator); monthly performance pack review (detective, owner: model risk committee); adverse action notice quality sampling (detective, owner: consumer compliance).
- **Change management** — re-validation triggers: feature add or remove, training data window shift > 6 months, performance trigger breach for two consecutive months, new state added to operating footprint, regulatory change in adverse action notification standard. Approver: head of model risk for tier-2.
- **Sign-off questions** — six concrete questions tagged to sections: (i) what is the trigger to re-fit, who approves; (ii) policy for proxy variables identified after deployment; (iii) thin-file segment treatment plan and timeline; (iv) integration with consumer-compliance fair-lending test plan, frequency; (v) monitoring escalation path when complaint-rate drift breaches; (vi) override pattern monitoring across dealer segments for unfair-treatment risk.
- **Source trace and confidence** — every claim cited to source: validation report 2025-Q2, monitoring pack 2025-09, fair-lending test plan 2025-Q1, adverse action notice review 2025-08. Two `[evidence needed]` flags carried forward to the issue log: foundation-model dependence statement (n/a here) and prompt-injection exposure (n/a here).

#### Why this scenario matters

- It exercises the segment-level performance reporting requirement: an overall AUC is acceptable but the segment table reveals the thin-file exposure and the post-bankruptcy exposure that drive the limitations section.
- It exercises the conduct cross-cutting overlay: complaint-rate drift in monitoring, adverse action notice quality in controls, integration with consumer-compliance fair-lending test plan in sign-off questions. The model card and the fair-lending test plan are different artifacts but they reference each other.
- It exercises the banking sector overlay: ECOA/Reg B adverse action surface, OCC primary regulator framing, model risk committee as the sign-off body. Tier-2 depth, not tier-1: the card is reviewable in a single committee session.
- It exercises the lifecycle distinction: refresh is not a first draft. Most fields carry forward; the fields that move are performance (new monitoring period), limitations (new evidence from the segment table), controls (new override sampling), and sign-off questions (new ones raised by this period's evidence).

## genai-customer-support

### Example: first model card for a vendor-hosted GenAI customer-support assistant

Public-source-derived. No named institution. Pattern drawn from NIST AI 600-1 Generative AI Profile (Map 1.1, Measure 2.x), public model and system card precedents from frontier labs (Anthropic Claude system cards, OpenAI system cards) used as a documentation form factor only, and NYDFS October 2024 industry letter on GenAI cybersecurity risks.

#### Input description

A regional US bank holding company is launching a vendor-hosted GenAI assistant inside the consumer-banking customer-support call center. The assistant summarises customer history, suggests next-best-action steps for the agent, and drafts written follow-ups for the agent to review and send. No auto-decisioning, no auto-sending. First model card; pre-prod gate is the consuming review.

Engagement scope provided by `scoping`:
- Institution type: bank holding company, asset size mid-cap, primary regulators FRB and CFPB; OCC for the national-bank subsidiary.
- Persona: AI Governance Lead, second line, reporting jointly to CRO and CCO.
- Sector overlay set: banking. Cross-cutting overlays: cyber (NYDFS Part 500 in NY footprint, NYDFS October 2024 letter), privacy (regulated NPI), conduct (UDAAP exposure on customer-facing communications).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2 (customer-impact-adjacent, agent-mediated, not auto-decisioning, not enterprise-defining).

#### Output sketch

Card sections produced (abbreviated):

- **Card metadata** — model ID `cs-assistant-v1.0`; tier-2; lifecycle stage pre-prod; scope ID cited.
- **Intended use** — customer-support agent productivity. Intended users: licensed bank customer-support agents. In-scope decisions: summarise customer history; suggest next-best-action; draft written follow-ups for agent review. Out-of-scope decisions: any direct customer communication without agent review; any account action; any product recommendation; any fee waiver; any complaint resolution.
- **System description** — vendor-hosted GenAI assistant. Foundation model from named vendor, version pinned (vendor change-of-version notice required by contract). RAG over the bank's customer-history datastore and policy/procedure corpus. No tools. Autonomy level: human-in-the-loop (agent must review and send). Dependencies: vendor API, internal policy corpus refresh pipeline.
- **Training and reference data** — foundation model trained by vendor (firm has no visibility beyond vendor system card; recorded in source trace at confidence: low). RAG corpus: customer history (regulated NPI under GLBA; retention 7 years per firm policy; lineage to system of record), policy and procedure documents (confidential business data; retention indefinite; lineage to policy management system). Excluded from RAG: any data outside the agent's customer; any data older than the customer's relationship start date.
- **Performance summary** — faithfulness on summary outputs (sample-based, monthly), citation precision on policy citations (sample-based, monthly), refusal rate on out-of-scope queries, agent-edit rate on draft follow-ups (proxy for utility), latency. All deployed-environment metrics; lab-only metrics from vendor system card recorded separately and clearly labelled. Initial values: from pre-prod pilot, segmented by call-type (account inquiry, dispute, fee waiver request, complaint).
- **Robustness and stress testing** — prompt injection adversarial test suite (firm-internal red team plus vendor-supplied test set), jailbreak test results, RAG poisoning test (synthetic policy-corpus poisoning), dialect and accent coverage on transcribed call audio, refusal behaviour under prompt-engineering by curious agents.
- **Fairness and explainability** — explainability via citation-of-source for any factual claim in the assistant output (intrinsic to RAG architecture; no separate post-hoc method). Fairness: agent-edit rate by call-type and by inferred customer segment (where lawfully tracked); UDAAP-relevant content flag rate by call-type. Method limitations recorded.
- **Limitations and known failure modes** — concrete list:
  - Hallucinated policy specifics: assistant may state a fee waiver threshold from training data rather than from the bank's current policy corpus. Example: pilot found the assistant cited an industry-typical late-fee policy that did not match the bank's current policy. Mitigation: agent review gate, plus policy-corpus citation precision metric in monitoring.
  - Cross-customer information bleed: RAG retrieval can return adjacent customer records under poorly scoped queries. Example: pilot found two cases of cross-customer record retrieval over 1,000 calls; mitigation: query scoping at retrieval layer, plus retrieval-source audit in monitoring.
  - Foundation-model swap risk: vendor releases a new model version with materially different behaviour; firm has version pinning and change-of-version notice but the swap is partially outside firm control. Example: in the pilot, vendor released a new model and behaviour shifted on refusal frequency; mitigation: change-of-version notice triggers re-validation per change-management table.
  - Prompt injection from customer-supplied content: customer email forwarded into the call record can carry adversarial instructions. Mitigation: input filtering on customer-supplied content; agent training to recognise injected content.
  - Dialect and accent under-coverage on transcribed call audio: pilot found higher transcription error rate on non-Mainstream-American-English speakers; downstream impact on summary faithfulness. Mitigation: transcription-error monitoring by inferred dialect, with the inferred-dialect classifier itself flagged as a fairness-sensitive element.
- **Monitoring plan** — faithfulness sampling (50 cases per week, owner: AI governance team, escalation to model risk committee at breach of threshold); citation precision (50 cases per week); cross-customer retrieval audit (continuous, owner: information security); prompt-injection signal monitoring (continuous, owner: information security, escalation to CISO at breach); complaint-code monitoring on calls handled by the assistant (continuous, owner: consumer compliance, escalation to fair lending and complaints committee); agent-edit rate (weekly, owner: customer-support operations); foundation-model version monitoring (continuous, owner: vendor management, escalation to AI Governance Lead at any change-of-version notice). Each monitoring entry has threshold, frequency, owner, and escalation path.
- **Controls** — preventive: input filtering on customer-supplied content; output filtering for policy-fact statements; agent training; query scoping at retrieval layer. Detective: agent review gate before any send; monthly faithfulness sampling; cross-customer retrieval audit; prompt-injection signal monitoring; UDAAP-relevant content flag review. Response: vendor change-of-version notice triggers re-validation; cross-customer retrieval finding triggers incident response; complaint-code spike triggers consumer-compliance review. Owners and evidence pointers recorded for each control.
- **Change management** — re-validation triggers: vendor model swap (always); RAG corpus expansion or scope change; addition of any tool to the agent; change in autonomy level (e.g., move to human-on-the-loop or auto-sending); state-footprint change (cyber overlay implication). Approver: AI Governance Lead jointly with head of model risk.
- **Sign-off questions** — eight concrete questions tagged to sections: (i) what happens when the vendor swaps the underlying model, who approves the post-swap deployment; (ii) what is the escape path if a hallucinated policy fact reaches a customer; (iii) cross-customer retrieval incident response — who owns, what is the customer notification posture under Reg P and state breach laws; (iv) prompt-injection finding response — what is the threshold for taking the assistant offline; (v) UDAAP exposure on assistant-drafted follow-ups — who reviews, how is it sampled; (vi) NYDFS October 2024 letter alignment for the NY footprint — what evidence supports the statement; (vii) inferred-dialect classifier in monitoring is itself a fairness-sensitive element — who validates that classifier; (viii) lifecycle exit — what is the retirement plan if the assistant is decommissioned, including data retention and customer-history audit trail.
- **Source trace and confidence** — pre-prod pilot results with high confidence; vendor-supplied evaluation evidence with low to medium confidence (firm has no visibility into vendor pre-training); NYDFS October 2024 letter alignment cited at high confidence; foundation-model swap risk recorded at medium confidence (vendor commitment to notice, but operational implementation has not yet been tested in production).

#### Why this scenario matters

- GenAI cards inherit a structure designed for traditional ML; this scenario shows where the structure stretches: foundation-model dependence, RAG corpus drift, prompt injection, content provenance, vendor swap risk. The card has to carry these.
- Architecture flags `foundation_model = present`, `uses_rag = true`, `uses_tools = false`, `autonomy_level = human-in-the-loop`. The schema's GenAI sub-fields fire and the card answers them.
- Cyber cross-cutting overlay activates explicitly: NYDFS October 2024 letter, prompt-injection threat, cross-customer retrieval audit. The model card section that touches cyber is concrete and inspectable.
- Conduct cross-cutting overlay activates: UDAAP exposure on assistant-drafted follow-ups, complaint-code monitoring as a consumer-compliance signal. The card carries the consumer-impact framing despite no direct customer-facing surface.
- Sign-off questions are concrete and sit on the seams a reviewer is most likely to challenge. The list is not generic; each question is tagged to a card section.
- The card is the pre-prod gate input to `genai-pre-prod-review`; it consumes upstream artifacts (intake, tier, AI Act triage if applicable) and emits a structured object the reviewer skill can read programmatically.

## troubleshooting

### Troubleshooting: model-card-builder

Recurring failure modes when a model card looks complete but is not. The reviewer pass should catch these; the builder pass should preempt them.

#### The card describes the model as it should be, not as it is

Symptom: limitations section reads aspirationally ("the model is monitored continuously for drift"), monitoring plan describes the operating intent rather than what is wired up, controls list policies rather than implemented mechanisms.

Why it happens: model owner drafted the card from the design spec, not from the operating evidence. Common at first-card stage; also common on refresh when the prior card was inherited and never re-evidenced.

Fix: every monitoring entry, control, and performance metric carries a source-trace pointer (monitoring pack, control evidence pointer, validation report, performance pack). Items without an evidence pointer go to the issue log, not into the card. If the card cannot be fully evidenced today, the gaps go to the engagement before sign-off, not after.

#### Performance summary cites lab metrics, not deployed-environment metrics

Symptom: AUC, faithfulness, accuracy reported as a single number from a holdout set or vendor evaluation, no segment breakdown, no monitoring-pack pull.

Why it happens: lab numbers exist before the model goes live; deployed numbers wait on the monitoring infrastructure. Card-writing pressure beats wait-for-monitoring.

Fix: schema field `performance.deployed_environment` is required. Lab-only metrics are recorded but labelled. Production cards lean on deployed metrics. Pre-prod cards may carry lab metrics, but the card states that deployed monitoring replaces them at the first cycle, with metric, threshold, and owner named.

#### Limitations section is generic platitudes

Symptom: "model may not generalise to populations outside the training data"; "performance may degrade over time"; "the model has bias that should be monitored". A reviewer learns nothing from these.

Why it happens: limitations get drafted last when card-writer fatigue is highest; the section is treated as a hedge.

Fix: schema requires `limitations[].failure_mode` and `limitations[].example`. Each limitation needs to be concrete enough that a reviewer can picture the failure and a monitoring metric to detect it. If you cannot give an example, you do not yet know the limitation. Surface it as a sign-off question instead.

#### Monitoring plan does not name owners or escalation paths

Symptom: list of metrics with thresholds, no owner column, no escalation column. Monitoring lives on paper; no one is accountable when a threshold breaches.

Why it happens: the model owner does not control all the owners (consumer compliance owns complaint rate, infosec owns prompt-injection signal, vendor management owns version notice). The card-writer leaves the owner column blank rather than chasing across functions.

Fix: schema requires `monitoring[].owner` and `monitoring[].escalation_path` on every entry. Missing fields fail schema validation. Chasing the owner across functions is part of the work.

#### Sign-off questions are too generic

Symptom: questions like "is the model fit for purpose?" or "are the controls adequate?". The reviewer cannot use them to challenge anything.

Why it happens: the card-writer treats sign-off questions as a closing flourish rather than a reviewer aid, or copies questions from a prior card without re-reading the new one.

Fix: each sign-off question is tagged to a section (`signoff_questions[].section_tag`) and points at a specific seam in this card. Bad: "are the controls adequate?". Good: "the agent-review gate is the only preventive control between the assistant output and the customer; what is the off-switch criterion if agent-edit rate falls below the threshold for two consecutive months?". A question that can be cut-and-pasted to any card is too generic.

#### GenAI card uses the traditional-ML structure unmodified

Symptom: foundation model dependence omitted; RAG corpus not described; prompt-injection exposure absent; vendor change-of-version risk not in change management.

Why it happens: the card template was built around traditional ML and the GenAI fields look optional. The owner ticks the boxes that exist and skips the others.

Fix: when `architecture.foundation_model.provider` is set, or `architecture.uses_rag` is true, or `architecture.uses_tools` is true, the GenAI overlay block fires: foundation-model dependence (provider, name, version, pinning), RAG corpus and retrieval scoping, tool inventory and tool-boundary controls, prompt injection in robustness, vendor change-of-version trigger in change management. Builder check before submission, reviewer check before sign-off.

#### Card is updated only at validation cycles

Symptom: card date is 14 months old; meanwhile the foundation model has been swapped, the RAG corpus expanded, a tool was added, the prompt template changed.

Why it happens: card refresh is treated as an annual exercise; in-flight changes are tracked in the change log but never re-flowed into the card.

Fix: the change-management table lists re-validation triggers; foundation-model swap, RAG corpus scope change, tool addition, and autonomy-level change are always triggers. Each trigger event re-validates the card section that names the changed element. The card is a living document; the annual refresh is consolidation, not sole maintenance.

#### Tier and depth do not match

Symptom: tier-4 model with a 12-page card detailing every nuance; or tier-1 model with a one-pager.

Why it happens: a single template depth is being applied across the inventory.

Fix: tier drives depth. Tier-4 cards are short, focused on intended use, data, owner, monitoring. Tier-1 cards are deep, with full robustness, fairness, and sign-off coverage. The template is a maximum; the scope sets how much of it to fill. When tier and depth disagree, the scope record wins.

#### Sector overlay loaded but ignored

Symptom: insurance pricing model card reads in fairness/bias vocabulary but never names unfair discrimination under NAIC Model #880; banking AML model card never names FFIEC manual exposure; capital-markets surveillance card never names the Rule 15c3-5 overlap.

Why it happens: the sector overlay file exists in references/ but the card-writer treated it as background reading.

Fix: when the scope names a sector, the matching `references/sector-overlays.md#<sector>` content lands as named items in the card. Sign-off questions probe the sector items. If the overlay is loaded but the card has no overlay-specific content, the loader did not run; rerun with the overlay reference in scope.

#### Source trace omits the foundation-model dependency

Symptom: GenAI card has full source trace on firm-supplied evidence; the foundation-model facts (training cutoff, vendor evaluations, system card statements) are missing or claimed at high confidence without a pointer.

Why it happens: vendor system cards are external documents; the card-writer treats them as background, not as evidence.

Fix: vendor system cards and vendor evaluation reports are evidence. Cite them in source trace with confidence appropriate to vendor self-attestation (typically low to medium). Where the firm has run an independent evaluation, cite that separately at higher confidence. Do not collapse vendor and firm evidence into a single line.

#### Audience and tone mismatch

Symptom: card reads like vendor marketing; or like an academic paper; or like a developer README. Practitioner reviewer cannot use it for committee or examiner review.

Why it happens: the card-writer borrowed phrasing from the vendor system card or an academic paper, or imported the development README into the card.

Fix: voice is senior model risk practitioner. The audience is the model risk committee, the validator, the examiner. Depth and formality flex with the scope `persona.role` and the lifecycle stage. A pre-prod committee card is more formal than a development working note; an exam-response card is more formal still.
