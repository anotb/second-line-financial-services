# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for marketing-claim-review

When the scope record names sector `banking`, this overlay adds banking-specific disclosure rules, FDIC-attribution mechanics, and recurring fact patterns to the asset-level marketing review. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `marketing-claim-review/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for banking marketing-review memos

Banking is one of the heaviest overlays on this skill. Most consumer-financial advertising rules and the FDIC-attribution framework are banking-specific.

##### 1. Deposit-account advertising under Regulation DD

For deposit-account assets (checking, savings, MMA, time deposit), the operative rule is the truth-in-savings advertising rule. The asset-level review reads:

- The clear-and-conspicuous standard on the rate or APY representation.
- Trigger-term mechanics (a bonus; the APY; the term of a time account; certain other elements) requiring the additional disclosures.
- Bonus disclosure requirements where the asset markets a deposit-opening bonus.
- The exemption framework where the asset is a brief broadcast or other low-information surface.

Where the deposit asset omits a triggered disclosure (the recurring failure mode is mobile-vs-desktop layout drift), the memo records the finding and the recommended remediation by device class.

##### 2. FDIC insurance representation under 12 CFR Part 328

For any asset that promotes a deposit product or that operates on a consumer-facing surface where a reasonable consumer might infer FDIC insurance, the FDIC advertising rule applies. The asset-level review reads:

- The official advertising statement requirement on insured-depository-promoting advertisements.
- Misrepresentation analysis where a non-bank entity (or a bank-affiliated non-deposit product) might be read as FDIC-insured.
- The 2022 final rule on §328.5 and its application to fintech-attribution patterns (sponsor-bank sweep programs; cash-management surfaces; non-bank fintech surfaces partnered with insured depositories).

The memo names the fintech-attribution analysis where the asset operates on a sponsor-bank or BaaS-style surface; the failure mode is fintech surfaces that lead a reasonable consumer to believe a non-deposit product is FDIC-insured, or that misrepresent the scope of FDIC insurance coverage on sweep-style products.

##### 3. Mortgage advertising under TILA / RESPA / TRID

For mortgage assets (purchase-money mortgage; refinance; HELOC; home-equity loan; reverse mortgage), the operative framework spans Regulation Z closed-end advertising rules (with the §1026.24(i) mortgage-specific prohibitions), the HELOC advertising rule for HELOCs, and the TRID-adjacent disclosure mechanics where the asset previews mortgage terms. The asset-level review reads:

- §1026.24(i) prohibitions: misleading payment claims; misleading comparisons; misuse of "government" terms; misleading use of the current lender's name; misleading claims of debt elimination; misleading use of "counselor"; foreign-language disclosures (the asset must disclose in the same language as the advertisement).
- HELOC-specific advertising rule additions for HELOC assets.
- TRID-adjacent reading on rate-quote pages, pre-qualification screens, monthly-payment calculators where the marketing previews mortgage terms; the marketing review does not draft the Loan Estimate but reads whether the marketing leads a reasonable consumer to believe the marketing preview is the disclosure.
- FHA §3604(c) discriminatory-advertising read on mortgage marketing distribution and content (the dwelling-related advertising prohibition is operative).

##### 4. CRA-related advertising

For assets in CRA-relevant marketing (community development products; LMI-targeted credit products; small-business products in CRA assessment areas), the asset-level review notes whether the marketing distribution is consistent with the bank's CRA assessment-area framework and whether the marketing content claims about LMI focus or community-development orientation are substantiated. CRA examination procedures read marketing distribution as one input to the assessment-area analysis; the asset-level review surfaces the relevant facts without performing the CRA assessment.

##### 5. Card application and solicitation under §1026.60

For card-account assets (credit card; charge card) that constitute applications or solicitations under Regulation Z, the §1026.60 tabular-disclosure framework (the "Schumer box") applies. The asset-level review reads:

- Whether the asset is an application or solicitation under §1026.60 (channel-specific tests for direct-mail, electronic, telephone, in-person, publicly-available).
- The §1026.60(b) tabular disclosure presence and accuracy.
- The channel-specific additional rules.

The Schumer-box requirements are detailed and are the most-frequent enforcement target for card-marketing review.

##### 6. Sponsor-bank attribution where the bank operates a fintech program

Where the bank is the sponsor for a fintech consumer-finance program, marketing assets bearing the program's brand may also implicate the bank's UDAAP and advertising-rule duties. The interagency third-party guidance (June 2023) anchors the bank-side accountability. The memo records:

- Whether the asset bears the bank's name or logo.
- Whether a reasonable consumer would attribute the asset to the bank.
- The bank-side review obligation and the fintech-side review obligation under the program agreement.

##### 7. Bank-specific evidence sources

Banking marketing-review typically pulls evidence from:

- The marketing-asset library (versioned, by channel, by audience).
- The MAP record system (advertising-review approvals; substantiation files; sign-off audit trail).
- The CRA management system for CRA-relevant marketing.
- The deposit-product fee schedule and Reg DD §1030.4 truth-in-savings disclosures (for the deposit-asset cross-reference).
- The Schumer-box source-of-truth system for card-application substantiation.
- The complaint-management-system records (CFPB-portal complaints filtered by "advertising" or "disclosure" themes; firm-direct complaints).

The memo names the evidence sources used and flags the sources that would be needed but are not yet available.

#### Banking-specific memo template additions

The following fields are added to the per-asset block:

- `asset.product_type` — enum (`deposit-checking`, `deposit-savings`, `deposit-mma`, `deposit-time`, `card-credit`, `card-charge`, `mortgage-purchase`, `mortgage-refi`, `heloc`, `home-equity-loan`, `reverse-mortgage`, `auto`, `personal-loan`, `small-business`, `other`).
- `asset.fdic_attribution_in_play` — boolean; if true, the §328.4/§328.5 read is required.
- `asset.is_card_application_or_solicitation` — boolean; if true, the §1026.60 tabular-disclosure read is required.
- `asset.is_mortgage_advertisement` — boolean; if true, the §1026.24(i) prohibition read and the FHA §3604(c) read are required.
- `asset.cra_relevant` — boolean; if true, the CRA assessment-area read is added.
- `asset.sponsor_bank_program` — boolean; if true, joint-attribution analysis applies.

#### Common pitfalls in banking marketing-review memos

- Reading the deposit-asset disclosure on desktop and missing the mobile-layout drift on the trigger-term disclosure; the clear-and-conspicuous standard runs by device class.
- Treating the FDIC official advertising statement as a logo footer requirement only and missing the misrepresentation analysis under §328.5 for fintech-attribution patterns.
- Reading the §1026.24(i) mortgage prohibitions as a stylistic guideline rather than as enforceable prohibitions.
- Treating a card-marketing asset as below the §1026.60 application or solicitation threshold without testing the channel-specific application and solicitation tests.
- Reading mortgage marketing distribution under FHA §3604(c) only after a complaint surfaces; distribution review is asset-level on every dwelling-related campaign.
- Sponsor-bank-program assets reviewed only by the program-operator's marketing-compliance function and not by the sponsor-bank's; the bank's UDAAP and advertising-rule exposure travels with the bank's name on the asset.
- TRID-adjacent rate-quote pages and pre-qualification screens reviewed as marketing only and missing the disclosure-mechanic question (whether a reasonable consumer might read the marketing as the operative TRID disclosure).
- CRA-relevant marketing claims reviewed for substantiation only and missing the assessment-area distribution read.

## capital-markets

### Capital markets sector overlay for marketing-claim-review

When the scope record names sector `capital-markets`, this overlay sets the scope boundary first. Most capital-markets marketing review sits in a different doctrinal lane (the SEC investment adviser Marketing Rule, Rule 206(4)-1; the FINRA communications-with-the-public framework, Rule 2210). This skill is the consumer-financial UDAAP / Reg Z lane and does not extend into those regimes. The overlay is short on purpose.

Loaded by: `marketing-claim-review/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type implicates a broker-dealer, investment adviser, private bank, or wealth-management entity that operates a retail consumer-facing credit, deposit-equivalent, or consumer-finance product surface.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Scope boundary first

