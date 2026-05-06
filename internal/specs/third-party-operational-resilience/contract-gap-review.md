# contract-gap-review — Phase 1 spec sheet

Plugin: `third-party-operational-resilience`
Phase: 1 (per-skill scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Activation-tuned description

```
Reviews a third-party contract or master services agreement against named regulatory clause-coverage expectations and produces a clause-by-clause gap memo with proposed amendments and reviewer questions for legal and second-line.

Best for:
- A new vendor contract is in negotiation and the firm needs the second-line clause-coverage view before legal redlines.
- Renewal or assignment of an existing contract triggers a refresh against current regulatory expectations.
- A DORA preparation cycle requires evidence that critical-or-important-function ICT contracts meet Article 30 contractual provisions.

Not the right tool when:
- The criticality tier has not been set (use criticality-assessment first; the depth of clause review depends on tier).
- The work is the full diligence pack, not the contract layer (use vendor-diligence).
- The work is exit and termination logistics rather than clause coverage (use exit-plan).

Anchored to: Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023) §IV contract negotiation [verify section]; OCC Bulletin 2013-29 contract issues [verify section]; FFIEC IT Handbook — Outsourcing Technology Services contract section [verify section]; DORA Article 30 (key contractual provisions); EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02) §13 contractual phase [verify section]; NYDFS 23 NYCRR 500.11 third-party contractual expectations.
```

## Source anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 6, 2023). Contract-negotiation section enumerates expected clauses: scope and performance, responsibilities for compliance with applicable laws, audit and reporting rights, ownership and licenses, business resumption and contingency, subcontracting, confidentiality and information security, indemnification, limits on liability, insurance, dispute resolution, default and termination, regulatory access [verify section letter].
- OCC Bulletin 2013-29 — contract-issues section as the predecessor framing (still cited).
- FFIEC IT Examination Handbook — Outsourcing Technology Services booklet, contract-issues section [verify section]. SLA, performance reporting, problem reporting, regulatory examiner access.
- DORA — Regulation (EU) 2022/2554, Article 30 mandatory contractual provisions for ICT services. For critical-or-important-function arrangements, Article 30(2) and 30(3) impose enhanced clauses [verify subarticle]. Termination triggers Article 28(7) [verify].
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02). Written outsourcing agreement guideline [verify section number]; rights of access, information, and audit; sub-outsourcing; termination; data location; cooperation with competent authorities.
- NYDFS Part 500 — 23 NYCRR 500.11 expectations for third-party security policies and contractual safeguards (multi-factor authentication, encryption, notification of cybersecurity events, access controls, representations and warranties).
- For SaaS and cloud arrangements: FFIEC Joint Statement on Risk Management of Cloud Services (April 2020) for shared-responsibility-model contractual expectations.

## Sector overlays needed

