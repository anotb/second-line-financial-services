# Exam brief — output template

Engagement-side scaffolding for a live regulator engagement. Roles only, never named individuals. The brief is a draft until the named lead attests.

## Cover

| Field | Value |
|---|---|
| Regulator | |
| Regulator office or division | |
| Engagement type | full-scope / targeted / limited-scope / horizontal / for-cause / follow-up / supervisory-letter response / consent-order response / mock / self-assessment |
| Trigger | routine cycle / risk-based selection / supervisory-letter follow-up / consent-order monitoring / complaint-driven for-cause / horizontal / M&A-driven |
| Fieldwork window | start — end |
| Review-period | start — end |
| Lead examiner role | (do not name) |
| Firm single point of contact role | (do not name) |
| Source posture | public-only / public-plus-firm-policy / public-plus-firm-policy-plus-evidence / connector-aware |
| Brief lead role | |
| Date drafted | |

## Scope confirmation

Pointer to first-day letter or scope memorandum (regulator-issued). If scope was confirmed verbally only, that is itself a brief entry; ask for written confirmation.

| Field | Value |
|---|---|
| In-scope products | |
| In-scope business units | |
| In-scope legal entities | |
| Geographies | |
| Out-of-scope (regulator-confirmed in writing) | |
| Confirmation document pointer | |

## Named points of contact (single-point-of-contact map by topic)

Roles only. Examination correspondence has a primary; each substantive topic in scope has a primary and a backup; outside-counsel engagement is flagged per topic.

| Topic | Primary role | Backup role | Outside counsel engaged | Notes |
|---|---|---|---|---|
| Examination correspondence | | | | single point of contact |
| | | | | |

## Document-handling and privilege posture

| Field | Value |
|---|---|
| Production channel | regulator portal / secure file transfer / on-site reading-room / examiner laptop / paper |
| Privilege-review lead role | typically inside counsel; outside counsel for higher-stakes / internal-investigation work product |
| Privilege-log requirement | yes (regulator indicated) / yes (firm policy) / no |
| Redaction workflow | counsel-supervised, burned-in only, metadata stripped, reviewer named per document |
| Deduplication method | hash-based at production-package level (convention) |
| Production-log location | |
| CSI-handled flag | true / false (true when regulator's prior supervisory letters, MRAs, or examination reports are referenced; CSI cannot leave the firm without written authorisation under the regulator-specific CSI regime — 12 CFR Part 4 Subpart C OCC; Part 261 FRB; Part 309 FDIC; Part 1070 Subpart D CFPB) |
| CSI access-population | role list with access |
| Source-anchor pointer | |

## Request-list mapping

The first-day-letter or follow-up request items, each mapped. The mapping is the operative production tracker; the engagement lead runs the daily standup against it.

| Item ID | Verbatim or paraphrased text | Owner role | Status | Due date | Produced date | Artifact pointer (system-of-record path) | Privilege posture | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|
| | | | ready / partial / not-started / escalated / produced / withdrawn | | | | producible / redacted-and-producible / privileged-withhold / csi-held-by-regulator / under-review | high / medium / low / unknown | |

## Interview-prep posture

Roles only. Off-limits topics are the privileged territory or out-of-scope material the interviewee redirects to counsel if raised; naming them avoids the in-meeting failure mode of an interviewee waiving privilege under pressure.

| Interviewee role | Topic | Prep-session date | Counsel attending | Key documents to re-read | Anticipated topics | Off-limits topics |
|---|---|---|---|---|---|---|
| | | | yes / no | | | |

## Supervisory history (engagement inherits)

Open MRAs, MRIAs, consent-order milestones, in-flight supervisory-letter responses, and self-identified issues the firm intends to surface proactively. Roles only.

| Item ID | Type | Source | Topic | Owner role | Due date | Status | Surface proactively |
|---|---|---|---|---|---|---|---|
| | MRA / MRIA / consent-order milestone / supervisory-letter open response / self-id | | | | | open / in-progress / closed-pending-validation | yes / no |

## Anticipated reviewer questions

Each question ties to a current supervisory priority or a public enforcement theme. The talking-point field carries the firm-side response posture, brief, not a script.

| Question | Source pattern | Talking point | Owner role |
|---|---|---|---|
| | SEC Division of Examinations annual priorities / FINRA Annual Regulatory Oversight Report / CFPB Supervisory Highlights / OCC semiannual operating plan / FFIEC interagency communication / NYDFS Industry Letter / NAIC focus areas / public consent order | | |

## Strategy posture

Where the firm intends to push back, on what basis, via what channel. Pre-positions the disagreement posture so counsel is not surprised in the room. Roles only.

| Topic | Firm posture | Basis | Channel | Notes |
|---|---|---|---|---|
| | accept / push back with rebuttal / push back with escalation / regulator engagement at office-director level / written response only | | verbal at exit / written response / escalation to office director or supervisory committee | |

## Exit-meeting prep

| Field | Value |
|---|---|
| Scheduled date | |
| Firm attendees by role | (no names) |
| Anticipated findings | drawn from in-flight examiner signals |
| Disagreement posture | (cross-reference to Strategy posture rows) |
| Expected response window | days |

## Response posture

| Field | Value |
|---|---|
| Response owner role | typically head of compliance or chief compliance officer |
| Topic-primary roles | |
| Response-due basis | receipt of supervisory letter / exit memo / final examination report (federal banking convention generally 30 days from receipt of supervisory letter; CFPB and SEC vary) |
| Remediation-plan template | pointer to `implementation-plan` for milestone build-out |
| Board or committee reporting required | yes (almost always for MRIAs and consent orders; often for material MRAs) / no |
| External-counsel-for-response flag | yes / no |

## Post-exam follow-up

| Field | Value |
|---|---|
| Lessons-learned session date | |
| After-action record pointer | |
| Next-cycle preparation owner role | |
| Follow-up commitments (carry into next cycle) | |

## Open issues and evidence-needed

| Item | Owner role | Needed-by date | Blocks |
|---|---|---|---|
| `[evidence needed]` items from request-list mapping | | | |
| `[verify section]` items from source-anchors | | | |

## Source trace and confidence

| Claim | Source | Date as-of | Confidence |
|---|---|---|---|
| | source-anchors.md / sector-overlay path / firm-overlay (when present) | | high / medium / low / unknown |

Brief-level confidence label: medium is the honest read while request-list items are partial or escalated, regardless of how clean the rest of the brief looks.

## Sign-off

| Role | Sign-off | Date |
|---|---|---|
| Drafter (regulatory affairs / compliance) | | |
| Reviewer (compliance / legal) | | |
| Lead (head of regulatory affairs / general counsel / CRO chief of staff) | | |
