# OCC 2026 model risk and AI governance gap assessment

## Source anchors

- OCC Bulletin 2026-13 states the revised model risk guidance is risk-based and discusses model development and use, validation and monitoring, governance and controls, and vendor or third-party products.
- OCC Bulletin 2026-13 also states generative AI and agentic AI are novel and rapidly evolving and are not within the scope of that guidance.
- NIST AI RMF and ISO/IEC 42001 provide public AI risk management anchors for AI systems that fall outside traditional model-risk guidance scope.

## Scenario

A banking organization wants to use a tool-using AI agent to summarize commercial borrower files, compare covenant data to policy thresholds, draft monitoring commentary, and create cases for relationship-manager review.

## Expected risk and control focus

| Risk | Control expectation | Evidence |
|---|---|---|
| Agent output influences credit monitoring without sufficient reviewer challenge | Human approval gate before case closure or customer action | Approval queue, override log, reviewer procedure |
| Agent accesses systems beyond approved scope | Least-privilege tool permissions and audit logs | Tool permission matrix, access review, log sample |
| Prompt or document injection changes agent behavior | Treat source documents as untrusted and restrict executable actions | Prompt-injection test results, runbook, incident log |
| Monitoring model or AI performance degrades | Periodic outcomes analysis and exception review | Performance dashboard, drift report, validation memo |

## Human-review gate

Model risk, AI governance, credit risk, compliance, and technology risk should review before production deployment.
