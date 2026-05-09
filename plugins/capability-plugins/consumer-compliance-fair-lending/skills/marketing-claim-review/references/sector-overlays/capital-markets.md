# Capital markets sector overlay for marketing-claim-review

When the scope record names sector `capital-markets`, this overlay sets the scope boundary first. Most capital-markets marketing review sits in a different doctrinal lane (the SEC investment adviser Marketing Rule, Rule 206(4)-1; the FINRA communications-with-the-public framework, Rule 2210). This skill is the consumer-financial UDAAP / Reg Z lane and does not extend into those regimes. The overlay is short on purpose.

Loaded by: `marketing-claim-review/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type implicates a broker-dealer, investment adviser, private bank, or wealth-management entity that operates a retail consumer-facing credit, deposit-equivalent, or consumer-finance product surface.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## Scope boundary first

The doctrinal lanes:

- *SEC investment adviser Marketing Rule.* Rule 206(4)-1 (in force from November 4, 2022 compliance date) sets advertising and solicitation requirements for SEC-registered investment advisers under the Advisers Act antifraud framework. The lane covers general prohibitions, performance presentation, testimonials and endorsements, third-party ratings, predecessor performance, and recordkeeping. The substantive standards differ from CFPB UDAAP and Regulation Z. Reviewer: the firm's investment-adviser compliance function.
- *FINRA Rule 2210.* Communications-with-the-public requirements for FINRA-member broker-dealers (categorisation as institutional, retail, correspondence, etc.; pre-use approval and principal sign-off; recordkeeping; content standards). The substantive standards differ from CFPB UDAAP and Regulation Z. Reviewer: the firm's broker-dealer compliance function.
- *SEC Regulation Best Interest (Reg BI).* Standard of conduct for broker-dealers when making recommendations to retail customers. Reaches sales-practice fairness and disclosure mechanics. Adjacent to UDAAP framing but the legal architecture differs.

This skill does not extend into those regimes. Where the scope implicates them, route to the firm's broker-dealer compliance, investment-adviser compliance, or wealth-management compliance function.

## Where this skill does apply on the capital-markets side

Three narrow cases:

### 1. Consumer-credit marketing by a capital-markets-affiliated entity

Where a capital-markets-affiliated entity (broker-dealer; private bank; wealth-management entity; bank holding company subsidiary) markets consumer credit (margin facilities offered to retail customers; securities-based lending to retail; wealth-credit products including jumbo mortgages, lines of credit secured by assets), the consumer-credit-side asset is in scope under this skill. The asset-level review reads:

- Regulation Z advertising rules per the credit product type (open-end vs. closed-end; HELOC if a wealth-credit product is structured as a HELOC).
- TRID-adjacent reading where the marketing previews mortgage terms.
- ECOA / Reg B §1002.4(b) discouragement read on the wealth-population marketing distribution.
- FHA §3604(c) read on dwelling-related wealth-credit advertising.

The wealth-population skew (high-net-worth and ultra-high-net-worth audiences) is not itself an ECOA finding; the substantive read is whether the marketing distribution or content discourages on a prohibited basis.

### 2. Cash-management and sweep-program marketing

Brokerage cash-management features and sweep programs (automated sweeps to bank-affiliated deposit accounts; rate spreads on the sweep rate vs. the prevailing market rate) are marketed alongside the brokerage account. The asset-level review reads:

- The sweep-rate disclosure and the rate-spread mechanic.
- The FDIC insurance representation under the FDIC advertising rule (load the banking sector overlay alongside) where the sweep is into a bank-affiliated insured depository.
- The deception read on the sweep-rate framing (whether a reasonable consumer would understand the rate-spread mechanic and the alternative cash-management options).

The sweep-program marketing review can also implicate the SEC and broker-dealer disclosure framework on a parallel track; this skill carries the consumer-finance side, the broker-dealer compliance function carries the SEC side.

### 3. Bundled consumer-credit-and-investment marketing

Where the marketing surface bundles a consumer-credit product (margin; SBL; wealth-credit) with an investment-product representation (advisory recommendation; brokerage account; managed-portfolio offering), the consumer-credit-side asset is in scope and the investment-side asset routes to the firm's investment-adviser or broker-dealer compliance function. Where the bundling representation obscures the boundary, the deception analysis on the credit-side representation is in scope.

## What does not extend into this skill

- Performance advertising of investment-adviser and broker-dealer products. Routes to the SEC Marketing Rule and FINRA Rule 2210 review function.
- Testimonial and endorsement compliance under the SEC Marketing Rule. Routes to the investment-adviser compliance function.
- Third-party rating use in adviser advertising. Routes to the investment-adviser compliance function.
- FINRA Rule 2210 categorisation, approval, recordkeeping, and content-standard review. Routes to the broker-dealer compliance function.
- Reg BI disclosure-mechanic review. Routes to the broker-dealer compliance function with a consumer-protection cross-read where the underlying product is a consumer-financial-product-or-service.

The skill does not resize into an SEC Marketing Rule or FINRA Rule 2210 review. Reviewers asked to do that work should route to the relevant compliance function; the boundary skill in `capital-markets-asset-management-compliance/skills/marketing-rule-evidence` is the closer-fit surface inside this repo for the SEC Marketing Rule lane.

## Capital-markets-specific memo template additions

The fields are minimal because the overlay is mostly a scope boundary:

- `asset.product_perimeter_capital_markets[]` — enum list (`securities-based-lending`, `retail-margin`, `wealth-mortgage`, `wealth-line-of-credit`, `brokerage-cash-management-sweep`, `bundled-credit-and-investment`).
- `asset.cfpb_authority_plausible` — boolean; explicit flag to record whether the CFPB UDAAP / Reg Z perimeter reaches the in-scope asset.
- `asset.parallel_sec_or_finra_framework[]` — list of overlapping frameworks (`SEC-Marketing-Rule-206(4)-1`, `FINRA-Rule-2210`, `Reg-BI`).
- `out_of_scope_routing[]` — list of compliance functions the asset routes to where it is out of scope (investment-adviser compliance; broker-dealer compliance; wealth-management compliance).

## Common pitfalls when capital-markets is flagged

- Building a marketing-claim-review memo for an investment-adviser performance advertisement; the regime is wrong. Route to the SEC Marketing Rule review function.
- Treating wealth-credit marketing as out-of-scope because the audience is high-net-worth; the consumer-credit-side asset is in scope under Regulation Z and ECOA / Reg B regardless of audience sophistication.
- Sweep-program marketing reviewed under the SEC disclosure framework only and missing the consumer-finance-side read where the sweep is into a bank-affiliated insured depository (FDIC advertising rule applies).
- Bundled consumer-credit-and-investment marketing reviewed under one regime only; the bundling-representation analysis runs across regimes and the boundary needs to be made explicit on the asset.
- Routing margin or SBL marketing to the broker-dealer compliance function only and missing the consumer-finance read; both are in play.
- Reading the SEC Marketing Rule and Reg Z advertising rules as substitutes; they are doctrinally distinct (antifraud lane vs. consumer-protection lane) and both can apply to the same asset on different theories.
