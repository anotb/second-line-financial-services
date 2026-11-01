# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## credit-scoring-ml

### Example: annual revalidation plan for an in-house consumer credit-scoring model

Public-source-derived. No named institution. Framing patterns drawn from the joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17 2026; supersedes SR 11-7 and SR 21-8) for the validation-pillar framing on a traditional non-generative ML model, Reg B §1002.9 on adverse action notification, and the public ECOA / Reg B fair-lending exam record. CFPB Circular 2022-03 informed earlier framing but was **withdrawn May 12, 2025; historical only**. No firm-specific facts asserted.

#### Input description

A US mid-size bank holding company runs a gradient-boosted classifier for indirect-channel auto-loan underwriting. Tier-2 model, 18 months in production, prior validation completed at pre-prod gate. Annual revalidation is the next required cycle. Engagement is staffed by the model risk function in the second line; the model owner sits in the consumer-lending business.

Engagement scope provided by `scoping`:
- Institution type: bank holding company, mid-cap, primary regulators OCC and CFPB.
- Persona: head of model risk (validator, second line). Model owner: head of consumer credit (1.5 line).
- Sector overlay set: banking. Cross-cutting overlays: privacy (regulated NPI), conduct (consumer credit decisioning).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2, carried forward from prior `ai-risk-tiering` output.
- Validation type: annual-revalidation.

#### Output sketch

Plan sections produced (abbreviated):

- **Plan metadata** — model ID `auto-uw-gbm-v3.2`; tier-2; validator: head of model risk; validation type: annual-revalidation; scope date set; use-case ID and scope ID cited.

