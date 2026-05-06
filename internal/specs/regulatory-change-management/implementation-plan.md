# Spec: implementation-plan

Plugin: regulatory-change-management
Status: phase 1 spec sheet, pending phase 2 build
Date: 2026-05-06

## Activation-tuned description

Sequences regulatory remediation into a workplan. Takes the obligation list, the policy diff, and any control gaps and produces milestones, owners (by role), dependencies, acceptance criteria, governance checkpoints, and implementation risks. Output is sized for a regulatory-change committee or program-management office (PMO) and is structured for tracking against a mandatory compliance date.

Best for:
- Obligations have been extracted and policy diffed; the firm now needs a sequenced, owner-assigned plan to reach compliance by the effective date.
- A consent order or MRA requires a remediation plan that names workstreams, owners, milestones, and acceptance criteria.
- A regulatory change program needs a refreshed plan after a transition-period change or a regulator's frequently-asked-questions (FAQ) update.

Not the right tool when:
- Obligations have not been extracted yet (use rule-to-obligation-extraction).
- Gaps have not been identified (use policy-diff and any control-gap output from compliance-testing).
- Output is for an exam (use exam-brief or the sector exam-readiness skills).
- The objective is to assess whether the firm should comply at all (that is a legal determination, out of scope).

Anchored to: 12 CFR Part 30 Appendix B (heightened standards, escalation and corrective action) [verify section]; OCC Heightened Standards governance expectations on remediation; SR 13-19 (operational risk including change management); FRB SR 21-3 / OCC 2021-X management of remediation [verify]; FFIEC IT Examination Handbook (Management Booklet) on project management [verify]; PMI / PMBOK as a generic technique reference (not authoritative).

## Source anchors

- 12 CFR Part 30 Appendix B (Heightened Standards) — escalation, corrective action, three-lines-of-defense expectations [verify section ref].
- OCC Bulletin 2014-24 / Heightened Standards FAQs — remediation expectations [verify].
- FRB SR 13-19 (Outsourcing) — remediation and change-management posture for third parties.
- FFIEC IT Examination Handbook, Management Booklet — project and change management expectations.
- Federal Reserve interagency MRA/MRIA framework — public references in supervisory speeches and SR letters [verify exact public source].
- Consent-order templates from public OCC, FDIC, FRB, CFPB enforcement actions — for remediation-plan structure as observed in public orders.
- Risk-compliance-core/issue-management plugin reference (cross-plugin dependency, not regulator).

## Sector overlays needed

- banking.md — Heightened Standards remediation expectations; MRA/MRIA cadence; capital-plan remediation if related to CCAR/DFAST.
- insurance.md — state insurance department remediation requirements; ORSA-driven remediation.
- capital-markets.md — SEC deficiency-letter remediation; FINRA exam findings remediation; IAA Rule 206(4)-7 remediation cadence.
- payments-fintech.md — CFPB MRA/MRIA-style remediation under non-bank supervision; state money-transmitter remediation.

## Cross-cutting overlays needed

- cyber.md — incident-disclosure remediation, NYDFS Part 500 remediation expectations.
- privacy.md — GLBA Safeguards remediation.
- climate.md — climate-risk management plan elements for in-scope institutions.
- conduct.md — UDAAP remediation, customer redress design.

## Output template named sections

1. Plan summary (mandatory date, in-scope obligations count, workstreams count, top three implementation risks)
2. Scope and source posture (rule citation, obligation IDs in scope, gap inventory in scope)
3. Workstream structure (workstream → obligations covered → owner role → milestones)
4. Milestone schedule (Gantt-style table; date, owner, dependency, acceptance criteria)
5. Acceptance criteria per milestone (what evidence demonstrates milestone closure)
6. Governance checkpoints (committee, frequency, decision rights, escalation triggers)
7. Implementation risks (delivery risks, second-order risks like control drift during change)
8. Resource asks (explicit named gaps, not generic "more resources")
9. Effective-date posture and contingency (early adoption, late adoption, phased adoption)
10. Open questions for legal, business, and regulatory liaison
11. Handoff into BAU (when remediation closes; how the obligation lands in the obligation inventory)
12. Source trace and confidence labels

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| plan_id | string | Stable ID for the plan |
| effective_date | date | Mandatory compliance date |
| obligations_in_scope | array<string> | Obligation IDs from the extraction |
| gaps_in_scope | array<string> | Finding IDs from policy-diff and control-gap inputs |
| workstreams | array<workstream> | Workstreams |
| workstream.id | string | Stable workstream ID |
| workstream.name | string | Plain-language name |
| workstream.owner_role | string | Owner role (not person) |
| workstream.obligations_covered | array<string> | Obligation IDs |
| workstream.milestones | array<milestone> | Milestones |
| milestone.id | string | Stable milestone ID |
| milestone.name | string | Plain-language name |
| milestone.due_date | date | Target date |
| milestone.dependencies | array<string> | Dependent milestone IDs |
| milestone.acceptance_criteria | array<string> | Evidence-based criteria |
| milestone.evidence_artifacts | array<string> | Artifacts that prove closure |
| governance_checkpoints | array<object {body, cadence, decision, escalation_trigger}> | Committees and triggers |
| implementation_risks | array<object {risk, likelihood, impact, mitigation, owner_role}> | Implementation risk register |
| resource_asks | array<object {role, headcount_or_budget, justification}> | Explicit named asks |
| handoff_to_bau | object {target_owner_role, evidence_pack, monitoring_cadence} | BAU handover plan |
| confidence | enum {high, medium, low, unknown} | Plan confidence |

## Example scenarios (public-source-derived)

1. Implementation plan for CFPB Section 1071 small business lending data rule (12 CFR 1002.107) at a community bank in tier 2. Workstreams: data-collection program design; firewall implementation; LOS/origination platform changes; staff training; recordkeeping; reporting; consumer-facing notice. Milestones aligned to the tiered compliance dates; acceptance criteria reference firewall test results and a sample submission to CFPB.
2. Implementation plan for SEC cybersecurity disclosure rule at a registered investment adviser (Form ADV / 8-K applicability where parent is a public company). Workstreams: materiality determination playbook, incident-response playbook hand-offs, board oversight disclosure language drafting, annual Reg S-K Item 106 disclosure design, internal disclosure committee charter update.

## Common pitfalls

1. Owners as names not roles. Roles survive turnover; names do not. The plan tracks roles and links names through a separate RACI.
2. Acceptance criteria that read like activities instead of evidence ("complete training" versus "training-completion record covers 100% of in-scope staff with attestation captured by [date]"). Examiners want evidence, not activity language.
3. Milestones that bunch at the effective date. A plan with 70% of milestones in the last month of the transition is high-risk by construction. Push to mid-transition where possible and call out the risk explicitly where not.
4. No handoff to BAU. A remediation that closes without a documented transition into the obligation inventory and ongoing monitoring cadence will drift within 12 months.
5. Skipping the second-line review point. The plan needs an explicit checkpoint where the second line confirms control design before go-live, not just a first-line attestation.
