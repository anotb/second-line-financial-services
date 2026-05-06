# AI Governance Reviewer

Runs end-to-end second-line review of AI use cases, model-risk artifacts, agentic controls, EU AI Act triage, AI vendor evidence, and AI risk committee materials.

## Subagent design

This standalone agent plugin is self-contained. It bundles the skills it uses and ships a primary workflow agent plus focused worker subagents under `agents/`. The design follows Claude Code plugin conventions: plugin-shipped agents are Markdown files with YAML frontmatter, specialized descriptions, tool scoping, and focused prompts.

## Human review

Outputs are drafts for qualified review. The agent stops before approvals, filings, customer communications, final risk ratings, vendor onboarding, model releases, issue closure, or SAR filing.
