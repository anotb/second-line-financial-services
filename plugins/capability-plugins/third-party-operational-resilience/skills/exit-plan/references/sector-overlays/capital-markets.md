# Capital-markets sector overlay — exit-plan

When the scope flags capital markets (advisers, broker-dealers, registered funds, asset managers), load this overlay alongside `references/source-anchors.md`. The bank-flavoured interagency-guidance termination frame is not the operative supervisory frame for SEC and FINRA registrants. Capital-markets exit plans for fund service-provider transitions are the most substantive sub-domain in this overlay.

## Operative supervisory frame

- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule. Service-provider transitions must be reflected in the adviser's policies and procedures and in CCO oversight.
- **Investment Company Act Rule 38a-1(a)(4)** — fund compliance-program rule, including service-provider compliance-program-adequacy assessment for transfer agent, custodian, fund accountant, principal underwriter, valuation designee, pricing services. The fund CCO oversees; the fund board approves transitions of these critical service providers.
- **Investment Company Act §15** — investment advisory contracts; shareholder-vote thresholds and interim-contract authority on adviser or sub-adviser changes. **Rule 15a-4 interim contracts** carries the interim-period authority. Where the exit plan transitions an adviser or sub-adviser arrangement, ICA §15 and Rule 15a-4 are the operative spine.
- **Form N-CEN** — annual census report; service-provider-change disclosure for registered funds [verify the exact items that pick up service-provider changes].
- **FINRA Rule 3110 (supervision)** — for broker-dealers, supervisory continuity through vendor transitions.
- **Reg SCI — 17 CFR §242.1000 et seq.** — substitutability and BCDR posture for SCI entities; exit plans for SCI-system vendors must address Reg SCI substitutability expectations [verify subsection].

## Books-and-records continuity

- **Investment Advisers Act Rule 204-2** — adviser books-and-records preservation continues through and after transition. Record formats, retention periods, and reproducibility-on-demand must survive cutover.
- **17 CFR §240.17a-4** — broker-dealer books-and-records preservation continues. The vendor's records that fall in the firm's 17a-4 scope must be returned in a format meeting the rule, including the preservation-medium requirements.
- **Rule 31a (under the Investment Company Act)** — fund records continuity.
- **Reg S-P (May 2024 amendments)** [verify exact compliance dates] — customer-information treatment on termination of a service-provider arrangement; service-provider written-contract elements including breach-notification carry through.

## Fund service-provider transitions

This is the sub-domain where capital-markets exit planning carries the most weight. The named service providers under Rule 38a-1(a)(4) and the operative transition mechanics:

- **Transfer agent transition** — shareholder-record continuity; SAR position reconciliation; tax-cost-basis and 1099 reporting continuity across the cutover; advance-notice to record holders; coordination with NSCC for fund-supermarket distribution; Form N-CEN update.
- **Custodian transition** — qualified-custodian status continuity under Rule 206(4)-2; surprise-audit posture across the cutover; account-statement delivery continuity; SLOA inventory reconciliation; sub-custody arrangements; fund-board notice and approval.
- **Fund accountant transition** — NAV calculation continuity and dual-running across the cutover; pricing-source continuity; tax-lot accounting; fund expense accruals; 1099 reporting; fund-board notice and approval.
- **Pricing-services transition** — methodology continuity; fair-valuation governance under **Rule 2a-5**; pricing-vendor diligence under Rule 38a-1(a)(4) for the substitute.
- **Sub-adviser transition** — ICA §15 shareholder-vote threshold; Rule 15a-4 interim-contract authority; portfolio-handover mechanics including in-flight trade settlement; soft-dollar and affiliated-broker conflict carry-over; Form ADV Part 2A Item 10 and Item 14 updates; fund-board approval.
- **Adviser transition** — full ICA §15 process; Rule 15a-4 interim contract; Form ADV-W on termination of the outgoing adviser if applicable; fund-board approval; shareholder vote.
- **Principal-underwriter transition** — selling-agreement re-papering; sales-load and 12b-1 fee continuity.
- **Valuation-designee transition** under Rule 2a-5 — fund-board oversight and approval.

## Outsourced CCO transition