- **Validation depth** — set per pillar, not as a single label. Conceptual soundness: targeted (no theory change, segmentation review only because the firm added two states to its operating footprint). Outcomes analysis: full (12 months of new deployed-environment evidence to read against prior validation). Ongoing monitoring: targeted (review the validator-trigger thresholds against the year's monitoring pack). Tier justification documents why the depths land where they do.

- **Conceptual soundness scope** — segmentation review for the two added states; review of the override policy update applied in 2025-Q2; alternatives-considered note carried from prior validation (no new alternatives evaluated this cycle); foundation-model selection rationale: not applicable.

- **Data review scope** — bureau attribute fitness (named bureau, GLBA in scope); training-window check (2022-01 through 2024-12, plus Q1-Q3 2025 monitoring data used for outcomes analysis); exclusions check (ZIP-proxy fields removed in 2024 fair-lending review confirmed still excluded); lineage to system of record verified.

- **Outcomes analysis scope** — KS and AUC overall and by FICO band; capture rate by FICO band and by region; override outcomes versus policy (a control point that escaped the prior validation cycle); comparison against challenger model run in shadow over the same period; deployed-environment metrics dominate, lab-only metrics labelled separately. Each test names dataset, success criterion, owner.

- **Robustness scope** — out-of-time backtest on the 12 months since prior validation; recession-scenario backtest using the firm's internal stress framework; segment robustness on the two added states (sample size flagged as a constraint).

- **Fairness, explainability, transparency scope** — ECOA / Reg B disparity testing across protected classes per the firm's fair-lending test plan; disparity ratios calculated; SHAP-based adverse action reason generation reviewed for accuracy against a sample of recent declines; Reg B §1002.9 specific-principal-reasons requirement and Comment 9(b)(2)-3 of the Official Staff Commentary (cited reasons must accurately describe factors actually considered or scored) read into the explainability success criterion. CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only**.

- **Ongoing monitoring scope** — review of PSI thresholds on top input features (monthly), score drift (KS on score distribution), decisioning-rate drift (state-level and dealer-level), complaint-rate drift (CFPB complaint database plus internal feed). Each monitoring entry declares whether breach triggers re-validation; the validator's view and the model owner's monitoring view are aligned but distinct (operational alerts versus revalidation triggers).

- **Effective challenge questions** — six concrete questions, each tagged to a design choice or assumption: (i) the segmentation cuts pre-date the two added states; what evidence supports their continued validity post-expansion; (ii) the override policy update in 2025-Q2 shifted human approval rate by an unnamed amount; what was the analysis behind the threshold change; (iii) the training-window cutoff at 2024-12 means 2025 data has not entered training; what is the policy on training-window refresh, and at what cadence; (iv) thin-file applicants are flagged in the prior limitations section; what is the trigger to re-fit the thin-file segment treatment; (v) post-bankruptcy applicants in the 24-to-48-month window are noted as undermargined; what evidence does the validator need to see to retire that limitation; (vi) the SHAP-based adverse action notice generation has a sampling QC; what is the accuracy threshold and what is the escalation if accuracy drifts.

- **Dependencies** — bureau attribute extract for the validation window; performance-pack data feed access; fair-lending test plan output (cross-reference to consumer-compliance test cycle); override decision log access; complaint-rate data feed access.

- **Timeline** — 8-week revalidation cycle with milestones (data assembly, conceptual soundness review, outcomes analysis, fairness testing, draft validation report). Deliverables: downstream validation report, refreshed model card via `model-card-builder`, MRA / issue log entries where defects are found.

- **Source trace and confidence** — every scope item cited to the source artifact (prior validation report, firm fair-lending test plan, monitoring pack 2025-09, override policy update memo 2025-Q2, scope record). Two `[evidence needed]` flags carried forward to the engagement issue log: 2025-Q2 override policy threshold change rationale (memo refers to a quantitative analysis the validator has not yet seen); two-added-states sample size for segment robustness testing (whether the sample is large enough to support a credible test).

#### Why this scenario matters

- It exercises the per-pillar depth setting. Setting validation depth as a single label misses that conceptual soundness, outcomes analysis, and ongoing monitoring scope independently for an annual revalidation. The plan reads CS at targeted, OA at full, OM at targeted, and explains why.
- It exercises effective challenge that probes design choices, not generic policy compliance. Each question names the choice or assumption it interrogates, with expected evidence and an owner of response.
- It exercises the conduct cross-cutting overlay: SHAP-based adverse action reason generation with sampling QC, complaint-rate drift in monitoring, ECOA / Reg B disparity testing in fairness scope.
- It exercises the banking sector overlay: ECOA / Reg B adverse action surface, OCC primary regulator framing, CFPB consumer-protection authority over a large bank.
- It exercises the validator-vs-model-owner monitoring distinction: each monitoring entry declares whether breach is a revalidation trigger or a routine operational alert. The two views overlap but are not the same.
- The plan stops at draft. The head of model risk signs off. The downstream validation report consumes this plan as its scope contract.

## genai-customer-service

### Example: initial validation plan for a vendor-hosted GenAI customer-support assistant

Public-source-derived. No named institution. Patterns drawn from the joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17 2026; supersedes SR 11-7 and SR 21-8) for traditional-model framing (the bulletin expressly excludes GenAI and agentic AI from scope, footnote 3); NIST AI 600-1 (Generative AI Profile) Measure subcategories on hallucination, prompt injection, and information integrity for the GenAI substantive anchors; NYDFS October 2024 industry letter on GenAI cyber risks; and public model and system card precedents from frontier labs as a documentation form factor only. No firm-specific facts asserted.

#### Input description

A regional US bank holding company is preparing the validation plan for a vendor-hosted GenAI assistant that supports the consumer-banking call center. The assistant summarises customer history, suggests next-best-action steps for the agent, and drafts written follow-ups for the agent to review and send. No auto-decisioning, no auto-sending. Initial validation; pre-prod gate is the consuming review.

