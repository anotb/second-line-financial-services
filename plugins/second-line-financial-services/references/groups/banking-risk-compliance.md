# Banking Risk Compliance

Sector overlay plugin for US bank holding companies, national banks, state member banks, state non-member banks, and federal and state savings associations. Primary regulators: OCC, FRB, FDIC, state banking departments, and NYDFS for NY-licensed entities.

Audience: chief risk officer, chief credit officer, chief compliance officer, head of TPRM, BSA officer, examination coordinator, and the second-line review pods that feed those roles.

## Posture

This is a strict sector-overlay plugin. It ships skills that are genuinely banking-only, shaped by the federal banking statutes, interagency guidance, and the OCC Comptroller's Handbook / FFIEC manual / FDIC RMS Manual / FRB BHC Supervision Manual lattice. Capability skills that already cover the underlying second-line function (control matrix, vendor diligence, exit plan, exam brief, risk committee pack, AI use-case intake, and so on) are not duplicated here. Banking nuance for those capability skills lives as a `references/sector-overlays.md#banking` reference inside each capability skill.

## Skills

| Skill | What it produces |
|---|---|
| `bank-fintech-partnership-review` | Bank-side partnership pack: service description and risk classification, risk-based diligence under the June 2023 Interagency Guidance, contract gaps under Bank Service Company Act §1867(c), customer-facing controls, Reg O / Reg W / Reg E / Reg DD applicability, and termination / wind-down readiness. Built for sponsor-bank deposit programs, embedded-lending partnerships, BaaS card programs, and fraud / KYC service relationships. |
| `banking-supervision-readiness` | OCC / FRB / FDIC supervisory-cycle readiness pack: CAMELS-component preparation (or BHC rated components for BHC cycles), examiner-letter response readiness, MRA / MRIA closure cross-walk, and Heightened Standards (12 CFR Part 30 Appendix D) readiness for covered banks. Built for full-scope, targeted, BSA, IT, CRA, compliance, and BHC-supervisory cycles. |
| `credit-risk-governance` | Second-line credit-governance memo: credit-policy alignment to Comptroller's Handbook expectations, underwriting framework, risk-rating discipline, concentration governance (including the 2006 CRE 100% / 300% triggers), ACL / CECL methodology oversight, Reg O and Reg W applicability, and second-line challenge of first-line lending decisions. |
| `deposit-operations-controls` | Deposit-operations control matrix: account opening and CIP (31 CFR §1020.220), beneficial-ownership collection (31 CFR §1010.230), Reg DD account disclosures and advertising, Reg E EFT and ATM operations, Reg CC funds availability, reconciliation and ledgering (including FBO-account governance for sponsor-bank programs), exception handling, access controls, and evidence retention. |

## Banking overlays into capability skills

The plugin contributes banking overlay content into capability skills where banking adds material nuance:

- `vendor-diligence` — Interagency Guidance June 2023, OCC Bulletin on Bank-Fintech Arrangements, 2024 Joint Agency Statement, §1867(c) examination flow-down, Reg O insider screen on vendor principals, Heightened Standards covered-bank evidence.
- `exit-plan` — Interagency Guidance termination expectations, FBO-account wind-down sequence, Reg DD §1030.5 / Reg E §1005.8 customer-notification, §1867(c) examination-access continuity, FDIC consultation in stressed-exit scenarios.
- `control-matrix` — Heightened Standards §III risk-governance-framework integration, FFIEC IT Information Security rows, BSA / AML control rows (CIP, CDD, BO, suspicious activity, CTR, OFAC), Call Report / UBPR evidence pointers.
- `risk-committee-pack` — Part 30 Appendix D risk-appetite, interagency-defined risk types, BHC SR 12-17 cycle integration, MRA / MRIA standing section, capital-planning content (DFAST / CCAR for applicable BHCs), LCR / NSFR liquidity content, three-lines-of-defense maturity reporting.
- `exam-brief` — banking exam types (OCC full-scope, FRB BHC, FDIC, FFIEC BSA / AML, FFIEC IT, consumer compliance, CRA), CAMELS organization, MRA / MRIA framework, examiner entry-meeting protocols, explicit pointer to `banking-supervision-readiness` for full preparation.
- `edd-escalation-pack` and `sanctions-screening-qa` — banking-specific escalation paths and OFAC examiner expectations.

## Source posture

Public anchors only. Named anchors include:

- Heightened Standards: 12 CFR Part 30 Appendix D for $50B+ covered banks (risk governance framework, board's role, risk appetite).
- OCC Comptroller's Handbook: Bank Supervision Process, Third-Party Relationships, Loan Portfolio Management, Commercial Lending, Retail Lending, Allowances for Credit Losses, Concentrations of Credit, Rating Credit Risk, Capital and Dividends, Liquidity, Earnings, Interest Rate Risk, Bank Operations, Internal Control, Deposit-Related Credit (current editions; pin edition dates).
- FFIEC manuals: IT Examination Handbook (Information Security, Retail Payment Systems, Outsourcing Technology Services booklets), BSA / AML Examination Manual (CIP, CDD, Beneficial Ownership Requirements for Legal Entity Customers).
- FDIC: Risk Management Manual of Examination Policies, FDIC FIL-29-2023, 12 CFR Part 330 pass-through deposit-insurance recordkeeping.
- FRB: BHC Supervision Manual, SR 12-17 (Consolidated Supervision Framework for Large Financial Institutions), SR 23-4, SR letters governing the MRA / MRIA framework.
- Joint OCC / FRB / FDIC: Interagency Guidance on Third-Party Relationships: Risk Management (June 6 2023); 2024 Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services; Interagency Guidance on Credit Risk Review Systems (May 2020); Interagency Guidance on Concentrations in Commercial Real Estate Lending (December 2006) and the 2015 statement; Interagency CECL implementation guidance.
- Statutes and regulations: Bank Service Company Act 12 USC §1867(c); Reg O 12 CFR Part 215; Reg W 12 CFR Part 223; Reg E 12 CFR Part 1005; Reg DD 12 CFR Part 1030; Reg CC 12 CFR Part 229; Reg P 12 CFR Part 1016; 31 CFR Part 1020 (CIP for banks); 31 CFR Part 1010 (BSA / FinCEN BO rule); USA PATRIOT Act §326.
- State: NYDFS 23 NYCRR Part 500 cybersecurity for NY-licensed entities.

The bank-fintech regulatory pipeline has moved repeatedly post-2023 (Interagency Guidance June 2023, OCC RFI July 2024, 2024 Joint Agency Statement, multiple OCC and FDIC consent orders against sponsor-bank programs). Skills must be re-validated against current public sources before each major release; minimum annual refresh.

## Components

- `skills/` — the four skills above. Each ships its own `SKILL.md`, `references/source-anchors.md`, `templates/`, and (where useful) `schemas/` and `examples.md`.
- `references/` — plugin-level shared references: banking source map, policy-control library rows, named decision forums.
- `schemas/` — banking-specific artifacts.

## Operating posture

The skills draft second-line work product for qualified review by the firm's CRO, CCO, Chief Credit Officer, Head of TPRM, Examination Coordinator, BSA Officer, General Counsel, Chief Audit Executive, or external counsel. They do not approve transactions, file regulatory reports, certify Heightened Standards compliance, sign Call Reports, close MRAs / MRIAs, onboard fintech partners, approve credit, or close issues. Every output is staged for human sign-off.