- Where the vendor is an outsourced CCO or compliance-service provider, the SEC's 2022 Risk Alert sets the bar [verify exact title and date]. Transition mechanics:
  - CCO-of-record handover with the seam dated.
  - Independence, resourcing, expertise, and access-to-information all re-evidenced on the substitute.
  - Reporting-line clarity to the adviser's senior management or the fund board re-established before the transition is effective.

## Form ADV currency on transition

- **Form ADV Part 2A Item 10 and Item 14** — material-relationship disclosures must be updated on substantive vendor changes. Brochure amendment cycle is part of the customer-notice posture for advisers.

## AI vendor mode for advisers and BDs

When `ai_vendor=true`:

- **SEC focus on AI / predictive analytics in adviser practices** — risk-alert and rulemaking activity has been ongoing; pin the current state on the date of analysis [verify].
- **Marketing Rule (Rule 206(4)-1)** — AI-generated marketing-content vendor transition must address content-retention and recordkeeping posture including the substitute model's marketing-content production.
- **Reg BI care obligation** for broker-dealers — AI-driven recommendation transitions must keep the BD's documentation of the care analysis intact.
- **Rule 204-2 books-and-records** — AI outputs supporting investment decisions must remain retrievable post-transition.
- Cross-link to `ai-governance-model-risk/llm-vendor-evidence-review` for the substitute model's evidence-pack review.

## Fund-board reach

- **Rule 38a-1(a)(4)** — fund-board notice or approval for material service-provider changes (custodian, transfer agent, fund accountant, sub-adviser, valuation designee, principal underwriter, pricing services).
- **ICA §15** — shareholder-vote thresholds for adviser and sub-adviser changes; Rule 15a-4 interim contracts carry the interim authority.
- The fund board's review of the substitute service-provider's compliance program is part of the transition; the exit plan carries the timing of board materials and the package contents.

## Cross-link inside the plugin

- **`vendor-diligence` capital-markets overlay** carries the diligence depth the exit plan consumes; the substitute service-provider's diligence pack is a precondition to transition.
- **`contract-gap-review` capital-markets overlay** carries the Reg S-P clause set, the Custody Rule SLOA terms, the sub-adviser code-of-ethics clauses, and the Reg SCI terms; clause gaps surfaced here flag the exit-readiness gap.
- **`concentration-risk-review`** flags fund-administrator, custodian, and sub-adviser concentration that drives substitute-service-provider viability.

## Output-template additions for capital markets

- Registration-class scoping line: adviser, BD, registered fund, dual-registrant, state-registered IA.
- Service-provider category against Rule 38a-1(a)(4) when the firm is a fund adviser or trustee.
- Custody Rule applicability check.
- Reg S-P treatment-of-customer-information posture as a named line.
- ICA §15 / Rule 15a-4 path as a named line for adviser or sub-adviser transitions.
- Form N-CEN update trigger as a named line.
- Form ADV Part 2A Item 10 / Item 14 amendment trigger as a named line.
- Fund-board notice and approval timing as a named line for fund service-provider transitions.

## Common pitfalls in capital-markets exit planning

- Importing the bank-flavoured interagency-guidance frame as if it were operative for an adviser or BD. The capital-markets supervisory frame runs through Rule 206(4)-7, Rule 38a-1, ICA §15, FINRA Rule 3110, and Reg S-P, not through the June 2023 interagency guidance.
- Missing the fund-board notice / approval path for service-provider changes at a registered fund.
- Treating an outsourced-CCO transition as a routine vendor change. CCO-of-record handover is a compliance-program-design transition.
- Missing the Reg S-P (May 2024) treatment-of-customer-information clauses on a transition that pre-dates the amendments.
- Treating Rule 204-2, Rule 17a-4, and Rule 31a books-and-records continuity as a vendor problem. The firm remains responsible regardless of vendor transition.
- Skipping ICA §15 and Rule 15a-4 sequencing on adviser or sub-adviser transitions.
- Missing Reg SCI substitutability expectations on SCI-system vendor transitions.
- Missing fair-valuation-governance considerations under Rule 2a-5 on a pricing-vendor transition.
