# Capital markets sector overlay for complaint-theme-analysis

When the scope record names sector `capital-markets`, this overlay flags the scope boundary, names the analogous regimes, and adapts the theme-analysis pattern for retail brokerage and adjacent activities. Most capital-markets activity sits outside the CFPB's jurisdiction; the theme-analysis method is reusable but the regulatory exposure mapping shifts.

Loaded by: `complaint-theme-analysis/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type implicates a registered broker-dealer, registered investment adviser, futures commission merchant, or capital-markets affiliate of a banking organization.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## Scope boundary first

Retail brokerage complaints are not CFPB-jurisdictional. The substantive complaint-handling regime for FINRA-member firms is FINRA Rule 4513 (Records of Written Customer Complaints) and FINRA Rule 4530 (Reporting Requirements). The customer-protection regime is Reg BI (Regulation Best Interest, 17 CFR §240.15l-1 for broker-dealers) and the IA fiduciary standard for investment advisers. The complaint-theme analysis method is reusable; the regulatory exposure mapping cites FINRA, SEC, and (for futures) NFA / CFTC sources rather than the CFPB authorities.

The overlay is named so reviewers do not over-extend the CFPB framing into capital-markets activity. It is also named so reviewers can run the same theme-analysis discipline (taxonomy, coding, trend, severity, root-cause hypothesis, recommended action) on retail-brokerage complaints under the FINRA framework.

## What the theme-analysis method looks like under the FINRA / SEC framework

### 1. Recurring retail-brokerage complaint themes

A non-exhaustive theme catalogue (FINRA Rule 4530 reportable categories overlap with these but are not identical):

- *Sales-practice themes.* Suitability themes (Reg BI care obligation; fact-pattern of recommendations not reasonably aligned to investment profile); concentration themes; high-cost-product themes; rollover themes (the IRA rollover decision and Reg BI care); annuity themes (fact-pattern of complex products sold to retail-eligible-but-unsophisticated investors); private placement and Reg D themes.
- *Account-handling themes.* Unauthorised trading themes; fee-disclosure themes (advisory fee, ticket charges, market-data fees, custody fees); margin-call themes (the consumer-experience friction and the disclosure of margin mechanics); securities-based lending themes (the credit-side intersection where retail clients use SBL).
- *Best-execution and order-handling themes.* Execution-quality complaints; payment-for-order-flow disclosure complaints; the Reg NMS-adjacent fact patterns.
- *Communication themes.* Marketing communication themes (Rule 2210 retail communication content); social-media-generated themes; AI-generated-research themes (the bot-generated commentary surfaces).
- *Account-opening and KYC themes.* Onboarding-friction themes; Reg S-K and Reg S-P privacy intersection on data collection; identity-verification themes.
- *Cybersecurity-incident-related themes.* Where account-takeover or unauthorised activity arises from an incident, the complaint surface intersects the Reg S-P safeguards rule and the firm's incident-disclosure conduct.
- *Customer-experience themes on the brokerage app.* (Same app-store-review pattern as payments-fintech; recurring themes are platform-friction, glitch-during-volatility, hold-on-deposit, settlement-confusion.)

### 2. FINRA Rule 4513 / 4530 framing

FINRA Rule 4513 requires member firms to make and keep written customer complaints; FINRA Rule 4530(d) requires reporting of statistical and summary information about written customer complaints quarterly to FINRA. The memo records, per top theme:

- Whether the theme has been reported under Rule 4530(d) statistical reporting.
- Whether the firm's Rule 4513 retention is current.
- Whether the underlying conduct is also reportable under Rule 4530(a) or (b) (specific events, including written customer complaints alleging theft, misappropriation, or forgery).

The complaint-theme analysis surfaces the substantive theme; the FINRA reporting compliance is the parallel inquiry.

### 3. Reg BI and the IA fiduciary standard

For broker-dealer themes, Reg BI (Regulation Best Interest) is the substantive framework: care obligation, disclosure obligation, conflict of interest obligation, compliance obligation. For investment adviser themes, the IA fiduciary standard governs (the IA Act §206 antifraud provision; the Commission's interpretation of the fiduciary standard in IA Release No. 5248, June 5, 2019).

The memo's regulatory exposure mapping cites the operative framework per theme; the customer-outcome lens (carried by the conduct overlay) extends the analysis beyond the rule-compliance check.

### 4. SEC Whistleblower and complaint-as-tip intersection

Where a complaint contains tip-grade information about firm conduct (an alleged §10b-5 violation; an alleged Reg BI care violation), the firm's complaint-management process intersects the SEC Whistleblower program (Securities Exchange Act §21F). The memo flags themes where this intersection is operative and routes to counsel; the theme analysis does not extend into whistleblower-program decisions.

### 5. Securities-based lending and the credit-side intersection

Where the firm offers securities-based lending (SBL) to retail clients, the SBL theme set can raise consumer-finance-style complaint patterns (margin-call mechanics; pledged-collateral disputes; account-suspension during market stress). The credit-side theme has a UDAAP-equivalent analytical structure even where CFPB jurisdiction does not reach. The memo names the analytical pattern but cites the securities-side authorities (Reg T; FINRA Rule 4210; FINRA Rule 4524 supplemental schedules).

### 6. AI / algorithmic surfaces in capital-markets

Capital-markets firms deploy AI / ML in research-generation, retail-investor messaging, robo-advisory account management, customer-service voice agents, fraud-deny decisioning, and trade-execution-quality decisioning. Themes that touch retail-investor-facing AI surfaces carry `ai_flag: true`. The SEC's July 2023 Proposed Rule on conflicts of interest associated with predictive data analytics by broker-dealers and investment advisers (Release No. 34-97990) is the operative framing [verify operative status given comment period and rulemaking schedule]. The April 2023 Joint Statement applies; FINRA has issued AI-related guidance [verify].

## Capital-markets-specific theme matrix additions

Per theme:

- `finra_4530_reportable` — boolean; if true, the Rule 4530(d) statistical reporting status is named.
- `reg_bi_intersection` — boolean; if true, the Reg BI obligation that the theme touches is named (care, disclosure, conflict of interest, compliance).
- `ia_fiduciary_intersection` — boolean.
- `sbl_credit_side_pattern` — boolean.
- `whistleblower_tip_routing` — boolean; if true, theme is flagged for counsel routing.

## Common pitfalls in capital-markets complaint-theme analysis

- Applying CFPB UDAAP framing to retail-brokerage themes. The substantive regime is Reg BI / IA fiduciary; the theme analysis adapts to the regime that has jurisdiction.
- Reading FINRA Rule 4530(d) statistical reporting as the firm's complaint surveillance program. The reporting is the regulator-facing summary; the firm's internal theme-analysis is the operating program and is broader.
- Missing the SBL credit-side intersection when the SBL theme arises during market stress; the theme has consumer-finance-pattern shape even where the regulatory regime is securities-side.
- Treating retail-investor robo-advisory complaints as broker-dealer or investment-adviser by default without naming the firm's registration; the regime depends on how the firm is registered.
- Routing whistleblower-tip-grade themes through the routine complaint-handling workflow without flagging counsel; the SEC Whistleblower intersection has timing and confidentiality consequences.
- Excluding app-store reviews on the brokerage app from the theme analysis; for retail-brokerage, the brokerage-app reviews are a meaningful channel and the same payments-fintech app-store-review treatment applies.
