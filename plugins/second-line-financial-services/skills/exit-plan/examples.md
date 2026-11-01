# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## core-banking-saas-community-bank

#### Example: core-banking SaaS exit plan at a community bank

Public-source-derived. No named vendor or bank. The shape mirrors a common exit-plan pattern at $2-10B community banks running a hosted core-banking platform that supports deposit accounting, loan servicing, and the general ledger.

#### Input

- **Vendor**: a US-based core-banking SaaS provider hosting deposit, loan, and GL modules in a single-tenant configuration on a hyperscaler.
- **Service**: end-to-end core-banking platform; teller, ATM, online banking and bill-pay integrations; nightly batch and report generation.
- **Business process supported**: deposit-account servicing, consumer-loan servicing, regulatory reporting feed.
- **Important business service**: deposit-account servicing (firm IBS map names a 24-hour impact tolerance for transactional outage and a longer tolerance for ancillary reporting).
- **Inputs already on file**: vendor-diligence record (criticality = critical; subcontractors include the hyperscaler and two integration vendors; data_access includes NPI, PCI, books-and-records; residual risk = high; exit_plan_status = missing); contract executed three years ago carrying a six-month transition-assistance commitment and a fee for early termination; FFIEC inter-agency cloud joint statement (April 2020) is on the firm's source list.
- **Engagement scope supplied**: institution = state member bank; primary regulators = FRB, state DFI; persona = head of operational resilience; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **AI vendor**: false.

#### Output sketch

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

#### Why this scenario matters

- **Time-to-transition vs tolerance is honest.** The plan documents a tolerance breach rather than reporting "ten months" because that fits the policy. The skill must be honest about the breach and surface it to the IBS owner and the COO.
- **Trigger-set covers all four categories.** A plan that covers only vendor-driven triggers misses regulator-driven and market-driven scenarios that have shorter lead times.
- **The contract is not the plan.** The vendor's six-month transition-assistance commitment is a clause; the firm's playbook is the plan. Different things.
- **Customer notice and regulator notice are both real clocks.** Reg DD and Reg E for customers; FRB and state DFI for the regulator. Lead times must be planned, not improvised on the day.
- **Bank Service Company Act examination access continues through wind-down.** The contract clause and the actual evidence-preservation choreography are both required.
- **Testing cadence is the difference between paper and posture.** A plan that has never been tested gets surfaced as a finding even if the plan itself reads complete.

#### Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023) §V ongoing monitoring and §VI termination [verify section].
- FFIEC IT Examination Handbook — Outsourcing Technology Services booklet, contingency planning and termination expectations [verify section].
- FFIEC IT Examination Handbook — Business Continuity Management booklet, testing-and-exercise section [verify section].
- FFIEC inter-agency cloud joint statement (April 2020).
- Bank Service Company Act, 12 USC §1867(c).
- Reg DD, 12 CFR §1030.5 (change-in-terms notice).
- Reg E, 12 CFR §1005.8 (change-in-terms notice).

See `references/source-anchors.md` for full citations.

## foundation-model-api-eu-subsidiary

#### Example: foundation-model API exit plan at an EU subsidiary

Public-source-derived. No named vendor or firm. The shape mirrors a DORA-in-scope arrangement at a credit-institution EU subsidiary using a foundation-model API for KYC narrative summarisation in the AML investigations workflow.

#### Input

- **Vendor**: a non-EU foundation-model API provider with an EU data-residency commitment, a published system card, and an enterprise data-handling addendum.
- **Service**: foundation-model API consumed by the firm's AML case-management system to summarise narrative artefacts (transaction-explanation memos, customer-correspondence excerpts, public-source notes) for AML investigators.
- **Business process supported**: AML investigations and SAR-narrative drafting support.
- **Important business service**: financial-crime investigations (firm IBS map names a tolerance for investigator workflow disruption).
- **Inputs already on file**: vendor-diligence record (criticality = important; subcontractors include the upstream cloud providers; data_access includes model-prompts containing customer name, narrative excerpts, and identifiers; residual risk = medium; exit_plan_status = draft); the executed enterprise contract carrying training-use disabled by default with a 30-day abuse-monitoring exception; system card and trust-and-safety pages on file; `llm-vendor-evidence-review` record open with `eval_evidence_status = deferred-to-evidence-review`.
- **Engagement scope supplied**: institution = credit-institution EU subsidiary; primary regulators = ECB SSM, national competent authority; persona = head of operational resilience; source posture = public-plus-firm-policy; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **DORA in scope**: true. The arrangement supports a function the firm has classified as critical or important under DORA Article 28(8); Article 30(3) [verify subarticle] expects exit-strategy and transitional-support clauses in the contract.
- **AI vendor**: true.

