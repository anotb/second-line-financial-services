# Troubleshooting: genai-pre-prod-review

Recurring defects from pre-prod gate reviews and how to address them. Read alongside the spec sheet's common-pitfalls list and the loaded sector and cross-cutting overlays.

## Gate review proceeds without one or more upstream artifacts

The roll-up is the gate review's spine. If the model card is stale, the validation-plan results are missing, the prompt-injection review has not been run, or the RAG evaluation has not been refreshed for the architecture in scope, the gate decision is asserting coverage the upstream work does not support.

Fix: the upstream-artifact roll-up section requires status on every relevant artifact. Any status of `stale` or `missing` blocks `go` by policy. The decision is `hold` until the upstream work is current, or the scope of the gate review is reduced to the artifacts that are current and the missing scope is recorded as out-of-scope for this gate. Reducing scope is preferable to defaulting to go.

## Open conditions listed without owners or SLAs

Conditions without owners and SLAs become forever-open. The committee marks the gate "go-with-conditions" and six months later the conditions are still open, the use case is in production, and the conditions are now incident-history.

Fix: each open-condition entry requires owner role (function, never an individual), SLA (date or named milestone like pre-prod gate or go-live + 30 days), severity, and an explicit blocking-versus-tracking flag. Missing fields fail the review. Critical-severity items typically block go.

## "Go" with a long blocking-condition list (no-go in disguise)

A `go` recommendation paired with five blocking conditions is `no-go in disguise` and signals that the reviewer wanted to issue go and worked around the substantive position by routing the conditions through the conditions section. The committee reads "go" as approved; the conditions land as routine.

Fix: if any condition is blocking, the recommended decision is `go_with_conditions` or `hold`, not `go`. The blocking-versus-tracking section makes this explicit. When blocking conditions are material to the use case operating safely, the decision moves to `hold` until they close.

## Foundation-model swap re-validation policy is silent

The model card and the validation plan name foundation-model swap as a re-validation trigger. The vendor change-of-version notice is the operational moment the trigger fires. Without a documented swap re-validation policy, the firm has the trigger and no playbook; the trigger fires and nothing happens.

Fix: when `foundation_model_posture.dependency_present = true`, the `swap_revalidation_policy` field is required and names the explicit re-run scope (which upstream reviews re-run, on what cadence, with what owner). An unstated policy on a foundation-model-dependent system is itself a critical-severity finding and blocks `go`.

## Monitoring listed as live but the dependency is not

A signal listed as `live_before_golive = true` may depend on a control or configuration change that has not landed. A cross-customer retrieval audit signal needs the audit-log retention; a citation-precision signal needs the sampling pipeline; a foundation-model version signal needs the vendor-management notification feed.

Fix: each `monitoring_readiness[]` entry that depends on an upstream change records the dependency in the notes column. A signal blocked on a dependency is not live; mark `live_before_golive = false` and add the dependency to open conditions.

## Incident-response procedures documented but not drilled for an AI-specific scenario

The firm IR programme exists; the AI-specific incident classes (confirmed cross-customer information bleed, confirmed indirect-injection-driven misrouted action, suspected RAG corpus poisoning, foundation-model behaviour shift suggesting upstream compromise) have not been exercised. The first AI-specific incident is the drill.

Fix: `incident_response_readiness.last_drilled` records the date and `drill_scope` records which incident classes were exercised. If the drill scope does not include the highest-likelihood AI-specific incident class for the architecture, the gate is `hold` candidate until the drill executes; alternatively the IR drill is a critical-severity blocking condition.

## Single-name sign-off block on a tier-1 or tier-2 use case

A sign-off block with one name reads to the committee as broader sign-off than exists. The cyber lens, the privacy lens, the consumer-compliance lens, the BSA lens, the actuarial lens, the legal lens — each has its own seam and its own residual-risk concerns. One name signs for one of those.

Fix: the `signoff[]` array requires named reviewers across the relevant functions per the loaded overlays. For a banking customer-facing GenAI use case the standard set is AI Governance Lead, model risk lead, CISO function, consumer compliance, Privacy Officer, BSA officer if AML touch, legal. For an insurance use case substitute chief actuarial officer and add state-level compliance. Dissent is recorded explicitly with a basis; the gate decision proceeds with the dissent visible.

## Human oversight design names a decision point but no off-switch criterion

"Human-in-the-loop with agent review" sounds preventive; in practice the gate becomes rubber-stamping under volume pressure. Without an off-switch criterion (e.g., agent-edit rate falling below a threshold for two periods), the human-in-the-loop control degrades silently.

Fix: `human_oversight.off_switch_criterion` is required for any tier-1 or tier-2 use case with a human-in-the-loop or human-on-the-loop design. The criterion names the operational signal and the threshold that takes the system back to manual. Without it, the human oversight is recorded as nominal, not effective, and routes to open conditions.

## Sector or cross-cutting overlay loaded but the seam not surfaced

Each loaded overlay carries seams the gate review tends to miss without the overlay (banking BSA officer co-sign and 36-hour banking computer-security incident notification rule; insurance HIPAA and AIS Program documentation; capital markets Marketing Rule reach and surveillance-system adjacency; payments-fintech sponsor-bank co-acceptance; cyber regulator-notification triggers and CISO co-review; privacy notification timelines; conduct UDAAP exposure on customer-facing communications). Loading the overlay without surfacing the seam in the sign-off block, the conditions, or the residual risk is the failure mode.

Fix: re-read each loaded overlay against the review and confirm each named overlay-specific consideration is reflected in the open-conditions, residual-risk, monitoring-readiness, incident-response-readiness, or overlay-signoffs sections. The `overlay_signoffs[]` array lists every loaded overlay with status, including those still pending.

## Engagement scope not formalised

When the engagement-scope record is not supplied and the practitioner declines to formalise scope, the review still proceeds against a default public posture but should record the omission.

Fix: the gate-metadata section notes that engagement scope was not formalised; the open-conditions section includes formalising engagement scope as a low-or-medium-severity item; the source-trace confidence labels reflect the lack of formalised scope on items that would have been resolved by it.

## Material-expansion gate treated as a copy-paste of the initial-release gate

A material expansion (new user population, new tool, new corpus, new geography) changes the threat surface, the residual risk, and often the regulator-notification footprint. Treating the expansion gate as a refresh of the initial-release gate without re-running the upstream artifacts is the recurring defect for second-and-third-gate reviews.

Fix: for `gate_type = material_expansion`, the upstream-artifact roll-up records the refresh status of each artifact against the expanded scope. Stale-relative-to-the-expansion artifacts are recorded as `stale` even if they were current for the original scope. The model card, the prompt-injection review, the RAG evaluation, and the validation-plan results are typically the artifacts that need refresh on material expansion.
