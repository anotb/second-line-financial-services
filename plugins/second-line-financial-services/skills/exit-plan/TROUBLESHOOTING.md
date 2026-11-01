# Troubleshooting: exit-plan

Recurring pitfalls. Read before producing the plan and again before sign-off.

## Plan vs contract

### Treating the contract's transition-assistance period as the exit plan

The contract clause is a vendor commitment. The plan is the firm's playbook. They are different things. The plan reads the clause and goes well beyond it: trigger set, transition target options, time-to-transition test against tolerance, data return-and-destruction choreography, customer-notice posture, regulator-notice posture, supervisory readiness during transition, testing cadence, named approver. A plan that simply restates the clause has not been written.

### Skipping the regulator-directed-termination clause read

For DORA-in-scope arrangements, Article 30(3) [verify subarticle] expects the contract to preserve the firm's ability to terminate on regulator direction without penalty. For banking arrangements, supervisory expectations are similar in substance. Where the clause is absent, the plan must flag the gap and chain to `contract-gap-review`.

## Trigger and target set

### Covering only one trigger category

Vendor-driven, firm-driven, regulator-driven, market-driven all need treatment. Lead times differ across categories: distress and unexpected termination usually have shorter lead times than annual recertification or planned migration. A plan that covers only the planned-transition path leaves the firm exposed on the day a different trigger fires.

### Relying on a single transition target

Substitute-vendor as primary is normal; it is rarely the only viable path. In-source, hybrid, retire-service, and graceful-degradation should each be assessed honestly. A plan with one option only is a single point of failure dressed up as a plan.

### Treating "we use multi-cloud" as a free exit posture

Multi-cloud architecture without tested failover is marketing, not resilience. The exit plan must reflect what has actually been tested, not what the architecture diagram suggests is possible.

## Time-to-transition vs tolerance

### Skipping the impact-tolerance test

An exit plan that takes longer than the impact tolerance for the supported important business service is itself a finding. Document the gap. The COO and the IBS owner need to see the breach honestly, not dressed up.

### Setting the time-to-transition to the substitute vendor's marketing claim

The substitute's onboarding-time claim is a starting point, not the test. The realistic time-to-transition includes substitute-vendor diligence, contract negotiation, data migration, end-customer notice, regulator notice, dual-running, UAT, and cutover. Each leg has dependencies; sum them honestly.

## Data return and destruction

### Treating data extraction as solved by "we have an export API"

Exports need format compatibility with the substitute, schema mapping, validation against firm-of-record, integrity verification, and destruction evidence afterwards. An export API is the start of the work, not its conclusion.

### Missing derivative artifacts in destruction scope

Caches, indexes, vector embeddings (AI vendors), model fine-tune artifacts (AI vendors), backup tapes, BCDR replicas, log archives. The destruction obligation reaches each of these explicitly or it leaks.

### Skipping the carve-outs

Lawful retention by the vendor (regulatory archive, fraud investigation, legal hold, AI-vendor abuse-monitoring windows) must be carved out explicitly with the retention period named and the post-retention destruction commitment carried.

## Fourth parties

### Forgetting fourth-party dependencies

The vendor's own subcontractors are often the bottleneck on transition. Hyperscaler region, BIN-sponsor processor, KYC vendor, fund-accountant subcontractor, foundation-model upstream: any of these can determine the realistic transition window.

### Treating subcontractor flow-down as visibility

Flow-down clauses do not equal visibility. The exit plan must reflect what the firm actually knows about the subcontractor chain.

## Regulator and customer notice

### Missing the regulator-notification posture

Exit events for critical or important functions usually require supervisory notification: DORA Article 28 register-of-information update, bank-regulator material-vendor-change notification, Form ADV brochure update, Form N-CEN service-provider change, NAIC ORSA update, NYDFS event-reporting. The plan must include the notification clock and the supervisory-engagement posture, not be a surprise on the day.

### Setting the customer-notice clock to the easiest one

Where multiple consumer-protection clocks apply (Reg DD §1030.5 for deposit accounts, Reg E §1005.8 for EFT services, Reg E §1005.18 for prepaid, NACHA Operating Rules for ACH-customer-impactful changes), the longer of the operative clocks usually controls. Pin to the operative rule on the day.

### Treating BaaS program-end as the program-operator's problem

The sponsor bank carries customer-notice responsibility, deposit-insurance-representation responsibility, and end-customer reconciliation responsibility under the July 2024 Joint Statement [verify title and date]. The program operator cannot accept these obligations on the bank's behalf.

## Supervisory readiness during transition

### Skipping the dual-running window

A multi-month transition runs alongside live supervisory and audit activity. Evidence-collection from both vendors, the seam dated, MRA / MRIA exposure, examination-access continuity (Bank Service Company Act §1867(c) for banks, books-and-records continuity for advisers and BDs) all live here.

### Failing to pre-brief an examination scheduled in the cutover quarter

Where a planned safety-and-soundness, conduct-of-business, or thematic examination falls in the transition window, the plan should reflect a pre-brief to the examiner and an artifact set ready for inspection.

## Testing cadence

### Skipping the test

A plan that has never been tested has unknown viability. Document the testing cadence and the last-test outcome (even if "no test yet"), and surface it as a reviewer question. A plan without a test history is paper, not posture.

### Treating tabletop as sufficient for a critical arrangement

Tabletop is the entry-level method. For critical arrangements the plan should escalate over time: walkthrough, partial-simulation, data-extraction-rehearsal, shadow-cutover. Full-live exercise may be out of reach for cost reasons; the plan documents the trade-off honestly.

## AI vendor specifics

### Assuming prompt templates and RAG corpora are vendor-portable

Prompt behaviour is model-specific; templates and retrieval pipelines need rework when the underlying model changes. Vector spaces are model-specific too; embeddings have to be re-computed. Build in an AI-specific transition-engineering line item.

### Treating the AI-vendor exit as a generic data-extraction problem

Prompts, completions, vector embeddings, fine-tune artifacts, model-version pin handling, guardrail and eval porting, agent-tool revocation are AI-specific. None of these collapse cleanly into generic data-extraction language.

### Skipping model-version pin handling

The deployed checkpoint at termination is a moving target. The plan must address whether the vendor provides a final-version export and whether deprecation pressure forces an earlier transition.

### Missing the substitute model's evidence-pack precondition

A new model vendor needs its own `vendor-diligence` record and `llm-vendor-evidence-review` record before cutover. The exit plan should call out the precondition.

## Ownership

### Letting the exit-plan owner be a procurement role only

The accountable executive should be the IBS owner or the head of operational resilience. Procurement supports execution but does not own customer-facing impact. A plan owned only by procurement misses the IBS lens.

### Treating the plan as the decision

The plan stops at the recommendation. The named approver decides per the firm's third-party-risk and operational-resilience policy for the criticality tier.

## Output discipline

### Citing without sections

Every regulator citation in the plan carries a section reference or a `[verify section]` placeholder. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the plan body.

### Marking unsupported claims silently

Use `[evidence needed]` explicitly. An inferred claim presented as evidenced is the failure mode.

### Closing with too much certainty

The confidence label is `high` only when the source posture, the testing history, and the named-approver review line up. `medium` and `low` are normal for a plan with a thin testing history; `unknown` is honest where the substitute path has not been validated against tolerance.
