# Source anchors — rule-to-obligation-extraction

The named, dated regulatory sources this skill anchors to for rule-text decomposition convention. Sector-specific extraction patterns live in the corresponding overlay files in `references/sector-overlays/`. Cross-cutting topical patterns live in `references/cross-cutting/`. SKILL.md cites this file by path and does not restate excerpts.

## Federal Register and CFR — citation and structure conventions

- **Federal Register publication convention**, 1 CFR Part 5 (Office of the Federal Register; Document Drafting Handbook). Cite form `__ FR __` (volume and starting page; e.g., `88 FR 51896`). Federal Register publishes the proposed rule, the final rule, and the adopting release; the operative text in the final rule (the codified amendments to the CFR) is binding; the preamble is interpretive. Effective date and compliance date are distinct: effective date is when the rule becomes part of the CFR; compliance date is when the regulated party must comply (often staged). https://www.federalregister.gov/reader-aids/office-of-the-federal-register-blog/2018/03/the-difference-between-the-federal-register-and-the-code-of-federal-regulations .

- **Code of Federal Regulations citation convention**, 1 CFR Part 21 (Office of the Federal Register). Cite form `Title CFR Part.Section` (e.g., `12 CFR 1002.107`); subsections drill down with `(a)(1)(i)`. The eCFR is the daily-current consolidation; the print CFR is annual. https://www.ecfr.gov/ . When extracting, pin to the eCFR section as published; the preamble in the corresponding Federal Register adopting release is the interpretive context.

- **Office of the Federal Register Document Drafting Handbook** (current edition) [verify edition year]. Documents the structure of a Federal Register rule document: preamble, regulatory-text amendments, transition provisions, and effective-date statements. https://www.archives.gov/federal-register/write/handbook .

## SEC adopting release and CFR structure

- **SEC adopting-release convention**. SEC final rules publish in the Federal Register as adopting releases; the release contains the preamble (Sections I-VIII typically: introduction, background, comments received, amendments adopted, economic analysis, paperwork-reduction, regulatory-flexibility, statutory authority) followed by the operative regulatory-text amendments. The operative amendments are what codifies in 17 CFR; the preamble is interpretive. https://www.sec.gov/rules/final.shtml .

- **SEC Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure final rule**, 88 FR 51896 (July 26 2023), codified at 17 CFR 229.106 (Regulation S-K Item 106), 17 CFR 232.405 (inline XBRL), 17 CFR 239.13 and 17 CFR 239.16b (Form S-K coverage), 17 CFR 240.13a-11 and 17 CFR 240.15d-11 (Form 8-K), and 17 CFR 249.308 (Form 8-K Item 1.05). Effective date September 5 2023; compliance dates staged: incident-disclosure compliance December 18 2023 for non-smaller reporting companies; June 15 2024 for smaller reporting companies; risk-management-and-strategy compliance with annual reports for fiscal years ending on or after December 15 2023. https://www.sec.gov/files/rules/final/2023/33-11216.pdf .

- **SEC Investment Adviser Marketing Rule**, Rule 206(4)-1 under the Investment Advisers Act of 1940, 17 CFR 275.206(4)-1; adopting release 86 FR 13024 (March 5 2021). Compliance date November 4 2022. The rule consolidates the prior advertising rule (former 206(4)-1) and the cash-solicitation rule (former 206(4)-3); operative provisions are at §§275.206(4)-1(a) through (e). https://www.sec.gov/rules/final/2020/ia-5653.pdf .

- **SEC Reg S-P amendments**, 89 FR 47688 (June 3 2024) [verify final FR cite], codified amendments to 17 CFR Part 248. The amendments add an incident-response programme requirement and a customer-notice requirement. Compliance dates staged by registrant size. https://www.sec.gov/rules/final.shtml .

## CFPB rule structure

