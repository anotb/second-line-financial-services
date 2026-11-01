# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## credit-card-fee-disclosure-quarterly

### Example: quarterly complaint-theme analysis on a mid-size credit-card issuer with a "fees not disclosed at point of sale" cluster

#### Input

A mid-size monoline credit-card issuer (consumer general-purpose card; over $10B in assets; CFPB consumer-compliance supervision) runs the standard quarterly complaint-themes pack to the consumer compliance committee. The period is the prior calendar quarter. The population pulled: the firm's internal complaint records for the period (CFPB-portal complaints routed through the firm; firm-direct complaints from the call center, web form, and chat); the public CFPB Complaint Database extract for the same period filtered to the firm and the credit-card product; app-store reviews on the firm's mobile-banking app (one quarter rolling); employee-escalation log entries flagged as consumer-impact.

A December marketing campaign in the prior quarter restructured the card's rewards-bonus offer; the foreign-transaction fee disclosure on the post-click landing page sits below the fold on mobile. The complaint-management team has a working hypothesis that the campaign drove a fee-disclosure cluster.

The CCO and the head of consumer compliance are jointly sponsoring the review. Source posture is public-plus-firm-policy-plus-evidence; the firm has the complaint records, the marketing-asset library for the December campaign, the cardholder agreement, and the post-click landing-page archive. Outside counsel is not directing; this is a routine quarterly cycle.

#### Why this scenario matters

The quarterly-theme cycle is the canonical fact pattern: multiple complaint sources to triangulate; a hypothesised root cause tied to a specific marketing campaign; a regulatory exposure that crosses UDAAP §1031 deception and Reg Z §1026.6 disclosure framing; a cross-skill chain to `marketing-claim-review` (asset-side), `udaap-risk-review` (theme-to-element-test), and the firm's complaint-management committee. The example exercises the theme-aggregation table (the structured artifact) and the memo-narrative analysis (the judgement-shaped artifact) in the same delivery.

The example also exercises the period-over-period trend treatment: the theme moves from 19 percent of period complaints to 28 percent, which is meaningful even before the rate adjustment for the campaign-driven volume increase. The memo carries both the count-share and the rate framing.

#### Output sketch

##### Theme matrix (Excel artifact, abbreviated)

| theme_id | theme_label | definition | count | share | trend | severity | regulatory_exposure | conduct_flag | fair_lending_flag | ai_flag |
|---|---|---|---|---|---|---|---|---|---|
| THEME-CC-FEE-FX-01 | Foreign-transaction fee not disclosed at point of sale | Complaints citing surprise FX fee on the December rewards-bonus signup; complainant references the post-click landing page; calls the FX fee "hidden" or "small print" | 1,247 | 28% | up (from 19% prior quarter; new theme last quarter) | high | UDAAP §1031 deception; Reg Z 12 CFR §1026.6(b)(1) account-opening fee disclosure; Reg Z §1026.16 advertising | true | false | false |
| THEME-CC-DEC-PAYAPP-02 | Payment application order disputes | Complaints citing payment posted to wrong balance segment under the cardholder agreement; concentrated in deferred-interest promotional balances | 342 | 8% | flat | medium | Reg Z §1026.53 (allocation of payments); UDAAP §1031 deception on the deferred-interest mechanic | true | false | false |
| THEME-CC-LATE-FEE-03 | Late fee assessment on payment received in window | Complaints citing late fee assessed where the consumer asserts payment was received before the cutoff; clustered on weekend and holiday cutoffs | 188 | 4% | up (from 2% prior quarter) | medium | Reg Z §1026.10 prompt crediting; UDAAP §1031 unfairness; intersects pending §1026.52 late-fee rule [verify operative status] | true | false | false |
| THEME-CC-AAN-REASONS-04 | Adverse-action reason codes not specific (credit-line decrease) | Complaints citing CLD with reason code that does not match the consumer's understanding of their account history; clustered post-March model refresh | 96 | 2% | new | medium | Reg B §1002.9 specificity (CFPB Circular 2023-03 withdrawn May 12, 2025; obligation survives on regulation); UDAAP deception on AAN content | true | false | true |
| ... | (additional themes in full extract) | | | | | | | | | |
| TOTAL | | | 4,453 | 100% | | | | | | |

The full Excel file carries: per-theme `definition`, `severity_rationale`, `root_cause_hypotheses`, `regulatory_exposure[]` (one row per citation), `recommended_actions[]` (one row per action with owner, due date, named control), `demographic_skew` (state and ZIP3 distributions where present), `cross_references` (named downstream skill).

##### Memo (Word artifact, abbreviated narrative)

