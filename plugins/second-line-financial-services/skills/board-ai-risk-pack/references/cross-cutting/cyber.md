# Cross-cutting overlay: cyber — board AI risk pack

Loaded when the scope flags cyber. The overlay carries content that lands in the pack body, not background reading. The standing anchor for AI cyber posture in financial services is the NYDFS Industry Letter on Cybersecurity Risks Arising from AI (October 16, 2024) for NY-footprint firms, layered over existing cyber program expectations (23 NYCRR Part 500, FFIEC IT Booklet, FRB SR 20-15, sector-specific frameworks).

## Where it lands in the pack

The cyber overlay does not get its own appendix. It threads through several pack sections:

- **Top AI risks**: AI-cyber risks named explicitly when elevated. AI-enabled threats (deepfake-driven social engineering, AI-aided phishing, voice-clone attacks on call centres, synthetic identity fraud) are one bucket; the firm's own use of AI as a cyber surface (prompt injection, indirect prompt injection through retrieved content, data exposure through GenAI outputs, vendor concentration on AI providers) is the other.
- **Incidents and near-misses**: AI-cyber incident classifications surface here. Prompt-injection signal events, data-leakage events through AI systems, AI-vendor security incidents, deepfake-attempt events targeting customer authentication, and AI-aided phishing campaigns directed at the firm.
- **Foundation-model and AI vendor exposure**: AI vendor security posture is part of the standing exposure picture. Vendor security incidents, vendor breach notifications, vendor SOC 2 / ISO 27001 / FedRAMP posture, vendor model-supply-chain integrity attestations.
- **GenAI program status**: prompt-injection signal trend is the standing GenAI cyber metric. Indirect prompt injection through retrieved content (RAG poisoning, retrieved-document tampering) is an explicit sub-line where RAG is in production. Agentic tool-boundary events are the agentic-cyber metric.
- **AI governance maturity posture**: cyber program integration is one of the standing maturity dimensions. Coverage of AI in the cybersecurity program governance, integration with the firm's incident response runbook, integration with the third-party cyber-risk program for AI vendors.

## Top AI cyber risks (catalogue for selection, not all-required)

The pack does not enumerate every category every cycle; the top-risks list carries the small number that drove committee attention this period.

- AI-enabled external threats: deepfake voice for call-centre social engineering; AI-aided phishing including spear-phishing and BEC; voice-clone attacks on executive-impersonation channels; synthetic-identity fraud on customer onboarding.
- Firm's own use of AI as cyber surface: prompt injection (direct and indirect through RAG, tool inputs, agentic context); data exposure through GenAI outputs (NPI leakage, PHI leakage where applicable, IP exposure); inappropriate use of GenAI by employees with confidential firm data (shadow AI).
- AI vendor cyber surface: foundation-model vendor security incidents; foundation-model vendor breach posture; AI-evaluation vendor security; agent-platform security; RAG infrastructure security; supply-chain integrity of vendor model artifacts.
- AI-driven monitoring degradation: cyber-AI tools (SIEM, XDR, fraud monitoring) degrading over time without re-tuning; false-positive volume spikes; coverage gaps from over-tuning.

## Sign-off questions tagged to cyber

Surface in the reviewer-questions section of the pack when applicable:

- How does the firm monitor prompt-injection signal in production GenAI systems, and what is the trend this period.
- How does the firm assure foundation-model vendor breach posture, and what is the inventory of vendor incidents disclosed to the firm in the period.
- How does the firm address AI-enabled external threats in the cybersecurity program, and where in the program is the named ownership.
- For NY-footprint firms: how does the firm document NYDFS October 2024 Industry Letter alignment in the cybersecurity program.

## Linkage

The depth on cyber-AI controls lives in `prompt-injection-risk` and `agentic-ai-controls` outputs (where the firm has run them). The board AI risk pack consumes briefs from those outputs rather than re-anchoring the cyber sources.