- **CFPB final-rule convention**. CFPB final rules publish in the Federal Register and codify in 12 CFR Chapter X (Parts 1001 through 1099). The Bureau's adopting release follows the same preamble-plus-operative-text shape as other federal agencies; the operative text in the corresponding 12 CFR section is binding. https://www.consumerfinance.gov/rules-policy/final-rules/ .

- **CFPB Section 1071 small-business-lending data rule**, 88 FR 35150 (May 31 2023), codified at 12 CFR 1002.101 through 12 CFR 1002.114 (Subpart B of Regulation B). The rule has been the subject of post-publication litigation that affected the originally published tier-based compliance schedule; the extraction-time row reflects the dates in effect at extraction (do not transcribe a stale schedule into the register without dating it as-of). The originally published schedule was Tier 1 (2,500+ covered originations) October 1 2024; Tier 2 (500-2,499) April 1 2025; Tier 3 (100-499) January 1 2026 — these are the published dates, not necessarily the operative dates at extraction time. https://www.consumerfinance.gov/rules-policy/final-rules/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b/ .

- **CFPB circulars** (e.g., Circular 2022-03 on adverse-action notice requirements when AI is used; numbering by year and sequence). Circulars are the Bureau's interpretive position on existing law; they are not new rules and do not codify in the CFR, but they are the Bureau's stated supervisory and enforcement basis. Pin extractions to the circular's section structure. https://www.consumerfinance.gov/compliance/circulars/ .

- **CFPB Section 1033 (open banking) final rule**, 89 FR 90838 (November 18 2024) [verify final FR cite], codified at 12 CFR Part 1033. Status: subject to litigation post-publication; portions have been stayed and the tier-based compliance-date schedule has shifted. The extraction must reflect the stay-and-compliance-date posture in effect at extraction time rather than the originally published schedule. https://www.consumerfinance.gov/rules-policy/final-rules/required-rulemaking-on-personal-financial-data-rights/ .

## Federal banking supervisory-instrument format

- **OCC Bulletin format**. OCC Bulletins are issued by the Office of the Comptroller of the Currency to provide guidance to OCC-supervised institutions; they are interpretive and supervisory rather than rules in the CFR sense. The bulletin carries a year-and-sequence number (`OCC Bulletin 2013-29`), a title, an effective date, and an enumerated body. Pin to the section number inside the bulletin (e.g., `OCC Bulletin 2013-29 §III.A`). https://www.occ.gov/news-issuances/bulletins/index-bulletins.html .

- **OCC Bulletin 2013-29: Third-Party Relationships: Risk Management Guidance** (October 30 2013), rescinded by **OCC Bulletin 2023-17** rescission-and-replacement effective with the **June 6 2023 Interagency Guidance on Third-Party Relationships: Risk Management** (88 FR 37920, June 9 2023). The interagency guidance was issued jointly by FRB, FDIC, and OCC; it replaces the prior agency-specific guidance and is the operative supervisory expectation for third-party-risk obligations. https://www.federalregister.gov/documents/2023/06/09/2023-12340/interagency-guidance-on-third-party-relationships-risk-management .

- **FRB SR Letter format**. FRB Supervision and Regulation Letters are issued by the Board of Governors of the Federal Reserve System to provide guidance to FRB-supervised institutions; they are interpretive and supervisory. Cite form `SR YY-NN` (year and sequence; e.g., `SR 11-7`). Pin to the section inside the letter (e.g., `SR 11-7 §IV.A`). https://www.federalreserve.gov/supervisionreg/srletters/srletters.htm .

