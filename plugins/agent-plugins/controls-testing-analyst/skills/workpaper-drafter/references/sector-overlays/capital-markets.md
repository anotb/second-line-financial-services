# Capital-markets sector overlay — workpaper-drafter

Loaded when `engagement-scope.sector_overlay_set` includes `capital-markets` or when the test addresses SEC, FINRA, NFA, or fund-board rules. Supplements `references/source-anchors.md`.

## Workpaper conventions SEC and FINRA examiners expect

SEC Division of Examinations staff and FINRA examiners read CCO and supervisory-control testing workpapers against compliance-program rule frames rather than safety-and-soundness frames. Three conventions matter:

- **Annual review evidence carries the testing workpaper.** Investment Advisers Act Rule 206(4)-7 and Investment Company Act Rule 38a-1(a)(4) are written around an annual review; testing workpapers feed the annual review compendium. The workpaper restates the annual-review-period framing.
- **Supervisory testing is the FINRA 3120 / 3130 anchor.** Broker-dealer compliance testing workpapers feed the FINRA 3120 supervisory-controls report and the FINRA 3130 CEO certification. The workpaper identifies which 3120 testing area it covers and the certification cycle.
- **Recordkeeping evidence treatment is regulated.** SEC Rule 17a-4 and FINRA Rule 4511 govern format, retention, and accessibility of the records the workpaper relies on. The workpaper does not invent a recordkeeping convention; it relies on the firm's records-management posture and notes any deficiency in evidence accessibility as a control finding distinct from the substantive test.

## Capital-markets-supervisory anchors (load by reference; do not restate)

- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 .
- **Investment Company Act Rule 38a-1(a)(4)** — fund compliance-program rule, including service-provider compliance-program-adequacy assessment [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-270/section-270.38a-1 .
- **FINRA Rule 3110 — Supervision** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3110 .
- **FINRA Rule 3120 — Supervisory Control System** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3120 .
- **FINRA Rule 3130 — Annual Certification of Compliance and Supervisory Processes** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3130 .
- **SEC Rule 17a-4** — broker-dealer recordkeeping [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-4 .
- **FINRA Rule 4511 — General Books and Records Requirements** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/4511 .
- **Investment Advisers Act Rule 206(4)-2 (Custody Rule)** [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-2 .
- **Investment Advisers Act Rule 206(4)-1 (Marketing Rule)** [verify subsection labels for advertisement testing]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 .
- **17 CFR Part 248 (Reg S-P) as amended May 16, 2024** [verify exact compliance dates by entity type and size]. https://www.sec.gov/files/rules/final/2024/34-100155.pdf [verify URL].

## Capital-markets-control-area workpaper notes

### Adviser annual compliance review (206(4)-7)

- Workpaper conventions: annual-review testing covers each named compliance area in the firm's compliance manual; the workpaper aggregation reads observed deviation against the firm's compliance-policy tolerance and against the regulatory minimum where prescribed. The annual-review summary is itself a separate artifact (firm-side compliance report); the testing workpaper feeds it.

### Fund compliance program (38a-1)

- Workpaper conventions: 38a-1(a)(4) requires the fund to obtain certification from each material service provider that they have adopted and implemented compliance policies reasonably designed to prevent violations of federal securities laws. Workpaper testing of service-provider adequacy reads service-provider attestation, on-site or remote diligence, and any examination findings the service provider has disclosed. Cross-link to `vendor-diligence` and `dora-register-builder` (where DORA also applies).

### Supervisory testing (FINRA 3110 / 3120 / 3130)

- Workpaper conventions: supervisory testing is the firm-side compendium of FINRA-required testing. Each tested supervisory procedure ties to a 3110 or 3120 area. The workpaper aggregation feeds the 3120 annual report; the firm's CEO certification under 3130 is the downstream consumer.

### Marketing rule (206(4)-1)

- Workpaper conventions: advertisement testing reads the disseminated advertisement (cited by ad ID and date), the supporting evidence for performance claims and case studies, the Marketing Rule disclosures, and the firm's review-and-approval evidence. Testimonial and endorsement testing covers compensation arrangements and required disclosures by sample.

### Custody rule (206(4)-2)

- Workpaper conventions: custody testing reconciles client-account positions and transactions against qualified-custodian records by sample; surprise-examination evidence is referenced by ID, with the surprise-examiner's report carried as third-party-assurance evidence; sole authority over a private fund triggers audit-or-surprise-exam testing of the audit pathway.

### Trade surveillance (best execution, market manipulation, manipulative-trading)

- Workpaper conventions: surveillance-alert testing reads alert disposition by sample, with the alert criteria, the case file, and the disposition rationale carried as evidence. Trade-reconstruction testing reads the order-execution timeline by sample with NMS or fixed-income market-data references.

## Reg S-P safeguards testing

- Reg S-P (as amended May 16, 2024) imposes incident-response, customer-notification, and service-provider-oversight obligations on broker-dealers, advisers, and investment companies [verify exact compliance dates by entity type]. Workpaper conventions: customer-notification timing testing reads the incident timeline against the regulatory clock; service-provider-oversight testing reads diligence and ongoing-monitoring evidence per the rule's standards.

## Audience and tone

A workpaper drafted with an upcoming SEC Division of Examinations exam in mind reads heavier on annual-review evidence, marketing-rule supporting evidence, and custody-rule reconciliations. A workpaper drafted for FINRA cycle exam preparation reads heavier on 3120 supervisory testing, 3110 supervisory-procedure design evidence, and Rule 4511 recordkeeping posture. A fund-board-facing workpaper reads heavier on 38a-1(a)(4) service-provider compliance-program-adequacy evidence with the fund-board reporting cycle as the deliverable consumer.
