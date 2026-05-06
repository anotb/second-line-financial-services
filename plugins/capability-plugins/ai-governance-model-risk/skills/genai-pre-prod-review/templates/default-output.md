# GenAI pre-prod gate review: [use case name and version]

Starting structure for the second-line pre-prod gate review memo. Depth flexes with tier, gate type, and audience; the section list does not. A tier-2 initial-release review compresses; a tier-1 agentic system with cyber overlay and material-expansion scope expands. Items without evidence carry `[evidence needed]` and route to open conditions, not silently into the memo.

The memo is a draft until the human reviewers attest. The decision is a recommendation; the AI risk committee owns the gate.

---

## 1. Gate metadata

- Gate ID: [canonical ID]
- Gate type: [initial_release / material_expansion / recurring_revalidation / regulatory_response]
- Use case ID (links to `ai-use-case-intake`): [ID]
- Tier (per `ai-risk-tiering`): [tier-1 / tier-2 / tier-3 / tier-4]
- Lifecycle stage: [development / pre-prod / prod / monitoring-only]
- Engagement-scope ID (if `engagement-scoping` was run): [ID]
- Requested date: [YYYY-MM-DD]
- Review date: [YYYY-MM-DD]
- Recommended decision date: [YYYY-MM-DD]
- Reviewer role consolidating the memo: [AI Governance Lead / AI risk committee secretary]

---

## 2. Recommended decision

**Decision**: [go / go-with-conditions / hold / no-go]

**Rationale**: [one paragraph, regulator-readable. Names the conditions that drove the call. For go-with-conditions, identifies which conditions are blocking and which are tracking; "go" with a long blocking list is no-go in disguise.]

**Blocking versus tracking**: [explicit list when decision is go-with-conditions; cross-references the open-conditions section.]

---

## 3. Upstream artifact roll-up

For each artifact:

| Artifact | Status | Last updated | Link | Notes |
|---|---|---|---|---|
| ai-use-case-intake | [current / stale / missing / not-applicable] | [YYYY-MM-DD] | [ID or path] | |
| ai-risk-tiering | | | | |
| ai-act-triage (if EU AI Act in scope) | | | | |
| model-card | | | | |
| validation-plan results | | | | |
| prompt-injection-review (if GenAI threat surface relevant) | | | | |
| rag-evaluation-review (if RAG architecture) | | | | |
| llm-vendor-evidence-review (if foundation-model dependence) | | | | |
| agentic-ai-controls (if agentic configuration) | | | | |

Any artifact `stale` or `missing` reflects in the recommended decision; the gate review does not assert coverage that the upstream artifacts do not support. Artifacts marked `not-applicable` carry a one-line basis in the notes column (e.g., "no RAG corpus in this architecture").

---

## 4. Open conditions and named gates

For each condition:

| Condition | Owner role | SLA | Severity | Blocking? |
|---|---|---|---|---|
| [concrete condition] | [function, never an individual] | [date or milestone] | [low / medium / high / critical] | [yes / no] |

Conditions without owners and SLAs become forever-open; missing fields fail the review. Critical-severity items typically block go.

The standard condition that fires for any architecture depending on a third-party foundation model is the foundation-model swap re-validation policy: an explicit re-run of the relevant upstream reviews on every vendor change-of-version notice. Missing this condition on a foundation-model-dependent system is itself a finding.

---

## 5. Residual risk summary

The top three to five named residual risks for tier-2; more for tier-1.

| Risk | Likelihood | Impact | Basis | Accepted owner role | Review cadence |
|---|---|---|---|---|---|
| [concrete description] | [low / medium / high] | [low / medium / high] | [one-line basis] | [role] | [quarterly / on foundation-model swap / etc.] |

"Low" without a basis is opinion. The basis column is required and typically references the upstream artifact (model card, prompt-injection review, RAG evaluation) that establishes the rating.

---

## 6. Monitoring readiness

For each signal that must be live before go:

| Signal | Threshold | Frequency | Live before go-live? | Owner role | Escalation path |
|---|---|---|---|---|---|
| [name] | [in firm policy units] | [continuous / daily / weekly] | [yes / no] | [function] | [named committee, officer, or process] |

