# EU AI Act creditworthiness triage

## Source anchors

- Regulation (EU) 2024/1689, Annex III, point 5(b), classifies AI systems used to evaluate creditworthiness of natural persons or establish a credit score as high-risk, except systems used for fraud detection only.
- NIST AI RMF 1.0 provides voluntary govern, map, measure, and manage functions for AI risk management.
- ISO/IEC 42001 provides an AI management system structure for responsible AI governance.

## Scenario

A financial institution proposes an AI-assisted consumer credit pre-screening workflow. The workflow scores natural-person applicants, recommends whether the application should move to manual underwriting, and provides reason-code suggestions for reviewer consideration. The workflow is not limited to fraud detection.

## Expected analysis

| Area | Draft finding |
|---|---|
| EU AI Act triage | Potential high-risk AI system because the use case evaluates creditworthiness of natural persons or establishes a credit score. |
| Human oversight | Required before adverse customer impact. Reviewer must be able to understand, challenge, override, and document the decision. |
| Evidence needed | Use-case intake, model card, data lineage, bias and performance testing, monitoring plan, reviewer procedure, override log, customer-impact assessment. |
| Open questions | Provider versus deployer role, profiling assessment, jurisdictional scope, whether pre-screening materially influences final credit decision. |

## Human-review gate

Legal and compliance review required before classification, deployment, customer communication, or regulatory representation.
