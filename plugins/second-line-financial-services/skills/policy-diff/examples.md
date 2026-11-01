# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## cybersecurity-policy-mra-amendment

### Example: Cybersecurity policy MRA-driven amendment

#### Input

A NYDFS-covered insurance company received a Matter Requiring Attention from its New York State Department of Financial Services examination naming three weaknesses in its cybersecurity policy: the policy lacked an explicit data-classification scheme tied to the firm's risk assessment, lacked an explicit asset-inventory provision, and did not name the customer-data retention period. Version A is the cybersecurity policy approved March 2025 and last reviewed annually under §500.3. Version B is the proposed amendment, drafted by the CISO's office in coordination with privacy and records management. Trigger is `mra-remediation`. Named approver is the senior officer designated under §500.3 (the CISO with audit committee notification). Source posture is public-plus-firm-policy.

#### Output sketch

The change log surfaces twelve rows. Highlights:

- CHG-001, §3.2 Data classification, `added`. Version A had no data-classification provision. Version B adds a four-tier classification (public, internal, confidential, regulated-customer) tied to handling, storage, and transmission requirements. Substantive delta: new policy provision establishing classification and binding handling requirements; closes MRA finding 1. Materiality material. Downstream: new training module for all-staff (delivery within 60 days of effective date); control revision against the firm's data-handling control set (control IDs CTRL-CYB-007 through CTRL-CYB-011 update; new CTRL-CYB-024 added for regulated-customer-tier handling); system change in the data loss prevention configuration to enforce tier-based rules; communication to all-staff with targeted line-manager pack; fresh attestation for staff with access to confidential and regulated-customer data. Open question: whether existing data without classification metadata gets a default tier or requires a one-time classification sweep — flagged for the working group with the records-management lead.

- CHG-004, §4.1 Asset inventory, `added`. Version A had no explicit asset-inventory provision. Version B requires a maintained asset inventory covering information systems, applications, and data assets, refreshed quarterly with annual sign-off by IT operations and CISO. Substantive delta: closes MRA finding 2. Materiality material. Downstream: control revision (new CTRL-CYB-025 asset inventory completeness test, new CTRL-CYB-026 quarterly refresh evidence); system change (asset-management tool configuration and report); communication to IT operations leadership; attestation re-up annually. Approver routing: CISO with audit committee notification.

- CHG-006, §5.3 Customer-data retention, `reworded-substantive`. Version A required "appropriate retention"; version B names the retention periods by data category, aligns to GLBA Safeguards Rule and state privacy law where applicable, and binds destruction at retention-period expiry. Substantive delta: closes MRA finding 3 and aligns to the firm's privacy policy retention schedule. Materiality material. Downstream: control revision (CTRL-CYB-018 retention-policy compliance test refreshed; CTRL-CYB-019 destruction evidence test refreshed); system change (records-management system retention-rule configuration); communication to records management and privacy office; attestation re-up at the records-retention-officer level.

- CHG-009, §7.2 Third-party security, `reworded-substantive`. Version A pointed to the third-party risk policy without naming the §500.11 expectations directly. Version B carries the §500.11 elements explicitly: risk-based diligence, contractual security commitments, periodic assessment. Substantive delta: incremental tightening; the third-party policy already covered these elements but the cybersecurity policy now also names them, closing the cross-policy ambiguity. Materiality incremental. Downstream: cross-policy ripple flag — the third-party risk policy needs a reciprocal cross-reference; no new training; no new controls; communication to vendor-facing security staff for awareness.

- Three `reworded-substantive` rows tighten incident-notification language to the §500.17 72-hour clock. Materiality material.

- Four `reworded-cosmetic` rows. Materiality cosmetic. No downstream impact.

Approver routing summary clusters the seven material rows for CISO approval with audit committee notification. Communication plan summary sequences delivery: data-classification training as the lead artifact, asset-inventory rollout in parallel with the IT-operations leadership, retention-period changes communicated with the privacy office, third-party-security awareness as a vendor-facing comms item.

Cross-policy ripple flags three: the third-party risk policy needs a reciprocal cross-reference; the records-retention policy already carries the retention periods and needs a reconciliation note; the data-handling procedure (subordinate to the policy) needs the four-tier classification cascaded. Defined-term inventory carries "regulated-customer data" as `added` — downstream consumers include the privacy notice, the records-retention policy, and the marketing-data-use procedure.

