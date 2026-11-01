# Best-execution surveillance review

The skill produces two deliverables together — an Excel surveillance workbook (the substantive analytical record) and a Word committee memo (the read-out for the best-execution committee, the CCO, the fund board where applicable, and the FINRA / SEC examiner-facing file). Both share the same review identification, scope, and findings; the workbook carries the tabular evidence and the memo carries the narrative.

This file is the content spec for both renderings. The `xlsx` skill (Anthropic `document-skills` plugin) consumes the workbook section to render `.xlsx`; the `docx` skill consumes the memo section to render `.docx`.

---

## Review identification (workbook front sheet + memo header)

| Field | Value |
|---|---|
| Review ID | [stable identifier; reused across quarters for trend tracking] |
| Firm | [legal entity; no brand name unless engagement supplied] |
| Firm registration | [IA / BD / IA_and_BD / fund_adviser] |
| CRD / SEC file # | [firm CRD; SEC file 801- or 8- as applicable] |
| Review period | [start date — end date] |
| Cadence | [quarterly / monthly+quarterly+annual / quarterly-into-fund-board / annual] |
| Asset-class scope | [equities / options / fixed-income / etfs / mutual-funds / derivatives / fx / crypto / other] |
| Engagement ID | [pointer to scope record, or "scope not formalised"] |
| Audience | [best-ex committee / CCO / fund board / FINRA exam file / SEC IM exam file] |
| Owner (role) | [head of trading / head of investments / CCO] |
| Approver (role) | [best-ex committee chair / CCO / fund-board CCO for fund variant] |
| Confidence label | [high / medium / low / unknown] |

---

# Part A — Excel surveillance workbook (rendered via `xlsx`)

The workbook has eight sheets. Tabular by nature; narrative belongs in the memo.

## Sheet 1: Scope and source posture

| Field | Value |
|---|---|
| Data feeds | [OMS / EMS / ledger / TCA vendor / Rule 605 venue downloads / Rule 606 internal report] |
| TCA vendor | [name and methodology summary, or "in-house"] |
| Sample method | [stratified by asset class and order type / random / risk-based / 100% off-NBBO; describe stratification] |
| Sample size | [N trades sampled; total population] |
| Period coverage | [period start — end] |
| Exclusions | [excluded orders with rationale: e.g., not-held orders, working orders crossing period, error trades] |
| Thresholds for exception flag | [e.g., off-NBBO at execution, > X bps from arrival mid, fill rate < Y%] |

## Sheet 2: Venue inventory and changes

| Venue ID | Venue type | Status | Watchlist flag | Period share (%) | Period prior share (%) | Change reason |
|---|---|---|---|---|---|---|
| [exchange / ATS / wholesaler / market-maker / dealer-platform] | [lit / dark / wholesaler / single-dealer / dealer-network] | [active / added / removed / on-watchlist] | [yes / no] | | | |

## Sheet 3: Aggregate execution-quality metrics — by venue and asset class

| Venue ID | Asset class | Metric | Period value | Period prior value | Threshold | Breach flag | Source |
|---|---|---|---|---|---|---|---|
| | equities | Effective-over-quoted ratio | | | | | [TCA vendor / internal] |
| | equities | Price improvement ($/share) | | | | | |
| | equities | At-or-better fill rate (%) | | | | | |
| | equities | Average effective spread (bps) | | | | | |
| | equities | Market-on-close fill rate (%) | | | | | |
| | options | Net liquidity capture | | | | | |
| | fixed-income | Distance from competitive quote (bps) | | | | | |

Cite the data feed by file path or by report identifier in the Source column. Where the threshold is firm-set, link to firm-overlay; where firm thresholds are not on file, mark `[evidence needed]`.

## Sheet 4: Rule 605 / 606 reconciliation

| Item | Source | Period value | Reconciliation status |
|---|---|---|---|
| Internal % of customer orders routed to Venue X | Internal routing system | | |
| Rule 606 quarterly report % to Venue X | Firm's published 606 | | [match / off by Y%; investigated; remediation noted] |
| Rule 605 effective spread at Venue X (NMS stocks) | Venue's published 605 | | |
| Internal observed effective spread at Venue X | TCA / internal | | [match / divergence Y bps; investigated] |
| Rule 605 price improvement at Venue X | Venue's published 605 | | |
| Internal observed price improvement at Venue X | TCA / internal | | |

For periods governed by SEC Release 34-99679 amendments, the field set follows the amended definitions and categories; verify the operative compliance date for the period under review.

## Sheet 5: Trade-by-trade exception sample

| Trade ID | Trade timestamp (UTC) | Asset class | Side | Symbol / CUSIP | Order type | Order size | Routed venue | Executed price | NBBO bid at execution | NBBO ask at execution | Arrival mid | Miss type | Rule 5310 / IA factor analysis | Root cause | Remediation | Owner role | Due date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

`Miss type` examples: off-NBBO fill; price-improvement miss vs alternative venue; large-block routing decision (broker-of-choice not used); principal-trade execution outside reasonable price band; agency-cross unfavourable to one side; soft-dollar-eligible flow routed to PFOF venue with weaker price improvement.

`Factor analysis` is structured against the rule lattice for the firm registration: Rule 5310 .01 factors for BD review (character of market, size and type of transaction, number of markets checked, accessibility of quotation, terms and conditions of order); IA fiduciary factors (price, speed, likelihood of execution, size, market impact, accessibility, total transaction costs, customer instructions); both for dual registrants.

Sample is stratified. Block trades, illiquid securities, after-hours fills, principal trades, agency crosses, and conflicted-routing flows are over-represented relative to their share of total volume — the tail is where best-execution issues concentrate.

