# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — rule-to-obligation-extraction

Load this overlay when the rule under extraction is issued by OCC, FRB, FDIC, NCUA, or by the federal banking agencies jointly (FFIEC inter-agency statements). The overlay carries banking-rule citation conventions and recurrent extraction patterns for OCC bulletins, FRB SR letters, FDIC FILs, NCUA letters to credit unions, and FFIEC inter-agency statements. The base SKILL.md row spine does not change; this overlay tells the practitioner which sources are permitted citations and which extraction patterns recur for banking rules.

#### Banking-rule citation conventions

- **12 CFR** is split across the three federal banking agencies. OCC rules generally land in Parts 1 to 199 (OCC under Title 12 Chapter I); FRB rules in Parts 200 to 299 (FRB under Title 12 Chapter II); FDIC rules in Parts 300 to 399 (FDIC under Title 12 Chapter III). NCUA rules land in Parts 700 to 799 (NCUA under Title 12 Chapter VII). CFPB rules transfer-of-authority rules land in 12 CFR Chapter X (Parts 1001 onward).
- The 36-hour bank notification rule was adopted in parallel by all three agencies: 12 CFR Part 53 (OCC); 12 CFR Part 225 Subpart N (FRB Regulation Y); 12 CFR Part 304 Subpart C (FDIC). When extracting from the parallel rule, the obligation rows are agency-specific by codified Part; the substantive obligation is the same shape across the three agencies.
- OCC Bulletins, FRB SR letters, FDIC FILs, and NCUA Letters to Credit Unions are interpretive supervisory instruments rather than rules in the CFR sense. The pin is the section inside the instrument (e.g., `OCC Bulletin 2013-29 §III.A`; `SR 11-7 §IV.A`). Operative-text-vs-preamble distinction does not apply the same way as it does for Federal Register rules; the entire bulletin text is interpretive, and the section structure inside the bulletin is the spine for extraction.

#### Recurrent extraction patterns — federal banking supervisory letters

The supervisory-letter genre carries recurrent obligation patterns that the extraction should expect:

- **Program-and-process pattern**. The letter identifies a programme (third-party-risk management; model risk management; operational resilience; cybersecurity; BSA/AML; capital planning) and decomposes into governance (board oversight; senior management oversight; written programme approval; periodic review), risk-assessment, life-cycle controls (onboarding/development; ongoing monitoring; offboarding/decommissioning), independent testing or validation, and reporting to the board or board committee. Each named life-cycle stage is a row.
- **Tier-by-tier scope pattern**. The letter scales expectations by institution size, complexity, or risk. The obligation is the same shape across tiers but the implementation depth differs. Capture each tier as its own scope-trigger row when the letter is explicit; capture the tier-language verbatim where it is not.
- **Examples-as-expectation pattern**. Bulletins and SR letters frequently embed examples as `For example, the institution should consider ...`. The example is interpretive, not binding; the binding obligation sits in the surrounding text. Resist extracting examples as obligations.

#### OCC Bulletin 2013-29 (rescinded) and the June 2023 Interagency Guidance — worked pattern

OCC Bulletin 2013-29 was the OCC's third-party-risk-management guidance from October 2013 to June 2023. It was rescinded on issuance of the **Interagency Guidance on Third-Party Relationships: Risk Management** (88 FR 37920, June 9 2023), issued jointly by FRB, FDIC, and OCC. The interagency guidance is the operative supervisory expectation for third-party-risk obligations across federally regulated banking organizations.

The interagency guidance decomposes into the third-party-risk life-cycle (planning; due diligence and third-party selection; contract negotiation; ongoing monitoring; termination) plus governance and oversight. Each life-cycle stage carries discrete obligations on the banking organisation: documentation expectations (risk assessment of the third-party relationship; due-diligence record), contract-clause expectations (right-to-audit, subcontracting controls, business-continuity, incident-notification, termination triggers), monitoring expectations (performance-monitoring, control-testing, financial-condition tracking), and termination expectations (data-return-or-destruction, exit transition). Each is a row in the extraction.

