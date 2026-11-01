# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## asset-manager-annual

### Example: annual adviser risk committee pack at a registered investment adviser

Public-source-derived. No named institution. The shape mirrors the standing annual cycle at a large SEC-registered investment adviser with a broker-dealer affiliate. The adviser-level risk committee (CRO function) is distinct from the fund boards; this pack is for the adviser, not the funds.

#### Input

- Institution: large RIA with an affiliated broker-dealer; complex registered fund complex; significant separately-managed account business.
- Engagement scope supplied: primary regulators SEC (Investment Management, Trading and Markets) and FINRA; persona = head of risk reporting, second line, reporting to the CRO; sector overlay = capital-markets; cross-cutting overlays = cyber (because of SEC cyber disclosure obligations on the public parent and Reg S-P amendments touching adviser and fund records); climate not loaded (not material at the adviser-firm level for this period); source posture = public-plus-firm-policy-plus-system-of-record-evidence.
- Period: full year; annual standing meeting of the adviser-level Enterprise Risk Committee.
- Upstream artifacts on file: adviser-level KRI feed (18 metrics across investment risk, operational risk, technology, vendor, regulatory, conduct, financial crime, cyber, fiduciary); the open-issues register from internal audit and the affiliated BD compliance function; the loss-event log; the firm's risk appetite statement (15 metrics); the latest cyber tabletop results; one Form PF current-event filing in the period; one BD net-capital headroom alert (within tolerance, no breach).

#### Output sketch

- **Cover and decision items requested** — meeting date, committee = Adviser Enterprise Risk Committee (distinct from fund boards), period = full year, classification = internal. Two decisions: (i) approval of the refreshed adviser RAS for the next cycle, including a new RAS metric on cyber tabletop success rate; (ii) acknowledgement of the Form PF current-event filing posture and the proposed forward escalation path.
- **CRO summary** — five bullets. Headline: risk profile stable across most types; cyber elevated due to threat-environment shift not firm-specific incidents; vendor concentration narrowing on a single trade-execution vendor flagged as elevated and deteriorating; one Form PF current-event filing during the period; BD net capital headroom adequate.
- **Heat map by risk type** — adviser-level taxonomy: investment, operational, technology, vendor, regulatory, conduct, financial-crime, cyber, fiduciary. Climate not separately rated this period; rationale documented (climate is not material at the adviser-firm level given product mix). Each cell carries current/prior/direction.
- **Top risks** — five named risks. Trade-execution vendor concentration; cyber threat environment with named impact pathway through the SaaS portfolio-management platform; Form PF current-event reporting accuracy and timeliness; fiduciary risk on best-execution evidence; regulatory risk around SEC cyber disclosure rule applicability to the public parent (Item 1.05 / Item 106 mechanics) and Reg S-P May 2024 amendments compliance posture.
- **Material risk events** — Form PF current-event filing logged with date, type, status = closed; one near-miss on the order-management system (failed-trade detection caught within tolerance); one regulatory-action item (FINRA inquiry not yet at exam stage).
- **KRI movement and breaches** — 18 KRIs with prior, current, threshold, RAG, commentary. Two RED breaches (vendor-concentration on trade execution; cyber phishing-click rate). One AMBER. The three over-threshold KRIs each have commentary from `kri-commentary`.
- **Risk appetite status** — 15 RAS metrics. One breach (vendor concentration), one at-trigger (cyber phishing). Ladder-to-operating-limit column populated for adviser-firm RAS metrics; the BD net-capital RAS metric ladders to Exchange Act Rule 15c3-1 limits and is reported separately for the BD entity within the adviser group.
- **Issues and remediation status** — open MRAs (0; not a bank), audit issues (9, three over 90 days), regulatory exam findings (2 from the most recent SEC adviser exam, both in remediation), internal high-severity (5).
- **Forward-looking commentary** — named items: SEC cyber disclosure rule applicability and the public parent's Item 1.05 / Item 106 readiness state; Reg S-P May 2024 amendments and the 30-day customer notice posture for individuals reasonably likely to have been affected (compliance dates flagged for verification at write time); SEC proposed Cybersecurity Risk Management Rule for advisers and funds with current state flagged for verification; NYDFS Part 500 amendments effective dates affecting the NY-licensed BD entity; FINRA Rule 4530 reporting items in motion.
- **Climate section** — omitted this period; rationale documented in the appendix.
- **Decision items (full detail)** — both decisions with options, recommended option, requested vote/acknowledgement, owner.
- **Appendices** — data confidence label = high on most KRIs (system-of-record evidence); medium on vendor-concentration KRI (tracker rebuilt this year); BCBS 239 not directly applicable but reference to the firm's internal data-quality framework; source trace; glossary; sign-off block (CRO, committee chair).

