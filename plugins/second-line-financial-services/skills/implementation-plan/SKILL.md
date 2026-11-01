---
name: implementation-plan
description: "Sequence regulatory change or remediation into a workplan with milestones, owners, dependencies."
argument-hint: "[obligation list, policy-diff output, control-gap input, trigger artifact (rule, MRA, MRIA, consent order), effective date, scope]"
---

# Implementation plan

A regulatory remediation runs on a small set of operational artifacts. What triggered the plan and what the trigger says (final rule, supervisory letter, consent order, self-identified issue). What obligations and gaps the plan covers. The mandatory date the plan runs to. The workstreams the plan breaks into and the role that owns each. The milestone chain through each workstream, with evidence-based acceptance criteria and dependencies between workstreams. The governance cadence the programme reports up through. The risks to delivery and what the firm does about them. The resource asks the steering committee approves. The pre-effective-date readiness checkpoints that demonstrate readiness ahead of supervision. What the firm does if a milestone slips past the mandatory date. The handoff into BAU when remediation closes.

This skill produces the implementation plan as a written artifact and a structured record (`schemas/implementation-plan.schema.json`). It is the artifact the regulatory-change PMO, head of compliance, transformation lead, or business sponsor carries through the implementation programme and updates as milestones land. The plan is a draft until the named programme sponsor and the second-line oversight role attest. The skill stops short of approving the plan; the approval gate is human.

## When to use

Sequences a regulatory remediation into the workplan a regulatory-change PMO, head of compliance, transformation lead, or business sponsor runs to a mandatory compliance date. Takes an obligation list (from rule-to-obligation-extraction), a policy diff (from policy-diff), and any control-gap output, and produces workstreams, milestones with dependencies, owners by role, evidence-based acceptance criteria, governance cadence (working group, steering, executive, board), implementation risks, resource asks, regulator-readiness checkpoints, and the BAU handoff. Sized for a regulatory-change committee or PMO and structured for tracking against a mandatory compliance date or supervisory-letter deadline. Generic across regulator type and trigger; sector and cross-cutting overlays load from the scope.

Best for:
- A new final rule has effective dates approaching and the firm needs a sequenced, owner-assigned plan with governance cadence and evidence criteria.
- A supervisory letter, MRA, MRIA, or consent order requires a remediation plan with named workstreams, milestones, owners, monitor or independent-consultant integration, and reporting cadence.
- A regulatory-change programme needs a refresh after a transition-period change, a regulator FAQ update, or a litigation-driven shift in the effective date.
- A self-identified issue or audit finding warrants a programme-level plan with second-line oversight rather than an issue-management ticket.

Not the right tool when:
- Obligations have not been extracted yet. Use `rule-to-obligation-extraction` first; this skill takes its output as input.
- Policy gaps have not been identified. Use `policy-diff` to surface the gaps; combine with control-gap output from compliance-testing where available.
- The artifact is for an active examination engagement. Use `exam-brief` for the engagement-side scaffolding; this skill chains downstream from exam-brief when an MRA, MRIA, or supervisory letter is issued.
- The objective is to assess whether the firm should comply at all. That is a legal determination and is out of scope for the second line.
- The trigger is a single low-risk issue suited to the routine issue-management lifecycle (use `issue-writeup`); this skill is for programme-level remediation.

## Ask first

A handful of facts settle before drafting. Most of them come from the trigger artifact, the obligation list, and the policy-diff output. Where they do not, default to a public posture and flag the default in the plan.

- **What triggered the plan, and what does the trigger say.** Final rule with a published effective date; supervisory letter naming an MRA or MRIA with a date; consent order with a milestone schedule; a self-identified issue routed through issue-management policy. The trigger sets the binding deadline and the supervisory follow-up posture.
- **What obligations and gaps are in scope.** The obligation list (from `rule-to-obligation-extraction`) and the gap inventory (from `policy-diff` and any control-gap output) define the plan's perimeter. A plan drafted from a gap list alone misses the supervisory and governance dimension.
- **Who is the audience.** Programme working group, steering committee, executive risk committee, board risk committee. Each consumes a different cut. The same structured record drives all four, with the artifact narrative re-cut to audience.
- **What is the source posture.** Public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, or connector-aware. The plan can assert at higher confidence as the source posture deepens; what cannot be asserted carries `[evidence needed]`.
- **What sector and cross-cutting overlays apply.** Banking, insurance, capital markets, payments-fintech for sector. Cyber, privacy, climate, conduct for cross-cutting. The plan loads only the overlays the trigger and scope implicate; loading all four cross-cutting overlays for a plan that touches none of them is noise.