#### Joint Interagency Revised Guidance on Model Risk Management — worked pattern

OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026 (April 17, 2026) is one document issued through three agency channels with the same date, text, and signatories; it is the operative supervisory expectation for model risk management and supersedes SR 11-7 / OCC Bulletin 2011-12 (April 4, 2011) and SR 21-8 (Interagency Statement on Model Risk Management for BSA/AML Compliance, April 9, 2021). Extraction decomposes the guidance into definitions and scope (Section II — including the threshold relevance for banking organizations over $30 billion in total assets), model identification and inventory, validation, ongoing monitoring, and governance. Each section carries discrete supervisory expectations.

Caveats the extraction carries on every row drawn from this bulletin: the joint guidance is non-binding (does not set forth enforceable standards or prescriptive requirements; non-compliance does not result in supervisory criticism per Section I, footnote 1) and is "expected to be most relevant to banking organizations with over $30 billion in total assets" — the row's `requirement statement` and `confidence` carry that posture. Generative AI and agentic AI models are explicitly out of scope (footnote 3 of the joint guidance text); the principles cover only traditional statistical / quantitative models and non-generative, non-agentic AI models. Where a rule under extraction touches GenAI or agentic AI, the obligation is anchored to NIST AI RMF, NIST AI 600-1, ISO/IEC 42001, or the EU AI Act rather than to this bulletin. The bulletin contains zero references to NIST AI RMF or NIST AI 600-1; do not assert it incorporates them.

Where the extraction is reading a pre-April-17-2026 firm policy, validation report, or examination evidence that cites SR 11-7 or SR 21-8 by name, retain the legacy pin alongside the operative one (the legacy citation becomes a defined-terms entry pointing at the superseded source).

#### The 36-hour bank notification rule — worked pattern

12 CFR Part 53 (OCC); 12 CFR Part 225 Subpart N (FRB); 12 CFR Part 304 Subpart C (FDIC), 86 FR 66424 (November 23 2021), compliance date May 1 2022. Extraction pattern:

