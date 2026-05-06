# Capital-markets sector overlay — vendor-diligence

When the engagement scope flags capital markets (advisers, broker-dealers, registered funds, asset managers), load this overlay alongside `references/source-anchors.md`. The bank-flavoured interagency-guidance frame is not the operative supervisory frame for non-bank registrants.

## Operative supervisory frame

There is no single interagency TPRM bulletin for SEC and FINRA registrants. Expectations come through:

- **Investment Advisers Act Rule 206(4)-7** — the compliance-program rule for advisers. The adviser must have written policies and procedures reasonably designed to prevent violations; oversight of service providers is part of that.
- **Investment Company Act Rule 38a-1(a)(4)** — the fund's compliance-program rule, including service-provider compliance-program-adequacy assessment for transfer agent, custodian, fund accountant, principal underwriter, valuation designee, pricing services. The fund CCO oversees.
- **FINRA Rule 3110 (supervision)** — for broker-dealers, supervisory obligations extend to outsourced functions.
- **SEC Division of Examinations Risk Alerts** on outsourced CCO arrangements (the SEC's 2022 Risk Alert is the most-cited; [verify exact title and date]).
- **Sub-adviser oversight**: where a sub-adviser is the vendor, oversight under the fund adviser's 38a-1 program and the contractual code-of-ethics reach are operative; soft-dollar and affiliated-broker conflicts are part of the diligence.

## Custody Rule

- **Investment Advisers Act Rule 206(4)-2** — where the vendor touches client assets, qualified custodian status, account-statement delivery, surprise audit, SLOA inventory all enter the diligence.

## Trade-execution venue diligence

- **Best execution** under Investment Advisers Act §206 fiduciary duty and FINRA Rule 5310 — broker selection and trade-execution venue diligence overlap with `best-execution-surveillance` (capital-markets sector skill). Where the diligence vendor is an execution venue, ATS, or broker-dealer counterparty, the best-execution diligence belongs alongside the third-party-risk diligence.

## Reg S-P (May 2024 amendments)

- **17 CFR Part 248 (Reg S-P) as amended May 2024** [verify exact compliance dates by entity type and size]: safeguarding and customer-notice obligations imposed on covered institutions; service-provider written-contract requirements; breach-notification timing. The diligence pack must surface Reg S-P contract elements and the vendor's breach-notification-clock posture.

## Form ADV currency

- **Form ADV Part 2A Item 10 and Item 14** disclosures of material relationships with related and unrelated third parties. Diligence outputs feed brochure currency. Where a new vendor relationship is material, the brochure-update path is part of the human-review chain.

## Outsourced CCO

- Where the vendor is an outsourced CCO or compliance-service provider, the SEC's 2022 Risk Alert sets the bar [verify exact title and date]. Diligence must address: independence, resourcing, expertise, access to information, and reporting-line clarity to the adviser's senior management or the fund board.

## AI vendor mode for advisers and BDs

When `ai_vendor=true`:

- **SEC focus on AI / predictive analytics in adviser practices** — risk-alert and rulemaking activity has been ongoing; pin the current state on the date of analysis [verify].
- **SEC proposed rule on conflicts of interest in the use of predictive data analytics** (proposed July 26, 2023) — track current state [verify whether final, withdrawn, repurposed].
- **Marketing Rule (Rule 206(4)-1)** — AI-generated marketing content (hypothetical performance, testimonials, endorsements, AI-personalised content) must comply. Diligence on a vendor providing marketing-AI must flag the Marketing Rule reach.
- **Reg BI care obligation** for broker-dealers — where AI surfaces a recommendation to a retail customer, the BD's documentation of the care analysis must reflect the AI's role.
- **Rule 204-2 books-and-records** — AI outputs that support an investment decision are likely required to be retained; the diligence must surface the vendor's retention and exportability posture.

Cross-link to `ai-governance-model-risk/llm-vendor-evidence-review` via `ai_specific_findings.eval_evidence_status = deferred-to-evidence-review`.

## Fund-board reach

- For registered funds, material vendor changes (especially custodian, transfer agent, fund accountant, sub-adviser, valuation designee) trigger fund-board notice or approval and may trigger Form N-CEN reporting on certain service-provider changes.
- ICA §15 considerations apply when the adviser or sub-adviser is being replaced — shareholder-vote thresholds and interim-contract authority are part of the planning lens.

## Cross-link inside the plugin

- **`exit-plan` capital-markets overlay** carries the transfer-agent migration, custodian transition, fund-accountant change, sub-adviser termination mechanics, including 38a-1 board-notification posture and Reg S-P record-return obligations.
- **`contract-gap-review` capital-markets overlay** carries the Reg S-P clause set, the Custody Rule SLOA terms, and the sub-adviser code-of-ethics clauses.

## Output-template additions for capital markets

- Registration-class scoping line: adviser, BD, registered fund, dual-registrant, state-registered IA.
- Service-provider category against Rule 38a-1(a)(4) when the firm is a fund adviser.
- Custody Rule applicability check.
- Reg S-P clause status as a named line.
- Marketing Rule applicability check when the vendor produces or distributes investment-related content.
- Form ADV Part 2A Item 10 / Item 14 brochure-update trigger as a named line.

## Common pitfalls in capital-markets vendor diligence

- Importing the bank interagency-guidance frame as if it were operative for an adviser or BD.
- Missing the fund-board notice/approval path for service-provider changes at a registered fund.
- Treating an outsourced-CCO arrangement as a routine vendor when it is a compliance-program-design relationship subject to its own SEC focus.
- Missing the Reg S-P May 2024 service-provider clause set when reusing a pre-2024 contract template.
- Skipping the Marketing Rule analysis on a marketing-content vendor.
