# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## card-authorisation-ibs-us-bank

#### Example: annual resilience-testing pack for the card-payment authorisation IBS at a US bank

Public-source-derived. No named bank or vendor. The shape mirrors a mid-tier US bank running its annual operational-resilience testing cycle on the card-payment authorisation important business service.

#### Input

- **Subject of test**: card-payment authorisation IBS, end-to-end. The chain spans the card-network connection, the firm's authorisation host, the fraud-decisioning vendor, the customer-account ledger, and the customer-facing channels.
- **Inputs already on file**: the firm's IBS register entry for card-payment authorisation; the criticality-assessment outputs for the card-network connection (critical) and the fraud-decisioning vendor (important); the prior-year test outcomes including the partial-simulation finding that the secondary network path took longer than expected to take traffic; the impact tolerance from the firm's IBS map (no more than thirty minutes of authorisation outage; no more than five percent of authorisations declined for connectivity reasons over the disruption window).
- **Engagement scope supplied**: institution = US national bank, mid-tier; primary regulators = OCC, FRB; persona = head of operational resilience; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking, payments-fintech; cross-cutting overlays = cyber.
- **DORA in scope**: false. **TLPT in scope**: false. **AI in scope**: false (the fraud-decisioning vendor uses ML, but the test cycle does not specifically test the model; that scenario sits in the next cycle).
- **Exit plan cross-reference**: exit-plan record on file for the fraud-decisioning vendor; this pack contains an exit-rehearsal scenario for that arrangement.

#### Output sketch

The skill produces the testing pack. Headlines:

- **Scenarios** — card-network primary connectivity loss (severity tolerance-breach; plausibility anchor: prior-year network-partner outage events publicly reported); fraud-decisioning vendor outage (severity near-tolerance; plausibility anchor: prior partial-simulation finding); identity-provider outage at the firm's core (severity near-tolerance; plausibility anchor: industry IdP outages publicly reported); hyperscaler primary-region failure on the firm's primary compute region (severity catastrophic; plausibility anchor: hyperscaler-region outage events publicly reported).
- **Test design** — full-live exercise on the card-network failover with the network partner (cadence: annual; preconditions: legal sign-off, network-partner participation confirmed, customer-impact-threshold safety control set; exit triggers: real customer-impact spike, real network event on an unrelated path); partial-simulation on the fraud-decisioning vendor failover (cadence: semi-annual; vendor participation: full); tabletop on the hyperscaler-region scenario (cadence: annual; participants include the hyperscaler-vendor account team as observers); walkthrough on the IdP outage scenario (cadence: annual; participants include the IdP vendor as observers).
- **Success criteria** — for each scenario, the criterion is tied to the firm's thirty-minute authorisation-outage tolerance and the five-percent-decline customer-impact threshold, not to the vendor's published SLA. The fraud-decisioning vendor's contractual ninety-percent uptime is not the test.
- **Evidence-collection plan** — telemetry from the firm's authorisation host, the network partner's status feed, the fraud-decisioning vendor's status feed, customer-channel error rates, comms-bridge transcripts, observer notes per workstream. Retention: seven years per firm policy and supervisory-inspection windows.
- **Observation method** — in-room observers per workstream (operations, technology, fraud, customer channels, communications); recorded comms-bridge transcripts; second-line risk runs the observation; first-line runs the exercise.
- **Communication plan** — internal pre-test brief to the operational-resilience committee and to the COO; in-test status to the on-call leadership group; post-test read-out to the operational-resilience committee within two weeks. Customer communication: suppressed for the partial-simulation and tabletop scenarios; pre-positioned customer-comms templates for the full-live network-failover exercise in case real customer impact triggers the exit-condition. Regulator communication: no supervisory pre-notification required for the scope this cycle; observer invitation extended to the prudential supervisor for the full-live exercise as a relationship-management posture.
- **Read-out template sections** — exercise summary; scenarios run and method per scenario; results against tolerance; findings; root-cause; remediation owners and clocks; programme-cycle implications. Locked at design time.
- **Findings-and-actions framework** — findings flow into the firm's issue-management cycle through `issue-writeup`, with each finding owned and clocked; the prior-year fraud-vendor-failover finding is on the agenda as a re-test.
- **Programme alignment** — sits inside the firm's annual operational-resilience testing programme; feeds the BCDR programme summary at the operational-resilience committee.
- **Approver** — head of operational resilience; reviewer questions clustered for the operational-resilience committee.