Engagement scope provided by `scoping`:
- Institution type: bank holding company, mid-cap, primary regulators FRB and CFPB; OCC for the national-bank subsidiary.
- Persona: AI Governance Lead (validator coordination role) jointly with head of model risk.
- Sector overlay set: banking. Cross-cutting overlays: cyber (NYDFS Part 500 in NY footprint, NYDFS October 2024 letter), privacy (regulated NPI), conduct (UDAAP exposure on customer-facing communications).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2 (customer-impact-adjacent, agent-mediated, not auto-decisioning).
- Validation type: initial.

#### Output sketch

Plan sections produced (abbreviated):

- **Plan metadata** — model ID `cs-assistant-v1.0`; tier-2; validator: head of model risk; validation type: initial; scope ID cited.

- **Validation depth** — set per pillar. Conceptual soundness: targeted (vendor model is opaque; focus is on selection rationale, RAG architecture, prompt design, tool-boundary review). Outcomes analysis: full (no prior cycle to lean on; the plan defines the test set and success criteria from scratch). Ongoing monitoring: full (pre-prod plan that anchors what production monitoring must produce). Tier justification documents the agent-mediated lower autonomy as a depth modifier.

- **Conceptual soundness scope** — foundation-model selection rationale review (vendor evidence: published system card, vendor evaluation report, red-team summary from vendor; firm-side rationale memo); RAG architecture review (corpora named, retrieval scoping rules, refresh cadence); prompt design review (system prompt, retrieval prompt, output guardrails); tool boundary review (no tools; no auto-decisioning; agent-review gate as the only preventive between assistant output and customer). `vendor_model_card_review` flag set true; vendor evidence in scope is enumerated.

- **Data review scope** — RAG corpus inventory (customer history datastore, policy/procedure corpus); access-control review on the customer-history datastore (regulated NPI under GLBA); retention review; lineage to system of record verified; exclusions check (cross-customer retrieval explicitly out of scope; data older than the customer relationship start date excluded). Foundation-model training data: firm has no visibility beyond vendor system card; recorded as a known limitation, not a data-review failure.

- **Outcomes analysis scope** — faithfulness on summary outputs against held-out call records (success criterion: faithfulness rate at or above firm-policy threshold); citation precision on policy citations (success criterion: precision against ground-truth policy corpus); refusal rate on out-of-scope queries (success criterion: refusal rate at or above threshold for the named out-of-scope query set); hallucination rate on policy specifics (success criterion: zero hallucinated fees, thresholds, or policy terms in the test set); agent-edit rate as a utility-and-faithfulness proxy (sampled); latency as an SLA check.

- **Robustness scope** — direct prompt injection test (firm-internal red team plus vendor-supplied test set); indirect prompt injection test on customer-supplied content forwarded into the call record (a real attack class for this architecture); jailbreak attempts to extract PHI on unrelated claimants (n/a here, but recorded as out-of-scope to make the boundary explicit); RAG poisoning test (synthetic policy-corpus poisoning); vendor model-version swap drill (validator runs the assistant against a held-out test set under the prior version and a candidate next version, measures behaviour shift). Each test names attack class, method, success criterion, owner.

- **Fairness, explainability, transparency scope** — explainability via citation-of-source for any factual claim (intrinsic to RAG architecture; no separate post-hoc method); fairness: agent-edit rate by call-type and by inferred customer segment where lawfully tracked; UDAAP-relevant content flag rate by call-type; dialect and accent coverage on transcribed call audio (transcription error rate by inferred dialect, with the inferred-dialect classifier itself flagged as a fairness-sensitive element).

- **Ongoing monitoring scope** — faithfulness sampling (50 cases per week, owner: AI governance team, escalation to model risk committee at breach, revalidation trigger: yes if breach for two consecutive months); citation precision (50 cases per week, similar escalation, revalidation trigger: yes); cross-customer retrieval audit (continuous, owner: information security, revalidation trigger: any finding); prompt-injection signal monitoring (continuous, owner: information security, escalation to CISO, revalidation trigger: any breach); complaint-code monitoring on calls handled by the assistant (continuous, owner: consumer compliance, revalidation trigger: spike against baseline); agent-edit rate (weekly, owner: customer-support operations, revalidation trigger: drop below threshold for two consecutive months); foundation-model version monitoring (continuous, owner: vendor management, escalation to AI Governance Lead, revalidation trigger: any change-of-version notice).

