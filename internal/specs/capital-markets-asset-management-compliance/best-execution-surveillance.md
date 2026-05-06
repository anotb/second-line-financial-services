# Spec: best-execution-surveillance

Plugin: capital-markets-asset-management-compliance
Status: phase 1 spec sheet, pending phase 2 build
Date: 2026-05-06
Sector overlay: capital-markets (SEC-registered investment advisers, broker-dealers, registered funds)

## Activation-tuned description

Drafts a periodic best-execution surveillance review for an investment adviser, broker-dealer, or registered fund. Produces trade-by-trade exception sampling, aggregate venue and counterparty metrics, the FINRA Rule 5310 / SEC IA fiduciary best-execution factor analysis (price, speed, likelihood, size, market impact, accessibility, transaction costs, customer instructions), Rule 605/606 reconciliation where applicable, and the best-execution committee escalation pack. Output is the reviewable artifact a best-ex committee or fund 15(c) report consumes.

Best for:
- A registered investment adviser is performing its quarterly or annual best-execution review for its non-discretionary or discretionary brokerage arrangements (Advisers Act §206 fiduciary best-execution duty).
- A broker-dealer is performing its FINRA Rule 5310 "regular and rigorous" review of execution quality across venues for retail and institutional order flow.
- A registered fund's adviser is preparing the best-execution and brokerage section of the 15(c) board materials, including soft-dollar (§28(e)) arrangements and commission-sharing arrangements.
- A second-line reviewer is sampling trade exceptions (price-improvement misses, off-NBBO fills, large-block routing decisions, principal cross trades, agency cross trades) for a periodic surveillance write-up.

Not the right tool when:
- The objective is real-time order-routing technology selection. This skill is the periodic governance review, not vendor selection (use third-party-operational-resilience/vendor-diligence).
- The objective is exam-readiness or 38a-1 program design (use adviser-exam-readiness or risk-compliance-core/policy-gap-review).
- The objective is to build a transaction cost analysis (TCA) model. This skill consumes TCA outputs; it does not build them.
- The institution is not subject to a US fiduciary, FINRA, or SEC best-execution duty (out of scope).

Anchored to: Investment Advisers Act §206 fiduciary duty (best execution as a component of the duty of care, see SEC IM Guidance 1986 and SEC Interpretation Regarding Standard of Conduct for Investment Advisers IA-5248 (June 5 2019)); Investment Company Act §17(e) and §28(e) of the Exchange Act; FINRA Rule 5310 (Best Execution and Interpositioning); FINRA Rule 5310 Supplementary Material .09 (regular and rigorous review); FINRA Rule 3110 (supervision); SEC Rule 605 (17 CFR 242.605, market center execution quality reports) and Rule 606 (17 CFR 242.606, broker order routing reports), as amended by SEC release 34-99679 (March 6 2024) [verify exact release and effective dates]; FINRA Regulatory Notices on best execution including 15-46 (Nov 2015) and the 2024 best-execution refresh [verify].

## Source anchors

- 17 CFR 275.206 / Investment Advisers Act §206 — fiduciary duty.
- SEC Commission Interpretation Regarding Standard of Conduct for Investment Advisers, Release IA-5248 (June 5 2019) — best-execution as part of duty of care.
- 15 USC 78bb(e) / Exchange Act §28(e) — soft dollar safe harbor.
- 15 USC 80a-17(e) / Investment Company Act §17(e) — affiliated brokerage.
- FINRA Rule 5310 — Best Execution and Interpositioning, including Supplementary Material .01-.09.
  - .09 "regular and rigorous review" of execution quality.
  - .01 list of factors: character of the market, size and type of transaction, number of markets checked, accessibility of the quotation, terms and conditions of the order.
- FINRA Rule 3110 — supervision, including written supervisory procedures for best execution.
- 17 CFR 242.605 — market center disclosure of execution quality (as amended 2024) [verify].
- 17 CFR 242.606 — broker-dealer disclosure of order routing (as amended 2018, 2024) [verify].
- SEC Final Rule, "Disclosure of Order Execution Information," Release 34-99679 (Mar 6 2024). [verify release number and exact name]
- SEC IM Guidance: best-execution position from the 1986 Kidder Peabody and subsequent letters; SEC v. Robare Group (2018) [verify cite] context for §206 disclosures of brokerage and conflict.
- SEC Examination Risk Alert on best execution (recent — periodic). [verify which release covers 2024-2026 priorities]
- SEC Division of Examinations Annual Examination Priorities (current year) — best-execution and trading practices typically appear annually. [verify current year coverage]
- For fund context: Form N-CEN, Form N-CSR best-execution disclosures; 15(c) board materials practice as documented in fund-board governance literature.

## Sector overlays needed

Only `capital-markets`. This skill is sector-unique. No banking/insurance/payments overlay file under `references/sector-overlays/`.