#### Output sketch

The skill produces an exit plan. Headlines:

- **Triggers** — vendor-driven (vendor-side enterprise terms change, model deprecation, prolonged regulator-driven service restriction in non-EU jurisdiction); firm-driven (model-risk-committee decision to switch vendors after eval drift, AI-policy-driven retirement of the use case); regulator-driven (DORA-driven supervisory direction, EU AI Act-driven obligation that the vendor cannot meet, customer-data-incident at the vendor with EU regulator-led action); market-driven (vendor distress, geopolitical sanctions affecting the vendor's home jurisdiction, hyperscaler-region disruption).
- **Transition target options** — substitute-vendor as primary (substitute-foundation-model with portable prompt-template library and sanitised RAG corpus, viability `viable` only after prompt-template portability and RAG corpus migration are tested; in-source as `weak` because the firm has no GPU capacity for a self-hosted model of comparable capability; retire-service-and-fall-back-to-pre-AI-investigator-workflow as `viable` for transitional use, viability `viable` as a graceful-degradation option). Selected primary: substitute-vendor; secondary: graceful-degradation to pre-AI workflow.
- **Time-to-transition vs tolerance** — `near`. Substitute-vendor cutover is months not weeks; graceful-degradation cutover is days because the pre-AI workflow still exists. Within tolerance under graceful-degradation; near-tolerance under substitute-vendor cutover.
- **Data return and destruction** — prompts, completions, and any vendor-side abuse-monitoring retention must be returned and destroyed; vendor must provide a destruction certificate covering the abuse-monitoring window and any logs; encryption-key revocation and credential rotation choreographed against cutover.
- **AI-specific transition considerations** — prompt-template portability is unproven (templates have only ever been engineered against the incumbent model); RAG corpus migration requires re-embedding and re-indexing because vector spaces are model-specific; fine-tune artifacts are not in scope for this use case; model-version pin handling driven by vendor's deprecation-notice clock; carrier-side guardrails (PII redaction at prompt entry, output-quality gates) need rework on the substitute model; agent tool offboarding not applicable (no agent integration in scope).
- **Knowledge transfer** — prompt library, evaluation harness, prompt-template engineering decisions, redaction-rule library all owned firm-side; vendor knowledge transfer covers operational integration only.
- **Contract termination mechanics** — clause reference cited; termination-for-convenience present; transition-assistance period limited to API access continuity; regulator-directed-termination clause absent — flag to `contract-gap-review` because DORA Article 30(3) [verify subarticle] expects this; in-flight data lock-in low because deployment is stateless other than the abuse-monitoring window.
- **Customer notice posture** — no customer-facing change at cutover (the AI is in the investigator workflow, not customer-facing). No regulated customer-notice clock applies.
- **Regulator notice posture** — DORA Article 28 [verify subarticle] register-of-information update on the substitute vendor required; ECB SSM notification posture per the firm's significant-incident reporting policy where exit triggers on a vendor incident; supervisory engagement on the model-risk-committee-driven switch.
- **Supervisory readiness during transition** — model-risk evidence carries over (the model-risk evaluation lives in the firm's MRM, not at the vendor); evidence of evaluation on the substitute model required before cutover; the substitute model's diligence pack and `llm-vendor-evidence-review` record both required as preconditions.
- **Fourth-party dependencies** — vendor's upstream compute provider is not the firm's choice; geopolitical exposure on the upstream provider feeds the trigger set.
- **Testing plan** — quarterly tabletop with model-risk and TPRM functions; annual rehearsal of switching vendors for a low-risk subset of prompts (sandboxed); data-extraction rehearsal annually. `last_test_date = none`, `last_test_outcome = never-tested`.
- **Cost estimate range** — moderate range; cost drivers named (prompt re-engineering effort, RAG re-embedding, evaluation re-baselining, dual-vendor period).
- **Approver** — head of operational resilience and head of model risk jointly; reviewer questions clustered for the AI risk committee.

The plan stops at the recommendation.

#### Why this scenario matters

- **DORA Article 28(8) is the primary anchor.** The exit-strategy expectation drives the plan's existence; the contract gap on Article 30(3) [verify subarticle] exit-strategy clauses gets surfaced and chained to `contract-gap-review`.
- **Prompt and RAG portability is the AI-specific transition-engineering problem.** A non-AI exit plan would treat data extraction as schema mapping; an AI vendor exit plan must address prompt re-engineering and re-embedding because vector spaces and model behaviour are model-specific.
- **Graceful degradation is a real option for AI vendors.** The pre-AI investigator workflow still exists; treating it as a fallback keeps the impact tolerance achievable under any forced cutover.
- **The substitute vendor's diligence is a precondition, not an afterthought.** A new model vendor needs its own `vendor-diligence` record and `llm-vendor-evidence-review` record before cutover.
- **Customer notice does not always apply.** AI used in investigator workflows triggers no customer-facing notice clock. Regulator notice still applies via DORA register update and SSM-level supervisory engagement.

#### Anchors

- DORA, Regulation (EU) 2022/2554, Article 28(8) exit strategies [verify subarticle] and Article 30(3) exit-related contractual provisions [verify subarticle].
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02), exit-strategy section [verify section].
- NIST AI Risk Management Framework 1.0 (NIST AI 100-1, January 2023), Govern function [verify subsection].
- NIST AI 600-1, Generative AI Profile (July 2024) [verify subsection].
- EU AI Act, Regulation (EU) 2024/1689 [verify Annex III item number where applicable].

See `references/source-anchors.md` for full citations.

## troubleshooting

### Troubleshooting: exit-plan

Recurring pitfalls. Read before producing the plan and again before sign-off.

#### Plan vs contract

##### Treating the contract's transition-assistance period as the exit plan

The contract clause is a vendor commitment. The plan is the firm's playbook. They are different things. The plan reads the clause and goes well beyond it: trigger set, transition target options, time-to-transition test against tolerance, data return-and-destruction choreography, customer-notice posture, regulator-notice posture, supervisory readiness during transition, testing cadence, named approver. A plan that simply restates the clause has not been written.

##### Skipping the regulator-directed-termination clause read

For DORA-in-scope arrangements, Article 30(3) [verify subarticle] expects the contract to preserve the firm's ability to terminate on regulator direction without penalty. For banking arrangements, supervisory expectations are similar in substance. Where the clause is absent, the plan must flag the gap and chain to `contract-gap-review`.

#### Trigger and target set

##### Covering only one trigger category

Vendor-driven, firm-driven, regulator-driven, market-driven all need treatment. Lead times differ across categories: distress and unexpected termination usually have shorter lead times than annual recertification or planned migration. A plan that covers only the planned-transition path leaves the firm exposed on the day a different trigger fires.

##### Relying on a single transition target

Substitute-vendor as primary is normal; it is rarely the only viable path. In-source, hybrid, retire-service, and graceful-degradation should each be assessed honestly. A plan with one option only is a single point of failure dressed up as a plan.

##### Treating "we use multi-cloud" as a free exit posture

Multi-cloud architecture without tested failover is marketing, not resilience. The exit plan must reflect what has actually been tested, not what the architecture diagram suggests is possible.

#### Time-to-transition vs tolerance

##### Skipping the impact-tolerance test

An exit plan that takes longer than the impact tolerance for the supported important business service is itself a finding. Document the gap. The COO and the IBS owner need to see the breach honestly, not dressed up.

##### Setting the time-to-transition to the substitute vendor's marketing claim

The substitute's onboarding-time claim is a starting point, not the test. The realistic time-to-transition includes substitute-vendor diligence, contract negotiation, data migration, end-customer notice, regulator notice, dual-running, UAT, and cutover. Each leg has dependencies; sum them honestly.

#### Data return and destruction

##### Treating data extraction as solved by "we have an export API"

Exports need format compatibility with the substitute, schema mapping, validation against firm-of-record, integrity verification, and destruction evidence afterwards. An export API is the start of the work, not its conclusion.

##### Missing derivative artifacts in destruction scope

Caches, indexes, vector embeddings (AI vendors), model fine-tune artifacts (AI vendors), backup tapes, BCDR replicas, log archives. The destruction obligation reaches each of these explicitly or it leaks.

##### Skipping the carve-outs

Lawful retention by the vendor (regulatory archive, fraud investigation, legal hold, AI-vendor abuse-monitoring windows) must be carved out explicitly with the retention period named and the post-retention destruction commitment carried.

#### Fourth parties

##### Forgetting fourth-party dependencies

The vendor's own subcontractors are often the bottleneck on transition. Hyperscaler region, BIN-sponsor processor, KYC vendor, fund-accountant subcontractor, foundation-model upstream: any of these can determine the realistic transition window.

##### Treating subcontractor flow-down as visibility

Flow-down clauses do not equal visibility. The exit plan must reflect what the firm actually knows about the subcontractor chain.

#### Regulator and customer notice

##### Missing the regulator-notification posture

Exit events for critical or important functions usually require supervisory notification: DORA Article 28 register-of-information update, bank-regulator material-vendor-change notification, Form ADV brochure update, Form N-CEN service-provider change, NAIC ORSA update, NYDFS event-reporting. The plan must include the notification clock and the supervisory-engagement posture, not be a surprise on the day.

##### Setting the customer-notice clock to the easiest one

Where multiple consumer-protection clocks apply (Reg DD §1030.5 for deposit accounts, Reg E §1005.8 for EFT services, Reg E §1005.18 for prepaid, NACHA Operating Rules for ACH-customer-impactful changes), the longer of the operative clocks usually controls. Pin to the operative rule on the day.

##### Treating BaaS program-end as the program-operator's problem

The sponsor bank carries customer-notice responsibility, deposit-insurance-representation responsibility, and end-customer reconciliation responsibility under the July 2024 Joint Statement [verify title and date]. The program operator cannot accept these obligations on the bank's behalf.

#### Supervisory readiness during transition

##### Skipping the dual-running window

A multi-month transition runs alongside live supervisory and audit activity. Evidence-collection from both vendors, the seam dated, MRA / MRIA exposure, examination-access continuity (Bank Service Company Act §1867(c) for banks, books-and-records continuity for advisers and BDs) all live here.

##### Failing to pre-brief an examination scheduled in the cutover quarter

Where a planned safety-and-soundness, conduct-of-business, or thematic examination falls in the transition window, the plan should reflect a pre-brief to the examiner and an artifact set ready for inspection.

#### Testing cadence

##### Skipping the test

A plan that has never been tested has unknown viability. Document the testing cadence and the last-test outcome (even if "no test yet"), and surface it as a reviewer question. A plan without a test history is paper, not posture.

##### Treating tabletop as sufficient for a critical arrangement

Tabletop is the entry-level method. For critical arrangements the plan should escalate over time: walkthrough, partial-simulation, data-extraction-rehearsal, shadow-cutover. Full-live exercise may be out of reach for cost reasons; the plan documents the trade-off honestly.

#### AI vendor specifics

##### Assuming prompt templates and RAG corpora are vendor-portable

Prompt behaviour is model-specific; templates and retrieval pipelines need rework when the underlying model changes. Vector spaces are model-specific too; embeddings have to be re-computed. Build in an AI-specific transition-engineering line item.

##### Treating the AI-vendor exit as a generic data-extraction problem

Prompts, completions, vector embeddings, fine-tune artifacts, model-version pin handling, guardrail and eval porting, agent-tool revocation are AI-specific. None of these collapse cleanly into generic data-extraction language.

##### Skipping model-version pin handling

The deployed checkpoint at termination is a moving target. The plan must address whether the vendor provides a final-version export and whether deprecation pressure forces an earlier transition.

##### Missing the substitute model's evidence-pack precondition

A new model vendor needs its own `vendor-diligence` record and `llm-vendor-evidence-review` record before cutover. The exit plan should call out the precondition.

#### Ownership

##### Letting the exit-plan owner be a procurement role only

The accountable executive should be the IBS owner or the head of operational resilience. Procurement supports execution but does not own customer-facing impact. A plan owned only by procurement misses the IBS lens.

##### Treating the plan as the decision

The plan stops at the recommendation. The named approver decides per the firm's third-party-risk and operational-resilience policy for the criticality tier.

#### Output discipline

##### Citing without sections

Every regulator citation in the plan carries a section reference or a `[verify section]` placeholder. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the plan body.

##### Marking unsupported claims silently

Use `[evidence needed]` explicitly. An inferred claim presented as evidenced is the failure mode.

##### Closing with too much certainty

The confidence label is `high` only when the source posture, the testing history, and the named-approver review line up. `medium` and `low` are normal for a plan with a thin testing history; `unknown` is honest where the substitute path has not been validated against tolerance.
