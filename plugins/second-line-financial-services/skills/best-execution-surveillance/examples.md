# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## dual-registrant-quarterly-review

### Example: dual-registrant quarterly best-execution review with PFOF and principal-trade exposure

#### Scenario

A dual-registered investment adviser / broker-dealer runs a retail equity book and a small institutional desk. Retail equity flow is routed to two wholesalers paying for order flow. The institutional desk occasionally crosses agency and principal under Advisers Act §206(3). Current quarter under review.

#### Input

- Firm registration: `IA_and_BD`.
- Asset-class scope: equities (NMS stocks), some retail options.
- Cadence: quarterly best-ex committee, monthly venue surveillance for the BD limb feeding into the quarterly read.
- Source posture: connector-aware (live OMS, EMS, TCA vendor portal, internal Rule 606 quarterly working file).
- Sample: stratified — 50 retail equity exception trades, 15 large-block equity trades, all 8 principal trades and all 4 agency-cross trades from the period.
- Audience: best-ex committee, with the BD-side surveillance also feeding the WSP file under FINRA Rule 3110.

#### Output sketch (workbook headlines)

- **Aggregate metrics**: retail equity routing to the two wholesalers shows price improvement of 0.31 cents/share (Wholesaler A) and 0.27 cents/share (Wholesaler B) — within firm appetite (≥ 0.20 cents/share). Effective-over-quoted ratio 0.42 and 0.45 — within appetite (≤ 0.50). At-or-better fill rate 99.1% / 98.8% — within appetite.
- **Rule 605 / 606 reconciliation**: internal % of orders to Wholesaler A matches the 606 quarterly figure within 0.4 percentage points; venue 605 effective spread aligns with the firm's TCA observation within 0.3 bps. No material anomalies.
- **Trade-exception sample (retail)**: 7 of 50 sampled trades carry an off-NBBO fill at execution; factor analysis under both Rule 5310 .01 and the IA fiduciary factor list shows 5 are explainable by quote-fade between routing decision and execution (NBBO moved < 50 ms before fill), 2 are unexplained and routed to investigation.
- **Trade-exception sample (principal trades — all 8)**: 6 carry the pre-transactional written disclosure and the per-transaction client consent on file. 2 lack the per-transaction consent document — both for the same client over a two-week window where the operations team's consent-collection process appears to have lapsed.
- **Conflict review**:
  - PFOF: present; $X received from Wholesaler A and $Y from Wholesaler B over the period; weighed in the routing decision per the November and February committee minutes (committee considered alternative venues with no PFOF and concluded the price-improvement and fill-rate evidence supported continued routing); residual conflict flagged; disclosure consistency — Form CRS and Form ADV item 12 disclosure consistent with arrangement; Rule 606 disclosure consistent.
  - Principal trades §206(3): present; 8 trades; weighing of conflict noted in the trading desk's pre-trade procedure; residual conflict — adviser bears the burden under §206(3); evidence — 6/8 transactions have full consent file; 2/8 are the finding above.
  - Agency cross §206(3) (Rule 206(3)-2): present; 4 trades; written disclosure and prospective consent on file for all 4; pricing fairness analysis using midpoint-at-order-entry shows acceptable distribution of benefit between the two sides.
  - Affiliated brokerage, soft dollars, CSAs, other inducements: none.
- **Findings**: (1) two principal trades lack the per-transaction consent document — significant; remediate by [date]; control owner: head of operations; (2) PFOF disclosure in Form ADV is present but the November committee minutes do not explicitly record the PFOF conflict in the determination narrative — observation; remediate by tightening the committee-minute template by next meeting; control owner: CCO.
- **KRI trends**: price improvement per share trending stable across four quarters; principal-trade transactional consent on-file rate dropped from 100% (4 prior quarters) to 75% this quarter — the finding above is the cause; affiliated-broker share zero (no affiliate); soft-dollar mixed-use products with documented allocation: n/a (no soft dollars in use).
- **Committee record**: meeting held on [date]; attendees CCO, head of trading, head of operations, head of risk, counsel; no dissents recorded; two follow-ups assigned (the per-transaction consent gap; the committee-minute template); two prior-quarter follow-ups closed (one venue removed from watchlist after two clean quarters; one TCA threshold recalibrated as agreed).

#### Output sketch (memo headlines)

