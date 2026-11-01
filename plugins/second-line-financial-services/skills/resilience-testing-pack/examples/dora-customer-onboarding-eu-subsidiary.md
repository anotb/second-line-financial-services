## Example: DORA resilience-testing pack for an EU subsidiary's customer-onboarding IBS, including TLPT scoping

Public-source-derived. No named firm or vendor. The shape mirrors a credit-institution EU subsidiary preparing its digital operational resilience testing programme for the customer-onboarding important business service, with an AI vendor in the chain and TLPT scoping under consideration.

## Input

- **Subject of test**: customer-onboarding IBS, end-to-end. The chain spans the firm's onboarding portal, the ID-document-verification AI vendor (foundation-model-driven), the document-storage vendor, the firm's KYC orchestration service, the sanctions-screening vendor, and the customer-account provisioning workflow.
- **Inputs already on file**: the firm's IBS map naming customer-onboarding as critical; the criticality-assessment outputs for the AI vendor (critical-or-important-function), the document-storage vendor (critical), and the sanctions-screening vendor (important); the firm's DORA register draft; the prior-year basic-testing-programme summary; the firm's impact tolerance for onboarding (no more than four hours of new-application processing disruption; no more than two percent of in-flight applications failed for technology reasons over the disruption window).
- **Engagement scope supplied**: institution = credit-institution EU subsidiary; primary regulators = ECB SSM, national competent authority; persona = head of operational resilience and head of ICT risk jointly; source posture = public-plus-firm-policy; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **DORA in scope**: true. **TLPT in scope**: under designation review; the firm is preparing for designation under DORA Article 26 [verify subarticle] and the testing-programme design includes a TLPT-scoping line for the onboarding chain. **AI in scope**: true.
- **Exit plan cross-reference**: exit-plan records on file for the AI vendor and the document-storage vendor; this pack contains an exit-rehearsal scenario for the AI vendor and pulls forward an open finding from the AI-vendor exit plan that prompt-template portability is unproven.

## Output sketch

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

## Why this scenario matters

- **DORA programme alignment is the spine.** The pack is not just a one-off cycle; it sits inside the digital operational resilience testing programme under Article 24 [verify subarticle] and feeds the supervisory submission.
- **AI-specific scenarios are real scenarios.** Vendor model regression and prompt-template portability are not generic vendor outages; they need their own scenario design and they need the model-risk function in the room.
- **Concentration scenarios are part of the testing programme.** The AI vendor and the document-storage vendor sharing an upstream hyperscaler is the kind of single-point-of-failure that surfaces in `concentration-risk-review` and gets tested here.
- **TLPT is its own workstream.** TLPT-scoping requires legal sign-off, supervisory engagement under TIBER-EU methodology, and a different testing posture; the pack records the scoping line but does not collapse TLPT into the operational testing cycle.
- **Substitute-vendor evidence is a precondition for the partial-simulation.** Running a partial-simulation that exercises the substitute AI vendor requires the substitute's own vendor-diligence record and `llm-vendor-evidence-review` record on file. The pack flags these as preconditions, not as in-test work.
- **The AI risk committee is in the read-out path.** AI-specific findings cluster for the AI risk committee; non-AI findings cluster for the operational-resilience committee. Different forums; different decisions.

## Anchors

- DORA, Regulation (EU) 2022/2554, Articles 24-26 [verify subarticle numbering against the official OJ text] — digital operational resilience testing programme; advanced testing including TLPT.
- TIBER-EU framework (ECB) [verify reference and current version] — TLPT methodology.
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02) [verify section] — outsourcing-test posture.
- BCBS Principles for Operational Resilience (March 2021), scenario-testing and ICT principles.
- NIST AI Risk Management Framework 1.0 (NIST AI 100-1, January 2023), Map and Govern functions [verify subsection].

See `references/source-anchors.md` for full citations.
