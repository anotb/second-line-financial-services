# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay: obligation-mapping

Loaded when the scope includes `banking` in `sector_overlay_set`. Adds banking-specific source labels and obligation patterns the practitioner expects to find when the register scopes a banking process. Does not change the row spine.

#### Sources the register may cite

##### Heightened standards and large-bank governance

- 12 CFR Part 30 Appendix D — OCC Heightened Standards for Large Insured National Banks. Standards I-V on the risk-governance framework, three-lines-of-defense, independent risk management, front-line-unit responsibilities. Threshold: covered banks at the OCC asset-size population. [verify the exact appendix-and-standard labels against the current Code of Federal Regulations text.]
  - Use for: enterprise-risk-governance obligations, risk-appetite-statement obligations, board-risk-committee oversight obligations at large national banks.
  - Link: https://www.ecfr.gov/current/title-12/chapter-I/part-30/appendix-Appendix%20D%20to%20Part%2030

##### Insider lending and affiliate transactions

- Regulation O — 12 CFR Part 215 (Loans to Executive Officers, Directors, and Principal Shareholders of Member Banks). §215.4 (general prohibitions and lending limits), §215.5 (executive-officer loans), §215.8 (records), §215.11 (disclosure of loans by member banks).
  - Use for: insider-lending obligation rows where the register scopes commercial-lending or executive-officer credit processes.
  - Link: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-215

- Regulation W — 12 CFR Part 223 (Transactions Between Member Banks and Their Affiliates). §223.11 (10% limit), §223.12 (20% limit), §223.13 (collateral requirements), §223.16 (low-quality assets). [verify subsection labels against current Part 223.]
  - Use for: affiliate-transaction obligations when the register scopes intercompany funding, asset transfers, or services.
  - Link: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-223

##### FRB SR letters as obligation source

- SR 16-11 — Supervisory Guidance for Assessing Risk Management at Supervised Institutions. [verify section labels.]
  - Use for: risk-management governance obligations at FRB-supervised institutions; the SR letter pattern is to extract the obligation by SR-letter number and section, then cross-reference to the underlying rule.
  - Link: https://www.federalreserve.gov/supervisionreg/srletters/sr1611.htm

- SR 20-15 / SR 13-19 — supervisory guidance on operational resilience and outsourcing. [verify section labels and current applicability.]
  - Use for: operational-resilience and outsourcing obligation rows when the register scopes a banking process touching critical operations.

##### Bank-supervised information security and privacy

- Interagency Guidelines Establishing Information Security Standards (12 CFR Part 30 Appendix B for OCC; Part 208 Appendix D for FRB; Part 364 Appendix B for FDIC). §III (information security program elements), §III.C (assess risk), §III.D (manage and control risk).
  - Use for: bank-side information-security-program obligations when the register scopes information-security or vendor-information-security work; load alongside the cyber cross-cutting overlay where the engagement also includes NYDFS Part 500 or FFIEC IT.
  - Link: https://www.ecfr.gov/current/title-12/chapter-I/part-30/appendix-Appendix%20B%20to%20Part%2030

- 12 CFR Part 332 (FDIC Privacy of Consumer Financial Information) and 12 CFR Part 1016 (CFPB Reg P). §1016.4 (initial notice), §1016.10 (disclosure limits and exceptions). [verify FDIC Part 332 numbering against current Code.]
  - Use for: GLBA Privacy Rule obligation rows when the register scopes consumer-deposit or lending products at a bank; load alongside the privacy cross-cutting overlay.
  - Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1016

#### Obligation patterns the practitioner expects to find

- **Three-lines-of-defense obligation rows.** OCC Heightened Standards split into front-line, second-line independent risk, and third-line audit obligations; the register surfaces them as separate rows even when the underlying rule reads as one section, because the owner and the evidence are different on each line.
- **Capital and liquidity reporting obligations.** Reg YY enhanced prudential standards for $100B+ holding companies, FR Y-9C and FR Y-14 reporting cycles, LCR reporting under 12 CFR Part 249. The register treats each report as its own row when the scope includes regulatory reporting.
- **CRA and fair-lending obligation pair-up.** When the register scopes a lending process, expect Reg B (12 CFR Part 1002) ECOA obligations alongside CRA performance-evaluation obligations under 12 CFR Part 25 (OCC) / Part 228 (FRB) / Part 345 (FDIC). Load the conduct cross-cutting overlay.
- **BSA/AML obligations.** Use the FFIEC BSA/AML Examination Manual section structure; the bank-side rows extract from 31 CFR Part 1020 (CDD for banks), 31 CFR 1010.230 (BO), 31 CFR 1020.220 (CIP), 31 CFR 1020.320 (SAR).

