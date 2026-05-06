# Banking sector overlay snippets — input to capability spec sheets

Plugin: `banking-risk-compliance`
Status: phase 1 input. Each entry is the outline of a `references/sector-overlays/banking.md` reference document that lives inside the named capability skill. Capability-plugin leads pick these up when they spec their skills; phase 2 capability authors write the full reference.

These snippets exist because the strict sector-overlay rule keeps banking-only nuance out of the sector plugin when the skill itself already lives as a capability skill. The capability skill stays generic; the banking flavor lives next to it as a reference.

## Convention

For each entry:
- **Capability skill** — `<plugin>/skills/<skill>/references/sector-overlays/banking.md`
- **What the banking overlay should cover** — bullets of the banking-specific anchors, lens shifts, and gating considerations that a senior banking second-line practitioner would expect to see.

## third-party-operational-resilience / vendor-diligence

Capability skill: `third-party-operational-resilience/skills/vendor-diligence`
Path: `vendor-diligence/references/sector-overlays/banking.md`

What the banking overlay should cover:
- Interagency Guidance on Third-Party Relationships: Risk Management (June 6, 2023, OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023): risk-based lifecycle, criticality determination, banking-specific tailoring (especially for community and midsize banks).
- OCC Bulletin on Bank-Fintech Arrangements [verify bulletin number] and Joint Agency Statement on Bank-Fintech Arrangements (FDIC/OCC/FRB, 2024) [verify title and date]: banking-specific overlay when the vendor is a fintech, including end-user ledgering, FBO-account governance, BaaS-program criticality classification.
- Bank Service Company Act, 12 U.S.C. §1867(c): regulator examination authority over bank service providers and required contract flow-down (examination access, audit rights). This is a banking-only contract-clause expectation that does not apply to non-bank vendors.
- Reg O screen (12 CFR Part 215): vendor-diligence must include an insider screen on the vendor's principals when the vendor is owned by or has significant interests held by an insider of the partner bank. Most non-bank vendor-diligence frameworks do not consider this.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards): for covered banks ($50B+), vendor-diligence outputs feed the risk-governance framework and the board's third-party oversight; the overlay should specify the additional evidence expected (board-level reporting, risk-appetite linkage).
- Comptroller's Handbook, Third-Party Relationships: Risk Management [verify current edition]: OCC examiner-facing detail on diligence, contract, and monitoring expectations; pin the most recent edition.
- AI-vendor mode within vendor-diligence (per the v1 plan): banking overlay should reference OCC Bulletin 2026-13 model risk implications when the vendor supplies a model or AI system used in a credit, compliance, or fraud decision.

## third-party-operational-resilience / exit-plan

Capability skill: `third-party-operational-resilience/skills/exit-plan`
Path: `exit-plan/references/sector-overlays/banking.md`

