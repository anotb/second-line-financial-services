## Example: annual resilience-testing pack for the card-payment authorisation IBS at a US bank

Public-source-derived. No named bank or vendor. The shape mirrors a mid-tier US bank running its annual operational-resilience testing cycle on the card-payment authorisation important business service.

## Input

- **Subject of test**: card-payment authorisation IBS, end-to-end. The chain spans the card-network connection, the firm's authorisation host, the fraud-decisioning vendor, the customer-account ledger, and the customer-facing channels.
- **Inputs already on file**: the firm's IBS register entry for card-payment authorisation; the criticality-assessment outputs for the card-network connection (critical) and the fraud-decisioning vendor (important); the prior-year test outcomes including the partial-simulation finding that the secondary network path took longer than expected to take traffic; the impact tolerance from the firm's IBS map (no more than thirty minutes of authorisation outage; no more than five percent of authorisations declined for connectivity reasons over the disruption window).
- **Engagement scope supplied**: institution = US national bank, mid-tier; primary regulators = OCC, FRB; persona = head of operational resilience; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking, payments-fintech; cross-cutting overlays = cyber.
- **DORA in scope**: false. **TLPT in scope**: false. **AI in scope**: false (the fraud-decisioning vendor uses ML, but the test cycle does not specifically test the model; that scenario sits in the next cycle).
- **Exit plan cross-reference**: exit-plan record on file for the fraud-decisioning vendor; this pack contains an exit-rehearsal scenario for that arrangement.

## Output sketch

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

## Why this scenario matters

- **Testing against firm impact tolerance, not vendor SLA.** The fraud-decisioning vendor's contractual uptime is the vendor's commitment; the firm's thirty-minute authorisation-outage tolerance is the test. Conflating the two is a recurring failure mode.
- **A mix of methods, not tabletop everywhere.** Tabletop is the cheapest method; a programme that uses tabletop everywhere has not been tested in supervisory terms. This pack mixes full-live, partial-simulation, walkthrough, and tabletop.
- **Vendor participation is the test of the partnership.** The fraud-decisioning vendor's full participation is required; the network partner's participation in the full-live exercise is the test of the operational relationship as much as the failover technology.
- **Safety controls on the live exercise.** A full-live exercise that introduces real customer impact is a real incident. Safety controls (kill-switch, customer-impact-threshold for early termination, pre-positioned customer-comms templates) are not optional.
- **Read-out template locked at design.** The committee's narrative shape is set on day one of the cycle, not invented under time pressure on read-out day.

## Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 6, 2023), ongoing-monitoring section [verify section].
- FFIEC IT Examination Handbook, Business Continuity Management booklet, testing-and-exercise section [verify section].
- FFIEC inter-agency cloud joint statement (Security in a Cloud Computing Environment, April 30, 2020) [verify exact title and date].
- BCBS Principles for Operational Resilience (March 2021), scenario-testing principle.

See `references/source-anchors.md` for full citations.
