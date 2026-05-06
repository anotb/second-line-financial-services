# Insurance sector overlay — dora-register-builder

When the engagement scope flags insurance, load this overlay alongside `references/source-anchors.md`. It carries the insurance-specific competent-authority and prior-register considerations the generic skill does not own.

## Competent-authority routing

- **EIOPA-coordinated approach**. For insurance and reinsurance undertakings, intermediaries (where in DORA scope), institutions for occupational retirement provision (IORPs, where in scope), and Solvency II groups, the technical reporting channel sits with the host-state NCA following the EIOPA-coordinated approach. EIOPA is not a direct-supervisor for filings; it coordinates.
- **Solvency II group register interplay**. A Solvency II insurance group with multiple EU undertakings: each in-scope undertaking files at its host-state NCA; the group's consolidated view is informational. The group supervisor coordinates but does not substitute for the per-undertaking submission.

## Pre-existing register inputs

- **EIOPA Guidelines on outsourcing to cloud service providers (EIOPA-BoS-20-002)** [verify exact reference and section]. Many EU insurers maintain an outsourcing register under the EIOPA cloud guidelines and their national-supervisor outsourcing notification regime. The DORA register subsumes this and broadens scope to all ICT-third-party arrangements; map and reconcile, do not copy.
- **Solvency II Article 49 outsourcing notification** [verify article structure]. Outsourcing of critical or important functions under Solvency II requires NCA notification; the underlying data (function reference, criticality, counterparty identity) is the input to the DORA register's `b_04` and `b_03` records.

## US-parent considerations (the cross-border dimension)

- **NAIC Insurance Holding Company System Regulatory Act (Model #440) [verify model number]**. Form B and Form F at the US parent of a US-headquartered insurance group with EU underwriting subsidiaries: the EU subsidiary's DORA register data may flow into Form B (intercompany services) and Form F (enterprise risk report) at the US parent. Two regulators, two artifacts; the underlying truth is the firm's TPRM data.
- **NAIC Insurance Data Security Model Law (Model #668), §4.F** third-party service-provider obligations. Where the US parent has a §668-state subsidiary, the third-party service-provider obligations carry US-side reporting expectations distinct from the EU DORA register.
- **Group ORSA**. Critical outsourced functions identified in the DORA register's `b_04` entries map into the group ORSA Summary Report at the US parent. Pointer to the firm's `risk-reporting/risk-committee-pack` and ORSA materials.

## CTPP designation in insurance

- DORA Article 31 oversight framework [verify article number] applies to ICT third parties supplying insurers as well as banks. The designation criteria include criticality and concentration. EIOPA participates in the Joint Examination Team for insurance-relevant CTPPs.

## Output-template additions for insurance

- Host-state NCA channel routing in the source-data-posture section. Multiple host-state NCAs may apply if the group has subsidiaries across EU jurisdictions.
- Solvency II outsourcing-notification reconciliation as a standing reconciliation row where applicable.
- US parent's Form B / Form F flow noted in `open_questions` for a US-headquartered group, for the parent's own consolidated outsourcing reporting (not for the DORA submission itself).

## Common pitfalls in insurance register builds

- Treating the Solvency II Article 49 notification as the DORA register. Different schema, different scope (DORA covers all ICT third parties, not just outsourcing of critical or important functions), different submission channel.
- Missing the IORP scope question for occupational pension arrangements managed by the insurer.
- Confusing the EIOPA cloud guidelines outsourcing register with the DORA Register of Information; the cloud guidelines are narrower (cloud-only) and pre-DORA in vintage.
- Forgetting the US parent's Form B / Form F dimension where the EU subsidiary's outsourcing data flows back into US-side filings.