- **Joint Interagency Revised Guidance on Model Risk Management** (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026). One document issued through three agency channels with the same date, text, and signatories; supersedes and replaces SR 11-7 / OCC Bulletin 2011-12 (April 4, 2011) and SR 21-8 (Interagency Statement on Model Risk Management for BSA/AML Compliance, April 9, 2021). Pin to the section structure of the joint guidance (Section II for definitions and scope, including the threshold relevance for banking organizations over $30 billion in total assets; sections covering model identification and inventory, validation, ongoing monitoring, and governance). The guidance is non-binding (does not set forth enforceable standards or prescriptive requirements per Section I, footnote 1). Generative AI and agentic AI models are explicitly out of scope (footnote 3 of the joint guidance text); rows extracting GenAI or agentic-AI obligations route to NIST AI RMF / NIST AI 600-1 / EU AI Act / ISO/IEC 42001 instead. The bulletin contains zero references to NIST AI RMF or NIST AI 600-1. https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-13a.pdf ; https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm ; https://www.fdic.gov/news/financial-institution-letters/2026/agencies-revise-interagency-model-risk-management-guidance .

- **Superseded — SR 11-7 / OCC Bulletin 2011-12 (April 4, 2011) and SR 21-8 (April 9, 2021).** Retained as citation anchors only because pre-April-17-2026 firm policies, validation reports, and examination evidence reference these documents by name. Cite as superseded when extracting against historical evidence. https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm ; https://www.federalreserve.gov/supervisionreg/srletters/SR2108.htm .

- **FDIC FIL format**. FDIC Financial Institution Letters are issued by the FDIC to provide guidance to FDIC-supervised institutions; they are interpretive and supervisory. Cite form `FIL-NN-YYYY` (sequence and year). Pin to the section inside the FIL. https://www.fdic.gov/news/financial-institution-letters/ .

- **NCUA Letter to Credit Unions format**. NCUA Letters to Credit Unions provide guidance to federally insured credit unions; they are interpretive. Cite form `LtCU NN-YY`. Pin to the section inside the letter. https://ncua.gov/regulation-supervision/letters-credit-unions-other-guidance .

- **FFIEC inter-agency statements**. The FFIEC issues inter-agency statements signed by some or all of OCC, FRB, FDIC, NCUA, and CFPB; the statement format mirrors the SR letter and OCC bulletin format. https://www.ffiec.gov/press/press_releases.htm .

- **The 36-hour bank notification rule**: 12 CFR Part 53 (OCC); 12 CFR Part 225 Subpart N (FRB Regulation Y); 12 CFR Part 304 Subpart C (FDIC). 86 FR 66424 (November 23 2021), compliance date May 1 2022. Each agency adopted a parallel rule; the obligation triggers on a "notification incident" as defined; notification to the primary federal regulator is required as soon as possible and no later than 36 hours after the banking organization determines a notification incident has occurred. https://www.federalregister.gov/documents/2021/11/23/2021-25510/computer-security-incident-notification-requirements-for-banking-organizations-and-their-bank .

## NYDFS and state instrument format

- **NYDFS 23 NYCRR Part 500: Cybersecurity Requirements for Financial Services Companies** (effective March 1 2017; second amendment 7 NYCRR final rule effective November 1 2023, with staged transitional periods through May 1 2025 and November 1 2025). Pin to the section inside Part 500: §500.2 Cybersecurity Program; §500.3 Cybersecurity Policy; §500.4 Chief Information Security Officer; §500.5 Penetration Testing and Vulnerability Assessments; §500.7 Access Privileges; §500.11 Third Party Service Provider Security Policy; §500.17 Notices to Superintendent. https://www.dfs.ny.gov/industry_guidance/cybersecurity .

- **NYDFS Industry Letter format**. NYDFS issues Industry Letters as interpretive guidance to DFS-licensed entities; cite form by date and topic. Pin to the section inside the letter. https://www.dfs.ny.gov/industry_guidance .

- **State adoption of NAIC model laws**. State insurance departments adopt NAIC model laws and model regulations through state legislative or regulatory process. The NAIC model number is a starting reference; the state-adopted version is the binding text in that state, and amendments at adoption are common. The extraction must distinguish between the model and the state-adopted version when the rule under extraction is a state insurance code section. https://content.naic.org/cipr-topics/topics/model-laws .

