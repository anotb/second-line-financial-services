# Capital-markets sector overlay — qa-workpaper

Loaded when `scope.sector_overlay_set` includes `capital-markets` or when the QA review covers a workpaper at a broker-dealer, investment adviser, or registered fund. Supplements `references/source-anchors.md`.

## QA conventions for capital-markets testing workpapers

Capital-markets second-line testing workpapers carry methodology distinct from bank consumer-compliance testing:

- **FINRA 3120 / 3130 supervisory-controls testing supports CEO certification.** Broker-dealer CCO testing of supervisory processes feeds the FINRA Rule 3130 annual CEO certification. The QA reviewer challenges whether the workpaper's documentation supports the certification posture, not just the testing-program posture; severity calibration on supervisory-controls deficiencies carries certification-language implications.
- **Rule 206(4)-7 adviser-compliance-program annual review.** The Rule 206(4)-7 annual review is itself a self-test; QA over the annual-review workpapers is the review-of-the-review. SEC examiner expectations on the documentation underlying the annual review are explicit in published Division of Examinations risk alerts; the QA reviewer carries that posture.
- **Conclusion language hygiene is structurally important.** Capital-markets enforcement environment makes legal-violation framing in workpaper conclusions particularly costly: a workpaper concluding "the firm violated [Rule X]" can be discoverable and used adversely. The QA reviewer rewrites to control-effectiveness language and routes the legal question to legal counsel separately.
- **Recordkeeping evidence reliance.** SEC Rule 17a-4 and FINRA Rule 4511 govern the recordkeeping the workpaper relies on. The QA reviewer confirms the workpaper named the source system, the recordkeeping-rule applicable to that record class, and the retention posture; reliance on a record that has aged out of retention is an evidence-reliability finding.

## Capital-markets-supervisory anchors (load by reference; do not restate)

- **FINRA Rule 3120 — Supervisory Control System** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3120 .
- **FINRA Rule 3130 — Annual Certification of Compliance and Supervisory Processes** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3130 .
- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule, including annual review documentation expectations [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 .
- **SEC Rule 17a-4 (17 CFR §240.17a-4) — Records to be Preserved by Certain Exchange Members, Brokers, and Dealers** [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-4 .
- **FINRA Rule 4511 — General Requirements (Books and Records)** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/4511 .
- **SEC Division of Examinations risk alerts on adviser compliance-program documentation** (current alerts) [verify alert IDs and dates]. https://www.sec.gov/exams .

## Capital-markets-control-area QA notes

### FINRA 3120 supervisory-controls testing — QA scope items

- The QA reviewer confirms the workpaper's annual report on supervisory controls covers the required tests and verifications, that the documented review of those tests names the reviewer role separate from the tester, and that the report's conclusions on supervisory-control effectiveness do not drift into rule-violation framing.

### Rule 206(4)-7 annual review — QA scope items

- The QA reviewer confirms the annual-review workpaper documents the methodology, the testing performed, the deficiencies identified, the remediation tracked, and the CCO's involvement. SEC Division of Examinations risk alerts have repeatedly cited annual-review workpapers that document only the conclusion without the methodology underneath; the QA reviewer pushes back on conclusion-only documentation.

### Trade-surveillance and best-execution testing — QA scope items

- The QA reviewer confirms the trade-surveillance testing workpaper documents the alert-population definition, the disposition sample, and the timeline reperformance from alert to disposition with the surveillance-rule reference. Best-execution testing carries the venue-analysis methodology; the QA reviewer challenges whether the venue-analysis reperformance reads against the firm's best-execution policy effective during the period.

### Recordkeeping testing — QA scope items

- The QA reviewer challenges reliance on records that have aged out of retention; reliance on archived emails reconstructed from backups (rather than the original WORM-compliant archive); and reliance on text-message records where the firm's archiving posture for off-channel communications is incomplete.

## Audience and tone

A QA review note drafted for a broker-dealer workpaper reads heavier on the FINRA 3120 / 3130 certification-support posture; for an adviser workpaper, heavier on the Rule 206(4)-7 annual-review documentation posture. The conclusion-language hygiene posture is heaviest in capital-markets QA notes because of the enforcement environment; the QA reviewer's rewrite of legal-violation framing to control-effectiveness language is a recurring intervention.
