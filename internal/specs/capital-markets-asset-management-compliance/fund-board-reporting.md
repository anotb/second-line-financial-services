# Spec: fund-board-reporting

Plugin: capital-markets-asset-management-compliance
Status: phase 1 spec sheet, pending phase 2 build
Date: 2026-05-06
Sector overlay: capital-markets (registered investment company boards under the Investment Company Act of 1940)

## Activation-tuned development description

Assembles the periodic compliance and risk pack delivered to the board of a registered investment company (mutual fund, ETF, closed-end fund, BDC). Covers the Rule 38a-1 chief compliance officer report (annual written report on operation and adequacy of compliance program), 15(c) advisory contract renewal materials (the "Gartenberg" factors), service-provider compliance program oversight (transfer agent, custodian, fund accountant, distributor, sub-advisers), liquidity risk management (Rule 22e-4), valuation oversight (Rule 2a-5), derivatives risk (Rule 18f-4), and material compliance matters since the prior report. Output is the reviewable artifact the fund's CCO and independent trustees consume, with material compliance matters surfaced and 15(c) inputs assembled.

Best for:
- A fund CCO is preparing the annual Rule 38a-1(a)(4)(iii) written report to the board on the operation of the fund's and each service provider's compliance program.
- A fund secretary or fund-administration compliance team is preparing the quarterly compliance section of the board pack.
- An adviser is preparing the 15(c) advisory-contract renewal materials covering the Gartenberg factors (nature/extent/quality of services; investment performance; profitability; economies of scale; fall-out benefits; comparative fees and expenses).
- A fund board secretariat is assembling material compliance matters, MCEs, exceptions, breaches of investment limitations, valuation overrides, derivatives risk events, and liquidity classification breaches for the trustee meeting.

Not the right tool when:
- The institution is not a registered investment company (out of scope; private fund advisers use a different reporting cadence — use risk-reporting/risk-committee-pack with the capital-markets overlay).
- The deliverable is the adviser's enterprise risk committee pack (use risk-reporting/risk-committee-pack).
- The deliverable is a single MCE write-up (use risk-compliance-core/issue-writeup).
- The deliverable is the adviser's Rule 206(4)-7 annual review (use risk-compliance-core/policy-gap-review or adviser-exam-readiness in this plugin).

Anchored to: Investment Company Act §38a-1 / Rule 38a-1 (compliance programs of investment companies and investment advisers); ICA §15(c) (advisory contract renewal); Gartenberg v. Merrill Lynch Asset Management (2nd Cir. 1982) and Jones v. Harris Associates (S. Ct. 2010) for the §15(c) factor analysis; Rule 22e-4 (Investment Company Liquidity Risk Management Programs, adopted Oct 2016); Rule 2a-5 (Good Faith Determinations of Fair Value, compliance date Sept 8 2022); Rule 18f-4 (Derivatives Use by Registered Investment Companies, compliance date Aug 19 2022); Rule 17a-7 (affiliated cross trades); Rule 17e-1 (affiliated brokerage); ICA §17(e); ICA §10(a) board independence; Form N-CEN; Form N-CSR; SEC Examination Priorities (current year) on fund governance and 38a-1.

## Source anchors

- 17 CFR 270.38a-1 — fund and adviser compliance programs.
  - (a)(1) policies and procedures.
  - (a)(2) board approval.
  - (a)(3) annual review of adequacy and effectiveness.
  - (a)(4) chief compliance officer designation, reporting line to board, written annual report to board, and protection from removal without board approval.
- 15 USC 80a-15(c) — advisory contract approval; the §15(c) materials request.
- Gartenberg v. Merrill Lynch Asset Management Inc., 694 F.2d 923 (2d Cir. 1982).
- Jones v. Harris Associates L.P., 559 U.S. 335 (2010).
- 17 CFR 270.22e-4 — Liquidity Risk Management Programs (LRMP).
  - LRMP elements; classification buckets; highly liquid investment minimum (HLIM); 15% illiquid limit; board approval/oversight.
- 17 CFR 270.2a-5 — Fair Value Determinations.
  - Board may designate the valuation designee (typically the adviser); board oversight obligations; periodic and prompt reporting; valuation testing.