The doctrinal lanes:

- *SEC investment adviser Marketing Rule.* Rule 206(4)-1 (in force from November 4, 2022 compliance date) sets advertising and solicitation requirements for SEC-registered investment advisers under the Advisers Act antifraud framework. The lane covers general prohibitions, performance presentation, testimonials and endorsements, third-party ratings, predecessor performance, and recordkeeping. The substantive standards differ from CFPB UDAAP and Regulation Z. Reviewer: the firm's investment-adviser compliance function.
- *FINRA Rule 2210.* Communications-with-the-public requirements for FINRA-member broker-dealers (categorisation as institutional, retail, correspondence, etc.; pre-use approval and principal sign-off; recordkeeping; content standards). The substantive standards differ from CFPB UDAAP and Regulation Z. Reviewer: the firm's broker-dealer compliance function.
- *SEC Regulation Best Interest (Reg BI).* Standard of conduct for broker-dealers when making recommendations to retail customers. Reaches sales-practice fairness and disclosure mechanics. Adjacent to UDAAP framing but the legal architecture differs.

This skill does not extend into those regimes. Where the scope implicates them, route to the firm's broker-dealer compliance, investment-adviser compliance, or wealth-management compliance function.

#### Where this skill does apply on the capital-markets side

Three narrow cases:

