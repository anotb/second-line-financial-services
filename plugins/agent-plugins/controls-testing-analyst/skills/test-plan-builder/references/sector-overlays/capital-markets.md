# Capital-markets sector overlay — test-plan-builder

Loaded when `engagement-scope.sector_overlay_set` includes `capital-markets` or when the test addresses SEC, FINRA, NFA, or fund-board rules. Supplements `references/source-anchors.md`.

## Test-plan conventions SEC and FINRA examiners expect

SEC Division of Examinations staff and FINRA examiners read CCO and supervisory-control test plans against compliance-program rule frames rather than safety-and-soundness frames. Three conventions matter:

- **Annual review framing carries the test plan.** Investment Advisers Act Rule 206(4)-7 and Investment Company Act Rule 38a-1(a)(4) are written around an annual review; test plans feed the annual review compendium. The plan restates the annual-review-period framing and identifies which annual-review element it covers.
- **Supervisory testing maps to FINRA 3120 and 3130.** Broker-dealer compliance test plans feed the FINRA 3120 supervisory-controls report and the FINRA 3130 CEO certification. The plan identifies which 3120 testing area the cycle covers and the certification cycle the test feeds.
- **Recordkeeping evidence treatment is regulated.** SEC Rule 17a-4 and FINRA Rule 4511 govern format, retention, and accessibility of the records the plan relies on. The plan does not invent a recordkeeping convention; it relies on the firm's records-management posture and notes any deficiency in evidence accessibility as a planning constraint distinct from the substantive test.

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
- **SEC Regulation Systems Compliance and Integrity (Reg SCI), 17 CFR §§242.1000-242.1007** [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-242 .

## Capital-markets-control-area test-plan notes

### Adviser annual compliance review (206(4)-7)

- Test-plan conventions: criteria section cites the firm's compliance manual section under test plus the corresponding Advisers Act rule; population is the activity in the named compliance area for the annual-review period; design procedures cover the policy-and-procedure adequacy review; operating procedures cover sample-based reperformance against the policy clock or the rule's substantive requirement.

### Fund compliance program (38a-1)

- Test-plan conventions: 38a-1(a)(4) requires the fund to obtain certification from each material service provider that they have adopted and implemented compliance policies reasonably designed to prevent violations of federal securities laws. Test plans for service-provider adequacy carry service-provider attestation, on-site or remote diligence evidence, and any examination findings the service provider has disclosed. Cross-link to `vendor-diligence` and `dora-register-builder` (where DORA also applies).

### Supervisory testing (FINRA 3110 / 3120 / 3130)

- Test-plan conventions: each tested supervisory procedure ties to a 3110 or 3120 area; the plan aggregation feeds the 3120 annual report; the firm's CEO certification under 3130 is the downstream consumer named in the plan.

### Marketing rule (206(4)-1)

- Test-plan conventions: criteria section names the disseminated advertisement (cited by ad ID and date), the supporting evidence for performance claims and case studies, the Marketing Rule disclosures, and the firm's review-and-approval evidence. Testimonial and endorsement test plans cover compensation arrangements and required disclosures by sample.

### Custody rule (206(4)-2)

- Test-plan conventions: custody test plans reconcile client-account positions and transactions against qualified-custodian records by sample; surprise-examination evidence is referenced by ID with the surprise-examiner's report carried as third-party-assurance evidence; sole authority over a private fund triggers audit-or-surprise-exam testing of the audit pathway.

### Trade surveillance (best execution, market manipulation, manipulative-trading)

- Test-plan conventions: surveillance-alert test plans cover alert disposition by sample, with the alert criteria, the case file, and the disposition rationale named as expected evidence. Trade-reconstruction test plans cover the order-execution timeline by sample with NMS or fixed-income market-data references.

### Reg SCI testing (where applicable)

- Test-plan conventions: SCI-system test plans cover the SCI policies and procedures, the SCI-system inventory, the SCI-event reporting evidence, and the SCI-event business-continuity testing per §242.1003 [verify subsection labels].

## Reg S-P safeguards testing

- Reg S-P (as amended May 16, 2024) imposes incident-response, customer-notification, and service-provider-oversight obligations on broker-dealers, advisers, and investment companies [verify exact compliance dates by entity type]. Test-plan conventions: customer-notification timing test plans cite the regulatory clock; service-provider-oversight test plans cite the rule's diligence and ongoing-monitoring standards.

## Audience and tone

A test plan drafted with an upcoming SEC Division of Examinations exam in mind reads heavier on annual-review framing, marketing-rule supporting evidence, and custody-rule reconciliations. A plan drafted for FINRA cycle exam preparation reads heavier on 3120 supervisory testing, 3110 supervisory-procedure design evidence, and Rule 4511 recordkeeping posture. A fund-board-facing plan reads heavier on 38a-1(a)(4) service-provider compliance-program-adequacy evidence with the fund-board reporting cycle as the deliverable consumer.
