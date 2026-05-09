# Resilience-testing pack

**Subject of test**: [IBS name | arrangement (vendor + service) | portfolio cut]
**Subject type**: [ibs | arrangement | portfolio]
**Subject ID**: [stable ID; reused across IBS map, vendor-diligence, exit-plan, dora register]
**Pack ID**: [stable ID]
**Engagement ID**: [pointer to engagement-scope record, or "none — scope not formalised"]
**As of**: [date]
**Review type**: [annual-programme-cycle | quarterly-cycle | off-cycle-trigger | post-incident-rehearsal | post-onboarding-validation | regulator-driven | exit-rehearsal]
**DORA in scope**: [true | false]
**TLPT in scope**: [true | false | under-designation-review]
**AI in scope**: [true | false]
**Owner (role)**: [BCDR lead | head of operational resilience | head of TPRM]
**Approver (role)**: [per firm policy for tests of this scope and method]
**Confidence label**: [high | medium | low | unknown]

## Mapping summary

The pack consumes mapping; it does not redo it. Pull from the firm's IBS map and the linked vendor-diligence records.

- **IBS name** (where subject_type = ibs): [name].
- **Process chain**: [end-to-end description].
- **Third parties on the chain**: [list].
- **Fourth parties (material)**: [hyperscaler regions, BIN-sponsor processors, KYC vendors, fund-accountant subcontractors, foundation-model upstreams].
- **Internal dependencies**: [systems, data stores, control points].

## Impact tolerance

The firm's tolerance is the test. Sourced from the firm's IBS map; the vendor's SLA is not the test.

| Field | Value | Source |
|---|---|---|
| RTO | | firm IBS map |
| RPO | | firm IBS map |
| Customer-impact threshold | | firm IBS map |
| Regulatory-impact threshold | | firm policy |
| Financial-impact threshold | | risk-appetite statement |

## Severe-but-plausible scenarios

Each scenario is grounded in a public-source plausibility anchor (a prior real event of the same shape, a regulator-cited scenario, an industry tabletop pack). "Low likelihood" is not a basis for exclusion.

| ID | Name | Description | Rationale | Plausibility anchor | Expected stress | Severity | AI-specific |
|---|---|---|---|---|---|---|---|
| | | | | | | near-tolerance / tolerance-breach / catastrophic | true / false |

## Test design

Per scenario: method, cadence, preconditions, safety controls, exit triggers, participants, vendor participation. Mix the methods across the programme.

| Scenario ID | Method | Cadence | Preconditions | Safety controls | Exit triggers | Participants | Vendor participation |
|---|---|---|---|---|---|---|---|
| | tabletop / walkthrough / partial-simulation / full-live-exercise / data-extraction-rehearsal / shadow-cutover / tlpt | | | | | | full / partial / observer-only / none |

Notes on method choice:

- **Tabletop**: low fidelity, low operational risk; first cycle on a new scenario; cyber tabletop and disclosure-committee rehearsal.
- **Walkthrough**: incident-response plan or runbook walkthrough step-by-step.
- **Partial-simulation**: tested-failover for one path or one component; safety controls required.
- **Full-live-exercise**: real failover under controlled conditions; safety controls and exit triggers mandatory.
- **Data-extraction-rehearsal**: actual data extraction tested against substitute target; exit-rehearsal scenario.
- **Shadow-cutover**: substitute provisioned in parallel; exit-rehearsal scenario at higher fidelity.
- **TLPT**: separate workstream; legal-and-supervisory engagement preconditions.

## Success criteria

Per scenario, criteria tied to the impact tolerance. Each criterion is measurable.

| Scenario ID | Criterion | Metric | Threshold | Tolerance link |
|---|---|---|---|---|
| | | | | RTO / RPO / customer-impact / regulatory-impact / financial-impact |

## Evidence-collection plan

What is captured during the exercise, by whom, in what form, and how it is preserved.