- `references/sector-overlays/banking.md` — interagency contract clauses; OCC 12 CFR Part 30 Appendix B (interagency guidelines for safeguarding customer information) cross-references; large-bank heightened standards on third-party contracts.
- `references/sector-overlays/insurance.md` — NAIC Model Law on outsourcing — required contract provisions; state department of insurance contract-content requirements; Form D filings for affiliate agreements.
- `references/sector-overlays/capital-markets.md` — Reg SCI vendor-contract expectations for SCI entities; FINRA contract-management notices; SEC books-and-records (17a-3, 17a-4) impact on retention clauses; CFTC books-and-records.
- `references/sector-overlays/payments-fintech.md` — NACHA originator-agreement requirements; card-network contract requirements; banking-as-a-service partner contract clauses (settlement, BSA/AML, customer liability).

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — NYDFS 500.11 contract clauses; SEC cyber-disclosure rule clause implications (vendor incident-notification timing must align with the firm's Item 1.05 8-K determination window); FFIEC IT Handbook Information Security Booklet expectations on third-party security; SOC 2 audit-rights clauses; vulnerability-management and pen-test rights.
- `references/cross-cutting/privacy.md` — GLBA Safeguards Rule 16 CFR 314.4(f) service-provider oversight contractual requirements; state-privacy-law data-processing-agreement expectations (CCPA/CPRA service-provider clause; VCDPA processor contract); HIPAA business-associate agreement content where in scope.

## Output template named sections

`templates/default-output.md`:

1. Arrangement and contract identifiers
2. Criticality input (from `criticality-assessment`)
3. Applicable regimes and clause-coverage matrix
4. Clause-by-clause findings (each row: clause topic, source criterion with section ref, contract reference, present/partial/absent, gap rationale, recommended amendment language posture, severity)
5. Mandatory clauses for critical or important function (DORA Article 30(2)/(3)) if in scope
6. Cyber clauses (notification windows, incident cooperation, audit rights, encryption-at-rest and -in-transit)
7. Privacy clauses (data-processing agreement coverage, sub-processor flow-down, deletion and return)
8. Subcontracting and fourth-party clauses
9. Termination, exit, and assignment clauses
10. Liability, indemnity, and insurance clauses
11. Audit, reporting, and regulator-access clauses
12. Open questions for legal and the contract owner
13. Reviewer questions
14. Source trace and confidence label

## Structured output fields

Anchor: `schemas/vendor.schema.json` `contract_gap_summary` field (string) is the current rollup; the structured per-clause artifact is produced as an array.

Per-clause record (type, purpose):

- `clause_id` (string)
- `clause_topic` (string) — e.g., "Subcontracting", "Cybersecurity event notification", "Audit rights"
- `source_criterion` (object: `regime`, `citation`, `section`, `date`) — the named regulatory expectation
- `contract_reference` (string) — section/clause number in the contract
- `coverage` (enum: `present | partial | absent | not-applicable`)
- `gap_rationale` (string)
- `recommended_amendment_posture` (string) — high-level redline posture, not legal language
- `severity` (enum: `low | medium | high`)

Top-level rollup:

- `arrangement_id` (string)
- `contract_identifier` (string) — MSA/SOW reference
- `criticality_input` (enum) — from `criticality-assessment`
- `dora_in_scope` (boolean)
- `clauses` (array of clause records)
- `summary_severity` (enum)
- `reviewer_questions` (array of string)
- `confidence_label` (enum)
- `source_trace` (array of object)

## Example scenarios (two, public-source-derived)

1. **Cloud IaaS contract for a regional US bank.** Inputs: the master agreement, the order form, and the firm's criticality output (critical). Anchored to: interagency guidance (June 2023) contract-negotiation section; FFIEC IT Handbook contract section; FFIEC cloud joint statement (April 2020); NYDFS 500.11. The output identifies that the audit-rights clause defaults to "the report we publish", the cybersecurity-event-notification window is set to "within a reasonable period" (gap against NYDFS 500.17(a) 72-hour expectation [verify subsection]), and the sub-region change clause does not require firm consent (gap against the firm's data-residency requirements). Recommended-amendment posture is captured per clause; legal review is flagged.

2. **DORA-in-scope SaaS contract for an EU subsidiary's collections platform.** Inputs: the contract, the criticality output (important; DORA critical-or-important-function = yes). Anchored to: DORA Article 30(2) and 30(3) [verify subarticle]; EBA outsourcing guidelines [verify section]; NAIC outsourcing model for the parent insurer's other obligations. The output identifies that the contract is missing several Article 30(2)/(3) mandatory provisions: termination rights tied to supervisory recommendation, full description of services, locations of data processing, sub-outsourcing notification timing, exit-strategy and transitional support. Severity high; legal redlines required before signature.

## Common pitfalls

1. **Reviewing the contract without knowing the criticality.** Clause depth and the DORA Article 30 layer depend on tier and DORA-in-scope. Pull the criticality output first.
2. **Treating "industry standard" SLA language as sufficient.** Industry-standard often means below the firm's tolerance. Compare against the criticality output's RTO/RPO tolerance, not the vendor's default.
3. **Missing the cybersecurity-event-notification window mismatch.** SEC cyber-disclosure determinations and NYDFS 500.17 each impose their own clocks. Flag the contract notification window against the tightest applicable clock.
4. **Accepting "right to audit subject to reasonable cooperation" as audit rights.** This is a reservation of the vendor's discretion. Audit rights need scope, frequency, cost-allocation, and a path when the auditor's findings dispute vendor representations.
5. **Treating sub-processor flow-down as visibility.** Flow-down is a contractual mechanic. The contract should also require sub-processor identification, change notification, and rejection rights.
6. **Skipping exit-and-transition clauses for a "non-critical" arrangement.** Even non-critical arrangements need basic data-return and deletion clauses for privacy compliance. Do not gate exit clauses entirely on criticality.
7. **Confusing limit-of-liability caps with risk transfer.** A liability cap below the firm's expected loss is a finding, not a deal-closer. Surface it.
