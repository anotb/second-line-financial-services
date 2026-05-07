# Conduct cross-cutting overlay for marketing-claim-review

This overlay loads where the asset-level finding chains up to a product-level UDAAP read or where the marketing-asset pattern is itself a conduct-risk signal. The asset-level review surfaces the finding; the product-level UDAAP read lives in `udaap-risk-review`; the conduct-risk implications are recorded here so the marketing-compliance committee and the conduct committee both get the read they need.

Loaded by: `marketing-claim-review/SKILL.md` when `engagement_scope.cross_cutting_set` includes `conduct` or when the asset-level finding crosses UDAAP themes (deception material to a reasonable consumer; unfairness on the asset's representation of cost; abusiveness on dark-pattern asset design).

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for conduct-flagged marketing-review memos

### 1. Asset-level finding to product-level UDAAP chain

The asset-level review is scoped to the displayed asset; product-level UDAAP belongs in `udaap-risk-review`. Where the asset-level finding is one of a pattern (the same misleading representation appears across multiple assets in the campaign; the same dark pattern appears on multiple flows; the same substantiation gap recurs), the conduct overlay records:

- Whether the asset-level finding is isolated to the reviewed asset or part of a campaign or program-level pattern.
- Whether the pattern warrants chaining to `udaap-risk-review` for the product-level read.
- The cross-reference path and the named owner for the chained review.

### 2. Conduct-risk taxonomy tie-back

The memo records the conduct-risk taxonomy tie-back per the firm's framework. Common categories applicable to marketing-asset findings:

- *Communication* — marketing copy, in-product messaging, AI-generated communication, dynamic disclosure. The dominant taxonomy entry for marketing-asset findings.
- *Product design* — where the asset-level disclosure failure reflects a product-design choice (e.g., a fee mechanic that does not naturally fit the disclosure framework).
- *Sales practices* — where the asset is part of an acquisition-funnel design that channels consumers toward a particular outcome through friction asymmetry or default state.
- *Customer outcome* — outcome disparity across policy-relevant segments where the marketing distribution or AI-personalisation concentrates on or away from those segments.
- *Complaint linkage* — where the asset-level finding aligns with a complaint theme already surfaced in the firm's complaint-monitoring loop.

### 3. Named conduct-accountable manager

For UK-licensed firms in SMCR scope, the senior manager with the prescribed responsibility for marketing or for the relevant business is a named sign-off audience. For non-UK firms, the firm's conduct framework names a manager (often the head of marketing or the head of consumer / customer); the memo names the role, not the individual. The marketing-compliance committee and the conduct-accountable manager are separable items.

### 4. Conduct-event candidate

Where the firm operates a conduct-event taxonomy and the asset-level finding (or the chained product-level finding) constitutes a conduct event, the memo names the candidate classification. The classification is not the memo's job to finalise; the conduct-risk function classifies. The memo carries the recommendation.

### 5. Customer-outcome lens supplements the protected-class lens

Where the marketing-asset review intersects fair-lending themes (distribution; targeting; AI-personalisation), the customer-outcome lens extends the analysis beyond the protected-class lens. Customer-outcome disparity across policy-relevant segments (rural; low-balance; digital-only; English-as-second-language; recent-immigrant cohorts) is a conduct concern even where the protected-class disparity tests pass. The memo records:

- Whether policy-relevant segments under the conduct framework are affected by the in-scope asset's distribution or targeting.
- Whether the asset-level finding raises a parallel ECOA / FHA theory (cross-reference `fair-lending-test-plan`).
- Whether complaint-monitoring drift in the relevant complaint codes was a leading indicator (cross-reference `complaint-theme-analysis`).

### 6. Complaint-monitoring loop closure

The memo names the downstream complaint-monitoring posture: which complaint codes the firm will watch for re-emergence after the recommended edits land; the cadence; the escalation trigger if complaints persist. Marketing-edit remediation that does not close the complaint-monitoring loop is incomplete; the conduct overlay surfaces the loop as a controls-hypothesis item.

## Conduct-specific memo template additions

The following fields are added to the per-asset block where the conduct overlay loads:

- `asset.conduct_risk_taxonomy_tie_back[]` — list of conduct-risk taxonomy categories the asset-level finding touches.
- `asset.conduct_accountable_manager_role` — named role under SMCR or the firm's conduct framework, distinct from the marketing-compliance committee.
- `asset.conduct_committee_read` — boolean; if true, the conduct or customer-outcome committee gets a read alongside the marketing-compliance committee.
- `asset.conduct_event_candidate` — boolean; if true, the finding is recommended for classification by the conduct-risk function under the firm's conduct-event taxonomy.
- `asset.customer_outcome_segments_affected[]` — list of policy-relevant segments affected.
- `asset.chain_to_udaap_risk_review` — boolean; if true, the asset-level finding warrants a chained product-level UDAAP review.
- `asset.complaint_monitoring_loop_closure` — string; description of the post-edit complaint-monitoring posture.

## Common pitfalls in conduct-flagged marketing-review memos

- Treating the asset-level finding as a one-off and missing the campaign-level or program-level pattern that warrants chaining to `udaap-risk-review`.
- Conflating asset-level UDAAP findings with product-level UDAAP findings; the asset-level review handles the displayed claim, the product-level review handles the fee or flow.
- Naming the marketing-compliance committee as the only sign-off audience and missing the conduct-accountable manager role.
- Treating customer-outcome segments as the same as protected-class segments; the vocabulary and the regulatory framework differ.
- Recommending marketing edits without naming the complaint-monitoring loop-closure posture; remediation that does not close the loop is incomplete.
- Treating the asset-level finding as the conduct-event determination; the conduct-risk function classifies, not the marketing reviewer.
