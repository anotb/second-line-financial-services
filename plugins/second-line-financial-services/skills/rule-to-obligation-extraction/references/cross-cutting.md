# cross-cutting

One section per topic. Read only the sections the scope calls for.

## climate

### Climate cross-cutting overlay — rule-to-obligation-extraction

Load only when the rule under extraction is anchored to climate-related disclosure, climate-risk management, or sustainability reporting. The space is unsettled in the United States and more developed in the EU and UK; the extraction must capture the rule under extraction at the version in effect at the extraction date and flag the litigation or revision history where it is material.

#### US — SEC climate-related disclosure rule history

The SEC adopted the climate-related disclosure final rule on March 6 2024 (89 FR 21668, March 28 2024) and stayed it on April 4 2024 pending litigation. The rule's effective and compliance dates have been overtaken by subsequent procedural events; the extraction must read the rule's current operational status before producing rows. When the rule is operative, decomposition includes:

- **Material-climate-related-risks disclosure** (Reg S-K Item 1500 series). Annual disclosure of material climate-related risks affecting the registrant's strategy, business model, and outlook.
- **Governance disclosure**. Board oversight; management's role in assessing and managing material climate-related risks.
- **Risk-management disclosure**. Processes for identifying, assessing, and managing material climate-related risks.
- **Material-climate-targets-and-goals disclosure** (where the registrant has them).
- **Greenhouse-gas-emissions disclosure** (Scope 1 and Scope 2 for large accelerated filers and accelerated filers, where material). Scope 3 was not part of the final rule (changed from the proposal). Assurance requirements phased in.
- **Financial-statement footnote disclosures** of climate-related effects on financial statements.

When extracting from the rule (in any operational status), the source pin is the codified Reg S-K item number plus the FR cite. Litigation status goes in the open-extraction-questions section with a note on the blocker for downstream skills.

#### EU — Corporate Sustainability Reporting Directive (CSRD) and ESRS

- **Directive (EU) 2022/2464 (CSRD)** amends prior accounting and audit directives to require sustainability reporting by in-scope entities. Implementation is through member-state legislation; the directive is binding as to result. Reporting follows the European Sustainability Reporting Standards (ESRS) adopted as Commission Delegated Regulations.
- **ESRS adopted standards** (Commission Delegated Regulation (EU) 2023/2772): cross-cutting standards (ESRS 1 General requirements; ESRS 2 General disclosures); environmental standards (E1 climate change, E2 pollution, E3 water and marine resources, E4 biodiversity and ecosystems, E5 resource use and circular economy); social standards (S1 own workforce, S2 workers in the value chain, S3 affected communities, S4 consumers and end-users); governance standards (G1 business conduct).
- **Phased application**. CSRD applies in stages: large public-interest entities (financial year 2024); other large undertakings (FY 2025); listed SMEs and small and non-complex credit institutions (FY 2026 with a two-year deferral option); third-country undertakings (FY 2028).

Extraction from CSRD plus an ESRS standard pins to the ESRS standard reference (e.g., `ESRS E1 §AR.46`); each ESRS disclosure requirement is potentially a row depending on the granularity required.

#### EU — Sustainable Finance Disclosure Regulation (SFDR)

- **Regulation (EU) 2019/2088 (SFDR)** plus Commission Delegated Regulation (EU) 2022/1288 (RTS). Applies to financial-market participants and financial advisers. Decomposition: entity-level disclosures (Article 3 sustainability-risk policy; Article 4 due-diligence statements on principal adverse impacts; Article 5 remuneration policies); product-level disclosures (Article 6 sustainability-risk integration; Article 8 light-green products promoting environmental or social characteristics; Article 9 dark-green products with sustainable investment objective); periodic-reporting under the RTS templates.

#### EU — Taxonomy Regulation

- **Regulation (EU) 2020/852 (Taxonomy Regulation)** plus Commission Delegated Regulations. Defines environmentally sustainable economic activities and imposes turnover, capex, and opex disclosure obligations on financial-market participants and large undertakings. Decomposition: in-scope-activity classification; technical-screening-criteria conformity; do-no-significant-harm assessment; minimum-safeguards conformity; reported KPIs.

#### UK — TCFD-aligned and SDR

- **FCA TCFD-aligned disclosure** in PS 21/23 (asset managers) and PS 21/24 (listed-company premium-listed and standard-listed segment) [verify FCA policy-statement numbers]. Pin to the FCA Handbook chapter (ESG sourcebook; LR sourcebook).
- **FCA Sustainability Disclosure Requirements (SDR) and labels** (PS 23/16, November 28 2023; rules in ESG sourcebook). Anti-greenwashing rule effective May 31 2024; labels and naming-and-marketing rules staged through 2025.

