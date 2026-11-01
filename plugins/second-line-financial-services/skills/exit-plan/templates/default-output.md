# Exit plan

**Vendor**: [legal entity; brand name if different]
**Service type**: [concise, e.g., core banking SaaS, transfer agent, claims TPA, foundation-model API]
**Arrangement ID**: [stable ID; reused across criticality-assessment, vendor-diligence, contract-gap-review, concentration-risk-review]
**Vendor-diligence record**: [ID; the plan consumes criticality, subcontractors, data_access, residual_risk, exit_plan_status from this record]
**Engagement ID**: [pointer to scope record, or "none — scope not formalised"]
**As of**: [date]
**Review type**: [pre-onboarding | annual-recertification | off-cycle-trigger | post-incident-re-review | concentration-driven-re-review | scope-change-re-review]
**Owner (role)**: [usually IBS owner or head of TPRM]
**Approver (role)**: [per firm policy for this criticality tier]
**Confidence label**: [high | medium | low | unknown]

## Arrangement and criticality

- Business process and important business service supported.
- Customer-impact path; whether the vendor sits on the IBS critical chain.
- Data scope at termination: [NPI | PHI | PCI | books-and-records | model-prompts | model-outputs | training-data | logs-only | metadata-only | none].
- Subcontractors known: [list].
- Criticality tier (consumed from `vendor-diligence`; do not re-set): [not-critical | important | critical | unknown].
- DORA in scope: [true | false].
- AI vendor: [true | false].

## Triggers

Cover vendor-driven, firm-driven, regulator-driven, and market-driven categories. A plan covering only one category is incomplete.

| Category | Trigger | Lead-time assumption | Detection signal |
|---|---|---|---|
| vendor-driven | | | |
| firm-driven | | | |
| regulator-driven | | | |
| market-driven | | | |

## Transition target options

Score each realistic option. A plan with one option only is a single point of failure.

| Option | Candidate (or "unidentified") | Viability | Time-to-transition | Dependencies |
|---|---|---|---|---|
| substitute-vendor | | primary / viable / weak / not-viable | | |
| in-source | | | | |
| hybrid-substitute-and-in-source | | | | |
| retire-service | | | | |
| graceful-degradation | | | | |

- **Selected primary**: [option].
- **Secondary**: [option] — used when the primary is unavailable on the day.

## Time-to-transition versus tolerance

