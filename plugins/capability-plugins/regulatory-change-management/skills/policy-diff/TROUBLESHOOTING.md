# Troubleshooting: policy-diff

The change log feeds the policy committee, training, control owners, and change management. Defects propagate downstream. This file walks the recurring defects and how to resolve them.

## 1. The diff is anchored against an unidentified base

**Symptom**: Version A carries no version label, no approval date, or no document hash. The artifact reads "current vs proposed" without naming the current.

**Why it happens**: The practitioner pulled the live policy from a system that does not surface version metadata, or the firm's policy lifecycle does not stamp policies with a hash. Or the policy was migrated from an older system and the baseline version was lost.

**Resolution**:
- Version A and version B both carry version label, approval date, and approver role. Document hash where available; system-of-record pointer otherwise.
- Where the base version is genuinely lost (the prior version was not retained through a system migration), the row says so explicitly and the open-question summary picks it up. The lost-baseline situation is itself a finding worth surfacing.
- "vs the previous version" is not a citation. The skill does not silently accept it.

## 2. The materiality call collapses to redline volume

**Symptom**: Rows with extensive rewording carry `materiality: material` and rows with minimal rewording carry `materiality: cosmetic`, regardless of substantive impact.

**Why it happens**: The practitioner equated visual change with material change. A long paragraph rewritten for clarity got tagged material; a single-word operative-verb change got tagged clarifying.

**Resolution**:
- Materiality is the operational lens, not the redline lens. Does the firm do something differently because of this change?
- A reworded paragraph can be cosmetic; a single-word change can be material. "Should" to "must" is one word and material almost always; an entire paragraph rephrased for readability with no operative-verb, threshold, or scope change is cosmetic.
- Where the call is contested, the row carries `materiality: open-question` and routes to the named reviewer. The skill does not pre-empt the call; it surfaces it.

## 3. Downstream-impact rows say "yes" without rationale

**Symptom**: Training, control revision, system change, communication, or attestation columns carry `yes` with no one-sentence rationale.

**Why it happens**: The practitioner ticked the boxes from a generic checklist rather than tying each yes to the specific operational consequence of the change.