- **Effective challenge questions** — eight concrete questions, each tagged to a design choice or assumption: (i) the foundation model is vendor-opaque; what is the firm's evidence base for selection that does not depend on vendor self-attestation; (ii) the agent-review gate is the only preventive control between assistant output and customer; what is the off-switch criterion if agent-edit rate falls below threshold for two consecutive months; (iii) cross-customer retrieval was found in pilot at low rate; what is the residual risk acceptance and what is the customer-notification posture under Reg P and state breach laws if it recurs in production; (iv) vendor change-of-version is a known revalidation trigger; what is the validator's escape path if vendor swaps the model without notice; (v) NYDFS October 2024 letter alignment for the NY footprint; what evidence supports the firm's posture; (vi) the inferred-dialect classifier in monitoring is itself a fairness-sensitive element; who validates that classifier and against what; (vii) prompt-injection signal monitoring is in place but the detection layer is novel; what is the validator's confidence in detection precision and recall; (viii) the assistant has zero auto-decisioning today; what is the change-management trigger if the autonomy level shifts.

- **Dependencies** — vendor system card, vendor evaluation report, vendor red-team summary, vendor contract addenda on training-data use and abuse monitoring; firm-internal red-team capacity and scheduling; held-out call record dataset for faithfulness testing; ground-truth policy corpus for citation precision testing; customer-history datastore access for cross-customer retrieval audit setup; complaint-code data feed access; access to the AI risk committee for sign-off.

- **Timeline** — 12-week initial validation cycle with milestones (vendor evidence collection and review, RAG architecture review, faithfulness and citation precision test set construction, robustness and adversarial testing, fairness review, draft validation report, AI risk committee review). Deliverables: downstream validation report, pre-prod gate input via `genai-pre-prod-review`, model card via `model-card-builder`, issue-log entries.

- **Source trace and confidence** — every scope item cited to source. Vendor evidence at low to medium confidence (vendor self-attestation); firm-internal red-team and faithfulness evidence at higher confidence; pilot evidence at medium confidence (small sample size). `[evidence needed]` flags routed to the engagement issue log: vendor model-swap operational test (vendor commitment to notice exists, operational implementation has not been tested).

#### Why this scenario matters

- It exercises the GenAI-specific pillar depth: conceptual soundness on a vendor-opaque model leans on vendor evidence review (system card, evaluation report, red-team summary) plus firm-side rationale, not on theory replication. The plan flags `vendor_model_card_review = true` and enumerates the vendor evidence in scope.
- It exercises the architecture-driven attack class catalogue: direct prompt injection, indirect prompt injection on customer-supplied content, RAG poisoning, vendor model-version swap drill. Skipping any of these would miss a real surface for this architecture.
- It exercises the validator-perspective monitoring scope: each monitoring entry has an explicit `revalidation_trigger` flag. The plan separates what triggers re-validation from what is a routine operational alert.
- It exercises the cyber cross-cutting overlay: NYDFS October 2024 letter alignment, prompt-injection signal monitoring with CISO escalation, cross-customer retrieval audit. The plan carries cyber-tagged scope items in addition to the model-risk pillars.
- It exercises the conduct cross-cutting overlay: UDAAP exposure on assistant-drafted follow-ups, complaint-code monitoring as a consumer-compliance signal.
- It exercises the chain-handoff: this plan consumes the upstream `ai-use-case-intake` and `ai-risk-tiering` artifacts; it produces inputs that `model-card-builder` and `genai-pre-prod-review` consume; the downstream validation report reads this plan as its scope contract. The plan stops at draft. The head of model risk and the AI Governance Lead jointly sign off.

