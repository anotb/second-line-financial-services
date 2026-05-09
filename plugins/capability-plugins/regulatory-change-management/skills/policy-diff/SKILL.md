---
name: policy-diff
description: |
  Compares two versions of a firm policy (or a proposed policy edit against the current approved version) and produces a section-by-section change log with materiality flags, downstream impact, approver routing, and effective date. One row per change. Each row carries the diff (added, removed, reworded, restructured), the section path, the substantive delta, the materiality call, and the downstream consequences (training refresh, control revision, system change, communication, attestation re-up). Used by policy owners during the annual review cycle, by compliance running a redline against an MRA-driven amendment, and by change-management standing up the rollout package after the policy committee approves.

  Best for:
  - Annual or scheduled policy review where the second line needs the version-over-version delta before recertification.
  - Proposed policy amendment where compliance, legal, or the policy owner needs the change log and downstream impacts before the policy committee meets.
  - Post-MRA or post-issue policy revision where the firm needs to show the regulator exactly what moved between the prior approved version and the remediated version.
  - Pre-approval review of a draft policy against the live approved version where the question is what changed, what it touches, and who needs to know.

  Not the right tool when:
  - The work is comparing a single policy version against external regulatory obligations (use `risk-compliance-core/policy-gap-review`; that skill is policy vs obligation, this skill is policy version A vs version B).
  - The work is parsing a new rule into atomic obligations before any policy work begins (use `regulatory-change-management/rule-to-obligation-extraction`).
  - The work is sequencing remediation across business units after the policy is approved (use `regulatory-change-management/implementation-plan`).
  - The trigger is drafting a new policy from scratch (route to the policy owner; this skill diffs, it does not draft).

argument-hint: "[two policy versions, or current policy plus proposed redline]"
---

# Policy diff

Two versions of a firm policy come in. A change log comes out: section by section, what moved, why it matters, who has to do something about it. The skill is the version-over-version diff that the policy owner, compliance, training, and change management all need before a refreshed policy goes live. The boundary with `policy-gap-review` is sharp: that skill compares a single policy version against external regulatory obligations and surfaces gaps; this skill compares two versions of the policy itself and surfaces what changed and what the change touches downstream.

The output reads like an annotated redline plus a downstream-impact view. The redline column says what physically changed in the document. The materiality column says whether the change matters. The downstream-impact view says who has to refresh training, revise a control, change a system, communicate to staff, re-attest, or wait for a follow-on amendment. The artifact is a draft until the policy owner and the named approver attest; the skill does not move a policy to live.

## Ask first

Before drafting, settle a few things. The conversation usually surfaces them in the first exchange.

- Which two versions. Version A and version B by version number, approval date, and document hash where available. "Current vs proposed" is allowed; "the latest" is not. A diff against an unidentified base is not a diff.
- What triggered the new version. Annual review, MRA remediation, regulatory amendment, internal incident, board direction, control failure, system migration, scope expansion. The trigger drives the materiality lens and the audience for the change log.
- Who reads the change log and what decision it supports. Policy committee approval, training-rollout planning, examiner response, audit support, board-paper appendix, line-manager comms. A diff for a policy committee differs from a diff for the line-manager rollout pack.
- What downstream artifacts need to refresh. Training modules, controls in the matrix, attestation rosters, system configurations, customer-facing disclosures, vendor contracts, the risk register. The skill enumerates the touchpoints that the change actually affects, not a generic checklist.
- Whether a control matrix or obligation register exists for the policy domain. When they do, the change log can foreign-key into them so a control owner sees the affected control IDs and the obligation register sees the affected obligation IDs without a separate cross-walk.

When `scope` is supplied, the skill consumes it for institution type, persona, source posture, sector overlay, and cross-cutting overlay. Otherwise it asks the few questions above and defaults to public posture if the practitioner declines. The change log notes when scope was not formalised.

## How the change log gets built

The skill walks the two versions section by section in document order. The conversation surfaces changes in whatever order the practitioner reads them, but the artifact reorders to document order so the reviewer can trace it against the policy itself.

The frame opens with what the diff is anchored on: policy name, version A (number, approval date, approver, document hash or pointer), version B (same), the trigger for the new version, the policy owner, the named approver for the new version, the target effective date, and the source posture. Source posture matters because policy diffs run in three modes: public-only when the firm has not supplied evidence pointers and the diff stays at structural level; public-plus-firm-policy when the diff cites internal cross-references and supersession chains; and connector-aware when the diff can read the live policy library and the control matrix to populate downstream-impact rows automatically.

