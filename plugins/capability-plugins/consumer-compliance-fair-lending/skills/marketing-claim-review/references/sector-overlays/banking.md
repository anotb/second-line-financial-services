# Banking sector overlay for marketing-claim-review

When the engagement-scope record names sector `banking`, this overlay adds banking-specific disclosure rules, FDIC-attribution mechanics, and recurring fact patterns to the asset-level marketing review. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `marketing-claim-review/SKILL.md` when `engagement_scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for banking marketing-review memos

Banking is one of the heaviest overlays on this skill. Most consumer-financial advertising rules and the FDIC-attribution framework are banking-specific.

### 1. Deposit-account advertising under Regulation DD

For deposit-account assets (checking, savings, MMA, time deposit), the operative rule is the truth-in-savings advertising rule. The asset-level review reads:

- The clear-and-conspicuous standard on the rate or APY representation.
- Trigger-term mechanics (a bonus; the APY; the term of a time account; certain other elements) requiring the additional disclosures.
- Bonus disclosure requirements where the asset markets a deposit-opening bonus.
- The exemption framework where the asset is a brief broadcast or other low-information surface.

Where the deposit asset omits a triggered disclosure (the recurring failure mode is mobile-vs-desktop layout drift), the memo records the finding and the recommended remediation by device class.

### 2. FDIC insurance representation under 12 CFR Part 328

For any asset that promotes a deposit product or that operates on a consumer-facing surface where a reasonable consumer might infer FDIC insurance, the FDIC advertising rule applies. The asset-level review reads:

- The official advertising statement requirement on insured-depository-promoting advertisements.
- Misrepresentation analysis where a non-bank entity (or a bank-affiliated non-deposit product) might be read as FDIC-insured.
- The 2022 final rule on §328.5 and its application to fintech-attribution patterns (sponsor-bank sweep programs; cash-management surfaces; non-bank fintech surfaces partnered with insured depositories).

The memo names the fintech-attribution analysis where the asset operates on a sponsor-bank or BaaS-style surface; the failure mode is fintech surfaces that lead a reasonable consumer to believe a non-deposit product is FDIC-insured, or that misrepresent the scope of FDIC insurance coverage on sweep-style products.

### 3. Mortgage advertising under TILA / RESPA / TRID

For mortgage assets (purchase-money mortgage; refinance; HELOC; home-equity loan; reverse mortgage), the operative framework spans Regulation Z closed-end advertising rules (with the §1026.24(i) mortgage-specific prohibitions), the HELOC advertising rule for HELOCs, and the TRID-adjacent disclosure mechanics where the asset previews mortgage terms. The asset-level review reads:

- §1026.24(i) prohibitions: misleading payment claims; misleading comparisons; misuse of "government" terms; misleading use of the current lender's name; misleading claims of debt elimination; misleading use of "counselor"; foreign-language disclosures (the asset must disclose in the same language as the advertisement).
- HELOC-specific advertising rule additions for HELOC assets.
- TRID-adjacent reading on rate-quote pages, pre-qualification screens, monthly-payment calculators where the marketing previews mortgage terms; the marketing review does not draft the Loan Estimate but reads whether the marketing leads a reasonable consumer to believe the marketing preview is the disclosure.
- FHA §3604(c) discriminatory-advertising read on mortgage marketing distribution and content (the dwelling-related advertising prohibition is operative).

### 4. CRA-related advertising

For assets in CRA-relevant marketing (community development products; LMI-targeted credit products; small-business products in CRA assessment areas), the asset-level review notes whether the marketing distribution is consistent with the bank's CRA assessment-area framework and whether the marketing content claims about LMI focus or community-development orientation are substantiated. CRA examination procedures read marketing distribution as one input to the assessment-area analysis; the asset-level review surfaces the relevant facts without performing the CRA assessment.

### 5. Card application and solicitation under §1026.60

For card-account assets (credit card; charge card) that constitute applications or solicitations under Regulation Z, the §1026.60 tabular-disclosure framework (the "Schumer box") applies. The asset-level review reads:

- Whether the asset is an application or solicitation under §1026.60 (channel-specific tests for direct-mail, electronic, telephone, in-person, publicly-available).
- The §1026.60(b) tabular disclosure presence and accuracy.
- The channel-specific additional rules.

The Schumer-box requirements are detailed and are the most-frequent enforcement target for card-marketing review.

### 6. Sponsor-bank attribution where the bank operates a fintech program

Where the bank is the sponsor for a fintech consumer-finance program, marketing assets bearing the program's brand may also implicate the bank's UDAAP and advertising-rule duties. The interagency third-party guidance (June 2023) anchors the bank-side accountability. The memo records:

- Whether the asset bears the bank's name or logo.
- Whether a reasonable consumer would attribute the asset to the bank.
- The bank-side review obligation and the fintech-side review obligation under the program agreement.

### 7. Bank-specific evidence sources

Banking marketing-review typically pulls evidence from:

- The marketing-asset library (versioned, by channel, by audience).
- The MAP record system (advertising-review approvals; substantiation files; sign-off audit trail).
- The CRA management system for CRA-relevant marketing.
- The deposit-product fee schedule and Reg DD §1030.4 truth-in-savings disclosures (for the deposit-asset cross-reference).
- The Schumer-box source-of-truth system for card-application substantiation.
- The complaint-management-system records (CFPB-portal complaints filtered by "advertising" or "disclosure" themes; firm-direct complaints).

The memo names the evidence sources used and flags the sources that would be needed but are not yet available.

## Banking-specific memo template additions

The following fields are added to the per-asset block:

- `asset.product_type` — enum (`deposit-checking`, `deposit-savings`, `deposit-mma`, `deposit-time`, `card-credit`, `card-charge`, `mortgage-purchase`, `mortgage-refi`, `heloc`, `home-equity-loan`, `reverse-mortgage`, `auto`, `personal-loan`, `small-business`, `other`).
- `asset.fdic_attribution_in_play` — boolean; if true, the §328.4/§328.5 read is required.
- `asset.is_card_application_or_solicitation` — boolean; if true, the §1026.60 tabular-disclosure read is required.
- `asset.is_mortgage_advertisement` — boolean; if true, the §1026.24(i) prohibition read and the FHA §3604(c) read are required.
- `asset.cra_relevant` — boolean; if true, the CRA assessment-area read is added.
- `asset.sponsor_bank_program` — boolean; if true, joint-attribution analysis applies.

## Common pitfalls in banking marketing-review memos

- Reading the deposit-asset disclosure on desktop and missing the mobile-layout drift on the trigger-term disclosure; the clear-and-conspicuous standard runs by device class.
- Treating the FDIC official advertising statement as a logo footer requirement only and missing the misrepresentation analysis under §328.5 for fintech-attribution patterns.
- Reading the §1026.24(i) mortgage prohibitions as a stylistic guideline rather than as enforceable prohibitions.
- Treating a card-marketing asset as below the §1026.60 application or solicitation threshold without testing the channel-specific application and solicitation tests.
- Reading mortgage marketing distribution under FHA §3604(c) only after a complaint surfaces; distribution review is asset-level on every dwelling-related campaign.
- Sponsor-bank-program assets reviewed only by the program-operator's marketing-compliance function and not by the sponsor-bank's; the bank's UDAAP and advertising-rule exposure travels with the bank's name on the asset.
- TRID-adjacent rate-quote pages and pre-qualification screens reviewed as marketing only and missing the disclosure-mechanic question (whether a reasonable consumer might read the marketing as the operative TRID disclosure).
- CRA-relevant marketing claims reviewed for substantiation only and missing the assessment-area distribution read.
