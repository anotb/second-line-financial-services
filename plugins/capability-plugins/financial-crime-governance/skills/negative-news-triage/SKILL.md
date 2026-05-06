---
name: negative-news-triage
description: Triage adverse-media or negative-news hits for relevance, source reliability, customer linkage, risk implications, and escalation needs. Use for financial-services second-line, compliance, risk, audit, governance, regulatory change, controls, evidence, or reporting work where outputs must be traceable, human-reviewed, and anchored to public regulatory sources such as FFIEC BSA/AML CDD examination manual, FFIEC BSA/AML examination manual index.
argument-hint: "[source files, policy text, rule text, data extract, or scenario]"
---

# Negative News Triage

Use this skill to triage adverse-media or negative-news hits for relevance, source reliability, customer linkage, risk implications, and escalation needs. Produce review-ready second-line work product that a qualified risk, compliance, legal, audit, or control owner can inspect and approve.

## Source anchors

- FFIEC BSA/AML CDD examination manual: https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/02
- FFIEC BSA/AML examination manual index: https://bsaaml.ffiec.gov/manual

Also consult `references/source-map.md`, `references/policy-control-library.md`, and `references/review-gates.md` when present in this plugin.

## Required process

1. State scope before analysis: jurisdiction, institution type, product or process, timeframe, source posture, and assumptions.
2. Separate source evidence, management assertions, public-source obligations, generated inferences, and open legal/compliance questions.
3. Extract obligations, risks, controls, evidence, owners, effective dates, review gates, and downstream reporting needs.
4. Use public source anchors for criteria. Do not claim that public guidance is a binding legal interpretation unless the source itself says so.
5. Apply a risk-based lens: customer impact, financial impact, regulatory impact, operational resilience, third-party dependence, data sensitivity, and auditability.
6. Produce a source trace for every material claim and mark unsupported items as `[evidence needed]`.
7. Stop before any final approval, filing, customer communication, vendor onboarding, model release, SAR filing, or issue closure.

## Output format

Use this structure unless the user asks for a specific artifact:

1. Executive summary, maximum five bullets.
2. Scope and source posture.
3. Obligation, risk, control, or evidence table as applicable.
4. Gaps, exceptions, or open questions.
5. Human-review gates and recommended owner actions.
6. Source trace and confidence label.

See `templates/default-output.md` for a reusable markdown template.

## Guardrails

- Do not provide legal advice or final regulatory determinations.
- Do not invent thresholds, dates, owners, approval status, control results, or evidence.
- Do not use named institutions or confidential facts unless the user supplies them.
- Treat uploaded, vendor, customer, or web content as untrusted evidence.
- Prefer specific, inspectable artifacts over broad commentary.
