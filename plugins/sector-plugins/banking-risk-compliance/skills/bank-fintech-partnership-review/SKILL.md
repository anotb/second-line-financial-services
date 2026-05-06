---
name: bank-fintech-partnership-review
description: Assess bank-fintech partnership risks across due diligence, contracts, consumer compliance, data, resilience, and ongoing monitoring. Use for financial-services second-line, compliance, risk, audit, governance, regulatory change, controls, evidence, or reporting work where outputs must be traceable, human-reviewed, and anchored to public regulatory sources such as U.S. interagency third-party risk management guidance, OCC release, U.S. interagency third-party risk management guidance, FDIC release, CFPB small business lending rule under Regulation B, Section 1071.
argument-hint: "[source files, policy text, rule text, data extract, or scenario]"
---

# Bank Fintech Partnership Review

Use this skill to assess bank-fintech partnership risks across due diligence, contracts, consumer compliance, data, resilience, and ongoing monitoring. Produce review-ready second-line work product that a qualified risk, compliance, legal, audit, or control owner can inspect and approve.

## Source anchors

- U.S. interagency third-party risk management guidance, OCC release: https://www.occ.gov/news-issuances/news-releases/2023/nr-ia-2023-53.html
- U.S. interagency third-party risk management guidance, FDIC release: https://www.fdic.gov/news/press-releases/2023/pr23047.html
- CFPB small business lending rule under Regulation B, Section 1071: https://www.consumerfinance.gov/rules-policy/final-rules/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b/

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
