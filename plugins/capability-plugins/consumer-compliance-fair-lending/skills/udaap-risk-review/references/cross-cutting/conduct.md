# Conduct cross-cutting overlay for udaap-risk-review

This overlay is mandatory on this skill. UDAAP findings are the dominant conduct-risk signal in US consumer financial services; every UDAAP review memo carries a conduct-risk implications block. The overlay names what changes when the engagement-scope record flags `conduct` (which it does by default for this skill).

Loaded by: `udaap-risk-review/SKILL.md` whenever invoked. Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for conduct-flagged UDAAP review memos

### 1. UDAAP-conduct vocabulary clarified

Conduct in second-line vocabulary names a customer-outcome lens, a named-manager accountability lens, and a regulatory-engagement lens. UDAAP is one specific legal regime under that umbrella. The overlap is not total: every UDAAP defect is potentially a conduct defect, but not every conduct defect rises to UDAAP. The memo is explicit about which lens is doing the analytical work; the seam between "this is a UDAAP §1031 element finding" and "this is a conduct-framework finding that does not yet rise to UDAAP" matters because the regulatory consequences differ.

### 2. Conduct-risk taxonomy tie-back

The memo records the conduct-risk taxonomy tie-back per the firm's framework. Common categories include:

- *Incentives* — sales or LO compensation design that encourages the conduct under review.
- *Product design* — fee architecture, disclosure design, default-state design, choice-architecture design.
- *Communication* — marketing copy, in-product messaging, AI-generated communication, dynamic disclosure.
- *Sales practices* — branch and digital sales conduct, retention-offer conduct, friction-design.
- *Customer outcome* — outcome disparity across policy-relevant segments (rural, low-balance, digital-only, English-as-second-language, recent-immigrant cohorts).
- *Complaint linkage* — whether the underlying complaint signal already surfaced in the firm's complaint-monitoring loop and what was done with it.

The memo lists each category that the in-scope fact pattern touches; the conduct committee reads against the taxonomy.

### 3. Named conduct-accountable manager

For UK-licensed firms in SMCR scope, the senior manager with the prescribed responsibility for the relevant business is a named sign-off audience. For non-UK firms, the firm's conduct framework names a manager (often the head of the relevant business or the head of consumer / customer); the memo names the role, not the individual. The UDAAP-decision forum (product committee, CCO, conduct committee, fair-lending committee, counsel) and the conduct-accountable manager are separable items; the memo is explicit about which is which and which forum decides what.

### 4. Customer-outcome lens supplements the protected-class lens

Where the UDAAP review intersects fair-lending themes (steering, marketing distribution, servicing, loss-mitigation), the customer-outcome lens extends the analysis beyond the protected-class lens. Customer-outcome disparity across policy-relevant segments is a conduct concern even where the protected-class disparity tests pass. The memo records:

- Whether policy-relevant segments under the conduct framework are affected by the fact pattern, in addition to or instead of protected-class segments.
- Whether the fact pattern raises a parallel ECOA / FHA theory (cross-reference `fair-lending-test-plan`).
- Whether complaint-monitoring drift in the relevant complaint codes was a leading indicator (cross-reference `complaint-theme-analysis`).

### 5. Conduct-event taxonomy classification

Where the firm operates a conduct-event taxonomy (a register of conduct-risk events with severity, root cause, and customer-impact classification), the memo names whether the in-scope finding is a conduct-event candidate. The classification is not the memo's job to finalise; the conduct-risk function classifies. The memo carries the recommendation.

### 6. Regulatory-engagement intersection

Where the UDAAP memo is responding to a regulatory-engagement event (CFPB inquiry, OCC Matter Requiring Attention, FDIC corrective action, state AG inquiry, FCA Section 166 review for UK-licensed entities), the conduct overlay records:

- The event that triggered the memo.
- The regulator-engagement counsel posture (privilege, work-product, response-file management).
- Whether the conduct committee gets a read alongside the UDAAP-decision forum.
- Whether the firm's conduct-event reporting to the regulator is implicated (e.g., FCA reportable concern under Principle 11 for UK-licensed entities; or a CFPB self-reporting consideration for US entities).

### 7. Complaint-monitoring loop closure

The memo names the downstream complaint-monitoring posture: which complaint codes the firm will watch for re-emergence after remediation; the cadence; the escalation trigger if complaints persist. UDAAP remediation that does not close the complaint-monitoring loop is incomplete; the conduct overlay surfaces the loop as a controls-hypothesis item.

## Conduct-specific memo template additions

The following fields and sections are added to the memo (mapped to schema where present):

- `conduct_risk_taxonomy_tie_back[]` — list of conduct-risk taxonomy categories the fact pattern touches.
- `conduct_accountable_manager_role` — named role under SMCR or the firm's conduct framework, distinct from the UDAAP-decision forum.
- `conduct_committee_read` — boolean; if true, the conduct or customer-outcome committee gets a read alongside the UDAAP-decision forum.
- `conduct_event_candidate` — boolean; if true, the finding is recommended for classification by the conduct-risk function under the firm's conduct-event taxonomy.
- `customer_outcome_segments_affected[]` — list of policy-relevant segments affected (in addition to or instead of protected-class segments).
- `regulator_engagement_trigger` — string; named regulator-engagement event that triggered the memo, if any.
- `complaint_monitoring_loop_closure` — string; description of the post-remediation complaint-monitoring posture.

## Common pitfalls in conduct-flagged UDAAP review memos

- Conflating UDAAP review with conduct review and producing a memo that does not separate the findings cleanly; counsel and the regulator both need the seams visible.
- Extending the protected-class lens into customer-outcome segments without recording the test-framing change; the vocabulary matters because the legal regime differs.
- Treating complaint themes as a noisy input rather than as a leading indicator; complaint-rate and complaint-code drift are signal, not noise.
- Missing the named conduct-accountable manager on the sign-off audience list; the conduct framework names a role separate from the product owner and separate from the CCO.
- Writing the memo without recording the regulator-engagement trigger where one exists; the response-file posture and the privilege posture both turn on whether the memo is responding to engagement or running on the routine cycle.
- Recommending remediation without naming the complaint-monitoring loop-closure posture; remediation that does not close the loop is incomplete and the conduct committee will catch the gap.
- Treating UDAAP and the conduct framework as the same regime for global firms; they are aligned in spirit but the legal architecture differs and the memo should not pretend otherwise.