Sub-flavors inside the capital-markets overlay (handled in the SKILL.md, not as separate sector files):
- Investment adviser flow (Advisers Act §206 fiduciary best-execution).
- Broker-dealer flow (FINRA Rule 5310 "regular and rigorous" review).
- Fund flow (adviser's best-execution review feeding 15(c) board materials and §17(e), §28(e) reporting).

## Cross-cutting overlays needed

- `cyber.md` — venue and connectivity outage incidents, market-data integrity events, SOR/EMS/OMS resilience as it affects execution quality. Square with SEC Reg SCI for covered entities and Reg S-P safeguarding of trade data.
- `conduct.md` — payment for order flow conflicts; principal trade and agency cross conflicts under Advisers Act §206(3); soft-dollar conflicts under §28(e); affiliated-broker conflicts under ICA §17(e); how the conflict factors into the best-execution determination, not just the disclosure.

## Output template named sections

1. Review identification (firm, registration type — IA / BD / both, review period, asset classes covered, venue scope, sample basis)
2. Scope and source posture (data feeds, TCA vendor, exception thresholds, sample method, exclusions)
3. Aggregate execution-quality metrics (per venue / counterparty / asset class: fill rate, price improvement, effective-over-quoted ratio, at-or-better fills, average spread, market-on-close performance, large-block performance)
4. Rule 605/606 reconciliation (where applicable: own routing report figures vs. internal data; venue 605 disclosures vs. observed quality)
5. Trade-exception sampling (sampled trades, miss type, factor analysis under Rule 5310 .01 / IA fiduciary factors, root cause, remediation note)
6. Conflict and best-execution analysis (PFOF, principal trades §206(3), agency crosses §206(3), affiliated brokerage §17(e), soft-dollar §28(e) — for each: how it was weighed in the best-execution determination, evidence)
7. Venue / counterparty review and changes (added, removed, on watchlist; rationale)
8. Findings, exceptions, and corrective actions (with owner and target date)
9. Best-ex committee escalation pack (committee membership, materials reviewed, decisions, dissents, follow-ups)
10. Fund 15(c) escalation (where applicable: fund-by-fund best-execution attestation, soft-dollar usage, affiliated-brokerage usage, escalation to fund board)
11. Source trace and confidence

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| review_id | string | Stable ID |
| firm_registration | enum {IA, BD, IA_and_BD, fund_adviser} | Drives applicable rule set |
| review_period | object {start_date, end_date} | Period covered |
| asset_class_scope | array<enum {equities, options, fixed_income, etfs, mutual_funds, derivatives, fx, crypto, other}> | Coverage |
| venues | array<{venue_id, venue_type, status, watchlist_flag, period_share}> | Venue inventory |
| aggregate_metrics | array<{venue_id, asset_class, metric, value, period, threshold, breach_flag}> | Aggregate measures |
| rule_605_606_reconciliation | object {applicable, deltas_summary, material_anomalies, source_pin} | 605/606 cross-check |
| sample_basis | object {method, size, period_coverage, exclusions} | Sampling design |
| exceptions | array<{trade_id, miss_type, factor_analysis, root_cause, remediation, owner, due_date}> | Per sampled exception |
| conflict_review | object {pfof_present, pfof_treatment, principal_trades_count, agency_cross_count, affiliated_brokerage_share, soft_dollar_arrangements, conflict_in_best_ex_determination} | Conflict overlay |
| committee_pack | object {meeting_date, members_present, materials_reviewed, decisions, dissents, follow_ups} | Committee minutes |
| fund_15c_attestation | array<{fund_id, attestation_status, soft_dollar_summary, affiliated_brokerage_summary, escalation_to_board}> | Fund overlay |
| findings | array<{finding_id, severity, description, control_owner, due_date}> | Findings |
| confidence | enum {high, medium, low, unknown} | Reviewer confidence |
| open_questions | array<{question, blocker_for}> | Items needing legal/PM/trading input |

## Example scenarios (public-source-derived)

1. **IA quarterly best-execution review with PFOF and principal trade exposure.** A dual-registered IA/BD has retail equity flow routed to two market-makers paying PFOF, plus an institutional desk that occasionally crosses agency and principal under Advisers Act §206(3). The skill samples 50 retail trades for price improvement vs. NBBO, reconciles against the firm's most recent Rule 606 report, and runs the §206(3) cross-trade documentation check (written disclosure, client consent per transaction). Finding: aggregate metrics within tolerance, but two principal trades lack the specific transactional consent document; PFOF disclosure in Form ADV is present but the best-execution committee minutes do not record the conflict in the determination. [pattern derived from public Risk Alerts on best execution and Robare-style §206 conflict disclosures; verify exact public source]

2. **Fund adviser preparing 15(c) board pack with soft-dollar arrangements.** A registered fund's adviser is preparing the 15(c) materials. Soft dollars are used for third-party research under §28(e). The skill assembles the soft-dollar review (eligible products only, mixed-use allocation method, dollar volume per provider), reconciles broker selection against the best-execution committee's approved list, samples 25 fund trades for execution-quality review, and produces the affiliated-brokerage disclosure under §17(e). Finding: one mixed-use product (a market-data feed used 80% for research, 20% for operational use) was treated 100% as soft-dollar eligible; the §17(e)(1) "reasonable and fair" attestation needs supporting comparable-rate evidence.

## Common pitfalls

1. Treating "best execution" as best price. It is a multi-factor analysis. The factor list under Rule 5310 .01 and the IA fiduciary equivalent is non-exhaustive.
2. Confusing the broker-dealer regular-and-rigorous review (Rule 5310) with the IA fiduciary review (§206). They overlap in factors but the standards and documentation expectations differ. Dual registrants must document both.
3. Treating Rule 606 as the best-execution review. 606 is a routing-disclosure obligation; it does not itself satisfy the fiduciary or Rule 5310 review obligation.
4. Skipping the conflict-as-input step. PFOF, principal trades, agency crosses, affiliated brokerage, and soft dollars must be weighed in the best-execution determination, not just disclosed alongside it.
5. Soft-dollar mixed-use without proportional allocation. §28(e) requires that mixed-use products be allocated between research (eligible) and non-research (ineligible) based on a reasonable methodology and documented.
6. ICA §17(e) reasonable-and-fair compensation for affiliated-broker trades treated as "we used them" without a comparable-rate benchmark.
7. Sample sizes calibrated for the median trade, not for the tail. Block trades, illiquid bonds, and after-hours fills are where best-execution issues concentrate. Stratify the sample.
8. Fund 15(c) section copy-pasted year-on-year. Boards expect period-specific data and exception detail. A boilerplate attestation is itself a finding pattern in OCIE/EXAMS sweeps.
