# Capital markets sector overlay for fund-board-reporting

This skill is sector-unique to capital markets — registered investment companies under the Investment Company Act of 1940 and their advisers under the Investment Advisers Act of 1940. The overlay is the substantive frame for the entire skill, not an addition to a generic capability default. Other sectors (banking, insurance, payments-fintech) do not have a parallel artifact and there are no overlay files for them under this skill.

Loaded by: `fund-board-reporting/SKILL.md` for every invocation. The overlay sits in this directory for symmetry with sibling capability skills and for any future fund-complex variant overlays.

## Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators, rules, and judicial precedents without restating excerpts.

## What the capital-markets frame brings to the artifact

### 1. Fund board, not adviser ERM committee

The artifact is the periodic compliance-and-risk pack delivered to the board of a registered investment company — a mutual fund, ETF, closed-end fund, or business development company — and its independent trustees. It is not the adviser's enterprise risk committee pack. The audiences differ; the statutory hooks differ; the recommendations differ.

Adviser-level risk content (firm-wide investment risk, fiduciary risk, vendor risk at the firm level, BD net-capital and customer-protection content for dual-registrant firms) belongs in `risk-reporting/skills/risk-committee-pack` with the capital-markets sector overlay loaded. Where an item is material to both audiences, the two packs cross-link rather than collapse.

### 2. Registered-fund types in scope

The skill covers all registered investment company types: open-end mutual funds, ETFs (including those operating under Rule 6c-11), closed-end funds, and BDCs. Rule applicability varies by fund type and the artifact reflects that:

- Rule 22e-4 (liquidity) applies to open-end funds other than money market funds and ETFs operating under Rule 6c-11 with limited modifications. Closed-end funds and BDCs are out of scope for 22e-4; their liquidity reporting follows the registration statement and any board-adopted policy.
- Rule 2a-7 (money market funds) applies only to money market funds and brings its own board-reporting cadence; this skill carries the 2a-5 / 22e-4 / 18f-4 trio for non-MMFs and notes the 2a-7 substitution for MMFs.
- Rule 18f-4 (derivatives) applies to all registered investment companies and BDCs. Limited-derivatives-user status is a fund-by-fund determination.
- Rule 6c-11 (ETF operations) carries its own board-oversight expectations including for custom-basket procedures; ETF complexes integrate this content.

The skill expects the user to identify the funds in scope and the fund types; the artifact adapts.

### 3. Statutory and rule lattice the board owns

The fund board's compliance-and-risk oversight is anchored in the Investment Company Act and the rules thereunder. The artifact is shaped by:

- ICA §15(c) — advisory contract approval and renewal, with the Gartenberg / Jones v. Harris factor analysis.
- ICA §10(a) and §2(a)(19) — board independence; 75% independent-trustee threshold for reliance on the Independent Director exemptive rules.
- ICA §17 (and Rules 17a-7, 17e-1) — affiliated transactions; board determinations and procedure-adequacy reviews.
- Rule 38a-1 — fund and service-provider compliance program; CCO annual written report; CCO reporting line and removal protection.
- Rule 22e-4 — liquidity risk management program; board approval; annual program-administrator report.
- Rule 2a-5 — fair-value determinations; valuation designee designation; quarterly and prompt board reporting.
- Rule 18f-4 — derivatives risk management program; derivatives risk manager designation; annual report; VaR-breach reporting.
- Rule 35d-1 — fund-name 80% policy.
- Securities Exchange Act §28(e) — soft-dollar safe harbor; board disclosure of adviser's commission practices.

The board acts on these rules through documented determinations recorded in board minutes; the artifact is the supporting pack that informs those determinations.

### 4. Service-provider compliance program oversight

Rule 38a-1(a)(2) requires board approval of the policies and procedures of each "service provider" — defined to include the adviser, sub-advisers, principal underwriter, administrator, and transfer agent. The fund's CCO must reasonably believe each service provider's compliance program is adequate.

The artifact carries per-service-provider content: program adequacy assessment, material exceptions in the period, oversight evidence (CCO attestations supplemented by independent oversight artifacts — testing, examination findings, third-party reports), and any service-provider transition activity. A sub-adviser CCO attestation alone does not satisfy the oversight expectation; the parent CCO's oversight must rest on evidence the parent CCO has reviewed.

### 5. Sub-adviser oversight specifically

Multi-manager funds bring a distinct oversight surface. Sub-adviser oversight content in the artifact covers:

