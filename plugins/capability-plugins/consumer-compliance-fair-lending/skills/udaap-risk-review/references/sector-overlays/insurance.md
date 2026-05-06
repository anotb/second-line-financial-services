# Insurance sector overlay for udaap-risk-review

When the engagement-scope record names sector `insurance`, this overlay sets the scope boundary first. Insurance unfair-trade-practice review sits with state insurance departments under the NAIC Unfair Trade Practices Act framework and state-DOI statutes, not under Dodd-Frank UDAAP. The UDAAP review skill is the wrong tool for most insurance review work.

Loaded by: `udaap-risk-review/SKILL.md` when `engagement_scope.sector_overlay_set` includes `insurance`, or when the institution type implicates a life, health, or property-and-casualty insurer.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## Scope boundary

The vocabulary differs. Insurance regulators talk about "unfair trade practices" and "unfair claims settlement practices" under the NAIC Unfair Trade Practices Act (Model #880) and state-DOI statutes implementing the model. The substantive tests differ from UDAAP: the unfair-discrimination framing centers on whether underwriting and pricing reflect a sound actuarial basis and are not unfairly discriminatory between similarly-situated risks; the unfair-claims-settlement framing centers on bad-faith claims handling under state statutes and common-law doctrine. Dodd-Frank §1031 element tests do not naturally apply to most insurance fact patterns because insurance is not a consumer-financial-product-or-service under Dodd-Frank Title X (with the narrow exceptions noted below).

For most insurance fair-treatment review work, route to:

- The firm's own insurance-conduct or market-conduct review program.
- State-DOI market-conduct examination procedures.
- The NAIC Market Regulation Handbook for the operational baseline on market-conduct review.
- The NAIC AI Model Bulletin (December 2023) where the institution uses AI / ML in underwriting, pricing, marketing, claims, or fraud detection.
- The NYDFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) for NY-licensed life insurers.
- The Colorado Division of Insurance regulation implementing SB 21-169 for CO life-insurance underwriting using ECDIS or predictive models.

Those are the operative regimes. The UDAAP review skill is built around Dodd-Frank §1031 / §1036 and does not naturally extend into them.

## Where the UDAAP review skill does apply on the insurance side

Three narrow cases:

### 1. Credit-protection insurance bundled with a credit product

Where the institution sells credit-protection insurance (credit life, debt-cancellation, GAP, VSC bundled with auto-loan) packaged with an underlying credit product (mortgage, card, personal loan, auto loan), the credit-side decision (the bundling mechanic, the disclosure of the insurance fee in the cost-of-credit framing, the cancellation flow, the relationship between the insurance product and the credit product) is in CFPB UDAAP scope. The insurance-side decision (eligibility, pricing of the insurance product itself) is out of UDAAP scope and routes to the insurance-conduct framework.

The bundled-product seam is a recurring CFPB enforcement and supervisory focal area; the bureau has pursued fact patterns on auto add-on bundling, deferred-amortisation mechanics on credit-life, and disclosure-of-cost mechanics across multiple consent orders.

### 2. Marketing surface that distributes both credit and insurance

Where the institution operates a marketing surface that distributes both credit and insurance products to overlapping customer audiences, the marketing of the credit product is in UDAAP scope. The marketing of the insurance product is in the insurance-conduct framework. Where the marketing copy obscures the boundary (bundles credit and insurance in a single representation), the deception analysis on the credit-side representation is in scope.

### 3. CFPB-jurisdictional consumer-finance products that have an insurance component

Edge cases where the consumer-finance product has an embedded insurance feature (e.g., a deposit account with embedded insurance benefits) require careful boundary work. The consumer-finance side is in CFPB UDAAP scope; the insurance side routes to the insurance-conduct framework. The memo records the boundary explicitly.

## What does not extend into the UDAAP review skill

- Life-insurance underwriting and pricing, including ECDIS / AI / predictive-model use in underwriting. Apply the NAIC AI Model Bulletin, the NYDFS Insurance Circular Letter, the CO regulation per state footprint.
- Health-insurance underwriting and pricing. ACA non-discrimination provisions and HHS / state-DOI regimes apply.
- P&C insurance underwriting and pricing. State-DOI unfair-discrimination statutes apply; the NAIC AI Model Bulletin reaches insurer use of AI systems.
- Insurance claims handling. Bad-faith claims-handling and unfair-claims-settlement-practice statutes apply; the NAIC Unfair Trade Practices Act and state-DOI frameworks govern.
- Insurance marketing as such (apart from the bundled-marketing edge case in #2 above). State-DOI advertising review and the NAIC Advertisements of Life Insurance and Annuities Model Regulation (Model #570) and similar A&H model regulations apply.

The UDAAP review skill does not resize itself into an insurance unfair-trade-practice review. Reviewers asked to do insurance unfair-trade-practice work should route to the insurance-side skill set; this plugin's six skills do not currently cover the insurance-conduct frame as a primary surface.

## Insurance-specific memo template additions

The fields are minimal because the overlay is mostly a scope boundary. Where the narrow in-scope cases apply:

- `scope.bundled_credit_protection_insurance` — boolean; if true, the credit-side bundling mechanic is the in-scope UDAAP fact pattern; insurance-side eligibility and pricing are explicitly out of scope.
- `scope.credit_and_insurance_marketing_surface` — boolean; if true, the marketing-side review on the credit product is in scope; insurance-product marketing routes separately.
- `out_of_scope_routing[]` — list of insurance-conduct frameworks the memo routes to (NAIC AI Model Bulletin, NYDFS Circular Letter, CO regulation, state-DOI market-conduct procedures, NAIC Market Regulation Handbook, NAIC Model #880 unfair trade practices, state-DOI claims-settlement statutes).

## Common pitfalls when insurance is flagged

- Building a UDAAP memo for an insurance underwriting model; the regime is wrong. Route to the insurance unfair-trade-practice framework.
- Treating the NAIC AI Model Bulletin as a UDAAP-equivalent obligation; the bulletin sets governance and AIS-program expectations, not Dodd-Frank §1031 element-test expectations.
- Reading the bundled-credit-protection seam without separating the credit-side decision (in UDAAP scope) from the insurance-side decision (out of UDAAP scope); the consumer-experience flow seam runs through both regimes.
- Extending the §1031 element analysis into life or health-insurance underwriting; the substantive standards differ and the analytical conclusions do not port cleanly.
- Treating bad-faith-claims-handling fact patterns as UDAAP; bad faith is a state common-law and statutory regime, not a CFPB UDAAP frame.
