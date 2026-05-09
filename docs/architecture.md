# Architecture

## Layers

1. Common references and schemas: public source map, policy-control library, review gates, templates, and shared JSON schemas.
2. Capability plugins: horizontal second-line workflows that can be installed independently.
3. Sector plugins: institution-specific overlays that tailor capability workflows to banking, insurance, asset management, capital markets, payments, and fintech.
4. Agent plugins (planned): self-contained end-to-end workflow agents with bundled skills and focused subagents. Not in the current release; see [ROADMAP.md](../ROADMAP.md).

## Managed Agent API cookbooks

The main path of this repo is Claude Code and plugin-distributed standalone agents. Plugin-shipped subagents are sufficient for reader, critic, and writer worker patterns. Managed-agent cookbooks may be added later for upstream-contribution candidates; see [ROADMAP.md](../ROADMAP.md).