- Code of ethics reach into the sub-adviser (Rule 17j-1, Rule 204A-1) and any personal-trading violations or pre-clearance failures.
- Performance and risk attribution at the sub-adviser sleeve level.
- Trading practices including soft-dollar use, broker selection, and any affiliated-broker activity.
- Material compliance matters at the sub-adviser, including any matters that triggered a sub-adviser CCO escalation to the parent.
- Sub-adviser termination, replacement, or significant scope change activity in the period; ICA §15 considerations for any contract change.

The artifact distinguishes parent-CCO oversight evidence from sub-adviser self-attestation throughout.

### 6. Soft-dollar, brokerage, and §17(e) affiliated-brokerage disclosures

The artifact carries a defined affiliated-transactions and brokerage-disclosure section reporting:

- §28(e) soft-dollar use: total commissions paid for research and brokerage; adviser's commission-allocation methodology; eligibility analysis; any policy change in the period; MiFID II hard-dollar treatment where applicable.
- Rule 17e-1 affiliated brokerage: aggregate commissions paid to affiliated brokers; the board's quarterly procedure-adequacy determination; any procedure exception in the period.
- Rule 17a-7 affiliated cross trades: count and aggregate value of cross trades; the pricing methodology and the §17a-7 conditions analysis; any procedure exception.
- §17(a) and Rule 17a-8 affiliated transactions more broadly; related-person transactions in the period.

Counts without context are insufficient; each item carries the conflict shape, the procedure-adequacy evidence, and any exception.

### 7. Valuation oversight under Rule 2a-5

The board pack carries the valuation-designee report content:

- Valuation designee identification (typically the adviser or a sub-adviser); designation date and any change in the period.
- Quarterly written report from the valuation designee covering valuation risks, methodology changes, testing results, pricing-vendor oversight, and any material valuation events.
- Prompt-notification log: any matter the valuation designee promptly notified the board about during the period (the rule requires notification no later than five business days after the designee becomes aware), with the materiality assessment, the action taken, and any remediation.
- Fair-value override summary: instances where the designee's fair-value determination differed from the pricing-vendor mark, with the rationale and the recurrence pattern.

A quarterly summary alone is insufficient if material events occurred mid-period; the prompt-notification log is the test.

### 8. Liquidity risk management under Rule 22e-4

The board pack carries the liquidity program administrator's report content for in-scope open-end funds (non-MMF, non-ETF unless 22e-4 applicable):

- Classification distribution as of the reporting date and movement during the period: percentage of fund net assets in highly liquid, moderately liquid, less liquid, and illiquid buckets.
- Highly liquid investment minimum (HLIM) where applicable: current HLIM, any board-approved change, breach status and restoration.
- 15% illiquid limit: status, any breach (the rule prohibits acquiring additional illiquid investments above the 15% limit), board notification of any breach.
- Annual program-administrator report content: any program changes, any operational issues with classification, vendor and methodology pin.
- Stressed-market overlay: classifications must be reasonably current; a quarterly snapshot in a stressed market is stale; the report should address market-change-trigger reclassifications.

### 9. Derivatives risk management under Rule 18f-4

The board pack carries the derivatives risk manager's report content for in-scope funds:

- Limited-derivatives-user status (10% threshold) and any transition during the period to or from full DRMP.
- VaR-based limit type (relative VaR or absolute VaR), the designated reference index where relative VaR is used, and current VaR utilization against limit.
- Any VaR-limit breaches in the period, the duration, the corrective action, and the board notification.
- Stress-test summary: methodology, frequency, and material results.
- Backtesting exceptions: exception count and analysis.
- Annual derivatives risk manager report content covering program adequacy, material risks, and any program changes.

### 10. Marketing Rule and adviser-level content surfaced to the board

Rule 206(4)-1 (the Marketing Rule) is an adviser-level rule, not a fund-level rule, but material marketing-rule findings affecting the fund (hypothetical performance presented in fund marketing, testimonials and endorsements, third-party ratings, performance presentation methodology) appear in the board pack as part of the §15(c) materials (nature, extent, quality of services) and the 38a-1 service-provider compliance program assessment for the adviser.

Detail of marketing-rule evidence and substantiation lives in the sibling skill `marketing-rule-evidence`.

### 11. Form N-CEN and Form N-CSR cross-checks

The board pack does not file N-CEN or N-CSR, but the pack content informs both:

