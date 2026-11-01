# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay — adverse-action-review

Loads when the scope `cross_cutting_overlay_set` includes `conduct`, or when the adverse-action-review population intersects with material complaint signal, AI / complex-model communication surfaces, or product-distribution arrangements where the firm's conduct framework names the use case under its scope. The Reg B and FCRA frame on this skill is the regulatory minimum; the conduct overlay reads what the population says about how the firm is treating the consumer beyond the rule's text.

#### Why conduct belongs in the adverse-action review

Adverse-action notices are the firm's most direct communication on a refused, modified, or limited consumer-credit transaction. They are read by regulators as a window into how the firm communicates outcome decisions: are the cited reasons specific enough to let the consumer act on them, are they accurate against what the model actually relied on, are they consistent with the marketing the consumer saw, are they consistent with the way the front-line described the product. A population of notices that passes the §1002.9 timing-and-content test on the surface but reads as a generic "did not meet our credit standards" line across the sample carries a UDAAP exposure that the field-by-field review does not surface on its own. The conduct overlay reads the population for that signal.

The overlay also reads the AAN-population alongside the firm's complaint surveillance and against any open consent-order remediation. A theme in `complaint-theme-analysis` tagged to AAN content or to reason-coding is the same population this skill works on, read from a different angle; the conduct overlay names the seam.

#### Operative anchors

- **CFPB UDAAP authority** — 12 USC §5531 and §5536 (unfair, deceptive, or abusive acts or practices). The bureau's authority on AAN content reaches deceptive cited-reason content, abusive reason-suppression patterns, and unfair denial communications that obscure the basis for the decision.
- **FTC Section 5** — 15 USC §45 — for non-bank entities outside CFPB scope on the AAN-content population.
- **April 2023 Joint Statement** — CFPB, EEOC, DOJ Civil Rights Division, FTC — on enforcement of civil rights, fair competition, consumer protection, and equal opportunity laws against algorithmic discrimination and automated systems. Algorithmic AAN reason generation is reachable under existing UDAAP, ECOA, and FCRA authorities.
- **CFPB Circulars 2022-03 and 2023-03** — withdrawn May 12, 2025; preserved in `references/source-anchors.md` as historical context. The withdrawal does not affect the underlying §1002.9(a)(2) and Staff Commentary 9(b)(2)-3 specificity standard, which remains the binding regulation. The conduct frame on AI / complex-model AANs survives the withdrawal because the regulation does.
- **CFPB Supervisory Highlights** — recurring focal items on AAN content, reason-coding accuracy, and complex-model AAN-generation deficiencies. Cited at memo date with the specific issue and date.
- **FCA SMCR and Consumer Duty** — for UK-licensed firms operating into the US or with US customer overlap, the conduct-accountable manager frame and the Consumer Duty cross-border perimeter trigger.
- **NAIC Market Conduct Examiners Handbook and NAIC Models #880 (Unfair Trade Practices) and #900 (Unfair Claims Settlement Practices)** — for the narrow insurance touch-point where the AAN-equivalent obligation under FCRA applies (for insurance underwriting decisions affected by consumer-report data).
- **Firm-specific conduct framework** — lives in `references/firm-overlay.md` when present (named conduct-accountable manager role, conduct-event taxonomy, customer-outcome-segments definition, complaint-monitoring loop closure path).

#### What changes when conduct is flagged

##### 1. Specific reasons cited section gains a comprehensibility read

The §1002.9 specificity standard is the regulatory floor. The conduct overlay layers a comprehensibility read on top: per cited reason, can the consumer act on this. A reason that is technically specific (cites a feature, a threshold, a derogatory item) but is incomprehensible to a consumer (jargon-heavy, model-mathematics-leaking, cross-referenced to a code the consumer does not have) is conduct-flagged even if it passes specificity. The memo records:

- The cited reason text as it appears.
- A comprehensibility verdict (clear, requires-explanation, incomprehensible).
- Where requires-explanation or incomprehensible, the conduct-tagged finding routes to recommended action.

The discipline is not "rewrite for marketing"; it is "consumer can act on the reason or cannot". A consumer told the rejection was driven by "trended balance velocity exceeding cohort norm" cannot act on the reason in any meaningful way and the AAN does not satisfy the underlying purpose of the regulation even where it satisfies the text.

