# Troubleshooting

Common pitfalls when drafting an implementation plan.

## Owners are names, not roles

Roles survive turnover; names do not. The plan tracks roles. A separate RACI links the named individual to the role at any point in time. If an upstream input carries a named individual, translate to the role on intake (head of TPRM, CISO, head of regulatory reporting, business-line CRO, head of compliance testing).

## Acceptance criteria read like activities

"Complete training" is an activity, not evidence. "Training-completion record covers 100% of in-scope staff, attestation captured by [date], retained per recordkeeping policy" is evidence. Examiners ask for the artifact, not the activity log. Restate every activity-shaped acceptance criterion as the artifact that proves closure.

## Milestones bunch at the mandatory date

A plan with the bulk of milestones in the last month of the transition is high-risk by construction. The realistic recovery path is narrow because dependent milestones cannot start until prior ones close. Push the bulk to mid-transition where the dependency chain allows; where it does not, flag the late-loaded milestone as an explicit implementation risk with a contingency.

## No second-line review point before go-live

A plan that goes from first-line build to go-live without an explicit second-line review of control design fails the second-line gate. The regulator's expectation is that the second line independently confirms control design and challenges residual gaps before the control runs in production. Name the second-line role per workstream and place a dated review checkpoint before the milestone closes.

## Plan ends at go-live with no BAU handoff

A remediation that closes without a documented handoff into the obligation inventory and an ongoing monitoring cadence will drift within twelve months. The BAU section names the role that owns the obligation after closure, the closure evidence pack, the monitoring cadence, and the KRI or KPI that picks up signal in BAU. If the plan does not name these, it is not finished.

## Resource asks are generic

"More resources" does not survive a steering committee. Each ask names the role, the milestone it unblocks, and the consequence if declined. A steering committee can act on "one business analyst with 1071 LOS experience for Q3-Q4, otherwise milestone MS-04 slips by six weeks". It cannot act on "we need more people".

## Anchored to the wrong source

Implementation-plan structure is rule-agnostic, but the rule citations belong to the trigger. If the trigger is a final rule, anchor to the final rule and the adopting release. If the trigger is an MRA or consent order, anchor to the supervisory letter or order text and to the agency's published supervisory framework. If the trigger is a self-identified issue, anchor to the firm's issue-management policy plus the underlying obligation. Generic citation to OCC or FRB without naming the bulletin or SR letter is not anchoring.

## Tiered compliance dates collapsed to a single date

A rule with tiered effective dates (e.g., 1071 by origination volume) at an institution that touches more than one tier needs the tier-specific dates carried in the plan. Collapsing to the latest date misreads the smaller-tier obligation and risks under-compliance for the bigger-tier population.

## Governance cadence does not match criticality

A weekly working group plus a quarterly steering committee may be right for a low-criticality programme. It is wrong for an MRIA-driven programme with material customer impact, where the cadence escalates to weekly working group, biweekly steering, monthly executive risk committee, and quarterly board reporting. Match cadence to criticality; under-governing a high-criticality programme is the more common failure mode than over-governing a small one.

## Regulator-readiness checkpoints missing

Going live on the mandatory date without a mock submission, a tabletop, and a second-line walkthrough leaves the firm with no rehearsal. The first encounter with the operating control should not be the first day of supervisory attention. Three readiness checkpoints (mock reporting submission, control-design walkthrough, tabletop) sized to the rule are the practitioner pattern.

## Confidence label inflated

`high` confidence on a plan with five open legal questions and three resource asks unfunded is not credible. The honest read is `medium`. Confidence drops further when the trigger source carries `[verify section]` flags or when the gap inventory is incomplete. The label is a signal to the steering committee about what they are signing off on.

## Plan drafted from the gap list alone

A plan built only from policy-diff and control-gap output misses the supervisory and governance dimension. The plan also covers governance cadence (steering, executive, board), implementation risks, regulator-readiness checkpoints, effective-date posture, and BAU handoff. A gap-only plan reads like a punch list and lands flat with the steering committee. The full shape is the practitioner artifact.
