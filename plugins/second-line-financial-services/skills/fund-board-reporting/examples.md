# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## annual-38a-1-multi-manager

### Example: annual Rule 38a-1 written report at a multi-manager fund complex with a sub-adviser MCM

Public-source-derived. No named institution. The shape mirrors the standing annual cycle at a multi-manager fund complex with several sub-advisers, where one sub-adviser had a material compliance matter during the period and self-reported.

#### Input

- Trust / fund complex: open-end mutual fund trust with eight series funds, four of which are multi-manager (parent adviser plus one to three sub-advisers each); two ETFs operating under Rule 6c-11; one money market fund under Rule 2a-7.
- Engagement scope supplied: primary regulators SEC (Investment Management) and the relevant state securities regulators for state-registered intermediaries; persona = fund CCO, with the trust's board secretariat as drafter; sector overlay = capital-markets (loaded for every invocation of this skill); cross-cutting overlays = cyber (loaded because of two service-provider Reg S-P customer-information events in the period and because the parent adviser is a subsidiary of a public-company asset-management group) and conduct (loaded because the §15(c) renewal pack is in scope this cycle for one of the eight funds and because of the sub-adviser MCM); climate not loaded (the trust does not operate ESG-labeled funds and Rule 35d-1 ESG-name considerations are not in scope this period); source posture = public-plus-firm-policy-plus-system-of-record-evidence.
- Period: full year ending [fiscal year end]; annual standing meeting of the Board of Trustees.
- Report type: annual Rule 38a-1 written report; one §15(c) advisory contract renewal pack for the in-renewal fund; standing quarterly compliance section; standing affiliated-transactions and soft-dollar disclosure.
- Upstream artifacts on file: the parent adviser's Rule 206(4)-7 annual review summary; each sub-adviser's CCO attestation supplemented by parent-CCO testing notes and the most recent SOC 2 Type II reports for the major operational platforms; the transfer agent's annual program summary and the transfer agent's most recent SOC 2 Type II; the custodian's annual program summary; the fund accountant's annual program summary; the distributor's quarterly Rule 12b-1 reports and annual continuance materials; the valuation designee's quarterly written reports for the period and the prompt-notification log (three notifications in the period); the derivatives risk manager's annual report for the two funds in full DRMP and the limited-derivatives-user monitoring evidence for the six funds in limited status; the liquidity program administrator's annual report and the quarterly classification snapshots; the affiliated-transactions log (Rule 17a-7 cross trades count: 12 in the period; Rule 17e-1 affiliated brokerage aggregate: low); the soft-dollar / §28(e) report from the parent adviser; one self-reported sub-adviser MCM (personal-trading violation under Rule 204A-1).

#### Output sketch

##### Deck (PowerPoint)

- **Cover** — trust name, eight funds in scope listed with fund type, meeting date, period, report type = annual Rule 38a-1 with one §15(c) renewal.
- **Executive summary for trustees** — five bullets. Headline: compliance program operating effectively across the trust; one material compliance matter at a sub-adviser (personal-trading violation, self-reported, remediated); two service-provider Reg S-P customer-information events with notice obligation analysis; §15(c) renewal recommendation for the in-renewal fund; 12 affiliated cross trades in the period under Rule 17a-7 with procedure adequacy.
- **Decisions and acknowledgements requested** — three items: (i) annual Rule 38a-1 program approval for the trust and each service provider; (ii) §15(c) advisory contract renewal for the in-renewal fund; (iii) Rule 17e-1 quarterly procedure-adequacy determination for the period.
- **Rule 38a-1 written report** — slide per major section. Per-service-provider summary: parent adviser, three sub-advisers, transfer agent, custodian, fund accountant, distributor, valuation designee, two pricing services. CCO recommendation = adequate with one material compliance matter assessed and remediated.
- **§15(c) renewal pack** — slides per Gartenberg / Jones v. Harris factor for the in-renewal fund. Headline conclusion: trustees deliberation supports renewal subject to substantive trustee questions on profitability methodology and economy-of-scale analysis.
- **Liquidity (Rule 22e-4)** — classification distribution for six in-scope open-end funds (the MMF substitutes Rule 2a-7); one fund had a 15% illiquid-bucket condition during a period of stress with restoration timeline; HLIM compliance maintained across the population.
- **Valuation (Rule 2a-5)** — three prompt-notification events in the period; valuation designee report content; testing results.
- **Derivatives (Rule 18f-4)** — two funds in full DRMP with VaR utilization within limit; six funds in limited-derivatives-user status with continuous monitoring of the 10% threshold.
- **Affiliated transactions** — 12 Rule 17a-7 cross trades with pricing methodology; Rule 17e-1 aggregate with quarterly procedure-adequacy on file; one §17(d) joint transaction with the SEC exemptive-order basis.
- **Soft-dollar / §28(e)** — period commission allocation; eligibility analysis; CSA / CCA arrangements; MiFID II not applicable (no EU client coverage at the parent adviser).
- **Cyber events** — two Reg S-P customer-information events at service providers (one transfer agent, one custodian); customer-notice posture met for both; public-parent disclosure-referral status flagged for one event.
- **Open issues and management actions** — sub-adviser MCM remediation status; service-provider cyber remediation status; one open audit finding affecting the fund accountant.
- **Forward-looking** — Reg S-P May 2024 amendments compliance phase-in status; SEC Cybersecurity Risk Management Rule for Advisers and Funds current state flagged; Tailored Shareholder Report rules implementation status for the open-end fund family; Rule 22e-4 liquidity rule amendment proposal current state flagged.
- **Source trace and sign-off** — confidence label = high on most claims (system-of-record evidence and SOC 2 Type II reports); medium on the sub-adviser MCM root-cause (sub-adviser self-investigation); fund CCO and board secretariat sign-off.

