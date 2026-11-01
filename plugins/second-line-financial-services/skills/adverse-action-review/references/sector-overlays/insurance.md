# Insurance sector overlay for adverse-action-review

When the scope record names sector `insurance`, this overlay flags the scope boundary. Insurance underwriting and pricing is regulated under state-DOI unfair-discrimination statutes, not under ECOA / Regulation B; the adverse-action review does not extend to insurance underwriting decisions.

Loaded by: `adverse-action-review/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. The default behavior on this trigger is to confirm scope with the engagement lead before proceeding.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What this overlay does

Stops scope creep. The skill is built for ECOA-covered credit decisions; insurance underwriting is a different legal regime, a different vocabulary ("unfair discrimination" rather than "adverse action"), a different test framing (actuarial-justification rather than ECOA effects-test), and a different supervisor (state DOI, NAIC model laws).

### 1. Out of scope: insurance underwriting and pricing decisions

Life, health, annuity, P&C, and title insurance underwriting decisions are out of scope for this skill. The applicable regime is the state-DOI unfair-discrimination statute, with NAIC Model #880 (Unfair Trade Practices Act) as the model law and individual state implementations carrying the operational detail. Adverse decisions on insurance applications follow state-specific notice and reason-disclosure requirements, not §1002.9.

Where the engagement lead has called this skill on an insurance-underwriting question, route to a state-DOI / NAIC-aware compliance review and note the scope boundary in the artifact.

### 2. In scope: bank-affiliated credit-protection insurance bundled with credit

Where a credit-protection insurance product (credit life, credit disability, debt-cancellation product, debt-suspension product) is bundled with a credit decision and the credit decision itself is in ECOA scope, the credit-side decision is in scope. The insurance-side underwriting is out of scope; the skill reviews the credit decision and flags the bundled-insurance pattern for separate review.

The bundled-insurance pattern carries UDAAP exposure under the unfairness and abusiveness prongs (the bureau has historically focused on credit-insurance and debt-cancellation products as conduct-risk surfaces); cross-reference `udaap-risk-review` from the consumer-compliance-fair-lending plugin where the bundled product is in scope.

### 3. In scope: bank-affiliated insurance referrals where credit-style decisioning is used

Some bank-affiliated insurance affiliates use credit-style decisioning (credit-bureau pull, credit-score-driven premium banding, FICO-based underwriting tiers). Where the credit-style decisioning interacts with a credit relationship at the bank affiliate, the credit-side question is in scope; the insurance-side question is out of scope and routes to the state-DOI / NAIC overlay.

## Insurance-specific review additions

- `population.bundled_insurance_present` boolean; if true, the credit decision is reviewed here and the bundled-insurance product flags for `udaap-risk-review`.
- `recommended_actions[].naic_routing_required` boolean where an insurance-underwriting question has been incorrectly routed to this skill.

## Common pitfalls

- Treating an insurance-underwriting decline as an "adverse action" under §1002.9; it is not. The notice obligation is set by the state-DOI unfair-discrimination statute and the state-specific notice rules.
- Reviewing a bundled credit-protection insurance product under ECOA effects-test framing; the framing applies to the credit decision, not to the insurance underwriting.
- Running BISG-driven disparate-impact panels on insurance populations using the ECOA / Reg B template; the legal regime is different and the actuarial-justification framework changes the test design. Route to the state-DOI / NAIC overlay.