#### What does not belong here

- Sponsor-bank-fintech allocation language. That belongs on the contractual source row in the register itself, anchored on the sponsor agreement, with `payments-fintech` overlay loaded if the fintech side is in scope.
- Insurance-side obligations even where a bank holding company also owns an insurance subsidiary. Run a separate register for the insurance subsidiary with `insurance` overlay.
- Internal firm policy and taxonomy. That goes in `references/firm-overlay.md` regardless of sector.

## capital-markets

### Capital markets and asset management sector overlay: obligation-mapping

Loaded when the scope includes `capital-markets` in `sector_overlay_set`. Adds capital-markets-specific source labels and obligation patterns the practitioner expects to find when the register scopes a broker-dealer, investment adviser, or registered fund process. Does not change the row spine.

The two regulators are SEC and FINRA (with the CFTC and NFA layered in for futures and swaps). Investment Advisers Act and Investment Company Act govern the buy-side; Securities Exchange Act and FINRA rules govern the sell-side; the Securities Act is mostly issuer-side. The register names the regulatory regime that imposes each row.

#### Sources the register may cite

##### Investment adviser obligations

- Investment Advisers Act of 1940 and rules thereunder (17 CFR Part 275).
  - Rule 206(4)-7 (compliance program rule) — the foundational compliance-program obligation. [verify subsection labels.]
  - Rule 206(4)-1 (marketing rule, as amended 2020). §275.206(4)-1(a) through (e).
  - Rule 204A-1 (code of ethics). §275.204A-1.
  - Rule 204-2 (recordkeeping). §275.204-2.
  - Rule 206(4)-2 (custody). §275.206(4)-2.
  - Use for: adviser-side obligations across compliance program, marketing, code of ethics, recordkeeping, custody. SEC Division of Examinations priorities are scoping input rather than rule-text source.
  - Link: https://www.ecfr.gov/current/title-17/chapter-II/part-275

##### Broker-dealer obligations

- Securities Exchange Act of 1934 and rules thereunder (17 CFR Part 240).
  - Rule 15c3-1 (net capital). §240.15c3-1.
  - Rule 15c3-3 (customer protection). §240.15c3-3.
  - Rule 17a-3 and Rule 17a-4 (recordkeeping). §240.17a-3 and §240.17a-4 (note 2022 amendments to electronic recordkeeping).
  - Rule 15c3-5 (market access). §240.15c3-5.
  - Reg BI (Best Interest, 17 CFR §240.15l-1).
  - Use for: broker-dealer obligations across capital, customer protection, recordkeeping, market access, retail-investor conduct.
  - Link: https://www.sec.gov/divisions/marketreg/

- FINRA rule book.
  - FINRA Rule 3110 (supervision).
  - FINRA Rule 4511 (general books-and-records retention).
  - FINRA Rule 4530 (reporting requirements, including disciplinary and customer-complaint reporting).
  - FINRA Rule 2010 (standards of commercial honor and just and equitable principles of trade).
  - Use for: FINRA-imposed supervision, recordkeeping, reporting, and conduct obligations on member firms.
  - Link: https://www.finra.org/rules-guidance

##### Registered investment company obligations

- Investment Company Act of 1940 and rules thereunder (17 CFR Part 270).
  - Rule 38a-1 (compliance program rule). §270.38a-1.
  - Rule 17a-7, 17a-8, 17a-9 (affiliated transactions and cross-trades).
  - Rule 18f-4 (derivatives and limits).
  - Rule 22c-2 (redemption fees, recordkeeping for trading activity).
  - Use for: fund-board, fund-CCO, and affiliated-transaction obligations on registered open-end and closed-end funds.
  - Link: https://www.ecfr.gov/current/title-17/chapter-II/part-270

##### Securities-issuer obligations (when the engagement covers issuer reporting)

- Securities Exchange Act of 1934 §§13, 15(d) and Reg S-K. Item 106 (cybersecurity) for cyber-related disclosures, Item 402 for executive compensation, Form 8-K Item 1.05 for material cybersecurity incident disclosure.
  - Use for: issuer-disclosure obligations when the register scopes issuer-reporting processes.

