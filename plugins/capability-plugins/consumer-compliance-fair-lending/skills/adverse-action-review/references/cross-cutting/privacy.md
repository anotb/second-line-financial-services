# Privacy cross-cutting overlay for adverse-action-review

When the scope record flags `privacy` for the adverse-action review, this overlay adds privacy-regime content to the named review sections. Privacy overlap on this skill is structural rather than incidental: the review pulls applicant data, model features, BISG inputs, and per-decision feature contributions, and that data is non-public personal information (NPI) under GLBA and personal information under the state-privacy regimes.

Loaded by: `adverse-action-review/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for privacy-flagged adverse-action review

### 1. GLBA Safeguards Rule applies to the review workflow itself

The data flowing through the review (applicant identifiers, decision data, model features, score contributions, BISG inputs) is NPI under GLBA. The Safeguards Rule (16 CFR Part 314, FTC; or the parallel banking regulator program — 12 CFR Part 30 Appendix B for OCC, 12 CFR Part 364 Appendix B for FDIC, 12 CFR Part 208 Appendix D-2 for Fed) sets the data-handling expectations for the review workflow itself, not for the underlying credit decision.

Operational implications for the review:

- Sample extraction and storage follow the firm's data-classification controls; ad-hoc CSV exports to a reviewer's local environment are typically out of policy.
- BISG geocoding inputs (address, surname) are NPI; the BISG service or in-house geocoder must be inside the firm's data perimeter or under a covered service-provider agreement.
- Per-decision feature contributions (SHAP values, LIME explanations) often expose model internals that the firm classifies separately under model-IP controls; coordinate with model risk on what can leave the modeling environment.

The artifact records the source posture for the review's own data handling, not just the source posture for the underlying decision evidence.

### 2. State-privacy regimes overlap

Where the institution serves customers in CCPA / CPRA, CDPA (Virginia), CPA (Colorado), CTDPA (Connecticut), or other state-privacy regimes, the personal information used in the review may be subject to additional consumer rights (access, deletion, opt-out from automated decision-making in some states). The state-privacy posture is evolving; CPRA's automated-decision-making rules are operative, and other state regulators are moving on similar ground.

The review records the state-privacy posture for the population covered, treating cross-state variation as `[verify state-specific scope]`. The artifact does not produce a state-privacy compliance finding (that work routes to a privacy-aware skill); it flags the interaction so the privacy team is on the routing list when consumer rights requests intersect adverse-action data.

### 3. BISG and consumer-attribute data tension

The disparate-impact red-flag panel uses BISG to derive a probability distribution over race and ethnicity for applicants whose race and ethnicity are not self-reported. The derived attribute is not collected from the consumer; it is statistically inferred from public data (geography and surname). The privacy-regime treatment of inferred consumer attributes is an open area:

- Under GLBA, the inferred attribute is NPI when stored alongside applicant identifiers.
- Under CPRA, inferred attributes used to create a profile are personal information subject to consumer rights.
- The fair-lending purpose is a recognized basis for using the inferred attribute under federal law (CFPB BISG methodology paper), but the privacy-regime treatment of the storage, retention, and downstream use is a separate question.

The review treats BISG-derived attributes as signal data with the BISG caveat for fair-lending purposes; storage, retention, and downstream use (e.g., feeding the inferred attribute into customer-facing systems) is out of scope and flags for privacy review.

### 4. Customer-facing notice content and privacy disclosure interaction

The §1002.9 notice and the FCRA risk-based pricing notice both carry data-source disclosures (consumer reporting agency identity for FCRA; specific reasons for §1002.9). The privacy-regime treatment of these disclosures is established (the disclosures are required by federal law and do not trigger a separate privacy notice obligation), but the firm's privacy notice should reference the data sources used in adverse-action decisions consistent with the firm's GLBA initial-and-annual privacy notice.

Where the review surfaces a notice-content defect that involves data-source identification, the recommended remediation routes through both the consumer-compliance team (Reg B / Reg V content fix) and the privacy team (notice consistency check).

### 5. Vendor and third-party data flows

Where the underwriting decision uses third-party data (alternative-data provider, fraud / identity service, open-banking data aggregator, vendor explainability service), the data flow inherits the firm's third-party privacy and data-protection program. The review records the vendor data flows present per decision; data-subject requests against the vendor data flow may interact with the adverse-action evidence trail.

## Privacy-specific review additions

- `population.review_data_handling_posture` enum (in-perimeter / approved-service-provider / ad-hoc-export-flagged).
- `population.state_privacy_jurisdictions[]` list of state-privacy regimes covering the population, with `[verify state-specific scope]` where confidence is low.
- `decisions[].vendor_data_flows[]` list of third-party data sources contributing to the decision.
- `model_reason_generation_review.feature_contribution_data_classification` string (the firm's classification level for the per-decision feature contribution data).
- `recommended_actions[].privacy_team_routing` boolean where the recommendation involves customer notice content, vendor data flow, or BISG storage and retention.

## Common pitfalls in privacy-flagged adverse-action review

- Extracting the review sample to an unmanaged local environment because the analytics environment is slow; the data is NPI and the workflow itself is in GLBA scope.
- Treating BISG inputs as non-NPI because they are public data sources; the inferred attribute combined with applicant identifiers is NPI.
- Producing a recommendation that requires an institutional change to customer notice content without routing to the privacy team for consistency check against the firm's GLBA privacy notice.
- Treating state-privacy regimes as a one-state question (CCPA-only); the state-privacy landscape is evolving and the cross-state posture often differs.
- Using BISG-derived attributes for any purpose beyond the fair-lending finding (e.g., feeding the inferred attribute into a customer-facing system or a marketing model); the fair-lending basis does not extend to other uses.
- Treating per-decision feature contribution data as out of scope for data-classification controls because it is "just numbers"; the data exposes model internals and applicant attributes simultaneously and the firm typically classifies it tightly.
