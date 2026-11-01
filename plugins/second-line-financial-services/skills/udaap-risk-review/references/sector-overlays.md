# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for udaap-risk-review

When the scope record names sector `banking`, this overlay adds banking-specific fact patterns, evidence sources, and review-gate detail to the UDAAP memo. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `udaap-risk-review/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for banking UDAAP review memos

Banking is one of the heaviest overlays on this skill. Most of the bureau's UDAAP enforcement and supervisory work has centered on depositories; the memo inherits that machinery directly.

##### 1. Recurring banking UDAAP themes

A non-exhaustive list of fact patterns that recur in banking UDAAP review:

- *Overdraft and NSF mechanics.* Authorize-positive-settle-negative (APSN) fees (Circular 2022-06); surprise representment NSF fees (Circular 2022-04); high-to-low transaction reordering for fee-maximisation; overdraft-protection program enrolment with deceptive opt-in; overdraft-program-related deposit-account closures.
- *Deposit-account fee mechanics.* Account-maintenance fee disclosure; minimum-balance-fee mechanics; surprise fees on dormant accounts; account-reopening fees on accounts the consumer believed closed (Circular 2023-02); paper-statement fees and electronic-delivery default state.
- *Mortgage servicing.* Loss-mitigation conduct (timing, completeness, accuracy of evaluation); force-placed insurance pricing and disclosure; fee assessment during loss-mit; payment-application order; escrow-account analysis; payoff-statement accuracy; transfer-of-servicing notices.
- *Credit-card UDAAP themes.* Deferred-interest promotion mechanics (the "no interest if paid in full" advertising vs. the back-end interest calculation); rewards-program changes (devaluation, expiration, mid-cycle term changes); balance-transfer fee mechanics; retention-offer mechanics; credit-card late-fee assessment in light of the §1026.52 amendment [verify operative status given litigation].
- *Auto-loan add-on products.* GAP, VSC, debt-cancellation, credit-life mechanics. Disclosure timing relative to closing; cancellation-and-refund mechanics; bundled-pricing transparency.
- *Indirect-auto dealer-finance practices.* Dealer-discretionary markup mechanics (the historical CFPB / DOJ focal area); add-on bundling at the dealer; the consumer's path to recourse.
- *Debt collection.* Convenience-fee mechanics (Pay-by-Phone Advisory Opinion 2022); debt-substantiation conduct; misrepresentations of legal status, credit-reporting consequences, or settlement terms.
- *Sales-practices conduct.* Account-opening-quota incentive design and the unauthorised-account-opening fact pattern; cross-sell mechanics; branch-incentive tie-backs to consumer-detrimental outcomes.

The memo names the in-scope theme(s); the element-analysis blocks address each theme separately where multiple are in scope.

##### 2. CFPB authority over banks

CFPB consumer-protection authority reaches large banks (over $10B in assets) for the named consumer-protection statutes including UDAAP. Smaller banks fall under the prudential regulator (OCC, FRB, FDIC) for supervisory purposes, but the substantive UDAAP standards apply across the size threshold. The memo records:

- Whether the institution is over the $10B threshold.
- The primary federal regulator for consumer-compliance supervision.
- Whether a CFPB enforcement angle is plausible on the in-scope fact pattern (driven by Supervisory Highlights focal items, peer enforcement actions, and the consumer-harm magnitude).

##### 3. Sponsor-bank arrangement attribution

Where the bank operates a sponsor-bank arrangement (deposit, card, lending program for a fintech partner, BaaS arrangement), UDAAP duty allocates per the program agreement and the bank's own consumer-compliance program. The interagency third-party guidance (June 2023) anchors the bank-side accountability; the bank is not insulated from UDAAP findings against the program operator. The memo records:

- Which legal entity holds the consumer-facing relationship (typically the sponsor bank for the deposit, card, or credit account).
- Which entity owns the product, marketing, and fee design at issue (often the program operator).
- Which second-line function is reviewing the in-scope fact pattern (typically the sponsor-bank consumer-compliance officer; sometimes joint with the fintech's compliance team).
- Joint approval and joint remediation framing where the fact pattern crosses both entities.

##### 4. Servicing-side UDAAP and CFPB Servicing Rules

Mortgage servicing UDAAP analysis interacts with the CFPB Servicing Rules (Reg X 12 CFR Part 1024 Subpart C; Reg Z 12 CFR §1026.41 periodic statements). Reg X §1024.41 (loss-mitigation procedures), §1024.39 (early intervention requirements), §1024.40 (continuity of contact), and the related provisions set the operational baseline; UDAAP analysis reaches conduct that complies with the literal Reg X requirements but materially misleads or harms the borrower in context.

##### 5. Deposit-account-specific evidence sources

Banking UDAAP review typically pulls evidence from:

- Core-banking-system transaction data (overdraft and NSF assessment patterns).
- Account-level fee-assessment logs.
- Branch and call-center call recordings (for the consumer-journey context).
- Marketing-asset library (for the deception-prong analysis).
- Complaint-management-system records (CFPB-portal complaints; firm-direct complaints).
- Account-disclosure documents and Reg DD §1030.4 truth-in-savings disclosures.

The memo names the evidence sources used and flags the sources that would be needed but are not yet available.

##### 6. Overdraft-as-fair-lending overlap

Where the overdraft-program impact is concentrated in particular customer segments, the UDAAP fact pattern can also raise a fair-lending angle (disparate-impact theory under ECOA / Reg B effects-test framing). The memo cross-references `fair-lending-test-plan` where the fact pattern raises the parallel ECOA theory; the UDAAP memo handles the §1031 elements, the fair-lending test plan handles the disparate-impact testing.

##### 7. AI / algorithmic surfaces in banking

Banks deploy AI / ML in marketing personalisation, retention-offer engines, fraud-deny decisioning, voice-agent customer service, conversational AI in the mobile app, and AI-generated communication. The AI-block in the memo names each in-scope AI surface and the UDAAP angle (typically unfairness on algorithmic outcome; deception on AI-generated communication; abusiveness on algorithmic dark-pattern design).

#### Banking-specific memo template additions

The following fields are added to the memo (mapped to schema where present):

- `scope.bank_size_threshold` — enum (`over-10b`, `under-10b`, `unknown`); drives CFPB authority framing.
- `scope.primary_federal_regulator` — enum (`OCC`, `FRB`, `FDIC`, `NCUA`, `n-a`).
- `scope.sponsor_bank_program` — boolean; if true, program agreement and joint review framing apply.
- `scope.servicing_rules_intersection` — boolean; if true, Reg X / Reg Z servicing rules baseline is named alongside the UDAAP analysis.
- `recurring_banking_themes[]` — list of themes from the recurring-themes catalogue above that the in-scope fact pattern matches.
- `evidence_base[].core_banking_system` — true where transaction-level evidence is pulled from core-banking systems.
- `cross_reference_skills[]` — extends to include `fair-lending-test-plan` where the fact pattern raises a parallel ECOA theory.

#### Common pitfalls in banking UDAAP review memos

- Treating CFPB authority as out of scope because the bank is OCC- or FRB-supervised; CFPB authority reaches large banks for the named consumer-protection statutes including UDAAP.
- Reading overdraft mechanics through the Reg E §1005.17 opt-in lens only and missing the unfairness analysis on the post-opt-in fee mechanic; opt-in compliance is a baseline, not a UDAAP defence.
- Treating the Reg X §1024.41 loss-mit checklist as a UDAAP defence; conduct that complies with the literal Reg X timing and content requirements can still raise UDAAP concerns where the loss-mit-evaluation accuracy or the borrower communication misleads.
- Sponsor-bank programs treated as the program-operator's UDAAP issue; the bank retains accountability under the third-party guidance and the program agreement.
- Auto-add-on review reading the disclosure document in isolation from the closing-flow context; UDAAP analysis reaches the moment of consumer commitment.
- Card-rewards-program changes reviewed for Reg Z §1026.9 change-in-terms compliance only and missing the deception analysis on the marketing of the rewards program over time.
- Sales-practices fact patterns reviewed only for the unauthorised-account-opening conduct and missing the underlying incentive-design root cause; the conduct-risk implications block names the incentive design.
- Treating AI-driven retention offers or AI-driven communication as out of UDAAP scope because the AI is "just personalisation"; the bureau has been explicit that existing UDAAP authority reaches algorithmic outcomes.

## capital-markets

### Capital markets sector overlay for udaap-risk-review

When the scope record names sector `capital-markets`, this overlay sets the scope boundary first. Most capital-markets activity sits outside the CFPB UDAAP perimeter. Where it does touch, the touch points are predictable and narrow. The overlay is short on purpose.

Loaded by: `udaap-risk-review/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type implicates a broker-dealer, investment adviser, private bank, or wealth-management entity that operates a retail consumer-facing credit, deposit-equivalent, or consumer-finance product surface.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for capital-markets UDAAP review memos