Executive summary: aggregate execution-quality posture within firm appetite this quarter; two findings of note (per-transaction consent gap on §206(3) principal trades, committee-minute template not capturing PFOF weighing); no venue inventory changes; recommended disposition `accept-with-conditions` pending follow-ups.

#### Why this scenario matters

It tests three things at once: the dual-registrant's parallel-rule-lattice obligation (the artifact carries both the §206 fiduciary factor analysis and the Rule 5310 .01 factor analysis on the trade-exception sheet); the PFOF conflict-as-input framing under the conduct overlay (disclosure is consistent but the surveillance still surfaces a finding because the committee-minute did not capture the weighing); and the §206(3) per-transaction consent operational lapse, a recurring finding pattern in dual-registrant exams that the surveillance catches because the sample stratifies to over-represent principal trades.

#### Pattern derived from

Public Risk Alerts on best execution (SEC Office of Compliance Inspections and Examinations / Division of Examinations); SEC enforcement actions in the §206 conflict-disclosure line including the SEC v. Robare Group context for the disclosure-vs-conduct distinction; FINRA Regulatory Notice 15-46 for cross-asset application. Verify exact public-source pins on the analysis date.

## fund-adviser-15c-pack-with-soft-dollars

### Example: fund-adviser quarterly review feeding §15(c) board materials with soft-dollar arrangements

#### Scenario

The adviser to a registered open-end equity fund family is preparing the brokerage and best-execution section of the quarterly fund-board materials. The current quarter feeds the annual §15(c) board approval cycle. The adviser uses third-party research paid for via §28(e) soft dollars across two brokers and has an affiliated broker that handles a small portion of fund commissions in one of the funds in the family.

#### Input

- Firm registration: `fund_adviser`.
- Asset-class scope: equities (US listed; some non-US listed via local custodian relationships).
- Cadence: quarterly into the fund-board cycle; full annual review supports §15(c) in the Q4 board meeting.
- Source posture: public-plus-firm-policy-plus-trade-data (live ledger and TCA vendor portal; soft-dollar provider invoices and budget-vs-spend reports; affiliated-broker rate-comparison file).
- Sample: stratified — 25 fund equity trades sampled per fund (top fund by AUM and the fund using the affiliated broker, so 50 trades); all soft-dollar provider invoices for the period reviewed; the §17(e)(1) comparable-rate evidence pulled for every trade routed to the affiliated broker.
- Audience: best-ex committee internally; fund board (via the adviser's CCO and the fund's CCO) for the §15(c) escalation.

#### Output sketch (workbook headlines)

- **Aggregate metrics (fund equity)**: effective-over-quoted ratio per executing broker shown against firm appetite; price-improvement and at-or-better fill metrics shown per executing broker; large-block slippage vs arrival mid shown by fund and by sleeve.
- **Conflict review**:
  - Soft dollars §28(e): present; $X across two brokers in the period; eligibility memo on file for each product (research only; one mixed-use product); mixed-use product allocation methodology — 80% research / 20% operations per the firm's documented method; budget vs spend within approved budget; commission-sharing arrangement with one broker — accumulated $A, disbursed $B per the CSA agreement and the disbursement controls. Finding: the mixed-use product (a market-data feed used for both research and operational monitoring) is currently allocated 100% to research-eligible based on the original eligibility memo; the firm's quarterly utilisation review now suggests an 80/20 split would more accurately reflect actual usage. Adjust the allocation methodology and re-document.
  - Affiliated brokerage §17(e): present in one fund; 6% of that fund's commissions; comparable-rate evidence file shows the affiliated broker's commission rate within the firm's selected peer band; §17(e)(2) board procedures in place; quarterly board determination on the calendar. Finding: the comparable-rate evidence draws from a peer set last refreshed 14 months ago; refresh the peer set before next quarter's board review.
  - Other conflicts: PFOF — n/a (institutional flow); principal trades — n/a in the period; agency cross — n/a; other inducements — n/a.
