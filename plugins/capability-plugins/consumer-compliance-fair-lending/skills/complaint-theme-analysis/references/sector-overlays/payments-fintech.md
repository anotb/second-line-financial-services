# Payments and fintech sector overlay for complaint-theme-analysis

When the engagement-scope record names sector `payments-fintech`, this overlay adds payments-fintech-specific theme patterns, evidence sources, and attribution detail. Where there is conflict between the capability defaults and this overlay, the overlay governs the payments-fintech-sector elements.

Loaded by: `complaint-theme-analysis/SKILL.md` when `engagement_scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a fintech program operator, money services business, P2P provider, BNPL provider, neobank, or sponsor-bank-aligned consumer-finance fintech.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for payments-fintech complaint-theme analysis

Payments and fintech is the second-heaviest overlay on this skill. The complaint surfaces are different from banking: app-store reviews carry meaningful signal; the CFPB Complaint Database coverage is uneven across product types; the sponsor-bank-vs-fintech attribution question is non-trivial; the dispute-handling rhythm under Reg E is the recurring substantive theme.

### 1. Recurring payments-fintech complaint themes

A non-exhaustive theme catalogue:

- *P2P and instant-payment themes.* Reg E §1005.11 error-resolution themes (provisional-credit timing; investigation depth on unauthorised-transfer claims; final-resolution communication); fraud-and-scam themes (the consumer-authorised-the-transfer-but-was-deceived pattern; the §1005.6 unauthorised-EFT scope question); account-takeover themes; recipient-error themes (consumer sent to wrong recipient; reversal mechanics); customer-service-friction themes on disputes.
- *BNPL themes.* Disclosure themes (the four-payment plan vs. interest-bearing extension); late-fee and missed-payment themes; merchant-dispute themes (consumer dispute with merchant intersecting the BNPL repayment obligation); credit-reporting themes (whether and when BNPL repayment hits the consumer's credit file); collections themes; subscription-style and recurring-purchase themes on BNPL.
- *Neobank themes.* Account-closure and frozen-account themes (often AML-driven; consumer recourse unclear); funds-availability themes; deposit-of-government-benefit themes (often overlaps with prepaid framing); customer-service-channel themes (chat-only support friction; AI-agent escalation friction); dispute-handling themes.
- *Subscription, negative-option, and "instant-funding" themes.* Cancellation-friction themes (the dark-pattern intersection); auto-renewal themes; tip-as-fee themes (variable tipping presented as voluntary but functionally required); instant-funding fee themes (where a small fee is charged for "instant" delivery of funds the consumer is told are theirs); the FTC Negative Option Rule [verify operative status given litigation] intersection.
- *Sponsor-bank attribution themes.* Themes where complaints arrive at the fintech but the legal entity holding the consumer-facing relationship is the sponsor bank; themes where complaints arrive at the bank but the product, marketing, and fee design originate from the fintech program operator.
- *AI agent themes.* Conversational-AI complaint-handling themes (the agent did not understand; the agent gave incorrect information; the consumer could not reach a human); AI-generated-communication themes (the email or in-app message misled); AI-driven personalisation themes (the offer or rate the consumer received differs from peer experience).
- *App-store review themes specific to fintech.* Onboarding-friction themes; identity-verification themes; account-closure-without-notice themes; the dispute-process themes that surface in app-store reviews more often than in CFPB-portal complaints.

The memo names the in-scope themes; the analysis blocks address each theme separately where multiple are at the top of the period count.

### 2. App-store reviews as a non-CFPB complaint channel

App-store reviews on the fintech's mobile app are a meaningful complaint channel for payments-fintech. The CFPB Complaint Database does not aggregate app-store reviews; the firm's complaint-management system typically does not pull them either. The memo treats app-store reviews as a separate channel:

- Channel coverage: which app stores (iOS App Store, Google Play, third-party stores where applicable) and the period reviewed.
- Volume normalisation: app-store reviews skew negative (reviewers self-select); the memo treats the volume as signal but the share comparison against CFPB-portal complaints is read with the bias in mind.
- Categorical coding: app-store reviews are coded to the firm's theme taxonomy alongside the CFPB-portal and firm-direct complaints.
- Action chain: app-store review themes that match a CFPB-portal or firm-direct theme reinforce the signal; themes that appear in app-store reviews and not in the CFPB-portal channel are surfaced separately as "app-store-only" themes for a specific watch.

App-store reviews are a leading indicator on consumer-experience friction themes that often do not yet rise to a regulator-portal complaint.

### 3. Sponsor-bank attribution per theme

The attribution question is non-trivial because the regulator looks through to whichever entity is accountable for the conduct under the program agreement and the bank's third-party-risk framework. The memo records, per theme:

- Which legal entity holds the consumer-facing relationship (typically the sponsor bank for the deposit, card, or credit account; the fintech for the app and the customer-service surface).
- Which entity owns the product, marketing, and fee design that the theme traces to.
- Which entity owns the disclosure that the theme traces to.
- Which complaint surface received the complaint (sponsor bank's CFPB portal; fintech's complaint surface; both).
- Joint-review framing where the theme runs through both entities.

The memo cross-references `udaap-risk-review` or `marketing-claim-review` with the bank as the accountable party (per the interagency third-party guidance).

### 4. Reg E error resolution as the recurring substantive theme

P2P and instant-payment themes recurrently raise the Reg E §1005.11 error-resolution framework. The memo records, per relevant theme:

- The error-resolution timing posture (10-day provisional credit, 45-day final determination, 90-day final determination for new accounts and certain transaction types).
- The §1005.6 unauthorised-EFT scope question (the consumer-authorised-the-transfer-but-was-deceived fact pattern is the most-litigated boundary).
- The CFPB and FTC enforcement themes on P2P providers and the §1005.11 process.
- The fintech-vs-sponsor-bank duty allocation on dispute handling under the program agreement.

Where Reg E themes are in the population, the memo also names whether the §1005.11 process compliance check has been done by the firm's first-line; the theme analysis surfaces the substantive theme, but the procedural Reg E compliance check is the parallel inquiry.

### 5. Junk-fee theme intersection

Payments-fintech is the bureau's recent focal area on junk fees: tip-as-fee mechanics; instant-funding fee mechanics; subscription-style fee mechanics; representment NSF on linked deposit accounts. The memo treats junk-fee themes specifically, with the cross-skill chain into `udaap-risk-review` for the element-by-element analysis on the operative fee mechanic.

### 6. CFPB Complaint Database coverage and limits for payments-fintech

The CFPB Complaint Database covers some payments-fintech products well (prepaid cards, money transfers, virtual currency-adjacent services where they touch the bureau's perimeter) and others patchily (BNPL coverage has improved but is still partial; some neobank deposit complaints are routed to the sponsor bank in the database). The memo records the database-coverage caveat per theme:

- Whether the bureau's taxonomy has a dedicated product or sub-product code for the in-scope theme.
- Whether the firm's CFPB-portal subset is comprehensive on the theme or whether the firm's internal records carry the larger share.
- Whether app-store reviews and social signals materially supplement the CFPB-portal coverage on the theme.

### 7. AI-agent and AI-generated-communication themes

Payments-fintech is heavy on consumer-facing AI: conversational AI in customer service; AI-generated messaging and notifications; AI-driven personalisation in offers and rates; AI-driven dispute-decisioning. Themes that trace to these surfaces carry `ai_flag: true` and feed the cross-skill chain. The April 2023 Joint Statement is the cross-agency anchor; CFPB Circulars 2022-03 and 2023-03 apply where the AI surface generates AAN content or reason coding.

The dark-pattern frame is mandatory loaded for any AI-agent or AI-generated-communication theme; AI-mediated cancellation friction, AI-driven retention-offer urgency, and AI-personalised disclosure variability are recurring dark-pattern themes that the memo surfaces as such.

### 8. Payments-fintech-specific evidence sources

Payments-fintech complaint-theme analysis typically pulls evidence from:

- The firm's complaint-management system (in-app complaint flow; chat transcripts; CFPB-portal complaints).
- The CFPB Consumer Complaint Database extract (where coverage is operative for the product).
- App-store reviews on iOS and Google Play (with the bias caveat noted).
- Social-listening signals (Twitter/X, Reddit, consumer-advocacy forums) where the firm operates a social-monitoring program.
- The fintech's product analytics (denominator for rate analysis: active users; transaction count; new-account openings).
- Conversational-AI transcript logs (for AI-agent themes).
- Marketing-asset library (for themes traced to a campaign).
- Sponsor-bank's complaint surface and program-level disclosures (for joint-attribution themes).

## Payments-fintech theme matrix additions

Per theme:

- `app_store_review_count` — count of app-store reviews coded to this theme in the period (with channel breakdown).
- `cfpb_portal_count` — count of CFPB-portal complaints (where applicable).
- `firm_direct_count` — count of firm-direct complaints (in-app, chat, web form).
- `social_signal_count` — count of social-listening signals (where the firm operates social monitoring).
- `sponsor_bank_attribution` — `bank-of-record` / `fintech-of-record` / `joint` / `under-program-agreement-allocation`.
- `reg_e_intersection` — boolean; if true, the §1005.11 process compliance check is named alongside the substantive theme.
- `ai_surface_in_path` — boolean; the AI cross-skill chain.
- `dark_pattern_frame` — `friction-design` / `choice-architecture` / `urgency-scarcity` / `confirm-shaming` / other.

## Common pitfalls in payments-fintech complaint-theme analysis

- Excluding app-store reviews because they "are not complaints". For payments-fintech, app-store reviews are a leading-indicator complaint channel and the memo treats them as such.
- Treating the CFPB Complaint Database as the full complaint surface for BNPL or neobank deposits where the database coverage is uneven.
- Reading the consumer-authorised-the-transfer-but-was-deceived theme as outside Reg E without naming the §1005.6 unauthorised-EFT scope question; the question is contested and the memo carries the analytical posture.
- Treating sponsor-bank arrangements as the bank's UDAAP issue or as the fintech's UDAAP issue without naming the program-agreement allocation; both entities carry duty under the interagency guidance.
- Reading AI-agent themes as customer-service-quality themes only and missing the deception or unfairness angle on AI-generated communication content.
- Theming at the firm's product taxonomy without recognising the dark-pattern frame; the journey-design theme is a separate read on the same complaint population.
- Counting a theme by app-store review volume as if app-store volume mapped 1:1 to the firm's overall consumer base; the volume is signal, the rate is the denominator-adjusted measure.
- Missing the social-signal channel where the firm has a social-listening program; consumer-advocacy-forum threads on neobank account-closure themes are a recurring leading indicator.