**Scope and population.** Period: prior calendar quarter. Sources reviewed: firm internal complaints (3,418); CFPB-portal complaints routed through the firm (892, deduplicated against firm-direct); CFPB public Complaint Database extract for the firm and credit-card product (1,206; not deduplicated against firm internal because the public extract redacts on consumer consent); app-store reviews on the mobile-banking app (147 in the period flagged for consumer-impact); employee-escalation log (38 entries). State AG complaints not pulled this cycle; called out as a scope gap. Total deduplicated unique complaint events in the period: 4,453.

**Theming method.** Firm taxonomy version 2026.Q1; 14 active themes plus a residual bucket. Each complaint coded to one primary theme and (where applicable) one secondary theme; primary-theme assignment used for the count and share. Pre-registered method applied to the entire sample, not to a narrative-read subset; coding agreement on a 200-complaint dual-read sample was 91 percent. BISG enrichment applied to the consumer name and ZIP9 where consent-flag permits; geographic enrichment to MSA and ZIP3. Reproducibility: the taxonomy mapping document is filed at `[firm-internal path]`; the coding rule for each theme is specified.

**Top themes.** The headline finding is THEME-CC-FEE-FX-01 (foreign-transaction fee not disclosed at point of sale). Theme appeared as a new theme in the prior quarter at 19 percent share and has moved to 28 percent in the current quarter. Counter-hypothesis tested: campaign-driven volume increase might inflate the share without a true rate increase. The rate (complaints per 1,000 new-account openings) for this theme moved from 4.2 to 7.8 in the current quarter; the rate movement is independent of the volume increase and supports the share movement as a real signal, not an artifact.

The remaining themes are listed in the matrix; each has a `theme_definition`, `count`, `share`, `trend`, and a `severity` per the rubric.

**Severity rubric.** Critical: theme matches a public CFPB enforcement focal item directly with material population and ongoing harm. High: theme matches a Supervisory Highlights focal item or peer enforcement; meaningful population; remediation needed in this committee cycle. Medium: real theme; population bounded; remediation enters the controls roadmap. Low: theme present but population is small or driven by isolated process defects.

THEME-CC-FEE-FX-01 is rated `high`. The theme matches a Supervisory Highlights focal item on credit-card fee disclosure (most recent two issues at memo date); population is meaningful (1,247 complaints in the period plus a non-trivial subset of the app-store reviews); the trend is up; the underlying campaign is still live.

**Root-cause hypotheses.** For THEME-CC-FEE-FX-01: (1) the December campaign restructured the rewards-bonus offer with the FX-fee disclosure in a position below the fold on mobile; (2) the cardholder agreement disclosure path (linked in the application flow) is a long-form PDF that consumers do not read in the application moment; (3) the call-center script for FX-fee questions does not surface the December campaign as the entry point and treats every caller as a generic FX-fee complaint. Hypothesis (1) is the operative root cause for the period; hypothesis (3) is a process-side amplifier. Hypothesis (2) is structural and does not explain the period-over-period trend on its own.

**Regulatory exposure.** Per theme. THEME-CC-FEE-FX-01 cites: UDAAP §1031 deception (the marketing-vs-actual-cost mismatch in the post-click landing page is a context-driven deception fact pattern; CFPB has consistently pursued context-driven deception); Reg Z 12 CFR §1026.6(b)(1) account-opening disclosure of fees; Reg Z §1026.16 advertising rules; potential FTC §5 angle if the marketing campaign reaches non-bureau-jurisdictional channels.

**Conduct-risk implications.** Per theme; the conduct overlay loads on this skill. THEME-CC-FEE-FX-01 ties to: product-design (the campaign offer structure); communication (the post-click landing page); customer-outcome (consumers who opted in to FX-using cards based on the bonus); complaint-linkage (the theme is the canonical complaint-monitoring leading indicator); and incentives (the marketing team's KPI on bonus-driven account opening). Conduct-accountable manager: head of card marketing (per the firm's conduct framework). Conduct committee read: yes. Conduct-event candidate: yes (recommendation only; the conduct-risk function classifies).

**Trends and movements.** THEME-CC-FEE-FX-01 trend up (19 percent to 28 percent share, with rate movement supporting the share movement as a real signal). THEME-CC-LATE-FEE-03 trend up (2 percent to 4 percent share, possibly seasonality on weekend cutoffs spanning the holiday period; flagged for next-quarter retest). THEME-CC-AAN-REASONS-04 new theme (post-March model refresh; ai_flag set; chains to `adverse-action-review`). All other themes flat or down within ±1 percentage point.

