# Sector overlay: capital markets

Loaded when `scope.sector_overlay_set` includes capital-markets. Carries the broker-dealer and investment-adviser-specific frame for foundation-model evidence-pack review: SEC and FINRA visibility, surveillance and execution adjacency, books-and-records and Marketing Rule reach into AI-generated content.

## Supervisory frame

Capital-markets entities are dual-supervised in different combinations: broker-dealers by FINRA and SEC, registered investment advisers by SEC (or state for sub-threshold), exchanges and ATSs by SEC, swap dealers by CFTC, FCMs and IBs by NFA and CFTC. The evidence-pack review is read against the supervisory constellation the scope identifies.

The SEC's published staff statements and risk alerts on AI use by registrants set the practical supervisory expectation in this scope: AI used in advisory, broker-dealer, surveillance, or fund-management functions falls within existing supervisory frameworks (Investment Advisers Act, Securities Exchange Act, Investment Company Act) and the related rules. There is, as of this skill's authoring, no SEC AI-specific final rule; published proposals and staff guidance are watched and tracked in `references/source-anchors.md`.

For investment advisers, the Marketing Rule (17 CFR 275.206(4)-1) and Books and Records Rule (17 CFR 275.204-2) reach into AI-generated client-facing content; vendor evidence on output-control posture and refusal behaviour around marketing-relevant outputs feeds the firm's compliance assessment. For broker-dealers, FINRA Rule 3110 supervision and Rule 2210 communications-with-the-public obligations carry the analogous lens.

For any AI use in surveillance, trade execution, or order-handling, FINRA Rule 3110 supervision expectations and SEC Rule 15c3-5 (market access rule) carry direct relevance; the evidence-pack review supports the firm's assessment of whether vendor evidence is sufficient for a use case within those rules' scope.

For investment companies (mutual funds, ETFs, closed-end funds), the fund board's oversight of service providers under the Investment Company Act and Rule 38a-1 compliance programme touches vendor-AI considerations; fund-board visibility and reporting cadence are relevant for fund-touching deployments.

## Sector-specific evidence asks

The capital-markets-vendor frame surfaces the following beyond the cross-cutting baseline:

- **Output-control evidence for marketing-relevant uses.** Where the foundation-model deployment produces or assists with content that may be subject to the Marketing Rule (for advisers) or Rule 2210 (for broker-dealers), the evidence pack should establish the vendor's output-control posture: refusal behaviour around performance claims, testimonial-handling, recommendation language. The firm's compliance function performs the regulatory-fit assessment; the evidence-pack review surfaces the inputs.

- **Surveillance and supervision adjacency.** Where the foundation model is consumed in or alongside surveillance systems (trade surveillance, communication surveillance, AML transaction monitoring), the evidence pack should establish the vendor's posture on output stability, false-positive and false-negative profile awareness, and explanation depth sufficient to support supervisory review under Rule 3110 or analogous frameworks. Record the gaps.

- **Books-and-records preservation reach.** AI-generated content used in regulated communications must be preserved per Rule 17a-4 (broker-dealers) or Rule 204-2 (advisers). The vendor's data-retention posture matters not only for privacy but for the firm's ability to meet preservation obligations. Where vendor default is short-window retention, the firm-side capture-and-preserve pattern carries the obligation; record the architecture in the evidence-pack review.

- **Fiduciary-lens framing for adviser-side use.** For investment advisers, the foundation-model deployment is read against the adviser's fiduciary duty (duty of care, duty of loyalty). Vendor evidence on output reliability and known failure modes feeds the firm's fiduciary-fit assessment; the firm's CCO carries the assessment, but the evidence-pack review surfaces the inputs.

- **Trading-system adjacency posture.** For deployments adjacent to order-handling or execution (smart-order-routing assist, pre-trade compliance assist), the evidence pack should establish the vendor's awareness of latency, determinism, and failure-mode requirements that pure-text-summarisation use cases do not impose. Where the vendor's model card or evaluation report is silent on these dimensions, record the gap and route the in-firm requirement-fit assessment to `validation-plan`.

- **Cross-border and reciprocity considerations.** For dual-registered entities (US adviser plus UK FCA, EU firms with passporting, APAC affiliates), the binding regulator constellation is layered. Loaded with this overlay; the cross-cutting privacy overlay carries the data-flow specifics.

## Sector-specific co-reviewer expectations

The CCO is a co-reviewer for any deployment touching marketing, communications, or recommendation-relevant outputs. For broker-dealer entities, the CSO or named supervisory principal under FINRA Rule 3110 is informed where the use case touches surveillance or supervision. For fund-touching deployments, the fund board's CCO under Rule 38a-1 receives the evidence-pack review summary as part of the periodic compliance reporting cycle (not as a primary attestation). The AI Governance Lead retains the lead attestation; the named function-level co-attests are recorded in `reviewer_attestation`.

## Sector-specific re-review triggers

In addition to the baseline triggers, capital-markets adds:

- SEC, FINRA, or CFTC enforcement action or risk alert referencing the vendor, vendor class, or use-case class.
- Final rule or amendment to AI-relevant adviser or broker-dealer rules (Marketing Rule, Rule 2210, supervision rules).
- Material change in the use case scope towards execution-adjacent or surveillance-adjacent deployment.
- Fund-board feedback on the deployment for fund-touching use cases.

## Sector-specific structured-output additions

The `sector_overlay_notes` block in the schema carries the capital-markets-specific findings:

```
"sector_overlay_notes": {
  "registration_constellation": [...],
  "marketing_rule_or_2210_reach": "...",
  "supervision_and_surveillance_adjacency": "...",
  "books_and_records_preservation_posture": "...",
  "fiduciary_lens_summary": "...",
  "trading_system_adjacency_posture": "..."
}
```
