# Troubleshooting: validation-plan

Recurring failure modes when a validation plan looks complete but is not. The reviewer pass should catch these; the planner pass should preempt them.

## Validation depth set as a single label across all three pillars

Symptom: the plan reads "validation depth: full" or "validation depth: targeted" once, applied across conceptual soundness, outcomes analysis, and ongoing monitoring uniformly.

Why it happens: shorthand from the model-risk policy gets imported into the plan as a single label. The planner does not stop to think about whether each pillar warrants the same depth this cycle.

Fix: SR 11-7 §IV expects depth set per pillar with justification. Schema requires `validation_depth.conceptual_soundness`, `validation_depth.outcomes_analysis`, `validation_depth.ongoing_monitoring`, and a `tier_justification` paragraph. For an annual revalidation on a stable model, conceptual soundness is often targeted while outcomes analysis is full. For an initial validation on a vendor-opaque GenAI model, conceptual soundness pivots to vendor-evidence review while outcomes analysis is full from scratch.

## Effective challenge questions are compliance theatre

Symptom: questions like "does the model meet our policy?", "are the controls adequate?", "is the model fit for purpose?". A senior reviewer cannot use them to challenge anything.

Why it happens: the planner treats effective-challenge questions as a closing flourish or copies them from a prior plan without re-grounding to the new model's design choices.

Fix: schema requires `effective_challenge_questions[].design_choice_or_assumption` on every entry. Each question names the specific design choice, assumption, or failure mode it interrogates. Bad: "are the controls adequate?". Good: "the agent-review gate is the only preventive control between assistant output and customer; what is the off-switch criterion if agent-edit rate falls below threshold for two consecutive months". A question that cuts and pastes to any plan is too generic.

## Vendor-opaque foundation model treated as a black box

Symptom: GenAI plan skips conceptual soundness on the vendor model entirely, citing "we cannot retrain it". No vendor-evidence review scope, no firm-side selection rationale, no vendor red-team summary in dependencies.

Why it happens: the planner equates conceptual soundness with theory replication; without retraining capacity, the planner concludes the pillar is out of scope.

Fix: for vendor-opaque foundation models, conceptual soundness pivots to vendor-evidence review (system card, evaluation report, red-team summary) plus firm-side selection rationale. Schema field `conceptual_soundness.vendor_model_card_review` is set true, and `vendor_evidence_in_scope` enumerates what the validator will read. The pillar is not skipped; its method changes.

## Robustness scope misses the most relevant attack class

Symptom: GenAI plan with adversarial-input testing only (the traditional ML robustness method), no direct or indirect prompt injection, no jailbreak, no RAG poisoning, no vendor model-version swap drill.

Why it happens: the planner imports the traditional-ML robustness template into a GenAI plan without re-reading the architecture flags.

Fix: attack-class catalogue is tied to architecture. For traditional ML: out-of-time backtest, stress scenario, segment robustness, adversarial input. For RAG: add direct prompt injection, indirect prompt injection on retrieved content, RAG poisoning. For agentic: add tool misuse, goal hijack. For vendor-hosted GenAI: add a vendor model-version swap drill. The cyber cross-cutting overlay catalogues the full set; load it when `scope.cross_cutting_set` includes `cyber`.

## Monitoring scope copy-pasted from the model card

Symptom: the plan's monitoring scope is identical to the model-card monitoring section. No `revalidation_trigger` flag, no validator-perspective distinction.

Why it happens: the planner treats the model-card monitoring as authoritative and re-imports it.

Fix: schema requires `monitoring[].revalidation_trigger` on every entry. The validator's monitoring view distinguishes what triggers re-validation from what is a routine operational alert. The same metric may be both, but the trigger flag makes the seam explicit. Reviewers pulling the plan ask: "if this metric breaches, do we re-validate?". The flag answers.

## Sector overlay loaded but ignored

Symptom: insurance pricing plan reads in fairness/bias vocabulary but never names unfair discrimination under NAIC Model #880; banking AML plan never names FFIEC manual scope; capital-markets execution-algo plan never names Rule 15c3-5 controls.

Why it happens: the sector overlay file exists in references/ but the planner treated it as background reading.

Fix: when the scope names a sector, the matching `references/sector-overlays/<sector>.md` content lands as named scope items in the plan. Effective-challenge questions probe the sector items. If the overlay is loaded but the plan has no overlay-specific scope, the loader did not run; rerun with the overlay reference in scope.

## Source trace omits vendor evidence

Symptom: GenAI plan has full source trace on firm-supplied evidence; foundation-model facts (training cutoff, vendor evaluations, system card statements) are missing or claimed at high confidence without a pointer.

Why it happens: vendor system cards are external documents; the planner treats them as background, not as evidence.

Fix: vendor system cards and vendor evaluation reports are evidence. Cite them in source trace with confidence appropriate to vendor self-attestation (typically low to medium). Where the firm has run an independent evaluation, cite that separately at higher confidence. Do not collapse vendor and firm evidence into a single line.

## Dependencies undercounted

Symptom: dependencies list has three items (data extract, environment, prior validation report) and the validation cycle stalls in week two when the validator discovers vendor evidence has not arrived, the cyber red-team is unscheduled, the consumer-compliance fair-lending test cycle is two months out, or the foundation-model card has not been requested from the vendor.

Why it happens: the planner thinks of dependencies as data, not as cross-function access and external evidence.

Fix: the dependencies block is for prerequisites and access needs, not just data. Include vendor evidence (system card, evaluation report, red-team summary, contract addenda); cross-function access (consumer compliance for fair-lending integration, information security for cyber tests, vendor management for vendor evidence chase, BSA officer for AML model sign-off); upstream artifacts (`ai-use-case-intake` record, `ai-risk-tiering` output, prior validation report, prior model card); environment access (validation environment, sandbox, replay capability).

## Plan reads as scope-only, no success criteria

Symptom: outcomes-analysis entries name a test and a method, but no success criterion. The validator runs the test, produces a number, and the reviewer cannot tell whether the result is a pass or a fail.

Why it happens: the planner defers success criteria to the validation report itself, treating the plan as a scope sketch.

Fix: schema requires `outcomes_analysis[].success_criterion` and `robustness_testing[].success_criterion` on every entry. Success criteria are stated in firm-policy units (KS at or above 0.30, faithfulness at or above the firm's threshold, false-positive rate at or below the operational target). If the firm has no policy on a metric, the plan flags that gap as an effective-challenge question on the firm's threshold-setting process, not as a missing field on the plan.

## Plan stops at draft, but the draft wraps the validation report

Symptom: the plan reads as if it has executed the validation rather than scoped it. Performance numbers, test pass or fail conclusions, recommendations.

Why it happens: the planner conflates the plan with the report; or the planner is repurposing the prior cycle's report into a new plan.

Fix: the validation plan is the validator's scope contract before testing. The downstream validation report consumes the plan and records execution. The plan does not assert results; it scopes what tests will run and what success looks like. If results are already in hand, route to the validation-report skill, not to the plan skill.

## Tier and depth disagree silently

Symptom: tier-1 model with a light-touch plan; or tier-4 model with a full plan reading every pillar at maximum depth.

Why it happens: a single template depth is being applied across the inventory, or the tier is stale and was not consumed at plan time.

Fix: tier drives depth. Consume the `ai-risk-tiering` output as an upstream artifact; if it does not exist or is stale, route to `ai-risk-tiering` before continuing. The `tier_justification` paragraph in the plan documents how tier and validation type drove the per-pillar depth distribution; if the tier and the depth disagree, the scope wins and the disagreement goes to the issue log.