##### 1. Consumer-credit marketing by a capital-markets-affiliated entity

Where a capital-markets-affiliated entity (broker-dealer; private bank; wealth-management entity; bank holding company subsidiary) markets consumer credit (margin facilities offered to retail customers; securities-based lending to retail; wealth-credit products including jumbo mortgages, lines of credit secured by assets), the consumer-credit-side asset is in scope under this skill. The asset-level review reads:

- Regulation Z advertising rules per the credit product type (open-end vs. closed-end; HELOC if a wealth-credit product is structured as a HELOC).
- TRID-adjacent reading where the marketing previews mortgage terms.
- ECOA / Reg B §1002.4(b) discouragement read on the wealth-population marketing distribution.
- FHA §3604(c) read on dwelling-related wealth-credit advertising.

The wealth-population skew (high-net-worth and ultra-high-net-worth audiences) is not itself an ECOA finding; the substantive read is whether the marketing distribution or content discourages on a prohibited basis.

##### 2. Cash-management and sweep-program marketing

Brokerage cash-management features and sweep programs (automated sweeps to bank-affiliated deposit accounts; rate spreads on the sweep rate vs. the prevailing market rate) are marketed alongside the brokerage account. The asset-level review reads:

- The sweep-rate disclosure and the rate-spread mechanic.
- The FDIC insurance representation under the FDIC advertising rule (load the banking sector overlay alongside) where the sweep is into a bank-affiliated insured depository.
- The deception read on the sweep-rate framing (whether a reasonable consumer would understand the rate-spread mechanic and the alternative cash-management options).

The sweep-program marketing review can also implicate the SEC and broker-dealer disclosure framework on a parallel track; this skill carries the consumer-finance side, the broker-dealer compliance function carries the SEC side.

##### 3. Bundled consumer-credit-and-investment marketing

Where the marketing surface bundles a consumer-credit product (margin; SBL; wealth-credit) with an investment-product representation (advisory recommendation; brokerage account; managed-portfolio offering), the consumer-credit-side asset is in scope and the investment-side asset routes to the firm's investment-adviser or broker-dealer compliance function. Where the bundling representation obscures the boundary, the deception analysis on the credit-side representation is in scope.

#### What does not extend into this skill

- Performance advertising of investment-adviser and broker-dealer products. Routes to the SEC Marketing Rule and FINRA Rule 2210 review function.
- Testimonial and endorsement compliance under the SEC Marketing Rule. Routes to the investment-adviser compliance function.
- Third-party rating use in adviser advertising. Routes to the investment-adviser compliance function.
- FINRA Rule 2210 categorisation, approval, recordkeeping, and content-standard review. Routes to the broker-dealer compliance function.
- Reg BI disclosure-mechanic review. Routes to the broker-dealer compliance function with a consumer-protection cross-read where the underlying product is a consumer-financial-product-or-service.

The skill does not resize into an SEC Marketing Rule or FINRA Rule 2210 review. Reviewers asked to do that work should route to the relevant compliance function; the boundary skill in `marketing-rule-evidence` is the closer-fit surface inside this repo for the SEC Marketing Rule lane.

#### Capital-markets-specific memo template additions

The fields are minimal because the overlay is mostly a scope boundary:

