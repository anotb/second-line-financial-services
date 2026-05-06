# Risk Reporting Analyst

Produces risk committee, BCBS 239, KRI, cyber disclosure readiness, attestation, and management-response materials from risk metrics and evidence.

## Subagent design

This standalone agent plugin is self-contained. It bundles the skills it uses and ships a primary workflow agent plus focused worker subagents under `agents/`. The design follows Claude Code plugin conventions: plugin-shipped agents are Markdown files with YAML frontmatter, specialized descriptions, tool scoping, and focused prompts.

## Human review

Outputs are drafts for qualified review. The agent stops before approvals, filings, customer communications, final risk ratings, vendor onboarding, model releases, issue closure, or SAR filing.