## troubleshooting

### Troubleshooting: validation-plan

Recurring failure modes when a validation plan looks complete but is not. The reviewer pass should catch these; the planner pass should preempt them.

#### Validation depth set as a single label across all three pillars

Symptom: the plan reads "validation depth: full" or "validation depth: targeted" once, applied across conceptual soundness, outcomes analysis, and ongoing monitoring uniformly.

Why it happens: shorthand from the model-risk policy gets imported into the plan as a single label. The planner does not stop to think about whether each pillar warrants the same depth this cycle.

Fix: SR 11-7 §IV expects depth set per pillar with justification. Schema requires `validation_depth.conceptual_soundness`, `validation_depth.outcomes_analysis`, `validation_depth.ongoing_monitoring`, and a `tier_justification` paragraph. For an annual revalidation on a stable model, conceptual soundness is often targeted while outcomes analysis is full. For an initial validation on a vendor-opaque GenAI model, conceptual soundness pivots to vendor-evidence review while outcomes analysis is full from scratch.

#### Effective challenge questions are compliance theatre

Symptom: questions like "does the model meet our policy?", "are the controls adequate?", "is the model fit for purpose?". A senior reviewer cannot use them to challenge anything.

Why it happens: the planner treats effective-challenge questions as a closing flourish or copies them from a prior plan without re-grounding to the new model's design choices.

Fix: schema requires `effective_challenge_questions[].design_choice_or_assumption` on every entry. Each question names the specific design choice, assumption, or failure mode it interrogates. Bad: "are the controls adequate?". Good: "the agent-review gate is the only preventive control between assistant output and customer; what is the off-switch criterion if agent-edit rate falls below threshold for two consecutive months". A question that cuts and pastes to any plan is too generic.

#### Vendor-opaque foundation model treated as a black box

Symptom: GenAI plan skips conceptual soundness on the vendor model entirely, citing "we cannot retrain it". No vendor-evidence review scope, no firm-side selection rationale, no vendor red-team summary in dependencies.

Why it happens: the planner equates conceptual soundness with theory replication; without retraining capacity, the planner concludes the pillar is out of scope.

Fix: for vendor-opaque foundation models, conceptual soundness pivots to vendor-evidence review (system card, evaluation report, red-team summary) plus firm-side selection rationale. Schema field `conceptual_soundness.vendor_model_card_review` is set true, and `vendor_evidence_in_scope` enumerates what the validator will read. The pillar is not skipped; its method changes.

#### Robustness scope misses the most relevant attack class

Symptom: GenAI plan with adversarial-input testing only (the traditional ML robustness method), no direct or indirect prompt injection, no jailbreak, no RAG poisoning, no vendor model-version swap drill.

Why it happens: the planner imports the traditional-ML robustness template into a GenAI plan without re-reading the architecture flags.

Fix: attack-class catalogue is tied to architecture. For traditional ML: out-of-time backtest, stress scenario, segment robustness, adversarial input. For RAG: add direct prompt injection, indirect prompt injection on retrieved content, RAG poisoning. For agentic: add tool misuse, goal hijack. For vendor-hosted GenAI: add a vendor model-version swap drill. The cyber cross-cutting overlay catalogues the full set; load it when `scope.cross_cutting_set` includes `cyber`.

#### Monitoring scope copy-pasted from the model card

Symptom: the plan's monitoring scope is identical to the model-card monitoring section. No `revalidation_trigger` flag, no validator-perspective distinction.

Why it happens: the planner treats the model-card monitoring as authoritative and re-imports it.

Fix: schema requires `monitoring[].revalidation_trigger` on every entry. The validator's monitoring view distinguishes what triggers re-validation from what is a routine operational alert. The same metric may be both, but the trigger flag makes the seam explicit. Reviewers pulling the plan ask: "if this metric breaches, do we re-validate?". The flag answers.

