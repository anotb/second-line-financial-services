# Concentration risk review

**Assessment ID**: [stable ID]
**Engagement ID**: [pointer to scope record, or "none — scope not formalised"]
**As of**: [date]
**Cycle type**: [annual-portfolio | pre-contract-preliminary-assessment | supervisor-information-request | stress-event-readiness | post-incident-re-review | off-cycle-trigger]
**Owner (role)**: [e.g., head of TPRM, ICT third-party programme lead]
**Approver (role)**: [per firm policy; operational-resilience committee chair, head of TPRM, head of operational resilience, CRO office, or accountable executive in EU pre-contract cycles]
**Confidence label**: [high | medium | low | unknown]

## Scope and source posture

- In-scope legal entities (with LEI where available): [list].
- Consolidation level: [individual | sub-consolidated | consolidated].
- Source register: [TPRM register | DORA register of information | EBA outsourcing register | hybrid] as of [date].
- Criticality cutoff: [critical-only | critical-or-important | important-business-service-supporting | all].
- Arrangements in scope: [count].
- Fourth-party visibility: [full | rank-2-and-deeper | rank-1-only | none].
- Data-quality caveats: [bulleted; missing identifiers, criticality-classification gaps, sub-contractor-chain visibility limits, intra-group flagging, vendor-restructuring records, etc.].

A clean concentration view with no caveats reads as either complete (rare) or unaware (more common).

## Concentration dimensions assessed

For each dimension: dimension, metric (criticality-weighted count, transaction or operational-volume share, function-dependency count, time-to-substitute — not spend), threshold reference (firm policy and the supervisory framing in the named anchors), distribution summary, top concentration nodes (with share and affected functions), severity, substitutability-read pointer, notes.

| Dimension | Metric | Threshold reference | Distribution summary | Top concentration | Severity | Substitutability ptr |
|---|---|---|---|---|---|---|
| Single-vendor | | | | | clear / watch / elevated / breach | |
| Fourth-party | | | | | | |
| Geographic | | | | | | |
| Jurisdictional | | | | | | |
| Hyperscaler | | | | | | |
| Foundation-model | | | | | | |
| Shared-utility | | | | | | |
| Sponsor-bank / BaaS | | | | | | |
| BIN sponsor | | | | | | |
| Payment rails | | | | | | |
| AI provider | | | | | | |
| Function-level | | | | | | |

## Cloud concentration view

- Hyperscaler share across critical-or-important arrangements.
- Region and sub-region distribution within each hyperscaler.
- Shared-control-plane and shared-identity-layer considerations (multi-region is not multi-resilience by default).
- Shared dependencies across nominally distinct vendors that run on the same hyperscaler footprint.

## AI-provider concentration view

> Populate when AI is in scope. Otherwise omit.

- Foundation-model-vendor share across AI use cases.
- Inference-region share.
- Fine-tuning-vendor share for the firm's customised models.
- Use-case spread the concentration covers (decisioning, summarisation, retrieval-augmented generation, agentic workflows, classification).
- Re-test cadence (shorter than the rest of the portfolio).

## Geographic and jurisdictional concentration view

- Country-level data-residency concentration (data at rest and data processing).
- Sub-region concentration within a single country.
- Cross-border data-flow posture.
- Governing-law and dispute-resolution-forum concentration.
- Sanctions-regime exposure.
- Regulator concentration where applicable.

## Single-points-of-failure

Functions where one failure removes the function entirely with no ready substitute. Sourced from the function-level dimension and the cross-dimension read.

| Function | Arrangement IDs | Rationale | Severity |
|---|---|---|---|
| | | | watch / elevated / breach |

## Substitutability read

For each concentration flagged at watch, elevated, or breach: alternative vendors known, time-to-substitute estimate, contractual portability (chain to `contract-gap-review`), operational substitutability, stressed-substitutability (the same test under a wider sector-event scenario where the substitute itself may be in demand).

| Concentration ref | Alternatives known | Time to substitute | Contractual portability | Operational substitutability | Stressed substitutability | Exit plan ID | Contract gap ID |
|---|---|---|---|---|---|---|---|
| | | | strong / partial / weak / absent / unknown | strong / partial / weak / absent / unknown | strong / partial / weak / absent / unknown | | |

A concentration with high apparent substitutability under benign conditions can collapse to zero substitutability under sector stress; the read names the difference.

## Recommended actions

Specific, owner-named, dependency-aware. The skill drafts; the named forum decides.

| Action | Owner role | Rationale | Dependent skill | Due date |
|---|---|---|---|---|
| | | | vendor-diligence / contract-gap-review / exit-plan / resilience-testing-pack / criticality-assessment / dora-register-builder / none | |

## Reviewer questions

Each question names the decision it supports and the forum that decides (operational-resilience committee, TPRM forum, risk committee, board, supervisor dialogue).

- [bulleted].

## Open questions

Items routed to legal, compliance, or supervisor dialogue.

- [bulleted].

## Review gates

- Review gates this artifact must clear: [scope, evidence, authority, impact, decision].
- Next-review trigger: [annual cycle date; pre-contract trigger; supervisor request; stress event; incident-driven re-review condition].
- The artifact does not approve. The named forum decides. In EU pre-contract cycles, the firm's signed preliminary assessment is the legal artifact and requires legal and compliance sign-off before becoming the legal record.

## Source trace

| Claim | Source | Section | Verification | Date | URL or file ref |
|---|---|---|---|---|---|
| | | | verified / verify-pending / inferred | | |

Cite `references/source-anchors.md` for canonical citations. Use `[verify section]` if the section reference is unknown; do not invent.

---

*Review depth scales to cycle type and audience.* Annual portfolio cycle runs broad with all dimensions. Pre-contract preliminary assessment runs narrow against the proposed arrangement and the portfolio it joins; the dimensions the proposed arrangement materially moves are read in depth, the others are summarised. Supervisor-information-request runs to the question. Stress-event readiness leads with single-points-of-failure and the substitutability read under stressed conditions.

*Audience shapes the artifact.* A pack for the operational-resilience committee reads operational. A pack for the CRO office leads with the residual concentration posture and the risk-appetite implications. A pack for board reads as a justification of the firm's own concentration tolerance. A pack supporting a supervisor dialogue reads as a justification of the firm's posture before the supervisor asks.