What the banking overlay should cover:
- Interagency Guidance on Third-Party Relationships: Risk Management (June 2023), §III.F termination [verify section label]: banking-specific exit expectations, including data return, evidence of exit-readiness, and supervisory expectations on tabletop testing.
- FBO-account wind-down sequence for sponsor-bank programs: deconversion pathway, customer-account portability to alternative bank, ledger reconciliation at termination, FDIC pass-through-deposit-insurance recordkeeping continuity.
- Bank Service Company Act §1867(c) examination-access continuity through wind-down: contract clauses must preserve regulator access to vendor records during and after termination.
- OCC, FDIC, FRB published consent orders involving fintech-partner exits: lessons on what examiners consider adequate exit evidence and tabletop testing.
- Customer-notification responsibility on deposit-account or credit-account termination, tied to Reg DD §1030.5 (subsequent disclosures) and Reg E §1005.8 (change-in-terms notice) where applicable.
- Stressed-exit scenarios for banks: counterparty failure of a critical vendor (e.g., BSA/AML system, core processor) and FDIC consultation requirements [verify under FDIC's role in resolutions and 12 USC §1820 examination authority].

## risk-compliance-core / control-matrix

Capability skill: `risk-compliance-core/skills/control-matrix`
Path: `control-matrix/references/sector-overlays/banking.md`

What the banking overlay should cover:
- 12 CFR Part 30 Appendix D (OCC Heightened Standards) §III risk governance framework [verify section]: control-matrix expectations for covered banks, including the three-lines-of-defense maturity, board independent risk committee evidence, and risk-appetite-statement integration into control objectives.
- FFIEC IT Examination Handbook, Information Security booklet (2016) [verify current edition]: technology-control rows expected when the matrix scopes a banking technology process.
- CRA / fair-lending control coverage triggers when the matrix scopes a lending process: ECOA / Reg B controls, HMDA controls, CRA-modernization-rule controls [verify CRA modernized rule current effective state given litigation history; the 2023 CRA final rule has been subject to legal challenge].
- BSA/AML control rows expected when the matrix scopes a customer-facing or money-movement process: CIP, CDD, BO, suspicious-activity monitoring, currency-transaction-reporting, OFAC screening.
- Bank-specific evidence pointers: Call Report (FFIEC 031/041), UBPR, internal liquidity and capital reports, ALCO and risk-committee minutes.
- Heightened Standards rebuttable-presumption posture for $50B+ banks if applied (overlay should flag the regulatory threshold, not just describe controls).

## risk-reporting / risk-committee-pack

Capability skill: `risk-reporting/skills/risk-committee-pack`
Path: `risk-committee-pack/references/sector-overlays/banking.md`

What the banking overlay should cover:
- 12 CFR Part 30 Appendix D §III.B risk appetite [verify section] and the board's role in approving and overseeing the risk-appetite statement: covered banks must include risk-appetite-statement updates in committee materials.
- Interagency-defined risk types for banks (credit risk, market risk, liquidity risk, operational risk, compliance risk, strategic risk, reputational risk, model risk; with additional supervisory focus on cyber, third-party, financial crime): the committee-pack section structure should map to these named risk types.
- BHC supervisory cycle integration (FRB SR 12-17): risk-committee materials at a BHC level should reference the consolidated supervision framework and rated components.
- MRA / MRIA aging and closure-status as a standing committee-pack section for banks; the overlay should specify the columns expected (regulator, finding, action plan, closure status, aging).
- Capital adequacy and capital-planning content expectations for banks, including DFAST / CCAR results integration for applicable BHCs [verify current CCAR scope].
- Liquidity-risk content expectations including LCR / NSFR position for applicable banks, contingency-funding-plan test record, and brokered-deposit / sponsor-program-FBO-deposit treatment.
- Three-lines-of-defense maturity reporting and independent-risk-management evidence for committee minutes.

## regulatory-change-management / exam-brief

Capability skill: `regulatory-change-management/skills/exam-brief`
Path: `exam-brief/references/sector-overlays/banking.md`

What the banking overlay should cover:
- Banking exam types covered by the overlay: OCC full-scope safety-and-soundness, FRB BHC supervisory cycle (SR 12-17), FDIC risk-management examination, FFIEC BSA/AML examination, FFIEC IT examination, OCC and FDIC consumer-compliance examination, CRA performance evaluation.
- CAMELS rating system integration: the exam-brief overlay should explain that for bank exams the brief organizes around CAMELS components rather than generic risk areas.
- BHC rated components vs depository-institution CAMELS: cross-reference to the BHC supervisory framework.
- MRA / MRIA framework: definitions, escalation cadence, examiner-letter response expectations specific to banks.
- Examiner entry-meeting protocols and supervisory-letter cycle, including request-letter format expectations for bank exams.
- Distinction from `banking-supervision-readiness` (sector-plugin skill): the capability skill `exam-brief` is the generic exam-prep brief used for any FS exam (SEC, FINRA, NYDFS, CFPB, FCA, BaFin, etc.); the banking sector overlay describes how banks adapt the brief; the sector-plugin skill `banking-supervision-readiness` is the deeper, banking-specific artifact (CAMELS-component preparation, MRA/MRIA closure cross-walk, Heightened Standards readiness). The exam-brief overlay should explicitly point users to `banking-supervision-readiness` for full preparation.

## financial-crime-governance — overlay note

The financial-crime-governance plugin is sector-neutral in capability shape (CDD program design, EDD escalation, SAR governance, sanctions screening), but FFIEC BSA/AML manual is itself banking-aligned source material. Sector overlay flavor for banks is largely already inside the capability skill's primary anchors. A thin banking overlay is still useful at:

- `financial-crime-governance/skills/edd-escalation-pack/references/sector-overlays/banking.md`: banking-specific escalation paths (BSA officer to chief risk officer to board), fintech-partner customer treatment, sponsor-bank-program end-user-customer treatment, and §326 USA PATRIOT Act CIP-program governance integration.
- `financial-crime-governance/skills/sanctions-screening-controls/references/sector-overlays/banking.md` (if present): banking-specific OFAC examiner expectations, correspondent-banking screening (12 CFR §1010.610 [verify]), and sponsor-bank-program OFAC flow.

(These are noted here so the financial-crime-governance lead is aware. Decision on whether to ship them stays with that plugin.)