- 17 CFR 270.18f-4 — Derivatives Risk Management Program (DRMP).
  - Derivatives risk manager; VaR-based limit (relative or absolute); stress testing; backtesting; board reporting; limited derivatives user exemption.
- 17 CFR 270.17a-7 — affiliated cross trades.
- 17 CFR 270.17e-1 — affiliated brokerage.
- 15 USC 80a-10 — board composition.
- SEC Form N-CEN (annual census report). [verify current schedule]
- SEC Form N-CSR (semi-annual shareholder report).
- SEC Division of Examinations Annual Examination Priorities (current year), section on registered funds. [verify current year]
- SEC adopted rules on shareholder reports and fee disclosures, "tailored shareholder reports" (effective July 24 2024). [verify exact citation]
- SEC Names Rule, Rule 35d-1 (revised Sept 20 2023), 80% investment policy. [verify post-rulemaking compliance dates]

## Sector overlays needed

Only `capital-markets`. Skill is sector-unique. No banking/insurance/payments overlay file under `references/sector-overlays/`.

## Cross-cutting overlays needed

- `cyber.md` — Reg S-P safeguarding (as amended 2024); SEC cyber proposed rule for advisers and funds (proposal status [verify current state]); breach notice posture for fund shareholders; cyber events material to the §38a-1 report; service-provider cyber events.
- `conduct.md` — affiliated transactions (§17(a), 17(e), Rule 17a-7), payment-for-order-flow at fund level, sub-adviser conflict review.
- `climate.md` — Names Rule (Rule 35d-1) ESG fund naming compliance; ESG-labeled fund disclosures; greenwashing risk in shareholder reports.

## Output template named sections

1. Reporting period and meeting context (board meeting date, prior-period meeting date, scope of report)
2. Executive summary for trustees (max 5 bullets, MCM count, residual issue summary, escalations)
3. Rule 38a-1 annual written report (where applicable)
   - Operation of the fund's compliance program
   - Operation of each service provider's compliance program (transfer agent, custodian, fund accountant, distributor, sub-advisers, valuation designee, principal underwriter)
   - Material compliance matters since the prior report
   - Material changes to policies and procedures
   - CCO recommendation regarding adequacy
4. 15(c) advisory contract renewal pack (where applicable)
   - Nature, extent, quality of services
   - Investment performance (period, benchmark, peer comparison)
   - Profitability of the adviser from the fund relationship
   - Economies of scale and breakpoints
   - Fall-out benefits to the adviser and affiliates
   - Comparative fees and expenses (peer group, methodology pin)
   - Trustee questions and adviser responses
5. Liquidity risk management report (Rule 22e-4): classification distribution, HLIM compliance, 15% illiquid bucket, breaches, restorations
6. Valuation oversight (Rule 2a-5): valuation designee report summary, fair-value events, overrides, testing results, prompt-notification events
7. Derivatives risk (Rule 18f-4): VaR utilization vs. limit, breaches, stress test summary, backtesting exceptions, derivatives risk manager report
8. Affiliated transactions: 17a-7 cross trades, 17e-1 affiliated brokerage activity, related-person disclosures
9. Service-provider compliance summary: each provider's compliance program adequacy, material exceptions, oversight evidence
10. Cyber and operational resilience events (where applicable)
11. Open issues and management actions (with owner, due date, escalation flag)
12. Source trace and confidence

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| report_id | string | Stable ID |
| board_meeting | object {date, prior_meeting_date, type: regular/special} | Meeting context |
| funds_in_scope | array<{fund_id, fund_name, fund_type, fiscal_year_end}> | Funds covered |
| report_type | enum {quarterly_compliance_section, annual_38a_1, 15c_renewal_pack, ad_hoc_escalation} | Drives required sections |
| material_compliance_matters | array<{mcm_id, fund_id, description, root_cause, remediation_status, escalation_level, owner}> | MCM list |
| service_provider_oversight | array<{provider_id, provider_type, program_adequacy, exceptions, evidence_pin}> | Per provider |
| section_15c | object {nature_extent_quality, performance_summary, profitability_summary, economies_of_scale, fall_out_benefits, comparative_fees, peer_group_methodology, trustee_questions} | §15(c) pack |
| liquidity_22e_4 | object {classification_distribution, hlim_status, illiquid_bucket_status, breaches, restorations} | LRMP |
| valuation_2a_5 | object {valuation_designee, fair_value_events, overrides, testing_results, prompt_notifications} | Rule 2a-5 |
| derivatives_18f_4 | object {limited_user, var_type, var_utilization, breaches, stress_test_summary, backtesting_exceptions} | Rule 18f-4 |
| affiliated_transactions | object {17a_7_count, 17e_1_count, related_persons, notable_events} | §17 transactions |
| cyber_resilience_events | array<{event_id, severity, fund_impact, customer_impact, remediation, regulator_notice}> | Cyber overlay |
| open_issues | array<{issue_id, severity, due_date, owner}> | Outstanding |
| confidence | enum {high, medium, low, unknown} | Reviewer confidence |
| open_questions | array<{question, blocker_for}> | Items needing legal/board input |