**Recommended actions.** Per theme. THEME-CC-FEE-FX-01: marketing review on the December campaign disclosure prominence (cross-reference `marketing-claim-review`; owner: head of card marketing; due date: end of next month; accountable forum: marketing review committee with consumer compliance read). UDAAP risk re-rating on the FX-fee mechanic (cross-reference `udaap-risk-review`; owner: head of consumer compliance; due date: in this committee cycle; accountable forum: consumer compliance committee). Cardholder-agreement disclosure path review (owner: head of card products; due date: next two committee cycles; accountable forum: product committee). Call-center script update on FX-fee complaints to surface the December campaign as the entry point and route to a dedicated handling path (owner: head of card servicing; due date: end of next month; accountable forum: consumer compliance committee). Complaint-monitoring loop closure: post-action monitoring on THEME-CC-FEE-FX-01 with a re-read at the next quarterly cycle and an off-cycle trigger if the rate continues to climb after the marketing change.

**Open questions and dissent.** Whether the cardholder-agreement disclosure-path review extends to a full account-opening-disclosure refresh (the second-line view is yes; the product team's view is to scope down). Whether the late-fee theme (THEME-CC-LATE-FEE-03) should be elevated given the pending §1026.52 rule status. Whether the BISG-enriched demographic skew on THEME-CC-FEE-FX-01 (slight over-representation in two MSAs with majority-minority concentrations) warrants a fair-lending flag in this cycle or a watch-list flag pending the next quarter's data.

**Source trace and confidence.** Material claims cite sources from `references/source-anchors.md` and the loaded banking and conduct overlays by file path. Confidence label: high on the count-share-and-rate analysis; medium on the root-cause hypotheses (the campaign is the leading hypothesis but the alternative explanations have not been ruled out by experiment); medium on the demographic-skew read (BISG signal only at this cycle; the fair-lending flag is a watch-list flag, not a finding).

#### What this delivers and does not deliver

The delivery operationalises the quarterly complaint-themes pack: theme aggregation table (Excel) plus memo (Word). The consumer compliance committee acts on the recommended actions; the conduct committee gets a read; the operations function executes the call-center script update and the marketing review. The memo does not finalise any UDAAP determination (chain to `udaap-risk-review` for THEME-CC-FEE-FX-01 if the committee elects to escalate); it does not finalise any fair-lending finding (the BISG signal feeds the watch-list, not a finding); and it does not take action on individual complaints (those run through the firm's case-management workflow).

The trend treatment uses both count-share and rate framing because the campaign drove a volume increase that would otherwise inflate the share artifact. The root-cause hypotheses are stated as hypotheses, not conclusions, because the theming method surfaces signal but does not establish causation; the experiments to confirm or reject the hypotheses run after the committee acts.

Pattern derived from public CFPB enforcement and supervisory observations on credit-card fee-disclosure themes; the marketing-campaign root-cause hypothesis is a public-source-derived structural pattern, not a specific firm. The example surfaces the theming-method discipline (pre-registered, applied to the full sample, dual-read agreement on a subset) that distinguishes a theme analysis from confirmation-bias theme inflation.

## mortgage-servicing-loss-mit-cluster

### Example: 12-month complaint-theme analysis on a mortgage servicer with a "loss mitigation application repeatedly lost" cluster concentrated in three MSAs

#### Input

A mortgage servicer (national bank-affiliated; servicer of record for both portfolio and GSE-investor loans; CFPB consumer-compliance supervision) runs a 12-month complaint-themes review after a CFPB-portal complaint cluster surfaced in routine quarterly monitoring. The trigger is the cluster, not the calendar.

The population pulled: CFPB-portal complaints routed through the servicer for the prior 12 months; firm-direct complaints from the loss-mit servicing line and the executive-resolution channel; CFPB public Complaint Database extract for the same period filtered to the firm, mortgage product, and the loss-mit and modification sub-issues; State AG referrals (HUD HOPE Hotline forwards and state-specific referrals); employee-escalation log entries from the loss-mit servicing team. App-store reviews not pulled (servicing-only, no consumer-facing app for portfolio-loan borrowers).

The clustered theme: "loss mitigation application repeatedly lost" (consumer submits a loss-mitigation package, is told it is incomplete or missing, resubmits, is again told it is incomplete or missing, and the loss-mit clock under Reg X §1024.41 is repeatedly reset). The cluster is concentrated in three MSAs: per-MSA share is 4-7x the firm's overall mortgage complaint share. State / ZIP3 / BISG enrichment shows two of the three MSAs are majority-minority by HMDA self-reported demographics on the firm's most-recent year of mortgage originations.

The CCO, the head of fair lending, and the head of mortgage servicing are jointly sponsoring the review. Outside counsel is directing for privilege. Source posture is public-plus-firm-policy-plus-evidence.

#### Why this scenario matters

The example exercises the fair-lending escalation chain, the demographic-enrichment treatment, and the cross-skill handoff to `fair-lending-test-plan`. The clustered theme matches a recurring CFPB enforcement and supervisory focus area on mortgage-servicing loss-mit conduct (multiple public consent orders); the geographic concentration plus the BISG signal is the pattern that triggers the fair-lending flag. The memo has to handle the population/rate framing carefully (per-MSA share comparison; rate per loss-mit-eligible borrower in each MSA); the BISG signal as flag-not-finding; and the cross-skill chain to `fair-lending-test-plan` for finding-grade analysis.

The example also exercises the privilege posture (counsel directing because the fair-lending implication is real) and the conduct-risk implications block (the servicing-team workflow is a conduct issue, not just a controls issue).

#### Output sketch

##### Theme matrix (Excel artifact, abbreviated)

| theme_id | theme_label | definition | count | share | trend | severity | regulatory_exposure | conduct_flag | fair_lending_flag | ai_flag | demographic_skew |
|---|---|---|---|---|---|---|---|---|---|---|---|
| THEME-MTG-LM-LOST-01 | Loss-mit application repeatedly lost or marked incomplete | Complaints citing repeated loss-mit submissions; document-receipt disputes; clock-reset under Reg X §1024.41 | 412 | 18% | up (from 9% prior 12-month period) | high | Reg X §1024.41 (loss-mit procedures); Reg X §1024.39 (early intervention); UDAAP §1031 unfairness; ECOA / FHA disparate impact | true | true (concentration plus BISG signal) | false | Concentrated in 3 MSAs (per-MSA share 4-7x baseline); 2 of 3 MSAs majority-minority |
| THEME-MTG-FORCE-INS-02 | Force-placed insurance pricing dispute | Complaints citing force-placed hazard insurance assessed where the borrower asserts existing coverage was on file | 187 | 8% | flat | medium | Reg X §1024.37 (force-placed insurance); UDAAP §1031 deception; Flood Disaster Protection Act intersection | true | false | false | Distributed |
| THEME-MTG-PAY-APP-03 | Payment application during loss-mit | Complaints citing payments held in suspense rather than applied during loss-mit evaluation; fee assessment on suspense balance | 134 | 6% | up | medium | Reg X §1024.36 (request for information); Reg Z §1026.41 (periodic statements); UDAAP §1031 unfairness | true | false | false | Distributed |
| THEME-MTG-XFER-04 | Transfer-of-servicing notice errors | Complaints citing payment misapplication or fee assessment after a servicer transfer | 89 | 4% | flat | medium | Reg X §1024.33 (transfer of servicing); UDAAP deception | true | false | false | Distributed |
| ... | (additional themes in full extract) | | | | | | | | | | |
| TOTAL | | | 2,287 | 100% | | | | | | | |

The full Excel file carries: per-theme `definition`, `severity_rationale`, `root_cause_hypotheses`, `regulatory_exposure[]`, `recommended_actions[]` (with owner, due date, named control), `demographic_skew` (per-MSA share, BISG-derived signal where present), `cross_references`.

##### Memo (Word artifact, abbreviated narrative)

**Scope and population.** Period: prior 12 months. Sources reviewed: firm internal complaints from the loss-mit servicing line and the executive-resolution channel (1,684); CFPB-portal complaints routed through the firm (587, deduplicated against firm-direct); CFPB public Complaint Database extract for the firm, mortgage product, loss-mit and modification sub-issues (412; not deduplicated against firm internal because of consent-redaction); HUD HOPE Hotline forwards and state-AG referrals on the same scope (52); employee-escalation log entries flagged for loss-mit-handling concern (76). Total deduplicated unique complaint events in the period: 2,287. Channels excluded: app-store reviews (no consumer-facing app for portfolio-loan borrowers).

**Theming method.** Firm taxonomy version 2026.Q2-mortgage; 11 active themes plus residual. Each complaint coded to one primary theme and (where applicable) one secondary theme. Pre-registered coding rules; full-sample application. Coding agreement on a 200-complaint dual-read sample was 89 percent (lower than the firm's typical 92 percent on credit-card complaints; the loss-mit narratives are more variable in language and the coding rule needed clarification mid-review for the THEME-MTG-LM-LOST-01 boundary). Geographic enrichment to MSA and ZIP3 by mailing address. BISG enrichment applied to consumer name and ZIP9 where data permits; HMDA self-reported demographics consulted at the MSA-aggregate level for context (HMDA is the operative demographic source for mortgage; BISG is supplemental and surname-based).

**Top themes.** The headline finding is THEME-MTG-LM-LOST-01 (loss-mit application repeatedly lost or marked incomplete). Theme share moved from 9 percent of period complaints (prior 12-month period) to 18 percent in the current period. Per-MSA share analysis: three MSAs (named in the firm-internal record by ZIP3, redacted in this memo per firm convention) carry per-MSA shares of 38 percent, 41 percent, and 47 percent on this theme, against a baseline firm-wide share of 18 percent. The 4-7x concentration is the operative red flag.

The other themes (force-placed insurance, payment application during loss-mit, transfer-of-servicing notice errors) are present at meaningful levels but do not show the geographic concentration of THEME-MTG-LM-LOST-01.

**Severity rubric.** Critical: theme matches a public CFPB enforcement focal item directly with material population and ongoing harm. High: theme matches a Supervisory Highlights focal item or peer enforcement; meaningful population; remediation needed in this committee cycle. Medium: real theme; population bounded; remediation enters the controls roadmap. Low: theme present but population is small or isolated.

THEME-MTG-LM-LOST-01 is rated `high`. The theme matches a recurring CFPB enforcement and supervisory focal item on mortgage-servicing loss-mit conduct (multiple public consent orders). The population is meaningful (412 complaints with the geographic concentration). The conduct flag is set. The fair-lending flag is set on the geographic and BISG signal; the flag is a watch-list flag, not a finding (the finding-grade analysis runs in `fair-lending-test-plan`).

**Root-cause hypotheses.** For THEME-MTG-LM-LOST-01: (1) the loss-mit-package intake workflow has a document-receipt logging gap that under-counts received documents in the consumer's file; (2) the team handling loss-mit packages in the three concentrated MSAs has a different workflow than the firm-wide standard (an intake-team-level practice variation); (3) the document-imaging vendor used for loss-mit packages has performance issues on certain document types (HUD-1 forms, hardship letters with non-standard formatting); (4) the geographic concentration may reflect demographic segments with non-standard documentation patterns (less-typical income documentation; informal hardship letters) that the workflow does not handle robustly. Hypothesis (1) is the most-likely operative root cause and is testable from the loss-mit-system audit log; hypothesis (2) is the workforce-level explanation and is testable from a workflow audit in the three MSAs; hypothesis (4) is the fair-lending-relevant alternative that requires the `fair-lending-test-plan` analysis to evaluate.

**Regulatory exposure.** For THEME-MTG-LM-LOST-01: Reg X §1024.41 (loss-mit procedures, including the duplicate-application provisions and the time-limit framework that the repeat-clock-reset pattern arguably evades); Reg X §1024.39 (early intervention requirements); Reg X §1024.40 (continuity of contact, where the repeat-loss pattern reflects a continuity gap); UDAAP §1031 unfairness (substantial injury through repeated loss-mit denials, not reasonably avoidable by the borrower because the borrower cannot verify document receipt independently); ECOA / Reg B §1002.4 prohibition on discrimination in any aspect of a credit transaction (loss-mit is part of the credit transaction); FHA prohibition on discrimination in residential real-estate-related transactions including servicing; potential disparate-impact theory under HUD's discriminatory-effects standard at 24 CFR §100.500 [verify].

**Conduct-risk implications.** Per theme; conduct overlay loads. THEME-MTG-LM-LOST-01 ties to: product-design (the loss-mit intake workflow); customer-outcome (the borrower's ability to access loss-mit relief is the consumer-outcome at issue); complaint-linkage (the theme has been a leading indicator for two prior quarters at lower share levels and was not escalated); vendor-or-third-party (if hypothesis (3) is operative; the document-imaging vendor is in path); and incentives (the loss-mit-team production metrics may incentivise speed at the expense of accuracy). Conduct-accountable manager: head of mortgage servicing (per the firm's conduct framework). Conduct committee read: yes. Conduct-event candidate: yes.

**Trends and movements.** THEME-MTG-LM-LOST-01 trend up materially (9 percent to 18 percent share); rate per loss-mit-eligible borrower also moved up in the same period, supporting the share movement as a real signal. THEME-MTG-PAY-APP-03 trend up modestly. Other themes flat. Seasonality treatment: loss-mit complaints typically peak in Q1 (post-holiday financial stress); the 12-month framing absorbs the seasonality. Product / campaign timeline: no in-period mortgage-servicing process changes identified that would account for the spike on THEME-MTG-LM-LOST-01.

**Recommended actions.** For THEME-MTG-LM-LOST-01: (1) loss-mit-system audit log review for the three concentrated MSAs (owner: head of mortgage servicing; due date: 30 days; accountable forum: consumer compliance committee); (2) workflow audit in the three MSAs to identify the practice variation hypothesis (owner: head of mortgage servicing operations; due date: 60 days; accountable forum: consumer compliance committee); (3) fair-lending escalation to `fair-lending-test-plan` for finding-grade analysis on the geographic and demographic concentration (owner: head of fair lending; due date: in the next fair-lending committee cycle; accountable forum: fair-lending committee); (4) UDAAP risk re-rating on the loss-mit conduct pattern (chain to `udaap-risk-review`; owner: head of consumer compliance; due date: in this committee cycle; accountable forum: consumer compliance committee); (5) document-imaging vendor performance review (owner: head of vendor management; due date: 60 days; accountable forum: vendor risk committee); (6) interim consumer-redress consideration for the borrowers in the three MSAs whose loss-mit clock was reset multiple times (counsel-directed; owner: counsel; due date: pending counsel; accountable forum: counsel and consumer compliance committee); (7) complaint-monitoring loop closure with quarterly read to the conduct committee until the share returns to the prior baseline plus a sustained period.

**Open questions and dissent.** Whether the fair-lending flag should be elevated to a finding-grade conclusion this cycle (the second-line view is no, run the finding-grade analysis through `fair-lending-test-plan` first; counsel may direct otherwise). Whether interim consumer-redress should begin before the workflow audit completes (counsel-directed; the urgency of the loss-mit clock-reset harm argues for action before full root-cause confirmation). Whether the geographic concentration warrants a HUD or DOJ self-reporting consideration (counsel to direct).

**Source trace and confidence.** Material claims cite sources from `references/source-anchors.md` and the loaded banking and conduct overlays by file path. Confidence label: high on the count-share-and-rate analysis with the per-MSA concentration; medium on the root-cause hypotheses (multiple plausible hypotheses; system audit and workflow audit needed to discriminate); medium on the demographic-skew read (BISG plus HMDA-aggregate context; BISG is a signal, not a finding, and the finding-grade analysis runs through `fair-lending-test-plan`); high on the regulatory-exposure mapping; high on the cross-skill chain to `fair-lending-test-plan` and `udaap-risk-review`.

#### What this delivers and does not deliver

The delivery operationalises the post-cluster review on a mortgage servicer's loss-mit complaint pattern: theme aggregation table (Excel) plus memo (Word). The consumer compliance committee acts on the recommended actions; the fair-lending committee receives the cross-skill handoff for finding-grade analysis; counsel directs on interim consumer-redress and self-reporting questions; the conduct committee receives a read.

The memo does not finalise a fair-lending finding (the BISG-plus-geographic signal is flag-grade evidence; the finding-grade work runs through `fair-lending-test-plan`). It does not finalise a UDAAP determination (chain to `udaap-risk-review` for element-by-element analysis on the loss-mit pattern). It does not execute consumer redress (counsel directs; operations executes; the memo recommends consideration). It does not take action on individual complaints (those run through the case-management workflow).

The geographic concentration plus BISG signal is the pattern that triggers the fair-lending escalation chain; the memo is explicit that BISG is signal, not proof, and that the finding-grade analysis happens in the fair-lending workstream. The repeat-loss pattern under Reg X §1024.41 is the regulatory-exposure spine; the memo treats the Reg X compliance check and the UDAAP unfairness analysis as parallel inquiries, not substitutes.

Pattern derived from public CFPB enforcement actions and Supervisory Highlights themes on mortgage-servicing loss-mit conduct; the geographic-concentration-plus-BISG fact pattern is a public-source-derived structural pattern, not a specific firm. The example surfaces the discipline of carrying both per-MSA share comparison and rate per loss-mit-eligible borrower; per-MSA share alone is exposure-confounded.

## troubleshooting

### Troubleshooting: complaint-theme-analysis

Recurring failure modes when a complaint-theme analysis looks complete but is not. The drafter should preempt these; the decision-forum reviewer (consumer compliance committee, conduct committee, head of fair lending, CCO, counsel) should catch the rest.

#### Counts at the bureau's sub-issue grain instead of at the theme grain

Symptom: the matrix has rows that mirror the CFPB sub-issue taxonomy. The "themes" are "Problem with a credit reporting company's investigation into an existing problem" or "Trouble during payment process" with no firm-taxonomy theme overlay.

Why it happens: it is the path of least resistance from the public extract. The drafter pulled the bureau's sub-issue facets and called them themes.

Fix: themes are firm-taxonomy themes, mapped to but not equal to the bureau's coding. Two distinct root causes can map to the same sub-issue; one root cause can split across sub-issues. The taxonomy version is named in the memo; the mapping is filed for reproducibility.

#### Confirmation-bias theme inflation

Symptom: the top theme is the theme the head of consumer compliance brought into the room. The drafter read 50 narratives, all of which seemed to confirm the theme, and wrote the matrix from those.

Why it happens: confirmation bias under time pressure. Reading narratives is the most-engaging part of the work; reading the entire population through a coding rule is the least.

Fix: theming method is pre-registered in the memo. The coding rule is applied to the entire sample, not just the narratives the drafter read. The method's coding agreement is reported (dual-read on a sample). Where the method has been adapted mid-review, the adaptation is named.

#### CFPB Complaint Database treated as the firm's full complaint surface

Symptom: the matrix counts come entirely from the public CFPB Complaint Database extract; the firm's internal complaint records are not consulted.

Why it happens: the public extract is easy to pull; the firm-internal channels require the complaint-management system access.

Fix: the scope-and-population section enumerates every channel reviewed and explicitly states channels excluded. The CFPB-portal subset is one channel; the firm-direct call-center, web-form, branch-escalation, and executive-resolution channels typically dwarf it. App-store reviews, social-listening signals, state-AG referrals, and employee-escalation logs are separate channels. The memo names what was pulled and what was not.

#### Counting inflation from CFPB-portal-and-firm-direct double counting

Symptom: the matrix totals exceed the firm's true complaint count for the period because CFPB-portal complaints are counted both in the public-extract pull and in the firm-internal records.

Why it happens: the CFPB-portal complaints arrive in the firm's complaint-management system through the bureau's company portal; if the deduplication is not done, both pulls capture the same complaint event.

Fix: deduplication is named in the theming-method section. The match key (consumer ID where consent-flag permits; or a composite of date, product, sub-issue, and ZIP3) is documented. Where deduplication is incomplete, the memo carries the residual-overlap estimate.

#### Apparent spike that is volume-driven, not rate-driven

Symptom: a theme moves from 8 percent to 18 percent of period complaints; the memo reports the share movement as a real signal. The firm's relevant denominator (new-account openings; loss-mit-eligible borrowers; active P2P users) doubled in the period because of a campaign or a launch.

Why it happens: the drafter computed share but not rate. Volume-driven share movements are misread as substantive theme spikes.

Fix: the rate framing accompanies the share framing where the data permits. The denominator is named (e.g., per 1,000 new accounts; per 1,000 loss-mit-eligible borrowers; per 1,000 active users). Where the denominator is unavailable, the share movement is read against the relevant volume movement and the dependence is named.

#### BISG signal asserted as protected-class evidence

Symptom: the matrix has `fair_lending_flag: true` on a theme with a BISG-derived demographic-skew read; the memo treats the BISG signal as evidence of disparate impact.

Why it happens: BISG is a probabilistic estimate, not a measurement. Drafters under time pressure conflate the signal with the finding.

Fix: BISG is signal, not proof. The fair-lending flag is a flag-grade signal that feeds the cross-skill chain into `fair-lending-test-plan` for finding-grade analysis. The matrix's `signal_grade` column carries `flag` or `watch-list`, not finding. For mortgage themes, HMDA self-reported demographics are the operative source where available; BISG is supplemental.

#### Trend movement not cross-walked against product or campaign timeline

Symptom: a theme spikes in the period; the memo reports the spike but does not name what changed in the product, marketing, or process timeline that would account for it.

Why it happens: the drafter ran the theme analysis without consulting the product-change log or the marketing-campaign calendar.

Fix: the trends-and-movements section cross-walks the theme movement against the product / campaign / process-change timeline. Apparent theme spikes that align with a launch or a campaign are called out and the timing relationship is named explicitly. Where no in-period change accounts for the spike, that absence is also noted.

#### Recommended actions read as generic policy advice

Symptom: the recommended-actions block lists items like "review the theme", "consider remediation", "engage the marketing team" without owners, due dates, named controls, or accountable forums.

Why it happens: the drafter wrote the actions in advisory voice rather than as a structured set of recommendations the decision-forum acts on.

Fix: each action names the specific intervention, the owner role, the due date, the named control to be modified or instituted, and the accountable forum. "Update the post-click landing page on the December rewards-bonus campaign to surface the FX-fee disclosure above the fold on mobile by [date], owned by the head of card marketing, with the marketing review committee as the accountable forum and the consumer compliance committee taking a read" is an action. "Review the marketing" is not.

#### Conduct overlay treated as a checklist

Symptom: the conduct-risk implications block lists the conduct-risk taxonomy categories as a generic checklist with no per-theme narrative; the conduct-accountable manager role is unfilled; the conduct-event candidate flag is missing.

Why it happens: the drafter consumed the conduct overlay as a checklist rather than as the substantive overlay the conduct framework expects.

Fix: conduct overlay is mandatory on this skill. Per top theme, the taxonomy tie-back is populated, the conduct-accountable manager role is named (a role under SMCR or the firm's conduct framework, distinct from the decision forum), the conduct-event candidate flag carries a recommendation, and the complaint-monitoring loop closure is specified.

#### Complaint-monitoring loop closure absent

Symptom: the recommended actions are well-specified but no post-action monitoring posture is named for any theme.

Why it happens: the drafter treated the memo as the work product itself rather than as the input to the conduct function's ongoing surveillance.

Fix: per top theme, the loop closure is named: which complaint codes the firm watches for re-emergence, the cadence of the read, the threshold for off-cycle re-review, the escalation trigger if the theme persists. Theme analysis without loop closure is incomplete.

#### Skill produces a UDAAP determination or fair-lending finding

Symptom: the memo concludes that a UDAAP violation has occurred or that disparate impact has been established. Or the memo concludes that no violation or disparate impact is present.

Why it happens: the drafter conflated the theme analysis with the determination. Theme analysis surfaces signal; the determinations live in `udaap-risk-review` and `fair-lending-test-plan` and ultimately in counsel and the decision forums.

Fix: the memo states the regulatory exposure (the citations the theme touches) and the recommended cross-skill chain (e.g., escalate to `udaap-risk-review` for element-by-element analysis). It does not declare a final UDAAP determination or a fair-lending finding. The guardrail in the SKILL.md frontmatter is reflected in the memo's status line and in the recommended-actions framing.

#### App-store reviews excluded for fintech themes

Symptom: a payments-fintech complaint-theme analysis pulls only the CFPB-portal extract and the firm-internal records; the app-store review channel is omitted entirely.

Why it happens: app-store reviews "are not complaints" in the firm's complaint-management taxonomy; they live in the marketing or product team.

Fix: for payments-fintech, app-store reviews are a meaningful complaint channel and the payments-fintech sector overlay flags them as such. The memo includes the app-store review pull (with the volume-bias caveat) or names the channel as excluded with a rationale.

#### State-AG channel pulled mechanically across all states

Symptom: the memo pulls state-AG referrals from every state where the firm operates, treating all states as equivalent.

Why it happens: defensive completeness. The drafter pulled everything that was pullable.

Fix: state-AG channels are pulled selectively based on the firm's footprint depth in the state, the state-AG's known focal areas, and the firm's routing relationship with the state-AG offices. The memo names the states pulled and the rationale; the states excluded are also named.

#### Severity rating without the rubric

Symptom: severities are assigned ("high", "medium") with no per-theme rationale and no rubric reference; the rubric is not stated in the memo.

Why it happens: severity drift is the canonical failure mode. Drafters set severity by feel.

Fix: the rubric is stated once in the memo (Critical / High / Medium / Low with explicit definitions). Each theme carries a per-theme `severity_rationale` referencing the rubric. Where multiple themes share a severity, each carries its own rationale.

#### AI-flagged themes do not feed the cross-skill chain

Symptom: a theme touches algorithmic decisioning, AI agents, or AI-generated communication; `ai_flag: true` is set on the matrix; no cross-skill chain into `adverse-action-review`, `udaap-risk-review`, or `fair-lending-test-plan` is named.

Why it happens: the drafter set the flag mechanically without considering the implications.

Fix: AI-flagged themes feed at least one cross-skill chain. AAN-content themes chain to `adverse-action-review`; algorithmic-outcome themes chain to `udaap-risk-review`; protected-class-disparity themes chain to `fair-lending-test-plan`. The April 2023 Joint Statement and CFPB Circulars 2022-03 and 2023-03 are cited where applicable.

#### Source trace and confidence label absent

Symptom: the memo cites no sources for material claims. Theme severity, regulatory exposure citations, and root-cause hypotheses appear without supporting references.

Why it happens: the drafter borrowed from prior memos without recording the source.

Fix: every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by file path. Source evidence (transaction data, complaint records), management assertions (first-line root-cause hypotheses), public-source obligations (regulatory anchors), generated inferences (the second-line's read of the pattern), and open legal questions stay distinguishable. The confidence label per major analytical claim reflects how well the memo supports the recommended actions.

#### Sponsor-bank-fintech theme attribution unclear

Symptom: the memo covers a sponsor-bank-fintech program; themes are reported with no attribution between the bank, the fintech, and the program-agreement allocation.

Why it happens: the drafter is operating from one entity's perspective and treats the other as administrative.

Fix: per theme, the attribution names which entity holds the consumer-facing relationship, which entity owns the product / marketing / fee design at issue, and which entity owns the disclosure. The cross-skill chain into `udaap-risk-review` or `marketing-claim-review` names the bank as the accountable party per the interagency third-party guidance.

#### Insurance-side theme analysed under CFPB framework

Symptom: the memo themes insurance underwriting, pricing, or claims-handling complaints under the UDAAP framework.

Why it happens: the drafter loaded the wrong sector overlay or did not load the insurance overlay.

Fix: route to the state-DOI / NAIC framework per the insurance sector overlay. The narrow exception is bank-affiliated credit-protection insurance bundled with credit, where the credit-side runs under the consumer-finance framework and the insurance-side runs under the state-DOI framework; the memo carries both reads.
