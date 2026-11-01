# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for complaint-theme-analysis

When the scope record names sector `banking`, this overlay adds banking-specific theme patterns, evidence sources, and cross-skill chain detail. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `complaint-theme-analysis/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for banking complaint-theme analysis

Banking is the heaviest overlay on this skill. The CFPB Complaint Database has the deepest history on depository products; the firm's internal complaint-management surface for banking is typically more mature than for payments-fintech; the regulatory exposure surface is the most articulated. The memo inherits that machinery directly.

##### 1. Recurring banking complaint themes

A non-exhaustive theme catalogue for the deposits, mortgage, credit-card, and auto-credit lines:

- *Deposit account themes.* Overdraft and NSF themes (the APSN pattern; surprise representment fees; daily-fee-cap surprise; high-to-low transaction reordering); account-closure themes (closed-account-reopened-for-deposit fee themes per Circular 2023-02; closure without notice; closure for AML reasons with unclear consumer recourse); account-fee themes (minimum-balance fee surprise; paper-statement fee; dormant-account fee); funds-availability themes (Reg CC hold disputes; provisional-credit reversal); error-resolution themes (Reg E §1005.11 dispute handling on debit-card unauthorised use); account-opening themes (denial reason coding; ChexSystems-driven denial).
- *Mortgage themes.* Loss-mitigation themes (the repeatedly-lost-application pattern; clock-reset under Reg X §1024.41; continuity-of-contact gap); force-placed insurance themes (pricing dispute; existing-coverage-on-file disputes); payment-application themes (payments held in suspense during loss-mit; payments applied in non-borrower-favorable order); transfer-of-servicing themes (payment misapplication after transfer; fee assessment disputes); escrow-analysis themes (payment-shock surprise on escrow shortage); payoff-statement themes; PMI-cancellation themes (HPA timing); foreclosure-process themes.
- *Credit-card themes.* Fee-disclosure themes (FX fee not disclosed at point of sale; annual fee surprise; balance-transfer fee mechanic); deferred-interest themes (the no-interest-if-paid-in-full mechanic and the back-end interest assessment); rewards-program themes (devaluation; expiration; mid-cycle term changes); payment-application themes (Reg Z §1026.53 allocation order disputes; promotional-balance-vs-purchase-balance handling); late-fee themes (cutoff-time disputes; weekend-and-holiday cutoff disputes; intersects pending §1026.52 rule [verify operative status]); credit-line-decrease and adverse-action themes (reason-code specificity per Circulars 2022-03 and 2023-03 where complex models are in path); identity-theft and dispute themes (FCRA §1681i timing; Regulation V furnisher conduct).
- *Indirect auto themes.* Add-on product themes (GAP, VSC, debt-cancellation cancellation-and-refund disputes); dealer-discretionary-markup themes (where complaints surface at the lender level); titling and registration themes; default and repossession themes.
- *HELOC themes.* Account-suspension themes (suspension during draw period); rate-change themes (tied to index movement); payment-shock themes (interest-only-to-amortising transition).

The memo names the in-scope themes; the analysis blocks address each theme separately where multiple are at the top of the period count.

##### 2. CFPB Complaint Database scope and limits

The CFPB Complaint Database is the public anchor for banking complaint-theme analysis. The database covers complaints submitted directly to the CFPB consumer portal; the firm reports these into its complaint-management system through the bureau's company portal. The database is not the firm's full complaint surface; the firm-direct complaint channels (call center, web form, branch escalation, executive-resolution) typically dwarf the CFPB-portal subset.

The memo records:

- The CFPB-portal subset count and share of the firm's total period complaints.
- The deduplication treatment (CFPB-portal complaints typically exist in both the CFPB extract and the firm's internal records; the memo deduplicates against the firm's internal where the consent-flag permits matching).
- The narrative-consent treatment (the public extract redacts narrative on consumers who did not consent; the firm's internal records have the full narrative).
- The product, sub-product, issue, sub-issue field handling (the bureau's taxonomy is the public coding; the firm typically maintains a parallel firm taxonomy that maps to but does not equal the bureau's).

The bureau's taxonomy is not a root-cause taxonomy; it is the bureau's complaint-coding taxonomy. The memo themes against the firm's taxonomy and maps back to the bureau's coding for the public-comparison work.

##### 3. Bank size and CFPB authority

CFPB consumer-compliance authority reaches large banks (over $10B in assets) directly for the named consumer-protection statutes including UDAAP. Smaller banks fall under the prudential regulator (OCC, FRB, FDIC) for supervisory purposes; the substantive standards apply across the threshold. The memo records:

- Whether the institution is over the $10B threshold.
- The primary federal consumer-compliance regulator.
- Whether a CFPB enforcement angle is plausible on the in-scope themes (driven by Supervisory Highlights focal items, peer enforcement actions, and the consumer-harm magnitude of the themes).

##### 4. Sponsor-bank arrangement attribution

Where the bank operates a sponsor-bank arrangement (deposit, card, lending program for a fintech partner, BaaS arrangement), complaints often arrive at the bank but originate from the program operator's product or marketing. The memo records:

- Which legal entity holds the consumer-facing relationship for each theme.
- Which entity owns the product, marketing, and fee design at issue.
- Joint-program complaint-routing patterns; whether the program operator's complaint surface is also reviewed.
- Cross-skill chain into `udaap-risk-review` or `marketing-claim-review` is named with the bank as the accountable party.

##### 5. Mortgage-servicing rules intersection

Mortgage-servicing themes interact with the CFPB Servicing Rules (Reg X 12 CFR Part 1024 Subpart C; Reg Z 12 CFR §1026.41). The intersection is operationally important:

- Reg X §1024.41 (loss-mitigation procedures) is the operational baseline; loss-mit themes are tested against the §1024.41 timing and content requirements as a parallel inquiry to the UDAAP analysis.
- Reg X §1024.39 (early intervention) and §1024.40 (continuity of contact) anchor the borrower-communication themes.
- Reg X §1024.37 (force-placed insurance) anchors the FPI themes.
- Reg X §1024.33 (transfer of servicing) anchors the transfer themes.
- Reg X §1024.36 (request for information) anchors the QWR themes.

Compliance with the literal Reg X requirements is a baseline, not a UDAAP defence; the memo treats the Reg X check and the UDAAP unfairness analysis as parallel inquiries.

##### 6. CRA and HMDA cross-walk for mortgage and small-business themes

For HMDA-reportable mortgage and (where operative) §1071-reportable small-business themes, the geographic and demographic concentration analysis can use the firm's HMDA LAR or §1071 register as the denominator rather than BISG. HMDA self-reported demographics are stronger evidence than BISG for mortgage; the memo uses HMDA where available and falls back to BISG where not. CRA assessment-area overlap matters where redlining-adjacent themes appear; the cross-skill chain into `fair-lending-test-plan` carries the CRA framing.

##### 7. Banking-specific evidence sources

Banking complaint-theme analysis typically pulls evidence from:

- The firm's complaint-management system (firm-direct complaints from call center, branch, web form, executive resolution; CFPB-portal complaints routed through the bureau's company portal).
- The CFPB Consumer Complaint Database (public extract for the firm and product).
- Core-banking transaction data (denominator for rate analysis).
- Deposit-account, card, and mortgage-servicing system logs.
- Branch and call-center call recordings (for the consumer-journey context on top themes).
- Marketing-asset library (where themes trace to a campaign).
- Account-disclosure documents and Reg DD §1030.4 truth-in-savings disclosures.
- HMDA LAR for the mortgage denominator.

##### 8. Banking AI / algorithmic surfaces

Banks deploy AI / ML in credit-line decisioning, fraud-deny decisioning, customer-service voice agents, conversational AI, retention-offer engines, marketing personalisation, and AI-generated communication. Themes that touch these surfaces carry `ai_flag: true` and feed the cross-skill chain to `adverse-action-review` (for AAN-content themes), `udaap-risk-review` (for algorithmic-outcome themes), or `fair-lending-test-plan` (for protected-class-disparity themes). The April 2023 Joint Statement and CFPB Circulars 2022-03 and 2023-03 anchor the algorithmic-discrimination framing.

#### Banking-specific theme matrix additions

Per theme:

- `cfpb_portal_count` — count of complaints in the CFPB Complaint Database for this theme in the period.
- `cfpb_portal_share` — share of the theme's period count that arrives via the CFPB portal.
- `bank_size_threshold` — `over-10b` / `under-10b` / `unknown` (sets the CFPB-authority framing).
- `primary_federal_regulator` — `OCC` / `FRB` / `FDIC` / `NCUA`.
- `sponsor_bank_program` — boolean; if true, the program-operator attribution is named in the memo.
- `servicing_rules_intersection` — boolean; if true for mortgage-servicing themes, Reg X / Reg Z servicing rules are named alongside the UDAAP analysis.
- `cra_intersection` — boolean; if true for redlining-adjacent mortgage themes, CRA assessment area is named.

#### Common pitfalls in banking complaint-theme analysis

- Treating the CFPB Complaint Database as the full complaint surface. The CFPB portal is one channel; the firm-direct channels typically carry the larger volume.
- Theming at the bureau's product / sub-product / issue / sub-issue grain. The bureau's taxonomy is a complaint-coding taxonomy, not a root-cause taxonomy; two themes can share a sub-issue.
- Counting CFPB-portal and firm-direct complaints separately and double-counting the routed-portal subset. The memo deduplicates explicitly.
- Treating Reg X §1024.41 compliance as a UDAAP defence on mortgage-servicing themes. Reg X compliance is a baseline; the UDAAP analysis is parallel.
- Treating sponsor-bank-program themes as the program-operator's issue. The bank carries accountability under the third-party guidance and the program agreement; the memo names the bank as the accountable party.
- Reading credit-card fee themes from the marketing copy alone and missing the cardholder-agreement disclosure path. Both surfaces are in the consumer journey.
- Watching only the volume movement on a theme without rate framing. A volume increase that aligns with a campaign may not represent a rate increase; the memo computes rate per relevant denominator.
- Treating the BISG signal on banking themes as protected-class evidence. For mortgage, HMDA self-reported demographics are the operative source; for non-mortgage, BISG is signal-grade and feeds the watch-list, not the finding.

## capital-markets

### Capital markets sector overlay for complaint-theme-analysis

When the scope record names sector `capital-markets`, this overlay flags the scope boundary, names the analogous regimes, and adapts the theme-analysis pattern for retail brokerage and adjacent activities. Most capital-markets activity sits outside the CFPB's jurisdiction; the theme-analysis method is reusable but the regulatory exposure mapping shifts.

Loaded by: `complaint-theme-analysis/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type implicates a registered broker-dealer, registered investment adviser, futures commission merchant, or capital-markets affiliate of a banking organization.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Scope boundary first