#### Sector overlay loaded but ignored

Symptom: insurance pricing plan reads in fairness/bias vocabulary but never names unfair discrimination under NAIC Model #880; banking AML plan never names FFIEC manual scope; capital-markets execution-algo plan never names Rule 15c3-5 controls.

Why it happens: the sector overlay file exists in references/ but the planner treated it as background reading.

Fix: when the scope names a sector, the matching `references/sector-overlays.md#<sector>` content lands as named scope items in the plan. Effective-challenge questions probe the sector items. If the overlay is loaded but the plan has no overlay-specific scope, the loader did not run; rerun with the overlay reference in scope.

#### Source trace omits vendor evidence

Symptom: GenAI plan has full source trace on firm-supplied evidence; foundation-model facts (training cutoff, vendor evaluations, system card statements) are missing or claimed at high confidence without a pointer.

Why it happens: vendor system cards are external documents; the planner treats them as background, not as evidence.

Fix: vendor system cards and vendor evaluation reports are evidence. Cite them in source trace with confidence appropriate to vendor self-attestation (typically low to medium). Where the firm has run an independent evaluation, cite that separately at higher confidence. Do not collapse vendor and firm evidence into a single line.

#### Dependencies undercounted

Symptom: dependencies list has three items (data extract, environment, prior validation report) and the validation cycle stalls in week two when the validator discovers vendor evidence has not arrived, the cyber red-team is unscheduled, the consumer-compliance fair-lending test cycle is two months out, or the foundation-model card has not been requested from the vendor.

Why it happens: the planner thinks of dependencies as data, not as cross-function access and external evidence.

Fix: the dependencies block is for prerequisites and access needs, not just data. Include vendor evidence (system card, evaluation report, red-team summary, contract addenda); cross-function access (consumer compliance for fair-lending integration, information security for cyber tests, vendor management for vendor evidence chase, BSA officer for AML model sign-off); upstream artifacts (`ai-use-case-intake` record, `ai-risk-tiering` output, prior validation report, prior model card); environment access (validation environment, sandbox, replay capability).

#### Plan reads as scope-only, no success criteria

Symptom: outcomes-analysis entries name a test and a method, but no success criterion. The validator runs the test, produces a number, and the reviewer cannot tell whether the result is a pass or a fail.

Why it happens: the planner defers success criteria to the validation report itself, treating the plan as a scope sketch.

Fix: schema requires `outcomes_analysis[].success_criterion` and `robustness_testing[].success_criterion` on every entry. Success criteria are stated in firm-policy units (KS at or above 0.30, faithfulness at or above the firm's threshold, false-positive rate at or below the operational target). If the firm has no policy on a metric, the plan flags that gap as an effective-challenge question on the firm's threshold-setting process, not as a missing field on the plan.

#### Plan stops at draft, but the draft wraps the validation report

Symptom: the plan reads as if it has executed the validation rather than scoped it. Performance numbers, test pass or fail conclusions, recommendations.

Why it happens: the planner conflates the plan with the report; or the planner is repurposing the prior cycle's report into a new plan.

Fix: the validation plan is the validator's scope contract before testing. The downstream validation report consumes the plan and records execution. The plan does not assert results; it scopes what tests will run and what success looks like. If results are already in hand, route to the validation-report skill, not to the plan skill.

#### Tier and depth disagree silently

Symptom: tier-1 model with a light-touch plan; or tier-4 model with a full plan reading every pillar at maximum depth.

Why it happens: a single template depth is being applied across the inventory, or the tier is stale and was not consumed at plan time.

Fix: tier drives depth. Consume the `ai-risk-tiering` output as an upstream artifact; if it does not exist or is stale, route to `ai-risk-tiering` before continuing. The `tier_justification` paragraph in the plan documents how tier and validation type drove the per-pillar depth distribution; if the tier and the depth disagree, the scope wins and the disagreement goes to the issue log.
