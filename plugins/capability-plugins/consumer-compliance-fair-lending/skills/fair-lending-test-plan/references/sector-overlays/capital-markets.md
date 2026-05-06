# Capital markets sector overlay for fair-lending-test-plan

When the engagement-scope record names sector `capital-markets`, this overlay adds the narrow set of capital-markets fair-lending considerations to the test plan. The overlay is short on purpose: most capital-markets activity sits outside the ECOA and FHA perimeter. Where it does touch, the touch points are predictable.

Loaded by: `fair-lending-test-plan/SKILL.md` when `engagement_scope.sector_overlay_set` includes `capital-markets`, or when the institution type implicates a broker-dealer, investment adviser, private bank, or wealth-management entity that extends credit to retail clients.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for capital-markets fair-lending test plans

### 1. Scope boundary first

Most capital-markets activity is not in fair-lending scope. Securities trading, asset management, institutional brokerage, and investment-adviser portfolio management do not extend credit; ECOA does not reach them. The capital-markets fair-lending perimeter is narrow:

- Securities-based lending (SBL) to retail clients (including individual customers of private-bank and wealth-management businesses).
- Margin lending to retail customers (subject to FINRA Rule 4210 and Reg T; the credit-decision component is in ECOA scope).
- Mortgage origination by capital-markets-affiliated entities (where the bank holding company operates a mortgage subsidiary; the mortgage entity carries the banking-overlay machinery).
- Wealth-credit products (jumbo mortgages, lines of credit secured by assets) where the bank or broker-dealer is the creditor.

Activity that is not credit (advisory recommendations, trade execution, custody) is outside fair-lending scope. Sales-practice fairness and best-interest framing apply (Reg BI for broker-dealers, fiduciary duty for advisers) but those are not ECOA tests.

### 2. SBL and margin-lending test plan content

Where SBL or retail margin lending is in scope, the test plan applies the regular ECOA machinery:

- Underwriting decision review (eligibility, line-size determination).
- Pricing review (rate spread, fee determination).
- Marketing distribution review (where SBL or margin is marketed to a defined retail audience).
- Demographic proxy method: BISG; record proxy-uncertainty handling. The wealth-customer demographic distribution may be skewed in ways that affect proxy accuracy.

LDA search applies where any AI/ML model drives the decision. Most retail SBL and margin-eligibility decisions are model-light or judgmental; record the model inventory honestly and scope LDA where it actually applies.

### 3. Wealth-credit boundary

Wealth-credit products to high-net-worth and ultra-high-net-worth clients raise an under-discussed fair-lending question: the addressable population for these products is itself skewed by wealth concentration, which correlates with race and ethnicity. The test plan should record this as an open question for the fair-lending committee where the institution is sizing a wealth-credit fair-lending review for the first time. The plan does not resolve the question; it surfaces it.

### 4. Non-applicability for trading-and-execution activity

Trading desks, execution algorithms, market-making, and surveillance models are out of fair-lending scope. They sit under Rule 15c3-5 (broker-dealer market-access controls), FINRA supervision rules, SEC market-integrity rules, and the firm's market-conduct framework. Do not extend the fair-lending test plan into trading activity; flag the scope boundary and refer to the firm's market-conduct surveillance program.

## Capital-markets-specific test-plan template additions

- `scope.product_perimeter` includes a capital-markets enum: `securities-based-lending`, `retail-margin`, `wealth-mortgage`, `wealth-line-of-credit`. Trading and execution products are excluded.
- `scope.wealth_population_caveat` — boolean; if true, wealth-population-skew open question is recorded for committee.
- `committee_approval_gate.private_bank_or_wealth_committee` — boolean; private-bank or wealth-management committee approval may join the fair-lending committee approval where the products are in their book.

## Common pitfalls in capital-markets fair-lending test plans

- Extending fair-lending scope into trading and execution activity; the perimeter is credit, not market activity.
- Treating SBL and margin as out of scope because they are capital-markets products; the credit-decision component is in ECOA scope.
- Ignoring the wealth-population-skew question; the test plan should at minimum surface the question for the fair-lending committee even where the firm has not yet designed a sizing-review framework.
- Defaulting to BISG without acknowledging that proxy accuracy may degrade in wealth-customer surname distributions.