Then the change log itself, one row per change. Sections that did not change get a single row stating no change so the reader can see they were inspected, not skipped. Each substantive row carries:

- **Change ID.** Stable identifier scoped to this diff run. Downstream artifacts (training-module register, control matrix, communication log) key off it.
- **Section path.** The policy's heading hierarchy plus paragraph or clause number. "§4.2(c) Vendor onboarding — Pre-contract due diligence." Section numbers from version B; if the section number itself moved between versions, both numbers appear.
- **Diff type.** One of `added`, `removed`, `reworded-substantive`, `reworded-cosmetic`, `restructured`, `defined-term-changed`, `cross-reference-changed`. Rewording is split because cosmetic edits (typo, formatting, capitalisation) are not material; substantive rewording (operative verb changed, scope expanded, threshold moved, exception added) usually is.
- **Version A excerpt.** The text as it stood. Short enough to be readable; long enough to carry the operative verb and object. Where the change is structural (entire subsection moved or removed), the excerpt is the heading plus first sentence.
- **Version B excerpt.** Same shape for the new text.
- **Substantive delta.** One sentence on what changed in operational terms. "Threshold for senior-management approval lowered from $5M to $2M" reads cleanly. "Updated to reflect current practice" does not. Capture the operative verb shift (must vs should), the operative object (each customer vs material customers), the threshold movement, the named-role change, the timing change, the scope-of-application change.
- **Materiality.** One of `material`, `incremental`, `clarifying`, `cosmetic`. Material means the obligation, control, or risk posture moves; the firm has to do something differently. Incremental means the same obligation, tightened or loosened in degree (frequency raised, threshold moved a step, named role refined). Clarifying means the substance is the same and the rewording removes ambiguity. Cosmetic means typography, spelling, formatting. The materiality call drives downstream-impact rows; cosmetic and clarifying rows usually carry no downstream impact.
- **Downstream impact.** What the change touches outside the policy text. The structured fields are training (yes / no / refresh-existing-module / new-module / specific roles only), control revision (yes / no / control IDs from the matrix), system change (yes / no / named system or control point), communication (yes / no / audience: all-staff / line-managers / specific function / customer-facing / vendor-facing / board), attestation (re-attestation required, fresh attestation required, none), and follow-on (linked open question or planned amendment). Each yes carries a one-sentence rationale; "yes" alone is not an impact.
- **Approver routing.** Who signs off on the change in this row. Policy committee, board, head of function, legal, compliance, model risk committee, AI governance committee, conduct committee, risk and audit committee. Where the row's materiality is material, named approver matters; where the materiality is cosmetic, the row's approver is usually the policy owner alone.
- **Effective date.** When the change takes effect for the firm. Same as the policy effective date by default; differs where the firm phases in a section (e.g., new control standard binds at year-end, training requirement binds 30 days after rollout). Phased rows carry both the policy's overall effective date and the section's specific binding date.
- **Open questions.** Items requiring legal or compliance review before the change moves out of draft. The conventional triggers: a substantive rewording where the practitioner is unsure if the operative verb shift is intended; a cross-reference change where the target document itself is mid-amendment; a defined-term change where the new term has not yet propagated to other policies; a threshold move where the firm's data has not been checked against the new threshold.
- **Confidence.** `high` where the diff is mechanical and the substantive delta is unambiguous (typo, additions called out in the redline, structural moves the policy committee documented). `medium` where the practitioner is reading interpretation into the rewording. `low` where the diff itself surfaces ambiguity (a paragraph deleted with no explanation in the change-control record).

The tail of the artifact carries what the rows cannot. Cross-policy ripple is where the change log notes references in other firm policies that point to a renamed defined term, a moved section number, or a deleted paragraph; those policies are stale until the references are reconciled. Defined-term inventory carries any term that changed name or scope; downstream skills (training, control matrix, attestation) pick this up. Approver routing summary groups material rows by approver so the policy committee or board paper can be drafted directly from it. Communication plan summary groups rows by audience so line-manager packs and all-staff comms can be sequenced. The source trace block records confidence by section. The sign-off block names the policy owner, the approver, and the independent reviewer (legal, compliance, or internal audit acting in advisory capacity).