- Impact tolerance for the supported important business service: [from the firm's IBS map; not a vendor commitment].
- Planned time-to-transition under primary target: [duration].
- Planned time-to-transition under secondary target: [duration].
- `time_to_transition_vs_tolerance = [within | near | breach | unknown]`.
- A `breach` is itself a finding. The plan documents the gap; it does not paper over it.

## Data return and destruction

Build for every data category in `data_access`.

- **Extraction format**: [vendor-proprietary or open; specify file format and schema].
- **Schema mapping required**: [yes | no]. Drives migration-engineering effort.
- **Volume estimate**: [order of magnitude].
- **Extraction window**: [realistic time once initiated].
- **Validation against firm-of-record**: [how the firm will reconcile the returned data].
- **Vendor obligations**: [contractual; pointer to `contract-gap-review` for the clause-by-clause read].
- **Firm obligations**: [target provisioning, credentials, cutover, UAT].
- **Destruction-evidence form**: [signed certificate, log evidence, third-party audit; firm retention of the evidence].
- **Post-termination retention**: [lawful retention by the vendor; named carve-outs for regulatory archive, fraud investigation, legal hold].
- **Key rotation and revocation**: [revoke vendor access; rotate shared keys and tokens; decommission tunnels; remove DNS; update DLP rules].

## Knowledge transfer

- **Documentation set**: [runbooks, integration specs, configuration baselines; for AI vendors add prompt templates, model-card extracts, evaluation rationale].
- **Personnel transition**: [named SMEs, knowledge-transfer sessions, reverse-shadowing for in-source paths].
- **Code and artifact escrow**: [source code, build artifacts, container images, model weights, prompt libraries, RAG corpora].

## Contract termination mechanics

Pointer to `contract-gap-review` for the clause-by-clause read. Headline reads here.

- Termination clause reference: [section in executed agreement; governing law].
- Termination-for-convenience: [yes | no].
- Termination-assistance period: [duration; the clause is not the plan].
- Termination fees: [posture].
- Regulator-directed-termination clause: [yes | no | partial]. Absence is a finding for any DORA-in-scope or banking-overlay arrangement.
- In-flight data lock-in: [vendor-proprietary formats, fine-tune artifacts, custodial assets requiring third-party movement, regulator-licensed registrations].

## Customer notice posture

Sector-specific obligations live in the sector overlays.

- Notification required: [yes | no].
- Lead time: [period; cite the regulated clock that drives it].
- Channel: [statement, email, in-app, mailed letter, advance change-in-terms].
- Regulated clock: [Reg DD §1030.5, Reg E §1005.8, NACHA Operating Rules, NAIC policyholder-notice statute, fund prospectus update window, etc. — sector-specific].

## Regulator notice posture

A critical or important function exit usually lands on a supervisory clock. Missing this is itself a finding.

- Notifiable regimes: [DORA Article 28 ICT-third-party register update; bank-regulator material-vendor-change notification; Form ADV brochure update; Form N-CEN service-provider change; NAIC ORSA update; NYDFS event-reporting; sector-specific].
- Windows: [clocks by regime].
- Filings triggered: [list].
- Supervisory engagement posture: [proactive engagement vs paper notice; for critical/important, proactive engagement is the expectation].

## Cyber considerations during transition

Detail in `references/cross-cutting/cyber.md`.

- Secure data extraction (encrypted transit, integrity verification).
- Key rotation, credential rotation, token revocation.
- Access-revocation choreography (vendor staff, vendor systems, vendor APIs).
- Vendor-side destruction certification with retained evidence.
- SEC cyber-disclosure exposure on a forced or contested termination [where firm is a publicly-listed registrant].
- SIEM and DLP rule updates on cutover.

## Privacy considerations during transition

Detail in `references/cross-cutting/privacy.md`.

- GLBA Safeguards data-handling on transition.
- State-privacy-law deletion and return obligations (CCPA / CPRA service-provider deletion).
- HIPAA business-associate transition (where in scope).
- Cross-border data flows during transition.
- Data-subject-rights handling continuity across the cutover.

## Supervisory readiness during transition

A multi-month transition runs alongside live supervisory and audit activity.

- Dual-running controls covering both vendors during cutover.
- Evidence-collection across both vendors, with the seam dated.
- MRA / MRIA exposure tracked.
- Bank Service Company Act §1867(c) examination-access continuity (banking).
- Books-and-records continuity (advisers, BDs, registered funds; Rule 204-2 / Rule 17a-4 / Rule 31a).
- Examination posture pre-briefed for the cutover quarter where one is on the calendar.

## Fourth-party dependencies

Subcontractors of the exiting vendor whose own posture creates a transition bottleneck.

| Fourth party | Dependency type | Transition impact |
|---|---|---|
| | | |

## AI-specific transition considerations

> Populate this section only when `ai_vendor = true`. AI-specific transition engineering does not collapse into generic data-extraction language.

- **Prompt-template portability**: [templates are usually model-specific; whether the firm has tested portability].
- **RAG corpus migration**: [vector spaces are model-specific; expect re-embedding and re-indexing].
- **Fine-tune artifact handling**: [returned, destroyed, or stranded].
- **Model-version pin handling**: [the deployed checkpoint at termination; vendor's final-version export posture; deprecation pressure on the timing].
- **Guardrail and eval porting**: [carrier-side guardrails and eval harnesses need rework on the new model].
- **Agent tool offboarding**: [for agentic vendors, action-authorisation surface and audit-trail sinks revoked and rewired].

## Cost and resourcing estimate

- Cost estimate range: [order-of-magnitude band].
- Cost drivers named: [data migration, dual-running, end-customer notification cycle, internal change management, prompt re-engineering and RAG re-embedding for AI vendors, model-risk re-evaluation for AI vendors].

## Testing plan

A plan never tested has unknown viability. Document the test posture honestly.

- **Cadence**: [tabletop / walkthrough / partial-simulation / full-live; aligned to criticality tier and the firm's policy].
- **Methods planned**: [tabletop, walkthrough, partial-simulation, full-live-exercise, data-extraction-rehearsal, shadow-cutover].
- **Last test date**: [date or "never tested"].
- **Last test outcome**: [pass or pass-with-findings / fail; summarise findings; "never tested" gets surfaced as a reviewer question].
- **Next test due**: [date].
- **resilience-testing-pack record**: [ID where the exit rehearsal sits in the integrated test programme].

## Open dependencies and risks

Items that have to close before the plan is anything more than paper.

- [bulleted; each is specific and verifiable]

## Reviewer questions

Each question names the decision it supports.

- [bulleted]

## Recommended owner actions and decision checkpoints

- **Owner (role)**: [IBS owner or head of TPRM; procurement supports execution but does not own customer-facing impact].
- **Approver (role)**: [per firm policy for this criticality tier].
- **Decision checkpoints this plan must clear**: scope, evidence, authority, impact, decision.
- **Decision forum and attestation block**: [operational-resilience committee | TPRM forum | risk committee | AI risk committee | fund board]; owner and approver named; sign-off conditions written out.
- **Next-review trigger**: [annual cycle date; scope-change trigger; contract-amendment trigger; vendor-incident-driven re-review condition; for AI vendors, model-version-change trigger].
- The plan does not approve transition. The named approver decides.

## Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

Cite `references/source-anchors.md` for canonical citations. Use `[verify section]` if the section reference is unknown; do not invent.

---

*Plan depth scales to criticality tier and DORA-in-scope status.* For an important-tier non-DORA arrangement, several sections may collapse to a paragraph. For a critical or DORA-in-scope arrangement, full depth applies and reviewer questions cluster for the operational-resilience committee, the AI risk committee (AI vendors), or the fund board (registered funds).
