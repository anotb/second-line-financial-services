# Capital markets sector overlay for agentic-ai-controls

When the engagement-scope record names `capital-markets` as the sector, this overlay adds capital-markets-specific authority-statement constraints, tool-inventory expectations, monitoring signals, regulator-notification triggers, and co-reviewer expectations.

Loaded by: `agentic-ai-controls/SKILL.md` when `engagement_scope.sector_overlay_set` includes `capital-markets`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- SEC Rule 15c3-5 — Market Access Rule (17 CFR §240.15c3-5): pre-trade controls, post-trade surveillance, immediate access to a kill switch.
- FINRA Rule 3110 — Supervision; FINRA Rule 4530 — Reporting Requirements.
- SEC Investment Advisers Act Rule 206(4)-1 — Marketing Rule (17 CFR §275.206(4)-1) and Rule 204-2 — Books and Records.
- SEC Reg AC (17 CFR §242.501-505) — research-analyst certification.
- MAR (Market Abuse Regulation, EU 596/2014) for EU-nexus operations and surveillance integrity.
- SEC 8-K Item 1.05 and Reg S-K Item 106 for public registrants (cybersecurity disclosure).
- NYDFS Part 500 for NY-licensed broker-dealers and investment advisers.
- The joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026; supersedes SR 11-7) for bank-affiliated broker-dealers — note the bulletin expressly excludes agentic AI from scope (footnote 3) and reaches non-agentic components only.

## Recurring capital-markets agentic-AI use-case patterns

- **Research-analyst assistant**: agent retrieves over price data, public-source databases, internal research; drafts client-facing notes for analyst review. Marketing Rule reach for adviser-side notes; Reg AC for research-analyst certification.
- **Surveillance-system assistant**: agent reads trade and communication surveillance signals; assists with alert disposition, narrative drafting, escalation triage. Surveillance integrity is structural; injected content in flagged communications is a recurring risk.
- **Adviser co-pilot**: agent reads client-portfolio data; drafts client communications, IPS updates, performance commentary. Marketing Rule and books-and-records (Rule 204-2) reach.
- **Order-routing or order-management agent**: agent makes or assists in routing decisions; Rule 15c3-5 is the load-bearing anchor; kill switch and pre-trade controls are non-optional.
- **Operations agent for trade-lifecycle workflows**: agent handles confirmations, allocations, settlement-exception triage. Less consumer-facing; books-and-records and surveillance integrity apply.

## Authority-statement constraints specific to capital markets

For research-analyst assistants the out-of-scope list at minimum includes: no client-communication actuation (no auto-send); no order-routing or order-management interaction; no client-list access; no confidential-information cross-contamination across analysts. These are non-optional.

For order-routing agents (where in scope): the in-scope actions are bounded by the firm's pre-trade control framework under Rule 15c3-5; the out-of-scope list includes no order routing outside firm risk thresholds, no order routing outside client mandate, no override of pre-trade controls.

For adviser co-pilots: no client-communication actuation without the adviser's affirmative review; no recommendation that bypasses fiduciary-lens standards; no books-and-records-relevant action without preservation evidence.

## Tool-inventory expectations

- Order-routing tools (where in scope): integrate with the firm's pre-trade control framework; rate limits and value limits at the tool layer are mandatory; the kill switch on the agent is the kill switch on the order flow.
- Communication tools: blast-radius framing in policy units; books-and-records preservation under Rule 204-2 is non-optional.
- Surveillance tools: read-only on alert data; agent does not close alerts or modify case state without human supervisor approval.
- Research-data tools: per-analyst scoping; cross-coverage retrieval is a structural risk for information-barrier integrity.

## Human-oversight bar specific to capital markets

- For research-analyst assistants: block-and-wait analyst review of any client-facing draft; Reg AC certification is on the human, not the agent; Marketing Rule expectations apply to the deployed surface.
- For order-routing agents: the kill-switch operational decision and the pre-trade control gating are the oversight surface; human-in-the-loop or human-on-the-loop posture per Rule 15c3-5; rapid-disable capability is non-optional.
- For surveillance-system assistants: block-and-wait supervisor review on alert closure; FINRA Rule 3110 supervisory bar applies.
- For adviser co-pilots: block-and-wait adviser review on any client-impacting communication; fiduciary-lens framing on recommendations.

## Monitoring signals the overlay adds

- Order-routing agents: order-rate and order-value distributions per agent; pre-trade control trip rate; cross-mandate query anomaly; kill-switch activation events (any activation is signal).
- Research-analyst assistants: cross-coverage retrieval audit; client-facing draft volume; Marketing Rule trip rate on draft scanning.
- Surveillance-system assistants: alert-closure rate, alert-reopen rate, false-negative review rate.
- Adviser co-pilots: client-communication volume, suitability-trip rate where applicable.

## Incident-response and regulator-notification triggers

- Rule 15c3-5 events: erroneous orders, cross-mandate routing, post-trade surveillance failures may trigger SEC and FINRA reporting under Rule 17a-3, Rule 17a-4, Rule 4530.
- NYDFS Part 500 §500.17(a) for NY-licensed entities.
- SEC 8-K Item 1.05 for public registrants.
- Marketing Rule violations from agent-generated content: enforcement risk and remedial-action expectations.
- Surveillance-failure events: state and federal AG / SEC enforcement implications; the firm's compliance and surveillance escalation chain runs in parallel.

## Recommended-action items the overlay surfaces

- For order-routing agents, the Rule 15c3-5 control review is rerun against the agent's tool inventory; pre-trade controls cover the agent's actuation surface; the kill switch is integrated with the firm's market-access kill switch.
- For research-analyst assistants, Marketing Rule and Reg AC framings are reflected in the human-oversight design and the books-and-records preservation evidence.
- For surveillance-system assistants, FINRA 3110 supervisory bar is reflected in the human-oversight design and the alert-disposition audit cadence.
- For adviser co-pilots, fiduciary-lens framing is reflected in the residual-risk view; books-and-records preservation under Rule 204-2 is exercised in test (sample log entry).

## Common pitfalls specific to capital markets

- Treating an order-routing agent as a Rule 15c3-5-out-of-scope assistant. If the agent influences routing or order parameters, Rule 15c3-5 applies.
- Treating Marketing Rule reach on AI-generated adviser communications as a compliance-team-only concern. The agentic-controls review records the human-oversight design that operationalises the Marketing Rule expectation; absence is a finding.
- Omitting cross-coverage retrieval audit on research-analyst assistants. Information-barrier integrity is structural.
- Designing post-hoc sampling oversight on alert closure or research-note drafting. Block-and-wait is the correct mode; post-hoc on a closed alert or a published note is a supervisory failure.
