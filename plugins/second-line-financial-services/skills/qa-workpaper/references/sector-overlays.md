# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — qa-workpaper

Loaded when `scope.sector_overlay_set` includes `banking` or when the QA review covers a workpaper addressing a banking regulator's rule. Does not replace `references/source-anchors.md`; supplements it with bank-specific QA conventions. This is the heaviest overlay in the qa-workpaper file set: bank-supervisory expectations on independent QA over the testing program are explicit and recurring CMS findings.

#### QA conventions banking examiners expect

A QA review note over a bank consumer-compliance, BSA/AML, or operational-risk testing workpaper carries a few conventions beyond the IIA / AICPA baseline:

- **Independent QA is structural, not advisory.** The CFPB CMS examination procedures, the OCC Comptroller's Handbook CMS module, and SR 08-8 read independent QA over the testing program as a CMS pillar. A workpaper that has not been QA-reviewed by an independent reviewer is a CMS finding distinct from any substantive control finding.
- **Reviewer-separation is a structural QA dimension.** Bank exam findings repeatedly cite preparer-and-reviewer-as-same-role and preparer-and-QA-as-same-role on the sign-off block. The QA review note checks the sign-off block first; same-role overlap is a critical deficiency that returns the workpaper.
- **Population definition and extract-integrity are QA scope items.** Examiners pull the workpaper, the population definition, and the extract integrity check together. The QA reviewer challenges whether the extract date is recorded, whether the run-by role is named, and whether the completeness check against an independent count is documented. Missing any of the three is a major deficiency.
- **Severity calibration ties to the firm's CMS rating implications.** Severity inflation in the workpaper distorts the testing-program output that feeds the CMS rating; severity deflation buries findings the examiner will surface anyway. The QA reviewer challenges severity against firm methodology floors and against analogous prior workpapers; both directions get pushback.
- **Conclusion language stays in second-line vocabulary.** Bank consumer-compliance workpapers occasionally drift into "the firm violated [Reg X]" framing. The QA reviewer rewrites to control-effectiveness language and routes the legal-violation question to legal counsel and the head of regulatory affairs separately.

#### Bank-supervisory anchors (load by reference; do not restate)

- **CFPB Compliance Management Review** examination procedures inside the **CFPB Supervision and Examination Manual** (current edition) [verify section labels for the testing-program independent-QA component]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **OCC Comptroller's Handbook — Compliance Management Systems** [verify current edition and section labels for independent-QA expectations]. https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/index-comptrollers-handbook.html .
- **SR 08-8 — Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles** (Federal Reserve, October 16, 2008) [verify section labels for independent-review of testing work product]. https://www.federalreserve.gov/boarddocs/srletters/2008/sr0808.htm .
- **OCC PPM 5310-3 — Bank Supervision Process** [verify exact PPM number and current effective date].
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks; independent-risk-management standards on testing-program QA feed the risk-governance framework and the board's third-line oversight [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-I/part-30 .
- **FFIEC Consumer Compliance Rating System** (Federal Register, 80 Fed. Reg. 67428, November 2, 2015) [verify Federal Register citation]. https://www.federalregister.gov/documents/2015/11/02/2015-27738/ffiec-consumer-compliance-rating-system [verify URL].

#### Bank-control-area QA notes

##### HMDA / Reg C testing — QA scope items

