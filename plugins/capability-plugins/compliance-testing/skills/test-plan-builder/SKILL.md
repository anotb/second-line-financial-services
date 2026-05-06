---
name: test-plan-builder
description: |
  Drafts the pre-fieldwork test plan for a single control test cycle: scope, control objective, named source criteria, period, population, sampling reference, walkthrough plan, design-effectiveness procedures, operating-effectiveness procedures, evidence-request reference, pass and fail criteria, limitations, downstream consumers, and reviewer sign-off block. Output is the planning artifact that gets reviewer sign-off before evidence pulls and fieldwork begin; it is the contract the workpaper is written against.

  Best for:
  - A compliance-testing or internal-audit team is scoping an annual test plan or a one-off targeted review and needs the pre-fieldwork planning workpaper before evidence pulls and fieldwork.
  - A second-line reviewer is responding to a regulatory-change-management trigger (a new rule, an updated examiner priority, a new exam letter) by standing up a fresh test against an updated control set.
  - An audit lead is rebuilding a test program after a prior issue, restating control objectives and procedures from first principles before the next cycle starts.

  Not the right tool when:
  - The control inventory and risk-to-control mapping has not been done. Run the control-matrix work in `risk-compliance-core` first; the test plan consumes a control ID, it does not invent one.
  - Sample design is the only thing needed. Use `control-sampling` standalone; the test plan references the sampling memo by ID.
  - The evidence ask is the only thing needed. Use `evidence-request-builder` standalone; the test plan references the evidence request list by ID.
  - Fieldwork is in flight or complete. Use `workpaper-drafter` for during and post-fieldwork documentation. Use `qa-workpaper` for review of the completed workpaper. Boundary: this skill is pre-fieldwork; `workpaper-drafter` is during and post; `qa-workpaper` is review of completed work. The three are sequential, not redundant.

  Anchored to: internal-audit professional standards on engagement planning, work-program structure, and engagement objectives; external-audit planning and risk-response standards used as second-line methodology anchors; bank-supervisory expectations on compliance-testing-program planning and risk-based scope; consumer-protection examination-program scoping conventions; framework guidance on monitoring and separate evaluations. Citations and excerpts live in `references/source-anchors.md`.
argument-hint: "[control ID, regulatory trigger, prior-cycle test plan, or scenario for the period under test]"
---

# Test plan builder

A test plan is the pre-fieldwork contract for a single control test cycle. It names what is being tested, against which criteria, over what period, on what population, with what walkthrough and procedures, and what observable conditions count as pass or fail. The named reviewer signs off the plan before evidence pulls begin; the workpaper that follows is written against the plan, and silent drift between the two is a QA finding.

This skill produces that plan. It does not run the test, draw the sample, draft the evidence request list, classify exceptions, or write the workpaper. It produces the planning artifact in `templates/default-output.md` shape and a structured record conforming to `schemas/test-plan.schema.json` for downstream consumers (`control-sampling`, `evidence-request-builder`, `workpaper-drafter`, `qa-workpaper`). The skill stops at preparer sign-off; the named reviewer signs separately, before evidence pulls.

## Ask first

Before drafting, get plain answers. Most cycles can answer them from the prior-period plan plus the current control inventory; if not, default and flag.

- **Whose plan is this for.** Compliance-testing manager, internal-audit lead, the testing pod that will execute, the QA reviewer who will read the workpaper later. Audience drives the depth of methodology restatement and the formality of the walkthrough plan. A plan drafted for a new tester reads heavier on procedure detail than a plan drafted for an experienced pod working a familiar control.
- **What triggered this test cycle.** Annual program coverage, a regulatory change, an open finding from a prior cycle, an examiner request, a control-owner-requested review. The trigger drives scope and shapes the criteria list.
- **Has the control inventory been mapped.** A test plan needs a control ID. If the control is not in the firm's inventory, route to control-matrix work first; this skill consumes the mapping rather than inventing one.
- **What does the firm already know about this control.** Prior testing results, known issues, recent changes (system migration, new regulator letter, new policy), open remediation. The plan restates what is known so the procedures target the right risk, not last cycle's risk.
- **Has anything material changed since the last cycle.** Rule renumbering, policy updates, system changes, business-unit reorganisation, regulator priority shift. Reusing a prior plan without restating the criteria for the current period is the most common drafting failure.

