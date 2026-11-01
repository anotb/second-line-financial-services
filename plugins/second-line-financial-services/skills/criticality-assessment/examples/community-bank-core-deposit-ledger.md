# Example: core-banking SaaS for a community bank's deposit ledger

Public-source-derived. No named vendor. The shape mirrors a common criticality call at a community bank ($2-5B in assets) selecting a core-banking SaaS to host the deposit ledger.

## Input

- **Arrangement**: a US-based core-banking SaaS that runs the bank's deposit subledger, posts daily settlement, and provides the system of record for retail and small-business deposits.
- **Business process supported**: deposit-account servicing across retail and small-business books.
- **Inputs already on file**: the bank's important-business-service map (deposits identified as IBS); the firm's impact tolerance for the deposit-servicing IBS (RTO 4 hours, RPO 15 minutes); vendor proposal with claimed RTO 8 hours and RPO 1 hour; SOC 2 Type II in process.
- **Engagement scope supplied**: institution = state-chartered community bank; primary regulators = FDIC, state DFI; persona = head of TPRM; source posture = public-plus-firm-policy; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **AI vendor**: false. The platform has an embedded summarisation feature for branch-staff workflows; the bank has not enabled it.

## Output sketch

The skill produces a criticality assessment record. Headlines:

- **Service in scope and process supported** — core deposit-ledger and daily settlement; named IBS = deposit servicing.
- **RTO and RPO** — firm tolerance is 4h / 15 min; vendor commitment is 8h / 1h. `recovery_meets_firm_tolerance = no`. Surfaced as a finding for `contract-gap-review` and as a precondition for `vendor-diligence` to flag in operational-resilience evidence.
- **Customer impact** — `severity = severe`; populations = retail-deposit and small-business; harm modes = financial-loss, fairness on disputed transactions, complaint exposure on extended outage. The deposit-account holder cannot reach balances during outage; reputational damage compounds within hours.
- **Regulatory impact** — `severity = high`; regimes = bank-prudential and consumer-compliance; notification triggers = potential FDIC and state-DFI material-event reporting on sustained outage; Reg E and Reg DD customer-notice exposure if the outage induces a change-in-terms or fee-incidence event.
- **Operational impact** — `substitutability = hard`; time-to-restore on a forced cutover measured in months, not days; `manual_workaround_viable = false` (paper and IVR fallback exists for inquiry but not for transaction processing at scale beyond a short window).
- **Concentration considerations** — single core-platform vendor for the institution; raise the flag and pass portfolio analysis to `concentration-risk-review`.
- **Tier** — `critical`. Rationale names the IBS dependency, the customer-impact severity, the substitutability read, and the gap between firm tolerance and vendor commitment.
- **DORA flag** — `not-in-scope` (US-only firm, no EU nexus). Rationale recorded.
- **UK IBS flag** — `not-in-scope`.
- **Owner** — head of TPRM, with the deposit-product SVP as the business owner and the COO as the IBS owner per the firm's resilience policy. Approver per policy is the operational-risk committee for critical-tier arrangements.
- **Reviewer questions** — RTO/RPO gap closure path; manual-workaround testing cadence; exit-plan precondition before contract execution.
- **Next-review trigger** — contract-renewal, material-service-change, any IBS-impact-tolerance revision.

The record stops at the recommendation. The named approver decides.

## Why this scenario matters

- **Tier set on impact, not spend.** A core-banking platform is critical because the IBS sits on it, not because of the contract value.
- **Vendor commitment is not the test.** The vendor's claimed RTO/RPO is a ceiling; the firm tolerance from the IBS analysis is the test. The gap is itself a finding.
- **Manual-workaround viability is load-bearing for the tier call.** Without it, "important" cannot survive contact with the firm's tolerance window.
- **Concentration is a flag here, not the analysis.** A single-arrangement assessment raises concentration; the portfolio call lives in `concentration-risk-review`.
- **DORA call is recorded explicitly even when negative.** US-only firm, no EU nexus, `not-in-scope`. The record carries the call and the rationale rather than leaving the field implied.

## Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023).
- FFIEC IT Examination Handbook — Business Continuity Management booklet, business-impact analysis section.
- BCBS Principles for Operational Resilience (March 2021) on important business services.
- Reg DD (12 CFR Part 1030) and Reg E (12 CFR Part 1005) for the customer-notice clock context.

See `references/source-anchors.md` for full citations.