- `asset.product_perimeter_capital_markets[]` — enum list (`securities-based-lending`, `retail-margin`, `wealth-mortgage`, `wealth-line-of-credit`, `brokerage-cash-management-sweep`, `bundled-credit-and-investment`).
- `asset.cfpb_authority_plausible` — boolean; explicit flag to record whether the CFPB UDAAP / Reg Z perimeter reaches the in-scope asset.
- `asset.parallel_sec_or_finra_framework[]` — list of overlapping frameworks (`SEC-Marketing-Rule-206(4)-1`, `FINRA-Rule-2210`, `Reg-BI`).
- `out_of_scope_routing[]` — list of compliance functions the asset routes to where it is out of scope (investment-adviser compliance; broker-dealer compliance; wealth-management compliance).

#### Common pitfalls when capital-markets is flagged

- Building a marketing-claim-review memo for an investment-adviser performance advertisement; the regime is wrong. Route to the SEC Marketing Rule review function.
- Treating wealth-credit marketing as out-of-scope because the audience is high-net-worth; the consumer-credit-side asset is in scope under Regulation Z and ECOA / Reg B regardless of audience sophistication.
- Sweep-program marketing reviewed under the SEC disclosure framework only and missing the consumer-finance-side read where the sweep is into a bank-affiliated insured depository (FDIC advertising rule applies).
- Bundled consumer-credit-and-investment marketing reviewed under one regime only; the bundling-representation analysis runs across regimes and the boundary needs to be made explicit on the asset.
- Routing margin or SBL marketing to the broker-dealer compliance function only and missing the consumer-finance read; both are in play.
- Reading the SEC Marketing Rule and Reg Z advertising rules as substitutes; they are doctrinally distinct (antifraud lane vs. consumer-protection lane) and both can apply to the same asset on different theories.

## insurance

### Insurance sector overlay for marketing-claim-review

