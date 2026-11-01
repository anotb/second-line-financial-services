# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## banking-kyc-assistant

### Example: pre-prod gate review for a tier-1 KYC analyst assistant

Public-source-derived. No named institution. Pattern aligns with a US national bank holding company moving a GenAI assistant into production for the KYC analyst desk.

#### Input description

A US national bank holding company is at the initial-release pre-prod gate for a tier-1 GenAI assistant supporting the KYC analyst desk. The assistant retrieves over the firm's KYC documentation corpus, customer-relationship-history datastore, third-party adverse-media feeds, and beneficial-ownership records, and drafts narrative summaries for analyst review and sign-off. RAG over four corpora; no tools enabled. Foundation model is vendor-hosted with version pinning and contractual change-of-version notice.

Engagement scope provided by `scoping`:
- Institution type: bank holding company, large-cap, primary regulators OCC and FRB; CFPB for the consumer-banking subsidiary; NYDFS for the NY-chartered subsidiary; FinCEN for BSA/AML scope.
- Persona: AI Governance Lead (second line) consolidating; AI risk committee secretary owns the gate motion.
- Sector overlay: banking. Cross-cutting overlays: cyber (NYDFS Part 500 in NY footprint, October 2024 letter), privacy (regulated NPI), conduct loaded but light (KYC analyst is internal user, not customer-facing).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.

Upstream artifacts:
- `ai-use-case-intake`: current.
- `ai-risk-tiering`: tier-1, current.
- `ai-act-triage`: not applicable (no EU establishment in scope).
- `model-card`: current; GenAI overlay sections complete.
- `validation-plan` results: full validation completed; effective challenge questions resolved with evidence.
- `prompt-injection-review`: residual risk medium with monitoring in place; firm-internal red team complete.
- `rag-evaluation-review`: faithfulness above firm threshold; citation precision above threshold; cross-corpus leakage testing passed with two minor findings tracked to closure.
- `llm-vendor-evidence-review`: vendor system card current; swap-revalidation policy documented; vendor SOC 2 Type II current.
- `agentic-ai-controls`: not applicable (no tools, no agentic configuration).

#### Output sketch

Sections produced (abbreviated):

- **Recommended decision**: go-with-conditions. Rationale: upstream artifacts current; prompt-injection and RAG evaluation residuals accepted with monitoring; vendor evidence in place; cyber and privacy overlay sign-offs pending pending IR drill and 90-day version pinning. Three blocking conditions pre-go-live; two tracking conditions post-go-live.

- **Upstream artifact roll-up**: nine artifacts, all current; `agentic-ai-controls` and `ai-act-triage` marked not-applicable with basis.

- **Open conditions** (three blocking, two tracking):
  - Blocking, owner role AI Governance Lead with CISO function, SLA pre-prod gate +14 days, severity high: drill the IR procedure on the highest-likelihood incident class (confirmed cross-customer information bleed) before go-live; the existing IR programme has not exercised an AI-specific scenario.
  - Blocking, owner role AI Governance Lead with vendor management, SLA pre-prod gate, severity high: pin the foundation-model version for the first 90 days post-go-live; vendor's published cadence is rolling-with-30-day-notice and the firm has elected to pin during stabilisation.
  - Blocking, owner role AI governance team with model risk, SLA pre-prod gate, severity medium: document refusal-rate baseline for the first 14 days of pilot; without a baseline the post-go-live monitoring threshold has no reference.
  - Tracking, owner role AI Governance Lead, SLA go-live + 60 days, severity medium: weekly AI risk committee escalation on faithfulness sampling for the first 60 days; thereafter move to standard cadence per model card.
  - Tracking, owner role vendor management with AI Governance Lead, SLA on every change-of-version notice, severity high: re-run the prompt-injection review and the RAG evaluation faithfulness block per the foundation-model swap re-validation policy.