The pack stops at draft. The CRO reviews before the committee secretary distributes.

#### Why this scenario matters

- The adviser-level enterprise risk committee is distinct from the fund boards. Items material to the fund board may also be material to the adviser, but the audiences and the recommendations differ; the pack reflects the adviser-firm scope.
- Risk taxonomy is adviser-shaped, not bank-shaped. Investment risk, fiduciary risk, and conduct risk are present. Credit, market, and liquidity in the bank sense are not in the heat map (market risk reads at the portfolio level, owned by investment risk; liquidity reads at the fund level, owned by fund boards).
- BD net capital and customer protection (Exchange Act Rules 15c3-1 and 15c3-3) feed the adviser-group view but are reported separately for the BD entity. The capital-markets sector overlay tells the skill how to surface this.
- Climate is not in scope this period, and the rationale is documented. The skill does not invent a climate cell; the cross-cutting overlay loader respects the scope.
- SEC cyber disclosure rule and Reg S-P amendments are forward-looking items, not in-period events. The forward-looking commentary names them with the verification posture intact.

#### Anchors

- BCBS 239 (January 2013), Principles 7-11 (referenced as a leading-practice anchor for adviser data-quality discipline; not directly binding).
- COSO ERM (2017).
- SEC Investment Advisers Act Rule 206(4)-7 (compliance program).
- SEC cyber disclosure final rule (Release Nos. 33-11216, 34-97989; effective dates phased).
- SEC Reg S-P amendments (final May 16, 2024; phased compliance dates flagged).
- NYDFS 23 NYCRR Part 500 (post-November-2023 amendments).
- Exchange Act Rules 15c3-1 and 15c3-3 (BD net capital and customer protection).

See `references/source-anchors.md` for full citations and verification flags.

## regional-bank-quarterly

### Example: quarterly risk committee pack for a Category III BHC

Public-source-derived. No named institution. Framing patterns from FRB tailoring (12 CFR Part 252), OCC Heightened Standards (12 CFR Part 30 Appendix D), and TCFD (June 2017; October 2021). Climate posture reflects voluntary TCFD-aligned reporting because the parent group reports under EU CSRD; SEC climate rule treated with `[verify current effectiveness]` per the source-anchors discipline.

#### Input

- Institution: Category III bank holding company under the FRB tailoring framework. Mid-cap regional, predominantly commercial and consumer banking, with a small payments-processing subsidiary.
- Engagement scope supplied: primary regulators FRB and OCC; persona = head of risk reporting, second line, reporting to the CRO; sector overlay = banking; cross-cutting overlays = climate, cyber; source posture = public-plus-firm-policy-plus-system-of-record-evidence.
- Period: Q2; standing quarterly risk committee meeting.
- Upstream artifacts on file: 14 KRIs from the upstream feed (three from `kri-commentary` already drafted), the open-issues register from internal audit and regulatory affairs, the loss-event log for the period, the firm's risk appetite statement (22 metrics), the latest BCBS 239 self-assessment, the latest FRB stress test results, and a vendor-outage incident report.
- CRO has flagged operational risk and third-party concentration as deteriorating, model risk as stable but with two open MRAs from the most recent OCC continuous-monitoring letter, and climate as in-scope under TCFD-aligned voluntary disclosure.

