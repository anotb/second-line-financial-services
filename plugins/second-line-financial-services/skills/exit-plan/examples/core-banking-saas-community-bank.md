## Example: core-banking SaaS exit plan at a community bank

Public-source-derived. No named vendor or bank. The shape mirrors a common exit-plan pattern at $2-10B community banks running a hosted core-banking platform that supports deposit accounting, loan servicing, and the general ledger.

## Input

- **Vendor**: a US-based core-banking SaaS provider hosting deposit, loan, and GL modules in a single-tenant configuration on a hyperscaler.
- **Service**: end-to-end core-banking platform; teller, ATM, online banking and bill-pay integrations; nightly batch and report generation.
- **Business process supported**: deposit-account servicing, consumer-loan servicing, regulatory reporting feed.
- **Important business service**: deposit-account servicing (firm IBS map names a 24-hour impact tolerance for transactional outage and a longer tolerance for ancillary reporting).
- **Inputs already on file**: vendor-diligence record (criticality = critical; subcontractors include the hyperscaler and two integration vendors; data_access includes NPI, PCI, books-and-records; residual risk = high; exit_plan_status = missing); contract executed three years ago carrying a six-month transition-assistance commitment and a fee for early termination; FFIEC inter-agency cloud joint statement (April 2020) is on the firm's source list.
- **Engagement scope supplied**: institution = state member bank; primary regulators = FRB, state DFI; persona = head of operational resilience; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **AI vendor**: false.

## Output sketch

The skill produces an exit plan. Headlines:

- **Triggers** — vendor-driven (bankruptcy, material breach, persistent SLA failure); firm-driven (strategic shift to a different core, post-merger consolidation); regulator-driven (supervisory criticism of vendor; MRA citing the arrangement); market-driven (vendor acquired by a competitor with conflicted ownership; widespread outage at the hyperscaler region). Lead-time assumptions vary from "weeks under distress" to "twelve to eighteen months under planned transition".
- **Transition target options** — substitute-vendor as primary (two named candidate cores in the community-bank segment, viability `viable`, time-to-transition twelve to eighteen months given core-data-migration realities, dependencies include data-migration build, end-customer notification cycle, regulator engagement); in-source as `not-viable` for a community bank of this size; retire-service as `not-applicable`; hybrid as `weak`. Selected transition target: substitute-vendor.
- **Time-to-transition vs tolerance** — `breach`. The planned twelve-to-eighteen-month transition exceeds the impact tolerance for deposit-account servicing under any forced-cutover scenario. Surface as a finding to the chief operating officer; the plan documents the gap rather than papering over it.
- **Data return and destruction** — vendor must return all customer data in a documented, schema-mapped extract; books-and-records under the Bank Service Company Act must be preserved for regulator examination access through the wind-down; key rotation and access revocation choreographed against the cutover; vendor attestation of destruction with a thirty-day post-validation hold.
- **Knowledge transfer** — runbooks, integration specs, configuration baselines, named SMEs available for ninety days post-cutover; code and artifact escrow on third-party-developed integrations.
- **Contract termination mechanics** — clause reference cited; termination-for-convenience present but with a fee; six-month transition-assistance commitment; regulator-directed-termination clause absent — flagged to `contract-gap-review`.
- **Customer notice posture** — Reg DD §1030.5 change-in-terms and Reg E §1005.8 advance notice required for affected deposit and consumer-loan account changes; lead time set at the longer of the two named regulated clocks; channel: statement insert plus mailed letter plus in-app notice.
- **Regulator notice posture** — material vendor change notification to the FRB and state DFI; ongoing supervisory engagement during transition rather than only on-paper notice; no DORA scope.
- **Supervisory readiness during transition** — dual-running controls covering both cores during cutover; Bank Service Company Act §1867(c) examination-access preserved on both sides; the firm's safety-and-soundness exam in the cutover quarter pre-briefed.
- **Fourth-party dependencies** — hyperscaler region as a substitution-window bottleneck; integration vendors must rebuild against the substitute core.
- **Testing plan** — tabletop in the next quarter (first-ever); partial-simulation within twelve months; full-live exercise out of scope for cost reasons. `last_test_date = none`, `last_test_outcome = never-tested`. Surface as a finding.
- **Cost estimate range** — multi-million range with named cost drivers (data migration, dual-running, end-customer notification cycle, internal change management).
- **Approver** — chief operating officer; reviewer questions clustered for the operational-resilience committee.

The plan stops at the recommendation. It does not approve transition.

## Why this scenario matters

- **Time-to-transition vs tolerance is honest.** The plan documents a tolerance breach rather than reporting "ten months" because that fits the policy. The skill must be honest about the breach and surface it to the IBS owner and the COO.
- **Trigger-set covers all four categories.** A plan that covers only vendor-driven triggers misses regulator-driven and market-driven scenarios that have shorter lead times.
- **The contract is not the plan.** The vendor's six-month transition-assistance commitment is a clause; the firm's playbook is the plan. Different things.
- **Customer notice and regulator notice are both real clocks.** Reg DD and Reg E for customers; FRB and state DFI for the regulator. Lead times must be planned, not improvised on the day.
- **Bank Service Company Act examination access continues through wind-down.** The contract clause and the actual evidence-preservation choreography are both required.
- **Testing cadence is the difference between paper and posture.** A plan that has never been tested gets surfaced as a finding even if the plan itself reads complete.

## Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023) §V ongoing monitoring and §VI termination [verify section].
- FFIEC IT Examination Handbook — Outsourcing Technology Services booklet, contingency planning and termination expectations [verify section].
- FFIEC IT Examination Handbook — Business Continuity Management booklet, testing-and-exercise section [verify section].
- FFIEC inter-agency cloud joint statement (April 2020).
- Bank Service Company Act, 12 USC §1867(c).
- Reg DD, 12 CFR §1030.5 (change-in-terms notice).
- Reg E, 12 CFR §1005.8 (change-in-terms notice).

See `references/source-anchors.md` for full citations.
