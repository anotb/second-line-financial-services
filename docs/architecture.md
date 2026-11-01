# Architecture

## Layers

1. Common references and schemas: public source map, policy-control library, review gates, templates, and shared JSON schemas.
2. Capability skill groups: horizontal second-line workflows, all in one plugin.
3. Sector skill groups: institution-specific skills and overlays that tailor capability workflows to banking, insurance, asset management, capital markets, payments, and fintech.
4. Agents (planned): end-to-end workflow agents in the same plugin, with focused subagents. Not in the current release; see [ROADMAP.md](../ROADMAP.md).

## Managed Agent API cookbooks

The main path of this repo is Claude Code and plugin-distributed standalone agents. Plugin-shipped subagents are sufficient for reader, critic, and writer worker patterns. Managed-agent cookbooks may be added later for upstream-contribution candidates; see [ROADMAP.md](../ROADMAP.md).