- **Residual risk summary** (top 4 for tier-1):
  - Indirect injection in adverse-media retrieved content. Likelihood: low (firm-internal red team coverage in place; source-vetting at the data-vendor layer). Impact: medium (analyst-facing, not customer-facing; analyst sign-off gate). Owner: AI Governance Lead, quarterly review.
  - Cross-corpus retrieval edge cases beyond those tested. Likelihood: low. Impact: high (privacy event, GLBA notification, NYDFS §500.17(a) trigger if confirmed). Owner: CISO function jointly with Privacy Officer; review on retrieval-platform configuration change.
  - Vendor foundation-model swap shifts refusal behaviour and analyst review effort goes up. Likelihood: medium (vendor cadence documented). Impact: medium. Owner: AI Governance Lead with vendor management; review on every change-of-version notice.
  - BSA/AML programme-integrity exposure if KYC narrative quality drifts. Likelihood: low (analyst sign-off gate). Impact: high (programme-integrity examination exposure). Owner: BSA officer; quarterly review with citation-precision and analyst-edit-rate signals.

- **Monitoring readiness** (six signals, all live before go-live except IR drill scope):
  - Refusal rate on out-of-scope queries; threshold drop greater than 20% week-over-week; weekly; AI governance team; escalation: model risk committee, then CISO if cyber correlates.
  - Citation precision sampling on KYC narrative source attributions; 50 cases per week; threshold precision drop greater than 5 points; weekly; AI governance team; escalation: model risk committee.
  - Cross-corpus retrieval audit (random sampling plus rule-based detection); continuous; information security with privacy officer; escalation: CISO and Privacy Officer.
  - Foundation-model version monitoring; threshold any change; continuous; vendor management; escalation: AI Governance Lead.
  - Analyst-edit rate on assistant-drafted narratives; threshold drop below 30% sustained for two periods; weekly; BSA officer with model owner; escalation: BSA committee.
  - Output-anomaly detection (length, refusal pattern); threshold greater than 3 standard deviations; continuous; information security; escalation: CISO.

- **Incident response readiness**: procedures documented in the firm IR programme; drill scheduled but not yet executed (blocking condition). Notification triggers evaluated: NYDFS Part 500 §500.17(a), GLBA Safeguards notification under 16 CFR §314.5(d), state breach laws per the firm's matrix, the 36-hour banking computer-security incident notification rule (12 CFR Part 53). Off-switch documented: pause assistant and revert to manual KYC narrative drafting.

- **Human oversight design**: KYC analyst reviews and signs the assistant-drafted narrative as the in-the-loop decision point; sampling expectation is 50 cases per week double-checked by senior analyst; effective oversight evidence is the analyst-edit-rate baseline collected during pilot; off-switch criterion is analyst-edit-rate below 30% sustained for two consecutive periods (interpreted as rubber-stamping).

- **Foundation-model dependency posture**: dependency present; provider X, model Y, version vN; pinned for first 90 days then rolling-with-notice. Swap re-validation policy: documented in change management with explicit re-run of prompt-injection review, RAG faithfulness block, and refusal-behaviour benchmark on every change-of-version notice. Vendor evidence review record on file.

- **Sector and cross-cutting overlay sign-offs**:
  - Banking (sector): pending; BSA officer signing after IR drill executes.
  - Cyber: pending; CISO function signing after IR drill executes.
  - Privacy: signed-with-conditions; Privacy Officer accepted residual risk on cross-corpus retrieval contingent on the cross-corpus retrieval audit signal staying live.
  - Conduct: not-applicable for this internal-user use case.

- **Sign-off block**: AI risk committee secretary (consolidating role), pending; model risk lead, signed; head of cyber (CISO function), pending pending IR drill; head of compliance, signed; BSA officer, pending pending IR drill and analyst-edit-rate baseline; Privacy Officer, signed-with-conditions.

- **Source trace and confidence**: upstream artifact IDs cited with attested confidence carried forward; vendor evidence at vendor-self-attestation confidence; firm-internal red-team results at high confidence.

#### Why this scenario matters