When an `scope` record is supplied, the skill consumes it for institution, persona, source posture, sector overlay set, and cross-cutting overlay set. When it is not supplied, ask the few questions and default. Note unresolved defaults in the plan summary.

## How the plan gets built

The plan has a spine that holds across triggers. The order below is the spine; in practice, several sections can fill in any order as inputs arrive. The structured record sorts itself.

**Plan summary.** Trigger type and source citation. Mandatory date. Obligation count and gap count in scope. Workstream count. Top three implementation risks. Confidence label. The summary is what the steering committee reads first and what the board pre-read condenses.

**Scope and the evidence posture.** Jurisdiction, institution type, in-scope products, business units, legal entities, and geographies. Out-of-scope list (an empty out-of-scope list is a signal that the conversation has not happened). Source posture. The trigger source citation with section reference.

**Tiered compliance dates.** Where the rule has tiered effective dates and the institution touches more than one tier, the plan carries the tier-specific dates with rationale. Collapsing tiered dates to a single date misreads the smaller-tier obligation.

**Workstream structure.** A workstream covers a coherent set of obligations and gaps with one owner role. Workstream owners are roles, never named individuals; roles survive turnover, names do not. Each workstream names a second-line oversight role that confirms control design. The workstream block lists the obligations covered, the gaps covered, and the dependencies on other workstreams.

The workstream cut should match the natural decomposition of the change. For a data-collection rule, workstreams generally include written-program design, system or platform changes, control build, training, recordkeeping, reporting, and consumer-facing changes. For a governance rule, workstreams generally include charter and policy, committee process, board reporting, and disclosure. The pattern is rule-agnostic in shape and rule-specific in content.

**Milestone schedule.** Each milestone names the workstream, the milestone name, the due date, the owner role (defaulting to the workstream owner where not different), the dependencies on other milestones, the acceptance criteria, the evidence artifacts the milestone produces, whether second-line review is required for closure, and the status. Milestones bunching at the mandatory date is the failure mode by construction; the steering committee should see the milestone-density profile across the transition window and push back where the loading is unworkable.

**Acceptance criteria.** This is where the plan stops being activity language and starts being evidence language. "Complete training" is an activity; "training-completion record covers 100% of in-scope staff with attestation captured by [date], retained per recordkeeping policy" is evidence. Examiners ask for the artifact, not the activity log. Restate every activity-shaped acceptance criterion as the artifact that proves closure.

**Governance checkpoints.** The committees and forums the programme reports up through, with cadence, decision rights, escalation triggers, membership roles, and the reporting artifact each consumes. Match cadence to criticality. A weekly working group plus a quarterly steering committee may be right for a low-criticality programme; an MRIA-driven programme generally calls for weekly working group, biweekly steering, monthly executive risk committee, and quarterly board reporting (or more frequent for consent-order monitoring). Under-governing a high-criticality programme is the more common failure mode than over-governing a small one.

**Implementation risks.** Delivery risks (vendor delivery, key-person, scope creep, funding) plus second-order risks the change introduces (control drift during change, regulator-interpretation risk, interdependency risk). Each risk names likelihood, impact, mitigation, owner role, and an early-warning indicator that surfaces the risk before it materialises. Generic risks ("change is hard") fail the second-line gate; risks tied to a specific milestone or obligation pass.

**Resource asks.** Each ask names the role, the headcount or budget, the milestone the ask unblocks, and the consequence if declined. Generic "more resources" does not survive a steering committee. A steering committee can act on "one business analyst with 1071 LOS experience for Q3-Q4, otherwise milestone MS-04 slips by six weeks". It cannot act on "we need more people".

**Regulator-readiness checkpoints.** Pre-effective-date checkpoints that rehearse the control before supervision arrives. Mock submissions against the published technical specification, control-design walkthroughs with second line and outside counsel where the change touches privileged territory, tabletops with the operating team, attestations by the second-line oversight role. Three readiness checkpoints sized to the change is the practitioner pattern. Going live on the mandatory date without a rehearsal leaves the firm with no margin and the first operating instance under supervisory attention.

**Effective-date posture and contingency.** Posture is one of early-adopt, on-time, phased-by-tier, or late-with-contingency. The contingency plan is what the firm does if a milestone slips past the mandatory date. Manual workaround for the first reporting cycle. Scope reduction with regulator engagement. Customer-impact mitigant. The contingency is the answer to the steering committee question "what happens if we slip".