##### 2. Reasons supported by underlying model and data section flags conduct-relevant defects

The section tests whether the cited reasons are the principal reasons relied on (Staff Commentary 9(b)(2)-3). The conduct overlay names two specific defect classes that recur on AI / complex-model AANs and that read as conduct exposure independent of the regulatory text:

- **Sample-form-substitution at population scale.** Where the firm's reason-coding maps every model output to one of N sample-form reasons regardless of feature contributions, the population reads as deceptive even where individual notices may be defensible. The memo cites the population pattern, not just per-notice findings.
- **Reason-suppression for unfavourable patterns.** Where the firm's reason-coding rules systematically suppress reasons that would surface a recurring pattern (e.g., reasons that would map to a marketing claim, a fee architecture, or a product-design feature), the suppression reads as an abusive pattern. The memo cites the suppression rule and the affected population.

Each conduct-flagged defect carries an evidence pointer (the reason-coding rule reference, the population pattern statistics) and routes to recommended action with a named conduct-function owner.

##### 3. Reg B §1002.9 content compliance section gains the disclosure-consistency read

The section tests notice content against the regulation. The conduct overlay layers the disclosure-consistency read: do the cited reasons reconcile with the marketing the consumer saw, the front-line representation, and the firm's product-fact library. Where the AAN cites a reason the consumer was not told to expect (a feature the marketing did not surface as a decision input, a documentation requirement the application path did not flag), the inconsistency is conduct-flagged. The recommended action routes to marketing-claim-review (where the marketing is at issue), to the front-line-script owner (where the representation is at issue), or to product-governance (where the product-fact library is at issue).

##### 4. AI / complex-model specific findings section names the conduct dimension

The section already names the AI / complex-model defect taxonomy (`no-explainability`, `impossible-mapping`, `sample-form-substitution`, `generic-reason-only`, `model-reason-mismatch`). The conduct overlay extends each defect with a conduct-event candidate read:

- **`no-explainability`** — conduct-event candidate where the population is material and the firm's commitment to consumers (in marketing or in the application path) was that decisions are explainable.
- **`impossible-mapping`** — conduct-event candidate by default. A consumer told a reason that cannot be true for the product is being misled.
- **`sample-form-substitution`** — conduct-event candidate where the substitution rule operates at population scale (rather than per-notice).
- **`generic-reason-only`** — conduct-event candidate where the population is material and the underlying model is complex enough that specificity is achievable.
- **`model-reason-mismatch`** — conduct-event candidate where the affected population is material.

The conduct-event-candidate flag does not classify the event; the conduct-risk function classifies. The flag routes the finding into the conduct-event evaluation chain alongside the regulatory-content finding.

##### 5. Disparate-impact red flags section reads alongside the conduct framework

The disparate-impact section produces signals (BISG-derived, geography-derived, HMDA-derived where applicable). The conduct overlay reads each signal against the firm's customer-outcome-segments definition under the conduct framework: is the affected segment a policy-relevant cohort under the conduct framework, beyond the protected-class lens. Where the firm's conduct framework names additional cohorts (vulnerable customers, recently-onboarded customers, customers in a specific channel or product), the signal is read against those cohorts as well. The output is signal, not a finding; the cross-skill chain into `fair-lending-test-plan` and into the conduct-risk function is named.

##### 6. Recommended action section adds conduct-specific routing and a conduct-accountable manager

Each recommended action that carries a conduct dimension (comprehensibility-flagged reasons, disclosure-inconsistency findings, conduct-event-candidate AI / complex-model findings, conduct-framework-cohort signals) carries:

- A conduct-function cross-routing (Head of Conduct Risk, consumer compliance committee, conduct committee) in addition to the operational owner.
- The named conduct-accountable manager role under the firm's conduct framework (or under SMCR for UK-licensed firms operating into the US). The conduct-accountable manager is named distinct from the model owner and distinct from the consumer compliance lead, even where the firm's structure assigns the role to a person who also holds one of those titles.
- A complaint-monitoring loop closure: which complaint codes the firm watches post-action, the cadence, the escalation trigger if the theme persists.
- Where the recommended action is a notice-template change, a marketing-claim refresh, a front-line-script change, or a product-fact-library update, the customer-comprehension assessment is named as the verifier; legal review is necessary but not sufficient.

