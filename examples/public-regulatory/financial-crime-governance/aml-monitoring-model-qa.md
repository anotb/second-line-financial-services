# AML monitoring model QA

## Source anchors

- OCC 2026 model risk guidance discusses development and use, validation and monitoring, governance and controls, and vendor or third-party model considerations.
- FFIEC BSA/AML CDD and SAR materials describe ongoing monitoring and suspicious activity reporting expectations.

## Scenario

A transaction-monitoring scenario was tuned to reduce false positives. Alert volumes dropped materially, but the change record does not include outcomes analysis or independent challenge evidence.

## QA focus

| Area | Question |
|---|---|
| Change rationale | What business, typology, data, or performance evidence justified tuning? |
| Data quality | Were input fields complete and stable before and after tuning? |
| Outcomes analysis | Did the change reduce true-positive detection or SAR-worthy activity? |
| Validation | Was conceptual soundness and performance independently reviewed? |
| Governance | Was the change approved by the correct model, AML, and compliance owners? |

## Human-review gate

AML compliance and model risk reviewers must approve any final conclusion or remediation plan.
