# Capital-markets sector overlay — rule-to-obligation-extraction

Load this overlay when the rule under extraction is issued by the SEC, CFTC, FINRA, NFA, MSRB, or a foreign capital-markets supervisor (FCA, ESMA), or when the rule applies to investment advisers, broker-dealers, registered investment companies, swap dealers, FCMs, or other capital-markets registrants. The overlay carries SEC adopting-release structure conventions, Investment Advisers Act and 1934 Act citation conventions, FINRA rulebook structure, and Form ADV instruction parsing.

## SEC adopting-release structure

A SEC final rule publishes in the Federal Register as an adopting release. The release contains:

- **Preamble** (typically Sections I-VIII): introduction; background; comments received; amendments adopted; economic analysis; paperwork-reduction analysis; regulatory-flexibility analysis; statutory authority and text of amendments. The preamble is interpretive; it explains what the rule does and why. Extraction does not pin obligations to preamble text.
- **Operative regulatory-text amendments** (typically the closing section). The amendments are listed by CFR section and are what codifies in 17 CFR. Pin obligations to the codified section (e.g., `17 CFR 275.206(4)-1(d)(1)`); cross-reference to the adopting release by FR cite for the interpretive context.
- **Effective date and compliance date statements**. The release names a single effective date (when the rule joins the CFR) and one or more compliance dates (when the regulated party must comply, often staged by registrant size).

Common pitfall: extracting an obligation from the preamble that does not appear in the codified section. The preamble may describe the agency's expectations in language not present in the operative text. The binding obligation is the operative text; preamble framing is captured in the source-pin's `preamble_context` field, not as a freestanding obligation.

## Investment Advisers Act and 1934 Act citation conventions

- **Investment Advisers Act of 1940**. Sections of the Act are cited as `Section X of the Advisers Act` (e.g., `Section 206 of the Advisers Act`). Rules promulgated under the Act are codified in 17 CFR Part 275 and cited as `Rule 206(4)-Y under the Advisers Act` or `17 CFR 275.206(4)-Y`. Common rules:
  - **Rule 206(4)-1** — investment-adviser marketing rule (advertising; solicitation).
  - **Rule 206(4)-2** — custody rule.
  - **Rule 206(4)-7** — compliance-program rule.
  - **Rule 204-2** — books-and-records rule.
  - **Rule 204A-1** — code-of-ethics rule.
- **Securities Exchange Act of 1934**. Sections cited as `Section X of the Exchange Act`. Rules in 17 CFR Part 240 (broker-dealer rules), 17 CFR Part 242 (Reg ATS, Reg SHO, Reg NMS), 17 CFR Part 248 (Reg S-P privacy).
- **Investment Company Act of 1940**. Sections cited as `Section X of the Investment Company Act`. Rules in 17 CFR Part 270.
- **Securities Act of 1933**. Sections cited as `Section X of the Securities Act`. Rules in 17 CFR Part 230. Form requirements in 17 CFR Part 239.

## SEC Cybersecurity Disclosure Rule — worked pattern

88 FR 51896 (July 26 2023), codified at 17 CFR 229.106 (Reg S-K Item 106), 17 CFR 232.405 (inline XBRL), 17 CFR 240.13a-11 and 17 CFR 240.15d-11 (Form 8-K coverage), 17 CFR 249.308 (Form 8-K Item 1.05). Compliance dates: incident-disclosure compliance December 18 2023 for non-smaller reporting companies, June 15 2024 for smaller reporting companies; risk-management-and-strategy compliance with annual reports for fiscal years ending on or after December 15 2023.

Extraction decomposes into atomic obligations:

- **Materiality determination obligation**. Trigger: a covered cybersecurity incident. Action: determine materiality. The rule does not name a specific timing for the determination, but Item 1.05 instructions require that the determination be made "without unreasonable delay following discovery." Pin to Form 8-K Item 1.05 instructions and the adopting-release preamble framing.
- **4-business-day disclosure timing obligation**. Trigger: materiality determination. Action: file Form 8-K disclosing the incident. Deadline: within 4 business days of the materiality determination. Exception: Attorney General national-security delay (limited circumstances; Item 1.05(c)).
- **Risk-management-process disclosure obligation (annual)**. Action: describe in annual report (Form 10-K Item 1C; Form 20-F coverage) the registrant's processes for assessing, identifying, and managing material risks from cybersecurity threats. Frequency: periodic (annual). Pin: 17 CFR 229.106(b).
- **Board-oversight disclosure obligation (annual)**. Action: describe the board's oversight of cybersecurity risks. Pin: 17 CFR 229.106(c)(1).
- **Management-role disclosure obligation (annual)**. Action: describe management's role in assessing and managing material risks. Pin: 17 CFR 229.106(c)(2).
- **Inline-XBRL tagging obligation**. Action: tag the disclosures in inline XBRL. Pin: 17 CFR 232.405. Effective dates lag by registrant size.