#### ISSB-aligned standards

- **IFRS S1 General Requirements for Disclosure of Sustainability-related Financial Information** and **IFRS S2 Climate-related Disclosures** (issued June 2023). The ISSB standards are adopted by jurisdictions as their domestic-disclosure framework permits; jurisdiction-by-jurisdiction adoption status applies. Where a jurisdiction has adopted ISSB, the extraction pins to the jurisdiction's adoption instrument (e.g., the relevant securities regulator's rule) plus the IFRS S1/S2 reference.

#### Defined-term sensitivity

Climate rules are particularly sensitive to defined-term scope. Definitions to capture verbatim with their source pins:

- "Material climate-related risks" — varies; SEC framing under Reg S-K is the materiality standard from US securities law; CSRD-ESRS double-materiality differs.
- "Greenhouse-gas emissions" and the Scope 1/2/3 framing — usually GHG-Protocol-aligned but the rule's own definition controls.
- "Physical risk" and "transition risk" — sometimes defined; sometimes used without definition.
- "Sustainable investment" (SFDR Article 2(17)).
- "Environmentally sustainable economic activity" (Taxonomy Regulation Article 3).

#### When to layer with sector overlays

Climate obligations frequently sit on top of sector-specific rules. When the rule under extraction is a banking-supervisor climate-risk-management framework (e.g., FRB SR 23-5; OCC framework; PRA Supervisory Statement 3/19), load `cross-cutting.md#climate` and `sector-overlays.md#banking`. When the rule is a SEC disclosure rule, load `cross-cutting.md#climate` and `sector-overlays.md#capital-markets`. When the rule is a NAIC climate-risk disclosure framework, load `cross-cutting.md#climate` and `sector-overlays.md#insurance`.

## conduct

### Conduct cross-cutting overlay — rule-to-obligation-extraction

Load when the rule under extraction is anchored to UDAAP, fair lending, fair-and-responsible-banking, sales-practice supervision, complaint handling, marketing-and-disclosure conduct, or other conduct-risk topics. The conduct space combines affirmative-act obligations (deliver disclosures; maintain complaint-handling procedures) with prohibitions (do not engage in unfair, deceptive, or abusive acts; do not discriminate). The extraction must distinguish the two.

#### Prohibition versus affirmative-act distinction

Conduct rules typically combine:

- **Prohibitions**. The rule prohibits an act or pattern. Examples: UDAAP prohibition under Dodd-Frank Section 1031 (12 USC §5531); ECOA prohibition on discrimination on prohibited bases (15 USC §1691; 12 CFR 1002.4); Reg Z anti-evasion under §1026.43; SEC anti-fraud under Section 17(a) of the Securities Act and Section 10(b) of the Exchange Act and Rule 10b-5; FINRA Rule 2010 (just and equitable principles). Each prohibition is a row with `action_type: prohibition`.
- **Affirmative acts**. The rule requires the regulated party to do something to manage the conduct risk. Examples: maintain a written complaint-handling procedure; train personnel; conduct fair-lending statistical-monitoring analysis; deliver disclosures at named decision points; supervise sales practices.

A common extraction defect is folding the affirmative-act obligation into the prohibition. The two are different and the evidence shape differs (a prohibition is satisfied by absence of the prohibited conduct, evidenced by surveillance records and incident reviews; an affirmative act is satisfied by the named act, evidenced by the artifact of the act).

#### UDAAP — extraction posture

UDAAP is unusual: the operative standard sits in 12 USC §5531 plus the agency-statement framing (CFPB UDAAP Exam Manual; OCC and FDIC adoption of CFPB framework for institutions in their primary supervision). Extraction from "UDAAP" alone is not feasible; UDAAP is a standard, not a discrete rule. The practical extraction approach:

- When the source is a CFPB circular interpreting UDAAP for a specific practice (e.g., Circular 2022-03 on adverse-action notices when AI is used; Circular on negative-option marketing; Circular on overdraft practices), pin to the circular and decompose into the specific obligation pattern the circular surfaces.
- When the source is a CFPB consent order describing UDAAP-prohibited practices, pin to the order's articles and decompose into the remediation obligations the firm should also satisfy.
- When the source is the CFPB UDAAP Exam Manual, pin to the manual section; the manual is interpretive, and the binding text is 12 USC §5531 plus the agency's stated interpretation.

