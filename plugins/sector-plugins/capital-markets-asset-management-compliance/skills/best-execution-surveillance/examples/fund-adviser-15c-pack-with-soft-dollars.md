# Example: fund-adviser quarterly review feeding §15(c) board materials with soft-dollar arrangements

## Scenario

The adviser to a registered open-end equity fund family is preparing the brokerage and best-execution section of the quarterly fund-board materials. The current quarter feeds the annual §15(c) board approval cycle. The adviser uses third-party research paid for via §28(e) soft dollars across two brokers and has an affiliated broker that handles a small portion of fund commissions in one of the funds in the family.

## Input

- Firm registration: `fund_adviser`.
- Asset-class scope: equities (US listed; some non-US listed via local custodian relationships).
- Cadence: quarterly into the fund-board cycle; full annual review supports §15(c) in the Q4 board meeting.
- Source posture: public-plus-firm-policy-plus-trade-data (live ledger and TCA vendor portal; soft-dollar provider invoices and budget-vs-spend reports; affiliated-broker rate-comparison file).
- Sample: stratified — 25 fund equity trades sampled per fund (top fund by AUM and the fund using the affiliated broker, so 50 trades); all soft-dollar provider invoices for the period reviewed; the §17(e)(1) comparable-rate evidence pulled for every trade routed to the affiliated broker.
- Audience: best-ex committee internally; fund board (via the adviser's CCO and the fund's CCO) for the §15(c) escalation.

## Output sketch (workbook headlines)

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

## Output sketch (memo headlines)

Executive summary: surveillance posture supports the §15(c) attestations for the funds in scope; two findings to remediate before the Q4 annual approval (mixed-use soft-dollar allocation refresh; affiliated-broker comparable-rate peer-set refresh); no venue inventory changes; recommended disposition `accept-with-conditions`.

The fund-board escalation section (memo Section 10) carries the fund-by-fund attestation feeding the §15(c) board materials.

## Why this scenario matters

It tests the fund-adviser variant's specifically-fund-shaped blocks: the §17(e)(1) reasonable-and-fair compensation evidence pinned to a peer-set (and the surveillance surfacing the peer-set refresh as itself a finding); the §28(e) mixed-use allocation methodology challenged against actual usage rather than accepted on the original eligibility memo; the §15(c) per-fund attestation block supporting the annual board approval. These are the substantive blocks the fund's CCO and the fund-board independent counsel read in the §15(c) materials, beyond the surveillance proper.

## Pattern derived from

Public §17(e) and §28(e) interpretive materials including the SEC's 2006 Commission Guidance Regarding Client Commission Practices Under §28(e); SEC Risk Alerts and EXAMS focus areas on adviser brokerage and soft-dollar practices; documented fund-board governance practice as reflected in academic and industry literature on the §15(c) factor analysis. Verify exact public-source pins on the analysis date.