##### Word annex

- All sections of the deck developed at length, plus:
  - Full per-service-provider compliance program assessment (parent CCO's reasonable belief with the evidence basis for each provider; SOC 2 Type II report dates; testing summaries; in-period exam findings affecting any provider).
  - Full §15(c) factor analysis for the in-renewal fund (profitability with methodology pin: direct expense allocation, indirect cost basis, capital usage; fall-out benefits substantively catalogued; comparative fees with peer-group methodology pin; trustee questions and adviser responses on the record).
  - Full sub-adviser MCM write-up (personal-trading violation under Rule 204A-1; self-reported; root cause = pre-clearance system gap that was remediated; recurrence-risk analysis; sub-adviser CCO attestation supplemented by parent-CCO testing of the remediated control).
  - Reg S-P customer-information event analyses for the two service-provider events (event detail; affected information types; customer count affected; notice posture and timing; service-provider remediation status; contractual notification adequacy review).
  - Rule 17a-7 pricing methodology evidence for the 12 cross trades against the four §17a-7 conditions.
  - Source trace mapping every material claim to its source system, evidence reference, and confidence.
  - Reviewer questions for the secretariat to surface in the meeting.

The pack stops at draft. The fund CCO and the board secretariat review before the meeting.

#### Why this scenario matters

- The Rule 38a-1 written report is the substantive annual artifact, not a logbook of incidents. The sub-adviser MCM is assessed (root cause, recurrence risk, remediation status), not merely listed.
- Sub-adviser oversight rests on the parent CCO's reasonable belief in the sub-adviser's compliance program. The sub-adviser CCO's attestation is supplemented by the parent CCO's testing of the remediated control; the §38a-1 expectation is satisfied.
- The §15(c) renewal pack carries methodology pins for profitability and peer-group selection. Trustee questions are substantive and period-specific (AUM growth and economy-of-scale analysis; performance versus benchmark for the period; profitability movement; fall-out benefit changes); recycled prior-year questions are absent.
- The cyber overlay drives the Reg S-P customer-notice analysis for the two service-provider events. The fund retains the customer-notice obligation when fund-shareholder customer information was affected; the pack documents the obligation analysis.
- The conduct overlay drives the §17(e) / Rule 17e-1 procedure-adequacy treatment, the Rule 17a-7 pricing methodology evidence, and the soft-dollar disclosure. Counts without context are insufficient; the pack carries the conflict shape and the procedure adequacy.
- Climate is not in scope this period (no ESG-labeled funds; Rule 35d-1 ESG-name considerations not relevant). The cross-cutting overlay loader respects the scope; the pack does not invent a climate section.

#### Anchors

- ICA §15(c) and the Gartenberg / Jones v. Harris factor analysis (for the in-renewal fund).
- ICA Rule 38a-1 — fund and service-provider compliance programs; CCO annual written report; material compliance matter definition.
- ICA Rule 17a-7 — affiliated cross trades; pricing methodology; §17a-7(e) annual board procedure review.
- ICA §17(e) and Rule 17e-1 — affiliated brokerage; quarterly procedure-adequacy determination.
- ICA Rule 204A-1 — adviser code of ethics; sub-adviser code of ethics under fund-complex sub-adviser oversight loop.
- Securities Exchange Act §28(e) — soft-dollar safe harbor; SEC Release No. 34-54165 (July 2006) interpretive guidance.
- ICA Rule 22e-4 — liquidity risk management program; classification, HLIM, 15% illiquid limit; annual program-administrator report.
- ICA Rule 2a-5 — valuation designee; quarterly written report; prompt-notification log.
- ICA Rule 18f-4 — derivatives risk management program; limited-derivatives-user; VaR-based limit.
- SEC Reg S-P (May 2024 amendments) — customer-information safeguarding; 30-day customer notice posture.

See `references/source-anchors.md` for full citations and verification flags.

## sub-adviser-approval-manager-of-managers

### Example: interim board approval of a new sub-adviser at a multi-manager fund under manager-of-managers exemptive relief

Public-source-derived. No named institution. The shape mirrors an off-cycle special board meeting at a multi-manager fund complex to approve the addition of a new sub-adviser to one fund under the trust's manager-of-managers exemptive relief, without a shareholder vote.

#### Input

- Trust / fund complex: open-end mutual fund trust with eight series funds, four of which are multi-manager (parent adviser plus one to three sub-advisers each). The trust operates under SEC manager-of-managers exemptive relief that permits the parent adviser, subject to board approval, to enter into and materially amend sub-advisory agreements with unaffiliated sub-advisers without a shareholder vote, on the conditions stated in the order (board approval, information statement to shareholders within the prescribed timeline, no increase in aggregate advisory fee, independent-trustee composition condition, prospectus update).
- Engagement scope supplied: primary regulator SEC (Investment Management); persona = fund CCO and parent adviser CCO, with the trust's board secretariat as drafter; sector overlay = capital-markets (loaded for every invocation of this skill); cross-cutting overlays = conduct (loaded because §15(c) factor analysis is the load-bearing fiduciary record) and cyber (loaded because the proposed sub-adviser's operational platforms and SOC 2 Type II posture sit in the program-adequacy assessment); climate not loaded; source posture = public-plus-firm-policy-plus-system-of-record-evidence.
- Period: special board meeting called between standing quarterly meetings; one fund affected (one of the four multi-manager funds); proposed sub-adviser is unaffiliated with the parent adviser; proposed effective date approximately six weeks after the meeting to allow the §15(a) information statement timeline.
- Report type: ad-hoc / interim board pack supporting a §15(c) factor-based deliberation on a new sub-advisory agreement under manager-of-managers exemptive relief; standing quarterly compliance content not in scope (the next standing meeting carries that).
- Upstream artifacts on file: the parent adviser's due-diligence package on the proposed sub-adviser (firm overview, ownership and control, key personnel, investment philosophy and process, performance composite under GIPS, AUM history, regulatory history including most recent Form ADV Parts 1 and 2 and disciplinary disclosures, Rule 206(4)-7 program summary, code of ethics under Rule 204A-1, business-continuity posture, cyber-security posture and most recent SOC 2 Type II for the relevant operational platforms, key-vendor list with criticality, trade-error history for trailing 36 months, soft-dollar posture and CSA / CCA arrangements, MiFID II posture); the proposed sub-advisory agreement and fee schedule; the parent adviser's recommendation memo with the §15(c) factor analysis; the proposed information statement to shareholders compliant with §15(a) information-statement requirements under the exemptive order; the prospectus supplement; the parent CCO's reasonable-belief assessment of the sub-adviser's compliance program; counsel memo confirming the conditions of the exemptive order are satisfied (no increase in aggregate advisory fee at the fund level; independent-trustee composition met; information-statement timeline; no affiliation between parent adviser and proposed sub-adviser).