When `engagement-scope` is supplied, consume it: `institution.type` and `institution.primary_regulators` set the citation focus and tone, `sector_overlay_set` selects which `references/sector-overlays/<sector>.md` loads, `cross_cutting_overlay_set` selects the `references/cross-cutting/<topic>.md` files. When it is not supplied, draft against what is on file (the prior-period plan and the control inventory usually carry enough), default to the testing program's standing posture, and note in the plan that scope was not formalised separately.

## How the plan gets built

The plan has the same spine across control types. A senior preparer fills it in roughly in the order a reviewer expects to read it, not in the order the conversation happens.

The header pins the plan to its test cycle: test ID, control ID, obligation IDs the control addresses, period under test, business unit, jurisdiction, source posture, preparer role and date, reviewer role and date placeholder. The header is the audit trail when the cycle is later reopened. Reviewer separation is structural: the same role cannot both prepare and review. The reviewer signs the plan before evidence pulls begin.

Scope and source posture restates the trigger for this cycle in two or three sentences and names the source posture the testing will operate under (public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, connector-aware). The pointer to the prior-period plan goes here when applicable, with a note on what changed. Recent supervisory posture (open findings, prior issues, recent examiner letters) goes here when public or when the source posture allows.

The test objective is a single statement of what the test concludes on: design effectiveness only, operating effectiveness only, design and operating combined. The objective is not the procedure list; it is the read the cycle is set up to deliver. A plan whose objective is "test the control" has not yet been scoped.

Source criteria names the criteria the test will evaluate evidence against. For each criterion the plan carries the source (regulator and instrument), the section reference, and either a verbatim excerpt or a paraphrase tight enough that the criterion is unambiguous. This is the regulatory frame; the loaded sector and cross-cutting overlays add sector-specific or topical detail by reference, not restated. Cite by file path into `references/source-anchors.md` and the loaded overlays. Reusing prior-period criteria without restating them for the current period is a recurring drafting failure; rule sections renumber, policies update.

Population and sampling reference describes the population the test addresses (originations during the period, accounts open during the period, transactions executed during the period, packets due in the period), the source of truth for the population extract, the period boundaries, and a pointer to the sampling memo (`control-sampling` output, by ID) where one is produced separately. For small tests with inline sample design the sample method, size rationale, and tolerable deviation rate sit in this section directly; for larger tests the pointer to the sampling memo is the single source of truth and the workpaper later reads against that memo.

The walkthrough plan names the walkthrough scope, the roles to interview, the processes to observe, the system screens to inspect, and the evidence to capture during the walkthrough. The walkthrough is the design read that justifies the procedures; skipping it on "small" controls is the most common cause of a "design-gap" exception being surfaced for the first time only in the workpaper, when it should have been planned-against from the start. Where the prior cycle covered design and the current cycle is operating-only, the walkthrough plan can be light (a refresher walkthrough on system changes), and the plan says so explicitly with the prior workpaper ID referenced.

Design-effectiveness procedures are numbered procedures evaluating whether the control as designed addresses the criterion. Each procedure carries a description, the expected evidence type (configuration screen, policy excerpt, attestation form template, training record), and the expected observable condition that supports a met or not-met read. Design procedures are walkthrough-and-inspection procedures; they are not sample-based reperformance.

Operating-effectiveness procedures are numbered procedures testing whether the control operated as designed during the period. Each procedure carries a description, the expected evidence type per sample (case file, system extract, attestation packet, reconciliation), and the expected observable condition. Operating procedures are typically sample-based reperformance, observation, inquiry, or confirmation; the plan names the methodology per procedure so the workpaper later reads against the planned methodology, not whatever the preparer chose in the moment.

Evidence-request reference points to the evidence request list (`evidence-request-builder` output, by ID) where one is produced separately, or carries the evidence request list inline for small tests. Evidence-request reference is the contract the firm operates against when fielding the ask; the plan does not invent the request list independently of the dedicated skill.

Pass and fail criteria name the observable conditions for design and operating effectiveness. Pass criterion: the observable condition that supports an "effective" read (e.g., 100% of sampled disputes within the procedural clock with current evidence; the form supports per-entitlement attestation). Fail criterion: the observable condition that supports a "not effective" read (e.g., any sampled item outside the procedural clock without escalation evidence; the form supports only blanket per-system approval). Tolerable deviation rate is named here (or pointer into the sampling memo); zero-tolerable populations (privileged access, sanctions screening, customer-funds segregation) are read severity-driven, not rate-driven, and the plan says so.

