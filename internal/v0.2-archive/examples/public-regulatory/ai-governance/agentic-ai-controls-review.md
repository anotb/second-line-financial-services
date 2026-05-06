# Agentic AI controls review

## Source anchors

- NIST AI RMF supports govern, map, measure, and manage practices for AI risks.
- ISO/IEC 42001 describes an AI management system for policies, objectives, processes, performance evaluation, and continual improvement.
- OCC 2026 model risk materials identify generative AI and agentic AI as outside the revised model risk guidance scope, requiring separate governance consideration.

## Scenario

A second-line team reviews an AI agent that can read policies, summarize exceptions, draft risk acceptances, and create tickets in a workflow tool.

## Expected control matrix

| Control ID | Objective | Activity | Evidence |
|---|---|---|---|
| C-AI-001 | Prevent unauthorized action | Tool access limited to approved systems and actions; ticket creation requires human approval | Permission matrix, approval record, access review |
| C-AI-002 | Preserve traceability | Every generated risk acceptance includes source references and reviewer sign-off | Output sample, evidence binder, sign-off log |
| C-AI-003 | Detect unsafe behavior | Prompt-injection, policy-conflict, and hallucination tests performed before release and after material changes | Test plan, test results, remediation log |
| C-AI-004 | Govern changes | Prompt, tool, model, and policy changes follow change-control and approval workflow | Change ticket, reviewer approval, version history |

## Human-review gate

The AI agent must not approve risk acceptances, close issues, or submit regulatory responses.