## NAIC model laws

- **NAIC Insurance Data Security Model Law (Model 668)** (adopted 2017; amended periodically). The model requires licensees to develop a written information-security programme, conduct risk assessment, oversee third-party service providers, investigate cybersecurity events, and notify the Commissioner. State-by-state adoption status is tracked at the NAIC. Pin extractions to the model section number (e.g., `Model 668 §4 Information Security Program`). https://content.naic.org/cipr-topics/insurance-data-security-model-law .

- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model 505)** (adopted 2012; amended). Operative sections: §3 Definitions; §4 Risk Management Framework; §5 ORSA Requirements; §6 ORSA Summary Report. https://content.naic.org/sites/default/files/MO505.pdf .

- **NAIC Standard Valuation Law (Model 820); Annual Financial Reporting Model Regulation (Model 205); Corporate Governance Annual Disclosure Model Act (Model 305)**. Pin extractions to the model section number (each model is structured by numbered sections). https://content.naic.org/cipr-topics/topics/model-laws .

## EU regulation, directive, and technical-standards structure

- **EU regulation structure**. Regulations adopted under the Treaty on the Functioning of the European Union have direct effect in member states. Structure: title, recitals (numbered, interpretive), articles (numbered, binding operative text), annexes. Cite form `Regulation (EU) YYYY/NNNN, OJ L NNN/N` (Official Journal cite). Pin obligations to the article and paragraph (e.g., `Article 17(1)(a)`); recitals carry interpretive weight but are not binding obligations. https://eur-lex.europa.eu/ .

- **Digital Operational Resilience Act (DORA): Regulation (EU) 2022/2554** (December 14 2022; entry into force January 16 2023; application date January 17 2025), OJ L 333/1. Operative articles: Article 5 governance; Article 6 ICT risk management framework; Article 17 ICT-related incident management; Article 19 reporting of major ICT-related incidents to competent authorities; Article 28 management of ICT third-party risk; Article 31 designation of critical ICT third-party service providers. https://eur-lex.europa.eu/eli/reg/2022/2554/oj .

- **EU Markets in Crypto-Assets Regulation (MiCA): Regulation (EU) 2023/1114** (May 31 2023), OJ L 150/40. Pin obligations to the article (e.g., Article 16 capital requirements; Article 60 authorisation requirements; Article 68 governance arrangements). https://eur-lex.europa.eu/eli/reg/2023/1114/oj .

- **EU Artificial Intelligence Act: Regulation (EU) 2024/1689** (June 13 2024), OJ L 2024/1689 [verify exact OJ cite]. Operative-article structure mirrors other EU regulations; high-risk-system classification in Annex III; obligations on providers, deployers, importers, and distributors. Application dates staged by topic. https://eur-lex.europa.eu/eli/reg/2024/1689/oj .

- **EU directive structure**. Directives adopted under the TFEU bind member states as to the result; member-state implementation legislation is the operative text in each state. Cite form `Directive (EU) YYYY/NNNN, OJ L NNN/N`. Pin obligations to the article in the directive plus the implementing-legislation section in the relevant member state.

- **EU regulatory and implementing technical standards (RTS / ITS)**. RTS and ITS are issued by the European Supervisory Authorities (EBA, ESMA, EIOPA) and adopted by the Commission as Commission Delegated Regulations or Commission Implementing Regulations. Cite form `Commission Delegated Regulation (EU) YYYY/NNNN`. Pin obligations to the article in the delegated regulation. https://www.esma.europa.eu/ .

## FCA Handbook structure

