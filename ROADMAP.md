# Roadmap

## Highest priority

1. Run `claude plugin validate` against each plugin in the target Claude Code version.
2. Add golden conversation tests for the six standalone agent workflows.
3. Add firm-specific overlays for policy taxonomy, risk ratings, issue severity, control naming, evidence standards, and committee templates.
4. Add approved MCP connectors for GRC, policy, document management, ticketing, data lineage, model inventory, vendor inventory, and incident management systems.

## Capability backlog

- Add supervisory priority watchlist skills by regulator and sector.
- Add policy lifecycle workflows: annual review, attestation, exception handling, and policy-control traceability.
- Add data governance controls for AI, BCBS 239, regulatory reporting, and data quality incidents.
- Add operational resilience scenario-test planner for severe but plausible scenarios.
- Add issue remediation validation and closure QA.

## Test backlog

- Add JSON Schema validation tests for every sample output.
- Add no-unsupported-claims lint for generated examples.
- Add source-trace completeness tests.
- Add agent subagent-name uniqueness tests across plugins.
- Add drift checks for copied references and schemas, not just skills.