- Reg C — 12 CFR Part 1003. §1003.4 data points, §1003.5 disclosure and reporting [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1003 .
- QA conventions: the QA reviewer re-performs a small subsample of the LAR-to-LOS reconciliation and the per-field reperformance to confirm the preparer's findings; QA challenges whether the field-level deviation rate calculation matches the FFIEC HMDA Filing Instructions Guide [verify edition] field-validation logic; QA challenges whether the segment concentration commentary is supported (e.g., non-residential refinances clustered) and whether the FFIEC HMDA re-submission threshold consideration was routed to legal review and the head of regulatory affairs as a reviewer question, not concluded in the workpaper.

##### CRA testing — QA scope items

- CRA — 12 CFR Part 25 (OCC), Part 195 (former OTS, OCC), Part 228 (FRB Reg BB), Part 345 (FDIC) [verify current effective state given the 2023 final-rule litigation history]. https://www.federalreserve.gov/supervisionreg/regbbcg.htm .
- QA conventions: the QA reviewer challenges whether the lending-test workpaper carries the geography distribution, borrower-profile distribution, and product-mix distribution against the assessment-area definition; whether the qualified-investment register reconciles to the workpaper's investment-test sample; whether performance-context narrative was carried from the test plan rather than invented in the workpaper.

##### Reg B / ECOA testing — QA scope items

- Reg B — 12 CFR Part 1002. §1002.4, §1002.6, §1002.9, §1002.13 [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- QA conventions: the QA reviewer challenges whether adverse-action notice-timing testing reconciles application date to notice date by sample; whether spousal-signature testing reads the underwriting file (not just the front-end application); whether demographic-firewall testing reads the production environment (not the test environment). Production-versus-test environment evidence reliance is a recurring QA finding on Reg B workpapers.

##### Reg DD, Reg E, Reg Z testing — QA scope items

- Reg DD — 12 CFR Part 1030; Reg E — 12 CFR Part 1005 (especially §1005.11 and §1005.18); Reg Z — 12 CFR Part 1026 [verify subsection labels].
- QA conventions: error-resolution workpapers under Reg E §1005.11 are walked by sample with QA re-perform of the timeline (notice date, investigation start, provisional credit, final determination, customer notice). Common QA findings: "investigation completed" rows without an evidence ID; severity rated medium where firm methodology floor for §1005.11(c) timing is high; conclusion language drifting toward "the bank did not comply with Reg E §1005.11(c)" instead of control-effectiveness framing. Disclosure-content workpapers carry a redline against the regulatory model; QA confirms the redline and the noted deviations.

##### BSA/AML testing — QA scope items

- FFIEC BSA/AML Examination Manual (current edition) [verify last-revision date]. https://bsaaml.ffiec.gov/manual .
- 31 CFR Part 1010, 1020, 1022, 1023, 1024, 1025, 1026 (FinCEN AML rules by industry) [verify part references].
- QA conventions: CIP testing QA confirms new-account opening packet ties to the documented identification and verification step; CDD/EDD testing QA confirms the customer-due-diligence questionnaire and EDD enrichment evidence is sampled and reperformed; SAR-decision testing QA confirms the case-management file walks alert to disposition with timing checks against 31 CFR §1020.320. SAR content review is restricted to authorised reviewers; the QA reviewer does not restate SAR content in the QA review note and confirms the access-control posture on the underlying file is documented.

##### CFPB CMS exam-cycle workpapers — QA scope items

- The QA review reads against the four CMS pillars (board and management oversight, compliance program, response to consumer complaints, compliance audit). The compliance-audit pillar carries the independent-QA requirement; a workpaper that has not been independently QA-reviewed creates a separate CMS finding from any substantive control finding. The QA reviewer flags this distinction in the review note where applicable.

#### Sponsor-bank / bank-fintech-arrangement QA — examiner-prep sweep posture

A Federal Reserve, OCC, or FDIC targeted exam on third-party risk frequently arrives with six-to-eight-week notice. The second-line QA function is often called to do an examiner-prep sweep on the population of TPRM workpapers from the most recent testing cycle. The sweep posture differs from in-cycle QA:

- **Per-workpaper QA notes batched into one summary review.** The deliverable is a portfolio QA review with population-level deficiency themes plus per-workpaper notes.
- **Common deficiencies carried explicitly.** Vendor-supplied SOC 2 reports cited as evidence without the firm's reliance assessment documented; critical-vendor monitoring conclusions without evidence of the firm's KRI dashboard tie-out for that vendor; severity calibration on exit-plan-testing absence rated medium where firm methodology floor (and supervisory expectation) is high.
- **Issue closure approval status flagged separately from workpaper closure.** A workpaper accepted by QA does not close any open issue identified in the workpaper. The QA review note carries `issue_closure_approval` separately from `decision`.
- **Methodology-drift finding.** A population-level pattern (e.g., reviewer drift across workpapers in the cycle) is itself a finding worth documenting; the recommendation seed routes back to a methodology refresh before the next cycle, not to per-workpaper rework.

The frame:

- **Interagency Guidance on Third-Party Relationships: Risk Management** (FRB / FDIC / OCC, June 2023; 88 Fed. Reg. 37920, June 9, 2023) [verify section labels for ongoing-monitoring evidence and the firm's testing-and-review posture]. https://www.federalreserve.gov/supervisionreg/srletters/sr2304.htm .
- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. End-customer reconciliation, FBO subledger, deposit-insurance representation, and the fourth-party register all sit inside this frame.
- **Bank Service Company Act, 12 USC §1867(c)**: examiner-access posture for vendor systems the firm relied on for evidence; the QA reviewer confirms the workpaper named the BSCA-relied-on systems separately so the examiner can sequence the access request.

#### Audience and tone

A QA review note drafted with an upcoming OCC, FRB, FDIC, or CFPB exam in mind reads heavier on independent-QA evidence (sign-off block, reviewer separation, QA reviewer role and date), heavier on extract-integrity dimensions, and heavier on conclusion-language hygiene. A QA note for in-cycle testing-program closure reads operationally with the same dimensions but lighter on the examiner-prep posture.

## capital-markets

### Capital-markets sector overlay — qa-workpaper

Loaded when `scope.sector_overlay_set` includes `capital-markets` or when the QA review covers a workpaper at a broker-dealer, investment adviser, or registered fund. Supplements `references/source-anchors.md`.

#### QA conventions for capital-markets testing workpapers

Capital-markets second-line testing workpapers carry methodology distinct from bank consumer-compliance testing:

- **FINRA 3120 / 3130 supervisory-controls testing supports CEO certification.** Broker-dealer CCO testing of supervisory processes feeds the FINRA Rule 3130 annual CEO certification. The QA reviewer challenges whether the workpaper's documentation supports the certification posture, not just the testing-program posture; severity calibration on supervisory-controls deficiencies carries certification-language implications.
- **Rule 206(4)-7 adviser-compliance-program annual review.** The Rule 206(4)-7 annual review is itself a self-test; QA over the annual-review workpapers is the review-of-the-review. SEC examiner expectations on the documentation underlying the annual review are explicit in published Division of Examinations risk alerts; the QA reviewer carries that posture.
- **Conclusion language hygiene is structurally important.** Capital-markets enforcement environment makes legal-violation framing in workpaper conclusions particularly costly: a workpaper concluding "the firm violated [Rule X]" can be discoverable and used adversely. The QA reviewer rewrites to control-effectiveness language and routes the legal question to legal counsel separately.
- **Recordkeeping evidence reliance.** SEC Rule 17a-4 and FINRA Rule 4511 govern the recordkeeping the workpaper relies on. The QA reviewer confirms the workpaper named the source system, the recordkeeping-rule applicable to that record class, and the retention posture; reliance on a record that has aged out of retention is an evidence-reliability finding.

#### Capital-markets-supervisory anchors (load by reference; do not restate)

- **FINRA Rule 3120 — Supervisory Control System** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3120 .
- **FINRA Rule 3130 — Annual Certification of Compliance and Supervisory Processes** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3130 .
- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule, including annual review documentation expectations [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 .
- **SEC Rule 17a-4 (17 CFR §240.17a-4) — Records to be Preserved by Certain Exchange Members, Brokers, and Dealers** [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-4 .
- **FINRA Rule 4511 — General Requirements (Books and Records)** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/4511 .
- **SEC Division of Examinations risk alerts on adviser compliance-program documentation** (current alerts) [verify alert IDs and dates]. https://www.sec.gov/exams .

#### Capital-markets-control-area QA notes

##### FINRA 3120 supervisory-controls testing — QA scope items

- The QA reviewer confirms the workpaper's annual report on supervisory controls covers the required tests and verifications, that the documented review of those tests names the reviewer role separate from the tester, and that the report's conclusions on supervisory-control effectiveness do not drift into rule-violation framing.

##### Rule 206(4)-7 annual review — QA scope items

- The QA reviewer confirms the annual-review workpaper documents the methodology, the testing performed, the deficiencies identified, the remediation tracked, and the CCO's involvement. SEC Division of Examinations risk alerts have repeatedly cited annual-review workpapers that document only the conclusion without the methodology underneath; the QA reviewer pushes back on conclusion-only documentation.

##### Trade-surveillance and best-execution testing — QA scope items

- The QA reviewer confirms the trade-surveillance testing workpaper documents the alert-population definition, the disposition sample, and the timeline reperformance from alert to disposition with the surveillance-rule reference. Best-execution testing carries the venue-analysis methodology; the QA reviewer challenges whether the venue-analysis reperformance reads against the firm's best-execution policy effective during the period.

##### Recordkeeping testing — QA scope items

- The QA reviewer challenges reliance on records that have aged out of retention; reliance on archived emails reconstructed from backups (rather than the original WORM-compliant archive); and reliance on text-message records where the firm's archiving posture for off-channel communications is incomplete.

#### Audience and tone

A QA review note drafted for a broker-dealer workpaper reads heavier on the FINRA 3120 / 3130 certification-support posture; for an adviser workpaper, heavier on the Rule 206(4)-7 annual-review documentation posture. The conclusion-language hygiene posture is heaviest in capital-markets QA notes because of the enforcement environment; the QA reviewer's rewrite of legal-violation framing to control-effectiveness language is a recurring intervention.

## insurance

### Insurance sector overlay — qa-workpaper

Loaded when `scope.sector_overlay_set` includes `insurance` or when the QA review covers a workpaper at an insurer or insurance holding company. Supplements `references/source-anchors.md`.

#### QA conventions for insurance testing workpapers

Insurance second-line testing workpapers carry methodology distinct from bank consumer-compliance testing:

- **Model Audit Rule ICFR documentation review.** ICFR-relevant tests at insurers reportable under the NAIC Model Audit Rule (Model #205) carry documentation review by the firm's audit committee and external auditor; the QA reviewer challenges whether the workpaper's documentation supports the ICFR-attestation posture, not just the testing-program posture. Severity calibration on ICFR-relevant deficiencies carries Section-404-equivalent framing (deficiency / significant deficiency / material weakness) per AU-C 265.
- **Market-conduct workpaper review reads against state DOI examination standards.** State DOI market-conduct examiners apply the NAIC Market Conduct Examiners Handbook conventions when reading firm self-testing files. The QA reviewer confirms the workpaper's evidence inspection posture matches what the examiner would re-perform: claim-file sample reperformance, complaint-handling timeline reperformance, agent-licensing reconciliation.
- **Producer-licensing and appointment workpapers.** A recurring QA finding is reliance on the firm's producer-licensing system without an independent reconciliation against the NAIC State Producer Licensing Database (PLDB) or the state DOI license verification page. The QA reviewer challenges whether the reconciliation evidence is documented.

#### Insurance-supervisory anchors (load by reference; do not restate)

- **NAIC Annual Financial Reporting Model Regulation (Model Audit Rule, Model #205)** [verify section references for ICFR documentation review and audit-committee oversight]. https://content.naic.org/cipr-topics/topic-naic-model-laws-and-regulations [verify URL].
- **NAIC Market Conduct Examiners Handbook** (current edition) [verify section labels for the workpaper-review conventions state DOI examiners apply]. https://content.naic.org/cmte_d_mceh.htm [verify URL].
- **NAIC Financial Condition Examiners Handbook** (current edition) [verify section labels for ICFR-relevant audit-quality conventions]. https://content.naic.org/cmte_e_ex_ws_handbook.htm [verify URL].

#### Insurance-control-area QA notes

##### Claim-handling timeliness and unfair-claims-settlement testing

- State Unfair Claims Settlement Practices acts (state-by-state) [verify state citations applicable to the firm's licensed states]. The QA reviewer challenges whether the claim-file sample carries the timing reperformance against the state's specified clocks (acknowledgement, investigation, decision, payment), and whether the sample stratification by claim type and state reflects the population.

##### Producer-licensing and appointment testing

- State producer-licensing rules (state-by-state) [verify state citations]. NAIC PLDB. The QA reviewer confirms the producer-licensing extract reconciles against PLDB or the state DOI verification page, not just against the firm's internal CRM-licensing field.

##### Underwriting and rating testing

- State rating-rule files and the firm's filed rate manual. The QA reviewer challenges whether the underwriting-file sample reperformance reads against the firm's filed rate manual (the version effective on the policy date), not the current version.

##### ICFR-relevant testing under the Model Audit Rule

- The QA reviewer reads the workpaper against the AU-C 265 deficiency / significant deficiency / material weakness severity hierarchy and against the firm's ICFR-attestation posture. A workpaper severity-rated low on an ICFR-relevant control may still warrant a significant-deficiency communication if the control failure is reasonably possible to result in a material misstatement; the QA reviewer challenges the severity-to-ICFR-communication mapping.

#### Audience and tone

A QA review note drafted for an insurance workpaper reads heavier on the ICFR-attestation posture when the test is ICFR-relevant, heavier on the state DOI market-conduct conventions when the test is market-conduct-relevant, and heavier on the producer-licensing reconciliation when the test touches producer activity. A QA note drafted with an upcoming state DOI market-conduct exam in mind reads heaviest on the claim-file sample reperformance posture.

## payments-fintech

### Payments-fintech sector overlay — qa-workpaper

Loaded when `scope.sector_overlay_set` includes `payments-fintech` or when the QA review covers a workpaper at a payments firm, money-services business, sponsor-bank fintech program, or BIN-sponsorship arrangement. Supplements `references/source-anchors.md`. Pairs with `banking.md` when the test addresses a sponsor-bank arrangement.

#### QA conventions for payments-fintech testing workpapers

Payments-fintech second-line testing workpapers carry methodology distinct from direct-bank consumer-compliance testing:

- **Sponsor-bank workpapers carry the interagency TPRM frame.** Ongoing-monitoring evidence, end-customer reconciliation, FBO subledger testing, deposit-insurance representation review, and the fourth-party register all sit inside the interagency TPRM guidance (June 2023) plus the joint statement on bank deposit arrangements (July 2024). The QA reviewer challenges whether the workpaper's evidence inspection posture matches what the sponsor bank's regulators (FRB / FDIC / OCC) would re-perform on examination.
- **Reg E error-resolution testing carries clock-driven QA dimensions.** §1005.11(c) timing has explicit clocks (10 business days for investigation, 45 days for completion or 90 days for new accounts and POS / foreign transactions). The QA reviewer challenges the timeline reperformance for every sample item and confirms the severity calibration reads against the firm methodology floor (typically high for §1005.11(c) timing).
- **NACHA Operating Rules reliance is paywalled and version-sensitive.** The QA reviewer confirms the workpaper named the edition of the NACHA rules it tested against, since the rules amend annually; reliance on a stale edition is an evidence-reliability finding.
- **End-customer reconciliation testing reads against the firm-and-sponsor split.** Sponsor-bank arrangements split end-customer reconciliation responsibility between the fintech and the sponsor; the QA reviewer confirms the workpaper named the responsibility split and tested the firm side, with reliance on the sponsor side noted as a limitation.

#### Payments-fintech-supervisory anchors (load by reference; do not restate)

- **Interagency Guidance on Third-Party Relationships: Risk Management** (FRB / FDIC / OCC, June 2023; 88 Fed. Reg. 37920, June 9, 2023) [verify section labels]. https://www.federalreserve.gov/supervisionreg/srletters/sr2304.htm .
- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date].
- **Reg E — 12 CFR Part 1005**, especially §1005.6 (consumer liability), §1005.11 (procedures for resolving errors), and §1005.18 (prepaid accounts) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1005 .
- **NACHA Operating Rules (current edition)** Third-Party Sender risk management and ODFI obligations [verify rule citations and edition year]. Paywalled. https://www.nacha.org/ .
- **Bank Service Company Act, 12 USC §1867(c)** — examiner access to vendor systems sponsor banks rely on. https://www.law.cornell.edu/uscode/text/12/1867 .

#### Payments-fintech-control-area QA notes

##### Reg E error-resolution testing — QA scope items

- The QA reviewer reperforms a small subsample of the timeline (notice date, investigation start, provisional credit, final determination, customer notice) per sample item, confirms the evidence ID is present for each timeline event, and challenges any "investigation completed" entry without an evidence ID. Severity calibration on §1005.11(c) timing deviations is the most-challenged dimension; firm methodology floors are typically high.

##### Sponsor-bank end-customer reconciliation testing — QA scope items

- The QA reviewer confirms the workpaper documents the FBO account structure, the subledger reconciliation cadence, the threshold for breaks investigated, and the aging of unreconciled items. Reliance on sponsor-bank-supplied reconciliation evidence is an evidence-reliability dimension; the QA reviewer challenges whether the firm independently verified the sponsor's reconciliation posture.

##### Critical-vendor monitoring testing — QA scope items

- The QA reviewer confirms the workpaper's conclusion on critical-vendor monitoring is supported by evidence of the firm's KRI dashboard tie-out for that vendor, not just by the existence of a vendor-supplied SOC 2 report. Conclusion without dashboard tie-out is a recurring deficiency in examiner-prep sweeps.

##### Exit-plan testing — QA scope items

- The QA reviewer confirms exit-plan-testing workpapers carry tabletop evidence (date, scenario, participants by role, observations, action-item closure) and that absence of exit-plan testing is rated to firm methodology floor (typically high for critical vendors, with supervisory expectations under interagency TPRM aligned).

##### NACHA Third-Party Sender testing — QA scope items

- The QA reviewer confirms the workpaper named the NACHA edition tested against, that the Third-Party Sender risk-assessment evidence is documented per the named rule citation, and that reliance on the ODFI's separate testing is noted as a limitation rather than a substitute.

#### Audience and tone

A QA review note drafted for a sponsor-bank fintech-program workpaper reads heavier on the interagency TPRM frame, the end-customer reconciliation responsibility split, and the FBO subledger reconciliation evidence. A QA note drafted with an upcoming Federal Reserve targeted exam on third-party risk in mind reads heaviest on the population-level deficiency themes across the TPRM workpaper portfolio (vendor SOC 2 reliance, KRI dashboard tie-out, exit-plan testing severity calibration).