- **FCA Handbook block structure**. The FCA Handbook is organised by sourcebook (e.g., SYSC for Senior Management Arrangements, Systems and Controls; COBS for Conduct of Business; SUP for Supervision; DEPP for Decision Procedure and Penalties). Each sourcebook has chapters; each paragraph carries a label from the FCA's status taxonomy: `R` for binding rule, `G` for guidance, `D` for direction, `E` for evidential provision, `EU` for retained EU-derived material. Cite form `SOURCEBOOK CHAPTER.SECTION.PARA STATUS` (e.g., `SYSC 6.1.1R`). Pin obligations to the paragraph and respect the status: `R` paragraphs are obligations; `G` paragraphs are interpretive only. https://www.handbook.fca.org.uk/ .

- **PRA Rulebook structure**. The PRA Rulebook is organised by category and chapter; rules are binding on PRA-authorised firms. Pin obligations to the chapter and rule number. https://www.prarulebook.co.uk/ .

## FinCEN advisory and rule format

- **FinCEN advisory format**. FinCEN advisories are issued under FinCEN's authority and provide red-flag and typology guidance for SAR-filing convention; they are interpretive. Cite form `FIN-YYYY-A-NNN`. Pin to the section inside the advisory. https://www.fincen.gov/resources/advisories .

- **FinCEN Beneficial Ownership Reporting Rule**, 31 CFR 1010.380 (88 FR 17557, March 24 2023 [verify]), implementing the Corporate Transparency Act. Operative obligations: 31 CFR 1010.380(a) reporting; 31 CFR 1010.380(b) reporting-company definition; 31 CFR 1010.380(c) beneficial-owner definition; 31 CFR 1010.380(d) company-applicant definition; 31 CFR 1010.380(e) updates and corrections. https://www.fincen.gov/boi .

- **FinCEN Customer Due Diligence Rule**, 31 CFR 1010.230 (81 FR 29397, May 11 2016). https://www.fincen.gov/resources/statutes-regulations/cdd-final-rule .

## Consent orders as obligation sources

- **Public consent-order convention**. Federal regulators (OCC, FRB, FDIC, CFPB, NCUA, SEC, FINRA, NYDFS) publish finalised consent orders that name a defendant institution and impose specific remediation obligations under articles. The articles operate as obligations the named defendant must satisfy; firms not named in the order may treat the articles as obligations the firm should also satisfy when the firm has a similar exposure. Use only published, finalised consent orders for extraction. Cite form is the order's docket number plus the issuing agency (e.g., `OCC Consent Order #AA-EC-YYYY-NN`). Do not use named institutions in narrative beyond the public-defendant reference. https://apps.occ.gov/EnforcementActions/ ; https://www.federalreserve.gov/supervisionreg/enforcement.htm ; https://www.fdic.gov/regulations/laws/enforcement-decisions/ ; https://www.consumerfinance.gov/enforcement/actions/ ; https://www.sec.gov/enforce/litigation-releases ; https://www.finra.org/rules-guidance/oversight-enforcement/finra-disciplinary-actions ; https://www.dfs.ny.gov/reports_and_publications/enforcement_actions .

## Extraction-pattern reference (atomic-obligation shape)

- **ISO/IEC 42001:2023 Annex A control structure** (paraphrased pattern, not authority). The Annex A control table in ISO/IEC 42001 is a useful model for atomic-obligation shape: one control statement per row, with implementation guidance and references separated. Use as a model only; the binding text is whatever the rule under extraction is, not ISO. https://www.iso.org/standard/81230.html .

## Plugin-level shared references

Also consult, when present in the plugin:

- `references/source-map.md` — plugin-wide named-source map.
- `references/policy-control-library.md` — plugin-wide policy-and-control library.
- `references/review-gates.md` — named human-review gates and confidence-label definitions.

## Firm overlays

A firm using this skill in production may install firm-specific extraction conventions (preferred citation form, internal regulatory-instrument taxonomy, internal review machinery) in `references/firm-overlay.md`. The skill consumes that file when present. Firm overlays do not modify the public anchors above and do not introduce firm-specific control mappings into the register; that work belongs in `risk-compliance-core/obligation-mapping`.
