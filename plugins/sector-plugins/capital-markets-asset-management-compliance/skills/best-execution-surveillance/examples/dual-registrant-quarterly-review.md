# Example: dual-registrant quarterly best-execution review with PFOF and principal-trade exposure

## Scenario

A dual-registered investment adviser / broker-dealer runs a retail equity book and a small institutional desk. Retail equity flow is routed to two wholesalers paying for order flow. The institutional desk occasionally crosses agency and principal under Advisers Act §206(3). Current quarter under review.

## Input

- Firm registration: `IA_and_BD`.
- Asset-class scope: equities (NMS stocks), some retail options.
- Cadence: quarterly best-ex committee, monthly venue surveillance for the BD limb feeding into the quarterly read.
- Source posture: connector-aware (live OMS, EMS, TCA vendor portal, internal Rule 606 quarterly working file).
- Sample: stratified — 50 retail equity exception trades, 15 large-block equity trades, all 8 principal trades and all 4 agency-cross trades from the period.
- Audience: best-ex committee, with the BD-side surveillance also feeding the WSP file under FINRA Rule 3110.

## Output sketch (workbook headlines)

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

## Output sketch (memo headlines)

Executive summary: aggregate execution-quality posture within firm appetite this quarter; two findings of note (per-transaction consent gap on §206(3) principal trades, committee-minute template not capturing PFOF weighing); no venue inventory changes; recommended disposition `accept-with-conditions` pending follow-ups.

## Why this scenario matters

It tests three things at once: the dual-registrant's parallel-rule-lattice obligation (the artifact carries both the §206 fiduciary factor analysis and the Rule 5310 .01 factor analysis on the trade-exception sheet); the PFOF conflict-as-input framing under the conduct overlay (disclosure is consistent but the surveillance still surfaces a finding because the committee-minute did not capture the weighing); and the §206(3) per-transaction consent operational lapse, a recurring finding pattern in dual-registrant exams that the surveillance catches because the sample stratifies to over-represent principal trades.

## Pattern derived from

Public Risk Alerts on best execution (SEC Office of Compliance Inspections and Examinations / Division of Examinations); SEC enforcement actions in the §206 conflict-disclosure line including the SEC v. Robare Group context for the disclosure-vs-conduct distinction; FINRA Regulatory Notice 15-46 for cross-asset application. Verify exact public-source pins on the analysis date.