UDAAP-anchored extractions carry higher uncertainty because the operative standard is a standard rather than a rule; confidence labels are typically medium for the obligation rows, with the open-question section flagging the interpretive ambiguity.

#### Fair-lending — ECOA, FHA, HMDA

- **ECOA**, 15 USC §1691; **Reg B**, 12 CFR Part 1002. Prohibitions on discrimination on prohibited bases (race, color, religion, national origin, sex, marital status, age, receipt of public assistance, exercise of rights under the Consumer Credit Protection Act). Affirmative-act obligations include: notification of action taken (§1002.9); adverse-action notice content; record retention (§1002.12); and (for covered FIs) Section 1071 small-business-lending data (Subpart B; see the payments-fintech sector overlay for the worked pattern).
- **Fair Housing Act**, 42 USC §3601 et seq. Parallel prohibitions in mortgage and home-improvement lending; HUD and DOJ enforcement plus banking-agency enforcement under FFIEC framework.
- **HMDA / Reg C**, 12 CFR Part 1003. Reporting obligations on home-mortgage data: covered-institution determination; covered-loan determination; loan-application register data points; submission to the FFIEC by March 1 of each year.

#### Marketing rule and communications-with-the-public conduct

- **Investment Adviser Marketing Rule**, Rule 206(4)-1 (see capital-markets sector overlay for the worked pattern). The rule combines a general anti-fraud prohibition with specific affirmative-act obligations on testimonials, endorsements, third-party ratings, and performance presentations.
- **FINRA Rule 2210** communications with the public. Categorisation (institutional, retail, correspondence); pre-use approval; filing with FINRA; content standards.
- **Reg O 12 CFR 1024 RESPA** and other consumer-finance disclosure rules carry conduct-shaped obligations (delivery timing; clear-and-prominent standards; integrated-disclosure requirements).

#### Complaint handling

- **CFPB framing**. The CFPB UDAAP Exam Manual treats complaint-handling as a key indicator of UDAAP risk; the Bureau publishes the consumer-complaint database. Affirmative-act obligations: maintain a complaint-handling process; categorise and route complaints; report complaint trends to senior management and the board; investigate complaints meaningfully and provide responses; identify systemic issues from complaint patterns.
- **FINRA Rule 4530**. Reporting obligations to FINRA on customer complaints, certain regulatory and litigation events, and internal-conclusions-of-violation. Each named reporting trigger is a row.
- **Sectoral conduct rules**. Reg E error-resolution (12 CFR 1005.11; see payments-fintech overlay); Reg Z error-resolution and billing-error procedures (12 CFR 1026.13); Reg X loss-mitigation procedures (12 CFR 1024.41).

#### Sales-practice supervision

- **FINRA Rule 3110** supervision. Written supervisory procedures; designated supervisors; reasonable inquiry into associated persons; review of communications; internal inspections.
- **Section 15 of the Exchange Act** (broker-dealer registration and conduct).
- **Investment Adviser Compliance Programme Rule** 206(4)-7. Written compliance programme; chief compliance officer designation; annual review.
- **Reg BI** 17 CFR 240.15l-1. Best-interest obligation when making a recommendation to a retail customer.

#### Conduct rule expectations under principles-based regimes

UK (FCA) and EU (some directives) operate principles-based rather than rules-based. The FCA Principles for Businesses (PRIN sourcebook) and the Consumer Duty (PRIN 2A) are principles-anchored; the operative obligation under PRIN 2A is the firm's obligation to act to deliver good outcomes to retail customers across products and services, price and value, consumer understanding, and consumer support. Extraction from a principles-based regime captures the principle and then decomposes into the FCA's stated supervisory expectations (in policy statements, finalised guidance, and Dear CEO letters); each supervisory expectation is a row with `action_verb` carrying the FCA's modal verb (firms `should`; firms `must`; FCA `expects`).

#### When to layer with sector overlays

Conduct obligations frequently sit on top of sector-specific rules. When the rule under extraction is a CFPB circular, load `cross-cutting.md#conduct` and `sector-overlays.md#payments-fintech`. When the rule is FINRA Rule 2210 or Rule 3110, load `cross-cutting.md#conduct` and `sector-overlays.md#capital-markets`. When the rule is a state DOI market-conduct manual chapter, load `cross-cutting.md#conduct` and `sector-overlays.md#insurance`.

## cyber

### Cyber cross-cutting overlay — rule-to-obligation-extraction

