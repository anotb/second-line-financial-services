# Payments-fintech sector overlay — workpaper-drafter

Loaded when `scope.sector_overlay_set` includes `payments-fintech` or when the test addresses NACHA, sponsor-bank, money-transmitter, prepaid, or larger-participant rules. Supplements `references/source-anchors.md`.

## Workpaper conventions for payments and fintech testing

Payments and fintech testing workpapers carry conventions that bank consumer-compliance testing does not always anticipate:

- **Sponsor-bank arrangements load two sector overlays.** The fintech program tests against payments-fintech rules; the sponsor-bank arrangement tests against banking rules (Bank Service Company Act, Joint Statement on Bank-Third-Party Deposit Programs, end-customer reconciliation, deposit-insurance representation). Both overlays load and the workpaper names which controls sit on which side.
- **Reg E error-resolution case files are themselves workpapers.** The case file the firm produces in the ordinary course is the testing artifact under §1005.11. Compliance-testing workpapers reading Reg E error-resolution sample case files for adherence to the procedure are reading workpapers-of-workpapers; cite by case ID and treat the case file as system-of-record evidence.
- **NACHA Operating Rules are paywalled.** Cite as "current edition; specific sections to be confirmed against the firm's licensed copy" rather than restating rule text in the workpaper. The criteria section names the rule citation; the firm's licensed copy is the source of truth.

## Payments-fintech-supervisory anchors (load by reference; do not restate)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Operative for sponsor-bank programs.
- **Reg E — 12 CFR Part 1005**, especially §1005.6 (consumer liability), §1005.7 (initial disclosures), §1005.8 (change-in-terms), §1005.10 (preauthorized transfers), §1005.11 (error resolution), §1005.18 (prepaid accounts) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1005 .
- **NACHA Operating Rules (current edition)** Third-Party Sender risk-management rules and ODFI obligations [verify rule citations against the firm's licensed copy]. https://www.nacha.org/ .
- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1010.380 [verify subsection labels]. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022 .
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state including any litigation or congressional review]. https://www.consumerfinance.gov/compliance/supervisory-guidance/ [verify URL].
- **State money-transmitter rules** (state by state) — testing workpapers carry the state-adopted statute citation, not the Money Transmission Modernization Act text [verify state citations].
- **OCC Bulletin 2008-12 — Risk Management Guidance on Payment Processors** [verify exact bulletin number] for bank-side processor-relationship testing.

## Payments-fintech-control-area workpaper notes

### Reg E error-resolution testing

- Workpaper conventions: §1005.11 procedures are tested by case sample. The workpaper reads notice date, investigation start, provisional credit (where applicable, by day 10 or day 5 for new accounts [verify §1005.11(c) timing]), final determination, customer notice, and any reversal-of-provisional-credit. The case file is treated as system-of-record evidence with reliance test note on completeness against the dispute-management system.
- Prepaid-account testing under §1005.18 carries additional disclosure-format and access-time provisions; the workpaper notes the prepaid-program subset of the population.

### Sponsor-bank end-customer reconciliation testing

- Workpaper conventions: end-customer reconciliation testing reads the sponsor-bank FBO subledger against the fintech program's customer ledger by sample (or by full reconciliation if the program's volume is small). Reconciliation workpapers carry timing (daily, weekly, month-end), exception aging, and unmatched-balance treatment. The workpaper limitations section names the period covered; reconciliations rely on point-in-time extracts.
- Deposit-insurance representation review is a separate test; the workpaper reads the firm's customer-facing communications (account-opening, T&Cs, marketing) against FDIC pass-through-deposit-insurance requirements [verify FDIC citation].

### NACHA Third-Party Sender testing

- Workpaper conventions: TPS testing reads risk-management evidence per the firm's licensed NACHA Rules copy, the ODFI agreement, the originator-due-diligence file by sample, the return-rate monitoring evidence, and the unauthorised-return investigation evidence. Cite the NACHA rule by edition and section without restating; rely on the firm's licensed copy.

### BSA/AML for MSBs and fintechs

- Workpaper conventions: AML-program testing reads CIP, CDD, and EDD evidence per the FFIEC BSA/AML Examination Manual and 31 CFR Part 1022 [verify part references]. Suspicious-activity testing reviews case-management evidence with the same access-control posture as bank BSA testing (SAR content access restricted; the workpaper notes the access control without restating SAR content).

### Larger-participant CFPB scope (where applicable)

- Workpaper conventions: where the firm is a CFPB larger participant for digital consumer payment applications, CMS-aligned testing applies. The workpaper cites the larger-participant rule [verify Federal Register citation] alongside the substantive rule under test.

## Audience and tone

A workpaper drafted with an upcoming CFPB exam in mind reads heavier on UDAAP-relevant disclosures, error-resolution timing aggregation, and customer-impact framing. A workpaper drafted for a state money-transmitter exam reads heavier on the state-statute citation, the customer-funds protection (segregation, permissible investments) testing, and the surety-bond or net-worth status. A workpaper drafted for sponsor-bank governance reads heavier on the bank-side and fintech-side control split, with the bank service provider relationship explicit.