The change log is a draft until the policy owner (CISO) and the named approver (the CISO with audit committee notification under §500.3) attest. The MRA response file consumes this diff directly and references each material change ID against the MRA finding it closes.

#### Why this scenario matters

It tests the MRA-remediation trigger end to end: the materiality lens is set by the supervisory finding, the approver routing is set by §500.3, and the downstream-impact scope is wider than an annual-review diff because the additions are first-time provisions rather than refinements. It also tests the cross-policy ripple where the cybersecurity policy and the third-party risk policy both touch §500.11 expectations, and the defined-term cascade where a new term enters a policy that other firm artifacts will need to consume. The example is public-source-derived: NYDFS Part 500 is public; the §500.3 annual-approval and §500.11 third-party-policy expectations are public; the firm sector and product are described in posture only with no named institution.

## tprm-annual-review-subcontractor-notification

### Example: TPRM policy annual review with subcontractor-notification rewording

#### Input

Annual review cycle for a national bank's third-party risk management policy. Version A is the policy approved June 2023, drafted before the OCC/FRB/FDIC issued the June 2023 Interagency Guidance on Third-Party Relationships. Version B is the proposed June 2026 refresh, drafted after the policy committee absorbed two years of the new guidance plus an internal incident where a critical fourth-party outage was not surfaced until a customer complaint reached the board. Trigger is annual review with internal-incident overlay. Named approver is the board's risk committee. Source posture is public-plus-firm-policy because the diff cites the firm's vendor-tier definitions.

#### Output sketch

The change log surfaces nineteen rows. Highlights:

- CHG-003, §4.2(c) Pre-contract due diligence, `reworded-substantive`. Version A required "reasonable diligence on the third party"; version B requires "diligence proportionate to the third party's criticality tier, including the third party's own diligence on its material subcontractors." Substantive delta: scope expanded from third party to fourth party for critical-tier vendors. Materiality material. Downstream: training refresh for vendor management and procurement (refresh-existing-module); control revision against CTRL-VEN-014 (criticality-tier diligence checklist) and new CTRL-VEN-027 (fourth-party diligence evidence test); communication to vendor-facing staff and to in-flight onboarding workstreams; contract-template revision tracked as a follow-on planned amendment to the master vendor contract template.

- CHG-007, §6.1 Subcontractor notification, `added`. Version A was silent on the firm's right to notification of material subcontractor changes. Version B requires contractually that critical-tier vendors notify the firm within 30 days of any material change to a named-subcontractor relationship that supports the firm's services. Substantive delta: new contractual obligation introduced as policy. Materiality material. Downstream: control revision (new CTRL-VEN-031 monitoring of subcontractor-change notifications); system change (vendor-management system needs a new field and workflow); communication to vendor-facing staff; attestation re-up at the next annual vendor recertification cycle for critical vendors only. Open question: whether existing critical-tier contracts already in force require an amendment to bring them into compliance, or whether the policy applies only to renewals — flagged for legal review.

- CHG-011, §7.4 Termination and exit testing, `reworded-substantive`. Version A required "an exit plan for critical vendors"; version B requires "a tested exit plan for critical vendors, with the test cadence specified by tier and refreshed at least every 24 months." Substantive delta: untested exit plans no longer satisfy the policy; cadence introduced. Materiality material. Downstream: training refresh for business owners of critical vendors; control revision against CTRL-VEN-019 (exit-plan documentation) and new CTRL-VEN-032 (exit-plan testing evidence); system change (vendor-management system needs an exit-plan-test-due field); communication to all vendor-relationship-managers; attestation re-attestation at the policy effective date.

- CHG-016, §3.1 Defined term "critical activity", `defined-term-changed`. Version A used "critical activity" without anchor; version B aligns to the 2023 interagency guidance's risk-based language and explicitly names the criticality-tier criteria. Defined-term inventory carries this term as `scope-narrowed` because the new definition requires named criteria rather than judgment-only categorisation. Downstream consumers: TPRM operating procedure, vendor-onboarding training, vendor questionnaire, internal audit's TPRM testing program — all need to pick up the new definition.

- Eleven `reworded-cosmetic` rows (typography, capitalisation of "Third Party", paragraph-break adjustments). Each carries `materiality: cosmetic`; each carries no downstream impact; each routes to the policy owner alone for sign-off.

Approver routing summary clusters the four material rows for the risk committee. Communication plan summary clusters the rollout: vendor-facing staff get a 30-day window before policy effective date; line-managers get an all-staff-comms-plus-targeted-pack 14 days before. Cross-policy ripple flags two: the firm's BCM policy points to §7.4's exit-plan language and needs a reference refresh, and the firm's information-security policy carries a parallel third-party-security clause that should be reconciled with the new criticality-tier criteria.