Load when the rule under extraction is anchored to cybersecurity, computer-security incident response, ICT risk management, or operational resilience. Cyber rules cross sector boundaries: SEC Item 1.05 lands on registrants; the 36-hour bank notification rule lands on banking organisations; NYDFS Part 500 lands on DFS-regulated entities; DORA lands on EU financial entities; NAIC Model 668 lands on insurance licensees in adopting states. The overlay carries the recurrent extraction patterns specific to incident-reporting timing and to programme obligations.

#### Incident-reporting timing — comparative table

The extraction must respect each rule's specific clock; incident-reporting rules are notoriously close in shape and different in detail, and substituting one rule's clock for another is a quiet extraction defect.

| Rule | Trigger | Clock | Action |
|---|---|---|---|
| SEC Form 8-K Item 1.05 (17 CFR 249.308; Reg S-K Item 106) | Materiality determination of a covered cybersecurity incident | Within 4 business days of the determination | File Form 8-K Item 1.05 disclosure; Attorney-General-national-security delay exception under 1.05(c) |
| 12 CFR Part 53 (OCC); 12 CFR Part 225 Subpart N (FRB); 12 CFR Part 304 Subpart C (FDIC) — bank notification rule | Determination of a "notification incident" | As soon as possible and no later than 36 hours after determination | Notify the primary federal regulator |
| Bank-service-provider notification under the same rule | BSP determination of a covered incident materially disrupting or degrading services | As soon as possible | Notify each affected banking-organisation customer |
| 23 NYCRR Part 500.17(a) (NYDFS) | Cybersecurity event | As promptly as possible, no later than 72 hours from determination | Notify the Superintendent |
| NYDFS Part 500.17(c) (ransomware extortion payments, post-2023 amendment) | Extortion-payment determination | Within 24 hours of payment | Notify the Superintendent |
| EU Regulation 2022/2554 (DORA) Article 19 | Major ICT-related incident | Initial notification within hours; intermediate and final reports within deadlines set by RTS | Notify competent authority |
| NAIC Model 668 §6 / state-adopted versions | Determination of a "Cybersecurity Event" | Within 72 hours from determination | Notify Commissioner; affected-consumer and reinsurer notifications follow |
| GLBA Safeguards Rule, 16 CFR 314.5 (FTC; rev. 2023 amendments) | Notification event | As soon as possible, no later than 30 days after discovery (FTC-only; 500-customer threshold) | Notify the FTC |
| HIPAA Breach Notification Rule, 45 CFR 164.404 — 408 (when in scope) | Discovery of a breach of unsecured PHI | Without unreasonable delay; no later than 60 days for individual notice; concurrent HHS notice for breaches of 500+ | Multiple notices |

When extracting an incident-reporting obligation, the extraction row captures: the trigger (carefully — "material incident" is not the same as "notification incident" is not the same as "cybersecurity event" is not the same as "covered cybersecurity incident"); the clock and its starting condition; the recipient; the form of notice; and any exception or delay provision.

#### Programme-and-policy obligations

Cyber rules typically also impose standing programme obligations distinct from the incident-reporting timing:

- **Written programme**. The rule requires the regulated party to maintain a written cybersecurity programme covering risk-assessment, access controls, encryption (in transit and at rest), multi-factor authentication, monitoring and detection, incident response, business continuity and disaster recovery, vendor and third-party security, training, and periodic review. Each named domain is potentially its own obligation row depending on the rule's granularity. Examples: NYDFS Part 500 §500.2 (programme), §500.3 (policy), §500.5 (testing), §500.7 (access privileges), §500.11 (third-party); GLBA Safeguards Rule 16 CFR 314.4 elements; NAIC Model 668 §4.
- **Officer designation**. The rule requires designation of a CISO or qualified individual responsible for the programme. NYDFS §500.4; NAIC Model 668 §4(C); GLBA Safeguards Rule §314.4(a). Each is a row.
- **Risk assessment**. Periodic risk assessment that informs the programme. Most rules require it; the cadence varies (annual is common). Each rule has its own row.
- **Third-party security oversight**. The programme must extend to third-party service providers with access to information systems or non-public information. NYDFS §500.11; NAIC Model 668 §4(F); the bank notification rule's BSP-side row.
- **Penetration testing and vulnerability assessment**. NYDFS §500.5 explicitly; other rules implicitly through the programme requirement.
- **Reporting to the board or board committee**. Annual or more-frequent CISO report to the board on the programme. NYDFS §500.4(c); NAIC Model 668 §4(H); FFIEC IT Handbook expectations.

