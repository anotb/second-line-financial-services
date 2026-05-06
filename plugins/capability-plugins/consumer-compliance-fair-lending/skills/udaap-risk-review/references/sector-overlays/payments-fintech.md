# Payments and fintech sector overlay for udaap-risk-review

When the engagement-scope record names sector `payments-fintech`, this overlay adds payments- and fintech-specific fact patterns, evidence sources, and accountability framing to the UDAAP memo. Where there is conflict between the capability defaults and this overlay, the overlay governs the sector elements.

Loaded by: `udaap-risk-review/SKILL.md` when `engagement_scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a fintech consumer-credit platform, sponsor-bank-program operator, BNPL provider, prepaid issuer, P2P or instant-payment platform, neobank, or non-bank consumer-finance entity.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for payments and fintech UDAAP review memos

CFPB UDAAP authority under Dodd-Frank Title X reaches non-bank consumer-credit and consumer-financial-services providers. The fact-pattern catalogue is different from banking but the legal framework is the same; the overlay names the structural details that change.

### 1. Sponsor-bank attribution and joint accountability

Most fintech consumer-credit and many fintech deposit-equivalent products operate through a sponsor-bank arrangement. The UDAAP duty allocates per the program agreement and per the sponsor bank's consumer-compliance program. The memo records:

- Which legal entity holds the consumer-facing legal relationship.
- Which entity owns the product design, the marketing surface, and the fee architecture.
- Which second-line function reviews the in-scope fact pattern.
- Which committee approves remediation (sponsor-bank consumer-compliance committee; sometimes joint with the fintech AI risk committee or product committee).

The interagency third-party guidance (June 2023) anchors the bank-side accountability; the program operator is not the sole accountable party even where the operator built and operates the product.

### 2. Recurring fintech and payments UDAAP themes

A non-exhaustive list of fact patterns:

- *"Instant funding" fee mechanics.* Personal-loan and earned-wage-access products that offer instant funding for an additional fee or "tip", with the fee disclosed at the funding-selection step rather than at application; the APR shown at application does not include the funding fee. Element analysis: deception (the application-page APR misleads if funding fee is excluded); unfairness (consumer commitment is high at the funding-selection step, reasonable-avoidability turns on the slow-funding alternative being symmetric in the UI).
- *Tip and donation mechanics.* Earned-wage-access and small-dollar-credit products that present "tips" or "donations" as voluntary while structuring the consumer-journey to make the tip the default state; the cost of the financial product is communicated through a tip mechanic. Element analysis: abusiveness (material interference with the consumer's ability to understand the actual cost); deception where the "voluntary" framing misleads.
- *Subscription and negative-option mechanics.* Products with auto-renewal, recurring fees, or continuation by default; cancellation friction; opt-out asymmetry. Element analysis: unfairness (substantial injury, not reasonably avoidable through the cancellation friction); abusiveness (material interference with the cancellation flow).
- *BNPL UDAAP themes.* Late fees, returned-payment fees, dispute-resolution conduct, autopay-default mechanics, multi-merchant payment-allocation logic, the consumer's understanding of the credit nature of the product. Element analysis spans deception (marketing of "no interest" without the fee context), unfairness (fee mechanics on missed payments), and abusiveness (cancellation and dispute friction). The bureau's BNPL interpretive rule (May 2024) [verify exact title and date] affirms BNPL is credit under TILA / Reg Z and the consumer-protection framework reaches it.
- *P2P and instant-payment unauthorised-transfer conduct.* Unauthorised-transfer dispute handling on P2P platforms (Zelle-style and stand-alone P2P apps) under Reg E §1005.6 and §1005.11; refusal to credit or delayed credit on disputed transfers; deceptive representations during the dispute process. Element analysis: deception on the dispute communications; unfairness on the substantial injury and the reasonable-avoidability of the unauthorised transfer.
- *Algorithmic personalisation themes.* Personalised pricing, retention offers, AI-driven communication, lookalike-audience marketing. Element analysis ties to the AI / algorithmic-discrimination block in the main flow; the bureau's posture under the April 2023 Joint Statement is that existing UDAAP authority reaches algorithmic outcomes.
- *Crypto-adjacent consumer-finance products.* Where in scope, the same UDAAP framework applies; the bureau and the FTC have pursued fact patterns on the disclosure, custody, and recovery-of-funds mechanics. Confirm jurisdictional posture (CFPB; FTC; SEC where the product crosses into securities) before applying.
- *Fee-stacking on small-dollar credit.* Daily-fee, rollover, and reactivation mechanics on small-dollar products; the consumer's path to repayment without additional fees.
- *Account-closure and recovery friction.* Friction on closing fintech-program deposit-equivalent accounts; recovery-of-funds friction after account closure; the consumer's path to dispute or escalate.

### 3. State licensure and CFPB authority

CFPB consumer-protection authority reaches non-bank consumer-credit and consumer-financial-services providers under Dodd-Frank Title X. State licensure (consumer-lender licences, money-transmission licences) brings state examiners; multi-state CSBS-coordinated exams may apply. State AG offices have UDAP enforcement authority under state baby-FTC acts. The memo records:

- The state-licensure footprint and the strictest-applicable-state posture for any state with prescribed UDAAP-equivalent obligations beyond the federal baseline.
- Whether multi-state coordinated exams are likely on the in-scope fact pattern.
- Whether state AG enforcement is a plausible exposure (driven by state-AG focal items, peer state-AG actions, and the consumer-harm geography).

### 4. Marketing-funnel UDAAP angles

Fintech consumer-finance acquisition typically runs through digital channels (search, social, lookalike audiences, partner marketplaces, embedded-finance partner surfaces). UDAAP review reaches the marketing surface:

- *Pre-screen and lookalike-audience targeting.* Where the lookalike-audience model concentrates marketing on segments unlikely to qualify or unable to use the product, the UDAAP analysis on the substantial injury and reasonable-avoidability prongs may apply.
- *Embedded-finance surfaces.* Where the in-scope product is offered through an embedded-finance partner (e-commerce checkout, marketplace integration), the consumer-experience flow at the partner surface is part of the UDAAP perimeter; the partner is a third party but the program operator and the sponsor bank retain accountability.
- *Cross-reference `marketing-claim-review`* for asset-level marketing-claim review; this skill addresses UDAAP at the product-flow level, the marketing-claim-review skill addresses the asset-level claim.

### 5. AI / algorithmic-surface review

Fintech surfaces are typically AI-heavy: personalisation, dynamic pricing, conversational AI, agentic flows, AI-generated communication. The AI-block in the memo names each in-scope AI surface and the UDAAP angle. The bureau has been explicit that existing UDAAP authority reaches algorithmic outcomes (April 2023 Joint Statement; CFPB Circulars 2022-03 and 2023-03 on adverse action and complex models).

### 6. Evidence sources

Fintech UDAAP review typically pulls evidence from:

- The application platform and the consumer-journey logging.
- The fee-assessment logs (transaction-level).
- The marketing platform exports (audience definition, served-impression and click data).
- The customer-support ticketing system and the call-center recordings.
- The complaint-management system (CFPB-portal complaints; app-store review patterns; firm-direct complaints; social-signal patterns).
- The model-platform feature store and the model-card library for AI surfaces in path.
- The sponsor-bank's compliance-monitoring outputs (where joint).

### 7. Reg E and Reg Z framework intersections

For payments products, Reg E §1005 (unauthorised transfers, error resolution) and Reg Z §1026 (credit) are the operational baselines; UDAAP reaches conduct that complies with the literal regulatory requirements but misleads or harms in context. The memo names the operative Reg E or Reg Z provision and the UDAAP angle alongside it; the memo does not duplicate the Reg E or Reg Z compliance review.

## Payments and fintech-specific memo template additions

The following fields are added to the memo (mapped to schema where present):

- `scope.legal_entity_type` — enum (`fintech-program-operator`, `sponsor-bank-program`, `non-bank-consumer-finance`, `BNPL`, `P2P-or-instant-payment`, `prepaid-issuer`, `embedded-finance-partner`, `other`).
- `scope.sponsor_bank_program` — boolean; if true, sponsor-bank consumer-compliance officer named as joint reviewer.
- `scope.state_licensure_footprint[]` — list of states with consumer-lender or money-transmission licences.
- `recurring_fintech_themes[]` — list of themes from the recurring-themes catalogue above that the in-scope fact pattern matches.
- `marketing_funnel_in_scope` — boolean; if true, the marketing-funnel UDAAP review is in scope.
- `embedded_finance_partner_in_scope` — boolean; if true, the partner-surface consumer-experience flow is part of the UDAAP perimeter.
- `cross_reference_skills[]` — extends to include `marketing-claim-review`, `complaint-theme-analysis`, `vendor-diligence` where the fact pattern invokes those.

## Common pitfalls in payments and fintech UDAAP review memos

- Assuming the fintech is the sole accountable party when the sponsor bank inherits creditor-of-record duty; bank examiners catch this in third-party reviews and the bank's UDAAP exposure can be greater than the program operator's.
- Reading the Reg E §1005.11 error-resolution process as the entire UDAAP analysis on a P2P unauthorised-transfer fact pattern; UDAAP reaches the dispute communications and the substantial-injury analysis on the underlying unauthorised transfer.
- Treating BNPL as out of UDAAP scope on the assumption that BNPL is not credit; the bureau's interpretive posture and the underlying consumer-protection framework reach BNPL. Verify the operative status of the BNPL interpretive rule at memo date.
- "Tip" mechanics on earned-wage-access and small-dollar credit treated as outside the cost-of-credit framing; the bureau's UDAAP framing reaches the tip-as-cost mechanic and the consumer-journey design that makes the tip the default.
- Subscription-style fee mechanics reviewed for FTC Negative Option Rule compliance only and missing the abusiveness analysis on the cancellation friction; both regimes apply.
- Lookalike-audience targeting treated as out of UDAAP scope because the audience is "just marketing"; the bureau and the FTC have both pursued algorithmic-targeting fact patterns.
- AI-driven personalisation reviewed as a model-risk question only and missing the consumer-surface UDAAP angle; AI-block in the memo is mandatory.
- Embedded-finance partner surfaces treated as the partner's responsibility; the program operator and sponsor bank retain accountability for the consumer-experience flow at the partner surface.
- State AG enforcement angle missed because the memo focuses on CFPB authority only; many of the highest-profile fintech UDAAP-equivalent actions have been state AG actions under state baby-FTC acts.