### Sector and cross-cutting overlays

The change-log spine is the same across sectors. What flexes is the kind of policy in scope and the approver expectations. Load only the overlay the scope flags.

- `references/sector-overlays/banking.md` carries OCC heightened-standards expectations on written framework reviews and the federal-banking-agency expectation that material policy changes route to the board or a delegated committee with documented rationale.
- `references/sector-overlays/insurance.md` carries NAIC Corporate Governance Annual Disclosure expectations, ORSA policy lifecycle, and state market-conduct policy considerations.
- `references/sector-overlays/capital-markets.md` carries SEC IAA Rule 206(4)-7 annual-review obligations for compliance policies, FINRA Rule 3110 written supervisory procedures, and the Investment Company Act compliance-program lifecycle for funds.
- `references/sector-overlays/payments-fintech.md` carries Reg E, Reg Z, Reg DD policy considerations for consumer-payment products and the CFPB CMS expectation that policy changes are visible in the compliance management system's change record.
- `references/cross-cutting/cyber.md` loads when the policy is cyber-anchored: NYDFS Part 500 §500.3 cybersecurity-policy elements and the SEC Reg S-P safeguards-policy expectation.
- `references/cross-cutting/conduct.md` loads when the policy is a UDAAP or conduct-risk policy and the materiality lens covers customer harm.

Where firm policy or taxonomy applies (named approver titles, a defined committee structure, a particular policy-management system), it lives in `references/firm-overlay.md` and the change log pulls from there.

## Quality bar

The diff is anchored on two named versions. Version A and version B both carry version number, approval date, and approver. A diff against an unspecified base is not auditable; "vs the previous version" is not a citation. Where the base version is genuinely unidentified (the prior version was lost in a system migration), the row says so and the open-question summary picks it up.

The materiality call separates from the redline call. A reworded paragraph can be cosmetic; a single-word change can be material. The materiality lens is operational: does the firm do something differently because of this change. When the call is contested, the row carries `materiality: open-question` and routes to the named reviewer; the skill does not pre-empt the call.

The downstream-impact rows distinguish refresh-existing from new. A training module that needs a refreshed slide is not the same artifact as a new training module; a control whose evidence cadence changed is not the same as a new control. The granularity matters because change-management's effort estimate depends on it.

Approver routing matches the materiality. Material changes route to the named approver the firm's policy lifecycle requires (committee, board, function head). Cosmetic rows route to the policy owner alone. Routing a cosmetic row to the board is wasted committee time; routing a material row to the policy owner alone is a governance defect.

The change log is a draft until the policy owner and named approver attest. The skill does not set rows to approved, and it does not move a policy from draft to live. Material claims cite a source from version A or version B (or, for downstream impact, from the control matrix or obligation register where supplied). `[evidence needed]` flags items needing follow-up.

## Adaptation

Audience drives shape: a policy-committee paper clusters material rows to the front; a training-rollout pack clusters by audience; an examiner-readiness file pulls the trigger and the prior-state-vs-new-state delta forward. Source posture drives what the downstream-impact rows can carry. Sector and cross-cutting overlays load from scope. Confidence labels track by section.

## Output

The change log in `templates/default-output.md` shape and the structured record per `schemas/policy-diff.schema.json`. Downstream consumers: `implementation-plan` reads `changes[*].downstream_impact` to scope rollout sequencing; `control-matrix` reads `changes[*].linked_control_ids` to update affected controls; `obligation-mapping` and `policy-gap-review` read the diff when a refreshed policy needs an obligation re-anchor or a fresh gap review; `exam-brief` reads it when an examiner asks "what changed in your policy and why." The schema is the cross-skill contract; additive changes only between minor versions.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded from scope.
- `references/cross-cutting/{cyber,conduct}.md` — cross-cutting overlays loaded from scope.
- `references/firm-overlay.md` — firm-installed taxonomy, named approver titles, committee structure, policy-management system labels, internal cross-policy references; consumed when present.
- `templates/default-output.md` — change-log template.
- `schemas/policy-diff.schema.json` — structured-output contract.
- `examples/` — TPRM policy annual review with material rewording of subcontractor notification rights; cybersecurity policy MRA-driven amendment with new asset-inventory and data-classification provisions.
- `TROUBLESHOOTING.md` — recurring defects in policy diffs.