| Scenario ID | Evidence item | Captured by | Form | Retention |
|---|---|---|---|---|
| | | | logs / screenshots / recorded comms / vendor ticket exports / system traces / observer notes | |

## Observation method

[In-room observers per workstream | recorded video | command-and-control bridge transcript | after-action interviews]. Independent observation is the second-line role; first-line runs the exercise.

## Communication plan

| Audience | Pre-test | In-test | Post-test |
|---|---|---|---|
| Internal leadership | | | |
| On-call response | | | |
| Customer | suppressed / pre-positioned / in-test | suppressed / templated / live | post-test as needed |
| Regulator | pre-notification / observation invitation / none | live status / suppressed | read-out / submission |
| Vendor | | | |

## Read-out template (locked at design time)

Sections the operational-resilience committee receives:

1. Exercise summary
2. Scenarios run and method per scenario
3. Results against impact tolerance
4. Findings
5. Root cause
6. Remediation owners and clocks
7. Programme-cycle implications
8. [DORA-programme-cycle implications, where DORA in scope]
9. [Reg SCI submission implications, where SCI entity]
10. [AI risk committee escalation, where AI in scope and findings warrant]

## Findings-and-actions framework

Findings flow into the firm's issue-management cycle through `risk-compliance-core/issue-writeup`. Each finding gets an owner, a due date, a verification path, and an issue ID. A finding without an owner and a clock dies in the post-exercise deck.

| Finding | Severity | Owner | Due | Verification | Issue ID |
|---|---|---|---|---|---|
| | | | | | |

## Lessons-learned capture

Wider than findings: process improvements, runbook updates, training implications, programme-design adjustments. Filed against the IBS or arrangement, not against the test cycle, so the next cycle benefits.

- [bulleted]

## Post-test remediation

Remediation actions arising from the exercise. A pack that does not produce remediation has not tested anything that mattered.

| Action | Owner | Due | Verification | Issue ID |
|---|---|---|---|---|
| | | | | |

## Programme alignment

- **Firm programme link**: [where this pack sits in the firm's annual operational-resilience testing programme].
- **DORA programme link**: [where this pack sits in the digital operational resilience testing programme under DORA Article 24, where applicable].
- **Reg SCI programme link**: [for SCI entities, the BCDR-test or industry-wide-test cycle this pack feeds].
- **TLPT programme link**: [cross-reference to the TLPT exercise where the firm is in scope].

## Cross-references

- **Exit-plan record(s)**: [IDs for exit-rehearsal scenarios in this pack].
- **Vendor-diligence record(s)**: [IDs for the third parties in scope].
- **Concentration-risk-review record**: [ID where a portfolio scenario tests a flagged concentration].

## Reviewer questions

Each question names the decision it supports.

- [bulleted]

## Recommended owner actions and decision checkpoints

- **Owner (role)**: [BCDR lead or head of operational resilience for IBS-level packs; head of TPRM for arrangement-level packs].
- **Approver (role)**: [per firm policy for tests of this scope and method].
- **Decision checkpoints this pack must clear**: scope, evidence, authority, impact, decision.
- **Decision forum and attestation block**: [operational-resilience committee | TPRM forum | risk committee | AI risk committee | audit committee | supervisor]; owner and approver named; sign-off conditions written out.
- **Next-cycle trigger**: [annual cycle date; scenario-specific cadence; supervisory-driven trigger].
- The pack does not approve test execution. The named approver decides; the resilience function runs the exercise.

## Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

Cite `references/source-anchors.md` for canonical citations. Use `[verify section]` if the section reference is unknown; do not invent.

---

*Pack depth scales to subject criticality, DORA-in-scope status, AI-in-scope status, and the firm's testing programme maturity.* For a non-DORA arrangement-level pack, several sections collapse to a paragraph. For a DORA-in-scope IBS-level pack with TLPT scoping, full depth applies and reviewer questions cluster for the operational-resilience committee, the AI risk committee (where AI in scope), the audit committee, and the supervisor.
