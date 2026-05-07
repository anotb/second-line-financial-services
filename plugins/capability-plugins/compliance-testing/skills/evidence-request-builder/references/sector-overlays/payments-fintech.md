# Payments-fintech sector overlay — evidence-request-builder

Loaded when `engagement-scope.sector_overlay_set` includes `payments-fintech` or when the test addresses NACHA, sponsor-bank, money-transmitter, prepaid, or larger-participant rules. Supplements `references/source-anchors.md`.

## Request-list conventions payments-fintech testing programs apply

Payments and fintech testing PBC lists carry conventions distinct from bank consumer-compliance:

- **Sponsor-bank arrangements load two sector overlays.** The fintech program tests against payments-fintech rules; the sponsor-bank arrangement tests against banking rules (Bank Service Company Act, Joint Statement on Bank-Third-Party Deposit Programs, end-customer reconciliation, deposit-insurance representation). Both overlays load and the request list names which evidence sits on which side. Sponsor-bank-side requests cite the bank's BSCA-covered contract for examiner access.
- **Reg E case-file requests are per-case PDF bundles.** §1005.11 case files are the workpaper for Reg E error-resolution testing; request the case file (notice date, investigation evidence, provisional credit evidence, final determination, customer notice, any reversal) per sample case ID.
- **NACHA Operating Rules are paywalled.** Cite as "current edition; specific sections to be confirmed against the firm's licensed copy" rather than asking for rule text. Request the firm's compliance evidence against the NACHA rules (Third-Party Sender risk-management evidence, ODFI-warranty evidence, return-rate monitoring) drawing against the firm's licensed-copy sections.
- **Money-transmitter evidence carries state-by-state structure.** The request list lists per-state-licensed entity the licensing register, per-state surety bond or net-worth evidence, per-state customer-funds protection evidence (segregation, permissible investments), and per-state reporting evidence (call reports, MSB reports under FinCEN 31 CFR Part 1022).
- **Crypto and stablecoin evidence asks the source-of-record system explicitly.** Where the firm's evidence sits on-chain (wallet inventory, on-chain reserves attestation), the request cites the chain, the wallet address scope, and the block-height or snapshot date; off-chain evidence sits in the firm's exchange or custody system and the request names the system.

## Payments-fintech-supervisory anchors (load by reference; do not restate)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Operative for sponsor-bank programs.
- **Interagency Guidance on Third-Party Relationships: Risk Management** (FDIC / OCC / FRB, June 6, 2023) [verify section labels]. Sponsor-bank oversight evidence requests sit inside this frame. https://www.federalreserve.gov/supervisionreg/srletters/SR2304.htm .
- **Reg E — 12 CFR Part 1005**, especially §1005.6 (consumer liability), §1005.7 (initial disclosures), §1005.10 (preauthorized transfers), §1005.11 (error resolution), §1005.18 (prepaid accounts) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1005 .
- **NACHA Operating Rules (current edition)** [verify rule citations against the firm's licensed copy]. https://www.nacha.org/ .
- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1010.380 [verify subsection labels]. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022 .
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state including any litigation or congressional review]. https://www.consumerfinance.gov/compliance/supervisory-guidance/ [verify URL].
- **State money-transmitter rules** (state by state) — request lists carry the state-adopted statute citation, not the Money Transmission Modernization Act text [verify state citations].
- **OCC Bulletin 2008-12 — Risk Management Guidance on Payment Processors** [verify exact bulletin number] for bank-side processor-relationship testing.

## Payments-fintech-control-area request notes

### Reg E error-resolution testing (§1005.11)

- Request conventions: per-sample case file PDF bundle (notice date, investigation evidence, provisional credit evidence with timing, final determination, customer notice, any reversal). Dispute-management-system case extract per sample with case-event log (notice received, investigation start, provisional credit issued, final determination, customer notice, reversal where applicable). Reliance test note covers completeness of the case file against the dispute-management system. Prepaid-account testing under §1005.18 requests the prepaid-program subset of the population with the additional disclosure-format and access-time evidence.

### Sponsor-bank end-customer reconciliation testing

- Request conventions: end-customer reconciliation evidence for the period — sponsor-bank FBO subledger extract joined to the fintech program's customer ledger by sample (or full-population reconciliation if program volume is small). Reconciliation cadence evidence (daily, weekly, month-end). Exception-aging and unmatched-balance treatment evidence. The request list distinguishes bank-side and fintech-side ownership of each evidence row.
- Deposit-insurance representation review requests the firm's customer-facing communications (account-opening, T&Cs, marketing) per the FDIC pass-through-deposit-insurance requirements [verify FDIC citation].
- Fourth-party register evidence is requested where the fintech program relies on subcontractors that the sponsor-bank's TPRM frame requires registering.

### NACHA Third-Party Sender testing

- Request conventions: TPS testing requests risk-management evidence per the firm's licensed NACHA Rules copy, the ODFI agreement, the originator-due-diligence file by sample, the return-rate monitoring evidence, the unauthorised-return investigation evidence, and the OFAC screening evidence on originators. Cite the NACHA rule by edition and section without restating; rely on the firm's licensed copy.

### BSA/AML testing for MSBs and fintechs

- Request conventions: AML-program testing requests CIP, CDD, and EDD evidence per sample under the FFIEC BSA/AML Examination Manual and 31 CFR Part 1022 [verify part references]. Suspicious-activity testing requests case-management evidence with the same access-control posture as bank BSA testing (SAR content access restricted; the request notes the access control without restating SAR content). Sanctions-screening testing requests the screening configuration, the alert log per sample, and the alert-disposition evidence.

### State money-transmitter testing

- Request conventions: per-state-licensed entity, the licensing register, the surety-bond or net-worth evidence (per the state's standard), the customer-funds protection evidence (segregation accounts, permissible investments), the per-state reporting evidence (state-required call reports, customer-funds attestations), and the per-state customer-disclosure evidence. The request list groups by state because the criteria differ.

### Crypto and stablecoin program testing

- Request conventions: wallet inventory (chain, wallet address, custodian role), proof-of-reserves attestation evidence (where the program represents a reserves position), customer asset segregation evidence, sanctions-screening at the wallet level, and the firm's travel-rule compliance evidence under FinCEN 31 CFR §1010.410(f) [verify subsection]. On-chain evidence cites the chain, the wallet address scope, and the snapshot block-height or date.

### CFPB larger-participant scope (where applicable)

- Request conventions: where the firm is a CFPB larger participant for digital consumer payment applications, CMS-aligned testing applies. The request list cites the larger-participant rule [verify Federal Register citation] alongside the substantive rule under test (Reg E, UDAAP).

## Audience and tone

A request list drafted ahead of an upcoming CFPB exam reads heavier on UDAAP-relevant evidence (call recordings, complaint files, marketing-claim review records). A request list drafted ahead of a state money-transmitter exam reads heavier on the state-specific licensing, surety-bond, customer-funds protection, and reporting evidence. A request list drafted ahead of a sponsor-bank-led oversight cycle reads heavier on the bank-side and fintech-side control split, with the bank service provider relationship explicit and the BSCA examiner-access posture cited where relevant.