#### Output sketch

The skill emits a markdown pack and a structured record. Headlines:

- **Cover and decision items requested** — meeting date, committee = Risk Committee of the Board, period, classification = board-confidential. Two decisions requested up front: (i) extension request on the two model-risk MRAs with a revised remediation date; (ii) approval of a revised RAS metric on third-party concentration.
- **CRO summary** — five bullets in CRO voice. Headline: operational and third-party deteriorating, model stable but MRA load needs decision, climate scenario commentary added per TCFD, RAS within tolerance overall with one trigger-level alert on third-party concentration.
- **Heat map by risk type** — twelve-cell heat map. Operational: elevated, deteriorating, with YTD loss-event count quantified. Third-party: elevated, deteriorating, with concentration headroom narrative. Model: moderate, stable, with the two MRAs flagged. Cyber: moderate, stable. Climate: moderate, stable, narrative-only (no separately-rated cell because climate is reported under strategic with documented rationale per the climate overlay). Credit, market, liquidity, compliance, financial crime, strategic, reputational each carry current/prior/direction.
- **Top risks** — six named risks driving the elevated cells. Each has owner (role, not person), exposure where quantified, key drivers, and linkage to the heat-map cell. Top of the list: vendor-outage exposure in payments processing; concentration on a single sponsor relationship; two model-risk MRAs related to a transaction-monitoring model.
- **Material risk events** — one Tier 1 loss event (vendor outage in payments processing, 12-hour duration, customer-facing), with date, gross and net impact, root-cause summary, status = remediated, linked issue ID. Two near-misses logged but not material individually.
- **KRI movement and breaches** — table of 14 KRIs with prior, current, threshold, RAG, and commentary. Three RED breaches (operational loss, third-party concentration, model-risk MRA aging); one trigger-level alert (cyber phishing-click rate). Each breach commentary cites root cause, owner, and remediation status; the three drafts already produced by `kri-commentary` are consumed verbatim.
- **Risk appetite status** — 22 RAS metrics with limit, trigger, tolerance, current value, breach status, and the ladder-to-operating-limit column. One breach (third-party concentration), one at-trigger (operational-loss YTD), 20 within. Recalibration request named for third-party concentration; cited as decision item (ii).
- **Issues and remediation status** — open MRAs (3, two over 180 days), MRIAs (0), audit issues (12, four over 90 days), regulatory exam findings (4, all within age), internal high-severity (8, two over 60 days). Each over-age item carries owner, forward action, and slippage commentary; the MRA list is the source for decision item (i).
- **Forward-looking commentary** — three named items: FRB stress test 2026 hypothetical scenario published February 2026 and the firm's expected response posture; expected NYDFS Part 500 amendment effective date impact on the cyber program; the SEC climate disclosure rule current effectiveness flagged as unresolved with the firm's continuing voluntary TCFD posture noted.
- **Climate section** — TCFD-aligned governance and risk management subsections; NGFS Net Zero 2050 and Delayed Transition scenarios used; pointer to the parent group's CSRD-aligned disclosure. Source-trace appendix flags SEC climate disclosure rule current effectiveness.
- **Decision items (full detail)** — both decisions with options, recommended option, dissents (none recorded), requested vote (vote-required for both), owner (head of model risk for (i); head of TPRM for (ii)).
- **Appendices** — data confidence label = medium (three of 14 KRIs have known data-lineage gaps documented in the latest BCBS 239 self-assessment, so 'high' is not available); BCBS 239 known limitations enumerated; source trace per material claim; glossary; sign-off block (CRO and committee chair, with reviewer questions for the secretary to surface).

The pack stops at draft. The CRO and the head of risk reporting review before the committee secretary prepares for distribution.

#### Why this scenario matters

