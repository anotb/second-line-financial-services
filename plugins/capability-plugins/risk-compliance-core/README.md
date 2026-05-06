# Risk Compliance Core

Foundational primitives reused by other capability plugins.

This plugin is the canonical home for the second-line artifacts that show up in every other capability plugin: obligation registers, control matrices, evidence binders, issue write-ups, human-review gates, and policy gap reviews. Other capability plugins (compliance-testing, third-party-operational-resilience, regulatory-change-management, ai-governance-model-risk, risk-reporting, financial-crime-governance, consumer-compliance-fair-lending) consume these primitives rather than redefining them.

## v1 skill list

- `obligation-mapping` — convert source documents (rules, guidance, exam manuals, internal policies) into a structured obligation register with applicability, control objectives, evidence required, and owners.
- `control-matrix` — build an obligation-anchored risk-control matrix mapping control objectives, activities, owners, frequency, evidence pointers, test method, last test result, and open issues.
- `evidence-binder` — index evidence for a regulatory exam, internal audit, model validation, vendor review, or committee review, with system-of-record provenance and completeness flags.
- `issue-writeup` — draft a finding using the standard condition / criteria / cause / effect structure plus severity rationale, remediation, owner, target date, and closure-evidence definition.
- `human-review-gates` — produce the named-gate matrix for a workflow (AI use-case lifecycle, vendor onboarding, issue rating) with required reviewers, decision criteria, stop conditions, and escalation paths.
- `policy-gap-review` — compare a firm policy against a named obligation set or public-source-informed benchmark and produce a gap matrix with severity, recommended edits, and evidence needs.

## Use note

A second-line lead picks up this plugin when the work calls for one of these named artifacts: an obligation register fed from a fresh source, a control matrix that survives an internal audit walkthrough, an evidence binder a regulator can navigate without a guided tour, an issue write-up the audit committee will accept, a gate matrix a committee charter can adopt, or a policy gap review pitched at the redline-author. The skills draft. A qualified reviewer signs off. Nothing here approves use cases, files reports, rates issues finally, onboards vendors, or closes findings.

## Components

- `skills/` — the six skills above, each with a `SKILL.md` and a `templates/default-output.md`. Phase 2 adds per-skill `references/`, `examples/`, and (where applicable) `scripts/`.
- `references/` — plugin-level shared references: public-source map, policy and control library, review gates and confidence labels.
- `schemas/` — structured-output templates for obligations, controls, and issues. Other plugin schemas (AI use case, vendor, test plan, risk report) currently live here but move to their owning plugins in phase 3.

## Operating posture

This plugin drafts second-line work product for qualified review. It does not approve, file, rate, onboard, decline, notify, or close items. Public regulatory and standards sources are anchors, not legal interpretations.

## Shared schema definitions

`schemas/_defs.json` holds shared JSON Schema `$defs` (severity_enum, confidence_label, owner_role, source_trace_entry, human_review_gate, iso_date, engagement_scope_ref) that per-skill schemas can `$ref` instead of redefining inline. Per-skill schemas should reference these via `"$ref": "../_defs.json#/$defs/<name>"` from `<plugin>/skills/<skill>/schemas/<name>.schema.json`. Additive changes only between minor versions; breaking changes ship as a versioned migration.