- **Trade-exception sample**: 3 of 50 sampled fund trades carry exceptions (1 large-block slippage above firm appetite — explained by an unusual close-of-day liquidity event; 2 routed to a non-preferred broker for index-rebalance flow per the firm's pre-approved index-rebalance routing exception). Factor analysis under the IA fiduciary factor list shows acceptable explanations; no remediation.
- **Findings**:
  - Mixed-use soft-dollar allocation refresh — significant; remediate before the §15(c) annual approval; control owner: CCO.
  - Affiliated-broker comparable-rate peer-set refresh — observation; complete by next quarter's board meeting; control owner: head of trading.
- **Fund-board attestation block** (per fund):
  - Fund A: brokerage and best-execution attestation supported by the surveillance findings; soft-dollar usage summary attached; affiliated-brokerage usage 6%, with the §17(e)(1) comparable-rate evidence pinned (subject to the peer-set refresh finding).
  - Fund B: brokerage and best-execution attestation supported; soft-dollar usage applied per allocation methodology (subject to the mixed-use refresh finding); no affiliated brokerage.
  - [other funds]: similar shape.

#### Output sketch (memo headlines)

Executive summary: surveillance posture supports the §15(c) attestations for the funds in scope; two findings to remediate before the Q4 annual approval (mixed-use soft-dollar allocation refresh; affiliated-broker comparable-rate peer-set refresh); no venue inventory changes; recommended disposition `accept-with-conditions`.

The fund-board escalation section (memo Section 10) carries the fund-by-fund attestation feeding the §15(c) board materials.

#### Why this scenario matters

It tests the fund-adviser variant's specifically-fund-shaped blocks: the §17(e)(1) reasonable-and-fair compensation evidence pinned to a peer-set (and the surveillance surfacing the peer-set refresh as itself a finding); the §28(e) mixed-use allocation methodology challenged against actual usage rather than accepted on the original eligibility memo; the §15(c) per-fund attestation block supporting the annual board approval. These are the substantive blocks the fund's CCO and the fund-board independent counsel read in the §15(c) materials, beyond the surveillance proper.

#### Pattern derived from

Public §17(e) and §28(e) interpretive materials including the SEC's 2006 Commission Guidance Regarding Client Commission Practices Under §28(e); SEC Risk Alerts and EXAMS focus areas on adviser brokerage and soft-dollar practices; documented fund-board governance practice as reflected in academic and industry literature on the §15(c) factor analysis. Verify exact public-source pins on the analysis date.

## troubleshooting

### Troubleshooting: best-execution-surveillance

Recurring defects in best-execution surveillance artifacts. Each is a finding pattern an examiner or independent reviewer is likely to surface; the skill is structured to make each visible rather than letting it pass.

#### Treating "best execution" as best price

The duty is a multi-factor analysis. Rule 5310 .01 lists the BD factors (character of the market, size and type of transaction, number of markets checked, accessibility of the quotation, terms and conditions of the order); the IA fiduciary factor list runs price, speed, likelihood of execution, size, market impact, accessibility, total transaction costs, and customer instructions. Both lists are non-exhaustive. A surveillance read that scores trades only on price (or only on price improvement vs NBBO) misses the duty.

Fix: the trade-exception sheet's `factor_analysis` column walks the full applicable factor list per row, with the rule lattice keyed by `firm_registration`. Do not collapse the factor walk into a single price-comparison line.

#### Confusing the BD regular-and-rigorous review with the IA fiduciary review

Rule 5310 .09 requires a regular-and-rigorous review of execution quality at the venue level for BDs not running an order-by-order review. The IA fiduciary review under §206 is a separate duty with overlapping factors but different documentation expectations. Dual registrants commonly run one operational process and produce one document, then face an examiner who reads it under either lattice and finds gaps.

Fix: dual registrants explicitly produce both reads in the artifact. The trade-exception sheet's factor_analysis column walks both factor lists per row; the memo carries separate aggregate-quality summaries for the BD limb (5310 .09 frame) and the IA limb (§206 frame). The committee record references both rule lattices.

#### Treating Rule 606 as the best-execution review

Rule 606 is a routing-disclosure obligation under 17 CFR 242.606. It does not, by itself, satisfy the Rule 5310 or §206 review obligation. Surveillance artifacts that consist of a 606 summary plus a confirmation of routing match the disclosure are insufficient; the substantive review is what 5310 / §206 require beyond.

Fix: the 605 / 606 reconciliation sheet is a cross-check on operational data quality and on the firm's own measurement, not the surveillance itself. The trade-exception sheet, the venue-level aggregate-quality sheet, and the conflict-review sheet carry the substantive review.

#### Skipping the conflict-as-input step

PFOF, principal trades, agency crosses, affiliated brokerage, soft dollars, commission-sharing arrangements: each must be weighed in the best-execution determination, not just disclosed alongside it. An artifact that lists conflicts in a disclosure block but does not show how the conflict factored into routing or execution decisions misses the substantive review.

Fix: the conflict-review sheet's `weighed_in_determination` column is required for every present conflict, with reference to the committee minutes that captured the weighing. The disclosure-consistency check is a separate column; disclosure does not cure conflict if the underlying conduct does not match.

#### Soft-dollar mixed-use without proportional allocation

§28(e) and the 2006 interpretive release require that mixed-use products be allocated between research-eligible and non-research portions based on a reasonable methodology, with contemporaneous documentation. Default-to-100%-research-eligible is wrong; relying on the original eligibility memo years after the actual-usage pattern has shifted is also wrong.

Fix: the conflict-review sheet's soft-dollar row records the mixed-use allocation methodology and pulls the contemporaneous utilisation data; the surveillance reads the methodology against actual usage and surfaces a finding where they diverge. The fund-adviser variant escalates the finding into the §15(c) board materials.

#### Affiliated-broker §17(e) treated as "we used them" without comparable-rate benchmark

ICA §17(e)(1) requires reasonable-and-fair compensation; Rule 17e-1 sets the procedural framework. Practice expects a peer-set benchmark refreshed periodically. Affiliated-broker usage shown in the surveillance without the comparable-rate evidence on file is a finding regardless of whether the rates appear acceptable.

Fix: the conflict-review sheet's affiliated-brokerage row pins the comparable-rate evidence file. The fund-adviser variant carries the peer-set refresh date and surfaces a finding when the peer-set is stale.

#### Sample sizes calibrated for the median trade, not for the tail

Best-execution issues concentrate in block trades, illiquid securities, after-hours fills, principal trades, agency crosses, and conflicted-routing flow. A sample drawn proportionally from total volume under-samples the tail and misses the issues.

Fix: the sample method is stratified, with the strata over-representing the tail. The scope sheet records the stratification explicitly. A sample stated without an identification method is an assertion, not a finding.

#### Fund §15(c) section copy-pasted year-on-year

The §15(c) brokerage and best-execution discussion expects period-specific data and exception detail. Boilerplate attestations are themselves a finding pattern in EXAMS sweeps, regardless of whether the underlying execution quality is acceptable.

Fix: the fund-adviser variant's `fund_15c_attestation` block is per-fund per-period, with the surveillance findings, the §17(e) and §28(e) blocks, and the period-specific data pulled in. Boilerplate language is flagged.

#### Committee minutes with no dissents, no questions, no follow-ups across multiple periods

The conduct overlay reads committee minutes for substantive challenge. A multi-period run of meetings where the minutes record only attendance, materials reviewed, and a generic approval (no dissents recorded, no questions noted, no follow-ups assigned) is itself a culture finding even if every individual meeting passed.

Fix: the committee_pack block's `dissents_recorded` field carries an explicit "no dissents recorded" string when none occurred, so the field is not silently empty. The follow-ups field carries the prior-period follow-up status, so an examiner can read the rolling action discipline. The memo's Section 9 surfaces the absence of substantive challenge as a culture observation if the pattern persists.

#### Firm-set thresholds and appetite missing from the artifact

Aggregate-quality metrics shown without a threshold against which to read them produce read-outs no committee can act on. The skill default is to mark `[evidence needed]` rather than fabricate a threshold.

Fix: the aggregate_metrics rows record `threshold` and `breach_flag` explicitly; missing thresholds carry `[evidence needed]` and the memo flags the absence. The firm-overlay file is the place to install firm-specific appetite levels; the skill consumes them when present.

#### Crypto and FX scope claimed without honest evidence framework

For asset classes lacking a consolidated tape (FX, crypto, fixed income) the surveillance can only rely on the evidence framework that asset class supports: competitive-quote logs for fixed income; price-versus-mid-at-execution and last-look reads for FX; venue-by-venue execution data with the limitations explicitly named for crypto. Claiming NBBO-style coverage in these asset classes overstates the surveillance.

Fix: the asset-class flavour in the capital-markets sector overlay sets the evidence framework per class; the surveillance documents the limitations rather than claiming a coverage it cannot support.
