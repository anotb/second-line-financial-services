# Payments and fintech sector overlay for marketing-claim-review

When the scope record names sector `payments-fintech`, this overlay adds payments- and fintech-specific marketing fact patterns, sponsor-bank attribution mechanics, and influencer / creator-economy review framing to the asset-level marketing review. Where there is conflict between the capability defaults and this overlay, the overlay governs the sector elements.

Loaded by: `marketing-claim-review/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a fintech consumer-credit platform, sponsor-bank-program operator, BNPL provider, prepaid issuer, P2P or instant-payment platform, neobank, or non-bank consumer-finance entity.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for payments and fintech marketing-review memos

Most fintech consumer-finance marketing runs through digital channels (search, paid social, lookalike audiences, partner marketplaces, embedded-finance partner surfaces, app-store assets, creator and influencer placements). The fact-pattern catalogue is different from banking; the legal framework spans CFPB UDAAP, FTC Act §5, the FTC Endorsement Guides, and the operative Reg Z and Reg E provisions where the underlying product is credit or an electronic fund transfer.

### 1. Sponsor-bank attribution

Most fintech consumer-credit and many fintech deposit-equivalent products operate through a sponsor-bank arrangement. Marketing assets implicate both the program operator and the sponsor bank. The asset-level review records:

- Which legal entity holds the consumer-facing relationship.
- Whether the asset bears the sponsor bank's name or logo.
- Whether a reasonable consumer would attribute the asset to the sponsor bank.
- Joint review and joint approval framing where the asset crosses both entities.
- The interagency third-party guidance (June 2023) anchors the bank-side accountability; the program operator is not the sole accountable party.

Where the asset is for a deposit-equivalent product (consumer-facing surface where a reasonable consumer might infer FDIC insurance), the FDIC §328.5 fintech-attribution analysis applies (load the banking sector overlay alongside).

### 2. BNPL marketing themes

For BNPL assets, the asset-level review reads:

- "No interest" representations against the late-fee, returned-payment-fee, and cost-of-credit reality.
- Cost-of-credit framing against the underlying Reg Z framework as applied to the BNPL product structure (the May 2024 CFPB BNPL Interpretive Rule was **nullified by Pub. L. 119-11 (May 9, 2025); historical only.** Reg Z applicability now turns on the product structure under the regulatory text rather than the nullified interpretive rule).
- Autopay and default-payment-method representations.
- Multi-merchant payment-allocation logic where the asset implies a single-payment cadence but the underlying product allocates across merchants.
- Dispute-handling representations against the operative dispute-mechanics framework.

### 3. "Instant funding" and tip-mechanic marketing

For earned-wage-access, small-dollar-credit, and personal-loan products that market instant-funding or tip mechanics, the asset-level review reads:

- Whether the marketed APR or cost framing includes the instant-funding fee.
- Whether tip mechanics are presented as voluntary while the underlying product structures the tip as the default cost-of-credit.
- The cross-reference to `udaap-risk-review` for the product-level UDAAP read on the funding-fee mechanic; the asset-level review handles the on-asset claim.

### 4. P2P and instant-payment marketing

For P2P and instant-payment assets, the asset-level review reads:

- Speed-of-payment representations against the operational reality.
- Unauthorised-transfer dispute representations against the Reg E §1005.6 and §1005.11 framework; representations that overstate the consumer's recourse or that understate the firm's obligation are deception findings.
- Security claims against the firm's actual fraud-prevention posture.

### 5. Influencer, creator, and endorsement marketing

For assets involving paid influencers, creators, brand-affiliate partners, or other endorsements, the FTC Endorsement Guides framework applies (16 CFR Part 255). The asset-level review reads:

- Whether material connections between the endorser and the firm are clearly and conspicuously disclosed.
- Whether the endorsement reflects the endorser's honest opinions, findings, beliefs, or experience.
- Whether the endorsement involves an AI-generated avatar, AI-generated testimonial, or other synthetic-content element [verify exact 2023 Endorsement Guides treatment of AI-generated endorsements].
- Channel-specific disclosure mechanics (the Endorsement Guides FAQs document platform-by-platform expectations).

The Endorsement Guides framework applies to FTC-jurisdictional entities directly; the framework is also a useful reference for bank-jurisdictional entities under the CFPB UDAAP and joint-statement framing on AI-generated content.

### 6. App-store assets and marketing surfaces

App-store listings, app-store ad placements, and in-app marketing assets are in scope. The app-store-platform requirements (Apple App Store Review Guidelines; Google Play Developer Program Policies) supplement the regulatory framework; the asset-level review notes app-store-rule findings alongside the regulatory findings.

### 7. Prepaid-account marketing under Regulation E §1005.18

For prepaid-account assets, the §1005.18 short-form and long-form disclosure mechanics intersect with the asset-level review. The asset-level review reads representations about fees, error-resolution, and credit features against the §1005.18 disclosure framework.

### 8. Embedded-finance partner surfaces

Where the product is offered through an embedded-finance partner (e-commerce checkout; marketplace integration; super-app integration), the consumer-experience flow at the partner surface is part of the asset perimeter. The partner is a third party, but the program operator and the sponsor bank retain accountability for the consumer-facing claim under their respective duties. Cross-reference `udaap-risk-review` where the embedded-finance flow raises a product-level UDAAP angle.

### 9. State licensure and state-AG enforcement

CFPB consumer-protection authority reaches non-bank consumer-credit and consumer-financial-services providers under Dodd-Frank Title X. State licensure (consumer-lender licences, money-transmission licences) brings state examiners; state AG offices have UDAP enforcement authority under state baby-FTC acts. The memo records:

- The state-licensure footprint and the strictest-applicable-state posture for any state with prescribed advertising-rule obligations beyond the federal baseline.
- Whether multi-state coordinated exams are likely on the in-scope marketing fact pattern.
- Whether state AG enforcement is a plausible exposure on the in-scope claim or distribution pattern.

### 10. AI-personalisation and algorithmic-targeting themes

Fintech surfaces are typically AI-heavy: AI-rotated creative variants; AI-personalised landing-page headlines; lookalike-audience targeting; AI-driven communication scheduling; conversational AI in marketing surfaces. The AI-content review block in the memo (see SKILL.md AI overlay) carries the operational detail. The April 2023 Joint Statement is cited from `references/source-anchors.md` whenever algorithmic targeting or AI-content generation is in path.

### 11. Evidence sources

Fintech marketing-review typically pulls evidence from:

- The marketing-asset library and the AI-creative variant store.
- The audience-definition exports from the ad-platform.
- The served-impression and click data with creative-variant attribution.
- The MAP record system (or equivalent advertising-review approval system).
- The substantiation file system for claims.
- The model-card library for AI-personalisation surfaces.
- The complaint-management-system records (CFPB-portal complaints; app-store review patterns; firm-direct complaints; social-signal patterns).
- The sponsor-bank's marketing-review monitoring outputs (where joint).

## Payments and fintech-specific memo template additions

The following fields are added to the per-asset block:

- `asset.legal_entity_type` — enum (`fintech-program-operator`, `sponsor-bank-program`, `non-bank-consumer-finance`, `BNPL`, `P2P-or-instant-payment`, `prepaid-issuer`, `embedded-finance-partner`, `other`).
- `asset.sponsor_bank_program` — boolean; if true, joint-attribution analysis applies.
- `asset.endorsement_in_use` — boolean; if true, the FTC Endorsement Guides read is required.
- `asset.influencer_or_creator_attribution[]` — list of named endorsement arrangements.
- `asset.app_store_surface` — boolean; if true, the app-store-platform requirements are surfaced alongside the regulatory findings.
- `asset.embedded_finance_partner_surface` — boolean; if true, the partner-surface review is included.
- `asset.ai_creative_variants_in_play` — boolean; if true, the per-variant substantiation discipline applies.
- `state_licensure_footprint[]` — list of states with consumer-lender or money-transmission licences relevant to the in-scope asset distribution.

## Common pitfalls in payments and fintech marketing-review memos

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