## Sheet 6: Conflict review

| Conflict type | Present (Y/N) | Magnitude | How weighed in best-ex determination | Evidence | Residual conflict | Disclosure consistency check |
|---|---|---|---|---|---|---|
| Payment for order flow (PFOF) | | [$ received in period] | | [committee minutes ref / routing-policy ref] | | [matches Form CRS / Rule 606 / Form ADV] |
| Principal trades — Adv Act §206(3) | | [count and notional] | | [transaction-by-transaction consent file] | | |
| Agency cross trades — §206(3) / Rule 206(3)-2 | | [count and notional] | | [consent file] | | |
| Affiliated brokerage — ICA §17(e) | | [% of fund commissions] | | [comparable-rate evidence; 17e-1 board determination] | | |
| Soft dollars — §28(e) | | [$ in commissions] | | [eligibility memo; mixed-use allocation methodology] | | |
| Commission-sharing arrangement | | [$ accumulated; $ disbursed] | | [CSA agreement; budget vs spend; disbursement controls] | | |
| Other inducements | | | | | | |

A conflict the firm has not assessed is itself a finding.

## Sheet 7: Findings, exceptions, corrective actions

| Finding ID | Severity | Description | Source (sheet ref) | Control owner role | Target date | Status |
|---|---|---|---|---|---|---|

Severity gradient: descriptive (e.g., observation / minor / significant / material). Avoid forced enums; reviewers calibrate to firm norms.

## Sheet 8: KRIs and trend lines

| KRI | Definition | Period value | Period prior value | Threshold | Breach flag | Trend (4-period) |
|---|---|---|---|---|---|---|
| % of retail orders receiving price improvement | | | | | | |
| Average price improvement per share (cents) | | | | | | |
| Effective-over-quoted ratio (firm-wide) | | | | | | |
| Off-NBBO fill rate (%) | | | | | | |
| Block-trade slippage vs arrival mid (bps) | | | | | | |
| Principal-trade transactional consent on-file rate (%) | | | | | | |
| Affiliated-broker share of fund commissions (%) | | | | | | |
| Soft-dollar mixed-use products with documented allocation (%) | | | | | | |

Trend the metrics across at least four prior periods (where available) so the committee can read the direction, not just the period level.

---

# Part B — Word committee memo (rendered via `docx`)

## 1. Executive summary

Three to five bullets. The committee read for the period: aggregate execution-quality posture (within / outside firm appetite), exceptions of note from the sample, conflict-review headlines (including any new conflict identified), changes to the venue inventory, the recommended disposition of any open findings.

## 2. Scope and source posture

One paragraph naming the period, the registration class, the asset-class scope, the data feeds, the TCA methodology, the sample method, and material exclusions. Reference the workbook Sheet 1 for detail.

## 3. Aggregate execution-quality summary

Two to three paragraphs reading the headline metrics from workbook Sheet 3 against firm appetite and against the prior period. Material divergence (favourable or unfavourable) is called out with the suspected driver. Where the driver is not yet understood, the memo says so rather than guessing.

## 4. Rule 605 / 606 reconciliation summary

One paragraph noting reconciliation status from workbook Sheet 4, including any material anomalies investigated and the resolution.

## 5. Trade-exception sampling — themes

Narrative read of workbook Sheet 5. Group exceptions by miss-type theme rather than walking trade-by-trade. Three to five themes is typical; if everything is one-off, that is itself a read. The theme paragraphs name the factor analysis under the applicable rule lattice and the root-cause pattern.

## 6. Conflict-review read

Narrative read of workbook Sheet 6. For each conflict in scope, the memo records: how the conflict was weighed in the determination (referencing the committee minutes that captured the weighing), the residual conflict after mitigation, and any disclosure-consistency observations. The memo flags conflicts the surveillance newly identified that were not previously on the conflict register.

## 7. Venue and counterparty review

Narrative summary of workbook Sheet 2 changes. Adds, removes, and watchlist entries / exits with rationale and follow-up.

## 8. Findings, exceptions, and corrective actions

Tabular insert from workbook Sheet 7 carried into the memo for the committee record. The memo notes which findings escalate beyond the committee (CCO direct, fund board, exam-file).

## 9. Best-execution committee record

Committee meeting date; members present and absent; materials reviewed (this memo, this workbook, supporting TCA reports); decisions taken; dissents recorded (or "no dissents recorded"); follow-up actions assigned with owner and due date; status of follow-ups from prior meetings.

## 10. Fund-board escalation (fund-adviser variant only)

Where the fund-adviser variant applies, this section carries the fund-by-fund attestation feeding the §15(c) board materials: each fund's brokerage-and-best-execution attestation summary, the §17(e) reasonable-and-fair compensation evidence (where affiliated brokerage is in use), the §28(e) soft-dollar review summary (where soft dollars are in use), and the recommendations to the fund board.

## 11. Source citations and confidence

List of source citations with date (rule references, internal reports, vendor reports). Confidence label per the front-sheet field. Open questions flagged for legal / portfolio management / trading desk input before the next cycle.

---

## Notes for renderers

- The workbook front sheet (Sheet 0, not numbered above) carries the review identification table.
- Highlight cells with `Breach flag = Y` in red; `Watchlist flag = Y` in amber; conditional formatting applied in the renderer.
- Trend columns in Sheet 8 use sparkline cells where the renderer supports them; otherwise inline four-period values.
- The memo embeds two tables from the workbook (Sheet 7 findings; Sheet 9 KRIs) as Word tables; the renderer inserts them rather than re-typing.
- Both deliverables carry the same Review ID in the header so the workbook and memo bind together in the file room.
