# Spec: policy-diff

Plugin: regulatory-change-management
Status: phase 1 spec sheet, pending phase 2 build
Date: 2026-05-06

## Activation-tuned description

Compares current firm policy or procedure text against a regulatory source (rule, supervisory letter, manual chapter, or atomic obligation list) and produces a gap-and-conflict log. Each finding identifies the policy clause, the regulatory anchor, the nature of the gap (silent, partial, conflicting, stale), the proposed redline direction, and the open question for the policy owner.

Best for:
- A new rule has been extracted into obligations and the policy owner needs to know what the firm's current policy already covers, partially covers, or is silent on.
- An exam letter or MRA references specific policy clauses and the firm needs a structured comparison before responding.
- An annual policy review cycle and the second line needs to confirm policies still align to current rule text and updated supervisory expectations.

Not the right tool when:
- The rule has not been parsed into obligations yet (use rule-to-obligation-extraction first).
- The objective is to draft new policy from scratch rather than diff (the skill produces redline directions, not full policy drafts; route to first-line policy owner with the diff).
- The objective is to plan remediation across business units (use implementation-plan).

Anchored to: 12 CFR Part 30 Appendix B (heightened standards, written program requirements) [verify section]; OCC Bulletin 2013-29 §III (third-party policies); SR 11-7 §IV (policies and procedures for model risk); FFIEC BSA/AML Examination Manual (BSA/AML compliance program policies); FINRA Rule 3110 (supervision); SEC Investment Advisers Act Rule 206(4)-7 (compliance policies and procedures); NYDFS Part 500 §500.3 (cybersecurity policy).

## Source anchors

- 12 CFR Part 30 Appendix B (Heightened Standards) — written framework requirements [verify section ref].
- OCC Bulletin 2013-29 and the 2023 interagency revision — third-party policy elements.
- SR 11-7 §IV (policies and procedures for model risk management).
- FFIEC BSA/AML Examination Manual — sections on BSA compliance program policy elements.
- FINRA Rule 3110 (Supervision) — written supervisory procedures.
- SEC IAA Rule 206(4)-7 (Compliance Programs of Investment Advisers) — written policies and procedures.
- NYDFS 23 NYCRR Part 500 §500.3 (cybersecurity policy elements).
- ISO/IEC 42001:2023 §5 (leadership and policy) for AI policy diff.
- NIST AI RMF 1.0 Govern function for AI policy diff.

## Sector overlays needed

- banking.md — heightened-standards written framework expectations; Reg O, Reg W, Reg Y, Reg LL policy elements.
- insurance.md — NAIC Corporate Governance Annual Disclosure (CGAD); ORSA policy elements; market conduct policies.
- capital-markets.md — IAA Rule 206(4)-7 elements; Investment Company Act compliance policies; FINRA WSPs; SEC Marketing Rule policies.
- payments-fintech.md — Reg E policies, money-transmitter compliance program policies, CFPB UDAAP compliance management.

## Cross-cutting overlays needed

- cyber.md — NYDFS Part 500 written cybersecurity policy elements; SEC Reg S-P safeguards policy.
- privacy.md — GLBA written information security program; CCPA notice and privacy policy elements.
- climate.md — climate risk management policy elements where in scope (large banks).
- conduct.md — UDAAP/UDAP policy elements; conduct-risk framework elements.

## Output template named sections

1. Diff summary (counts: aligned / partial / silent / conflicting / stale)
2. Source-side scope (regulatory anchor inventory, citation, version, date)
3. Policy-side scope (policy document name, version, last-approved date, owner)
4. Finding log (one row per gap or conflict)
5. Cross-policy conflicts (where two firm policies disagree on the same obligation)
6. Stale references (policy citations to superseded rule versions)
7. Proposed redline directions (not full redline; direction with rationale)
8. Open questions for policy owner and legal
9. Source trace and confidence labels

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| diff_id | string | Stable ID for the diff run |
| policy_doc | object {name, version, approved_date, owner_role, scope} | Policy under review |
| regulatory_anchors | array<object {regulator, citation, section, date}> | What the policy is being compared against |
| findings | array<finding> | Gap and conflict log |
| finding.id | string | Stable finding ID |
| finding.policy_clause | object {section, page_or_para, text_excerpt} | Where in the policy |
| finding.regulatory_anchor | object {regulator, citation, section} | Where in the rule |
| finding.gap_type | enum {aligned, partial, silent, conflicting, stale} | Nature of finding |
| finding.severity | enum {high, medium, low} | Practitioner severity, not legal severity |
| finding.proposed_direction | string | Redline direction (e.g., "Add explicit annual review cadence; align defined term 'covered employee' to NYDFS Part 500 §500.1") |
| finding.owner_role | string | Policy owner role |
| finding.open_questions | array<string> | Items needing legal/owner sign-off |
| finding.confidence | enum {high, medium, low, unknown} | Confidence label |
| cross_policy_conflicts | array<object {policy_a, policy_b, obligation_ref, conflict}> | Inter-policy conflicts surfaced |
| source_trace | array<object {claim, citation}> | Material claims tied to citations |

## Example scenarios (public-source-derived)

1. Third-party risk policy at a national bank diffed against OCC Bulletin 2013-29 and the 2023 interagency TPRM guidance. Findings: policy is silent on contractual subcontractor notification rights (gap); policy still references "critical activities" without the 2023 guidance's risk-based language (stale); business-continuity expectations are partial (no exit-plan testing cadence).
2. Information security policy diffed against NYDFS 23 NYCRR Part 500 §500.3 elements. Findings: written policy lacks explicit data classification, customer data retention, and asset inventory provisions called out in §500.3; CISO sign-off cadence partial; vendor risk overlap with Part 500 §500.11 needs reconciliation.

## Common pitfalls

1. Generating full redline text instead of redline direction. Drafting policy is the policy owner's job. The diff names the gap and proposes direction; it does not write the new clause.
2. Diffing policy against a regulator press release or guidance summary instead of the operative rule text. Stale and inaccurate by construction.
3. Treating "the policy is silent" as automatically a gap. Silence may be acceptable if a downstream procedure or standard covers it. Pull the procedure and confirm before logging.
4. Missing cross-policy conflicts. The information security policy and the third-party risk policy will both touch vendor cyber expectations. Inconsistencies between them are a finding.
5. Not capturing policy version and approved date. A diff against a policy that is already mid-review is a different artifact from a diff against the live policy.