The pack stops at the design and the read-out template. The exercise itself is run by the firm's resilience function with the second-line role limited to challenge and observation.

#### Why this scenario matters

- **Testing against firm impact tolerance, not vendor SLA.** The fraud-decisioning vendor's contractual uptime is the vendor's commitment; the firm's thirty-minute authorisation-outage tolerance is the test. Conflating the two is a recurring failure mode.
- **A mix of methods, not tabletop everywhere.** Tabletop is the cheapest method; a programme that uses tabletop everywhere has not been tested in supervisory terms. This pack mixes full-live, partial-simulation, walkthrough, and tabletop.
- **Vendor participation is the test of the partnership.** The fraud-decisioning vendor's full participation is required; the network partner's participation in the full-live exercise is the test of the operational relationship as much as the failover technology.
- **Safety controls on the live exercise.** A full-live exercise that introduces real customer impact is a real incident. Safety controls (kill-switch, customer-impact-threshold for early termination, pre-positioned customer-comms templates) are not optional.
- **Read-out template locked at design.** The committee's narrative shape is set on day one of the cycle, not invented under time pressure on read-out day.

#### Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 6, 2023), ongoing-monitoring section [verify section].
- FFIEC IT Examination Handbook, Business Continuity Management booklet, testing-and-exercise section [verify section].
- FFIEC inter-agency cloud joint statement (Security in a Cloud Computing Environment, April 30, 2020) [verify exact title and date].
- BCBS Principles for Operational Resilience (March 2021), scenario-testing principle.

See `references/source-anchors.md` for full citations.

## dora-customer-onboarding-eu-subsidiary

#### Example: DORA resilience-testing pack for an EU subsidiary's customer-onboarding IBS, including TLPT scoping

Public-source-derived. No named firm or vendor. The shape mirrors a credit-institution EU subsidiary preparing its digital operational resilience testing programme for the customer-onboarding important business service, with an AI vendor in the chain and TLPT scoping under consideration.

#### Input

- **Subject of test**: customer-onboarding IBS, end-to-end. The chain spans the firm's onboarding portal, the ID-document-verification AI vendor (foundation-model-driven), the document-storage vendor, the firm's KYC orchestration service, the sanctions-screening vendor, and the customer-account provisioning workflow.
- **Inputs already on file**: the firm's IBS map naming customer-onboarding as critical; the criticality-assessment outputs for the AI vendor (critical-or-important-function), the document-storage vendor (critical), and the sanctions-screening vendor (important); the firm's DORA register draft; the prior-year basic-testing-programme summary; the firm's impact tolerance for onboarding (no more than four hours of new-application processing disruption; no more than two percent of in-flight applications failed for technology reasons over the disruption window).
- **Engagement scope supplied**: institution = credit-institution EU subsidiary; primary regulators = ECB SSM, national competent authority; persona = head of operational resilience and head of ICT risk jointly; source posture = public-plus-firm-policy; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **DORA in scope**: true. **TLPT in scope**: under designation review; the firm is preparing for designation under DORA Article 26 [verify subarticle] and the testing-programme design includes a TLPT-scoping line for the onboarding chain. **AI in scope**: true.
- **Exit plan cross-reference**: exit-plan records on file for the AI vendor and the document-storage vendor; this pack contains an exit-rehearsal scenario for the AI vendor and pulls forward an open finding from the AI-vendor exit plan that prompt-template portability is unproven.