Confidence is mostly high for the rewording rows where the change-control record carries policy-committee minutes; medium on CHG-007 because the subcontractor-notification provision was drafted by legal and the practitioner is taking the operational-impact assessment from the working-group narrative rather than the rule's own text.

The change log is a draft until the policy owner (Head of Vendor Management) and the named approver (Board Risk Committee chair) attest.

#### Why this scenario matters

It tests four things at once: the materiality call when the policy committee has narrative rationale that the diff is "alignment to current guidance" but the operational-impact assessment is doing the real work; the downstream-impact propagation when one row touches training, controls, systems, communication, and attestation; the cross-policy ripple where the firm's BCM and information-security policies need reference reconciliation; and the defined-term inventory where a redefined term changes the criticality classification across the vendor inventory. The example is public-source-derived: the OCC/FRB/FDIC June 2023 interagency guidance is public, and the named-subcontractor-notification pattern is in the published guidance text. No firm or vendor is named; the bank is described by sector posture only.

## troubleshooting

### Troubleshooting: policy-diff

The change log feeds the policy committee, training, control owners, and change management. Defects propagate downstream. This file walks the recurring defects and how to resolve them.

#### 1. The diff is anchored against an unidentified base

**Symptom**: Version A carries no version label, no approval date, or no document hash. The artifact reads "current vs proposed" without naming the current.

**Why it happens**: The practitioner pulled the live policy from a system that does not surface version metadata, or the firm's policy lifecycle does not stamp policies with a hash. Or the policy was migrated from an older system and the baseline version was lost.

**Resolution**:
- Version A and version B both carry version label, approval date, and approver role. Document hash where available; system-of-record pointer otherwise.
- Where the base version is genuinely lost (the prior version was not retained through a system migration), the row says so explicitly and the open-question summary picks it up. The lost-baseline situation is itself a finding worth surfacing.
- "vs the previous version" is not a citation. The skill does not silently accept it.

#### 2. The materiality call collapses to redline volume

**Symptom**: Rows with extensive rewording carry `materiality: material` and rows with minimal rewording carry `materiality: cosmetic`, regardless of substantive impact.

**Why it happens**: The practitioner equated visual change with material change. A long paragraph rewritten for clarity got tagged material; a single-word operative-verb change got tagged clarifying.

**Resolution**:
- Materiality is the operational lens, not the redline lens. Does the firm do something differently because of this change?
- A reworded paragraph can be cosmetic; a single-word change can be material. "Should" to "must" is one word and material almost always; an entire paragraph rephrased for readability with no operative-verb, threshold, or scope change is cosmetic.
- Where the call is contested, the row carries `materiality: open-question` and routes to the named reviewer. The skill does not pre-empt the call; it surfaces it.

#### 3. Downstream-impact rows say "yes" without rationale

**Symptom**: Training, control revision, system change, communication, or attestation columns carry `yes` with no one-sentence rationale.

**Why it happens**: The practitioner ticked the boxes from a generic checklist rather than tying each yes to the specific operational consequence of the change.