- Heat map with movement and exposure is the centrepiece. Static heat maps fail; this one shows direction and quantified exposure on the deteriorating cells.
- Decision items are first, not last. The committee charter calls for a status update and decisions; the load-bearing section is decisions, and the pack reflects that.
- Climate is in scope and treated as enterprise risk, not a bolt-on appendix. The decision to map it under strategic (rather than as a separately-rated heat-map cell) is documented; the climate cross-cutting overlay covers the scenarios and the link to disclosure.
- SEC climate rule is treated with verification discipline. The forward-looking commentary names the unresolved status and the firm's continuing voluntary TCFD posture; no claim of current effectiveness is asserted.
- Data confidence label is not 'high' because BCBS 239 known limitations are non-empty. Schema validation enforces this; the label is medium.

#### Anchors

- BCBS 239 (January 2013), Principles 7-11.
- COSO ERM (2017).
- 12 CFR Part 30 Appendix D (OCC Heightened Standards).
- FRB SR 12-17 (Consolidated Supervision Framework for Large Financial Institutions, December 2012).
- TCFD Final Report (June 2017); Implementing the Recommendations (October 2021).
- NGFS climate scenarios (current vintage, voluntary reference).
- 12 CFR Part 252 (FRB tailoring framework).

See `references/source-anchors.md` for full citations and verification flags.

## troubleshooting

### Troubleshooting: risk-committee-pack

Recurring failure modes when a committee pack looks complete but is not. The reviewer review should catch these; the builder review should preempt them.

#### The pack reads as a status update, not a committee instrument

Symptom: long heat map, dense KRI table, exhaustive issues register, no decision items. The committee meets, nods, and moves on.

Why it happens: builder treats the artifact as a snapshot for the file, not as the load-bearing input to a governance forum.

Fix: Decision items requested is the first body section. Every decision has named options, a recommended option, a requested vote or acknowledgement, and an owner. A pack with no decisions for the cycle is rare; usually it means the conversation between management and the committee has not happened yet, and the builder should surface that as a sign-off question rather than ship a status pack.

#### Static heat map

Symptom: heat-map cells with current rating only; no prior, no direction, no commentary.

Why it happens: the heat map gets ported forward from the prior pack with current ratings refreshed but the movement view never wired up.

Fix: every cell carries current, prior, and direction. Every deteriorating cell is addressed in the Top risks section. The structured object enforces the four required fields per cell (`risk_type`, `current_rating`, `prior_rating`, `direction`).

#### Climate as bolt-on appendix

Symptom: a separate "Climate appendix" floats outside the risk taxonomy; the heat map by risk type does not mention climate at all; physical and transition risk live nowhere on the enterprise view.

Why it happens: climate work has its own owner and its own scenario apparatus, and rolling it into the enterprise view feels like double-counting.

Fix: where climate is in scope, it appears in the heat map (as a separately-rated cell or under strategic with rationale documented in the cell commentary). The Climate section carries governance, scenarios, and the link to disclosure; it does not replace the heat-map placement. Load `references/cross-cutting.md#climate` for the placement guidance and the SEC-rule verification posture.

#### SEC climate rule overreach

Symptom: forward-looking commentary asserts the SEC climate disclosure rule is in force and the firm is reporting against it.

Why it happens: the rule was finalised March 2024 and the headline regulatory change is memorable; the legal challenges and the SEC's voluntary stay are not.

Fix: never assert current effectiveness of the SEC climate rule without checking SEC's posture as of the report date. Default posture: cite the rule with the verification flag in source-anchors, lean on TCFD for substantive content, note the firm's continuing voluntary posture in the climate section. The cross-cutting climate overlay carries the verification discipline; the SKILL.md does not over-claim.

#### RAS metrics with no ladder to operating limits

Symptom: RAS table reports limit, trigger, tolerance, current value, breach status. No column showing how the metric ladders down to first-line operating limits.

Why it happens: the ladder lives in the operating policy, not in the RAS document; the builder treats the two as separate.

