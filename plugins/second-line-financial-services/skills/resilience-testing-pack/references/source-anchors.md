# Source anchors — resilience-testing-pack

The named, dated regulatory sources this skill anchors to. SKILL.md cites this file by path and does not restate excerpts. Sector-specific and cross-cutting anchors live in the corresponding overlay files.

## Primary frame — operational-resilience and third-party testing expectations

- **Interagency Guidance on Third-Party Relationships: Risk Management** (OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, issued June 6, 2023). Ongoing-monitoring expectations include testing of vendor performance and contingency plans on a risk-based basis [verify section numbering across the released bulletin]. Risk-based application; more substantive testing expected for critical activities. OCC release: https://www.occ.gov/news-issuances/news-releases/2023/nr-ia-2023-53.html . FDIC release: https://www.fdic.gov/news/press-releases/2023/pr23047.html . FRB release: https://www.federalreserve.gov/newsevents/pressreleases/bcreg20230606a.htm .

- **OCC Bulletin 2013-29 — Third-Party Relationships: Risk Management Guidance** (October 30, 2013). Historical framing for vendor-test-result review. The June 2023 interagency guidance is the operative anchor. https://www.occ.gov/news-issuances/bulletins/2013/bulletin-2013-29.html .

- **FFIEC Information Technology Examination Handbook — Business Continuity Management booklet** [verify current edition and section structure]. The testing-and-exercise section is the examiner-facing reference for the test-method taxonomy: tabletop, walkthrough, simulation, full-functional exercise. Recovery-strategy considerations including third-party arrangements. https://ithandbook.ffiec.gov/ .

- **FFIEC Information Technology Examination Handbook — Outsourcing Technology Services booklet** [verify current edition and section structure]. Vendor BCDR-test posture; firm review of vendor test results; risk-based testing depth for technology service providers. https://ithandbook.ffiec.gov/ .

- **FFIEC inter-agency cloud joint statement** (Security in a Cloud Computing Environment, April 30, 2020) [verify exact title and date]. Cloud-services BCDR testing including failover validation, customer-data-portability rehearsals, and shared-responsibility-model testing.

- **DORA — Regulation (EU) 2022/2554, Article 24**. Digital operational resilience testing programme for in-scope financial entities; programme is risk-based, proportionate, and documented. https://eur-lex.europa.eu/eli/reg/2022/2554/oj .

- **DORA — Regulation (EU) 2022/2554, Article 25**. Test types: vulnerability assessments, open-source analyses, network security assessments, gap analyses, physical security reviews, source code reviews, scenario-based tests, compatibility testing, performance testing, end-to-end testing, penetration testing. The breadth of named test types matters for programme design.

- **DORA — Regulation (EU) 2022/2554, Article 26**. Advanced testing including threat-led penetration testing (TLPT) for designated firms. Designation criteria, methodology, and supervisory engagement model.

- **Commission Delegated Regulation (EU) 2025/1190 of 13 February 2025** (OJ 18 June 2025, applicable from 8 July 2025) — RTS on threat-led penetration testing under DORA Article 26. Specifies criteria for identifying financial entities required to perform TLPT; test cadence (at least once every three years unless otherwise specified by the competent authority); red-team / control-team / blue-team conventions; live-production testing scope; reporting. Aligned to TIBER-EU. https://eur-lex.europa.eu/eli/reg_del/2025/1190/oj/eng .

- **EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02)**. Test posture guideline within the outsourcing-monitoring expectations [verify section number]. https://www.eba.europa.eu/regulation-and-policy/internal-governance/guidelines-on-outsourcing-arrangements .

- **BCBS Principles for Operational Resilience** (March 2021). Mapping principle, scenario-testing principle, third-party-arrangement principle, ICT principle. https://www.bis.org/bcbs/publ/d516.htm .