#### Defined-term sensitivity

Cyber rules are particularly sensitive to defined-term scope. Definitions to capture verbatim with their source pins:

- "Cybersecurity incident" / "covered cybersecurity incident" (SEC Item 106(a) and the 8-K Item 1.05).
- "Computer-security incident" / "notification incident" (the bank notification rule, Part 53.2).
- "Cybersecurity event" (NYDFS Part 500.1; NAIC Model 668 §3).
- "ICT-related incident" / "major ICT-related incident" (DORA Article 3).
- "Critical or important function" (DORA Article 3).
- "Critical ICT third-party service provider" (DORA Article 31).
- "Information system" (multiple rules; definitions differ).
- "Nonpublic information" (NYDFS Part 500.1; NAIC Model 668 §3).
- "Multi-factor authentication" (NYDFS Part 500.1; NAIC Model 668 §3).

The defined-term differences across rules are the most common source of cross-rule confusion. The extraction's defined-terms section captures each term with its source pin; the obligation row's `defined_terms_used` column records which terms the row depends on.

#### DORA worked pattern

Regulation (EU) 2022/2554, OJ L 333/1. Application date January 17 2025. Decomposition:

- **Article 5** ICT governance. Governance row: management-body responsibility for ICT risk management framework approval and oversight.
- **Article 6** ICT risk-management framework. Programme row covering identification, protection, detection, response and recovery, learning and evolving.
- **Article 9** Protection and prevention.
- **Article 10** Detection.
- **Article 11** Response and recovery; business-continuity policy and ICT response and recovery plans.
- **Article 17** ICT-related incident management process. Programme row.
- **Article 18** Classification of ICT-related incidents. Methodology row.
- **Article 19** Reporting of major ICT-related incidents. Reporting rows: initial; intermediate; final; significant cyber-threat voluntary notification.
- **Article 24** Digital operational resilience testing programme. Programme row.
- **Article 28** Management of ICT third-party risk. Programme rows; contract-clause rows (Article 30 specifies minimum contractual provisions).
- **Article 30** Key contractual provisions. Each enumerated provision is a row that the financial entity must obtain in its contracts with ICT third-party service providers.
- **Article 31** Designation of critical ICT third-party service providers. Designation regime; not a direct obligation on the financial entity but a regulatory designation that triggers oversight.

#### When to layer with sector overlays

Cyber obligations frequently sit on top of sector-specific rules. When the rule under extraction is the bank notification rule (12 CFR Part 53 / 225 / 304), load both `cross-cutting.md#cyber` and `sector-overlays.md#banking`. When the rule is SEC Item 1.05, load both `cross-cutting.md#cyber` and `sector-overlays.md#capital-markets`. The cross-cutting overlay carries the comparative-table view; the sector overlay carries the rule's procedural and supervisory context.

## privacy

### Privacy cross-cutting overlay — rule-to-obligation-extraction

Load when the rule under extraction is anchored to privacy, data protection, notice-and-consent, data minimisation, deletion rights, or disposal of consumer information. Privacy rules cross sector boundaries: GLBA Privacy Rule and Safeguards Rule land on most financial institutions; Reg P implements the GLBA Privacy Rule for CFPB-regulated entities; SEC Reg S-P amendments add incident-response programme requirements for SEC registrants; state privacy laws (CCPA/CPRA, VCDPA, CTDPA, others) layer on top with broad data-controller obligations; sector-specific privacy rules (HIPAA for protected health information) apply where in scope.

#### Notice-and-consent extraction pattern

Privacy rules typically decompose into a notice-and-consent spine plus the substantive data-handling controls:

- **Initial-notice obligation**. At account opening or relationship establishment, the regulated party must deliver a privacy notice describing the categories of nonpublic personal information collected, disclosed, and the right (where it exists) to opt out of certain disclosures.
- **Annual-notice obligation** (where it applies). Where the rule requires annual delivery of the privacy notice (Reg P §1016.5; some state laws), the extraction captures the cadence and the form.
- **Opt-out obligation**. Where the consumer has the right to opt out of certain disclosures (e.g., disclosures to non-affiliated third parties under Reg P §1016.10; sale or sharing under CCPA/CPRA), the extraction captures the right, the timing of the notice giving effect to the right, and the recipient-side obligation to honour the opt-out.
- **Consent obligation** (where it applies). Where the rule requires affirmative consent for certain processing (e.g., targeted-advertising opt-in under CTDPA for sensitive data; sensitive-personal-information opt-in under CPRA; HIPAA authorisation for non-treatment uses), the extraction captures the trigger, the form, and the duration.