#### Output sketch

The skill produces the testing pack. Headlines:

- **Scenarios** — AI-vendor outage during peak onboarding window (severity tolerance-breach; plausibility anchor: prior AI-API outages publicly reported); AI-vendor model regression that drives a spike in false rejections of valid IDs (severity tolerance-breach; plausibility anchor: prior model-drift events publicly reported in adjacent industries; AI-specific true); ICT-third-party concentration scenario where the AI vendor and the document-storage vendor share an upstream hyperscaler region that fails (severity catastrophic; plausibility anchor: hyperscaler-region outage events publicly reported); identity-provider outage at the firm's core during onboarding peak (severity near-tolerance); document-storage vendor data-integrity event affecting in-flight applications (severity near-tolerance).
- **Test design** — tabletop for the AI-regression scenario (cadence: semi-annual; participants include the model-risk function, the AI-governance committee chair, the customer-experience lead, the legal lead on customer-impact remediation; AI vendor invited as observer); partial-simulation for the AI-vendor outage scenario with the substitute foundation-model vendor in shadow on a sanitised prompt subset (cadence: annual; vendor participation: full for the substitute, observer for the incumbent; preconditions include the substitute vendor's diligence pack and `llm-vendor-evidence-review` record on file); tabletop for the hyperscaler-region scenario (cadence: annual; participants include both vendors' account teams as observers); walkthrough for the IdP scenario (cadence: annual); partial-simulation for the document-storage data-integrity scenario (cadence: annual). TLPT-scoping is a separate workstream against the customer-onboarding chain; the testing pack records the scoping line and the legal-and-supervisory engagement preconditions.
- **Success criteria** — tied to the firm's four-hour onboarding-disruption tolerance and the two-percent in-flight-application-failure threshold. For the AI-regression scenario, additional criterion on false-rejection rate against the firm's customer-experience tolerance (a different threshold than the disruption tolerance). The AI vendor's contractual ninety-nine-point-five-percent availability is not the test.
- **Evidence-collection plan** — telemetry from the firm's onboarding portal, AI-vendor API status feeds, document-storage vendor status feeds, sanctions-screening vendor status feeds, customer-channel error rates, model-output samples for the AI-regression scenario (with prompt redaction per the privacy overlay), comms-bridge transcripts, observer notes per workstream. Retention per the firm's policy and DORA supervisory-inspection windows.
- **Observation method** — in-room observers per workstream; recorded comms-bridge; second-line risk and ICT-risk function jointly observe; first-line and the model-risk function jointly run the AI-regression and AI-outage scenarios.
- **Communication plan** — internal pre-test brief to the operational-resilience committee and to the AI risk committee; in-test status to the on-call leadership group; post-test read-out to the operational-resilience committee and the AI risk committee within two weeks. Customer communication: suppressed for the tabletop and partial-simulation scenarios; pre-positioned customer-facing messaging templates for any scenario that may surface real applicant impact. Regulator communication: SSM joint supervisory team observation invitation extended for the AI-vendor outage partial-simulation; TLPT supervisory engagement is its own workstream.
- **Read-out template sections** — exercise summary; scenarios run and method per scenario; results against tolerance; findings; root-cause; remediation owners and clocks; programme-cycle implications; DORA-programme-cycle implications including any updates needed to the digital operational resilience testing programme document. Locked at design time.
- **Findings-and-actions framework** — findings flow into the firm's issue-management cycle through `issue-writeup`. The open AI-vendor-exit-plan finding on prompt-template portability gets re-tested in the AI-outage partial-simulation; the result feeds back into the exit-plan testing history.
- **Programme alignment** — pack sits inside the firm's digital operational resilience testing programme under DORA Article 24 [verify subarticle]; the TLPT-scoping line carries the Article 26 [verify subarticle] preconditions.
- **Approver** — head of operational resilience and head of ICT risk jointly; reviewer questions clustered for the operational-resilience committee and the AI risk committee.