When the scope record names sector `insurance`, this overlay sets the scope boundary first. Insurance advertising review sits with state insurance departments under the NAIC Unfair Trade Practices Act framework (Model #880) and the NAIC advertising-content model regulations (Model #570 for life and annuities; Model #40 for accident and sickness; comparable models for other lines). This skill is the consumer-financial UDAAP / Reg Z lane and does not extend into insurance advertising as such. The overlay is short on purpose.

Loaded by: `marketing-claim-review/SKILL.md` when `scope.sector_overlay_set` includes `insurance`, or when the institution type implicates a life, health, or property-and-casualty insurer.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Scope boundary first

Insurance advertising vocabulary differs from CFPB UDAAP. The state-DOI framework addresses misleading advertising of insurance products under the NAIC Advertisements of Life Insurance and Annuities Model Regulation (Model #570), the NAIC Advertisements of Accident and Sickness Insurance Model Regulation (Model #40), and the broader NAIC Unfair Trade Practices Act framework (Model #880). The substantive standards differ from §1031 element tests. Reviewer: the firm's insurance-conduct or market-conduct review program; state-DOI examiners on examination.

For most insurance advertising review work, route to:

- The firm's insurance-conduct or market-conduct review program.
- State-DOI advertising-review and unfair-trade-practice statutes.
- The NAIC model regulations as the operational baseline.
- The NAIC Market Regulation Handbook for the broader market-conduct surface.
- Where AI / ML is used in advertising or audience targeting, the NAIC AI Model Bulletin (December 2023) and any state-specific AI / advertising guidance.

This skill does not extend into those regimes.

#### Where this skill does apply on the insurance side

Two narrow cases:

##### 1. Bank-affiliated credit-protection insurance bundled with credit

Where the bank or non-bank credit provider markets credit-protection insurance (credit life; debt-cancellation; GAP; VSC bundled with auto-loan) bundled with the underlying credit product (mortgage, card, personal loan, auto loan), the credit-side marketing representation is in scope under this skill. The asset-level review reads:

- The bundling representation against the cost-of-credit framing (whether the consumer can read the asset and understand that the insurance fee is a separate cost).
- The Regulation Z disclosure mechanics on the credit-side (open-end vs. closed-end advertising rules per the underlying credit product).
- The deception read on the bundled-product representation.

The insurance-side advertising (eligibility, pricing of the insurance product itself, claims handling representations) routes to the insurance-conduct framework and is out of scope here.

##### 2. Marketing surface that distributes both credit and insurance products

Where the firm operates a marketing surface that distributes both credit and insurance products to overlapping audiences, the marketing of the credit product is in scope. The marketing of the insurance product routes to the insurance-conduct framework. Where the marketing copy obscures the boundary (bundles credit and insurance in a single representation; suggests an insurance product is part of the credit offering when it is separate), the deception analysis on the credit-side representation is in scope.

#### What does not extend into this skill

- Life-insurance and annuity advertising as such. NAIC Model #570 and state-DOI implementing regulations apply.
- Accident-and-health insurance advertising. NAIC Model #40 and state-DOI implementing regulations apply.
- P&C insurance advertising. State-DOI advertising-review statutes apply; NAIC has additional model regulations for specific lines.
- Insurance underwriting and pricing representations in advertising. State-DOI unfair-discrimination statutes apply.
- Insurance claims-handling representations in advertising. NAIC Unfair Trade Practices Act framework and state-DOI bad-faith-claims-handling framework apply.
- AI use in insurance advertising and audience targeting. NAIC AI Model Bulletin and state-specific guidance (NYDFS Insurance Circular Letter on AI; CO regulation under SB 21-169 for life insurance) apply.

The skill does not resize into an insurance advertising review. Reviewers asked to do insurance advertising work should route to the firm's insurance-conduct function and the state-DOI framework; this plugin's six skills do not currently cover insurance advertising as a primary surface.

#### Insurance-specific memo template additions

The fields are minimal because the overlay is mostly a scope boundary:

- `asset.bundled_credit_protection_insurance` — boolean; if true, the credit-side bundling-representation review is the in-scope asset; insurance-side advertising is explicitly out of scope.
- `asset.credit_and_insurance_marketing_surface` — boolean; if true, the marketing-side review on the credit product is in scope; insurance-product marketing routes separately.
- `out_of_scope_routing[]` — list of insurance-conduct frameworks the asset routes to (NAIC Model #570 for life and annuity advertising; NAIC Model #40 for accident-and-sickness advertising; NAIC Model #880 for unfair trade practices; state-DOI advertising-review statutes; NAIC Market Regulation Handbook; NAIC AI Model Bulletin where AI is in path).

#### Common pitfalls when insurance is flagged

- Building a marketing-claim-review memo for a life-insurance advertising asset; the regime is wrong. Route to the insurance-conduct framework.
- Treating the bundling representation as an insurance-side issue; the credit-side representation on the bundled-product framing is in scope under UDAAP and Regulation Z.
- Reading the NAIC AI Model Bulletin as a UDAAP-equivalent obligation; the bulletin sets governance and AIS-program expectations, not Dodd-Frank §1031 element-test expectations.
- Reading bundled-credit-protection-insurance marketing without separating the credit-side review (in scope here) from the insurance-side review (out of scope, route separately).
- Extending the §1031 element analysis into life-or-health-insurance underwriting representations in advertising; the substantive standards differ.
- Treating bad-faith-claims-handling representations as UDAAP marketing findings; the regime is state common-law and statutory, not CFPB UDAAP.

## payments-fintech

### Payments and fintech sector overlay for marketing-claim-review

When the scope record names sector `payments-fintech`, this overlay adds payments- and fintech-specific marketing fact patterns, sponsor-bank attribution mechanics, and influencer / creator-economy review framing to the asset-level marketing review. Where there is conflict between the capability defaults and this overlay, the overlay governs the sector elements.

Loaded by: `marketing-claim-review/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a fintech consumer-credit platform, sponsor-bank-program operator, BNPL provider, prepaid issuer, P2P or instant-payment platform, neobank, or non-bank consumer-finance entity.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for payments and fintech marketing-review memos

Most fintech consumer-finance marketing runs through digital channels (search, paid social, lookalike audiences, partner marketplaces, embedded-finance partner surfaces, app-store assets, creator and influencer placements). The fact-pattern catalogue is different from banking; the legal framework spans CFPB UDAAP, FTC Act §5, the FTC Endorsement Guides, and the operative Reg Z and Reg E provisions where the underlying product is credit or an electronic fund transfer.

##### 1. Sponsor-bank attribution

Most fintech consumer-credit and many fintech deposit-equivalent products operate through a sponsor-bank arrangement. Marketing assets implicate both the program operator and the sponsor bank. The asset-level review records:

- Which legal entity holds the consumer-facing relationship.
- Whether the asset bears the sponsor bank's name or logo.
- Whether a reasonable consumer would attribute the asset to the sponsor bank.
- Joint review and joint approval framing where the asset crosses both entities.
- The interagency third-party guidance (June 2023) anchors the bank-side accountability; the program operator is not the sole accountable party.

Where the asset is for a deposit-equivalent product (consumer-facing surface where a reasonable consumer might infer FDIC insurance), the FDIC §328.5 fintech-attribution analysis applies (load the banking sector overlay alongside).

##### 2. BNPL marketing themes

For BNPL assets, the asset-level review reads:

- "No interest" representations against the late-fee, returned-payment-fee, and cost-of-credit reality.
- Cost-of-credit framing against the underlying Reg Z framework as applied to the BNPL product structure (the May 2024 CFPB BNPL Interpretive Rule was **nullified by Pub. L. 119-11 (May 9, 2025); historical only.** Reg Z applicability now turns on the product structure under the regulatory text rather than the nullified interpretive rule).
- Autopay and default-payment-method representations.
- Multi-merchant payment-allocation logic where the asset implies a single-payment cadence but the underlying product allocates across merchants.
- Dispute-handling representations against the operative dispute-mechanics framework.

##### 3. "Instant funding" and tip-mechanic marketing

For earned-wage-access, small-dollar-credit, and personal-loan products that market instant-funding or tip mechanics, the asset-level review reads:

- Whether the marketed APR or cost framing includes the instant-funding fee.
- Whether tip mechanics are presented as voluntary while the underlying product structures the tip as the default cost-of-credit.
- The cross-reference to `udaap-risk-review` for the product-level UDAAP read on the funding-fee mechanic; the asset-level review handles the on-asset claim.

##### 4. P2P and instant-payment marketing

For P2P and instant-payment assets, the asset-level review reads:

- Speed-of-payment representations against the operational reality.
- Unauthorised-transfer dispute representations against the Reg E §1005.6 and §1005.11 framework; representations that overstate the consumer's recourse or that understate the firm's obligation are deception findings.
- Security claims against the firm's actual fraud-prevention posture.

##### 5. Influencer, creator, and endorsement marketing

For assets involving paid influencers, creators, brand-affiliate partners, or other endorsements, the FTC Endorsement Guides framework applies (16 CFR Part 255). The asset-level review reads:

- Whether material connections between the endorser and the firm are clearly and conspicuously disclosed.
- Whether the endorsement reflects the endorser's honest opinions, findings, beliefs, or experience.
- Whether the endorsement involves an AI-generated avatar, AI-generated testimonial, or other synthetic-content element [verify exact 2023 Endorsement Guides treatment of AI-generated endorsements].
- Channel-specific disclosure mechanics (the Endorsement Guides FAQs document platform-by-platform expectations).

The Endorsement Guides framework applies to FTC-jurisdictional entities directly; the framework is also a useful reference for bank-jurisdictional entities under the CFPB UDAAP and joint-statement framing on AI-generated content.

##### 6. App-store assets and marketing surfaces

App-store listings, app-store ad placements, and in-app marketing assets are in scope. The app-store-platform requirements (Apple App Store Review Guidelines; Google Play Developer Program Policies) supplement the regulatory framework; the asset-level review notes app-store-rule findings alongside the regulatory findings.

##### 7. Prepaid-account marketing under Regulation E §1005.18

For prepaid-account assets, the §1005.18 short-form and long-form disclosure mechanics intersect with the asset-level review. The asset-level review reads representations about fees, error-resolution, and credit features against the §1005.18 disclosure framework.

##### 8. Embedded-finance partner surfaces

Where the product is offered through an embedded-finance partner (e-commerce checkout; marketplace integration; super-app integration), the consumer-experience flow at the partner surface is part of the asset perimeter. The partner is a third party, but the program operator and the sponsor bank retain accountability for the consumer-facing claim under their respective duties. Cross-reference `udaap-risk-review` where the embedded-finance flow raises a product-level UDAAP angle.

##### 9. State licensure and state-AG enforcement

CFPB consumer-protection authority reaches non-bank consumer-credit and consumer-financial-services providers under Dodd-Frank Title X. State licensure (consumer-lender licences, money-transmission licences) brings state examiners; state AG offices have UDAP enforcement authority under state baby-FTC acts. The memo records:

- The state-licensure footprint and the strictest-applicable-state posture for any state with prescribed advertising-rule obligations beyond the federal baseline.
- Whether multi-state coordinated exams are likely on the in-scope marketing fact pattern.
- Whether state AG enforcement is a plausible exposure on the in-scope claim or distribution pattern.

##### 10. AI-personalisation and algorithmic-targeting themes

Fintech surfaces are typically AI-heavy: AI-rotated creative variants; AI-personalised landing-page headlines; lookalike-audience targeting; AI-driven communication scheduling; conversational AI in marketing surfaces. The AI-content review block in the memo (see SKILL.md AI overlay) carries the operational detail. The April 2023 Joint Statement is cited from `references/source-anchors.md` whenever algorithmic targeting or AI-content generation is in path.

##### 11. Evidence sources

Fintech marketing-review typically pulls evidence from:

- The marketing-asset library and the AI-creative variant store.
- The audience-definition exports from the ad-platform.
- The served-impression and click data with creative-variant attribution.
- The MAP record system (or equivalent advertising-review approval system).
- The substantiation file system for claims.
- The model-card library for AI-personalisation surfaces.
- The complaint-management-system records (CFPB-portal complaints; app-store review patterns; firm-direct complaints; social-signal patterns).
- The sponsor-bank's marketing-review monitoring outputs (where joint).

#### Payments and fintech-specific memo template additions

The following fields are added to the per-asset block:

- `asset.legal_entity_type` — enum (`fintech-program-operator`, `sponsor-bank-program`, `non-bank-consumer-finance`, `BNPL`, `P2P-or-instant-payment`, `prepaid-issuer`, `embedded-finance-partner`, `other`).
- `asset.sponsor_bank_program` — boolean; if true, joint-attribution analysis applies.
- `asset.endorsement_in_use` — boolean; if true, the FTC Endorsement Guides read is required.
- `asset.influencer_or_creator_attribution[]` — list of named endorsement arrangements.
- `asset.app_store_surface` — boolean; if true, the app-store-platform requirements are surfaced alongside the regulatory findings.
- `asset.embedded_finance_partner_surface` — boolean; if true, the partner-surface review is included.
- `asset.ai_creative_variants_in_play` — boolean; if true, the per-variant substantiation discipline applies.
- `state_licensure_footprint[]` — list of states with consumer-lender or money-transmission licences relevant to the in-scope asset distribution.

#### Common pitfalls in payments and fintech marketing-review memos

- Assuming the fintech is the sole accountable party when the sponsor bank's name or logo is on the asset; the bank inherits asset-level review duty.
- BNPL marketing reviewed under generic deceptive-marketing framing without anchoring to the underlying Reg Z framework as applied to the product structure (the May 2024 CFPB BNPL Interpretive Rule was **nullified by Pub. L. 119-11 (May 9, 2025); historical only.**).
- "Instant funding" and tip-mechanic marketing reviewed for substantiation only and missing the cost-of-credit framing on the asset.
- Influencer and creator endorsements reviewed against firm-policy material-connection disclosure only and missing the channel-specific FTC Endorsement Guides expectations.
- AI-generated avatars or AI-generated testimonials reviewed as marketing creative without the synthetic-content disclosure analysis.
- App-store assets reviewed against app-store-platform rules only and missing the regulatory framework.
- Lookalike-audience targeting treated as out-of-scope because "the audience is just marketing"; the bureau and the FTC have both pursued algorithmic-targeting fact patterns; the audience-definition exports are part of the evidence base.
- AI-rotated creative variants reviewed against the brief only and not against the served variants; substantiation per served variant is the discipline.
- Embedded-finance partner surfaces treated as the partner's responsibility; the program operator and the sponsor bank retain accountability for the consumer-facing claim.
- State-AG enforcement angle missed because the memo focuses on CFPB authority only; many of the highest-profile fintech marketing-related actions have been state AG actions under state baby-FTC acts.