- **Defined terms** (each captured in the defined-terms section, with the rule's text of definition and the section pin): "computer-security incident"; "notification incident"; "banking organisation"; "bank service provider".
- **Trigger** (condition_or_trigger column): the banking organisation's determination that a notification incident has occurred.
- **Deadline** (deadline column): "as soon as possible and no later than 36 hours after the banking organisation determines that a notification incident has occurred."
- **Action** (action_type: notice_or_disclosure): notification to the primary federal regulator.
- **Evidence shape** (evidence_expected): incident-determination record; notification log; regulator-acknowledgement record.
- **Bank-service-provider obligation**: separate row. The bank service provider must notify each affected banking-organisation customer "as soon as possible" when the BSP determines a covered incident has occurred or is reasonably likely to occur. This is a third-party-side obligation that flows into the bank's third-party-risk register downstream.

#### BSA/AML rule structure

BSA/AML rules sit in 31 CFR Chapter X (Parts 1010 to 1029, FinCEN regulations) and in the relevant agency's BSA/AML rule (12 CFR 21 OCC; 12 CFR 208 and 12 CFR 211 FRB; 12 CFR 326 FDIC; 12 CFR 748 NCUA). The FFIEC BSA/AML Examination Manual is interpretive and is the inter-agency framework for examiner expectations; pin to the manual chapter when extracting from the manual, and to the underlying 31 CFR or 12 CFR section when extracting from the rule itself.

The Anti-Money Laundering Act of 2020 amendments to the BSA introduced: beneficial-ownership reporting under 31 CFR 1010.380 (FinCEN BOI rule); national priorities for AML/CFT under 31 USC 5318(h)(4)(A); modernisation of SAR/CTR processes. Each amendment carries its own implementation-rule schedule; capture extraction-time effective dates as the rule provides them.

#### When to escalate to a sector-skill chain

The base SKILL.md is the right tool when the extraction is from a banking rule and the next step is `obligation-mapping`. When the extraction is the upstream artifact for a full-scope OCC, FRB, or FDIC examination readiness sprint at a bank carrying the Heightened Standards (12 CFR Part 30 Appendix D), the downstream sector-readiness skill is `banking-supervision-readiness`; the extraction register feeds that readiness sprint. The base skill does not produce the readiness pack; it produces the obligation list the readiness pack reads.

## capital-markets

### Capital-markets sector overlay — rule-to-obligation-extraction

Load this overlay when the rule under extraction is issued by the SEC, CFTC, FINRA, NFA, MSRB, or a foreign capital-markets supervisor (FCA, ESMA), or when the rule applies to investment advisers, broker-dealers, registered investment companies, swap dealers, FCMs, or other capital-markets registrants. The overlay carries SEC adopting-release structure conventions, Investment Advisers Act and 1934 Act citation conventions, FINRA rulebook structure, and Form ADV instruction parsing.

#### SEC adopting-release structure

A SEC final rule publishes in the Federal Register as an adopting release. The release contains:

- **Preamble** (typically Sections I-VIII): introduction; background; comments received; amendments adopted; economic analysis; paperwork-reduction analysis; regulatory-flexibility analysis; statutory authority and text of amendments. The preamble is interpretive; it explains what the rule does and why. Extraction does not pin obligations to preamble text.
- **Operative regulatory-text amendments** (typically the closing section). The amendments are listed by CFR section and are what codifies in 17 CFR. Pin obligations to the codified section (e.g., `17 CFR 275.206(4)-1(d)(1)`); cross-reference to the adopting release by FR cite for the interpretive context.
- **Effective date and compliance date statements**. The release names a single effective date (when the rule joins the CFR) and one or more compliance dates (when the regulated party must comply, often staged by registrant size).

Common pitfall: extracting an obligation from the preamble that does not appear in the codified section. The preamble may describe the agency's expectations in language not present in the operative text. The binding obligation is the operative text; preamble framing is captured in the source-pin's `preamble_context` field, not as a freestanding obligation.

#### Investment Advisers Act and 1934 Act citation conventions

- **Investment Advisers Act of 1940**. Sections of the Act are cited as `Section X of the Advisers Act` (e.g., `Section 206 of the Advisers Act`). Rules promulgated under the Act are codified in 17 CFR Part 275 and cited as `Rule 206(4)-Y under the Advisers Act` or `17 CFR 275.206(4)-Y`. Common rules:
  - **Rule 206(4)-1** — investment-adviser marketing rule (advertising; solicitation).
  - **Rule 206(4)-2** — custody rule.
  - **Rule 206(4)-7** — compliance-program rule.
  - **Rule 204-2** — books-and-records rule.
  - **Rule 204A-1** — code-of-ethics rule.
- **Securities Exchange Act of 1934**. Sections cited as `Section X of the Exchange Act`. Rules in 17 CFR Part 240 (broker-dealer rules), 17 CFR Part 242 (Reg ATS, Reg SHO, Reg NMS), 17 CFR Part 248 (Reg S-P privacy).
- **Investment Company Act of 1940**. Sections cited as `Section X of the Investment Company Act`. Rules in 17 CFR Part 270.
- **Securities Act of 1933**. Sections cited as `Section X of the Securities Act`. Rules in 17 CFR Part 230. Form requirements in 17 CFR Part 239.

#### SEC Cybersecurity Disclosure Rule — worked pattern

88 FR 51896 (July 26 2023), codified at 17 CFR 229.106 (Reg S-K Item 106), 17 CFR 232.405 (inline XBRL), 17 CFR 240.13a-11 and 17 CFR 240.15d-11 (Form 8-K coverage), 17 CFR 249.308 (Form 8-K Item 1.05). Compliance dates: incident-disclosure compliance December 18 2023 for non-smaller reporting companies, June 15 2024 for smaller reporting companies; risk-management-and-strategy compliance with annual reports for fiscal years ending on or after December 15 2023.

Extraction decomposes into atomic obligations:

- **Materiality determination obligation**. Trigger: a covered cybersecurity incident. Action: determine materiality. The rule does not name a specific timing for the determination, but Item 1.05 instructions require that the determination be made "without unreasonable delay following discovery." Pin to Form 8-K Item 1.05 instructions and the adopting-release preamble framing.
- **4-business-day disclosure timing obligation**. Trigger: materiality determination. Action: file Form 8-K disclosing the incident. Deadline: within 4 business days of the materiality determination. Exception: Attorney General national-security delay (limited circumstances; Item 1.05(c)).
- **Risk-management-process disclosure obligation (annual)**. Action: describe in annual report (Form 10-K Item 1C; Form 20-F coverage) the registrant's processes for assessing, identifying, and managing material risks from cybersecurity threats. Frequency: periodic (annual). Pin: 17 CFR 229.106(b).
- **Board-oversight disclosure obligation (annual)**. Action: describe the board's oversight of cybersecurity risks. Pin: 17 CFR 229.106(c)(1).
- **Management-role disclosure obligation (annual)**. Action: describe management's role in assessing and managing material risks. Pin: 17 CFR 229.106(c)(2).
- **Inline-XBRL tagging obligation**. Action: tag the disclosures in inline XBRL. Pin: 17 CFR 232.405. Effective dates lag by registrant size.

Each is a row. The defined terms section captures "cybersecurity incident" and "cybersecurity threat" with their Item 106(a) definitions. Cross-references link the materiality determination row to the 4-business-day disclosure row (relationship `produces_record_for`).

#### SEC Investment Adviser Marketing Rule — worked pattern

Rule 206(4)-1, 17 CFR 275.206(4)-1, adopting release 86 FR 13024 (March 5 2021), compliance date November 4 2022. The rule consolidates the prior advertising rule and the cash-solicitation rule. Extraction decomposes into:

- §275.206(4)-1(a) — definitions: "advertisement" (with two prongs), "endorsement", "testimonial", "third-party rating".
- §275.206(4)-1(b) — general prohibitions on materially misleading content; principles-based (untrue statements; unsubstantiated claims; cherry-picking; etc.). Each prohibition is a row with action_type `prohibition`.
- §275.206(4)-1(c) — testimonials and endorsements: disclosure obligations (clear and prominent disclosure that the testimonial is given by a client and whether cash compensation was provided), oversight of promoters, written agreement when compensation exceeds de minimis, ineligibility for "bad actor" promoters.
- §275.206(4)-1(d) — third-party ratings: disclosure obligations on date, period, identity of the rater.
- §275.206(4)-1(e) — performance presentations: gross-and-net presentation; one-, five-, and ten-year periods for non-private-fund advertisements; related-performance and predecessor-performance conditions; hypothetical-performance disclosures.
- Books-and-records implications: Rule 204-2(a)(11) and (a)(15) record-retention obligations attached to advertisements; cross-reference rows.

#### SEC Reg S-P amendments — worked pattern

89 FR 47688 (June 3 2024) [verify final FR cite], codified amendments to 17 CFR Part 248. Extraction decomposes into:

- Incident-response programme obligation. Pin: 17 CFR 248.30 [verify].
- Customer-notice obligation following an incident. Pin: 17 CFR 248.30 [verify].
- Service-provider-oversight obligation.
- Records and recordkeeping rows.
- Compliance-date staging by registrant size.

#### FINRA rulebook structure

FINRA rules are organised into series (1000s through 9000s) plus the Conduct Rules and the IM (Interpretive Material) and the Notice-to-Members series. Pin to the rule number (e.g., `FINRA Rule 3110` supervision; `FINRA Rule 4511` books and records; `FINRA Rule 2210` communications with the public). FINRA rules are SRO rules; they are filed with the SEC under Section 19(b) of the Exchange Act and are binding on FINRA member firms once approved. Extraction from a FINRA rule pins to the rule number; from a Notice-to-Members or Regulatory Notice, pin to the notice number plus the section inside.

#### Form ADV and Form CRS

Form ADV (and Form ADV Part 2A and Part 2B) and Form CRS are not rules themselves; they are forms whose instructions impose obligations on registrants. Pin to the form item number plus the instruction reference (e.g., `Form ADV Part 1A Item 1`; `Form CRS Item 5`). The underlying obligations to file and to deliver are in the rules: `Section 203 of the Advisers Act` and `17 CFR 275.204-1` (Form ADV); `17 CFR 275.204-5` (Form CRS delivery).

#### CFTC and NFA citations

- **CFTC**. Sections of the Commodity Exchange Act cited as `Section X of the CEA` or `7 USC §X`. Rules in 17 CFR Parts 1 through 190.
- **NFA**. NFA rules are SRO rules; pin to NFA Compliance Rule number or Interpretive Notice number.

#### When to escalate

The base SKILL.md is the right tool when the extraction feeds `obligation-mapping` for a capital-markets registrant. When the extraction supports an SEC adviser or BD examination readiness sprint, the downstream consumer is `adviser-exam-readiness`; the extraction feeds that readiness sprint.

## insurance

### Insurance sector overlay — rule-to-obligation-extraction

Load this overlay when the rule under extraction is a NAIC model law or model regulation, a state insurance code section, a state DOI bulletin or industry circular, or a market-conduct examination standard. State insurance regulation is state-by-state; the NAIC model is a starting reference, not binding text. The overlay carries the model-versus-state-adopted distinction and recurring extraction patterns for insurance rules.

#### NAIC model-law versus state-adopted version

A NAIC model law is the model text the National Association of Insurance Commissioners adopts and circulates for state consideration. The model is not law in any state until the state adopts it through its legislative or regulatory process. State adoption is frequently with amendments. Extraction must distinguish:

- **Model-as-source**. When the rule under extraction is the NAIC model itself (e.g., reading the Model Law as a source for a national obligation inventory), pin to the model-section number with the model number (`Model 668 §4 Information Security Program`). Note that the model is not binding until adopted.
- **State-adopted version-as-source**. When the rule under extraction is a state-adopted version, pin to the state code section (e.g., `New York Insurance Law §305 Cybersecurity Requirements [verify]`; `Ohio Revised Code §3965.02`). State amendments at adoption are common; the extraction should capture material differences from the model in the open-extraction-questions section, with state-specific tags.
- **State-adoption status**. The NAIC tracks state-by-state adoption status. The extraction's source-trace should record adoption status as of the extraction date for the states in scope.

#### Recurrent insurance-rule extraction patterns

- **Programme-and-officer pattern**. State insurance codes typically require licensees to maintain a written programme (cybersecurity programme, anti-fraud plan, complaint-handling plan, MLR-rebate procedures, ORSA process) and to designate an officer (Chief Information Security Officer; Anti-Fraud Officer; Compliance Officer; Chief Risk Officer). The programme decomposes into risk-assessment, life-cycle controls, third-party oversight, periodic review, board-or-board-committee reporting, and incident-response. Each is a row.
- **Notification-and-reporting pattern**. State insurance codes attach notification obligations to specific events (cybersecurity event; data breach; MLR-rebate underpayment; market-conduct examination finding). Extraction captures the trigger, the deadline (often 72 hours for cybersecurity events; state-specific for other triggers), the recipient (Commissioner; Attorney General; affected consumers), and the form of notice.
- **Filing-and-attestation pattern**. State insurance codes require periodic filings (Annual Statement; ORSA Summary Report; corporate governance annual disclosure; MLR rebate filings). Each filing is a row, with frequency `periodic`, action_type `reporting`, and the filing form named (e.g., NAIC Annual Statement; ORSA Summary Report).

#### NAIC Insurance Data Security Model Law (Model 668) — worked pattern

Model 668 was adopted by the NAIC in 2017 and has been adopted by the majority of states (state-by-state status tracked at the NAIC). Extraction from the model decomposes into:

- §3 Definitions — the defined-terms section captures: "Cybersecurity Event"; "Information System"; "Licensee"; "Multi-Factor Authentication"; "Nonpublic Information"; "Risk Assessment"; "Third-Party Service Provider".
- §4 Information Security Program — programme, risk-assessment, designated officer, board-oversight rows.
- §5 Investigation of a Cybersecurity Event — incident-response, scope-of-investigation, retention rows.
- §6 Notification of a Cybersecurity Event — Commissioner-notification (within 72 hours of determination); affected-consumer-notification; reinsurer-notification rows.
- §7 Powers of the Commissioner — investigative-power, examination-power rows on the regulator-side; not obligation rows for the licensee.
- §9 Exceptions — exceptions row tied to small-licensee exemption (fewer than 10 employees per the model; state-amended thresholds common).

When extracting a state-adopted version of Model 668, capture the model section number alongside the state code section and flag material amendments (e.g., New York's NYDFS Part 500 was issued before Model 668 and has different definitions and timing; New York is sometimes counted as Model 668-equivalent and sometimes not, depending on the framing; the extraction should pin to the actual state instrument, not to the model when the state operates under its own rule).

#### NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model 505) — worked pattern

Model 505 (adopted 2012, amended periodically) requires insurers above a premium-volume threshold to maintain a risk-management framework and to file an annual ORSA Summary Report with the lead-state regulator. Extraction decomposes into:

- §3 Definitions — "Insurer"; "Insurance Group"; "Lead State"; "ORSA Summary Report".
- §4 Risk Management Framework — programme, board-oversight, risk-appetite rows.
- §5 ORSA Requirements — three-component ORSA (description of risk-management framework; insurer assessment of risk exposure; group risk-capital and prospective solvency assessment).
- §6 ORSA Summary Report — filing rows: annual filing with lead-state regulator; sharing with other domestic regulators on request.
- §8 Confidentiality — regulator-side confidentiality posture; not a licensee obligation row.
- §9 Sanctions — penalty regime; not a substantive obligation row.

#### Market-conduct examination standards

The NAIC Market Conduct Examiners Handbook is interpretive guidance for state-DOI market-conduct examinations of insurers. Pin to the handbook chapter when extracting (e.g., "Producer Licensing"; "Marketing and Sales"; "Underwriting and Rating"; "Claims"; "Complaint Handling"). The handbook is not directly binding on insurers; the binding text is the state insurance code provisions the handbook examines against. Extract from the underlying state code where the obligation lives, not from the handbook chapter alone.

#### NAIC Corporate Governance Annual Disclosure Model Act (Model 305)

Model 305 requires insurers to file an annual corporate-governance disclosure with the lead-state regulator. Extraction decomposes into the disclosure components (board governance; senior management responsibilities; oversight of audit, risk, and other key functions). State-adoption status varies; pin to the state-adopted version when extracting against a specific state.

#### When to escalate

The base SKILL.md is the right tool when the extraction feeds `obligation-mapping` for an insurer. When the extraction supports a state-DOI market-conduct examination readiness sprint, downstream consumers may include sector-specific exam-readiness skills (where they exist). The base skill produces the obligation list the readiness pack reads.

## payments-fintech

### Payments and fintech sector overlay — rule-to-obligation-extraction

Load this overlay when the rule under extraction is a CFPB rule under the consumer-financial protection statutes (Reg E, Reg Z, Reg DD, Reg P, Reg V, Reg X, Section 1071, Section 1033, UDAAP), a state money-transmitter rule, or a sponsor-bank or partnership-related rule for fintech-bank arrangements. The overlay carries the consumer-protection rule-citation conventions and the cross-jurisdiction obligation-decomposition pattern for state-by-state money-transmitter regimes.

#### CFPB Regulation citation conventions

- **Reg E** — Electronic Fund Transfer Act, 12 CFR Part 1005. Provisions: §1005.5 issuance; §1005.6 liability; §1005.7 disclosures; §1005.10 preauthorised transfers; §1005.11 procedures for resolving errors; §1005.18 prepaid accounts; §1005.20 gift cards; §1005.30-37 remittance transfers (the "Remittance Rule" subpart).
- **Reg Z** — Truth in Lending Act, 12 CFR Part 1026. Provisions span open-end and closed-end credit, mortgages, credit cards, ability-to-repay (§1026.43), HOEPA, integrated disclosures (TRID).
- **Reg DD** — Truth in Savings Act, 12 CFR Part 1030. Disclosure requirements for deposit accounts.
- **Reg P** — Privacy of Consumer Financial Information, 12 CFR Part 1016. GLBA privacy notices; opt-out rights; sharing-with-affiliates limitations.
- **Reg V** — Fair Credit Reporting Act, 12 CFR Part 1022. Identity-theft red-flag rules; risk-based-pricing notices; furnisher rules.
- **Reg X** — RESPA, 12 CFR Part 1024. Mortgage-servicer obligations; loss-mitigation procedures.
- **Reg B** — Equal Credit Opportunity Act, 12 CFR Part 1002. Includes Subpart B (Section 1071 small-business-lending data, 12 CFR 1002.101 through 12 CFR 1002.114, **as revised by the May 1, 2026 final rule**).
- **Section 1033** — Personal financial-data rights, 12 CFR Part 1033 (final rule 89 FR 90838, November 18 2024 [verify final FR cite]). **Compliance dates stayed as of October 29, 2025; CFPB-initiated reconsideration with ANPR.**
- **UDAAP** — 12 USC §5531 (Dodd-Frank Section 1031); not a rule with codified subsections, but the operative supervisory and enforcement standard. UDAAP-anchored extractions pin to the regulatory text, Supervisory Highlights, and consent-order articles for the operative standard. (Many CFPB Circulars on UDAAP topics were **withdrawn May 12, 2025; historical only**.)

#### CFPB Section 1071 — worked pattern

12 CFR 1002.101 through 12 CFR 1002.114 (Subpart B of Reg B), 88 FR 35150 (May 31 2023), as **revised by the May 1, 2026 final rule**. Under the revised rule the threshold is a single 1,000-covered-transactions trigger; the rule is effective June 30, 2026 and the compliance date is January 1, 2028. The 2023 tiered (2,500 / 500 / 100) compliance schedule is superseded; capture it only as historical context if at all.

Extraction decomposes into atomic obligations:

- **Covered-financial-institution determination** (12 CFR 1002.105(b), as revised). Trigger: each calendar year, the institution determines whether it originated 1,000 or more covered transactions in each of the two preceding years.
- **Covered-application-data-points obligation** (12 CFR 1002.107(a)). On each covered application: collect 20+ data points enumerated in §1002.107(a). Each data point is an obligation row in the extraction (or a single row with the data-point list as evidence_expected, depending on the granularity required by the consumer).
- **Firewall obligation** (12 CFR 1002.108). The covered FI must maintain procedures to limit the access of the underwriter to demographic data collected under §1002.107(a)(18)-(a)(20) where feasible. The exception (where a firewall is not feasible, the covered FI must provide a notice to the applicant) is its own row.
- **Recordkeeping obligation** (12 CFR 1002.111). Retain covered-application records for at least three years.
- **Reporting obligation** (12 CFR 1002.109). Submit the covered-application data to the CFPB by June 1 of each year covering the preceding calendar year. First-report due date follows the January 1, 2028 compliance date under the revised rule.
- **Effective-date-and-transition row**. Single compliance date (January 1, 2028) under the revised rule; rule effective June 30, 2026.

The defined terms section captures: "covered application"; "covered credit transaction"; "covered financial institution"; "covered originations"; "minority-owned business"; "women-owned business"; "LGBTQI+-owned business"; "small business"; "applicant".

#### CFPB Section 1033 — worked pattern

12 CFR Part 1033, 89 FR 90838 (November 18 2024) [verify final FR cite]. **Compliance dates stayed as of October 29, 2025; CFPB-initiated reconsideration with ANPR** — verify current docket status before transcribing tier-based compliance dates into the register. Extraction decomposes into:

- **Data-provider obligations**: make available to consumers and authorised third parties electronic-format data on covered consumer financial accounts.
- **Authorised-third-party obligations**: collect, use, and retain data only for the purposes authorised by the consumer; deletion-on-request obligation.
- **Standard-setter recognition**: CFPB process for recognising industry standard-setting bodies; not a direct obligation on regulated parties.
- **Recordkeeping obligation**: data providers must retain records of data-access requests.

#### Reg E error-resolution and remittance-rule patterns

- **Error-resolution procedures** (12 CFR 1005.11). Trigger: receipt of consumer notice of error within 60 days of the periodic statement. Action: investigate and report results within 10 business days; provisional credit if investigation extends beyond 10 business days. Action_type: notice_or_disclosure plus monitoring.
- **Remittance Rule disclosures** (12 CFR 1005.31, 1005.32, 1005.33). Pre-payment disclosure; receipt; error resolution; cancellation. Each is a row.

#### State money-transmitter rule structure

State money-transmission rules are state-by-state. The Money Transmission Modernization Act (MTMA) is a model law adopted by the Conference of State Bank Supervisors (CSBS) and adopted by an increasing number of states; the model is not law in any state until adopted. Extraction from a state money-transmitter rule pins to the state code section. Common shared concepts across states: licensing requirement; permissible-investments requirement; net-worth requirement; surety bond; reporting (call reports, BSA filings); notification of material change; consumer disclosures.

The cross-jurisdiction extraction pattern: when the rule under extraction is a model (MTMA, NAIC model, NCCUSL model), the extraction captures model-section obligations and flags state-by-state adoption status as the implementation question. Each state-adopted version is a separate extraction.

#### Sponsor-bank and bank-fintech partnership rule structure

The OCC, FRB, and FDIC have issued joint and individual guidance on bank-fintech partnerships and on banking-as-a-service relationships:

- **June 2023 Interagency Guidance on Third-Party Relationships: Risk Management** (88 FR 37920). Operative supervisory expectation; see the banking sector overlay.
- **OCC Bulletin 2023-25** [verify exact bulletin number] on third-party-relationships guidance for community banks.
- **Joint statement on the risks of crypto-asset arrangements** (January 3 2023; February 23 2023; September 7 2023 statements [verify dates]).
- **State-level bank-fintech partnership conditions** in some state DOIs.

Sponsor-bank obligations under partnership arrangements typically decompose into: oversight of the third-party fintech (life-cycle stages from the interagency guidance); BSA/AML programme responsibility for accounts opened through the fintech; consumer-protection programme responsibility; complaint handling; UDAAP oversight. The sponsor bank carries the regulatory obligation; the fintech carries contractual obligations to the sponsor bank that mirror the regulatory obligations. Extraction distinguishes between the regulatory obligation on the bank and the pass-through contractual obligation on the fintech.

#### When to escalate

The base SKILL.md is the right tool when the extraction feeds `obligation-mapping` for a fintech, payments firm, or sponsor bank. When the extraction crosses multiple jurisdictions (federal CFPB rule plus state money-transmitter regimes plus state UDAAP analogues), each jurisdiction is a separate extraction; the cross-jurisdiction view is built downstream by `obligation-mapping` running with multiple registers as input.
