# Example: annual Rule 38a-1 written report at a multi-manager fund complex with a sub-adviser MCM

Public-source-derived. No named institution. The shape mirrors the standing annual cycle at a multi-manager fund complex with several sub-advisers, where one sub-adviser had a material compliance matter during the period and self-reported.

## Input

- Trust / fund complex: open-end mutual fund trust with eight series funds, four of which are multi-manager (parent adviser plus one to three sub-advisers each); two ETFs operating under Rule 6c-11; one money market fund under Rule 2a-7.
- Engagement scope supplied: primary regulators SEC (Investment Management) and the relevant state securities regulators for state-registered intermediaries; persona = fund CCO, with the trust's board secretariat as drafter; sector overlay = capital-markets (loaded for every invocation of this skill); cross-cutting overlays = cyber (loaded because of two service-provider Reg S-P customer-information events in the period and because the parent adviser is a subsidiary of a public-company asset-management group) and conduct (loaded because the §15(c) renewal pack is in scope this cycle for one of the eight funds and because of the sub-adviser MCM); climate not loaded (the trust does not operate ESG-labeled funds and Rule 35d-1 ESG-name considerations are not in scope this period); source posture = public-plus-firm-policy-plus-system-of-record-evidence.
- Period: full year ending [fiscal year end]; annual standing meeting of the Board of Trustees.
- Report type: annual Rule 38a-1 written report; one §15(c) advisory contract renewal pack for the in-renewal fund; standing quarterly compliance section; standing affiliated-transactions and soft-dollar disclosure.
- Upstream artifacts on file: the parent adviser's Rule 206(4)-7 annual review summary; each sub-adviser's CCO attestation supplemented by parent-CCO testing notes and the most recent SOC 2 Type II reports for the major operational platforms; the transfer agent's annual program summary and the transfer agent's most recent SOC 2 Type II; the custodian's annual program summary; the fund accountant's annual program summary; the distributor's quarterly Rule 12b-1 reports and annual continuance materials; the valuation designee's quarterly written reports for the period and the prompt-notification log (three notifications in the period); the derivatives risk manager's annual report for the two funds in full DRMP and the limited-derivatives-user monitoring evidence for the six funds in limited status; the liquidity program administrator's annual report and the quarterly classification snapshots; the affiliated-transactions log (Rule 17a-7 cross trades count: 12 in the period; Rule 17e-1 affiliated brokerage aggregate: low); the soft-dollar / §28(e) report from the parent adviser; one self-reported sub-adviser MCM (personal-trading violation under Rule 204A-1).

## Output sketch

### Deck (PowerPoint)

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

### Word annex

- All sections of the deck developed at length, plus:
  - Full per-service-provider compliance program assessment (parent CCO's reasonable belief with the evidence basis for each provider; SOC 2 Type II report dates; testing summaries; in-period exam findings affecting any provider).
  - Full §15(c) factor analysis for the in-renewal fund (profitability with methodology pin: direct expense allocation, indirect cost basis, capital usage; fall-out benefits substantively catalogued; comparative fees with peer-group methodology pin; trustee questions and adviser responses on the record).
  - Full sub-adviser MCM write-up (personal-trading violation under Rule 204A-1; self-reported; root cause = pre-clearance system gap that was remediated; recurrence-risk analysis; sub-adviser CCO attestation supplemented by parent-CCO testing of the remediated control).
  - Reg S-P customer-information event analyses for the two service-provider events (event detail; affected information types; customer count affected; notice posture and timing; service-provider remediation status; contractual notification adequacy review).
  - Rule 17a-7 pricing methodology evidence for the 12 cross trades against the four §17a-7 conditions.
  - Source trace mapping every material claim to its source system, evidence reference, and confidence.
  - Reviewer questions for the secretariat to surface in the meeting.

The pack stops at draft. The fund CCO and the board secretariat review before the meeting.

## Why this scenario matters

- The Rule 38a-1 written report is the substantive annual artifact, not a logbook of incidents. The sub-adviser MCM is assessed (root cause, recurrence risk, remediation status), not merely listed.
- Sub-adviser oversight rests on the parent CCO's reasonable belief in the sub-adviser's compliance program. The sub-adviser CCO's attestation is supplemented by the parent CCO's testing of the remediated control; the §38a-1 expectation is satisfied.
- The §15(c) renewal pack carries methodology pins for profitability and peer-group selection. Trustee questions are substantive and period-specific (AUM growth and economy-of-scale analysis; performance versus benchmark for the period; profitability movement; fall-out benefit changes); recycled prior-year questions are absent.
- The cyber overlay drives the Reg S-P customer-notice analysis for the two service-provider events. The fund retains the customer-notice obligation when fund-shareholder customer information was affected; the pack documents the obligation analysis.
- The conduct overlay drives the §17(e) / Rule 17e-1 procedure-adequacy treatment, the Rule 17a-7 pricing methodology evidence, and the soft-dollar disclosure. Counts without context are insufficient; the pack carries the conflict shape and the procedure adequacy.
- Climate is not in scope this period (no ESG-labeled funds; Rule 35d-1 ESG-name considerations not relevant). The cross-cutting overlay loader respects the engagement scope; the pack does not invent a climate section.

## Anchors

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