#### Output sketch

##### Deck (PowerPoint)

- **Cover** — trust name, the one fund affected, meeting type = special board meeting, period = interim, report type = sub-adviser approval under manager-of-managers exemptive relief.
- **Executive summary for trustees** — five bullets. Headline: parent adviser recommends adding the proposed sub-adviser to the affected fund under the trust's manager-of-managers order; the conditions of the order are satisfied per counsel memo; the §15(c) factor analysis supports approval; aggregate advisory fee at the fund level does not increase; information statement to shareholders will issue within the prescribed timeline.
- **Decisions and acknowledgements requested** — three items: (i) approval of the new sub-advisory agreement with the proposed sub-adviser for the affected fund under §15(c), with the documented determination that the agreement is in the best interests of the fund and its shareholders; (ii) acknowledgement that the conditions of the manager-of-managers exemptive order are satisfied (counsel memo on the record); (iii) approval of the prospectus supplement and the information statement to shareholders.
- **Manager-of-managers framework** — slide on the exemptive order's conditions: shareholder-vote relief, board-approval requirement, information-statement timeline, no-increase-in-aggregate-fee condition, independent-trustee composition condition, unaffiliated-sub-adviser scope. Counsel memo cited for current order text and its conditions.
- **§15(c) factor analysis for the proposed sub-advisory agreement** — slide per Gartenberg / Jones v. Harris factor:
  - Nature, extent, and quality of services to be provided by the proposed sub-adviser.
  - Investment performance of the proposed sub-adviser on its representative composite, with benchmark and peer comparison and methodology pin (composite construction, dispersion, period selection rationale).
  - Profitability — proposed sub-adviser's expected profitability from the relationship at projected fund AUM, with methodology pin and the parent adviser's allocation of fund-level profitability across the manager / sub-adviser stack.
  - Economies of scale and breakpoints in the proposed sub-advisory fee schedule with AUM-growth scenarios.
  - Fall-out benefits substantively catalogued (soft-dollar / CSA / CCA arrangements, affiliated-broker considerations if any, revenue-sharing if any, related-party arrangements).
  - Comparative fees with peer-group methodology pin (peer set definition, fee-band selection, sub-advisory-versus-aggregate framing).
  - Trustee questions and adviser responses on the record (substantive and period-specific; not recycled prior-year).