The pack stops at the design and the read-out template. TLPT-scoping is recorded as a workstream with its own approver path.

#### Why this scenario matters

- **DORA programme alignment is the spine.** The pack is not just a one-off cycle; it sits inside the digital operational resilience testing programme under Article 24 [verify subarticle] and feeds the supervisory submission.
- **AI-specific scenarios are real scenarios.** Vendor model regression and prompt-template portability are not generic vendor outages; they need their own scenario design and they need the model-risk function in the room.
- **Concentration scenarios are part of the testing programme.** The AI vendor and the document-storage vendor sharing an upstream hyperscaler is the kind of single-point-of-failure that surfaces in `concentration-risk-review` and gets tested here.
- **TLPT is its own workstream.** TLPT-scoping requires legal sign-off, supervisory engagement under TIBER-EU methodology, and a different testing posture; the pack records the scoping line but does not collapse TLPT into the operational testing cycle.
- **Substitute-vendor evidence is a precondition for the partial-simulation.** Running a partial-simulation that exercises the substitute AI vendor requires the substitute's own vendor-diligence record and `llm-vendor-evidence-review` record on file. The pack flags these as preconditions, not as in-test work.
- **The AI risk committee is in the read-out path.** AI-specific findings cluster for the AI risk committee; non-AI findings cluster for the operational-resilience committee. Different forums; different decisions.

#### Anchors

- DORA, Regulation (EU) 2022/2554, Articles 24-26 [verify subarticle numbering against the official OJ text] — digital operational resilience testing programme; advanced testing including TLPT.
- TIBER-EU framework (ECB) [verify reference and current version] — TLPT methodology.
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02) [verify section] — outsourcing-test posture.
- BCBS Principles for Operational Resilience (March 2021), scenario-testing and ICT principles.
- NIST AI Risk Management Framework 1.0 (NIST AI 100-1, January 2023), Map and Govern functions [verify subsection].

See `references/source-anchors.md` for full citations.

## troubleshooting

### Troubleshooting: resilience-testing-pack

Recurring pitfalls. Read before producing the pack and again before sign-off.

#### Tolerance vs SLA

##### Designing tests against vendor SLAs instead of firm impact tolerance

The vendor's published service-level commitment is what the vendor has agreed to. The firm's impact tolerance is what the important business service must hold within. They usually differ; treating the SLA as the test understates what the firm has to evidence. Calibrate criteria to the IBS map's tolerance lines, not to the contractual commitment.

##### Setting tolerance from the architecture diagram

A multi-cloud or active-active diagram is not evidence that failover holds within tolerance. Tolerance is what the test demonstrates; the diagram is the hypothesis under test.

#### Scenario set

##### Skipping severe-but-plausible scenarios for "low likelihood"

Severe-but-plausible is the supervisory frame, not a probability judgement. Scenarios that have happened in adjacent firms are plausible by definition. A hyperscaler-region failure, an identity-provider outage, a payments-rails disruption, a major fraud-decision vendor outage: each has a public record in adjacent institutions.

##### Designing scenarios only against the primary path

The primary path is the easy test. Scenarios should also stress secondary paths, fourth-party dependencies (hyperscaler region, BIN-sponsor processor, KYC vendor, foundation-model upstream), and concentration points surfaced in `concentration-risk-review`.

##### Ignoring AI-specific scenarios on an AI-in-scope chain

Vendor model regression, eval drift on the deployed system, vendor model deprecation mid-cycle, prompt-injection on the deployed agent, training-data incident at the vendor: none of these collapse into generic vendor-outage language. The model-risk function belongs in the room when these scenarios run.

#### Method mix

##### Tabletop everywhere

Tabletop is the cheapest, lowest-fidelity method. A programme that uses tabletop for every scenario has not been tested in supervisory terms. A critical-or-important arrangement that has only ever been tabletop-tested is a finding waiting to be written.

