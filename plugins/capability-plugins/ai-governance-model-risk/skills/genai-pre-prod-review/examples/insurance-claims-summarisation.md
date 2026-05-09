# Example: pre-prod gate review for a tier-2 claims summarisation assistant at material expansion

Public-source-derived. No named institution. Pattern aligns with a regional life insurer expanding a claims summarisation assistant from one regional office to nationwide.

## Input description

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

## Output sketch

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

## Why this scenario matters

- The scenario is the v1 archetype for material-expansion pre-prod gate review: the use case is in production at one scope, the expansion changes the corpora scope, the privacy and notification footprint, and the operational handoff. Treating a material expansion as a copy-paste of the prior gate decision is the recurring failure mode.
- The hold call is principled: an open privacy-relevant retrieval finding combined with unverified state-by-state notification readiness is hold, not go-with-conditions. The skill enforces "go-with-conditions equivalent to no-go in disguise" by structure.
- The sector overlay (insurance) brings the chief actuarial officer and consumer compliance in as co-signers, surfaces HIPAA and state Insurance Data Security Model Law triggers alongside the cyber-overlay-named ones, and adds the AIS Program documentation expectation per state.
- The monitoring-readiness section flags the audit-log retention dependency: a signal listed as live but blocked on a policy-control change is not actually live before go-live. The structure surfaces the dependency by construction.
- Sign-off block has multiple pending entries from named roles, each tied to a specific blocking condition; pending sign-off is recorded explicitly rather than absent.
