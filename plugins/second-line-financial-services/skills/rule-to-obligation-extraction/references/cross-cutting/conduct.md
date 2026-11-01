# Conduct cross-cutting overlay — rule-to-obligation-extraction

Load when the rule under extraction is anchored to UDAAP, fair lending, fair-and-responsible-banking, sales-practice supervision, complaint handling, marketing-and-disclosure conduct, or other conduct-risk topics. The conduct space combines affirmative-act obligations (deliver disclosures; maintain complaint-handling procedures) with prohibitions (do not engage in unfair, deceptive, or abusive acts; do not discriminate). The extraction must distinguish the two.

## Prohibition versus affirmative-act distinction

Conduct rules typically combine:

- **Prohibitions**. The rule prohibits an act or pattern. Examples: UDAAP prohibition under Dodd-Frank Section 1031 (12 USC §5531); ECOA prohibition on discrimination on prohibited bases (15 USC §1691; 12 CFR 1002.4); Reg Z anti-evasion under §1026.43; SEC anti-fraud under Section 17(a) of the Securities Act and Section 10(b) of the Exchange Act and Rule 10b-5; FINRA Rule 2010 (just and equitable principles). Each prohibition is a row with `action_type: prohibition`.
- **Affirmative acts**. The rule requires the regulated party to do something to manage the conduct risk. Examples: maintain a written complaint-handling procedure; train personnel; conduct fair-lending statistical-monitoring analysis; deliver disclosures at named decision points; supervise sales practices.

A common extraction defect is folding the affirmative-act obligation into the prohibition. The two are different and the evidence shape differs (a prohibition is satisfied by absence of the prohibited conduct, evidenced by surveillance records and incident reviews; an affirmative act is satisfied by the named act, evidenced by the artifact of the act).

## UDAAP — extraction posture

UDAAP is unusual: the operative standard sits in 12 USC §5531 plus the agency-statement framing (CFPB UDAAP Exam Manual; OCC and FDIC adoption of CFPB framework for institutions in their primary supervision). Extraction from "UDAAP" alone is not feasible; UDAAP is a standard, not a discrete rule. The practical extraction approach:

- When the source is a CFPB circular interpreting UDAAP for a specific practice (e.g., Circular 2022-03 on adverse-action notices when AI is used; Circular on negative-option marketing; Circular on overdraft practices), pin to the circular and decompose into the specific obligation pattern the circular surfaces.
- When the source is a CFPB consent order describing UDAAP-prohibited practices, pin to the order's articles and decompose into the remediation obligations the firm should also satisfy.
- When the source is the CFPB UDAAP Exam Manual, pin to the manual section; the manual is interpretive, and the binding text is 12 USC §5531 plus the agency's stated interpretation.

UDAAP-anchored extractions carry higher uncertainty because the operative standard is a standard rather than a rule; confidence labels are typically medium for the obligation rows, with the open-question section flagging the interpretive ambiguity.

## Fair-lending — ECOA, FHA, HMDA

- **ECOA**, 15 USC §1691; **Reg B**, 12 CFR Part 1002. Prohibitions on discrimination on prohibited bases (race, color, religion, national origin, sex, marital status, age, receipt of public assistance, exercise of rights under the Consumer Credit Protection Act). Affirmative-act obligations include: notification of action taken (§1002.9); adverse-action notice content; record retention (§1002.12); and (for covered FIs) Section 1071 small-business-lending data (Subpart B; see the payments-fintech sector overlay for the worked pattern).
- **Fair Housing Act**, 42 USC §3601 et seq. Parallel prohibitions in mortgage and home-improvement lending; HUD and DOJ enforcement plus banking-agency enforcement under FFIEC framework.
- **HMDA / Reg C**, 12 CFR Part 1003. Reporting obligations on home-mortgage data: covered-institution determination; covered-loan determination; loan-application register data points; submission to the FFIEC by March 1 of each year.

## Marketing rule and communications-with-the-public conduct

- **Investment Adviser Marketing Rule**, Rule 206(4)-1 (see capital-markets sector overlay for the worked pattern). The rule combines a general anti-fraud prohibition with specific affirmative-act obligations on testimonials, endorsements, third-party ratings, and performance presentations.
- **FINRA Rule 2210** communications with the public. Categorisation (institutional, retail, correspondence); pre-use approval; filing with FINRA; content standards.
- **Reg O 12 CFR 1024 RESPA** and other consumer-finance disclosure rules carry conduct-shaped obligations (delivery timing; clear-and-prominent standards; integrated-disclosure requirements).

## Complaint handling

- **CFPB framing**. The CFPB UDAAP Exam Manual treats complaint-handling as a key indicator of UDAAP risk; the Bureau publishes the consumer-complaint database. Affirmative-act obligations: maintain a complaint-handling process; categorise and route complaints; report complaint trends to senior management and the board; investigate complaints meaningfully and provide responses; identify systemic issues from complaint patterns.
- **FINRA Rule 4530**. Reporting obligations to FINRA on customer complaints, certain regulatory and litigation events, and internal-conclusions-of-violation. Each named reporting trigger is a row.
- **Sectoral conduct rules**. Reg E error-resolution (12 CFR 1005.11; see payments-fintech overlay); Reg Z error-resolution and billing-error procedures (12 CFR 1026.13); Reg X loss-mitigation procedures (12 CFR 1024.41).

## Sales-practice supervision

- **FINRA Rule 3110** supervision. Written supervisory procedures; designated supervisors; reasonable inquiry into associated persons; review of communications; internal inspections.
- **Section 15 of the Exchange Act** (broker-dealer registration and conduct).
- **Investment Adviser Compliance Programme Rule** 206(4)-7. Written compliance programme; chief compliance officer designation; annual review.
- **Reg BI** 17 CFR 240.15l-1. Best-interest obligation when making a recommendation to a retail customer.

## Conduct rule expectations under principles-based regimes

UK (FCA) and EU (some directives) operate principles-based rather than rules-based. The FCA Principles for Businesses (PRIN sourcebook) and the Consumer Duty (PRIN 2A) are principles-anchored; the operative obligation under PRIN 2A is the firm's obligation to act to deliver good outcomes to retail customers across products and services, price and value, consumer understanding, and consumer support. Extraction from a principles-based regime captures the principle and then decomposes into the FCA's stated supervisory expectations (in policy statements, finalised guidance, and Dear CEO letters); each supervisory expectation is a row with `action_verb` carrying the FCA's modal verb (firms `should`; firms `must`; FCA `expects`).

## When to layer with sector overlays

Conduct obligations frequently sit on top of sector-specific rules. When the rule under extraction is a CFPB circular, load `cross-cutting/conduct.md` and `sector-overlays/payments-fintech.md`. When the rule is FINRA Rule 2210 or Rule 3110, load `cross-cutting/conduct.md` and `sector-overlays/capital-markets.md`. When the rule is a state DOI market-conduct manual chapter, load `cross-cutting/conduct.md` and `sector-overlays/insurance.md`.
