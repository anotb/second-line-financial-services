# Banking sector overlay for adverse-action-review

When the engagement-scope record names sector `banking`, this overlay adds banking-specific scope, methodology, and review-gate detail to the adverse-action notice review. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `adverse-action-review/SKILL.md` when `engagement_scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for banking adverse-action review

Banking is the heaviest overlay on this skill. The §1002.9 machinery, the FCRA risk-score disclosure overlay, and the model-risk fabric were all built for depositories; the adverse-action review inherits that machinery directly.

### 1. Notice population scope

A banking adverse-action review typically covers a wider product set than the fintech overlay. Routine review scope includes:

- HMDA-reportable mortgage (first-lien purchase, first-lien refi, junior-lien refi, home-improvement, HELOC) — declines, withdrawals coded as denials, counteroffers not accepted.
- Indirect auto declines (where the bank is the originator-of-record on third-party-dealer-arranged loans), with attention to the dealer-markup and minimum-rate-floor mechanics that have driven prior bureau focus.
- Credit card declines, line-decrease actions on existing accounts, and account closures coded as adverse action under §1002.2(c).
- Unsecured personal loan declines and overdraft-line-of-credit declines.
- Small-business credit declines on the §1071 perimeter where the bank is in-scope under the operative tier phase-in; the small-business adverse-action review consumes §1071 demographic data once the rule is operative for the bank's tier.

The review records the §1002.2(c) action category per decision (`denial`, `counteroffer_not_accepted`, `terms_less_favorable`, `incomplete_application`, `existing_account_action`); a review covering only outright denials misses populations that are also adverse action.

### 2. FCRA / Regulation V overlay is routine

Most banking adverse-action decisions involve a consumer report and / or a credit score. The per-decision `fcra_overlay_applied` flag is true for the bulk of the population; the notice must include the FCRA disclosure content (consumer reporting agency name, address, and telephone; statement that the agency did not make and cannot explain the decision; right to a free copy and to dispute) under 15 U.S.C. §1681m, and where a credit score was used, the score, range, and key factors under §1022.74. The combined Reg B / Reg V notice is the operational artifact in most banking templates; the review tests both regimes per notice.

### 3. Model-supported reasons review and SR 11-7 fabric

Where the underwriting decision uses an internal scorecard or AI / ML model, the adverse-action review consumes model documentation produced under the bank's MRM program. The cross-references are:

- Model card (intended use, feature list, monitoring KRIs) from the MRM model-risk inventory.
- Validation-plan output (performance, stability, fairness method, limitations).
- Per-decision feature contribution evidence (SHAP, LIME, leave-one-out, monotonic constraint trace, or the bank's named explainability method).

The review tests that the notice's cited reasons are the principal feature contributions, not a closest-sample-form proxy. The CFPB Circulars 2022-03 and 2023-03 are the operative anchors; the bank's MRM machinery is the evidence pipe.

### 4. Comparative file review interaction

Banking adverse-action review interacts with comparative file review (covered in `fair-lending-test-plan`). The overlap is the matched-pair on similarly-situated approved applicants: the adverse-action sample frames the test population, and the matched-pair review surfaces disparate-treatment evidence the notice review alone cannot. The review records `cross_reference: fair-lending-test-plan` in the assumptions block where comparative file review is in flight or planned.

### 5. CRA assessment-area overlap on redlining red flags

Where the disparate-impact red-flag panel surfaces an MSA-level decline-rate disparity, the bank's CRA assessment area is a load-bearing context. A redlining red flag inside the CRA assessment area routes to the CRA officer alongside the fair-lending committee; outside the assessment area, the routing is fair-lending only. The review records the CRA assessment-area overlap per flagged geography.

### 6. Sponsor-bank arrangements

Where the bank operates a sponsor-bank arrangement (deposit, card, lending program for a fintech partner), adverse-action notice and decision-model accountability allocates per the program agreement and the bank's own fair-lending program. The interagency third-party guidance (June 2023) anchors the bank-side accountability; the bank's compliance second-line typically reviews the program-operator's adverse-action notices and decision evidence and signs off jointly with the program-operator's compliance team. See `payments-fintech.md` for the program-operator-side detail.

### 7. CFPB authority over banks

CFPB consumer-protection authority reaches large banks (over $10 billion in assets) for ECOA, RESPA, EFTA, TILA, and UDAAP purposes. Smaller banks fall under the prudential regulator for these areas, but CFPB enforcement reach is not eliminated. Reviews for large banks consume the CFPB Fair Lending Report's most recent supervisory-priority signals; reviews for smaller banks consume the prudential regulator's exam manual sections.

## Banking-specific review additions

The following additions sharpen the artifact's named sections:

- `population.product_set[]` enumerates the banking product perimeter explicitly (mortgage / HELOC / indirect-auto / card / unsecured / overdraft-line / small-business).
- `decisions[].cra_assessment_area_overlap` boolean per dwelling-secured decision.
- `decisions[].sponsor_bank_arrangement` boolean where applicable.
- `model_reason_generation_review.mrm_model_id` references the bank's MRM inventory ID.
- `recommended_actions[].cra_officer_coordination` boolean where a redlining red flag is inside the CRA assessment area.

## Common pitfalls in banking adverse-action review

- Reviewing only outright denials and missing the counteroffer-not-accepted and terms-less-favorable populations that are also adverse action under §1002.2(c).
- Treating the combined Reg B / Reg V notice as a single compliance test; the two regimes carry separate content requirements and the review tests each.
- Treating model-supported reasons as out of scope on the basis that the model is an internal scorecard rather than AI / ML; the principal-reasons specificity standard applies to all credit-scoring systems under the Staff Commentary, with the AI-specific framing layered on top by the CFPB Circulars.
- Routing a redlining red flag inside the CRA assessment area only to fair lending; the CRA officer's exam-cycle preparation work overlaps and the routing is joint.
- Treating sponsor-bank-program adverse action as the program-operator's compliance issue; the bank retains accountability under the third-party guidance and the program agreement.
- Defaulting BISG everywhere on the disparate-impact panel; HMDA self-reported demographics are stronger evidence for dwelling-secured products and should be used directly.
- Producing a finding of disparate impact on a BISG-flagged red flag; BISG is a probabilistic proxy, the red flag is a signal, and the finding follows formal fair-lending testing (route to `fair-lending-test-plan`).