##### 7. Open legal / compliance questions section adds the conduct-event-classification question

Where the population carries material conduct-event-candidate findings, the open-questions section names the conduct-event-classification question for the conduct-risk function: is this a conduct event under the firm's taxonomy, what is the redress posture, what is the regulator-engagement posture, what is the privilege posture on the artifact itself. Counsel and the Head of Conduct Risk co-own the question.

#### Conduct-specific output additions

In the structured record the skill produces:

- A comprehensibility verdict on each cited reason (clear, requires-explanation, incomprehensible) alongside the specificity verdict.
- Population-pattern findings for sample-form-substitution and reason-suppression where present.
- Disclosure-consistency findings cross-referencing the marketing or front-line evidence.
- A conduct-event-candidate flag per AI / complex-model defect class where the criteria are met.
- A conduct-framework-cohort signal alongside the protected-class disparate-impact signal.
- A conduct-function cross-routing on conduct-flagged recommended actions.
- A named conduct-accountable manager role on the recommended-action block.
- A complaint-monitoring loop closure block on conduct-flagged recommended actions.

#### Common pitfalls when conduct applies

- Reading the §1002.9 specificity test as the conduct test. The regulation is the floor; the conduct frame asks whether the consumer can act on the reason.
- Treating per-notice defect findings as the conduct read. Population-pattern findings (sample-form-substitution at scale, reason-suppression rules, generic-reason-only as the firm's default) read as conduct exposure independent of the per-notice defect rate.
- Skipping the disclosure-consistency read. A notice that is internally consistent with the model but inconsistent with the marketing the consumer saw is conduct-flagged.
- Naming the model owner as the conduct-accountable manager. Under most firm conduct frameworks (and under SMCR), the conduct-accountable manager is a different role.
- Treating the conduct-event-candidate flag as a finding. The flag routes the finding to conduct-risk classification; the function classifies, not the review.
- Reading disparate-impact signals only against the protected-class lens. The firm's conduct framework typically names additional cohorts; the read is wider.
- Skipping the complaint-monitoring loop closure on recommended actions. A notice-template change without a complaint-code watch and a cadence is shipping without a feedback mechanism.
- Treating recommended notice changes as a legal-review-only item. Customer-comprehension is a conduct artifact; legal review is necessary, conduct review is not optional.

## privacy

### Privacy cross-cutting overlay for adverse-action-review

When the scope record flags `privacy` for the adverse-action review, this overlay adds privacy-regime content to the named review sections. Privacy overlap on this skill is structural rather than incidental: the review pulls applicant data, model features, BISG inputs, and per-decision feature contributions, and that data is non-public personal information (NPI) under GLBA and personal information under the state-privacy regimes.

Loaded by: `adverse-action-review/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for privacy-flagged adverse-action review

##### 1. GLBA Safeguards Rule applies to the review workflow itself

The data flowing through the review (applicant identifiers, decision data, model features, score contributions, BISG inputs) is NPI under GLBA. The Safeguards Rule (16 CFR Part 314, FTC; or the parallel banking regulator program — 12 CFR Part 30 Appendix B for OCC, 12 CFR Part 364 Appendix B for FDIC, 12 CFR Part 208 Appendix D-2 for Fed) sets the data-handling expectations for the review workflow itself, not for the underlying credit decision.

Operational implications for the review:

- Sample extraction and storage follow the firm's data-classification controls; ad-hoc CSV exports to a reviewer's local environment are typically out of policy.
- BISG geocoding inputs (address, surname) are NPI; the BISG service or in-house geocoder must be inside the firm's data perimeter or under a covered service-provider agreement.
- Per-decision feature contributions (SHAP values, LIME explanations) often expose model internals that the firm classifies separately under model-IP controls; coordinate with model risk on what can leave the modeling environment.

The artifact records the source posture for the review's own data handling, not just the source posture for the underlying decision evidence.

##### 2. State-privacy regimes overlap

Where the institution serves customers in CCPA / CPRA, CDPA (Virginia), CPA (Colorado), CTDPA (Connecticut), or other state-privacy regimes, the personal information used in the review may be subject to additional consumer rights (access, deletion, opt-out from automated decision-making in some states). The state-privacy posture is evolving; CPRA's automated-decision-making rules are operative, and other state regulators are moving on similar ground.

The review records the state-privacy posture for the population covered, treating cross-state variation as `[verify state-specific scope]`. The artifact does not produce a state-privacy compliance finding (that work routes to a privacy-aware skill); it flags the interaction so the privacy team is on the routing list when consumer rights requests intersect adverse-action data.

##### 3. BISG and consumer-attribute data tension

The disparate-impact red-flag panel uses BISG to derive a probability distribution over race and ethnicity for applicants whose race and ethnicity are not self-reported. The derived attribute is not collected from the consumer; it is statistically inferred from public data (geography and surname). The privacy-regime treatment of inferred consumer attributes is an open area:

- Under GLBA, the inferred attribute is NPI when stored alongside applicant identifiers.
- Under CPRA, inferred attributes used to create a profile are personal information subject to consumer rights.
- The fair-lending purpose is a recognized basis for using the inferred attribute under federal law (CFPB BISG methodology paper), but the privacy-regime treatment of the storage, retention, and downstream use is a separate question.

The review treats BISG-derived attributes as signal data with the BISG caveat for fair-lending purposes; storage, retention, and downstream use (e.g., feeding the inferred attribute into customer-facing systems) is out of scope and flags for privacy review.

##### 4. Customer-facing notice content and privacy disclosure interaction

The §1002.9 notice and the FCRA risk-based pricing notice both carry data-source disclosures (consumer reporting agency identity for FCRA; specific reasons for §1002.9). The privacy-regime treatment of these disclosures is established (the disclosures are required by federal law and do not trigger a separate privacy notice obligation), but the firm's privacy notice should reference the data sources used in adverse-action decisions consistent with the firm's GLBA initial-and-annual privacy notice.

Where the review surfaces a notice-content defect that involves data-source identification, the recommended remediation routes through both the consumer-compliance team (Reg B / Reg V content fix) and the privacy team (notice consistency check).

##### 5. Vendor and third-party data flows

Where the underwriting decision uses third-party data (alternative-data provider, fraud / identity service, open-banking data aggregator, vendor explainability service), the data flow inherits the firm's third-party privacy and data-protection program. The review records the vendor data flows present per decision; data-subject requests against the vendor data flow may interact with the adverse-action evidence trail.

#### Privacy-specific review additions

- `population.review_data_handling_posture` enum (in-perimeter / approved-service-provider / ad-hoc-export-flagged).
- `population.state_privacy_jurisdictions[]` list of state-privacy regimes covering the population, with `[verify state-specific scope]` where confidence is low.
- `decisions[].vendor_data_flows[]` list of third-party data sources contributing to the decision.
- `model_reason_generation_review.feature_contribution_data_classification` string (the firm's classification level for the per-decision feature contribution data).
- `recommended_actions[].privacy_team_routing` boolean where the recommendation involves customer notice content, vendor data flow, or BISG storage and retention.

#### Common pitfalls in privacy-flagged adverse-action review

- Extracting the review sample to an unmanaged local environment because the analytics environment is slow; the data is NPI and the workflow itself is in GLBA scope.
- Treating BISG inputs as non-NPI because they are public data sources; the inferred attribute combined with applicant identifiers is NPI.
- Producing a recommendation that requires an institutional change to customer notice content without routing to the privacy team for consistency check against the firm's GLBA privacy notice.
- Treating state-privacy regimes as a one-state question (CCPA-only); the state-privacy landscape is evolving and the cross-state posture often differs.
- Using BISG-derived attributes for any purpose beyond the fair-lending finding (e.g., feeding the inferred attribute into a customer-facing system or a marketing model); the fair-lending basis does not extend to other uses.
- Treating per-decision feature contribution data as out of scope for data-classification controls because it is "just numbers"; the data exposes model internals and applicant attributes simultaneously and the firm typically classifies it tightly.