- **Proposed sub-adviser compliance program assessment** — Rule 38a-1(a)(2) program adequacy at the moment of approval. Parent CCO's reasonable belief in the proposed sub-adviser's program with the evidence basis: Form ADV Parts 1 and 2 review, Rule 206(4)-7 program summary, code of ethics under Rule 204A-1, recent disciplinary history, SOC 2 Type II report dates, business-continuity posture, cyber-security posture. Three-year forward expectation on oversight cadence (quarterly CCO reports plus parent-CCO testing of named controls).
- **Operational and cyber assessment of the proposed sub-adviser** — SOC 2 Type II report status for the major operational platforms (portfolio-management system, order-management system, trade-allocation engine, reconciliation platform); cyber posture and any in-period security incidents; vendor-risk posture for the proposed sub-adviser's key vendors. Reg S-P customer-information safeguarding posture under the May 2024 amendments.
- **Affiliated-transactions and soft-dollar posture of the proposed sub-adviser** — affiliated-broker arrangements (none expected in this matter), §28(e) eligibility analysis on the soft-dollar / CSA program, MiFID II treatment, code-of-ethics and personal-trading posture under Rule 204A-1.
- **Information statement and prospectus disclosure** — content of the §15(a) information statement to shareholders (description of the new sub-adviser, the new sub-advisory agreement, the §15(c) board determination, comparative performance, no-fee-increase confirmation); prospectus supplement adding the sub-adviser to the affected fund's strategy disclosure and the principal-risks framing where the strategy implementation changes; timeline against the exemptive-order condition.
- **Conditions and undertakings** — restated conditions of the exemptive order with counsel-memo citation; trustee determination that the conditions are satisfied; ongoing-condition monitoring (independent-trustee composition; aggregate-fee constraint; information-statement timeline).
- **Forward-looking** — the sub-adviser's first standing quarterly cycle posture; first parent-CCO testing window on the new sub-adviser's named controls; transition-period operational considerations (account opening at the custodian, security-master onboarding, model-portfolio handover, position-transfer plan if any).
- **Source trace and sign-off** — confidence label = high on the §15(c) factor analysis (parent adviser's recommendation memo with documented methodology) and on the conditions-of-the-order analysis (counsel memo); medium on the proposed sub-adviser's profitability and economies-of-scale projections (forward-looking estimates); fund CCO and board secretariat sign-off.

##### Word annex

- All sections of the deck developed at length, plus:
  - Full §15(c) factor analysis for the proposed sub-advisory agreement (each factor with methodology pin and the supporting evidence; trustee questions and parent-adviser responses on the record).
  - Counsel memo on the conditions of the manager-of-managers exemptive order with the order citation, condition-by-condition analysis, and the determination that the conditions are satisfied.
  - Parent CCO's full reasonable-belief assessment of the proposed sub-adviser's compliance program (Rule 206(4)-7 program review; code of ethics under Rule 204A-1; SOC 2 Type II report dates; named-control testing plan; oversight cadence).
  - Full proposed sub-adviser due-diligence package (firm, personnel, philosophy, process, performance, regulatory, BCP, cyber, vendors, soft-dollar, MiFID II).
  - Proposed sub-advisory agreement and fee schedule cross-walked against the affected fund's existing aggregate advisory fee (no-increase confirmation).
  - Information statement to shareholders draft and prospectus supplement draft.
  - Source trace mapping every material claim to its source system, evidence reference, and confidence.
  - Reviewer questions for the secretariat to surface in the meeting.

The pack stops at draft. The fund CCO, the parent adviser CCO, and the board secretariat review before the meeting. The independent trustees and their counsel deliberate and record the determination.

#### Why this scenario matters

- A sub-adviser addition under manager-of-managers exemptive relief is a §15(c) determination on a new advisory contract, not a routine renewal. The factor analysis is forward-looking on a relationship that has not yet operated at the fund; the methodology pins and the evidence basis carry more weight, not less.
- The conditions of the exemptive order are not boilerplate. The independent-trustee composition condition, the aggregate-fee condition, the information-statement timeline, and the unaffiliated-sub-adviser scope condition each have to be confirmed on the record. A counsel memo is the standard evidence; the board's determination cites it.
- The Rule 38a-1(a)(2) program-adequacy assessment for a new sub-adviser is the parent CCO's reasonable-belief framing at the moment of approval. The §38a-1 expectation does not accept a sub-adviser CCO attestation alone; the parent CCO's evidence basis (Form ADV review, code of ethics review, SOC 2 Type II reports, named-control testing plan) supports the belief at intake and supports the standing oversight loop after approval.
- The cyber overlay carries the proposed sub-adviser's operational and cyber posture into the program-adequacy assessment. Reg S-P customer-information safeguarding under the May 2024 amendments is on the cycle for any new sub-adviser handling fund-shareholder customer information, even where the sub-adviser sits behind the parent adviser.
- The conduct overlay carries the §15(c) factor analysis as the fiduciary-bargain record; the §17(e) and Rule 17a-7 considerations sit at the standing quarterly cycle and not in this approval pack, but the proposed sub-adviser's affiliated-broker and soft-dollar posture are on the record now to set the baseline for those standing reviews.
- The aggregate-fee condition of the manager-of-managers order is not a pricing observation, it is a condition of the exemptive relief. Where the proposed sub-advisory fee plus other components would change the aggregate advisory fee at the fund level, the manager-of-managers route is unavailable and a shareholder vote is required. The counsel memo and the §15(c) pack confirm the no-increase posture.

#### Anchors

- ICA §15(a) — sub-advisory agreement requires shareholder approval absent exemptive relief.
- ICA §15(c) — Gartenberg / Jones v. Harris factor analysis for the board's approval of any advisory or sub-advisory agreement.
- Manager-of-managers exemptive order — SEC orders permitting the addition or material amendment of unaffiliated sub-advisory agreements without a shareholder vote, on stated conditions; the trust's specific order text and conditions cited in the counsel memo.
- ICA Rule 38a-1 — fund and service-provider compliance programs; CCO program-adequacy assessment for new service providers including sub-advisers.
- ICA Rule 204A-1 — adviser and sub-adviser code of ethics.
- Securities Exchange Act §28(e) — soft-dollar safe harbor; SEC Release No. 34-54165 (July 2006) interpretive guidance.
- SEC Reg S-P (May 2024 amendments) — customer-information safeguarding; sub-adviser posture relevant to the program-adequacy assessment.

See `references/source-anchors.md` for full citations and verification flags.

## troubleshooting

### Troubleshooting: fund-board-reporting

Recurring failure modes when a fund-board pack looks complete but is not. The reviewer pass should catch these; the builder pass should preempt them.

#### The Rule 38a-1 written report reads as a logbook

Symptom: long list of incidents during the period, no assessment of root cause, no recurrence-risk analysis, no CCO recommendation on adequacy.

Why it happens: builder treats §38a-1(a)(4)(iii) as a reporting requirement, not as a written assessment of the operation and adequacy of the compliance program.

Fix: the rule requires assessment, not enumeration. Each material compliance matter carries root cause, recurrence risk, and remediation status; the per-service-provider section carries the parent CCO's reasonable belief in the program's adequacy with the evidence basis; the report closes with the CCO's recommendation. The trustees consume the annual report as the fiduciary record of the §38a-1 oversight cycle.

#### Sub-adviser oversight resting on attestation alone

Symptom: each sub-adviser carries the sub-adviser CCO's attestation that the sub-adviser's compliance program is adequate. The parent CCO's oversight evidence is missing.

Why it happens: sub-adviser oversight is operationally distant; the sub-adviser CCO's signature feels sufficient.

Fix: Rule 38a-1 expects the parent CCO to reasonably believe the sub-adviser's program is adequate; the belief rests on evidence the parent CCO has reviewed. SOC 2 Type II reports for the sub-adviser's operational platform; independent assessment results; testing conducted by the parent CCO; any in-period exam findings affecting the sub-adviser; third-party reports. The pack documents the evidence basis, not just the attestation.

#### §15(c) profitability without methodology

Symptom: the §15(c) renewal pack carries a profitability number for the adviser's relationship with the fund. Methodology (direct expense allocation, indirect cost basis, capital usage) is not described.

Why it happens: the adviser provides the number; the pack carries it forward.

Fix: a bare profitability number is the §36(b) fee-litigation discovery finding pattern. The §15(c) pack describes how the adviser allocated direct expenses to the fund relationship; how the adviser computed the indirect cost basis (allocation key for shared infrastructure, executive time, technology); how the adviser treated capital usage and any opportunity-cost adjustments. Methodology pin is the substantive disclosure.

#### Recycled trustee questions

Symptom: the trustees' questions in the §15(c) materials are identical or near-identical to the prior year's. The adviser's responses are also recycled.

Why it happens: the deliberation is performative; the substantive challenge does not happen.

Fix: independent trustees' questions are the documented substantive challenge under the §15(c) deliberation. Period-specific updates demonstrate the deliberation; recycled questions are themselves a finding pattern in §36(b) discovery. The pack carries period-specific questions tied to the period's facts (AUM growth and economy-of-scale analysis; performance versus the stated benchmark; profitability movement; fall-out benefit changes; any new affiliated relationship; any change in the comparison peer set).

#### Liquidity classification static

Symptom: Rule 22e-4 classification distribution is reported as a quarterly snapshot. The classifications are months old by the time the board reads the pack.

Why it happens: the program administrator runs classifications on a quarterly cadence; the pack reports the most recent snapshot.

Fix: classifications must be reasonably current; a quarterly snapshot in a stressed market is stale. The pack notes classification timing, any market-change-trigger reclassification during the period (the rule requires reclassification when reasonably warranted), and any breach with restoration timeline. For periods of market stress, the pack addresses the timing gap explicitly and surfaces it as a sign-off question.

#### Rule 2a-5 prompt-notification log missing

Symptom: the valuation oversight section reports the quarterly written report from the valuation designee. The prompt-notification log for the period is absent.

Why it happens: the prompt-notification events are operationally distinct from the quarterly cycle; the builder consolidates everything into the quarterly summary.

Fix: Rule 2a-5 requires prompt board notification (no later than five business days after the designee becomes aware) of matters that materially affect the fair value of investments. A quarterly summary alone is insufficient if material events occurred mid-period. The pack carries the prompt-notification log as a separate item: each notification with the date the designee became aware, the materiality assessment, the action taken, and any remediation.

#### Limited-derivatives-user status assumed without monitoring

Symptom: Rule 18f-4 reporting asserts limited-derivatives-user status. The 10% notional threshold monitoring during the period is not shown.

Why it happens: the derivatives risk manager's monitoring lives in the operational layer; the pack reports the status without the monitoring evidence.

Fix: limited-derivatives-user status is fund-by-fund and can transition mid-period. The pack reflects either continuous compliance with the 10% threshold (with the monitoring evidence basis) or a documented transition to the full DRMP, including the timing, the program adoption, the derivatives risk manager designation, and the board approval.

#### Affiliated transactions reported as counts

Symptom: Rule 17e-1 affiliated brokerage shows aggregate commissions; Rule 17a-7 cross trades shows count and aggregate value. No procedure-adequacy detail; no pricing methodology evidence.

Why it happens: the upstream feed gives counts; the substantive content lives in the operational compliance file and never makes the pack.

Fix: each affiliated transaction type carries the conflict shape. Rule 17e-1 requires the board's quarterly procedure-adequacy determination; the pack reflects whether the determination was made and any procedure exception. Rule 17a-7 conditions the cross trade on a current-market-price determination and the four conditions; the pack carries the pricing methodology evidence and the §17a-7(e) annual board procedure review. §17(a) / Rule 17a-8 transactions carry the §17 analysis basis (no exemptive order without the order; reliance on Rule 17a-8 with the conditions analysis).

#### Soft-dollar disclosure as a generic statement

Symptom: §28(e) section reads "the adviser uses soft dollars in compliance with §28(e)". Commission allocation, eligibility analysis, CSA / CCA arrangements, and policy changes are absent.

Why it happens: soft-dollar disclosure is treated as a generic statement of policy, not as a substantive period disclosure.

Fix: the §28(e) section carries the period-specific disclosure: total commissions paid for research and brokerage; the allocation between research and execution; the adviser's eligibility analysis under the 2006 SEC interpretive release for the research and brokerage services received; CSA / CCA arrangements in use; MiFID II hard-dollar treatment for global advisers; any policy change in the period including any change in eligible-research categories.

#### Cyber events reported only at the fund's adviser

Symptom: cyber section covers events at the adviser. Events at the transfer agent, the custodian, the fund accountant, the distributor, sub-transfer agents, and pricing services are absent or under-reported.

Why it happens: the adviser's cyber posture is operationally familiar; the broader service-provider cyber surface is fragmented across third parties.

Fix: the §38a-1 service-provider compliance program loop reaches every service provider's cyber program. A cyber event at any service provider where fund-shareholder customer information was affected triggers the fund's Reg S-P notice obligation. The pack carries cyber events across the service-provider population, with the contractual notification posture, the fund's notice obligation analysis, and any remediation.

#### Public-parent SEC cyber disclosure decisions reported as if they bind the fund board

Symptom: cyber section asserts that the public-parent's 8-K Item 1.05 disclosure decision was made by the fund board, or that the fund board reviewed the public-parent's Item 106 disclosure for accuracy.

Why it happens: the lines between the fund's adviser and the adviser's public-company parent blur in operational discussion.

Fix: the public-parent disclosure committee or equivalent process owns the disclosure decision, not the fund board. The fund-board pack flags the event and the disclosure-process referral; the disclosure decision is reported separately and is not a fund-board determination.

#### §15(c) fall-out benefits catalogued generically

Symptom: fall-out benefits section reads "the adviser receives fall-out benefits including soft-dollar credits and affiliated-broker revenue".

Why it happens: the substantive catalogue is operationally distributed; the generic sentence is easier to write.

Fix: the catalogue is substantive: soft-dollar credits with the eligibility analysis; affiliated-broker revenue under Rule 17e-1 with the period total; 12b-1 distribution flows to the adviser's distributor affiliate with the fee total and the use of the fee; affiliated-bank deposit balances and cash-management revenue; sub-adviser-relationship economics where the sub-adviser is affiliated; revenue-sharing payments from the adviser to financial intermediaries. The Jones v. Harris substantive review tests this catalogue.

#### Pack stops too late

Symptom: the skill produces and "files" the pack with the secretariat, marks it as distributed, asserts CCO sign-off without evidence, certifies the §38a-1 written report under the CCO's name, signs the §15(c) renewal recommendation, or closes any issue.

Why it happens: builder over-runs the human-review gate.

Fix: the pack is a draft until the fund CCO and the board secretariat review. The skill stops at the draft and surfaces the reviewer questions for the secretariat to consider; it does not assert sign-off, certify the §38a-1 report, sign the §15(c) recommendation, or close any issue.

#### Pack reads as an adviser ERM committee pack

Symptom: the pack covers firm-wide investment risk, fiduciary risk at the firm level, vendor risk at the firm, BD net-capital content for dual-registrant firms. Fund-specific items (§15(c), §38a-1, §17, Rule 22e-4, Rule 2a-5, Rule 18f-4 by fund) are absent or thin.

Why it happens: the builder reaches for adviser-shaped templates and slots fund items into the absent adviser rows.

Fix: the audiences are different. The fund board oversees the funds; the adviser ERM committee oversees the adviser firm. The pack scope is per-fund (or per-trust). Adviser-firm content lives in `risk-committee-pack` with the capital-markets sector overlay; cross-link where an item is material to both, do not collapse.