**Resolution**:
- Each yes carries a one-sentence rationale naming the specific affected artifact: the named training module, the control IDs, the named system, the audience for the communication, the attestation roster.
- "Yes — training" alone is not an impact. "Yes — refresh the vendor-management onboarding module to cover the new criticality-tier diligence checklist" is.
- Where the impact is genuinely uncertain (e.g., the practitioner does not know whether the firm's training module already covers the change), the row carries `[evidence needed]` rather than a guess.

## 4. Cosmetic and clarifying rows route to the wrong approver

**Symptom**: Cosmetic rewording rows route to the policy committee or the board. The committee reads through pages of typo fixes before reaching the material rows.

**Why it happens**: The practitioner applied a single approver-routing rule across all rows. Or the firm's policy lifecycle does not differentiate routing by materiality.

**Resolution**:
- Cosmetic rows route to the policy owner alone. Routing them to the policy committee is wasted committee time and dilutes the committee's signal on the material rows.
- Material rows route to the named approver the firm's lifecycle requires (committee, board, function head). Incremental rows usually route the same as material; clarifying rows can route to the policy owner with committee notification.
- The approver routing summary clusters material rows for the relevant committee or board paper; cosmetic rows are not in the summary.

## 5. Cross-policy ripple block is empty

**Symptom**: The cross-policy ripple block carries no entries even though the diff renamed a defined term, moved a section number, or deleted a paragraph.

**Why it happens**: The practitioner did not search the firm's policy library for cross-references. Or the firm's policy library is not indexed and the cross-references are not findable without manual inspection.

**Resolution**:
- Defined-term changes almost always ripple. Renamed terms, narrowed scopes, and removed terms each carry consumer policies that need a reciprocal update.
- Section-number changes ripple where other policies cite the moved section. The diff captures the ripple even when the ripple itself is a downstream task.
- Where the firm's policy library is not searchable, the cross-policy ripple block carries an open question routing the search task to the policy librarian or compliance.
- Empty ripple blocks for diffs with substantive changes are usually a defect, not a clean result. Inspect first; declare empty second.

## 6. Defined-term inventory missing

**Symptom**: A defined term changed name or scope between version A and version B but the defined-term inventory block is empty.

**Why it happens**: The practitioner treated the term change as a single row in the change log without aggregating it as an inventory entry. Downstream consumers (training, controls, attestation) do not see the term-level cascade.

**Resolution**:
- Every defined-term change appears in the defined-term inventory block in addition to its row in the change log.
- The inventory block names downstream consumers (other firm policies, controls, training modules) so the cascade is one read away.
- Renamed terms and narrowed-scope terms carry the highest-cascade pressure; added terms ripple into glossaries and onboarding training; removed terms ripple into supersession of older artifacts that still use them.

## 7. Effective date applied uniformly when the policy phases sections in

**Symptom**: All rows carry the policy's overall effective date even though a particular section binds on a different date (e.g., new control standard binds at year-end, training requirement binds 30 days after rollout).

**Why it happens**: The practitioner used the policy's headline effective date as a default. The phased-in language in the body of the policy was not picked up.

**Resolution**:
- `effective_date` on each row defaults to the policy's overall effective date but takes the section-specific date where the policy phases sections in.
- The phase-in field captures the specific binding date and the rationale for the staggered date.
- Phased rows are common in policy diffs that reflect a transition period — vendor-contract refreshes happen at renewal, training applies after rollout, system changes apply after release. The change log captures the cadence so change-management can sequence.

## 8. The diff treats no-change sections as skipped rather than inspected

**Symptom**: The change log only includes rows where something changed. Sections that did not change do not appear at all.

**Why it happens**: The practitioner reasoned that no-change rows are noise. But the reader cannot tell whether a section was inspected and unchanged or simply missed.

**Resolution**:
- Sections that did not change get a single row with `diff_type: no-change` so the reader can see they were inspected.
- The no-change row carries no downstream impact and routes to no approver beyond the policy owner.
- For long policies with many no-change sections, an aggregate "sections X through Y unchanged" row is acceptable; the goal is reader assurance, not row volume.

## 9. The diff is run without the trigger documented

**Symptom**: The trigger field carries a generic value ("annual review") even though the new version was driven by a specific MRA, regulatory amendment, or internal incident.

**Why it happens**: The practitioner skipped the trigger detail because the annual-review label felt sufficient. The diff loses traceability for examiner and audit purposes.

**Resolution**:
- Trigger is one of `annual-review`, `scheduled-review`, `mra-remediation`, `mria-remediation`, `consent-order`, `regulatory-amendment`, `internal-incident`, `control-failure`, `board-direction`, `system-migration`, `scope-expansion`, `other`.
- The trigger detail field carries the specific reference: SR letter number, MRA reference, board minute date, incident ID, regulatory amendment cite.
- Material rows that close a specific MRA finding cross-reference the MRA finding ID in their open-question or rationale field. The MRA-response file consumes this cross-reference directly.

## 10. Confidence label as a single overall value

**Symptom**: The artifact carries one confidence label without per-row or per-section detail. Downstream review cannot tell which rows are pressure-test ready and which are interpretive.

**Why it happens**: The practitioner treated confidence as a summary judgment rather than a per-row discipline.

**Resolution**:
- Confidence tracks per row. High where the diff is mechanical and the substantive delta is unambiguous; medium where interpretation is involved; low where the diff itself surfaces ambiguity (a paragraph deleted with no explanation in the change-control record).
- The overall confidence label on the diff is allowed to be `mixed` and usually is.
- The source-trace block records confidence by section and explains the rationale (unambiguous redline, interpretation involved, change-control record incomplete).
