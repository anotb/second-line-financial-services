---
name: complaint-theme-analysis
description: "Theme a population of consumer complaints and flag root causes and regulatory risk."
argument-hint: "[complaint-data extract or pointer, period, source channels, product or business in scope; or trigger event (regulator inquiry, peer enforcement) and scope]"
---

# Complaint-theme analysis

A complaint-themes pack is what the second-line consumer-compliance team produces so the consumer compliance committee, the conduct committee, and (where the themes warrant escalation) the head of fair lending, the CCO, and counsel can read the population. The work is pulling complaints from every channel that carries signal, theming them under a firm taxonomy, computing share and rate and trend, severity-rating the themes against a stated rubric, naming root-cause hypotheses, mapping regulatory exposure, recording the conduct-risk implications, and recommending actions with owners and forums. The skill stops at recommendations and at the cross-skill handoff. The decision-makers decide.

The delivery is two artifacts. The theme matrix is the structured aggregation, rendered as an Excel workbook via the `xlsx` skill in the `document-skills` plugin. The memo is the narrative analysis, rendered as a Word document via the `docx` skill. The matrix is the data layer the committee scans; the memo is the analytical layer the committee reads. Both emit together; the committee acts on the memo, the conduct function consumes the matrix for ongoing surveillance.

The skill serves both lenses. A 1.5-line complaint-management lead inside the business uses it to consolidate the periodic theme pack; a 2-line independent reviewer or conduct-risk officer uses the same skill to challenge the pack and to surface the themes that the first-line did not name honestly. The seam between the two is the theming method (pre-registered, applied to the full sample, dual-read agreement reported), the root-cause-hypothesis discipline (hypotheses are hypotheses until tested), and the demographic-skew read (BISG signal flags watch-list status, not finding-grade evidence).

## When to use

Aggregates and themes a population of consumer complaints (CFPB Complaint Database extracts, internal complaint-management records, app-store reviews, social signals, state-AG referrals, employee escalations) into named themes with severity, root-cause hypotheses, regulatory exposure mapping, and trended movements. Produces two artifacts: an Excel theme-aggregation matrix and a Word memo with the narrative analysis. Themes (not individual complaints) are the unit of analysis. The skill surfaces signal for the consumer compliance committee, the conduct committee, and the cross-skill chain into UDAAP, fair-lending, and adverse-action review; it does not finalise UDAAP determinations, fair-lending findings, or actions on individual complaints.

Best for:
- Quarterly or monthly complaint-themes pack to the consumer compliance committee, conduct committee, or risk committee.
- Pre-exam preparation: re-running the firm's last 12 to 24 months of CFPB Complaint Database public data (and the firm-internal channels) against the current product set to triangulate likely examiner focus areas.
- Triage after a regulator inquiry or a peer enforcement action on a specific product, to scope the population and trend at the firm.
- Input to `udaap-risk-review` or `fair-lending-test-plan` when a theme suggests a specific product, fee, flow, or geographic concentration warrants element-by-element or finding-grade analysis.
- Annual conduct-risk surveillance pack where complaint themes are the canonical signal feeding the conduct framework.