Fix: the ladder column is required for OCC Heightened Standards covered banks (12 CFR Part 30 Appendix D §III) and recommended for any firm with a layered RAS. Without the ladder, the heightened-standards expectation that the board frames and oversees the RAS is not demonstrably met. The schema's `ras_status[].ladder_to_operating_limit` field is the place; the SKILL.md notes it as a sector-overlay reinforcement.

#### Issues section is a counter, not a manager

Symptom: issues table shows counts and ageing buckets only. Each over-age MRA, MRIA, or audit issue is a tally, not a managed item.

Why it happens: the upstream feed gives counts; the manager-level commentary lives in the issue owner's notes and never makes the pack.

Fix: each over-age item carries owner (role), forward action with date, and slippage commentary explaining why the prior commitment slipped. Counts alone fail the SR 12-17 expectation that the committee manage, not just count, the open population.

#### Confidence label gaming

Symptom: data confidence label is "high" while the BCBS 239 known-limitations list is non-empty.

Why it happens: the label is treated as an aspiration or as a brand statement, not as a BCBS-239-anchored claim.

Fix: schema validation enforces the rule that `data_confidence_label = "high"` is incompatible with non-empty `bcbs239_known_limitations`. Where limitations are present, the label is medium at best; the appendix names the limitations and the path to closure. The label is the BCBS 239 voice in the pack, not a marketing decision.

#### Generic forward-looking commentary

Symptom: forward-looking section reads "emerging risks include cyber, AI, and climate". The committee learns nothing.

Why it happens: forward-looking gets drafted last when builder fatigue is highest; the section is treated as a hedge.

Fix: each forward-looking item is named, dated, and regulator-anchored. "FRB stress test 2026 hypothetical scenario published February 2026: projected capital impact on the commercial real-estate book to be reported next cycle" is named, dated, and actionable. "Emerging risks include cyber" is filler; cut it.

#### Heat map with no quantified exposure on elevated cells

Symptom: operational risk cell rated elevated, deteriorating; no number anywhere in the row.

Why it happens: quantified exposure lives in the loss-event log, the loss-distribution model, and the YTD operational-loss tracker; pulling them into the cell commentary feels redundant.

Fix: every elevated or high cell carries a quantified exposure where one exists, in the cell commentary or the linked top-risks entry. The committee cannot calibrate "elevated" without a number to anchor it. If no number exists, the absence is itself a sign-off question.

#### Adviser-level pack reads as a fund board pack

Symptom: adviser risk committee pack covers fund-level liquidity, fund-level NAV-error events, fund-board-mapped issues. The adviser firm's enterprise view (investment risk at the firm, fiduciary risk at the firm, vendor and technology risk at the firm) is buried.

Why it happens: the builder uses bank-shaped templates and slots fund items into the absent bank rows.

Fix: the capital-markets sector overlay carries the adviser-firm-versus-fund-board distinction. Adviser-level risk committee scope is the adviser firm. Fund-level items go to the fund boards via separate reporting; cross-link if an item is material to both, do not collapse.

#### Sector overlay loaded but ignored

Symptom: insurance sector overlay loaded but the pack has no ORSA mapping; banking overlay loaded but the pack has no MRA / MRIA aging columns; capital-markets loaded but no Form PF current-event filings called out.

Why it happens: the overlay is treated as background reading, not as content that lands in the pack.

Fix: when the scope names a sector, the matching `references/sector-overlays.md#<sector>` content lands as named items in the pack. Sector-specific sign-off questions go to the reviewer-question list.

#### Pack stops too late

Symptom: the skill produces and "files" the pack with the secretary, marks it as distributed, asserts CRO sign-off without evidence.

Why it happens: builder over-runs the human-review gate.

Fix: the pack is a draft until the CRO and the head of risk reporting review. The skill stops at the draft and surfaces the reviewer questions for the secretary; it does not assert sign-off, distribute, or post to the committee folder.