Limitations and assumptions name the period coverage, the scope exclusions (a separate control, a separate process, a different period segment, a different population stratum), the reliance on prior testing (with the prior workpaper ID and the rationale), and the dependencies on other in-flight reviews. Limitations are the reviewer's protection paragraph in the plan: they declare upfront what the test will not conclude on so the workpaper does not over-reach later.

Downstream consumers names the skills the plan hands off to: `workpaper-drafter` for fieldwork documentation, `qa-workpaper` for review of the completed workpaper, `exception-analysis` for classification of exceptions surfaced in fieldwork, `risk-compliance-core/skills/issue-writeup` for any issues elevated from the cycle. Naming the consumers makes the cycle's lifecycle visible at planning time.

Reviewer sign-off block carries preparer (with date), reviewer (separate role, date placeholder; signs before evidence pulls), and the reviewer questions the preparer wants the named reviewer to consider before sign-off. Pre-fieldwork sign-off is a hard gate; evidence pulls before sign-off is a CMS finding in bank exams and a methodology weakness in any second-line program. Source trace and confidence label close the file: every material claim in the plan cites a source with section reference, and the confidence label (high / medium / low / unknown) reflects the source posture, the firm-policy maturity for the control area, and any open question on the criteria.

## What's load-bearing and what flexes

Load-bearing across every test plan: design and operating procedures are separated, never collapsed. Each procedure carries an expected evidence type and an expected observable condition; a procedure with no expected evidence cannot be passed or failed cleanly. Source criteria carry section references or `[verify section]` markers; URL alone does not pass. Reviewer separation is structural; the same role cannot both prepare and review. Pre-fieldwork sign-off is a hard gate; evidence pulls happen after sign-off, not before. Conclusions at workpaper time will speak to control effectiveness, not legal violation, and the plan's pass and fail criteria are written in that vocabulary. The plan stops at preparer sign-off here; the reviewer signs separately. No named institutions in the plan unless they are public defendants in a finalised enforcement action.

Flexes to the cycle: plan depth and length scale to control complexity, population size, and the prior-cycle history. A familiar low-volume control with a stable prior cycle reads short; a new control area, a regulatory-change-driven cycle, or a control with a recent finding reads longer with a heavier walkthrough plan and richer pass and fail criteria. Sector overlay loading follows engagement-scope plus the rule that the regulator the control was designed for drives the sector overlay (HMDA controls pull banking; an adviser compliance-program control pulls capital-markets; a sponsor-bank end-customer reconciliation control pulls payments-fintech and banking together). Cross-cutting overlay loading: cyber overlay is default-on for any control test touching IAM, data-protection, or NYDFS Part 500-mandated areas; conduct overlay is default-on for any consumer-facing test where customer-harm framing matters separately from technical control conclusion. Privacy overlay loads when GLBA Safeguards or HIPAA touches the population. Audience drives shape: a plan drafted for a new pod reads heavier on procedure detail and methodology restatement; a plan drafted for an experienced pod reads tighter with the procedure list as a contract rather than a tutorial.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/banking.md`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific test-plan conventions loaded per engagement-scope.
- `references/cross-cutting/cyber.md`, `conduct.md` — cross-cutting flavour; cyber default-on for IAM and Part 500 controls, conduct default-on for consumer-facing tests.
- `references/firm-overlay.md` — firm-installed methodology, taxonomy, review gates, and template variants beyond the regulatory baseline; consumed when present.
- `templates/default-output.md` — test-plan template.
- `schemas/test-plan.schema.json` — structured-output contract for downstream consumption.
- `examples/` — annual consumer-error-resolution test plan at a regional bank; periodic high-risk customer-due-diligence refresh test plan.
- `TROUBLESHOOTING.md` — recurring pitfalls (design-and-operating procedures collapsed, procedures without expected evidence, walkthrough skipped on "small" controls, prior-cycle plan reused without restating criteria, first-line owner drafting the plan, plan treated as a one-off rather than the workpaper's contract).

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Output

The skill emits a test plan in `templates/default-output.md` shape and a structured record conforming to `schemas/test-plan.schema.json`. Downstream consumers: `control-sampling` reads `control_id` and `population` to build the sampling memo and write back `sampling_id`; `evidence-request-builder` reads `criteria` and `procedures` to draft the evidence request list and write back `evidence_request_list_id`; `workpaper-drafter` reads the full plan as the contract for the workpaper; `qa-workpaper` reads the plan and the workpaper together to assess sufficiency. The schema is the cross-skill contract; additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.