- N-CEN: rule-reliance disclosures (Rule 18f-4 limited-derivatives-user status, Rule 17a-7 cross-trade reliance, Rule 17e-1 affiliated brokerage), service-provider identification, and board-composition information all appear in N-CEN. The board should be aware of the rule-reliance disclosures the adviser will submit.
- N-CSR: shareholder report disclosures and SOX certifications. The Tailored Shareholder Report rules (compliance date July 24, 2024) restructured the open-end fund shareholder-report content; the board oversees the disclosure-program implementation.

### 12. Cross-link to other capability and sector skills

- Adviser-level risk committee pack (firm-wide ERM): `risk-reporting/skills/risk-committee-pack` with capital-markets sector overlay.
- Adviser exam-readiness sprint (SEC EXAMS, FINRA exam): `capital-markets-asset-management-compliance/skills/adviser-exam-readiness`.
- Best-execution surveillance and best-ex committee pack: `capital-markets-asset-management-compliance/skills/best-execution-surveillance`.
- Marketing Rule evidence and substantiation: `capital-markets-asset-management-compliance/skills/marketing-rule-evidence`.
- Single-issue write-up for a material compliance matter: `risk-compliance-core/skills/issue-writeup`.
- Adviser policy gap review under Rule 206(4)-7: `risk-compliance-core/skills/policy-gap-review` chained with `adviser-exam-readiness`.
- Cyber-disclosure-decision content for the adviser's public parent: `risk-reporting/skills/cyber-disclosure-readiness`.

## Capital-markets-specific output content

The artifact's named-section content (PowerPoint deck plus Word annex) is the capital-markets output. The deck-and-annex structure is described in `templates/default-output.md`. Key capital-markets sections that the artifact carries:

- Executive summary for trustees: MCM count, 38a-1 recommendation summary, escalations, decisions.
- Rule 38a-1 annual written report (annual cycle): operation of the fund's compliance program; operation of each service provider's compliance program; material compliance matters since the prior report; material policy changes; CCO recommendation.
- §15(c) advisory contract renewal package (annual cycle): nature/extent/quality; performance; profitability; economies of scale; fall-out benefits; comparative fees; trustee questions and adviser responses.
- Compliance and risk reporting cadence (every cycle): material compliance matters in the period; service-provider compliance summary; affiliated transactions including §17(e), Rule 17e-1, Rule 17a-7, §17(a); soft-dollar / §28(e) disclosure.
- Rule 22e-4 liquidity report.
- Rule 2a-5 valuation oversight including prompt-notification log.
- Rule 18f-4 derivatives risk report including VaR utilization.
- Cyber and operational resilience events affecting fund operations or shareholder data.
- Open issues and management actions with owner role and due date.
- Source trace and confidence label.

## Common pitfalls in fund-board-reporting

- Treating the 38a-1 written report as a logbook of incidents. The rule requires an assessment of the operation and adequacy of the compliance program; material compliance matters must be assessed (root cause, recurrence risk), not merely listed.
- Sub-adviser oversight resting on the sub-adviser CCO attestation alone. The parent CCO must reasonably believe the sub-adviser's program is adequate; oversight evidence (testing, exam findings, third-party reports) supports the belief.
- §15(c) profitability without methodology. Boards expect a defined profitability methodology (direct expense allocation, indirect cost basis, capital usage). A bare number is the finding pattern in §36(b) fee-litigation discovery.
- Liquidity classification static. Rule 22e-4 classifications must be reasonably current; a quarterly snapshot in a stressed market is stale by the time the board reads it. Note classification timing and any market-change triggers.
- Rule 2a-5 valuation designee report missing prompt-notification events. Quarterly summary alone is insufficient if material events occurred mid-period.
- Rule 18f-4 limited-derivatives-user status used without monitoring the 10% notional threshold. The status can flip mid-period; the report must reflect either continuous compliance or a transition to full DRMP.
- Affiliated-transaction reporting that lists counts without conflict-shape context. The board needs Rule 17a-7 pricing methodology evidence and Rule 17e-1 reasonable-and-fair attestation, not just numbers.
- Boilerplate trustee questions. Independent trustees in §15(c) renewal materials look for evidence of substantive challenge; recycled prior-year questions without period-specific updates is itself a finding pattern in §36(b) discovery.
- Tailored shareholder report disclosures treated as a marketing exercise rather than a board-oversight item. The board oversees the disclosure process.
- Conflating the adviser ERM committee pack with the fund board pack. Audiences differ; statutory hooks differ; the artifacts are distinct and cross-link rather than collapse.