Retail brokerage complaints are not CFPB-jurisdictional. The substantive complaint-handling regime for FINRA-member firms is FINRA Rule 4513 (Records of Written Customer Complaints) and FINRA Rule 4530 (Reporting Requirements). The customer-protection regime is Reg BI (Regulation Best Interest, 17 CFR §240.15l-1 for broker-dealers) and the IA fiduciary standard for investment advisers. The complaint-theme analysis method is reusable; the regulatory exposure mapping cites FINRA, SEC, and (for futures) NFA / CFTC sources rather than the CFPB authorities.

The overlay is named so reviewers do not over-extend the CFPB framing into capital-markets activity. It is also named so reviewers can run the same theme-analysis discipline (taxonomy, coding, trend, severity, root-cause hypothesis, recommended action) on retail-brokerage complaints under the FINRA framework.

#### What the theme-analysis method looks like under the FINRA / SEC framework

##### 1. Recurring retail-brokerage complaint themes

A non-exhaustive theme catalogue (FINRA Rule 4530 reportable categories overlap with these but are not identical):

- *Sales-practice themes.* Suitability themes (Reg BI care obligation; fact-pattern of recommendations not reasonably aligned to investment profile); concentration themes; high-cost-product themes; rollover themes (the IRA rollover decision and Reg BI care); annuity themes (fact-pattern of complex products sold to retail-eligible-but-unsophisticated investors); private placement and Reg D themes.
- *Account-handling themes.* Unauthorised trading themes; fee-disclosure themes (advisory fee, ticket charges, market-data fees, custody fees); margin-call themes (the consumer-experience friction and the disclosure of margin mechanics); securities-based lending themes (the credit-side intersection where retail clients use SBL).
- *Best-execution and order-handling themes.* Execution-quality complaints; payment-for-order-flow disclosure complaints; the Reg NMS-adjacent fact patterns.
- *Communication themes.* Marketing communication themes (Rule 2210 retail communication content); social-media-generated themes; AI-generated-research themes (the bot-generated commentary surfaces).
- *Account-opening and KYC themes.* Onboarding-friction themes; Reg S-K and Reg S-P privacy intersection on data collection; identity-verification themes.
- *Cybersecurity-incident-related themes.* Where account-takeover or unauthorised activity arises from an incident, the complaint surface intersects the Reg S-P safeguards rule and the firm's incident-disclosure conduct.
- *Customer-experience themes on the brokerage app.* (Same app-store-review pattern as payments-fintech; recurring themes are platform-friction, glitch-during-volatility, hold-on-deposit, settlement-confusion.)