- The scenario is an archetype for the gate review: tier-1 GenAI use case where every upstream artifact is current and the gate review is the integration motion, not the diagnostic motion. Most pre-prod gate failures land here, not in artifact gaps.
- The blocking-versus-tracking distinction is load-bearing: without it, "go-with-conditions" is no-go in disguise or is permission to defer. The scenario shows three legitimate blocking items (IR drill, version pinning, baseline), and two legitimate tracking items.
- The sign-off block has six named roles, each with explicit position; the single-name sign-off failure mode is avoided by construction.
- The sector overlay (banking) brings the BSA officer in as co-signer and adds the 36-hour banking computer-security incident notification rule alongside the cyber-overlay-named NYDFS and SEC triggers; the overlay is consumed, not background reading.
- The foundation-model swap re-validation policy is explicit, with named re-run scope. Silent swap policy is the recurring defect this scenario closes by construction.

## insurance-claims-summarisation

### Example: pre-prod gate review for a tier-2 claims summarisation assistant at material expansion

Public-source-derived. No named institution. Pattern aligns with a regional life insurer expanding a claims summarisation assistant from one regional office to nationwide.

#### Input description

A regional US life insurer is at the material-expansion pre-prod gate for a tier-2 GenAI claims summarisation assistant. The assistant has been in production in one regional office for six months and is being expanded nationwide. RAG over scanned correspondence (claimant letters, third-party adjuster notes), medical records, and the firm's claims-handling policy corpus. No tools enabled. Foundation model is vendor-hosted with version pinning.

Engagement scope provided by `scoping`:
- Institution type: life insurance carrier, regional, primary regulators state insurance commissioners across operating states; NAIC AIS Program adoption status varies by state; HIPAA covered-entity status under group-health line.
- Persona: AI Governance Lead (second line) consolidating; AI risk committee owns the gate motion.
- Sector overlay: insurance. Cross-cutting overlays: cyber (state Insurance Data Security Model Law-adopting jurisdictions), privacy (PHI under HIPAA), conduct (claimant-facing communication exposure).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.

Upstream artifacts (refreshed for the expansion):
- `ai-use-case-intake`: refreshed.
- `ai-risk-tiering`: re-tiered as tier-2 (unchanged), current.
- `ai-act-triage`: not applicable.
- `model-card`: refreshed for the expansion (new corpora scope, new state-by-state notification matrix).
- `validation-plan` results: targeted validation focused on cross-regional faithfulness drift and refusal-posture stability across state-specific procedural variations.
- `prompt-injection-review`: refreshed; indirect injection in scanned correspondence remains the primary residual.
- `rag-evaluation-review`: refreshed; cross-claim leakage scoping retested under nationwide retrieval scoping rules; one finding open.
- `llm-vendor-evidence-review`: current.
- `agentic-ai-controls`: not applicable.

#### Output sketch

Sections produced (abbreviated):

- **Recommended decision**: hold. Rationale: cross-claim leakage finding from refreshed `rag-evaluation-review` is unresolved; PHI cross-claim audit log retention is below required state-by-state minima for two states in the expansion footprint; complaint-channel readiness has not been documented per state. The combination of an open privacy-relevant retrieval finding and unverified state-by-state notification readiness is hold, not go-with-conditions.

- **Upstream artifact roll-up**: nine artifacts; `rag-evaluation-review` shows one open finding flagged in the notes column; the rest current.

- **Open conditions** (four blocking, two tracking):
  - Blocking, owner role retrieval platform owner with Privacy Officer, SLA pre-prod gate, severity high: extend PHI cross-claim audit log retention to required state-by-state minima for the two affected states; the audit-log retention is the load-bearing control for the cross-claim retrieval audit signal.
  - Blocking, owner role consumer compliance with state-by-state operations, SLA pre-prod gate, severity medium: document complaint-channel readiness per state (the existing channel runs through the regional office; the nationwide expansion needs a state-by-state escalation matrix).
  - Blocking, owner role retrieval platform owner with AI Governance Lead, SLA pre-prod gate, severity high: close the cross-claim leakage finding from refreshed `rag-evaluation-review`; either resolve at the retrieval scoping layer or accept formally with named owner if firm policy permits acceptance for that finding class.
  - Blocking, owner role AI Governance Lead with state compliance, SLA pre-prod gate +30 days, severity medium: confirm AIS Program documentation per NAIC Model Bulletin in each adopting state; the existing documentation covers the home state only.
  - Tracking, owner role AI Governance Lead, SLA go-live +90 days, severity medium: re-run cross-regional faithfulness drift monitoring and report to AI risk committee.
  - Tracking, owner role vendor management with AI Governance Lead, SLA on every change-of-version notice, severity high: re-run the prompt-injection review and the RAG evaluation faithfulness block per the foundation-model swap re-validation policy.