##### CFTC and NFA hooks

- Commodity Exchange Act and CFTC regulations (17 CFR Chapter I).
  - 17 CFR §23.600 (risk management program for swap dealers).
  - 17 CFR §1.31 (recordkeeping for futures commission merchants).
  - Use for: swap-dealer and FCM obligations when the register scopes derivatives activity.

- NFA Compliance Rules (NFA member firms).
  - Use for: NFA-side obligations on commodity pool operators, commodity trading advisors, and FCMs.

#### Obligation patterns the practitioner expects to find

- **CCO-anchored compliance-program obligations.** Both Rule 206(4)-7 (advisers) and Rule 38a-1 (funds) impose compliance-program obligations and a CCO-attestation cycle. The register surfaces the program elements (annual review, written policies, designated CCO) as discrete rows.
- **Recordkeeping obligations with retention windows.** SEC Rule 17a-4, IAA Rule 204-2, FINRA Rule 4511. The register's evidence-required column reflects the retention window that the rule names; firm policy summaries are not the source.
- **Board-anchored fund obligations.** Fund-board approval obligations for advisory contracts (§15(c)), distribution arrangements (Rule 12b-1), valuation (Rule 2a-5), and affiliated transactions (Rule 17a-7). The owner column on these rows is the fund board, not the adviser CCO.
- **Reg BI and Form CRS for retail-facing brokers and dual-registrants.** The register splits the Reg BI care, conflicts, and disclosure obligations from the Form CRS delivery obligations because the test posture differs.
- **SEC Division of Examinations priorities as scoping input, not source.** When a SEC EXAMS priority letter highlights a topic, the register may note it as scoping rationale in `applicability_notes`, but the obligations still extract from the underlying rule.

#### What does not belong here

- Bank-side obligations even where the broker-dealer is part of a bank-holding company. Run a separate register with `banking` overlay if relevant.
- Insurance-side obligations on a variable-annuity sponsor's insurance company. Run a separate register with `insurance` overlay; the SEC-side obligations on the registered separate account stay here.
- Internal firm policy and taxonomy. That goes in `references/firm-overlay.md`.

## insurance

### Insurance sector overlay: obligation-mapping

Loaded when the scope includes `insurance` in `sector_overlay_set`. Adds insurance-specific source labels and obligation patterns the practitioner expects to find when the register scopes an insurance process. Does not change the row spine.

The federal-state interplay is the dominant feature: most insurance obligations live in state insurance code, with NAIC model laws as the starting point and state adoptions varying. The register must name the state of domicile and any host states with material business when applicability turns on state-specific rules.

#### Sources the register may cite

##### NAIC model laws as starting point

NAIC models do not bind directly; state-by-state adoption does. The register cites the NAIC model and the state adoption together where the state has adopted, and notes the state has not adopted where it has not.