## Example scenarios (public-source-derived)

1. **Annual 38a-1 written report with sub-adviser MCM.** A multi-manager fund's CCO is delivering the annual 38a-1 written report. A sub-adviser had a material compliance matter during the period: a personal trading violation under its Rule 204A-1 code of ethics, self-reported and remediated. The skill assembles the 38a-1 report covering the fund, the adviser, and each sub-adviser; surfaces the MCM with root cause, remediation, and the sub-adviser's CCO attestation; documents the parent CCO's oversight of the sub-adviser's compliance program; and proposes the recommendation language on adequacy. [pattern derived from public sub-adviser compliance disclosure practice]

2. **15(c) renewal with profitability and economies-of-scale challenge.** Independent trustees in advance of contract renewal request enhanced detail on the adviser's profitability allocation methodology, fall-out benefits (including soft-dollar credits and affiliated-broker revenue), and economies-of-scale realization given AUM growth without breakpoint reduction. The skill structures the §15(c) pack against the Gartenberg factors as interpreted in Jones v. Harris, pulls the comparative-fees peer set with methodology pin, surfaces fall-out benefits including 12b-1 distribution flows, and lists the trustee questions with adviser responses. Identified gap: AUM has grown 40% since the last breakpoint adjustment four years ago; the materials do not contain a written analysis of why no further breakpoint is appropriate. Pattern derived from publicly disclosed §15(c) practice and excessive-fee litigation themes. [verify any specific public order]

## Common pitfalls

1. Treating the 38a-1 written report as a list of incidents. It is a written assessment of the operation and adequacy of the compliance program, not just a logbook. Material compliance matters must be assessed (root cause, recurrence risk), not merely listed.
2. Sub-adviser oversight gap. The fund's CCO must reasonably believe the sub-adviser's compliance program is adequate. A sub-adviser CCO attestation alone is not enough; oversight evidence must support the belief.
3. §15(c) profitability without methodology. Boards expect a defined profitability methodology (direct expense allocation, indirect cost basis, capital usage). A bare number is a finding pattern in fee-litigation discovery.
4. Liquidity classification static. Rule 22e-4 classifications must be reasonably current; a quarterly snapshot in a stressed market is stale by the time the board reads it. Note classification timing and any market-change triggers.
5. Rule 2a-5 valuation designee report missing prompt-notification events. The rule requires prompt board notification of matters that materially affect the fair value of investments. Quarterly summary alone is insufficient if material events occurred mid-period.
6. Rule 18f-4 limited derivatives user status used without monitoring the 10% notional threshold. Status can flip mid-period; report must reflect either continuous compliance or a transition to full DRMP.
7. Affiliated transaction reporting that lists counts without context. The board needs to see the conflict shape: 17a-7 pricing methodology evidence, 17e-1 reasonable-and-fair attestation, related-person definitions used.
8. Boilerplate trustee questions. Independent trustees in 15(c) renewal materials look for evidence of substantive challenge. Recycled prior-year questions without period-specific updates is itself a finding pattern.
9. Tailored shareholder report disclosures (effective 2024) treated as a fund-marketing exercise rather than a board-oversight item. The board oversees the disclosure process. [verify rule effective date and applicability]