**Resolution**:
- Each yes carries a one-sentence rationale naming the specific affected artifact: the named training module, the control IDs, the named system, the audience for the communication, the attestation roster.
- "Yes — training" alone is not an impact. "Yes — refresh the vendor-management onboarding module to cover the new criticality-tier diligence checklist" is.
- Where the impact is genuinely uncertain (e.g., the practitioner does not know whether the firm's training module already covers the change), the row carries `[evidence needed]` rather than a guess.

#### 4. Cosmetic and clarifying rows route to the wrong approver

**Symptom**: Cosmetic rewording rows route to the policy committee or the board. The committee reads through pages of typo fixes before reaching the material rows.

**Why it happens**: The practitioner applied a single approver-routing rule across all rows. Or the firm's policy lifecycle does not differentiate routing by materiality.

**Resolution**:
- Cosmetic rows route to the policy owner alone. Routing them to the policy committee is wasted committee time and dilutes the committee's signal on the material rows.
- Material rows route to the named approver the firm's lifecycle requires (committee, board, function head). Incremental rows usually route the same as material; clarifying rows can route to the policy owner with committee notification.
- The approver routing summary clusters material rows for the relevant committee or board paper; cosmetic rows are not in the summary.

#### 5. Cross-policy ripple block is empty

**Symptom**: The cross-policy ripple block carries no entries even though the diff renamed a defined term, moved a section number, or deleted a paragraph.

**Why it happens**: The practitioner did not search the firm's policy library for cross-references. Or the firm's policy library is not indexed and the cross-references are not findable without manual inspection.

**Resolution**:
- Defined-term changes almost always ripple. Renamed terms, narrowed scopes, and removed terms each carry consumer policies that need a reciprocal update.
- Section-number changes ripple where other policies cite the moved section. The diff captures the ripple even when the ripple itself is a downstream task.
- Where the firm's policy library is not searchable, the cross-policy ripple block carries an open question routing the search task to the policy librarian or compliance.
- Empty ripple blocks for diffs with substantive changes are usually a defect, not a clean result. Inspect first; declare empty second.

#### 6. Defined-term inventory missing

**Symptom**: A defined term changed name or scope between version A and version B but the defined-term inventory block is empty.

**Why it happens**: The practitioner treated the term change as a single row in the change log without aggregating it as an inventory entry. Downstream consumers (training, controls, attestation) do not see the term-level cascade.

**Resolution**:
- Every defined-term change appears in the defined-term inventory block in addition to its row in the change log.
- The inventory block names downstream consumers (other firm policies, controls, training modules) so the cascade is one read away.
- Renamed terms and narrowed-scope terms carry the highest-cascade pressure; added terms ripple into glossaries and onboarding training; removed terms ripple into supersession of older artifacts that still use them.

#### 7. Effective date applied uniformly when the policy phases sections in

**Symptom**: All rows carry the policy's overall effective date even though a particular section binds on a different date (e.g., new control standard binds at year-end, training requirement binds 30 days after rollout).

**Why it happens**: The practitioner used the policy's headline effective date as a default. The phased-in language in the body of the policy was not picked up.

**Resolution**:
- `effective_date` on each row defaults to the policy's overall effective date but takes the section-specific date where the policy phases sections in.
- The phase-in field captures the specific binding date and the rationale for the staggered date.
- Phased rows are common in policy diffs that reflect a transition period: vendor-contract refreshes happen at renewal, training applies after rollout, system changes apply after release. The change log captures the cadence so change-management can sequence.

#### 8. The diff treats no-change sections as skipped rather than inspected

**Symptom**: The change log only includes rows where something changed. Sections that did not change do not appear at all.

**Why it happens**: The practitioner reasoned that no-change rows are noise. But the reader cannot tell whether a section was inspected and unchanged or simply missed.

**Resolution**:
- Sections that did not change get a single row with `diff_type: no-change` so the reader can see they were inspected.
- The no-change row carries no downstream impact and routes to no approver beyond the policy owner.
- For long policies with many no-change sections, an aggregate "sections X through Y unchanged" row is acceptable; the goal is reader assurance, not row volume.

#### 9. The diff is run without the trigger documented

**Symptom**: The trigger field carries a generic value ("annual review") even though the new version was driven by a specific MRA, regulatory amendment, or internal incident.

**Why it happens**: The practitioner skipped the trigger detail because the annual-review label felt sufficient. The diff loses traceability for examiner and audit purposes.

**Resolution**:
- Trigger is one of `annual-review`, `scheduled-review`, `mra-remediation`, `mria-remediation`, `consent-order`, `regulatory-amendment`, `internal-incident`, `control-failure`, `board-direction`, `system-migration`, `scope-expansion`, `other`.
- The trigger detail field carries the specific reference: SR letter number, MRA reference, board minute date, incident ID, regulatory amendment cite.
- Material rows that close a specific MRA finding cross-reference the MRA finding ID in their open-question or rationale field. The MRA-response file consumes this cross-reference directly.

#### 10. Confidence label as a single overall value

**Symptom**: The artifact carries one confidence label without per-row or per-section detail. Downstream review cannot tell which rows are pressure-test ready and which are interpretive.

**Why it happens**: The practitioner treated confidence as a summary judgment rather than a per-row discipline.

**Resolution**:
- Confidence tracks per row. High where the diff is mechanical and the substantive delta is unambiguous; medium where interpretation is involved; low where the diff itself surfaces ambiguity (a paragraph deleted with no explanation in the change-control record).
- The overall confidence label on the diff is allowed to be `mixed` and usually is.
- The source-trace block records confidence by section and explains the rationale (unambiguous redline, interpretation involved, change-control record incomplete).
