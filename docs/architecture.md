# Architecture

## Layers

1. Common references and schemas: public source map, policy-control library, review gates, templates, and shared JSON schemas.
2. Capability plugins: horizontal second-line workflows that can be installed independently.
3. Sector plugins: institution-specific overlays that tailor capability workflows to banking, insurance, asset management, capital markets, payments, and fintech.
4. Agent plugins: self-contained end-to-end workflow agents with bundled skills and focused subagents.

## Why bundle skills into agent plugins

Agent plugins should be installable on their own. The source skill remains in a capability or sector plugin. `scripts/sync-agent-skills.py` copies those skills into agent plugins and `scripts/check.py` detects drift.

## Managed Agent API cookbooks

The main path of this repo is Claude Code and plugin-distributed standalone agents. Plugin-shipped subagents are sufficient for reader, critic, and writer worker patterns. Managed-agent cookbooks may be added in v1.1 for upstream-contribution candidates and live under `managed-agent-cookbooks/<agent>/`, excluded from the marketplace manifest and from the skill-sync script.