- **Residual risk summary** (top four for tier-2 expansion):
  - Indirect injection in OCR'd scanned correspondence. Likelihood: medium (OCR-stage sanitisation in place; adversarial parties have access to claim file in adjudication). Impact: medium (claim-handler-facing, not claimant-facing; claim handler reviews summary). Owner: AI Governance Lead, quarterly review.
  - Cross-claim PHI retrieval edge cases. Likelihood: medium (open finding; mitigation plan in flight). Impact: high (HIPAA breach notification, state Insurance Data Security Model Law triggers per state). Owner: Privacy Officer with CISO function; review on every retrieval-platform configuration change.
  - State unfair-discrimination exposure if summary content shifts material claim decisions. Likelihood: low (claim-handler decision-of-record, not assistant decision; sampling shows assistant content rarely changes claim outcome). Impact: medium. Owner: chief actuarial officer with consumer compliance; quarterly review.
  - Vendor foundation-model swap shifts refusal behaviour and the cross-state procedural variations are no longer handled correctly. Likelihood: medium. Impact: medium. Owner: AI Governance Lead with vendor management; review on every change-of-version notice.

- **Monitoring readiness** (seven signals): refusal rate, citation precision on policy facts, cross-claim retrieval audit, OCR-stage anomaly rate, foundation-model version monitoring, claim-handler-edit rate, complaint-rate by state. The cross-claim retrieval audit is dependent on the audit-log retention extension; flagged as `live_before_golive = no` until the blocking condition closes.

- **Incident response readiness**: procedures documented; last drilled six months ago for the regional-office scope; drill scope did not exercise nationwide complaint-channel routing or state-by-state notification handoff. Regulator-notification triggers evaluated: HIPAA breach notification (45 CFR §§164.400-414), state Insurance Data Security Model Law per adopting state, state breach laws per state, NYDFS §500.17(a) for NY-licensed entity status. Off-switch documented: pause assistant in the affected state(s) and revert to manual claim summarisation.

- **Human oversight design**: claim handler reviews assistant-drafted summary as the in-the-loop decision point; sampling expectation is 25 cases per week per state, double-checked by claim supervisor; effective oversight evidence is the claim-handler-edit-rate baseline carried forward from the regional pilot, refreshed during nationwide pilot phase; off-switch criterion is claim-handler-edit-rate below 25% sustained for two consecutive periods.

- **Foundation-model dependency posture**: dependency present; pinned. Swap re-validation policy documented; vendor evidence review record current.

- **Sector and cross-cutting overlay sign-offs**:
  - Insurance (sector): pending; chief actuarial officer pending the AIS Program documentation completion in adopting states; consumer compliance pending the complaint-channel readiness documentation.
  - Cyber: signed-with-conditions; CISO function accepted contingent on the cross-claim audit-log retention extension.
  - Privacy: pending; Privacy Officer pending the cross-claim leakage finding closure.
  - Conduct: pending; consumer compliance pending the state-by-state complaint-channel readiness.

- **Sign-off block**: AI risk committee secretary (consolidating role), pending; model risk lead, signed; CISO function, signed-with-conditions; Privacy Officer, pending; consumer compliance, pending; chief actuarial officer, pending. State-level compliance sign-off pending in the affected states.

