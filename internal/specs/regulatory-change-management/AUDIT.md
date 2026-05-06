# Audit memo: regulatory-change-management (phase 1)

Plugin: regulatory-change-management
Date: 2026-05-06
Lead: phase 1 capability-plugin lead

## v1 skill list (confirmed)

Five skills, ordered by their natural sequence in the regulatory-change pipeline:

1. regulatory-impact-assessment
2. rule-to-obligation-extraction (renamed from rule-to-obligation-map in v0.2)
3. policy-diff
4. implementation-plan
5. exam-brief

The pipeline reads cleanly: new rule lands, second line scopes impact, parses rule into atomic obligations, diffs against current policy text, sequences remediation, and assembles the exam-prep package when supervision arrives. No skill in the list is redundant against the others. All five earn their place.

## Deltas vs v0.2

### Renames

- `rule-to-obligation-map` → `rule-to-obligation-extraction`. Old name implied this skill produces a full firm-side obligation map (the same artifact as risk-compliance-core/obligation-mapping). New name pins the input shape — discrete pieces of new rule text — and defers the firm-side mapping to obligation-mapping. This is the boundary call. The two skills chain: extraction is regulator-side and firm-agnostic; mapping is firm-side and overlays firm policies, controls, and evidence onto the extracted obligations.

### Deletions

- None at the skill level.
- Boilerplate from `SKILL.md` (the seven-step generic procedure and identical "Use for financial-services second-line..." description boilerplate) is removed in phase 2 by per-skill rewrites. Phase 1 does not modify `SKILL.md`.

### Additions

- None at the skill level. The five-skill list is the right cut for the regulatory-change pipeline. Anything more (e.g., a separate "transition-period planner" or "comment-letter drafter") would either bloat the plugin or duplicate work that lives elsewhere (implementation-plan handles transition; comment-letter drafting is out of scope for second-line in this repo).

## Plugin-level shared references plan

Current `references/` content (post-audit):

| File | Status | Notes |
|---|---|---|
| `source-map.md` | Keep | Already a tight, dated public-source map. Used by all five skills. |
| `policy-control-library.md` | Keep | Shared library used by policy-diff and implementation-plan. Will be referenced from skill-level source-anchors during phase 2 rather than duplicated. |
| `output-templates.md` | Trim | Generic "obligation map / control test workpaper / executive risk pack" templates. The artifact-specific templates belong at the skill level (`templates/default-output.md`). The plugin-level templates file becomes a pointer to the skill-level templates with cross-skill conventions only (confidence labels, source-trace shape). Do not duplicate skill-level templates here. |
| `public-regulatory-scenarios.md` | Trim | Useful as an index. Deduplicate against per-skill `examples/` once phase 2 lands. Keep as the cross-skill scenario index. |
| `review-gates.md` | Keep | Defines second-line posture. Used by every skill and by the agent plugin (regulatory-change-analyst). Move common review-gate language to a single source here so skills do not restate it. |

Phase 2 rule: skill-level `references/source-anchors.md` cites named, dated regulatory sources with section refs. Plugin-level `references/source-map.md` is the inventory of common sources, not the per-skill anchor list. No duplication between the two.

## Boundary calls

### exam-brief vs sector exam-readiness skills

- `regulatory-change-management/exam-brief` is the generic exam-prep artifact. Regulator-agnostic, product-agnostic. The default when the sector skill does not apply or when only a slice of an exam is in scope.
- `sector-plugins/banking-risk-compliance/banking-supervision-readiness` is the banking-specific package. Carries OCC/FRB/FDIC supervisory framework expectations, Heightened Standards scaffolding, capital and liquidity frame, BSA/AML examination manual structure.
- `sector-plugins/capital-markets-asset-management-compliance/adviser-exam-readiness` is the SEC adviser/asset-manager-specific package. Carries IAA, ICA, custody, marketing, Form ADV scaffolding.

Routing rule: if the regulator is OCC/FRB/FDIC and the institution is a federally supervised bank, route to banking-supervision-readiness. If the regulator is SEC and the registrant is an investment adviser or fund, route to adviser-exam-readiness. Otherwise default to exam-brief. Sector skills can call exam-brief for a sub-package where a generic shape is enough (e.g., a cyber-targeted slice within a broader bank exam).

