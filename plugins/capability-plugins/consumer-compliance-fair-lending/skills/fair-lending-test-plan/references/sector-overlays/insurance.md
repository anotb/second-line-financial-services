# Insurance sector overlay for fair-lending-test-plan

When the engagement-scope record names sector `insurance`, this overlay sets the scope boundary first. Insurance underwriting and pricing discrimination is regulated under state-DOI unfair-discrimination statutes, not under ECOA or the FHA. The fair-lending test-plan skill is the wrong tool for most insurance review work.

Loaded by: `fair-lending-test-plan/SKILL.md` when `engagement_scope.sector_overlay_set` includes `insurance`, or when the institution type implicates a life, health, or property-and-casualty insurer.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## Scope boundary

The vocabulary differs. Insurance regulators talk about "unfair discrimination" under the NAIC Unfair Trade Practices Act (Model #880) and state-DOI statutes implementing the model. The substantive tests differ from ECOA: the actuarial-justification framing centers on whether the rate or underwriting outcome reflects a sound actuarial basis and is not unfairly discriminatory between similarly-situated risks; the ECOA effects-test framing centers on disparate impact relative to legitimate business necessity with an LDA search.

For most insurance fair-treatment review work, route to:

- The firm's own insurance-conduct or market-conduct review program.
- The NAIC AI Model Bulletin (December 2023) where the institution uses AI/ML in underwriting, pricing, marketing, claims, or fraud detection.
- The NYDFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) for NY-licensed life insurers.
- The Colorado Division of Insurance regulation implementing SB 21-169 for CO life-insurance underwriting using ECDIS or predictive models.

Those are the operative regimes. The fair-lending test plan is built around ECOA and FHA and does not naturally extend into them.

## Where the fair-lending test plan does apply on the insurance side

Two narrow cases:

### 1. Credit-protection insurance bundled with a credit product

Where the institution sells credit-protection insurance (e.g., credit life, debt-cancellation product) bundled with an underlying credit product (mortgage, card, personal loan), the credit-side decision is in ECOA scope and the fair-lending test plan covers it normally. The insurance-side decision (eligibility, pricing) is out of fair-lending scope and routes to the insurance-conduct framework.

The bundled-product seam is a recurring complaint-theme source; coordinate with complaint-theme-analysis where complaint signals indicate cross-product issues.

### 2. Insurance products marketed alongside credit

Where the institution operates a marketing surface that distributes both credit and insurance products to overlapping customer audiences, the marketing-distribution test on the credit side is in fair-lending scope. The insurance-distribution side routes separately to the insurance-conduct framework. The plan flags the boundary so reviewers do not over-extend ECOA into insurance-marketing review.

## What does not extend into the fair-lending test plan

- Life-insurance underwriting and pricing — out of fair-lending scope. Apply the NAIC AI Model Bulletin, the NYDFS Insurance Circular Letter, the CO regulation per state footprint.
- Health-insurance underwriting and pricing — out of fair-lending scope. ACA non-discrimination provisions and HHS / state-DOI regimes apply.
- P&C insurance underwriting and pricing — out of fair-lending scope. State-DOI unfair-discrimination statutes apply; the NAIC AI Model Bulletin reaches insurer use of AI systems.
- Insurance claims handling — out of fair-lending scope. Bad-faith claims-handling and unfair-claims-settlement-practice statutes apply.

The fair-lending test plan does not resize itself into an insurance unfair-discrimination plan. Reviewers asked to do insurance unfair-discrimination work should route to the insurance-side skill set.

## Common pitfalls when insurance is flagged

- Building an ECOA test plan for an insurance underwriting model; the regime is wrong. Route to the insurance unfair-discrimination framework.
- Treating the NAIC AI Model Bulletin as an ECOA-equivalent obligation; the bulletin sets governance and AIS-program expectations, not ECOA-style effects-test expectations.
- Extending BISG-based regression methodology into insurance pricing without acknowledging that the test framing differs (actuarial-justification vs. business-necessity); the methodology is portable but the legal frame is not.
- Reading the bundled-credit-protection seam without separating the credit-side decision (in scope) from the insurance-side decision (out of scope).
