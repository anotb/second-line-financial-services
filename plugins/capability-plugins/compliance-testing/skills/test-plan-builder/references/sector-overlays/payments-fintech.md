# Payments-fintech sector overlay — test-plan-builder

Loaded when `scope.sector_overlay_set` includes `payments-fintech` or when the test addresses NACHA, sponsor-bank, money-transmitter, prepaid, or larger-participant rules. Supplements `references/source-anchors.md`.

## Test-plan conventions for payments and fintech testing

Payments and fintech test plans carry conventions that bank consumer-compliance test planning does not always anticipate:

- **Sponsor-bank arrangements load two sector overlays.** The fintech program tests against payments-fintech rules; the sponsor-bank arrangement tests against banking rules (Bank Service Company Act, the 2024 Joint Statement on bank-third-party deposit programs, end-customer reconciliation, deposit-insurance representation). Both overlays load and the plan names which controls sit on which side.
- **Reg E error-resolution case files are the operating-procedure unit.** The case file the firm produces in the ordinary course is the testing artifact under §1005.11. Compliance test plans for Reg E error-resolution sample case files for adherence to the procedure and the procedural clock.
- **NACHA Operating Rules are paywalled.** Cite as "current edition; specific sections to be confirmed against the firm's licensed copy" rather than restating rule text in the plan. The criteria section names the rule citation; the firm's licensed copy is the source of truth at fieldwork.
- **Larger-participant CFPB scope changes the criteria base.** Where the firm is a CFPB larger participant for digital consumer payment applications, CMS-aligned planning applies; the plan cites the larger-participant rule alongside the substantive rule under test. (The November 2024 final rule has been the subject of post-publication challenge and CFPB reconsideration since 2025 — verify current operative status before treating designation as firm.)

## Payments-fintech-supervisory anchors (load by reference; do not restate)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Operative for sponsor-bank programs.
- **Reg E — 12 CFR Part 1005**, especially §1005.6 (consumer liability), §1005.7 (initial disclosures), §1005.8 (change-in-terms), §1005.10 (preauthorized transfers), §1005.11 (error resolution), §1005.18 (prepaid accounts) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1005 .
- **NACHA Operating Rules (current edition)** Third-Party Sender risk-management rules and ODFI obligations [verify rule citations against the firm's licensed copy]. https://www.nacha.org/ .
- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1010.380 [verify subsection labels]. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022 .
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (November 21, 2024) — the rule has been the subject of post-publication challenge and CFPB reconsideration since 2025; verify current operative status before relying on designation. https://www.consumerfinance.gov/compliance/supervisory-guidance/ .
- **State money-transmitter rules** (state by state) — test plans cite the state-adopted statute citation, not the Money Transmission Modernization Act text [verify state citations].
- **Interagency Guidance on Third-Party Relationships: Risk Management** (FDIC / OCC / FRB, June 6, 2023) [verify section labels]. https://www.federalreserve.gov/supervisionreg/srletters/SR2304.htm .

## Payments-fintech-control-area test-plan notes

### Reg E error-resolution testing

- Test-plan conventions: criteria section cites §1005.11 and the firm's dispute-handling policy section; population is the Reg E disputes raised in the period; design procedures cover the dispute-management system workflow configuration (does the workflow enforce the day-10 or day-5 provisional-credit clock, the 45-day final-resolution clock, the customer-notice generation [verify §1005.11(c) / (d) timing]); operating procedures cover sample-based reperformance against the procedural clock with the case file as evidence per sample.
- Pass criterion: 100% of sampled disputes within the procedural clock with current evidence in the case file. Fail criterion: any sampled item outside the clock without escalation evidence.
- Prepaid-account test plans under §1005.18 carry additional disclosure-format and access-time provisions; the plan names the prepaid-program subset of the population.

### Sponsor-bank end-customer reconciliation testing

- Test-plan conventions: end-customer reconciliation test plans read the sponsor-bank FBO subledger against the fintech program's customer ledger by sample (or by full reconciliation if the program's volume is small). Plan carries timing (daily, weekly, month-end), exception aging, and unmatched-balance treatment as procedure design.
- Deposit-insurance representation review is a separate test; the plan reads the firm's customer-facing communications (account-opening, T&Cs, marketing) against FDIC pass-through-deposit-insurance requirements [verify FDIC citation].

### NACHA Third-Party Sender testing

- Test-plan conventions: TPS test plans cover risk-management evidence per the firm's licensed NACHA Rules copy, the ODFI agreement, the originator-due-diligence file by sample, the return-rate monitoring evidence, and the unauthorised-return investigation evidence. Cite the NACHA rule by edition and section without restating; rely on the firm's licensed copy.

### BSA/AML for MSBs and fintechs

- Test-plan conventions: AML-program test plans cover CIP, CDD, and EDD evidence per the FFIEC BSA/AML Examination Manual and 31 CFR Part 1022 [verify part references]. Suspicious-activity test plans review case-management evidence with the same access-control posture as bank BSA testing (SAR content access restricted; the plan names the access control rather than restating SAR content).

### Larger-participant CFPB scope (where applicable)

- Test-plan conventions: where the firm is a CFPB larger participant for digital consumer payment applications, CMS-aligned testing applies (verify operative status of the November 2024 designation rule on the engagement date). The plan cites the larger-participant rule alongside the substantive rule under test.

## Audience and tone

A test plan drafted with an upcoming CFPB exam in mind reads heavier on UDAAP-relevant disclosures, error-resolution timing, and customer-impact framing. A plan drafted for a state money-transmitter exam reads heavier on the state-statute citation, customer-funds protection (segregation, permissible investments) testing, and the surety-bond or net-worth status. A plan drafted for sponsor-bank governance reads heavier on the bank-side and fintech-side control split with the bank service provider relationship explicit.