Each is a row. The defined terms section captures "cybersecurity incident" and "cybersecurity threat" with their Item 106(a) definitions. Cross-references link the materiality determination row to the 4-business-day disclosure row (relationship `produces_record_for`).

## SEC Investment Adviser Marketing Rule — worked pattern

Rule 206(4)-1, 17 CFR 275.206(4)-1, adopting release 86 FR 13024 (March 5 2021), compliance date November 4 2022. The rule consolidates the prior advertising rule and the cash-solicitation rule. Extraction decomposes into:

- §275.206(4)-1(a) — definitions: "advertisement" (with two prongs), "endorsement", "testimonial", "third-party rating".
- §275.206(4)-1(b) — general prohibitions on materially misleading content; principles-based (untrue statements; unsubstantiated claims; cherry-picking; etc.). Each prohibition is a row with action_type `prohibition`.
- §275.206(4)-1(c) — testimonials and endorsements: disclosure obligations (clear and prominent disclosure that the testimonial is given by a client and whether cash compensation was provided), oversight of promoters, written agreement when compensation exceeds de minimis, ineligibility for "bad actor" promoters.
- §275.206(4)-1(d) — third-party ratings: disclosure obligations on date, period, identity of the rater.
- §275.206(4)-1(e) — performance presentations: gross-and-net presentation; one-, five-, and ten-year periods for non-private-fund advertisements; related-performance and predecessor-performance conditions; hypothetical-performance disclosures.
- Books-and-records implications: Rule 204-2(a)(11) and (a)(15) record-retention obligations attached to advertisements; cross-reference rows.

## SEC Reg S-P amendments — worked pattern

89 FR 47688 (June 3 2024) [verify final FR cite], codified amendments to 17 CFR Part 248. Extraction decomposes into:

- Incident-response programme obligation. Pin: 17 CFR 248.30 [verify].
- Customer-notice obligation following an incident. Pin: 17 CFR 248.30 [verify].
- Service-provider-oversight obligation.
- Records and recordkeeping rows.
- Compliance-date staging by registrant size.

## FINRA rulebook structure

FINRA rules are organised into series (1000s through 9000s) plus the Conduct Rules and the IM (Interpretive Material) and the Notice-to-Members series. Pin to the rule number (e.g., `FINRA Rule 3110` supervision; `FINRA Rule 4511` books and records; `FINRA Rule 2210` communications with the public). FINRA rules are SRO rules; they are filed with the SEC under Section 19(b) of the Exchange Act and are binding on FINRA member firms once approved. Extraction from a FINRA rule pins to the rule number; from a Notice-to-Members or Regulatory Notice, pin to the notice number plus the section inside.

## Form ADV and Form CRS

Form ADV (and Form ADV Part 2A and Part 2B) and Form CRS are not rules themselves; they are forms whose instructions impose obligations on registrants. Pin to the form item number plus the instruction reference (e.g., `Form ADV Part 1A Item 1`; `Form CRS Item 5`). The underlying obligations to file and to deliver are in the rules: `Section 203 of the Advisers Act` and `17 CFR 275.204-1` (Form ADV); `17 CFR 275.204-5` (Form CRS delivery).

## CFTC and NFA citations

- **CFTC**. Sections of the Commodity Exchange Act cited as `Section X of the CEA` or `7 USC §X`. Rules in 17 CFR Parts 1 through 190.
- **NFA**. NFA rules are SRO rules; pin to NFA Compliance Rule number or Interpretive Notice number.

## When to escalate

The base SKILL.md is the right tool when the extraction feeds `obligation-mapping` for a capital-markets registrant. When the extraction supports an SEC adviser or BD examination readiness sprint, the downstream consumer is `adviser-exam-readiness`; the extraction feeds that readiness sprint.