- NAIC Model Audit Rule (Model #205 — Annual Financial Reporting Model Regulation). [verify section labels against current NAIC version.]
  - Use for: financial-reporting and internal-control-over-financial-reporting (ICFR-equivalent) obligations on insurers. Section references vary by state adoption.
  - Link: https://content.naic.org/

- NAIC Risk Management and Own Risk and Solvency Assessment (ORSA) Model Act (Model #505).
  - Use for: ORSA filing obligations, risk-management framework obligations, group-level risk obligations on insurance holding companies.

- NAIC Insurance Holding Company System Regulatory Act (Model #440) and the related Form B / Form F obligations.
  - Use for: holding-company-level reporting and intercompany-transaction obligations.

- NAIC Insurance Data Security Model Law (Model #668).
  - Use for: cybersecurity-program obligations in states that have adopted; cross-load with the cyber overlay.

- NAIC AI Bulletin (2023) and emerging NAIC AI model regulation work.
  - Use for: AI-system obligations on insurers (use-case inventories, governance, third-party AI model expectations); cross-load with AI overlays from `ai-governance-model-risk` references when the engagement also touches AI.

##### ORSA and group capital

- ORSA Guidance Manual (NAIC) — the operational guidance behind Model #505. [verify section labels and current edition.]
  - Use for: ORSA Summary Report content obligations (sections 1, 2, 3 of the Manual).
  - Link: https://content.naic.org/cipr-topics/own-risk-and-solvency-assessment-orsa

##### State-specific anchors (sample; the register names the actual state)

- New York Insurance Law and 11 NYCRR (DFS regulations). NYDFS Insurance Regulation 187 (suitability and best interests in life insurance and annuity transactions) §224.4, §224.6. [verify subsection labels.]
  - Use for: market-conduct obligations on life and annuity products sold in New York.
  - Link: https://www.dfs.ny.gov/

- California Insurance Code §790 et seq. (Unfair Insurance Practices Act).
  - Use for: market-conduct obligations on California-domiciled or California-licensed insurers.

- Texas Insurance Code Chapter 4001 et seq. (Licensing of Insurance Agents).
  - Use for: producer-licensing obligations.

##### Federal hooks

- Gramm-Leach-Bliley Act privacy (15 U.S.C. §6801 et seq.) as implemented through state insurance privacy regulations modeled on NAIC Model #672 (Privacy of Consumer Financial and Health Information).
  - Use for: privacy obligations on insurers; cross-load with the privacy cross-cutting overlay.

- Federal Insurance Office Act provisions and federal preemption questions where federal action interacts with state insurance authority.
  - Use sparingly; FIO does not directly impose obligations on insurers in most contexts.

- Health Insurance Portability and Accountability Act for health insurers (45 CFR Parts 160, 162, 164).
  - Use for: PHI-handling obligations on health insurers.

#### Obligation patterns the practitioner expects to find

- **State-by-state extraction with a domicile anchor.** For multi-state insurers, the register extracts obligations at the state level where the rule is state-specific, with the domicile state as primary and material host states as secondary. Identical or near-identical obligations across states roll up only when the substance is genuinely identical and the difference is form.
- **Holding-company and operating-company split.** Holding-company obligations under Model #440 and ORSA under Model #505 extract on the holding-company tier; operating-company obligations extract at the licensed-entity tier. The register names the entity each row applies to.
- **Producer (agent) and broker obligations.** Producer-licensing, suitability, and supervision obligations extract as their own cluster when the register scopes distribution.
- **Reinsurance and ceded-business obligations.** State reinsurance credit rules and NAIC Credit for Reinsurance Model Regulation (#786) extract when the register scopes reinsurance, including the ceded-business reporting obligations.
- **NAIC accreditation and model adoption status.** Where the register cites a NAIC model that the relevant state has adopted with modifications, the row notes the adoption form and any deviation; where the state has not adopted, the row reads `not-applicable` with the rationale.

#### What does not belong here

- Bank-side obligations even where a financial-holding company owns both a bank and an insurer. Run a separate register on the bank with `banking` overlay.
- Federal securities-law obligations on the insurer's investment management or affiliated broker-dealer. Run a separate register or extend with the `capital-markets` overlay if the same engagement covers it.
- Internal firm policy and taxonomy. That goes in `references/firm-overlay.md`.

## payments-fintech

### Payments and fintech sector overlay: obligation-mapping

Loaded when the scope includes `payments-fintech` in `sector_overlay_set`. Adds payments- and fintech-specific source labels and obligation patterns the practitioner expects to find when the register scopes a consumer-payments product, a money-transmission process, a bank-fintech sponsor arrangement, or a BaaS program. Does not change the row spine.

The register here often runs across two parties: a sponsor bank with the regulatory obligation and a fintech with the operational obligation under contract. The register treats those as separate rows, anchored on the rule for the bank side and on the sponsor agreement for the fintech side.

#### Sources the register may cite

##### Consumer-payments rules

- Regulation E — 12 CFR Part 1005 (Electronic Fund Transfers Act implementation).
  - §1005.6 (consumer liability for unauthorized transfers).
  - §1005.7 (initial disclosures).
  - §1005.8 (change-in-terms notices).
  - §1005.9 (receipts and periodic statements).
  - §1005.11 (procedures for resolving errors); §1005.11(c) (10-day provisional credit window).
  - §1005.18 (prepaid accounts).
  - Use for: EFT obligations on the bank holding the deposit; allocate operational components to the fintech via the sponsor agreement.
  - Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1005

- Regulation Z — 12 CFR Part 1026 (Truth in Lending Act implementation).
  - §1026.6 (account opening disclosures for open-end credit).
  - §1026.7 (periodic statements for open-end credit).
  - §1026.13 (billing-error resolution).
  - §1026.40 (HELOCs); subpart G (credit cards).
  - Use for: TILA obligations on credit products, including BNPL where structured as open-end or closed-end credit under the rule. The CFPB BNPL interpretive rule (May 2024) was **nullified by Pub. L. 119-11 (May 9, 2025); historical only**; Reg Z applicability to BNPL is now an open question on the regulatory text.
  - Link: https://www.ecfr.gov/current/title-12/chapter-X/part-1026

- Regulation DD — 12 CFR Part 1030 (Truth in Savings Act implementation).
  - §1030.4 (account disclosures).
  - §1030.5 (subsequent disclosures).
  - Use for: deposit-account disclosure obligations on consumer-deposit products.

##### Bank-fintech and BaaS expectations

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC / FRB / FDIC, June 6, 2023). §III.A through §III.E lifecycle phases.
  - Use for: TPRM obligations on the bank when the bank is the sponsor; the fintech-side allocation flows through the sponsor agreement.
  - Link: https://www.federalreserve.gov/supervisionreg/srletters/SR2304.htm

- Joint Statement on Bank-Fintech Arrangements (FDIC / OCC / FRB, July 2024) and the related interagency RFI on bank-fintech arrangements. [verify exact title and citation; the joint statement names risk areas including end-user ledgering and FBO-account controls.]
  - Use for: BaaS-specific obligation rows that overlap with TPRM but go beyond standard third-party expectations: end-user ledgering integrity, FBO account governance, BaaS-program criticality classification.
  - Link: https://www.fdic.gov/news/financial-institution-letters/

##### Open banking

- CFPB Section 1033 (Personal Financial Data Rights) Final Rule, 12 CFR 1033 [verify subpart and section numbers against the published Final Rule]. **§1033 compliance dates stayed as of October 29, 2025; CFPB-initiated reconsideration with ANPR** — verify current docket status before treating phased compliance dates as firm.
  - Use for: data-provider obligations to make covered data available to consumer-authorized third parties; cross-load with privacy overlay.
  - Link: https://www.consumerfinance.gov/rules-policy/final-rules/

##### Money transmission

- State money-transmitter licenses and the NMLS-coordinated obligations under each state's money-transmitter act.
  - Use for: money-transmitter obligations when the fintech operates without a sponsor bank or operates licensed activities directly. The register names the licensing states explicitly.

- Bank Secrecy Act money-services-business obligations (31 CFR Part 1022). §1022.210 (AML program), §1022.310 (CTRs), §1022.320 (SARs), §1022.380 (registration as MSB).
  - Use for: MSB-side BSA obligations.
  - Link: https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022

##### Card-network and payment-rail obligations

- Card-network rules (Visa, Mastercard, Discover, Amex). Operating regulations and chargeback rules. Not regulator-issued, but contractually binding and treated as a contractual source row in the register.
- NACHA Operating Rules (ACH). Contractually binding on participating financial institutions.
- The Clearing House Real-Time Payments rules; FedNow operating circular (FRB Operating Circular 8 [verify circular number and current edition]).

#### Obligation patterns the practitioner expects to find

- **Bank-side and fintech-side row pair-up.** Reg E error-resolution obligations land on the bank as the financial institution; the sponsor agreement allocates the operational handoff to the fintech (intake, investigation, communication). Both rows extract.
- **The 10-day provisional-credit obligation under §1005.11(c).** Empirically grounded number; the register names it explicitly when consumer-payment processes are in scope.
- **BaaS criticality classification rows.** When the bank's TPRM treats the BaaS program as a critical third-party relationship, expected obligation rows include continuous monitoring, exit planning, and regulator-notification obligations specific to the BaaS arrangement.
- **End-user ledgering and FBO account integrity.** The 2024 joint statement and subsequent supervisory commentary treat these as distinct obligation areas; the register surfaces them rather than collapsing into "vendor oversight."
- **State money-transmitter license obligations.** Each licensing state imposes net-worth, surety-bond, and reporting obligations; the register lists these as distinct rows or groups them with explicit state-by-state notes in `applicability_notes`.

#### What does not belong here

- Capital-markets-side obligations on a fintech that operates a registered broker-dealer or investment adviser. Run with `capital-markets` overlay; the payments-fintech overlay covers the consumer-payments side.
- Bank-side obligations that do not interact with the fintech relationship (general capital, deposit insurance assessments, CRA). Run with `banking` overlay.
- Internal firm policy and taxonomy. That goes in `references/firm-overlay.md`.
