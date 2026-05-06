# Criticality assessment

**Vendor**: [legal entity; brand name if different]
**Service in scope**: [concise, e.g., core banking SaaS, claims TPA, foundation-model API]
**Arrangement ID**: [stable ID; reused across vendor-diligence, contract-gap-review, exit-plan, concentration-risk-review]
**Engagement ID**: [pointer to engagement-scope record, or "none — scope not formalised"]
**As of**: [date]
**Review type**: [pre-onboarding | annual-recertification | off-cycle-trigger | material-change-re-review | post-incident-re-review | ibs-change-re-review | contract-renewal-re-review]
**Owner (role)**: [head of TPRM, business owner SVP, IBS owner, or other per firm policy]
**Approver (role)**: [per firm policy for criticality calls at this tier]
**Confidence label**: [high | medium | low | unknown]

## Service in scope

- Vendor and contracting entity.
- Concise service description.
- Whether the service is a discrete arrangement or part of a broader vendor relationship.

## Business process supported

- Named business process the arrangement supports.
- Important business service mapping (the firm's named IBS where the arrangement sits on the IBS chain). Use the firm's IBS map; if the firm has no IBS map, note "no formal IBS map" and proceed against named candidate IBS for the sector (see the loaded sector overlay).
- Customer-facing position: on the IBS critical chain, supporting an IBS but off the critical chain, or non-IBS.

## Recovery time and recovery point objectives

| | Firm tolerance | Vendor commitment | Source |
|---|---|---|---|
| RTO | | | |
| RPO | | | |

- Firm tolerance from the IBS impact analysis. Not the vendor commitment.
- Vendor commitment from the contract or evidence pack.
- `recovery_meets_firm_tolerance = [yes | no | partial | unknown]`. A `no` or `partial` is a finding for `contract-gap-review` and a precondition for `vendor-diligence` to flag in operational-resilience evidence.

## Customer impact

- Severity: `[low | medium | high | severe]`.
- Affected populations: [retail-deposit | small-business | commercial | policyholder | fund-shareholder | other].
- Harm modes: [financial-loss | fairness | accessibility | complaint-exposure | fraud-exposure | privacy-breach | fiduciary-breach].
- Narrative on the harm pattern under disruption, degradation, and unavailability.

## Regulatory impact

- Severity: `[low | medium | high | severe]`.
- Regimes intersected: [bank-prudential | ICT-resilience | securities-compliance | insurance-solvency | BSA-AML | consumer-compliance | market-conduct | privacy].
- Notification triggers: [supervisory material-event reporting | breach-notice clock | customer-notice clock | filing-update trigger].

## Operational impact

- Substitutability: `[easy | moderate | hard | none]`.
- Time-to-restore estimate under a forced cutover. Compare to firm tolerance.
- `manual_workaround_viable = [true | false]`. True only when the firm can keep the supported process running without the vendor for the full tolerance window.

## Data scope

- Data categories the arrangement touches: [NPI | PHI | PCI | PII-non-sensitive | confidential-business | trading-data | model-prompts | model-outputs | training-data | logs-only | metadata-only | none].
- Cross-border flows: [yes | no | unknown].

## Concentration considerations

- Concentration considerations raised here: [hyperscaler region | sponsor-bank | BIN sponsor | foundation-model vendor | transfer agent | custodian | claims TPA | fund accountant | other].
- Pointer to `concentration-risk-review` record (where present): [ID]. The portfolio analysis lives there.

## Tier and rationale

- **Tier**: `[critical | important | not-critical | unknown]`.
- **Rationale**: name the criteria that drove the call. Cite the IBS dependency, customer-impact severity, regulatory exposure, substitutability read, and any cross-jurisdictional driver. Cite sources by file path (`references/source-anchors.md`) rather than restating excerpts here.

## DORA critical-or-important-function flag

- `dora_critical_or_important_function = [yes | no | not-in-scope]`.
- Rationale. The criteria differ from the firm's own tier; record both calls separately. `not-in-scope` where DORA does not apply to the entity. `no` where DORA applies but the arrangement does not meet the EBA criticality threshold (the arrangement may still belong in the DORA register).

## UK PRA important-business-service flag

- `uk_ibs_flag = [yes | no | not-in-scope]`. UK overlay only.

## Owner and approver

- **Owner (role)**: [head of TPRM | business owner SVP | IBS owner | head of operational resilience | other].
- **Approver (role)**: [per firm policy for criticality calls at this tier; commonly operational-risk committee for `critical`, TPRM forum or business unit risk for `important`, line management for `not-critical`].

## Reviewer questions

Each question names the decision it supports.

- [bulleted]

## Next-review trigger

- Annual cycle date: [date].
- Material-service-change trigger: [described].
- IBS-change trigger: [described].
- Contract-renewal trigger: [date].
- Incident-driven re-review condition: [described].
- For AI vendors, model-version-change trigger.

## Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

Cite `references/source-anchors.md` for canonical citations. Use `[verify section]` if the section reference is unknown; do not invent.

---

*Assessment depth scales to the proposed tier and to whether the engagement is in DORA or UK SS2/21 scope.* For a not-critical arrangement, several sections collapse to a paragraph; for a critical or DORA-in-scope arrangement, full depth applies and reviewer questions cluster for the operational-risk committee, the AI risk committee (AI vendors), or the fund board (registered funds).
