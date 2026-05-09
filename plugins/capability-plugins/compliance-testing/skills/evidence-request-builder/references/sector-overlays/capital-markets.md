# Capital-markets sector overlay — evidence-request-builder

Loaded when `scope.sector_overlay_set` includes `capital-markets` or when the test addresses FINRA, SEC, NFA, MSRB, or exchange rules. Supplements `references/source-anchors.md`.

## Request-list conventions capital-markets testing programs apply

Broker-dealer, investment adviser, and asset-management testing PBC lists carry conventions distinct from bank consumer-compliance:

- **Order-blotter pulls are recordkeeping evidence, not transaction reports.** Order blotters under SEC Rule 17a-3 / 17a-4 and FINRA Rule 4511 are the source-of-record for order events. Requests for order-blotter extracts cite the rule and name the format the recordkeeping rule preserves (non-rewriteable form, audit-trail intact). Cite the rule rather than restating the recordkeeping format requirements.
- **Communications-supervision evidence carries an archive scope.** FINRA Rule 3110(b)(4) communications-review evidence requests cite the firm's communications archive (Smarsh, Global Relay, Bloomberg Vault, or named equivalent), the channel scope (email, IM, social media, voice where retained), and the supervisory-review-evidence format (review-completion log per supervisor, sample of reviewed items per supervisor).
- **Trade-surveillance evidence carries the surveillance-platform scope and the alert-disposition log.** Trade-surveillance testing requests the alert log per sample (alert ID, alert reason, surveillance rule fired, disposition rationale, disposer role, disposition date) plus the underlying order-event evidence per alerted order.
- **Adviser compliance-program evidence draws the annual-review file under Rule 206(4)-7.** The annual review under Rule 206(4)-7 is itself a workpaper; testing the annual-review process requests the annual-review file (scope memo, testing performed, findings, remediation tracking).
- **Books-and-records request format respects the recordkeeping rule.** Broker-dealer record requests respect SEC Rule 17a-4 preservation requirements; the format requested reflects the firm's recordkeeping practice (PDF copies acceptable for second-line testing; the underlying preservation in non-rewriteable form is the firm's compliance posture, not the testing posture).

## Capital-markets-supervisory anchors (load by reference; do not restate)

- **FINRA Rule 3110 — Supervision** [verify subsection labels including §3110(a) supervisory system, §3110(b) written supervisory procedures, §3110(c) internal inspections, §3110(d) transaction review and investigation, §3110(e) qualifications of supervisors]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3110 .
- **FINRA Rule 3120 — Supervisory Control System** [verify subsection labels]. Annual report on supervisory controls. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3120 .
- **FINRA Rule 3130 — Annual Certification of Compliance and Supervisory Processes** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3130 .
- **SEC Rule 17a-3 (17 CFR §240.17a-3)** — broker-dealer recordkeeping (records to be made). https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-3 .
- **SEC Rule 17a-4 (17 CFR §240.17a-4)** — broker-dealer recordkeeping (records to be preserved). https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-4 .
- **FINRA Rule 4511 — General Requirements (Books and Records)** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/4511 .
- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 .
- **Investment Advisers Act Rule 204-2** — adviser books and records [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.204-2 .
- **SEC Marketing Rule (Rule 206(4)-1)** [verify subsection labels including testimonials, endorsements, and performance advertising provisions]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 .
- **SEC Regulation Best Interest (17 CFR §240.15l-1)** [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.15l-1 .
- **SEC Reg SCI (17 CFR §§242.1000-242.1007)** for SCI entities [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-242 .

## Capital-markets-control-area request notes

### Communications-supervision testing (FINRA 3110(b)(4))

- Request conventions: communications-archive extract for the sampled supervisor-period (channel, message ID, sender, recipients, date, content) from the firm's archive (Smarsh, Global Relay, Bloomberg Vault, or named equivalent). Per-supervisor review-completion log with sample items reviewed and the review-evidence (lexicon-hit disposition, escalation evidence where applicable). Reliance test note covers the archive's completeness against the messaging platform.

### Trade-surveillance testing

- Request conventions: alert log CSV for the sampled period per surveillance rule fired (alert ID, alert reason, fired rule, disposition rationale, disposer role, disposition date). Underlying order-event extract per alerted order (order entry, modification, execution, cancellation events with times). Surveillance-rule configuration extract for the period. Reliance test note distinguishes alert-disposition from supervisory-rule-tuning evidence.

### Books-and-records testing (17a-3, 17a-4, 4511)

- Request conventions: per-sample record retrieval from the firm's preservation system (order tickets, customer-account documents, communications, supervisory records). Format respects the recordkeeping rule's preservation form; the request asks for a copy in PDF or system-export and the preservation format itself is evidenced separately by a recordkeeping-system attestation.

### Adviser annual-review testing (206(4)-7)

- Request conventions: annual-review file from the firm's CCO (scope memo, testing performed by topic, findings register, remediation tracking, board or governance committee report). The annual review is itself a workpaper; the request asks for the annual-review file rather than evidencing the underlying activity for the second-line test.

### Marketing-rule testing (206(4)-1)

- Request conventions: marketing-materials register CSV for the period with material ID, channel, intended audience, period live, and the supervisory-review evidence per material; per-sample material PDF; performance-advertising supporting evidence (calculation methodology, GIPS-compliance evidence where claimed, fee-and-expense net-or-gross posture). Testimonials and endorsements draw the disclosure evidence and the compensation arrangement evidence per Rule 206(4)-1 [verify subsection].

### Supervisory-controls and annual-certification testing (3120, 3130)

- Request conventions: 3120 supervisory-controls report for the most recent year with supporting tests-and-verifications evidence. 3130 CEO certification with the underlying CCO testing-of-supervisory-processes evidence. The request list draws the certification cycle and the supporting tests; the testing this list serves is one input to the next 3130 cycle.

### Reg SCI testing (where the firm is an SCI entity)

- Request conventions: SCI systems inventory; SCI-event log for the period with materiality-determination evidence; quarterly material-systems-changes report; annual SCI review; business-continuity / disaster-recovery testing evidence. SCI evidence is connector-aware where the firm has automated SCI inventory and event-management systems.

## Audience and tone

A request list drafted ahead of an upcoming SEC OCIE / Examinations Division exam reads aligned to the SEC examination request-list shape (which the SEC publishes in its sample exam request-letter materials). A request list drafted ahead of a FINRA cycle exam reads aligned to FINRA's request-letter conventions. A request list for the firm's internal CCO-led periodic testing reads operationally with the same evidence shape; the methodology bar is the same, only the rendering audience changes.