- **UK PRA SS1/21 (Operational resilience: impact tolerances for important business services, March 2021; updated March 2022)** and **SS2/21 (Outsourcing and third-party risk management, March 2021)**. UK overlay only. Operational-resilience compliance milestone was 31 March 2025. PS7/26 with SS1/26 introduces a UK incident-reporting and material-third-party-arrangement-reporting framework and updates SS2/21; verify current version on engagement date. Severe-but-plausible scenario testing is the testing frame; impact-tolerance is the test the recovery posture must meet. https://www.bankofengland.co.uk/prudential-regulation/publication/2021/march/operational-resilience-impact-tolerances-for-important-business-services-ss . `[verify section]`

- **TIBER-EU framework** (European Central Bank) [verify current version and date]. Threat-led penetration-testing methodology referenced by DORA Article 26 advanced-testing requirements. https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/ .

- **CBEST framework** (Bank of England) [verify current version]. UK threat-led penetration-testing framework where applicable.

## Bank-specific anchors (banking overlay carries the detail)

- **12 CFR Part 30 Appendix D (OCC Heightened Standards)**. Risk-governance framework for $50B+ covered banks; the testing programme and outcomes feed the framework and the board's third-party oversight. §III risk-governance framework, §III.B risk appetite [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-I/part-30 .

- **Bank Service Company Act, 12 USC §1867(c)**. Statutory examiner-access right over bank service providers; examination access continues into and after a test. https://www.law.cornell.edu/uscode/text/12/1867 .

- **FRB SR 12-17 consolidated supervision framework** for BHCs [verify section]. https://www.federalreserve.gov/supervisionreg/srletters/sr1217.htm .

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Sponsor-bank programme reconciliation, FBO subledger validation, deposit-insurance representation; testing rehearsal for these elements.

- **Joint statement on community-bank fintech due diligence** (OCC / FRB / FDIC, FIL-59-2021, August 27, 2021) [verify exact title and date] [verify section]. Community-bank-specific framework for testing of fintech vendor relationships. https://www.fdic.gov/news/financial-institution-letters/2021/fil21059.html .

## Insurance-specific anchors (insurance overlay carries the detail)

- **NAIC Insurance Data Security Model Law (Model #668), §4.F** third-party service-provider obligations. State-by-state adoption.

- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]. Critical outsourced functions and material test outcomes feed the ORSA Summary Report.

- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and Holding Company Model Regulation (Model #450) [verify model number]. Form B / Form D filings on affiliate arrangements that are tested.

- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023). AIS Program elements include third-party-AI testing posture. https://content.naic.org/sites/default/files/inline-files/2023-12-04%20Model%20Bulletin_Adopted_0.pdf [verify URL].

- **Colorado SB 21-169 implementing regulation** (3 CCR 702-10 §1 [verify section]) — governance and risk management of ECDIS and predictive models in life-insurance underwriting; vendor-AI testing posture.

- **NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting** (January 2024) [verify exact circular number].

- **EIOPA Guidelines on outsourcing to cloud service providers (2020)** [verify reference]. EU insurer cloud-outsourcing test posture.

## Capital-markets-specific anchors (capital-markets overlay carries the detail)

- **Reg SCI — 17 CFR §242.1000 et seq.** [verify subsection numbering]. SCI-entity testing programme: BCDR test with designated members, industry-wide test, testing-of-system-changes, notice-and-reporting of test results. https://www.ecfr.gov/current/title-17/chapter-II/part-242 .

- **CFTC system-safeguards rules** — 17 CFR §38.1051 (DCMs), §39.18 (DCOs), §49.24 (SDRs) [verify section]. Testing-and-exercise expectations on covered entities. https://www.ecfr.gov/current/title-17 .

- **FINRA Rule 4370** (Business Continuity Plans) [verify reference]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/4370 .

- **Investment Advisers Act Rule 206(4)-7**. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 .

- **Investment Company Act Rule 38a-1(a)(4)**. Service-provider compliance-program adequacy includes BCDR-test posture. https://www.ecfr.gov/current/title-17/chapter-II/part-270/section-270.38a-1 .

- **17 CFR §§240.17a-4, 275.204-2, 270.31a — books-and-records preservation rules**. Test artefacts containing books-and-records material are inside the rule.