#### Reg P / GLBA Privacy Rule worked pattern

12 CFR Part 1016 (CFPB Reg P; the rule was formerly Federal Reserve Reg P at 12 CFR Part 216 before Dodd-Frank transferred authority). Extraction decomposes into:

- §1016.4 Initial notice. Programme row: initial-notice content and timing.
- §1016.5 Annual notice. Frequency: periodic (annual). Action_type: notice_or_disclosure. Exception: §1016.5(e) eliminates annual notice in some circumstances when the FI has not changed sharing practices and provides specific limited disclosures.
- §1016.6 Information to be included. Content rows.
- §1016.7 Form of opt-out notice. Form-of-notice rows.
- §1016.10 Limits on disclosure of nonpublic personal information to non-affiliated third parties. Prohibition rows; exception rows for service-provider and joint-marketing arrangements (§1016.13), processing-and-servicing exceptions (§1016.14), other exceptions (§1016.15).
- §1016.16 Limits on redisclosure and reuse of information. Prohibition rows.
- §1016.17 Limits on sharing account-number information for marketing purposes. Prohibition row.

#### GLBA Safeguards Rule worked pattern

16 CFR Part 314 (FTC). The 2021 amendments (effective in stages through June 9 2023) and the 2023 amendments (notification event added) restructured the Rule. Extraction decomposes into:

- §314.3 Standards for safeguarding customer information. Programme row.
- §314.4 Elements of the information-security programme. Each element is a row: §314.4(a) qualified-individual designation; §314.4(b) risk-assessment; §314.4(c) safeguards (eight enumerated controls, each a row); §314.4(d) regular monitoring and testing; §314.4(e) employee training and oversight; §314.4(f) service-provider oversight; §314.4(g) periodic re-evaluation; §314.4(h) incident-response plan; §314.4(i) annual report by the qualified individual to the board or governing body.
- §314.5 Notification event reporting (added 2023). Trigger and clock as captured in `cross-cutting.md#cyber`.

#### SEC Reg S-P amendments worked pattern

89 FR 47688 (June 3 2024) [verify final FR cite], codified amendments to 17 CFR Part 248. Extraction decomposes into incident-response programme; customer-notice obligation following an unauthorised access or use of customer information; service-provider oversight; recordkeeping. Compliance dates staged by registrant size.

#### State comprehensive privacy laws

State privacy laws (CCPA, CPRA, CDPA Virginia, CPA Colorado, CTDPA Connecticut, UCPA Utah, and others adopted since 2018) impose data-controller and data-processor obligations on a broad range of businesses. Extraction patterns vary by state but the spine is consistent:

- **Notice obligation** (privacy policy on collection and processing).
- **Consumer-rights obligations**: right to know; right to access; right to delete; right to correct; right to opt out of sale or sharing or targeted advertising; right to portability; right to limit use of sensitive personal information (CPRA only, with parallels in some other states).
- **Sensitive-personal-information processing obligation**: opt-in consent (most states) or opt-out (CCPA-style).
- **Data-protection-impact-assessment obligation** (most states except CCPA/CPRA, which has narrower assessment requirements).
- **Service-provider/processor contract obligation**: minimum contractual provisions on processing.
- **Universal opt-out signal recognition** (CPRA; CTDPA; CDPA opt-out preference signals).

Extraction is state-by-state. Where the rule under extraction is a single state's law, pin to that state's code. Where the work is a multi-state inventory, each state is a separate extraction.

#### HIPAA Privacy and Security Rules (where in scope)

Where the financial-services entity is a covered entity or business associate under HIPAA (e.g., an insurer that issues health plans; a third-party administrator), the HIPAA Privacy Rule (45 CFR Part 164 Subpart E) and HIPAA Security Rule (45 CFR Part 164 Subpart C) apply. Extraction follows the standard programme-plus-notice-plus-rights pattern; pin to 45 CFR §164.NNN.

#### When to layer with sector overlays

Privacy obligations frequently sit on top of sector-specific rules. When the rule under extraction is Reg P, load `cross-cutting.md#privacy` and `sector-overlays.md#payments-fintech` (or banking, depending on the institution). When the rule is SEC Reg S-P, load `cross-cutting.md#privacy` and `sector-overlays.md#capital-markets`. When the rule is NAIC Model 668 (which has both cyber and privacy elements), load `cross-cutting.md#cyber`, `cross-cutting.md#privacy`, and `sector-overlays.md#insurance`.