##### 1. Scope boundary first

Most capital-markets activity is not in CFPB UDAAP scope. Securities trading, asset management, institutional brokerage, and investment-adviser portfolio management do not extend consumer financial products and services as defined in Dodd-Frank Title X; CFPB UDAAP authority does not reach them. The capital-markets UDAAP perimeter is narrow:

- Securities-based lending (SBL) to retail clients, including individual customers of private-bank and wealth-management businesses.
- Margin lending to retail customers (the credit-decision component is in CFPB UDAAP scope alongside the FINRA Rule 4210 / Reg T framework).
- Mortgage origination by capital-markets-affiliated entities (where the bank holding company operates a mortgage subsidiary; the mortgage entity carries the banking sector overlay).
- Wealth-credit products (jumbo mortgages, lines of credit secured by assets) where the bank or broker-dealer is the creditor.
- Cash-management and deposit-equivalent surfaces inside brokerage accounts (sweep programs; cash-management features) where the consumer-experience flow on fees, disclosures, or account-closure mechanics raises UDAAP-equivalent concerns.

Activity that is not consumer-financial-product-or-service (advisory recommendations, trade execution, custody, trading-platform fees on retail brokerage where the SEC and FINRA rule frameworks govern) is outside CFPB UDAAP scope. The overlapping consumer-protection regime is sales-practice fairness and best-interest framing under Reg BI for broker-dealers (17 CFR §240.15l-1) and the fiduciary duty for investment advisers under the IAA. Those are not CFPB UDAAP tests.