**Open questions.** Each open question names the audience (legal, business, regulatory liaison, external counsel, regulator), the decision the answer unlocks, and the date the answer is needed. Open questions sitting on the plan past their needed-by date escalate to the steering committee.

**Handoff to BAU.** The remediation closes; the obligation lands in the firm's obligation inventory with a named BAU owner role, a closure evidence pack, a monitoring cadence (quarterly control test, annual attestation, monthly KRI), and KRI or KPI pointers. A plan that ends at go-live with no BAU section will drift within twelve months. The BAU section is where the plan is finished, not the milestone tracker.

**Source trace and confidence.** Every material claim about supervisory expectation, transition mechanic, governance convention, or remediation cadence cites a source from `references/source-anchors.md`. Unsupported items carry `[evidence needed]`. The plan carries an overall confidence label; medium is the honest read while open legal questions remain or while resource asks are unfunded, regardless of how clean the rest of the plan looks.

## How this skill chains with others

`rule-to-obligation-extraction` produces the obligation list this plan operationalises. `policy-diff` produces the gap inventory this plan remediates. `compliance-testing` (and any control-gap-analysis skill) produces the control-gap input. `exam-brief` chains downstream when the trigger is a supervisory engagement; the exam-brief response-posture section points to this skill for the milestone build-out. When the implementation programme touches third parties, the TPRM skills (vendor diligence, exit-plan) are called for the relevant workstreams. When the programme touches model risk, the model-card-builder and model-validation skills are called. The plan does not duplicate those skills; it points to them.

## Sector and cross-cutting overlays

When the scope names a sector, load `references/sector-overlays.md`. The overlay carries the sector-specific governance, MRA / MRIA / consent-order convention, and BAU-handoff pattern. Same pattern for cross-cutting overlays where the engagement flags cyber, privacy, climate, or conduct.

Loading an overlay the trigger does not implicate adds noise without challenge value. Loading none when one applies is the more common failure mode.

## Quality bar

Holds across every plan. Every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by path. Unsupported items carry `[evidence needed]`. Source evidence, management assertion, public-source obligation, generated inference, and open legal question stay distinguishable. Owners are roles, never named individuals. No named institutions in narrative beyond a public defendant in a finalised consent order, and only for structural pattern. The plan stops short of approving itself; the named programme sponsor and second-line oversight role attest.

## Adaptation

Plan depth scales to criticality and audience: a high-criticality MRIA-driven plan reads long with monitor integration and monthly board reporting; a low-criticality rule-implementation reads tight with biweekly steering and quarterly board reporting; a board pre-read distills to plan summary plus top three risks plus mandatory-date posture. Source posture (public-only through connector-aware) drives what the plan can assert at high confidence and what carries `[evidence needed]`. Sector and cross-cutting overlays load from the scope. Where firm-specific PMO conventions, named monitor relationships, board-charter-driven cadence, or approved governance templates apply, they live in `references/firm-overlay.md` and are consumed when present; the plan itself stays generic.

## Pointers

`references/sector-overlays.md` and `references/cross-cutting.md` hold one section per sector or topic, and `examples.md` one per example. Find the heading and read only that section.

- `references/source-anchors.md` — citations and excerpts for the named anchors (federal banking governance and remediation, CFPB supervision, SEC and FINRA, insurance, cyber and privacy, climate, EU DORA, MRA / MRIA / consent-order convention).
- `references/sector-overlays.md` — sector overlays loaded from scope.
- `references/cross-cutting.md` — cross-cutting overlays loaded when the scope flags the topic.
- `references/firm-overlay.md` — firm-installed PMO conventions, named monitor relationships, board-charter cadence, governance templates; consumed when present.
- `templates/default-output.md` — plan template.
- `schemas/implementation-plan.schema.json` — structured-output contract for downstream consumption.
- `examples.md` — public-source-derived scenarios (CFPB Section 1071 community-bank implementation; SEC cybersecurity disclosure rule at a registered investment adviser with a public-company parent).

## Output

Two artifacts: the plan per `templates/default-output.md`, and the structured record per `schemas/implementation-plan.schema.json`. The named programme sponsor and the second-line oversight role attest; the plan is a draft until that step.

Downstream consumers: BAU obligation inventory ingests the closure evidence pack and the BAU monitoring cadence. `compliance-testing` picks up the BAU control as a recurring test scope. `exam-brief` reads the open milestones and inherits them as supervisory-history entries when the next exam window opens. The schema is the cross-skill contract; additive changes only, never silent renames. Breaking changes ship as a versioned migration with downstream skills told in advance.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