## Payments-fintech-specific anchors (payments-fintech overlay carries the detail)

- **NACHA Operating Rules (current edition)** Third-Party Sender risk-management rules [verify rule citations]. Paywalled; cite as "current edition; specific sections to be confirmed against the firm's licensed copy." https://www.nacha.org/ .

- **FedNow Service operating rules and procedures** [verify section reference for current version]. Instant-payment-rail testing-of-failover posture. https://www.frbservices.org/financial-services/fednow .

- **The Clearing House RTP operating rules** [verify section reference for current version]. Instant-payment-rail testing-of-failover posture. https://www.theclearinghouse.org/payment-systems/rtp .

- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state including any litigation or congressional review].

- **Reg E (12 CFR Part 1005)** §1005.6, §1005.11, §1005.18. https://www.ecfr.gov/current/title-12/chapter-X/part-1005 .

## Cyber cross-cutting anchors (cyber overlay carries the detail)

- **NYDFS 23 NYCRR Part 500.16** — incident-response-plan testing obligation; §500.16 periodic testing requirement. https://www.dfs.ny.gov/industry_guidance/cybersecurity .

- **NYDFS 23 NYCRR Part 500.11** — third-party-service-provider security policy.

- **FFIEC Information Technology Examination Handbook — Information Security booklet** [verify current edition and section].

- **SEC final rule on cybersecurity disclosure** — Item 1.05 Form 8-K and Reg S-K Item 106 (effective 2023). https://www.sec.gov/files/rules/final/2023/33-11216.pdf [verify URL].

- **Reg S-P (May 2024 amendments)**, 17 CFR Part 248 [verify exact compliance dates by entity type and size]. https://www.sec.gov/files/rules/final/2024/34-100155.pdf [verify URL].

- **CISA shared-responsibility model for cloud** [verify exact title and section of the CISA publication referenced]. https://www.cisa.gov/ .

- **CISA tabletop-exercise packages** [verify section] as scenario inputs. https://www.cisa.gov/cisa-tabletop-exercise-packages .

- **MITRE ATT&CK** [verify section] as scenario taxonomy for cyber-event scenario design. https://attack.mitre.org/ .

## Privacy cross-cutting anchors (privacy overlay carries the detail)

- **GLBA Safeguards Rule, 16 CFR Part 314 as amended** (FTC, December 2021 amendments effective 2023). §314.4(h) incident-response programme. https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 .

- **GLBA Privacy Rule, 12 CFR Part 1016 (Regulation P)**. https://www.ecfr.gov/current/title-12/chapter-X/part-1016 .

- **HIPAA Privacy Rule (45 CFR Parts 160, 164 Subpart E) and Security Rule (45 CFR Parts 160, 164 Subpart C)**. Business-associate breach-notification posture. https://www.hhs.gov/hipaa/for-professionals/index.html .

- **NYDFS 23 NYCRR Part 500.17** — cybersecurity event notification (72-hour clock in many cases).

- **EU GDPR (Regulation (EU) 2016/679)** Article 33 (notification to supervisory authority within 72 hours) and Article 34 (notification to data subjects). https://eur-lex.europa.eu/eli/reg/2016/679/oj .

- **EU AI Act (Regulation (EU) 2024/1689)** Article 26 incident-reporting for high-risk AI systems [verify article number]. https://eur-lex.europa.eu/eli/reg/2024/1689/oj .

- **California Consumer Privacy Act (CCPA) as amended by CPRA, Cal. Civ. Code §1798.100 et seq.** https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CIV&title=1.81.5 [verify URL].

## Plugin-level shared references

Also consult, when present in the plugin:

- `references/source-map.md` — plugin-wide named-source map.
- `references/policy-control-library.md` — plugin-wide policy-and-control library.
- `references/review-gates.md` — named human-review gates and confidence-label definitions.

## Firm overlays

A firm using this skill in production adds firm-specific detail in `references/firm-overlay.md`. The skill consumes that file when present. Firm overlays do not modify the public anchors above.