Not the right tool when:
- The question is one specific complaint disposition (use the firm's complaint case-management workflow).
- The question is whether one marketing claim is misleading (use `marketing-claim-review`).
- The question is statistical fair-lending testing on outcomes data (use `fair-lending-test-plan`; this skill flags, that skill finds).
- The question is element-by-element UDAAP analysis on a specific product, fee, or flow (use `udaap-risk-review`; this skill themes the population, that skill tests the elements).
- The question is the firm's overall CMS or compliance-program quality (use the broader compliance-testing or risk-compliance-core skills).

## Ask yourself first

Most of what the analysis needs is on the table by the time someone reaches for this skill. A few things to settle before drafting:

- What triggered the analysis. Routine cycle (monthly, quarterly, annual), pre-exam preparation, regulator-inquiry triage, peer-enforcement parallel, post-incident review, or a specific cluster surfaced in monitoring. Trigger drives scope (period, channels, product perimeter), severity weighting, and which downstream forums the pack lands at.
- Who reads the pack. Consumer compliance committee at routine cycle; conduct committee on the conduct overlay (mandatory); fair-lending committee on themes with `fair_lending_flag` set; counsel where regulatory engagement is in posture. Audience drives memo depth and the privilege framing.
- Which complaint channels are in scope. CFPB Complaint Database public extract; firm-direct (call center, web form, branch escalation, executive resolution); CFPB-portal complaints routed through the bureau's company portal (deduplicated against firm-direct); app-store reviews on consumer-facing apps; social-listening signals; state-AG referrals; employee-escalation log; HUD HOPE Hotline forwards (mortgage). The CFPB-portal subset is one channel, not the firm's full complaint surface; channels excluded carry rationale.
- What the period and the comparison period are. Monthly, quarterly, 12-month rolling, or trigger-defined. The comparison period drives the trend treatment; a comparison period that overlaps a product launch or campaign needs the volume-vs-rate cross-walk.
- Which products and channels in the firm's perimeter are in scope. The full perimeter, a single product line, a sponsor-bank-fintech program subset, or a specific geography. Multi-product packs split into per-product matrix sheets.
- What the source posture is. Public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, or connector-aware. Source posture sets which channels can be pulled and which carry `[evidence needed]`. A public-only theme pack reads against the CFPB Complaint Database extract and the firm's public disclosures; a connector-aware pack pulls the firm's complaint-management system directly.

When `scope` is supplied, the skill consumes it for institution, persona, source posture, sector overlay set, and cross-cutting overlay set. Otherwise it asks the practitioner the few facts it needs and defaults to public posture if the practitioner declines, noting in the memo that scope was not formalised.

## How the analysis gets built

The analysis has the same spine across product lines, sectors, and triggers. A senior practitioner walks it roughly in the order below, but the conversation surfaces sections in whatever order the channels arrive and the firm-internal taxonomy permits; the matrix and memo sort themselves once the theming is done.

**Scope and population.** The scope-and-population section enumerates every channel reviewed and every channel excluded with rationale. The total deduplicated unique complaint events for the period is reported; per-channel counts are reported separately so the reader can see the channel mix. The CFPB-portal subset count is named explicitly because regulators read the public-extract subset alongside the firm's pack and inconsistencies surface. Channels excluded carry rationale (e.g., app-store reviews omitted for a portfolio-loan-only mortgage servicer with no consumer-facing app; state-AG referrals omitted in states where the firm has minimal footprint).

**Theming method.** Theming method is the discipline that distinguishes a population analysis from confirmation-bias theme inflation. The method is pre-registered: the firm taxonomy (with version), the active themes plus residual bucket, the per-theme coding rule, and the treatment of complaints that match multiple themes (primary-theme assignment for the count and share; secondary-theme tracking for the analytical narrative). The method is applied to the entire sample, not just the narratives the drafter reads. Coding agreement is reported on a dual-read sample (typically 200 complaints; the agreement percentage is the discipline check). Where the method has been adapted mid-review (a coding-rule clarification), the adaptation is named. The taxonomy mapping document is filed for reproducibility.

The bureau's product / sub-product / issue / sub-issue taxonomy is not a root-cause taxonomy; it is the bureau's complaint-coding taxonomy. The firm taxonomy maps to but does not equal the bureau's. Two distinct root causes can map to the same bureau sub-issue; one root cause can split across sub-issues. The mapping is documented; the theming runs on the firm taxonomy.

**Top themes with definitions, counts, share, rate, and trend.** Per top theme, the matrix carries the count, the share of period total, the prior-period share, the trend enum (`up` / `down` / `flat` / `new`), and where the relevant denominator permits, the rate per appropriate denominator (per 1,000 new accounts; per 1,000 loss-mit-eligible borrowers; per 1,000 active users). The rate framing accompanies the share framing where the firm has the denominator data because volume-driven share movements are misread as substantive theme spikes; the rate framing controls for the volume effect.

Denominator and confidence discipline matters here. A complaint count without a denominator is a number, not a rate; share-of-period figures without comparable prior-period denominators mislead the trend read. Where the firm has the denominator data (active accounts, originations, eligible borrower population), use it; where the firm only has the public CFPB Complaint Database extract (no denominator), say so and flag every theme as `signal-without-rate`. Per-theme confidence is reported alongside the count: `high` (firm-internal data, complete period, denominator available), `medium` (firm-internal data, period bounded or denominator partial), `low` (public extract only, no denominator, theme is flag-only), `unknown` (data quality not yet assessed). A pack that reports rates without confidence is a pack that misleads the committee on what the numbers actually support.

The product / campaign / process-change timeline is cross-walked against the trend movements. Apparent theme spikes that align with a launch or a campaign are called out; the timing relationship is named explicitly. Where no in-period change accounts for a spike, that absence is also noted.

**Severity rubric and per-theme severity.** The rubric is stated once in the memo and applied per theme:

- *Critical* — theme matches a public CFPB enforcement focal item directly; material population; ongoing harm; remediation cannot wait for the next committee cycle.
- *High* — theme matches a Supervisory Highlights focal item or a peer enforcement theme; meaningful population; remediation needed within this committee cycle.
- *Medium* — real theme; population bounded or uncertain; remediation enters the controls roadmap.
- *Low* — theme present but population small or driven by isolated process defects.

Per-theme `severity_rationale` carries the reasoning. Severity drift is the canonical failure mode on this skill; the rubric is named and the rationale is mandatory per theme.

**Root-cause hypotheses per theme.** Per theme, the memo names the hypotheses the second-line is carrying for the underlying conduct: process-side hypotheses (workflow gap; document-receipt logging; intake-team practice variation); product-side hypotheses (fee architecture; disclosure-path design; default-state design); marketing-side hypotheses (campaign messaging; channel-distribution mismatch); incentive-side hypotheses (compensation design; KPI architecture); vendor-side hypotheses (third-party processor; document-imaging vendor; sponsor-bank attribution); and (where relevant) demographic-segment hypotheses (the documentation-pattern mismatch; the language-access mismatch; the digital-literacy mismatch).

Hypotheses are stated as hypotheses, not conclusions. The matrix carries each hypothesis with a `tested` flag (`tested-supported`, `tested-rejected`, `untested`) and a pointer to the evidence that would discriminate. The theme analysis surfaces signal; root-cause confirmation runs on experiments after the committee acts.

**Regulatory exposure mapping per theme.** Per theme, the matrix lists the regulatory citations the theme touches with the operative section. Common citations: UDAAP §1031 elements (deception, unfairness, abusiveness); Reg Z disclosure provisions (per the operative section); Reg E §1005.11 (P2P and instant-payment themes); Reg X §1024 Subpart C (mortgage-servicing themes); Reg B §1002.9 (AAN-content themes); FCRA §1681s-2 / Reg V §1022.74 (furnisher-conduct themes); FHA / ECOA disparate-impact theory (themes with fair-lending flag); CFPB Circulars on specific fee mechanics (overdraft, NSF, account reopening, AAN with complex algorithms); CFPB Supervisory Highlights focal items at memo date; sector-specific authorities loaded by the relevant sector overlay (FINRA Rules 4513 / 4530 for retail brokerage; NAIC Model Acts for insurance).

The exposure mapping is signal-grade across-the-citation, not finding-grade per-citation. The memo cites the section; the cross-skill chain into `udaap-risk-review` or `fair-lending-test-plan` carries the element-by-element or finding-grade analysis.

**Conduct-risk implications per theme.** Loaded as the mandatory cross-cutting overlay on this skill. Per top theme, the memo records the conduct-risk taxonomy tie-back (incentives, product design, communication, sales practices, customer outcome, complaint linkage, vendor or third-party, AI / algorithmic surface); the named conduct-accountable manager role (a role under SMCR or the firm's conduct framework, distinct from the decision forum); whether the conduct committee receives a read; whether the theme is a conduct-event candidate (recommendation only; the conduct-risk function classifies); the customer-outcome segments affected (policy-relevant segments under the conduct framework, supplementing or replacing the protected-class lens); the regulator-engagement trigger (where the theme is in scope because of a regulator inquiry); and the complaint-monitoring loop closure (which complaint codes the firm watches post-action, the cadence of the read, the escalation trigger if the theme persists).

Theme analysis without loop closure is incomplete; the conduct function consumes the loop-closure instruction.

**Demographic-skew read where present.** Per theme, the matrix carries the demographic-skew read: state and ZIP3 distribution; per-MSA share against the baseline; BISG-derived signal where the data permits; HMDA self-reported demographics where available (mortgage themes); the signal grade (`flag`, `watch-list`, `no-signal`). For mortgage themes, HMDA is the operative source; for non-mortgage consumer credit, BISG is the supplemental signal. BISG is signal, not proof; the fair-lending finding-grade analysis runs through `fair-lending-test-plan`. The matrix `fair_lending_flag` is set when the geographic or demographic concentration plus the regulatory-exposure intersection warrants the cross-skill chain; the flag is a flag, not a finding.

**Trends and movements.** Period-over-period movements per theme. Seasonality treatment is named where applicable (e.g., loss-mit complaints peak in Q1 post-holiday financial stress; the 12-month rolling framing absorbs the seasonality). The product / campaign / process-change timeline is the cross-walk; the rate framing is the volume-vs-rate discipline check.

**Recommended actions per theme.** Per top theme, the matrix carries the recommended-actions list: the action; the type (control change, policy change, disclosure change, marketing review, UDAAP escalation, fair-lending escalation, vendor review, monitoring uplift, consumer-redress consideration, training, other); the owner role; the due date; the named control (the control to be modified or instituted); the accountable forum. Each action is specific and verifiable; generic advice is reviewer-flagged.

The cross-skill chain is named per theme: `udaap-risk-review` for themes warranting element-by-element analysis; `fair-lending-test-plan` for themes with fair-lending flag set; `marketing-claim-review` for themes traced to a marketing asset; `adverse-action-review` for themes touching AAN content or reason coding.

**Open questions and dissent.** Items deferred to counsel; items where the second-line view and the first-line view diverge; items flagged for the next-period retest. Privilege posture is named where the theme analysis is responding to a regulator engagement or where the recommended actions trigger a regulatory-notification consideration.

**Source trace and confidence.** Material claims cite sources from `references/source-anchors.md` and the loaded sector and conduct overlays by file path. Source evidence (transaction data, complaint records), management assertions (first-line root-cause hypotheses), public-source obligations (regulatory anchors), generated inferences (the second-line's read of the pattern), and open legal questions stay distinguishable. Confidence labels are reported per major analytical claim (count-share-and-rate analysis; root-cause hypotheses; demographic-skew read; regulatory-exposure mapping; cross-skill chain).

### AI / algorithmic-surface overlay

When complaint themes touch algorithmic decisioning, AI agents, AI-generated communications, AI-driven personalisation, or dynamic-disclosure surfaces, the AI overlay fires inside the named sections rather than as a separate document:

- *Theme matrix:* the `ai_flag` is set per theme. The cross-skill chain is named (AAN-content themes chain to `adverse-action-review`; algorithmic-outcome themes chain to `udaap-risk-review`; protected-class-disparity themes chain to `fair-lending-test-plan`).
- *Regulatory exposure:* the April 2023 Joint Statement is cited on the AI-flagged themes; CFPB Circulars 2022-03 and 2023-03 are cited where AAN content is touched; the bureau's existing UDAAP and ECOA authority reaches algorithmic outcomes.
- *Conduct overlay:* dark-pattern frames are loaded for AI-mediated friction, AI-driven retention urgency, AI-personalised disclosure variability, and AI-agent escalation friction.
- *Source-trace:* AI-driven complaint signals from conversational-AI transcript logs are an evidence source distinct from human-call recordings; the source type is named.

The overlay is mandatory once triggered. Missing the AI handling on themes where AI is in path is what the second-line reviewer or the conduct-risk lead flags first.

### Sector overlays

When the scope names a sector, load the matching `references/sector-overlays/<sector>.md`:

- *Banking* — depository-specific theme catalogue (overdraft, NSF, deposit-fee, mortgage-servicing, credit-card, indirect auto, HELOC); CFPB Complaint Database scope and limits; bank-size-and-CFPB-authority framing; sponsor-bank attribution; mortgage-servicing rules intersection (Reg X / Reg Z); CRA and HMDA cross-walk for mortgage and small-business themes.
- *Payments-fintech* — P2P / BNPL / neobank theme catalogue; app-store reviews as a non-CFPB complaint channel; sponsor-bank attribution per theme; Reg E §1005.11 error-resolution framework; junk-fee theme intersection; AI-agent and AI-generated-communication themes; payments-fintech evidence sources.
- *Capital-markets* — scope boundary first (FINRA Rule 4513 / 4530 framing; Reg BI / IA fiduciary substantive regime; not CFPB-jurisdictional); recurring retail-brokerage theme catalogue; FINRA-reportable theme intersection; SEC Whistleblower tip-grade routing; SBL credit-side intersection.
- *Insurance* — scope boundary first (state-DOI / NAIC framework; not CFPB-jurisdictional); recurring insurance theme catalogue; NAIC framework regulatory exposure mapping (Models #880 and #900); state-DOI complaint portals and NAIC CDS; MGA / MGU and program-business attribution; bundled credit-protection insurance as the narrow CFPB intersection.

### Cross-cutting overlays

Conduct overlay is mandatory on this skill. Complaints are the canonical conduct-risk surveillance signal in US consumer financial services; the overlay loads on every invocation. Privacy is not primary on this skill (privacy themes appear in the population but the privacy review framework is downstream). Cyber not primary (cyber-incident-related themes route to the firm's incident-response workflow). Climate not applicable.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/banking.md`, `payments-fintech.md`, `capital-markets.md`, `insurance.md` — sector-specific framing loaded per scope.
- `references/cross-cutting/conduct.md` — conduct overlay (mandatory on this skill).
- `references/firm-overlay.md` — firm-installed taxonomy (active themes, coding rules, taxonomy version), named committees, conduct-event taxonomy, complaint-system path, denominator data sources (consumed when present).
- `templates/default-output.md` — content spec for the theme matrix (Excel) and the narrative memo (Word).
- `examples/credit-card-fee-disclosure-quarterly.md`, `examples/mortgage-servicing-loss-mit-cluster.md` — public-source-derived worked examples.
- `TROUBLESHOOTING.md` — recurring failure modes the drafter should preempt and the reviewer should catch.

## Output

Two artifacts emit together. The theme matrix renders as an Excel workbook via the `xlsx` skill in the `document-skills` plugin: Sheet 1 is the headline theme summary; Sheets 2 through 6 carry per-theme regulatory exposure, root-cause hypotheses, recommended actions, demographic skew, and source trace. The memo renders as a Word document via the `docx` skill, following the named sections in `templates/default-output.md`. The consumer compliance committee acts on the memo; the conduct committee receives a read; the cross-skill chain into `udaap-risk-review`, `fair-lending-test-plan`, `marketing-claim-review`, or `adverse-action-review` is named per theme; the conduct function consumes the matrix for ongoing surveillance and complaint-monitoring loop closure.

The skill stops at recommendations and at the cross-skill handoff. It does not approve loans, deny adverse-action notices, finalise UDAAP determinations, finalise fair-lending findings, take action on individual complaints, or execute consumer redress. Themes are the population-scale signal for human decision by qualified compliance, fair-lending, conduct, legal, and product reviewers.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