The model card and the validation plan name the signals; this section is the gate review's confirmation that the signals are operational, not aspirational. A `live_before_golive = no` entry is an open condition unless the signal is post-go-live by design.

---

## 7. Incident response readiness

- **Procedures documented**: [yes / no, with pointer to the named runbook]
- **Last drilled**: [YYYY-MM-DD]; drill scope: [incident classes exercised]
- **Regulator-notification triggers evaluated**: [list per loaded overlays; e.g., NYDFS Part 500 §500.17(a) for NY-footprint covered entities, SEC 8-K Item 1.05 for public registrants, GLBA Safeguards Rule, state breach laws, the 36-hour banking computer-security incident notification rule, sector-specific notifications]
- **Off-switch documented and exercised**: [yes / no]

A pre-prod gate without a drilled incident-response procedure on the highest-likelihood incident class for the architecture is a `hold` candidate, not a `go-with-conditions` candidate.

---

## 8. Human oversight design

- **Decision points**: [named human-in-the-loop or human-on-the-loop points; e.g., agent reviews and sends customer communication; underwriter overrides recommendation; analyst signs final SAR narrative]
- **Sampling expectation**: [cadence and scope for output review and override audit]
- **Effective oversight evidence**: [training records, sampling results, override-rate baseline; the test for "effective" challenge under SR 11-7 §IV.5 has analogue here for human oversight]
- **Off-switch criterion**: [the operational decision that takes the system back to manual when oversight breaks down; e.g., agent-edit rate below threshold for two consecutive periods]

For tier-1 and tier-2 use cases the human oversight section runs full; for tier-3 and tier-4 it can compress.

---

## 9. Foundation-model dependency posture

- **Dependency present**: [yes / no]
- If yes: provider, model name, version, version pinning posture (pinned / floating / rolling-with-notice / unknown)
- **Swap re-validation policy**: [documented policy for re-validation on vendor change-of-version notice; pointer to change-management entry]
- **Vendor evidence review** (links to `llm-vendor-evidence-review`): [ID]

If `dependency_present = yes` and `swap_revalidation_policy` is silent, the gate review is `hold` until the policy is documented; an unstated policy is an unstated control.

---

## 10. Sector and cross-cutting overlay sign-offs

For each loaded overlay:

| Overlay | Owner role | Status | Notes |
|---|---|---|---|
| [banking / insurance / capital-markets / payments-fintech] | [function] | [signed / pending / dissent / not-applicable] | |
| [cyber / privacy / conduct] | [function] | | |

Loaded overlays are listed even when status is pending; an unstated pending status reads as oversight. Climate is not applicable to pre-prod gate reviews.

---

## 11. Sign-off block

The gate review is reviewable when sections 2 through 10 are filled and source trace is complete. Named reviewers attest:

| Reviewer role | Function | Decision date | Position | Basis |
|---|---|---|---|---|
| [role] | [AI governance / model risk / cyber / compliance / privacy / consumer compliance / BSA / legal] | [YYYY-MM-DD] | [signed / signed-with-conditions / dissent / pending] | [one-line basis; required for dissent] |

A single-name sign-off block on a tier-1 or tier-2 GenAI use case is itself a finding. The committee assumes broader sign-off than exists when only one role is named. Dissent is recorded explicitly with a basis; the gate decision proceeds with the dissent visible to the committee.

---

## 12. Source trace and confidence

For every material claim:

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| [claim] | [upstream artifact ID, document, system, vendor evidence, or `[evidence needed]`] | [pointer] | [high / medium / low / evidence-needed] |

Vendor self-attestation carries vendor-self-attestation confidence (typically low to medium). Upstream artifacts that are themselves source-traced (model card, validation plan results, prompt-injection review) carry their attested confidence forward; do not over-claim. `[evidence needed]` flags route to open conditions.

---

## Onward routing

After attestation:

- **AI risk committee**: receives the recommended decision and the open conditions.
- **MRMO and the model owner**: receive the residual-risk summary and any blocking conditions assigned to them.
- **Regulator response file** (if `regulatory_response` gate type or if the use case is examiner-relevant): receives the full memo with source trace.
- **Board pack** (if tier-1 or tier-2 with material residual risk): the `board-ai-risk-pack` skill consumes the residual-risk summary, the recommended decision, and the open conditions.
