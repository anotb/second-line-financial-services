# Troubleshooting — contract-gap-review

Recurring pitfalls. Read before producing the gap matrix and again before sign-off.

## Reading the contract

### Treating "right to audit subject to reasonable cooperation" as audit rights

Reservation of vendor discretion. Audit rights need scope, frequency, cost-allocation, on-site posture, third-party-auditor acceptability, and a remedy when auditor findings dispute vendor representations. Mark `partial` and surface the missing components as a single row, not as five rows that all read "absent".

### Treating "industry-standard SLA" as sufficient

Industry-standard often means below the firm's tolerance. Compare against the criticality output's RTO and RPO tolerance, not the vendor's default. Mark `partial` and recommend tightening to the firm's tolerance band.

### Missing the cybersecurity-event-notification clock mismatch

The contract clock must close upstream of the tightest applicable regulatory clock: the firm's public-company materiality determination window where listed; the New York State 72-hour cybersecurity-event-notification clock where the firm is a covered entity; the EU digital-operational-resilience-act major-ICT-related-incident reporting timetable where in scope; the GLBA Safeguards 30-day customer-notice clock where amended 314 reaches; the HIPAA 60-day breach-notification clock where PHI is in scope. Always a finding for a vendor touching NPI, PHI, PCI, or IBS controls.

### Treating sub-processor flow-down as visibility

Flow-down is a contractual mechanic. The contract must also require sub-processor identification (current list, not just "available on request"), change-notification with timing, and rejection rights. These are separate rows.

### Skipping exit-and-transition clauses for a "non-critical" arrangement

Even non-critical arrangements need basic data-return and deletion clauses for privacy compliance. Do not gate exit clauses entirely on criticality; gate the depth.

### Confusing limit-of-liability caps with risk transfer

A liability cap below the firm's expected loss is a finding, not a deal-closer. Surface the cap-below-expected-loss flag and require risk-acceptance documentation. The matrix does not gate the contract on this row alone.

### Missing the regulator-examination-access continuity clause

For banking arrangements, the Bank Service Company Act §1867(c) reach must be unconditional and must survive termination through the records-retention period. A regulator-access clause conditioned on prior notice or on the vendor's process is a `partial` finding and a `high`-severity row.

## Mandatory-clause overlay

### Skipping the overlay because the firm taxonomy says "important", not "critical"

The EU digital-operational-resilience-act in-scope flag is a function classification (critical-or-important-function ICT service), not the firm's internal criticality tier. An "important"-tier vendor under the firm's taxonomy can be in scope of the act; the mandatory-clause overlay loads off the in-scope flag, not the firm tier.

### Treating the M1-M6 rows as recommendations

The mandatory-clause rows are mandatory-by-source for an in-scope arrangement. Absence is `high`-severity-by-source regardless of the firm's bilateral position. Do not soften the severity on the strength of a strong commercial relationship.

### Conflating "EU regions" with named locations of data processing

The M3 row requires named locations (cities, data centres), not regions. A "EU regions" clause is `partial`, not `present`.

### Reading audit rights for the firm as audit rights for the firm and the competent authority

The M6 row covers both the firm and the competent authority. The clauses are distinct; coverage must be assessed separately.

## Sector overlays

### Applying the bank-flavoured interagency-guidance frame to a non-bank registrant

The non-bank registrant's contract clause set comes through 206(4)-7, 38a-1, FINRA 3110, and the rule-specific contract reach (Custody Rule, books-and-records, Reg S-P, Reg SCI). The matrix must build off the right frame; do not paste the bank checklist onto an adviser, fund, or BD contract.

### Missing the §4.F clause set on a TPA or MGA contract

The federal interagency-guidance frame does not cover NAIC Insurance Data Security Model Law §4.F third-party-service-provider contract terms. Where adopted, the §4.F clauses are mandatory-by-source.

### Missing the BaaS clause expansions

The standard generic clause set undercovers BaaS. The payments-fintech overlay adds the FBO subledger, end-customer reconciliation, deposit-insurance representation, customer-liability allocation, complaint-handling, and data-portability rows.

### Loading one sector overlay where the arrangement spans two

A dual-registrant contract or a sponsor-bank-program contract may need two sector overlays. Flag the choice in the scope record; do not collapse to one.

## AI-vendor mode

### Treating an "embedded AI feature" as automatically AI-vendor mode

If the AI feature is off and the firm has no plan to turn it on, the matrix is not in AI-vendor mode. Mark `ai_vendor = false` and add a re-review trigger if the feature is enabled. Do not pull the AI clause cluster in by reflex.

### Missing the model-version pin and deprecation-notice clock

For foundation-model arrangements, the deployed checkpoint is a moving target. The contract must address model-version pinning and deprecation-notice timing; absence is a finding regardless of the firm's read on the vendor's stability.

### Reading "we do not retain training data" without reading the abuse-monitoring exception

The enterprise default is rarely the consumer default; the contract addendum and the trust-and-safety pages set the operative posture. The matrix cites the contractual data-handling commitment and the abuse-monitoring exception, not the marketing default.

## Engagement-scope handling

### Running without scope

If the scope record is missing, ask the four questions (criticality tier, AI-vendor flag, regulatory profile, review type) and default to public posture if the practitioner declines. Note in the matrix that scope was not formalised. Do not silently apply a default sector overlay.

### Skipping cyber or privacy because "the contract is not a cyber or privacy contract"

Cyber applies whenever the contract touches NPI, PHI, PCI, customer prompts, or any control on the firm's important-business-service path. Privacy applies whenever the contract reaches regulated personal data, including customer prompts. Both default-on for AI vendors.

## Output discipline

### Citing without sections

Every regulator citation in the matrix carries a section reference or a `[verify section]` placeholder. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the matrix body.

### Marking unsupported findings silently

Use `[evidence needed]` explicitly. An inferred finding presented as evidenced is the failure mode.

### Closing with too much certainty

The confidence label is `high` only when the source posture, the evidence set, and the severity rollup line up. `medium` and `low` are normal for early-stage matrices; `unknown` is honest where the firm has not yet resourced the evidence ask.

### Drafting language instead of posture

The matrix records the recommended-amendment posture (a posture, not legal language). Counsel drafts language; the matrix names what the language must do. A posture that reads like a contract clause is over-stepping the skill's role.

### Approving the contract

The matrix stops at the recommended posture and the conditions. Counsel drafts language; the named approver decides. The skill outputs `recommended_posture`, not `decision`.