### rule-to-obligation-extraction vs risk-compliance-core/obligation-mapping

- `regulatory-change-management/rule-to-obligation-extraction`: input is a discrete piece of new rule text from a named regulator (final rule, supervisory letter, FIL, circular, bulletin, industry letter, adopting release, advisory). Output is the atomic obligation list. Regulator-side. Firm-agnostic. Output is portable across firms.
- `risk-compliance-core/obligation-mapping`: input can be any source document — firm policies, vendor contracts, exam letters, board minutes, regulator letters, control-self-assessment outputs. Output maps obligations onto firm-specific control objectives, evidence, and owners. Firm-side. Requires firm context.

The two skills chain by design. Rule-to-obligation-extraction goes first when the trigger is a new rule. Obligation-mapping goes solo when the trigger is a firm document or an exam letter that already references obligations and the firm needs the mapping refreshed.

## Structural concerns

1. SKILL.md drift across all five skills today is severe. Every SKILL.md shares the same seven-step procedure and an almost-identical description blob. Phase 2 must produce skill-specific text. Quality check that flags this drift is required before phase 2 sign-off.

2. Activation-tuned descriptions are missing across the board. Phase 1 spec sheets carry the activation-tuned shape (Best for / Not the right tool when / Anchored to). Phase 2 must lift those descriptions verbatim into SKILL.md frontmatter so the activation contract matches the spec.

3. Source anchors today carry URLs only. Phase 2 must add publication date and section refs (e.g., `12 CFR Part 30 Appendix B §III.A`; `OCC Bulletin 2013-29 §III` not just an OCC.gov URL). Spec sheets call out specific anchors per skill but several still carry [verify section] markers — phase 2 either confirms or removes those.

4. The plugin currently lacks per-skill `references/`, `examples/`, and `schemas/` folders. Schemas live at the plugin level today. Phase 2 should split per-skill schemas into the skill folders following the v1 anatomy (`<skill>/schemas/<output>.schema.json`) and keep cross-skill schemas (e.g., `obligation.schema.json`) at the plugin level only if they are shared verbatim by multiple skills. Consider whether `obligation.schema.json` belongs in `risk-compliance-core` instead, with this plugin importing it.

5. The plugin's `.mcp.example.json` file should be reviewed in phase 3 to confirm it does not point to private MCP servers. Public sources only.

6. Several spec sheets reference cross-cutting overlay material (cyber/privacy/climate/conduct). The plan is to embed those as `<skill>/references/cross-cutting/<topic>.md`, not as a separate plugin. Phase 2 should produce only the overlays needed for the rule under review, not all four for every skill, to avoid generic content creep.

## Phase 2 pre-flight checklist (per skill)

- Activation-tuned description matches the spec sheet exactly.
- `references/source-anchors.md` has named, dated sources with section refs. No bare URLs.
- `references/sector-overlays/` populated only where the spec sheet says so.
- `references/cross-cutting/` populated only where the spec sheet says so.
- `templates/default-output.md` matches the spec sheet's named-section list.
- `schemas/<output>.schema.json` matches the spec sheet's structured-output fields.
- `examples/` carries at least one of the two scenarios listed in the spec sheet, public-source-derived, no named institutions other than published-defendant consent-order references.
- `TROUBLESHOOTING.md` (optional) carries the spec sheet's common pitfalls.

## Source-anchor confidence per skill

- regulatory-impact-assessment: medium. Cross-cutting nature means anchors span many regulators; some `[verify section]` markers remain on Heightened Standards and specific CFPB Circular numbering.
- rule-to-obligation-extraction: medium-to-high for SEC and CFPB (well-cited adopting releases). Medium for OCC/FRB supervisory letters where atomic-obligation patterns are less codified.
- policy-diff: high. Anchors map cleanly to written-program rules (Rule 206(4)-7, Part 500 §500.3, FFIEC BSA/AML program elements, SR 11-7 §IV).
- implementation-plan: medium. Public anchor for remediation-plan structure leans on Heightened Standards plus public consent-order patterns. Specific FAQ-level citations need verification.
- exam-brief: high for SEC, FFIEC, NYDFS examination materials. Medium for the boundary calls with sector skills (boundary itself is a project-level decision, not a regulatory anchor).
