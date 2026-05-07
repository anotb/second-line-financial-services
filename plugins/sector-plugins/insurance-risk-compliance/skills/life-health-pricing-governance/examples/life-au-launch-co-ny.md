# Example — life carrier launching accelerated underwriting using ECDIS in Colorado and New York

**Public-source-derived. No named institutions.**

## Scenario

A US life insurer is launching an accelerated-underwriting (AU) program for term-life products. The AU model uses third-party prescription-history data and a vendor-supplied ML-derived risk score. The program is going live in Colorado and New York first, with a planned national rollout. Second-line wants the pricing-governance file before the SERFF submissions and before AU goes live in either state.

## Source posture

Public-plus-firm-policy-plus-evidence. The carrier has supplied the actuarial memorandum, the model documentation, the vendor SOC 2, the data-source contracts, the consumer-disclosure draft, and the AIS Program draft.

## What the artifact carries

### Rate filing summary

Two SERFF filings (CO and NY). New product (term life) with the AU pathway as a manual-underwriting alternative. Effective date 90 days from filing acceptance.

### Rating factor map (Excel workbook)

Twelve rating factors. Three are ECDIS-derived (a prescription-history-derived flag, a vendor-supplied composite risk score, a public-records-derived flag). State-status columns for CO and NY show three factors with `requires-justification` posture under #880; the composite score has `requires-justification` in CO under SB 21-169 and `requires-justification` in NY under the Circular Letter.

### Unfair discrimination analysis

Per-factor under #880 plus a rating-plan-as-a-whole assessment. The composite score is the open question: actuarial-justification status is `partial` because the carrier has the vendor's bias-evaluation evidence but not the carrier-level validation against the carrier's own portfolio. The artifact names this as an open item, not a clearance.

### Disparate-impact red flags

CO regulation: the proxy-variable risk for the public-records-derived flag surfaces (the flag may correlate with race in some geographies). The carrier has a monitoring-metric plan but not yet baseline data. Open item.

NY DFS Circular Letter: consumer-recourse channel is named (a dedicated AU-decline line with a 10-business-day SLA and manual-underwriting-fallback path) but the disclosure timing for adverse-information is `[evidence-needed]` against the Circular Letter's expectation.

### AI / ML governance — AIS Program cross-walk

Six AIS Program elements `in-place`, two `partial`, one `gap`. The gap is third-party-AI accountability for the vendor: the contractual clauses are present but the monitoring evidence is not yet flowing.

### Documentation completeness vs SR 11-7-equivalent

Validation evidence is `partial`; the vendor's validation is documented but the carrier's own outcomes-analysis plan is dated within the last 30 days and has no observation period yet. Cite SR 11-7 as analogous.

### State DOI bulletin alignment

CO: SB 21-169 implementing regulation. Most prescriptive on ECDIS provenance and consumer-recourse for life-insurance underwriting.
NY: NY DFS Insurance Circular Letter (January 2024). Disclosure and consumer-recourse expectations.

### Privacy and consumer-disclosure posture

HIPAA: the prescription-history data flows through a HIPAA business-associate chain; BAA on file. Minimum-necessary analysis is `partial`; the data set includes therapeutic categories that are not all underwriting-relevant. Open item.

ECDIS: consumer-recourse channel named (above); adverse-information-disclosure posture `[evidence-needed]` (above).

### Recommended disposition

`Remediate-then-re-review`. Three named gaps: (1) carrier-level outcomes analysis on the vendor composite score; (2) baseline monitoring data on the proxy-variable risk; (3) adverse-information-disclosure posture under NY DFS Circular Letter. AU launch held until remediation.

## Public sources used

- NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023).
- NAIC Unfair Trade Practices Act, Model #880.
- Colorado SB 21-169 implementing regulation.
- NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024).
- HIPAA Privacy Rule, 45 CFR Part 164 Subpart E.
- SR 11-7 (cited as analogous model-risk expectation language).