##### 2. Reg BI / FINRA Rule 2010 overlap

Where the in-scope fact pattern is a retail-broker sales-practice issue (steering between products with different revenue economics; payment-for-order-flow disclosure mechanics; account-conversion friction; fee-and-charge mechanics on brokerage accounts), the overlapping framework is Reg BI plus FINRA Rule 2010 (standards of commercial honor and just and equitable principles of trade) plus FINRA Rule 2210 (communications with the public). The substantive themes overlap with UDAAP though the legal frameworks differ. The memo:

- Names whether CFPB UDAAP authority is plausible on the fact pattern (driven by whether the product or service falls within the consumer-financial-product-or-service definition under Dodd-Frank §1002).
- Names the parallel SRO / SEC framework that applies (Reg BI; FINRA Rule 2010; FINRA Rule 2210).
- Names the firm's own market-conduct framework as the operational reviewer (the firm's broker-dealer compliance and supervision function, not the consumer-compliance function, typically reviews the fact pattern).

##### 3. SBL and margin-lending UDAAP fact patterns

Where SBL or retail margin lending is in scope, the regular UDAAP machinery applies:

- Disclosure of margin mechanics and the margin-call-and-liquidation flow.
- Fee and rate mechanics on the SBL or margin facility.
- Consumer-experience design at margin-call.
- Marketing of SBL and margin to retail and wealth clients.

The element analysis covers the three prongs as in any other consumer-credit product. The conduct-risk implications block names the wealth-management or private-bank conduct framework alongside the consumer-compliance framework; in practice, both forums review the fact pattern.

##### 4. Wealth-credit specific themes

