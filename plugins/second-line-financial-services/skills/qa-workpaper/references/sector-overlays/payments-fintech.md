# Payments-fintech sector overlay — qa-workpaper

Loaded when `scope.sector_overlay_set` includes `payments-fintech` or when the QA review covers a workpaper at a payments firm, money-services business, sponsor-bank fintech program, or BIN-sponsorship arrangement. Supplements `references/source-anchors.md`. Pairs with `banking.md` when the test addresses a sponsor-bank arrangement.

## QA conventions for payments-fintech testing workpapers

Payments-fintech second-line testing workpapers carry methodology distinct from direct-bank consumer-compliance testing:

- **Sponsor-bank workpapers carry the interagency TPRM frame.** Ongoing-monitoring evidence, end-customer reconciliation, FBO subledger testing, deposit-insurance representation review, and the fourth-party register all sit inside the interagency TPRM guidance (June 2023) plus the joint statement on bank deposit arrangements (July 2024). The QA reviewer challenges whether the workpaper's evidence inspection posture matches what the sponsor bank's regulators (FRB / FDIC / OCC) would re-perform on examination.
- **Reg E error-resolution testing carries clock-driven QA dimensions.** §1005.11(c) timing has explicit clocks (10 business days for investigation, 45 days for completion or 90 days for new accounts and POS / foreign transactions). The QA reviewer challenges the timeline reperformance for every sample item and confirms the severity calibration reads against the firm methodology floor (typically high for §1005.11(c) timing).
- **NACHA Operating Rules reliance is paywalled and version-sensitive.** The QA reviewer confirms the workpaper named the edition of the NACHA rules it tested against, since the rules amend annually; reliance on a stale edition is an evidence-reliability finding.
- **End-customer reconciliation testing reads against the firm-and-sponsor split.** Sponsor-bank arrangements split end-customer reconciliation responsibility between the fintech and the sponsor; the QA reviewer confirms the workpaper named the responsibility split and tested the firm side, with reliance on the sponsor side noted as a limitation.

## Payments-fintech-supervisory anchors (load by reference; do not restate)

- **Interagency Guidance on Third-Party Relationships: Risk Management** (FRB / FDIC / OCC, June 2023; 88 Fed. Reg. 37920, June 9, 2023) [verify section labels]. https://www.federalreserve.gov/supervisionreg/srletters/sr2304.htm .
- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date].
- **Reg E — 12 CFR Part 1005**, especially §1005.6 (consumer liability), §1005.11 (procedures for resolving errors), and §1005.18 (prepaid accounts) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1005 .
- **NACHA Operating Rules (current edition)** Third-Party Sender risk management and ODFI obligations [verify rule citations and edition year]. Paywalled. https://www.nacha.org/ .
- **Bank Service Company Act, 12 USC §1867(c)** — examiner access to vendor systems sponsor banks rely on. https://www.law.cornell.edu/uscode/text/12/1867 .

## Payments-fintech-control-area QA notes

### Reg E error-resolution testing — QA scope items

- The QA reviewer reperforms a small subsample of the timeline (notice date, investigation start, provisional credit, final determination, customer notice) per sample item, confirms the evidence ID is present for each timeline event, and challenges any "investigation completed" entry without an evidence ID. Severity calibration on §1005.11(c) timing deviations is the most-challenged dimension; firm methodology floors are typically high.

### Sponsor-bank end-customer reconciliation testing — QA scope items

- The QA reviewer confirms the workpaper documents the FBO account structure, the subledger reconciliation cadence, the threshold for breaks investigated, and the aging of unreconciled items. Reliance on sponsor-bank-supplied reconciliation evidence is an evidence-reliability dimension; the QA reviewer challenges whether the firm independently verified the sponsor's reconciliation posture.

### Critical-vendor monitoring testing — QA scope items

- The QA reviewer confirms the workpaper's conclusion on critical-vendor monitoring is supported by evidence of the firm's KRI dashboard tie-out for that vendor, not just by the existence of a vendor-supplied SOC 2 report. Conclusion without dashboard tie-out is a recurring deficiency in examiner-prep sweeps.

### Exit-plan testing — QA scope items

- The QA reviewer confirms exit-plan-testing workpapers carry tabletop evidence (date, scenario, participants by role, observations, action-item closure) and that absence of exit-plan testing is rated to firm methodology floor (typically high for critical vendors, with supervisory expectations under interagency TPRM aligned).

### NACHA Third-Party Sender testing — QA scope items

- The QA reviewer confirms the workpaper named the NACHA edition tested against, that the Third-Party Sender risk-assessment evidence is documented per the named rule citation, and that reliance on the ODFI's separate testing is noted as a limitation rather than a substitute.

## Audience and tone

A QA review note drafted for a sponsor-bank fintech-program workpaper reads heavier on the interagency TPRM frame, the end-customer reconciliation responsibility split, and the FBO subledger reconciliation evidence. A QA note drafted with an upcoming Federal Reserve targeted exam on third-party risk in mind reads heaviest on the population-level deficiency themes across the TPRM workpaper portfolio (vendor SOC 2 reliance, KRI dashboard tie-out, exit-plan testing severity calibration).
