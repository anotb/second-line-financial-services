# Insurance sector overlay for marketing-claim-review

When the scope record names sector `insurance`, this overlay sets the scope boundary first. Insurance advertising review sits with state insurance departments under the NAIC Unfair Trade Practices Act framework (Model #880) and the NAIC advertising-content model regulations (Model #570 for life and annuities; Model #40 for accident and sickness; comparable models for other lines). This skill is the consumer-financial UDAAP / Reg Z lane and does not extend into insurance advertising as such. The overlay is short on purpose.

Loaded by: `marketing-claim-review/SKILL.md` when `scope.sector_overlay_set` includes `insurance`, or when the institution type implicates a life, health, or property-and-casualty insurer.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## Scope boundary first

Insurance advertising vocabulary differs from CFPB UDAAP. The state-DOI framework addresses misleading advertising of insurance products under the NAIC Advertisements of Life Insurance and Annuities Model Regulation (Model #570), the NAIC Advertisements of Accident and Sickness Insurance Model Regulation (Model #40), and the broader NAIC Unfair Trade Practices Act framework (Model #880). The substantive standards differ from §1031 element tests. Reviewer: the firm's insurance-conduct or market-conduct review program; state-DOI examiners on examination.

For most insurance advertising review work, route to:

- The firm's insurance-conduct or market-conduct review program.
- State-DOI advertising-review and unfair-trade-practice statutes.
- The NAIC model regulations as the operational baseline.
- The NAIC Market Regulation Handbook for the broader market-conduct surface.
- Where AI / ML is used in advertising or audience targeting, the NAIC AI Model Bulletin (December 2023) and any state-specific AI / advertising guidance.

This skill does not extend into those regimes.

## Where this skill does apply on the insurance side

Two narrow cases:

### 1. Bank-affiliated credit-protection insurance bundled with credit

Where the bank or non-bank credit provider markets credit-protection insurance (credit life; debt-cancellation; GAP; VSC bundled with auto-loan) bundled with the underlying credit product (mortgage, card, personal loan, auto loan), the credit-side marketing representation is in scope under this skill. The asset-level review reads:

- The bundling representation against the cost-of-credit framing (whether the consumer can read the asset and understand that the insurance fee is a separate cost).
- The Regulation Z disclosure mechanics on the credit-side (open-end vs. closed-end advertising rules per the underlying credit product).
- The deception read on the bundled-product representation.

The insurance-side advertising (eligibility, pricing of the insurance product itself, claims handling representations) routes to the insurance-conduct framework and is out of scope here.

### 2. Marketing surface that distributes both credit and insurance products

Where the firm operates a marketing surface that distributes both credit and insurance products to overlapping audiences, the marketing of the credit product is in scope. The marketing of the insurance product routes to the insurance-conduct framework. Where the marketing copy obscures the boundary (bundles credit and insurance in a single representation; suggests an insurance product is part of the credit offering when it is separate), the deception analysis on the credit-side representation is in scope.

## What does not extend into this skill

- Life-insurance and annuity advertising as such. NAIC Model #570 and state-DOI implementing regulations apply.
- Accident-and-health insurance advertising. NAIC Model #40 and state-DOI implementing regulations apply.
- P&C insurance advertising. State-DOI advertising-review statutes apply; NAIC has additional model regulations for specific lines.
- Insurance underwriting and pricing representations in advertising. State-DOI unfair-discrimination statutes apply.
- Insurance claims-handling representations in advertising. NAIC Unfair Trade Practices Act framework and state-DOI bad-faith-claims-handling framework apply.
- AI use in insurance advertising and audience targeting. NAIC AI Model Bulletin and state-specific guidance (NYDFS Insurance Circular Letter on AI; CO regulation under SB 21-169 for life insurance) apply.

The skill does not resize into an insurance advertising review. Reviewers asked to do insurance advertising work should route to the firm's insurance-conduct function and the state-DOI framework; this plugin's six skills do not currently cover insurance advertising as a primary surface.

## Insurance-specific memo template additions

The fields are minimal because the overlay is mostly a scope boundary:

- `asset.bundled_credit_protection_insurance` — boolean; if true, the credit-side bundling-representation review is the in-scope asset; insurance-side advertising is explicitly out of scope.
- `asset.credit_and_insurance_marketing_surface` — boolean; if true, the marketing-side review on the credit product is in scope; insurance-product marketing routes separately.
- `out_of_scope_routing[]` — list of insurance-conduct frameworks the asset routes to (NAIC Model #570 for life and annuity advertising; NAIC Model #40 for accident-and-sickness advertising; NAIC Model #880 for unfair trade practices; state-DOI advertising-review statutes; NAIC Market Regulation Handbook; NAIC AI Model Bulletin where AI is in path).

## Common pitfalls when insurance is flagged

- Building a marketing-claim-review memo for a life-insurance advertising asset; the regime is wrong. Route to the insurance-conduct framework.
- Treating the bundling representation as an insurance-side issue; the credit-side representation on the bundled-product framing is in scope under UDAAP and Regulation Z.
- Reading the NAIC AI Model Bulletin as a UDAAP-equivalent obligation; the bulletin sets governance and AIS-program expectations, not Dodd-Frank §1031 element-test expectations.
- Reading bundled-credit-protection-insurance marketing without separating the credit-side review (in scope here) from the insurance-side review (out of scope, route separately).
- Extending the §1031 element analysis into life-or-health-insurance underwriting representations in advertising; the substantive standards differ.
- Treating bad-faith-claims-handling representations as UDAAP marketing findings; the regime is state common-law and statutory, not CFPB UDAAP.