##### 2. FINRA Rule 4513 / 4530 framing

FINRA Rule 4513 requires member firms to make and keep written customer complaints; FINRA Rule 4530(d) requires reporting of statistical and summary information about written customer complaints quarterly to FINRA. The memo records, per top theme:

- Whether the theme has been reported under Rule 4530(d) statistical reporting.
- Whether the firm's Rule 4513 retention is current.
- Whether the underlying conduct is also reportable under Rule 4530(a) or (b) (specific events, including written customer complaints alleging theft, misappropriation, or forgery).

The complaint-theme analysis surfaces the substantive theme; the FINRA reporting compliance is the parallel inquiry.

##### 3. Reg BI and the IA fiduciary standard

For broker-dealer themes, Reg BI (Regulation Best Interest) is the substantive framework: care obligation, disclosure obligation, conflict of interest obligation, compliance obligation. For investment adviser themes, the IA fiduciary standard governs (the IA Act §206 antifraud provision; the Commission's interpretation of the fiduciary standard in IA Release No. 5248, June 5, 2019).

The memo's regulatory exposure mapping cites the operative framework per theme; the customer-outcome lens (carried by the conduct overlay) extends the analysis beyond the rule-compliance check.

##### 4. SEC Whistleblower and complaint-as-tip intersection

Where a complaint contains tip-grade information about firm conduct (an alleged §10b-5 violation; an alleged Reg BI care violation), the firm's complaint-management process intersects the SEC Whistleblower program (Securities Exchange Act §21F). The memo flags themes where this intersection is operative and routes to counsel; the theme analysis does not extend into whistleblower-program decisions.

##### 5. Securities-based lending and the credit-side intersection

Where the firm offers securities-based lending (SBL) to retail clients, the SBL theme set can raise consumer-finance-style complaint patterns (margin-call mechanics; pledged-collateral disputes; account-suspension during market stress). The credit-side theme has a UDAAP-equivalent analytical structure even where CFPB jurisdiction does not reach. The memo names the analytical pattern but cites the securities-side authorities (Reg T; FINRA Rule 4210; FINRA Rule 4524 supplemental schedules).

##### 6. AI / algorithmic surfaces in capital-markets

Capital-markets firms deploy AI / ML in research-generation, retail-investor messaging, robo-advisory account management, customer-service voice agents, fraud-deny decisioning, and trade-execution-quality decisioning. Themes that touch retail-investor-facing AI surfaces carry `ai_flag: true`. The SEC's July 2023 Proposed Rule on conflicts of interest associated with predictive data analytics by broker-dealers and investment advisers (Release No. 34-97990) is the operative framing [verify operative status given comment period and rulemaking schedule]. The April 2023 Joint Statement applies; FINRA has issued AI-related guidance [verify].

#### Capital-markets-specific theme matrix additions

Per theme:

- `finra_4530_reportable` — boolean; if true, the Rule 4530(d) statistical reporting status is named.
- `reg_bi_intersection` — boolean; if true, the Reg BI obligation that the theme touches is named (care, disclosure, conflict of interest, compliance).
- `ia_fiduciary_intersection` — boolean.
- `sbl_credit_side_pattern` — boolean.
- `whistleblower_tip_routing` — boolean; if true, theme is flagged for counsel routing.

#### Common pitfalls in capital-markets complaint-theme analysis

- Applying CFPB UDAAP framing to retail-brokerage themes. The substantive regime is Reg BI / IA fiduciary; the theme analysis adapts to the regime that has jurisdiction.
- Reading FINRA Rule 4530(d) statistical reporting as the firm's complaint surveillance program. The reporting is the regulator-facing summary; the firm's internal theme-analysis is the operating program and is broader.
- Missing the SBL credit-side intersection when the SBL theme arises during market stress; the theme has consumer-finance-pattern shape even where the regulatory regime is securities-side.
- Treating retail-investor robo-advisory complaints as broker-dealer or investment-adviser by default without naming the firm's registration; the regime depends on how the firm is registered.
- Routing whistleblower-tip-grade themes through the routine complaint-handling workflow without flagging counsel; the SEC Whistleblower intersection has timing and confidentiality consequences.
- Excluding app-store reviews on the brokerage app from the theme analysis; for retail-brokerage, the brokerage-app reviews are a meaningful channel and the same payments-fintech app-store-review treatment applies.

## insurance

### Insurance sector overlay for complaint-theme-analysis

When the scope record names sector `insurance`, this overlay flags the scope boundary, names the analogous regime, and adapts the theme-analysis pattern for state-DOI complaint surfaces and MGA program complaints. Insurance complaint-handling sits outside the CFPB's jurisdiction; the theme-analysis method is reusable but the regulatory exposure mapping shifts entirely to state insurance departments and the NAIC framework.

Loaded by: `complaint-theme-analysis/SKILL.md` when `scope.sector_overlay_set` includes `insurance`, or when the institution type implicates a property and casualty insurer, life insurer, health insurer (in the consumer-finance scope where applicable), MGA / MGU, or insurance-licensed bank affiliate.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Scope boundary first

Insurance complaint-handling sits with state insurance departments under the NAIC Unfair Trade Practices Act framework (Model #880) and the NAIC Unfair Claims Settlement Practices Act framework (Model #900). The vocabulary differs: "unfair discrimination" between similarly-situated risks; "unfair claims settlement practices"; the substantive standards differ from the federal consumer-protection framework. State DOIs operate consumer complaint portals analogous to the CFPB Complaint Database; the NAIC Complaints Database (CDS) aggregates a subset of state complaint data.

The overlay is named so reviewers do not over-extend the CFPB framing into insurance underwriting, pricing, or claims handling. It is also named so reviewers can run the same theme-analysis discipline (taxonomy, coding, trend, severity, root-cause hypothesis, recommended action) on insurance complaints under the state-DOI framework.

The narrow exception is bank-affiliated credit-protection insurance bundled with a credit product, where the credit-side complaint theming runs under the consumer-finance framework and the insurance-side runs under the state-DOI framework; the memo carries both reads where the theme spans both surfaces.

#### What the theme-analysis method looks like under the state-DOI / NAIC framework

##### 1. Recurring insurance complaint themes

A non-exhaustive theme catalogue (the categories vary by line):

- *Underwriting themes.* Application-decision themes (denial reasons; rate-class themes; coverage-exclusion themes); rating-factor themes (the use of credit-based insurance score; the use of telematics or usage-based-insurance variables; the use of catastrophe modeling at the territory level); accelerated-underwriting themes for life insurance.
- *Claims-handling themes.* Claim-denial themes (reasonability of denial; claims-investigation conduct); claim-delay themes (failure to acknowledge, investigate, or pay within the prompt-payment statutes); claim-settlement-amount themes (low-ball offer pattern; depreciation-application themes; replacement-cost-vs-actual-cash-value); subrogation themes; coverage-interpretation themes (the policy-language dispute pattern).
- *Premium and billing themes.* Premium-increase themes (rate filing intersection); cancellation and non-renewal themes (statutory notice requirements; reason-for-cancellation themes); refund-handling themes; lender-placed insurance themes (where the insurance is placed by the credit lender; cross-references the banking sector overlay).
- *Marketing and producer-conduct themes.* Producer-misrepresentation themes; needs-analysis themes (annuity sales suitability); replacement-of-existing-coverage themes; producer-licensing themes.
- *AI / algorithmic-decisioning themes.* Themes that touch automated underwriting, automated claims-decisioning, AI-driven pricing, or generative-AI-driven communication; the NAIC Model Bulletin on AI (December 2023) [verify exact title and adoption status by state] is the operative cross-state framing.

##### 2. NAIC framework regulatory exposure mapping

For insurance themes, the regulatory exposure cites:

- NAIC Unfair Trade Practices Act (Model #880) section as adopted by the operative state(s).
- NAIC Unfair Claims Settlement Practices Act (Model #900) section as adopted by the operative state(s).
- State-specific market-conduct examination procedures.
- Line-specific regulatory framework (NAIC Annuity Suitability Model #275 and the best-interest amendments; NAIC Life Insurance Illustrations Model #582; etc.).
- For credit-based insurance scoring, the NAIC Credit-Based Insurance Score model and the state-specific filing posture.
- For the AI / algorithmic surfaces, the NAIC AI Model Bulletin (December 2023) and any state-adopted bulletin variants [verify per state].

The memo cites the operative state's adoption of the relevant NAIC model rather than citing the model alone, because adoption varies by state.

##### 3. State-DOI complaint portals and the NAIC CDS

Insurance complaint surveillance pulls from:

- State-DOI consumer complaint portals (each operative state).
- The NAIC Complaints Database (CDS) for the firm's complaint history and for peer comparison (where the firm is in CDS reporting scope).
- The firm's internal complaint records (call center, web form, broker channel, claims-team escalation).
- Producer-channel complaint records (where complaints route through the producer rather than direct to the carrier).

The memo names the channels reviewed; the firm-direct channel typically dwarfs the state-DOI channel by volume but the state-DOI channel carries weight because it is the regulator's own surveillance signal.

##### 4. MGA / MGU and program-business attribution

Where the firm operates through MGAs (managing general agents), MGUs (managing general underwriters), or program-business arrangements, the complaint-handling responsibility is allocated by the program agreement and the carrier's reinsurance posture. The memo records, per theme:

- Which entity holds the consumer-facing relationship (typically the MGA on the agent-side and the carrier on the policyholder relationship).
- Which entity owns the underwriting, pricing, or claims decision that the theme traces to.
- Which entity holds the ultimate coverage liability (the carrier; sometimes a reinsurer with cut-through).
- Joint-review framing where the theme runs through both the MGA and the carrier.

##### 5. Customer-outcome themes vs. unfair-discrimination themes

The state-DOI framework's "unfair discrimination" vocabulary is narrower than the federal framework's protected-class-disparate-impact vocabulary. Unfair discrimination in insurance generally refers to differential treatment among similarly-situated risks not justified by actuarial or other objective considerations; it is not coterminous with the disparate-impact framework. The memo is explicit about which framework is doing the analytical work; the customer-outcome lens (carried by the conduct overlay) extends the analysis where the policy-relevant segment lens supplements the actuarial-justification lens.

For lines where the federal framework also applies (credit insurance bundled with a federally-regulated credit product; ERISA-governed health insurance for the §1557 nondiscrimination angle), the memo cites both frameworks.

##### 6. Credit-protection insurance bundled with credit (the narrow CFPB intersection)

Where the in-scope theme involves credit-protection insurance bundled with a credit product (GAP, credit life, credit disability, credit unemployment, debt cancellation), the credit-side complaint theme runs under the consumer-finance framework (the bundling mechanic; the disclosure timing relative to closing; the cancellation-and-refund mechanic; the value-of-coverage-vs-cost analysis), and the insurance-side complaint theme runs under the state-DOI framework. The memo carries both reads. Cross-skill chain into `udaap-risk-review` for the credit-side bundling mechanic; the insurance-side stays in this overlay.

##### 7. AI / algorithmic surfaces in insurance

Insurance carriers deploy AI / ML in automated underwriting, accelerated underwriting, claims-decisioning, fraud-deny decisioning, customer-service voice agents, and policy-language summarisation. Themes that touch these surfaces carry `ai_flag: true`. The NAIC Model Bulletin on AI (December 2023) [verify] is the operative cross-state framing; state adoption varies. The memo cites the model bulletin and the state-specific adoption posture.

The April 2023 Joint Statement applies in spirit (the four federal agencies' framing on automated systems extends to insurance where federal authorities reach, though the EEOC, FTC, and CFPB are not the operating regulators on most insurance themes); the memo names the federal framing where the theme touches a federally-regulated decision.

#### Insurance-specific theme matrix additions

Per theme:

- `state_doi_complaint_count` — count of complaints in the operative state-DOI portal(s) for this theme.
- `naic_cds_count` — count of complaints in the NAIC Complaints Database for this theme (where firm is in CDS scope).
- `naic_model_intersection` — list of NAIC models that the theme touches (Model #880; Model #900; Model #275; etc.).
- `state_adoption_status` — for each NAIC model cited, the operative state's adoption status.
- `mga_program_attribution` — `carrier-of-record` / `mga-of-record` / `joint` / `under-program-agreement-allocation`.
- `bundled_with_credit` — boolean; if true, the credit-side cross-skill chain into `udaap-risk-review` is named.

#### Common pitfalls in insurance complaint-theme analysis

- Applying CFPB UDAAP framing to insurance underwriting, pricing, or claims-handling themes. The substantive regime is state-DOI under the NAIC framework; the federal authorities do not reach most insurance themes.
- Citing the NAIC model without naming the operative state's adoption status. NAIC models are guides; only state adoption is binding.
- Treating insurance "unfair discrimination" as equivalent to federal disparate-impact. The vocabulary and the substantive standards differ; the memo is explicit about which lens is operating.
- Missing the MGA / program-business attribution question. Program-business arrangements allocate the complaint-handling duty between MGA and carrier; the memo names the allocation.
- Theming credit-protection-insurance complaints as either pure-credit or pure-insurance when the theme spans both surfaces. The memo carries both reads.
- Reading state-DOI complaint volume in isolation from the NAIC CDS peer benchmark; the CDS comparison is part of how the regulator reads the firm's complaint posture.
- Treating accelerated-underwriting AI themes as model-risk-only issues; the consumer-experience surface is in scope and the theme analysis covers it.
- Missing the producer-channel complaint records when complaints route through the producer rather than direct to the carrier; both channels are in the population.

## payments-fintech

### Payments and fintech sector overlay for complaint-theme-analysis

When the scope record names sector `payments-fintech`, this overlay adds payments-fintech-specific theme patterns, evidence sources, and attribution detail. Where there is conflict between the capability defaults and this overlay, the overlay governs the payments-fintech-sector elements.

Loaded by: `complaint-theme-analysis/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a fintech program operator, money services business, P2P provider, BNPL provider, neobank, or sponsor-bank-aligned consumer-finance fintech.

Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for payments-fintech complaint-theme analysis

Payments and fintech is the second-heaviest overlay on this skill. The complaint surfaces are different from banking: app-store reviews carry meaningful signal; the CFPB Complaint Database coverage is uneven across product types; the sponsor-bank-vs-fintech attribution question is non-trivial; the dispute-handling rhythm under Reg E is the recurring substantive theme.

##### 1. Recurring payments-fintech complaint themes

A non-exhaustive theme catalogue:

- *P2P and instant-payment themes.* Reg E §1005.11 error-resolution themes (provisional-credit timing; investigation depth on unauthorised-transfer claims; final-resolution communication); fraud-and-scam themes (the consumer-authorised-the-transfer-but-was-deceived pattern; the §1005.6 unauthorised-EFT scope question); account-takeover themes; recipient-error themes (consumer sent to wrong recipient; reversal mechanics); customer-service-friction themes on disputes.
- *BNPL themes.* Disclosure themes (the four-payment plan vs. interest-bearing extension); late-fee and missed-payment themes; merchant-dispute themes (consumer dispute with merchant intersecting the BNPL repayment obligation); credit-reporting themes (whether and when BNPL repayment hits the consumer's credit file); collections themes; subscription-style and recurring-purchase themes on BNPL.
- *Neobank themes.* Account-closure and frozen-account themes (often AML-driven; consumer recourse unclear); funds-availability themes; deposit-of-government-benefit themes (often overlaps with prepaid framing); customer-service-channel themes (chat-only support friction; AI-agent escalation friction); dispute-handling themes.
- *Subscription, negative-option, and "instant-funding" themes.* Cancellation-friction themes (the dark-pattern intersection); auto-renewal themes; tip-as-fee themes (variable tipping presented as voluntary but functionally required); instant-funding fee themes (where a small fee is charged for "instant" delivery of funds the consumer is told are theirs); the FTC Negative Option Rule [verify operative status given litigation] intersection.
- *Sponsor-bank attribution themes.* Themes where complaints arrive at the fintech but the legal entity holding the consumer-facing relationship is the sponsor bank; themes where complaints arrive at the bank but the product, marketing, and fee design originate from the fintech program operator.
- *AI agent themes.* Conversational-AI complaint-handling themes (the agent did not understand; the agent gave incorrect information; the consumer could not reach a human); AI-generated-communication themes (the email or in-app message misled); AI-driven personalisation themes (the offer or rate the consumer received differs from peer experience).
- *App-store review themes specific to fintech.* Onboarding-friction themes; identity-verification themes; account-closure-without-notice themes; the dispute-process themes that surface in app-store reviews more often than in CFPB-portal complaints.

The memo names the in-scope themes; the analysis blocks address each theme separately where multiple are at the top of the period count.

##### 2. App-store reviews as a non-CFPB complaint channel

App-store reviews on the fintech's mobile app are a meaningful complaint channel for payments-fintech. The CFPB Complaint Database does not aggregate app-store reviews; the firm's complaint-management system typically does not pull them either. The memo treats app-store reviews as a separate channel:

- Channel coverage: which app stores (iOS App Store, Google Play, third-party stores where applicable) and the period reviewed.
- Volume normalisation: app-store reviews skew negative (reviewers self-select); the memo treats the volume as signal but the share comparison against CFPB-portal complaints is read with the bias in mind.
- Categorical coding: app-store reviews are coded to the firm's theme taxonomy alongside the CFPB-portal and firm-direct complaints.
- Action chain: app-store review themes that match a CFPB-portal or firm-direct theme reinforce the signal; themes that appear in app-store reviews and not in the CFPB-portal channel are surfaced separately as "app-store-only" themes for a specific watch.

App-store reviews are a leading indicator on consumer-experience friction themes that often do not yet rise to a regulator-portal complaint.

##### 3. Sponsor-bank attribution per theme

The attribution question is non-trivial because the regulator looks through to whichever entity is accountable for the conduct under the program agreement and the bank's third-party-risk framework. The memo records, per theme:

- Which legal entity holds the consumer-facing relationship (typically the sponsor bank for the deposit, card, or credit account; the fintech for the app and the customer-service surface).
- Which entity owns the product, marketing, and fee design that the theme traces to.
- Which entity owns the disclosure that the theme traces to.
- Which complaint surface received the complaint (sponsor bank's CFPB portal; fintech's complaint surface; both).
- Joint-review framing where the theme runs through both entities.

The memo cross-references `udaap-risk-review` or `marketing-claim-review` with the bank as the accountable party (per the interagency third-party guidance).

##### 4. Reg E error resolution as the recurring substantive theme

P2P and instant-payment themes recurrently raise the Reg E §1005.11 error-resolution framework. The memo records, per relevant theme:

- The error-resolution timing posture (10-day provisional credit, 45-day final determination, 90-day final determination for new accounts and certain transaction types).
- The §1005.6 unauthorised-EFT scope question (the consumer-authorised-the-transfer-but-was-deceived fact pattern is the most-litigated boundary).
- The CFPB and FTC enforcement themes on P2P providers and the §1005.11 process.
- The fintech-vs-sponsor-bank duty allocation on dispute handling under the program agreement.

Where Reg E themes are in the population, the memo also names whether the §1005.11 process compliance check has been done by the firm's first-line; the theme analysis surfaces the substantive theme, but the procedural Reg E compliance check is the parallel inquiry.

##### 5. Junk-fee theme intersection

Payments-fintech is the bureau's recent focal area on junk fees: tip-as-fee mechanics; instant-funding fee mechanics; subscription-style fee mechanics; representment NSF on linked deposit accounts. The memo treats junk-fee themes specifically, with the cross-skill chain into `udaap-risk-review` for the element-by-element analysis on the operative fee mechanic.

##### 6. CFPB Complaint Database coverage and limits for payments-fintech

The CFPB Complaint Database covers some payments-fintech products well (prepaid cards, money transfers, virtual currency-adjacent services where they touch the bureau's perimeter) and others patchily (BNPL coverage has improved but is still partial; some neobank deposit complaints are routed to the sponsor bank in the database). The memo records the database-coverage caveat per theme:

- Whether the bureau's taxonomy has a dedicated product or sub-product code for the in-scope theme.
- Whether the firm's CFPB-portal subset is comprehensive on the theme or whether the firm's internal records carry the larger share.
- Whether app-store reviews and social signals materially supplement the CFPB-portal coverage on the theme.

##### 7. AI-agent and AI-generated-communication themes

Payments-fintech is heavy on consumer-facing AI: conversational AI in customer service; AI-generated messaging and notifications; AI-driven personalisation in offers and rates; AI-driven dispute-decisioning. Themes that trace to these surfaces carry `ai_flag: true` and feed the cross-skill chain. The April 2023 Joint Statement is the cross-agency anchor; CFPB Circulars 2022-03 and 2023-03 apply where the AI surface generates AAN content or reason coding.

The dark-pattern frame is mandatory loaded for any AI-agent or AI-generated-communication theme; AI-mediated cancellation friction, AI-driven retention-offer urgency, and AI-personalised disclosure variability are recurring dark-pattern themes that the memo surfaces as such.

##### 8. Payments-fintech-specific evidence sources

Payments-fintech complaint-theme analysis typically pulls evidence from:

- The firm's complaint-management system (in-app complaint flow; chat transcripts; CFPB-portal complaints).
- The CFPB Consumer Complaint Database extract (where coverage is operative for the product).
- App-store reviews on iOS and Google Play (with the bias caveat noted).
- Social-listening signals (Twitter/X, Reddit, consumer-advocacy forums) where the firm operates a social-monitoring program.
- The fintech's product analytics (denominator for rate analysis: active users; transaction count; new-account openings).
- Conversational-AI transcript logs (for AI-agent themes).
- Marketing-asset library (for themes traced to a campaign).
- Sponsor-bank's complaint surface and program-level disclosures (for joint-attribution themes).

#### Payments-fintech theme matrix additions

Per theme:

- `app_store_review_count` — count of app-store reviews coded to this theme in the period (with channel breakdown).
- `cfpb_portal_count` — count of CFPB-portal complaints (where applicable).
- `firm_direct_count` — count of firm-direct complaints (in-app, chat, web form).
- `social_signal_count` — count of social-listening signals (where the firm operates social monitoring).
- `sponsor_bank_attribution` — `bank-of-record` / `fintech-of-record` / `joint` / `under-program-agreement-allocation`.
- `reg_e_intersection` — boolean; if true, the §1005.11 process compliance check is named alongside the substantive theme.
- `ai_surface_in_path` — boolean; the AI cross-skill chain.
- `dark_pattern_frame` — `friction-design` / `choice-architecture` / `urgency-scarcity` / `confirm-shaming` / other.

#### Common pitfalls in payments-fintech complaint-theme analysis

- Excluding app-store reviews because they "are not complaints". For payments-fintech, app-store reviews are a leading-indicator complaint channel and the memo treats them as such.
- Treating the CFPB Complaint Database as the full complaint surface for BNPL or neobank deposits where the database coverage is uneven.
- Reading the consumer-authorised-the-transfer-but-was-deceived theme as outside Reg E without naming the §1005.6 unauthorised-EFT scope question; the question is contested and the memo carries the analytical posture.
- Treating sponsor-bank arrangements as the bank's UDAAP issue or as the fintech's UDAAP issue without naming the program-agreement allocation; both entities carry duty under the interagency guidance.
- Reading AI-agent themes as customer-service-quality themes only and missing the deception or unfairness angle on AI-generated communication content.
- Theming at the firm's product taxonomy without recognising the dark-pattern frame; the journey-design theme is a separate read on the same complaint population.
- Counting a theme by app-store review volume as if app-store volume mapped 1:1 to the firm's overall consumer base; the volume is signal, the rate is the denominator-adjusted measure.
- Missing the social-signal channel where the firm has a social-listening program; consumer-advocacy-forum threads on neobank account-closure themes are a recurring leading indicator.