- **Source trace and confidence**: upstream artifact IDs cited with attested confidence carried forward; refreshed `rag-evaluation-review` finding cited at high confidence with mitigation plan reference; state-by-state notification matrix cited at firm-policy confidence.

#### Why this scenario matters

- The scenario is the archetype for material-expansion pre-prod gate review: the use case is in production at one scope, the expansion changes the corpora scope, the privacy and notification footprint, and the operational handoff. Treating a material expansion as a copy-paste of the prior gate decision is the recurring failure mode.
- The hold call is principled: an open privacy-relevant retrieval finding combined with unverified state-by-state notification readiness is hold, not go-with-conditions. The skill enforces "go-with-conditions equivalent to no-go in disguise" by structure.
- The sector overlay (insurance) brings the chief actuarial officer and consumer compliance in as co-signers, surfaces HIPAA and state Insurance Data Security Model Law triggers alongside the cyber-overlay-named ones, and adds the AIS Program documentation expectation per state.
- The monitoring-readiness section flags the audit-log retention dependency: a signal listed as live but blocked on a policy-control change is not actually live before go-live. The structure surfaces the dependency by construction.
- Sign-off block has multiple pending entries from named roles, each tied to a specific blocking condition; pending sign-off is recorded explicitly rather than absent.

## troubleshooting

### Troubleshooting: genai-pre-prod-review

Recurring defects from pre-prod gate reviews and how to address them. Read alongside the spec sheet's common-pitfalls list and the loaded sector and cross-cutting overlays.

#### Gate review proceeds without one or more upstream artifacts

The roll-up is the gate review's spine. If the model card is stale, the validation-plan results are missing, the prompt-injection review has not been run, or the RAG evaluation has not been refreshed for the architecture in scope, the gate decision is asserting coverage the upstream work does not support.

Fix: the upstream-artifact roll-up section requires status on every relevant artifact. Any status of `stale` or `missing` blocks `go` by policy. The decision is `hold` until the upstream work is current, or the scope of the gate review is reduced to the artifacts that are current and the missing scope is recorded as out-of-scope for this gate. Reducing scope is preferable to defaulting to go.

#### Open conditions listed without owners or SLAs

Conditions without owners and SLAs become forever-open. The committee marks the gate "go-with-conditions" and six months later the conditions are still open, the use case is in production, and the conditions are now incident-history.

Fix: each open-condition entry requires owner role (function, never an individual), SLA (date or named milestone like pre-prod gate or go-live + 30 days), severity, and an explicit blocking-versus-tracking flag. Missing fields fail the review. Critical-severity items typically block go.

#### "Go" with a long blocking-condition list (no-go in disguise)

A `go` recommendation paired with five blocking conditions is `no-go in disguise` and signals that the reviewer wanted to issue go and worked around the substantive position by routing the conditions through the conditions section. The committee reads "go" as approved; the conditions land as routine.

Fix: if any condition is blocking, the recommended decision is `go_with_conditions` or `hold`, not `go`. The blocking-versus-tracking section makes this explicit. When blocking conditions are material to the use case operating safely, the decision moves to `hold` until they close.

#### Foundation-model swap re-validation policy is silent

The model card and the validation plan name foundation-model swap as a re-validation trigger. The vendor change-of-version notice is the operational moment the trigger fires. Without a documented swap re-validation policy, the firm has the trigger and no playbook; the trigger fires and nothing happens.

Fix: when `foundation_model_posture.dependency_present = true`, the `swap_revalidation_policy` field is required and names the explicit re-run scope (which upstream reviews re-run, on what cadence, with what owner). An unstated policy on a foundation-model-dependent system is itself a critical-severity finding and blocks `go`.

#### Monitoring listed as live but the dependency is not

A signal listed as `live_before_golive = true` may depend on a control or configuration change that has not landed. A cross-customer retrieval audit signal needs the audit-log retention; a citation-precision signal needs the sampling pipeline; a foundation-model version signal needs the vendor-management notification feed.