##### Full-live everywhere

The opposite failure mode. Full-live exercises that introduce real customer impact are real incidents. They run for a small subset of scenarios, with safety controls, and not annually for every chain.

##### Treating data-extraction-rehearsal and shadow-cutover as outside the testing pack

These are test methods. The exit-rehearsal scenarios live in the testing pack; cross-link to the relevant `exit-plan` record.

#### Vendor participation

##### Excluding vendor participation

A test the vendor declines to join tests the technology, not the partnership. Vendor participation is a real test. Where the vendor declines, that itself is a finding for the diligence cycle.

##### Treating vendor account-team observation as participation

Account-team observers are not the vendor's incident-response function. Specify which vendor function is in the test and what they are doing.

#### Safety controls

##### Running a partial-simulation or live test without exit triggers

A live test that exceeds the customer-impact threshold is a real incident. Exit triggers (customer-impact volume, real incident on an unrelated path, vendor-declared issue, supervisor intervention) are mandatory for partial-simulation and full-live exercises.

##### No kill-switch and no rollback

A full-live exercise that cannot be aborted cleanly is reckless. Kill-switch and rollback procedures are preconditions, not nice-to-haves.

##### Suppressing customer-comms templates

For any scenario that may surface real customer impact, customer-facing comms templates are pre-positioned, even if the plan is to suppress comms during the test. The exit-condition path needs a comms-ready posture.

#### Read-out and findings

##### Producing a test design without a read-out template

The committee needs the post-exercise narrative shape on day one of the cycle, not on read-out day. Lock the template at design time; revise after the exercise only if a real finding requires a different shape.

##### Treating findings as ad-hoc

Findings flow into the firm's issue-management cycle through `issue-writeup`. A finding without an owner and a clock dies in the post-exercise deck. Each finding gets recorded with owner, due date, verification path, and an issue ID.

##### Skipping the lessons-learned capture

Lessons-learned are wider than findings (process improvements, runbook updates, training implications, programme-design adjustments). Filed against the IBS or arrangement, not against the test cycle, so the next cycle benefits.

#### Programme alignment

##### Producing the pack outside the firm's annual programme

A one-off pack that does not cite where it sits in the firm's annual operational-resilience testing programme is harder to sustain and harder to defend at the supervisor's read-out. Cite the programme; cite the prior cycle; cite the next cycle trigger.

##### Forgetting the regulator-observation posture

Some programmes have a regulator-observation expectation (SCI industry-wide test for SCI entities, advanced testing under DORA Article 26 [verify subarticle]). Build it in or call out the absence with the rationale.

##### Treating TLPT as part of the operational testing cycle

Threat-led penetration testing carries its own legal-and-supervisory engagement model under TIBER-EU and DORA Article 26 [verify subarticle]. The operational testing pack records the scoping line; TLPT itself runs as a separate workstream.

#### Boundary

##### Producing the pack as the test

This skill drafts the design and the read-out template. The exercise itself is run by the firm's resilience function with the second-line role limited to challenge and observation as appropriate. A pack that conflates design with execution has overstepped.

##### Letting the pack owner sit only in second line

Second line designs and observes; first line runs the exercise. The accountable executive is the BCDR lead or the head of operational resilience for IBS-level packs and the head of TPRM for arrangement-level packs. A pack owned only by second line has the wrong ownership.

#### Output discipline

##### Citing without sections

Every regulator citation in the pack carries a section reference or a `[verify section]` placeholder. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the pack body.

##### Marking unsupported claims silently

Use `[evidence needed]` explicitly. An inferred claim presented as evidenced is the failure mode.

##### Closing with too much certainty

The confidence label is `high` only when the source posture, the testing history, and the named-approver review line up. `medium` and `low` are normal for a first cycle; `unknown` is honest where preconditions (substitute-vendor diligence, vendor participation confirmation, legal sign-off for live tests) have not closed.
