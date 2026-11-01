# Capital markets sector overlay for udaap-risk-review

When the scope record names sector `capital-markets`, this overlay sets the scope boundary first. Most capital-markets activity sits outside the CFPB UDAAP perimeter. Where it does touch, the touch points are predictable and narrow. The overlay is short on purpose.

Loaded by: `udaap-risk-review/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type implicates a broker-dealer, investment adviser, private bank, or wealth-management entity that operates a retail consumer-facing credit, deposit-equivalent, or consumer-finance product surface.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for capital-markets UDAAP review memos

### 1. Scope boundary first

Most capital-markets activity is not in CFPB UDAAP scope. Securities trading, asset management, institutional brokerage, and investment-adviser portfolio management do not extend consumer financial products and services as defined in Dodd-Frank Title X; CFPB UDAAP authority does not reach them. The capital-markets UDAAP perimeter is narrow:

- Securities-based lending (SBL) to retail clients, including individual customers of private-bank and wealth-management businesses.
- Margin lending to retail customers (the credit-decision component is in CFPB UDAAP scope alongside the FINRA Rule 4210 / Reg T framework).
- Mortgage origination by capital-markets-affiliated entities (where the bank holding company operates a mortgage subsidiary; the mortgage entity carries the banking sector overlay).
- Wealth-credit products (jumbo mortgages, lines of credit secured by assets) where the bank or broker-dealer is the creditor.
- Cash-management and deposit-equivalent surfaces inside brokerage accounts (sweep programs; cash-management features) where the consumer-experience flow on fees, disclosures, or account-closure mechanics raises UDAAP-equivalent concerns.

Activity that is not consumer-financial-product-or-service (advisory recommendations, trade execution, custody, trading-platform fees on retail brokerage where the SEC and FINRA rule frameworks govern) is outside CFPB UDAAP scope. The overlapping consumer-protection regime is sales-practice fairness and best-interest framing under Reg BI for broker-dealers (17 CFR §240.15l-1) and the fiduciary duty for investment advisers under the IAA. Those are not CFPB UDAAP tests.

### 2. Reg BI / FINRA Rule 2010 overlap

Where the in-scope fact pattern is a retail-broker sales-practice issue (steering between products with different revenue economics; payment-for-order-flow disclosure mechanics; account-conversion friction; fee-and-charge mechanics on brokerage accounts), the overlapping framework is Reg BI plus FINRA Rule 2010 (standards of commercial honor and just and equitable principles of trade) plus FINRA Rule 2210 (communications with the public). The substantive themes overlap with UDAAP though the legal frameworks differ. The memo:

- Names whether CFPB UDAAP authority is plausible on the fact pattern (driven by whether the product or service falls within the consumer-financial-product-or-service definition under Dodd-Frank §1002).
- Names the parallel SRO / SEC framework that applies (Reg BI; FINRA Rule 2010; FINRA Rule 2210).
- Names the firm's own market-conduct framework as the operational reviewer (the firm's broker-dealer compliance and supervision function, not the consumer-compliance function, typically reviews the fact pattern).

### 3. SBL and margin-lending UDAAP fact patterns

Where SBL or retail margin lending is in scope, the regular UDAAP machinery applies:

- Disclosure of margin mechanics and the margin-call-and-liquidation flow.
- Fee and rate mechanics on the SBL or margin facility.
- Consumer-experience design at margin-call.
- Marketing of SBL and margin to retail and wealth clients.

The element analysis covers the three prongs as in any other consumer-credit product. The conduct-risk implications block names the wealth-management or private-bank conduct framework alongside the consumer-compliance framework; in practice, both forums review the fact pattern.

### 4. Wealth-credit specific themes

Wealth-credit products to high-net-worth and ultra-high-net-worth clients raise their own UDAAP angles where the consumer-experience flow obscures the cost or the consequences of the credit (fee mechanics on wealth-mortgage products, cancellation friction on lines of credit, disclosure timing relative to the wealth-management relationship). The memo records these where in scope; the wealth-population skew is not itself a UDAAP question (it is a fair-lending question, see `fair-lending-test-plan`).

### 5. Cash-management and sweep-program themes

Brokerage cash-management features and sweep programs (automated sweeps to bank-affiliated deposit accounts; rate spreads on the sweep rate vs. the prevailing market rate; disclosure of the rate-spread mechanic) have been a focal area in recent SEC and (at the bank-affiliate level) prudential-regulator and CFPB attention. The memo:

- Names the sweep-rate disclosure as the operative fact under deception analysis.
- Names the rate-spread mechanic as the operative fact under unfairness analysis (substantial injury through the rate spread; reasonable-avoidability through the consumer's ability to opt out and select a different cash-management option; countervailing-benefits analysis on the convenience offered by the sweep).
- Cross-references the broker-dealer-side disclosure obligations under Reg BI.

### 6. Non-applicability for trading-and-execution activity

Trading desks, execution algorithms, market-making, and surveillance models are out of CFPB UDAAP scope. They sit under the SEC market-integrity regime (Rule 15c3-5 broker-dealer market-access controls), FINRA supervision rules, and the firm's market-conduct framework. Do not extend the UDAAP memo into trading activity; flag the scope boundary and refer to the firm's market-conduct surveillance program.

## Capital-markets-specific memo template additions

- `scope.product_perimeter_capital_markets[]` — enum list (`securities-based-lending`, `retail-margin`, `wealth-mortgage`, `wealth-line-of-credit`, `brokerage-cash-management-sweep`, `retail-broker-sales-practice`).
- `scope.cfpb_authority_plausible` — boolean; explicit flag to record whether CFPB UDAAP authority reaches the in-scope fact pattern.
- `scope.parallel_sro_or_sec_framework[]` — list of overlapping frameworks (`Reg-BI`, `FINRA-Rule-2010`, `FINRA-Rule-2210`, `IAA-fiduciary-duty`, `SEC-Rule-15c3-5`).
- `committee_approval_gate.private_bank_or_wealth_committee` — boolean; private-bank or wealth-management committee approval may join the UDAAP-decision forum where the products are in their book.

## Common pitfalls in capital-markets UDAAP review memos

- Extending CFPB UDAAP scope into trading and execution activity; the perimeter is consumer-financial-product-or-service, not market activity.
- Treating SBL and margin as out of UDAAP scope because they are capital-markets products; the credit-decision component and the consumer-experience flow are in scope.
- Reviewing a retail-broker sales-practice issue under Reg BI only and missing the overlapping CFPB UDAAP framing where the underlying product is a consumer-financial-product-or-service.
- Sweep-program review limited to the SEC disclosure framework; the fact pattern can also raise CFPB UDAAP angles where the sweep is into a bank-affiliated deposit account and the disclosure-and-rate-spread mechanic implicates the deposit-side consumer-protection regime.
- Wealth-credit review running on the assumption that wealth clients are sophisticated and therefore outside UDAAP; the substantive UDAAP analysis applies to the consumer-experience design regardless of the consumer's sophistication, though the reasonable-consumer framing may shift.
- Conflating CFPB UDAAP review with FINRA suitability or Reg BI best-interest review; the regimes are aligned in spirit but the legal architecture and the operational reviewer differ.
