# Troubleshooting: resilience-testing-pack

Recurring pitfalls. Read before producing the pack and again before sign-off.

## Tolerance vs SLA

### Designing tests against vendor SLAs instead of firm impact tolerance

The vendor's published service-level commitment is what the vendor has agreed to. The firm's impact tolerance is what the important business service must hold within. They usually differ; treating the SLA as the test understates what the firm has to evidence. Calibrate criteria to the IBS map's tolerance lines, not to the contractual commitment.

### Setting tolerance from the architecture diagram

A multi-cloud or active-active diagram is not evidence that failover holds within tolerance. Tolerance is what the test demonstrates; the diagram is the hypothesis under test.

## Scenario set

### Skipping severe-but-plausible scenarios for "low likelihood"

Severe-but-plausible is the supervisory frame, not a probability judgement. Scenarios that have happened in adjacent firms are plausible by definition. A hyperscaler-region failure, an identity-provider outage, a payments-rails disruption, a major fraud-decision vendor outage: each has a public record in adjacent institutions.

### Designing scenarios only against the primary path

The primary path is the easy test. Scenarios should also stress secondary paths, fourth-party dependencies (hyperscaler region, BIN-sponsor processor, KYC vendor, foundation-model upstream), and concentration points surfaced in `concentration-risk-review`.

### Ignoring AI-specific scenarios on an AI-in-scope chain

Vendor model regression, eval drift on the deployed system, vendor model deprecation mid-cycle, prompt-injection on the deployed agent, training-data incident at the vendor: none of these collapse into generic vendor-outage language. The model-risk function belongs in the room when these scenarios run.

## Method mix

### Tabletop everywhere

Tabletop is the cheapest, lowest-fidelity method. A programme that uses tabletop for every scenario has not been tested in supervisory terms. A critical-or-important arrangement that has only ever been tabletop-tested is a finding waiting to be written.

### Full-live everywhere

The opposite failure mode. Full-live exercises that introduce real customer impact are real incidents. They run for a small subset of scenarios, with safety controls, and not annually for every chain.

### Treating data-extraction-rehearsal and shadow-cutover as outside the testing pack

These are test methods. The exit-rehearsal scenarios live in the testing pack; cross-link to the relevant `exit-plan` record.

## Vendor participation

### Excluding vendor participation

A test the vendor declines to join tests the technology, not the partnership. Vendor participation is a real test. Where the vendor declines, that itself is a finding for the diligence cycle.

### Treating vendor account-team observation as participation

Account-team observers are not the vendor's incident-response function. Specify which vendor function is in the test and what they are doing.

## Safety controls

### Running a partial-simulation or live test without exit triggers

A live test that exceeds the customer-impact threshold is a real incident. Exit triggers (customer-impact volume, real incident on an unrelated path, vendor-declared issue, supervisor intervention) are mandatory for partial-simulation and full-live exercises.

### No kill-switch and no rollback

A full-live exercise that cannot be aborted cleanly is reckless. Kill-switch and rollback procedures are preconditions, not nice-to-haves.

### Suppressing customer-comms templates

For any scenario that may surface real customer impact, customer-facing comms templates are pre-positioned, even if the plan is to suppress comms during the test. The exit-condition path needs a comms-ready posture.

## Read-out and findings

### Producing a test design without a read-out template

The committee needs the post-exercise narrative shape on day one of the cycle, not on read-out day. Lock the template at design time; revise after the exercise only if a real finding requires a different shape.

### Treating findings as ad-hoc

Findings flow into the firm's issue-management cycle through `issue-writeup`. A finding without an owner and a clock dies in the post-exercise deck. Each finding gets recorded with owner, due date, verification path, and an issue ID.

### Skipping the lessons-learned capture

Lessons-learned are wider than findings (process improvements, runbook updates, training implications, programme-design adjustments). Filed against the IBS or arrangement, not against the test cycle, so the next cycle benefits.

## Programme alignment

### Producing the pack outside the firm's annual programme

A one-off pack that does not cite where it sits in the firm's annual operational-resilience testing programme is harder to sustain and harder to defend at the supervisor's read-out. Cite the programme; cite the prior cycle; cite the next cycle trigger.

### Forgetting the regulator-observation posture

Some programmes have a regulator-observation expectation (SCI industry-wide test for SCI entities, advanced testing under DORA Article 26 [verify subarticle]). Build it in or call out the absence with the rationale.

### Treating TLPT as part of the operational testing cycle

Threat-led penetration testing carries its own legal-and-supervisory engagement model under TIBER-EU and DORA Article 26 [verify subarticle]. The operational testing pack records the scoping line; TLPT itself runs as a separate workstream.

## Boundary

### Producing the pack as the test

This skill drafts the design and the read-out template. The exercise itself is run by the firm's resilience function with the second-line role limited to challenge and observation as appropriate. A pack that conflates design with execution has overstepped.

### Letting the pack owner sit only in second line

Second line designs and observes; first line runs the exercise. The accountable executive is the BCDR lead or the head of operational resilience for IBS-level packs and the head of TPRM for arrangement-level packs. A pack owned only by second line has the wrong ownership.

## Output discipline

### Citing without sections

Every regulator citation in the pack carries a section reference or a `[verify section]` placeholder. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the pack body.

### Marking unsupported claims silently

Use `[evidence needed]` explicitly. An inferred claim presented as evidenced is the failure mode.

### Closing with too much certainty

The confidence label is `high` only when the source posture, the testing history, and the named-approver review line up. `medium` and `low` are normal for a first cycle; `unknown` is honest where preconditions (substitute-vendor diligence, vendor participation confirmation, legal sign-off for live tests) have not closed.