Wealth-credit products to high-net-worth and ultra-high-net-worth clients raise their own UDAAP angles where the consumer-experience flow obscures the cost or the consequences of the credit (fee mechanics on wealth-mortgage products, cancellation friction on lines of credit, disclosure timing relative to the wealth-management relationship). The memo records these where in scope; the wealth-population skew is not itself a UDAAP question (it is a fair-lending question, see `fair-lending-test-plan`).

##### 5. Cash-management and sweep-program themes

Brokerage cash-management features and sweep programs (automated sweeps to bank-affiliated deposit accounts; rate spreads on the sweep rate vs. the prevailing market rate; disclosure of the rate-spread mechanic) have been a focal area in recent SEC and (at the bank-affiliate level) prudential-regulator and CFPB attention. The memo:

- Names the sweep-rate disclosure as the operative fact under deception analysis.
- Names the rate-spread mechanic as the operative fact under unfairness analysis (substantial injury through the rate spread; reasonable-avoidability through the consumer's ability to opt out and select a different cash-management option; countervailing-benefits analysis on the convenience offered by the sweep).
- Cross-references the broker-dealer-side disclosure obligations under Reg BI.

##### 6. Non-applicability for trading-and-execution activity

Trading desks, execution algorithms, market-making, and surveillance models are out of CFPB UDAAP scope. They sit under the SEC market-integrity regime (Rule 15c3-5 broker-dealer market-access controls), FINRA supervision rules, and the firm's market-conduct framework. Do not extend the UDAAP memo into trading activity; flag the scope boundary and refer to the firm's market-conduct surveillance program.

#### Capital-markets-specific memo template additions

- `scope.product_perimeter_capital_markets[]` — enum list (`securities-based-lending`, `retail-margin`, `wealth-mortgage`, `wealth-line-of-credit`, `brokerage-cash-management-sweep`, `retail-broker-sales-practice`).
- `scope.cfpb_authority_plausible` — boolean; explicit flag to record whether CFPB UDAAP authority reaches the in-scope fact pattern.
- `scope.parallel_sro_or_sec_framework[]` — list of overlapping frameworks (`Reg-BI`, `FINRA-Rule-2010`, `FINRA-Rule-2210`, `IAA-fiduciary-duty`, `SEC-Rule-15c3-5`).
- `committee_approval_gate.private_bank_or_wealth_committee` — boolean; private-bank or wealth-management committee approval may join the UDAAP-decision forum where the products are in their book.

#### Common pitfalls in capital-markets UDAAP review memos

- Extending CFPB UDAAP scope into trading and execution activity; the perimeter is consumer-financial-product-or-service, not market activity.
- Treating SBL and margin as out of UDAAP scope because they are capital-markets products; the credit-decision component and the consumer-experience flow are in scope.
- Reviewing a retail-broker sales-practice issue under Reg BI only and missing the overlapping CFPB UDAAP framing where the underlying product is a consumer-financial-product-or-service.
- Sweep-program review limited to the SEC disclosure framework; the fact pattern can also raise CFPB UDAAP angles where the sweep is into a bank-affiliated deposit account and the disclosure-and-rate-spread mechanic implicates the deposit-side consumer-protection regime.
- Wealth-credit review running on the assumption that wealth clients are sophisticated and therefore outside UDAAP; the substantive UDAAP analysis applies to the consumer-experience design regardless of the consumer's sophistication, though the reasonable-consumer framing may shift.
- Conflating CFPB UDAAP review with FINRA suitability or Reg BI best-interest review; the regimes are aligned in spirit but the legal architecture and the operational reviewer differ.

## insurance

### Insurance sector overlay for udaap-risk-review

When the scope record names sector `insurance`, this overlay sets the scope boundary first. Insurance unfair-trade-practice review sits with state insurance departments under the NAIC Unfair Trade Practices Act framework and state-DOI statutes, not under Dodd-Frank UDAAP. The UDAAP review skill is the wrong tool for most insurance review work.

Loaded by: `udaap-risk-review/SKILL.md` when `scope.sector_overlay_set` includes `insurance`, or when the institution type implicates a life, health, or property-and-casualty insurer.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Scope boundary

The vocabulary differs. Insurance regulators talk about "unfair trade practices" and "unfair claims settlement practices" under the NAIC Unfair Trade Practices Act (Model #880) and state-DOI statutes implementing the model. The substantive tests differ from UDAAP: the unfair-discrimination framing centers on whether underwriting and pricing reflect a sound actuarial basis and are not unfairly discriminatory between similarly-situated risks; the unfair-claims-settlement framing centers on bad-faith claims handling under state statutes and common-law doctrine. Dodd-Frank §1031 element tests do not naturally apply to most insurance fact patterns because insurance is not a consumer-financial-product-or-service under Dodd-Frank Title X (with the narrow exceptions noted below).

For most insurance fair-treatment review work, route to:

- The firm's own insurance-conduct or market-conduct review program.
- State-DOI market-conduct examination procedures.
- The NAIC Market Regulation Handbook for the operational baseline on market-conduct review.
- The NAIC AI Model Bulletin (December 2023) where the institution uses AI / ML in underwriting, pricing, marketing, claims, or fraud detection.
- The NYDFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) for NY-licensed life insurers.
- The Colorado Division of Insurance regulation implementing SB 21-169 for CO life-insurance underwriting using ECDIS or predictive models.

Those are the operative regimes. The UDAAP review skill is built around Dodd-Frank §1031 / §1036 and does not naturally extend into them.

#### Where the UDAAP review skill does apply on the insurance side

Three narrow cases:

##### 1. Credit-protection insurance bundled with a credit product

Where the institution sells credit-protection insurance (credit life, debt-cancellation, GAP, VSC bundled with auto-loan) packaged with an underlying credit product (mortgage, card, personal loan, auto loan), the credit-side decision (the bundling mechanic, the disclosure of the insurance fee in the cost-of-credit framing, the cancellation flow, the relationship between the insurance product and the credit product) is in CFPB UDAAP scope. The insurance-side decision (eligibility, pricing of the insurance product itself) is out of UDAAP scope and routes to the insurance-conduct framework.

The bundled-product seam is a recurring CFPB enforcement and supervisory focal area; the bureau has pursued fact patterns on auto add-on bundling, deferred-amortisation mechanics on credit-life, and disclosure-of-cost mechanics across multiple consent orders.

##### 2. Marketing surface that distributes both credit and insurance

Where the institution operates a marketing surface that distributes both credit and insurance products to overlapping customer audiences, the marketing of the credit product is in UDAAP scope. The marketing of the insurance product is in the insurance-conduct framework. Where the marketing copy obscures the boundary (bundles credit and insurance in a single representation), the deception analysis on the credit-side representation is in scope.

##### 3. CFPB-jurisdictional consumer-finance products that have an insurance component

Edge cases where the consumer-finance product has an embedded insurance feature (e.g., a deposit account with embedded insurance benefits) require careful boundary work. The consumer-finance side is in CFPB UDAAP scope; the insurance side routes to the insurance-conduct framework. The memo records the boundary explicitly.

#### What does not extend into the UDAAP review skill

- Life-insurance underwriting and pricing, including ECDIS / AI / predictive-model use in underwriting. Apply the NAIC AI Model Bulletin, the NYDFS Insurance Circular Letter, the CO regulation per state footprint.
- Health-insurance underwriting and pricing. ACA non-discrimination provisions and HHS / state-DOI regimes apply.
- P&C insurance underwriting and pricing. State-DOI unfair-discrimination statutes apply; the NAIC AI Model Bulletin reaches insurer use of AI systems.
- Insurance claims handling. Bad-faith claims-handling and unfair-claims-settlement-practice statutes apply; the NAIC Unfair Trade Practices Act and state-DOI frameworks govern.
- Insurance marketing as such (apart from the bundled-marketing edge case in #2 above). State-DOI advertising review and the NAIC Advertisements of Life Insurance and Annuities Model Regulation (Model #570) and similar A&H model regulations apply.

The UDAAP review skill does not resize itself into an insurance unfair-trade-practice review. Reviewers asked to do insurance unfair-trade-practice work should route to the insurance-side skill set; this plugin's six skills do not currently cover the insurance-conduct frame as a primary surface.

#### Insurance-specific memo template additions

The fields are minimal because the overlay is mostly a scope boundary. Where the narrow in-scope cases apply:

- `scope.bundled_credit_protection_insurance` — boolean; if true, the credit-side bundling mechanic is the in-scope UDAAP fact pattern; insurance-side eligibility and pricing are explicitly out of scope.
- `scope.credit_and_insurance_marketing_surface` — boolean; if true, the marketing-side review on the credit product is in scope; insurance-product marketing routes separately.
- `out_of_scope_routing[]` — list of insurance-conduct frameworks the memo routes to (NAIC AI Model Bulletin, NYDFS Circular Letter, CO regulation, state-DOI market-conduct procedures, NAIC Market Regulation Handbook, NAIC Model #880 unfair trade practices, state-DOI claims-settlement statutes).

#### Common pitfalls when insurance is flagged

- Building a UDAAP memo for an insurance underwriting model; the regime is wrong. Route to the insurance unfair-trade-practice framework.
- Treating the NAIC AI Model Bulletin as a UDAAP-equivalent obligation; the bulletin sets governance and AIS-program expectations, not Dodd-Frank §1031 element-test expectations.
- Reading the bundled-credit-protection seam without separating the credit-side decision (in UDAAP scope) from the insurance-side decision (out of UDAAP scope); the consumer-experience flow seam runs through both regimes.
- Extending the §1031 element analysis into life or health-insurance underwriting; the substantive standards differ and the analytical conclusions do not port cleanly.
- Treating bad-faith-claims-handling fact patterns as UDAAP; bad faith is a state common-law and statutory regime, not a CFPB UDAAP frame.

## payments-fintech

### Payments and fintech sector overlay for udaap-risk-review

When the scope record names sector `payments-fintech`, this overlay adds payments- and fintech-specific fact patterns, evidence sources, and accountability framing to the UDAAP memo. Where there is conflict between the capability defaults and this overlay, the overlay governs the sector elements.

Loaded by: `udaap-risk-review/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a fintech consumer-credit platform, sponsor-bank-program operator, BNPL provider, prepaid issuer, P2P or instant-payment platform, neobank, or non-bank consumer-finance entity.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for payments and fintech UDAAP review memos

CFPB UDAAP authority under Dodd-Frank Title X reaches non-bank consumer-credit and consumer-financial-services providers. The fact-pattern catalogue is different from banking but the legal framework is the same; the overlay names the structural details that change.

##### 1. Sponsor-bank attribution and joint accountability

Most fintech consumer-credit and many fintech deposit-equivalent products operate through a sponsor-bank arrangement. The UDAAP duty allocates per the program agreement and per the sponsor bank's consumer-compliance program. The memo records:

- Which legal entity holds the consumer-facing legal relationship.
- Which entity owns the product design, the marketing surface, and the fee architecture.
- Which second-line function reviews the in-scope fact pattern.
- Which committee approves remediation (sponsor-bank consumer-compliance committee; sometimes joint with the fintech AI risk committee or product committee).

The interagency third-party guidance (June 2023) anchors the bank-side accountability; the program operator is not the sole accountable party even where the operator built and operates the product.

##### 2. Recurring fintech and payments UDAAP themes

A non-exhaustive list of fact patterns:

- *"Instant funding" fee mechanics.* Personal-loan and earned-wage-access products that offer instant funding for an additional fee or "tip", with the fee disclosed at the funding-selection step rather than at application; the APR shown at application does not include the funding fee. Element analysis: deception (the application-page APR misleads if funding fee is excluded); unfairness (consumer commitment is high at the funding-selection step, reasonable-avoidability turns on the slow-funding alternative being symmetric in the UI).
- *Tip and donation mechanics.* Earned-wage-access and small-dollar-credit products that present "tips" or "donations" as voluntary while structuring the consumer-journey to make the tip the default state; the cost of the financial product is communicated through a tip mechanic. Element analysis: abusiveness (material interference with the consumer's ability to understand the actual cost); deception where the "voluntary" framing misleads.
- *Subscription and negative-option mechanics.* Products with auto-renewal, recurring fees, or continuation by default; cancellation friction; opt-out asymmetry. Element analysis: unfairness (substantial injury, not reasonably avoidable through the cancellation friction); abusiveness (material interference with the cancellation flow).
- *BNPL UDAAP themes.* Late fees, returned-payment fees, dispute-resolution conduct, autopay-default mechanics, multi-merchant payment-allocation logic, the consumer's understanding of the credit nature of the product. Element analysis spans deception (marketing of "no interest" without the fee context), unfairness (fee mechanics on missed payments), and abusiveness (cancellation and dispute friction). The bureau's BNPL Interpretive Rule (May 2024) was **nullified by Pub. L. 119-11 (May 9, 2025); historical only.** Reg Z and the underlying consumer-protection framework apply on their own terms based on the product structure rather than through the nullified interpretive rule.
- *P2P and instant-payment unauthorised-transfer conduct.* Unauthorised-transfer dispute handling on P2P platforms (Zelle-style and stand-alone P2P apps) under Reg E §1005.6 and §1005.11; refusal to credit or delayed credit on disputed transfers; deceptive representations during the dispute process. Element analysis: deception on the dispute communications; unfairness on the substantial injury and the reasonable-avoidability of the unauthorised transfer.
- *Algorithmic personalisation themes.* Personalised pricing, retention offers, AI-driven communication, lookalike-audience marketing. Element analysis ties to the AI / algorithmic-discrimination block in the main flow; the bureau's posture under the April 2023 Joint Statement is that existing UDAAP authority reaches algorithmic outcomes.
- *Crypto-adjacent consumer-finance products.* Where in scope, the same UDAAP framework applies; the bureau and the FTC have pursued fact patterns on the disclosure, custody, and recovery-of-funds mechanics. Confirm jurisdictional posture (CFPB; FTC; SEC where the product crosses into securities) before applying.
- *Fee-stacking on small-dollar credit.* Daily-fee, rollover, and reactivation mechanics on small-dollar products; the consumer's path to repayment without additional fees.
- *Account-closure and recovery friction.* Friction on closing fintech-program deposit-equivalent accounts; recovery-of-funds friction after account closure; the consumer's path to dispute or escalate.

##### 3. State licensure and CFPB authority

CFPB consumer-protection authority reaches non-bank consumer-credit and consumer-financial-services providers under Dodd-Frank Title X. State licensure (consumer-lender licences, money-transmission licences) brings state examiners; multi-state CSBS-coordinated exams may apply. State AG offices have UDAP enforcement authority under state baby-FTC acts. The memo records:

- The state-licensure footprint and the strictest-applicable-state posture for any state with prescribed UDAAP-equivalent obligations beyond the federal baseline.
- Whether multi-state coordinated exams are likely on the in-scope fact pattern.
- Whether state AG enforcement is a plausible exposure (driven by state-AG focal items, peer state-AG actions, and the consumer-harm geography).

##### 4. Marketing-funnel UDAAP angles

Fintech consumer-finance acquisition typically runs through digital channels (search, social, lookalike audiences, partner marketplaces, embedded-finance partner surfaces). UDAAP review reaches the marketing surface:

- *Pre-screen and lookalike-audience targeting.* Where the lookalike-audience model concentrates marketing on segments unlikely to qualify or unable to use the product, the UDAAP analysis on the substantial injury and reasonable-avoidability prongs may apply.
- *Embedded-finance surfaces.* Where the in-scope product is offered through an embedded-finance partner (e-commerce checkout, marketplace integration), the consumer-experience flow at the partner surface is part of the UDAAP perimeter; the partner is a third party but the program operator and the sponsor bank retain accountability.
- *Cross-reference `marketing-claim-review`* for asset-level marketing-claim review; this skill addresses UDAAP at the product-flow level, the marketing-claim-review skill addresses the asset-level claim.

##### 5. AI / algorithmic-surface review

Fintech surfaces are typically AI-heavy: personalisation, dynamic pricing, conversational AI, agentic flows, AI-generated communication. The AI-block in the memo names each in-scope AI surface and the UDAAP angle. The bureau has been explicit that existing UDAAP authority reaches algorithmic outcomes (April 2023 Joint Statement; CFPB Circulars 2022-03 and 2023-03 on adverse action and complex models).

##### 6. Evidence sources

Fintech UDAAP review typically pulls evidence from:

- The application platform and the consumer-journey logging.
- The fee-assessment logs (transaction-level).
- The marketing platform exports (audience definition, served-impression and click data).
- The customer-support ticketing system and the call-center recordings.
- The complaint-management system (CFPB-portal complaints; app-store review patterns; firm-direct complaints; social-signal patterns).
- The model-platform feature store and the model-card library for AI surfaces in path.
- The sponsor-bank's compliance-monitoring outputs (where joint).

##### 7. Reg E and Reg Z framework intersections

For payments products, Reg E §1005 (unauthorised transfers, error resolution) and Reg Z §1026 (credit) are the operational baselines; UDAAP reaches conduct that complies with the literal regulatory requirements but misleads or harms in context. The memo names the operative Reg E or Reg Z provision and the UDAAP angle alongside it; the memo does not duplicate the Reg E or Reg Z compliance review.

#### Payments and fintech-specific memo template additions

The following fields are added to the memo (mapped to schema where present):

- `scope.legal_entity_type` — enum (`fintech-program-operator`, `sponsor-bank-program`, `non-bank-consumer-finance`, `BNPL`, `P2P-or-instant-payment`, `prepaid-issuer`, `embedded-finance-partner`, `other`).
- `scope.sponsor_bank_program` — boolean; if true, sponsor-bank consumer-compliance officer named as joint reviewer.
- `scope.state_licensure_footprint[]` — list of states with consumer-lender or money-transmission licences.
- `recurring_fintech_themes[]` — list of themes from the recurring-themes catalogue above that the in-scope fact pattern matches.
- `marketing_funnel_in_scope` — boolean; if true, the marketing-funnel UDAAP review is in scope.
- `embedded_finance_partner_in_scope` — boolean; if true, the partner-surface consumer-experience flow is part of the UDAAP perimeter.
- `cross_reference_skills[]` — extends to include `marketing-claim-review`, `complaint-theme-analysis`, `vendor-diligence` where the fact pattern invokes those.

#### Common pitfalls in payments and fintech UDAAP review memos

- Assuming the fintech is the sole accountable party when the sponsor bank inherits creditor-of-record duty; bank examiners catch this in third-party reviews and the bank's UDAAP exposure can be greater than the program operator's.
- Reading the Reg E §1005.11 error-resolution process as the entire UDAAP analysis on a P2P unauthorised-transfer fact pattern; UDAAP reaches the dispute communications and the substantial-injury analysis on the underlying unauthorised transfer.
- Treating BNPL as out of UDAAP scope on the assumption that BNPL is not credit; the underlying consumer-protection framework reaches BNPL based on the product structure. (The May 2024 CFPB BNPL Interpretive Rule was **nullified by Pub. L. 119-11 (May 9, 2025); historical only** — anchor the analysis to the regulatory text rather than the nullified interpretive rule.)
- "Tip" mechanics on earned-wage-access and small-dollar credit treated as outside the cost-of-credit framing; the bureau's UDAAP framing reaches the tip-as-cost mechanic and the consumer-journey design that makes the tip the default.
- Subscription-style fee mechanics reviewed for FTC Negative Option Rule compliance only and missing the abusiveness analysis on the cancellation friction; both regimes apply.
- Lookalike-audience targeting treated as out of UDAAP scope because the audience is "just marketing"; the bureau and the FTC have both pursued algorithmic-targeting fact patterns.
- AI-driven personalisation reviewed as a model-risk question only and missing the consumer-surface UDAAP angle; AI-block in the memo is mandatory.
- Embedded-finance partner surfaces treated as the partner's responsibility; the program operator and sponsor bank retain accountability for the consumer-experience flow at the partner surface.
- State AG enforcement angle missed because the memo focuses on CFPB authority only; many of the highest-profile fintech UDAAP-equivalent actions have been state AG actions under state baby-FTC acts.