Fix: each `monitoring_readiness[]` entry that depends on an upstream change records the dependency in the notes column. A signal blocked on a dependency is not live; mark `live_before_golive = false` and add the dependency to open conditions.

#### Incident-response procedures documented but not drilled for an AI-specific scenario

The firm IR programme exists; the AI-specific incident classes (confirmed cross-customer information bleed, confirmed indirect-injection-driven misrouted action, suspected RAG corpus poisoning, foundation-model behaviour shift suggesting upstream compromise) have not been exercised. The first AI-specific incident is the drill.

Fix: `incident_response_readiness.last_drilled` records the date and `drill_scope` records which incident classes were exercised. If the drill scope does not include the highest-likelihood AI-specific incident class for the architecture, the gate is `hold` candidate until the drill executes; alternatively the IR drill is a critical-severity blocking condition.

#### Single-name sign-off block on a tier-1 or tier-2 use case

A sign-off block with one name reads to the committee as broader sign-off than exists. The cyber lens, the privacy lens, the consumer-compliance lens, the BSA lens, the actuarial lens, the legal lens: each has its own seam and its own residual-risk concerns. One name signs for one of those.

Fix: the `signoff[]` array requires named reviewers across the relevant functions per the loaded overlays. For a banking customer-facing GenAI use case the standard set is AI Governance Lead, model risk lead, CISO function, consumer compliance, Privacy Officer, BSA officer if AML touch, legal. For an insurance use case substitute chief actuarial officer and add state-level compliance. Dissent is recorded explicitly with a basis; the gate decision proceeds with the dissent visible.

#### Human oversight design names a decision point but no off-switch criterion

"Human-in-the-loop with agent review" sounds preventive; in practice the gate becomes rubber-stamping under volume pressure. Without an off-switch criterion (e.g., agent-edit rate falling below a threshold for two periods), the human-in-the-loop control degrades silently.

Fix: `human_oversight.off_switch_criterion` is required for any tier-1 or tier-2 use case with a human-in-the-loop or human-on-the-loop design. The criterion names the operational signal and the threshold that takes the system back to manual. Without it, the human oversight is recorded as nominal, not effective, and routes to open conditions.

#### Sector or cross-cutting overlay loaded but the seam not surfaced

Each loaded overlay carries seams the gate review tends to miss without the overlay (banking BSA officer co-sign and 36-hour banking computer-security incident notification rule; insurance HIPAA and AIS Program documentation; capital markets Marketing Rule reach and surveillance-system adjacency; payments-fintech sponsor-bank co-acceptance; cyber regulator-notification triggers and CISO co-review; privacy notification timelines; conduct UDAAP exposure on customer-facing communications). Loading the overlay without surfacing the seam in the sign-off block, the conditions, or the residual risk is the failure mode.

Fix: re-read each loaded overlay against the review and confirm each named overlay-specific consideration is reflected in the open-conditions, residual-risk, monitoring-readiness, incident-response-readiness, or overlay-signoffs sections. The `overlay_signoffs[]` array lists every loaded overlay with status, including those still pending.

#### Engagement scope not formalised

When the scope record is not supplied and the practitioner declines to formalise scope, the review still proceeds against a default public posture but should record the omission.

Fix: the gate-metadata section notes that scope was not formalised; the open-conditions section includes formalising scope as a low-or-medium-severity item; the source-trace confidence labels reflect the lack of formalised scope on items that would have been resolved by it.

#### Material-expansion gate treated as a copy-paste of the initial-release gate

A material expansion (new user population, new tool, new corpus, new geography) changes the threat surface, the residual risk, and often the regulator-notification footprint. Treating the expansion gate as a refresh of the initial-release gate without re-running the upstream artifacts is the recurring defect for second-and-third-gate reviews.

Fix: for `gate_type = material_expansion`, the upstream-artifact roll-up records the refresh status of each artifact against the expanded scope. Stale-relative-to-the-expansion artifacts are recorded as `stale` even if they were current for the original scope. The model card, the prompt-injection review, the RAG evaluation, and the validation-plan results are typically the artifacts that need refresh on material expansion.
