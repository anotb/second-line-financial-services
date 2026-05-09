# Capital markets sector overlay for prompt-injection-risk

When the scope record names `capital-markets` as the sector, this overlay adds capital-markets-specific carriers, mitigations, monitoring signals, and incident-notification triggers to the review. Loaded by `prompt-injection-risk/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- SEC Investment Advisers Act Rule 206(4)-1 (Marketing Rule) for AI-generated client-facing content from registered investment advisers.
- SEC Adviser Books and Records Rule 17 CFR §275.204-2 and BD Rules 17 CFR §240.17a-3 / §240.17a-4 for preservation of AI-generated records supporting recommendations or trading decisions.
- SEC Investment Advisers Act Rule 206(4)-7 (Compliance Program Rule) where the AI system is in scope of the adviser's compliance programme.
- SEC Rule 15c3-5 (Market Access Rule) where the GenAI system is in the path of an order-routing or market-access decision.
- SEC Regulation BI and the SR/IA fiduciary lens where the AI output supports retail recommendations.
- SEC cyber disclosure rules (8-K Item 1.05 and Reg S-K Item 106) for public registrants.
- FINRA Rules 2010 (standards of commercial honor), 2210 (communications with the public), 3110 (supervision), and 4511 (general books and records) for FINRA member broker-dealers.
- Market Abuse Regulation (EU) 596/2014 and SEC Rule 10b-5 / Regulation FD where the AI system handles or generates content adjacent to material non-public information.

## Carriers and trust posture nuances specific to capital markets

The recurring capital-markets GenAI use-case patterns and the carriers that usually drive the threat surface:

- **Equity research assistant**: retrieves over internal research notes, past models, vendor research, earnings transcripts, news, social media. Highest-likelihood vector is indirect injection in third-party content (news, social media, transcripts, vendor research). For agentic configurations with tool use (web fetch, market-data API, draft-write), the threat surface fans out per the agentic example in `examples/agentic-research-assistant.md`.

- **Investment-banking deal assistant**: retrieves over deal documents, comparables, legal precedents, regulatory filings. The MNPI handling lens is structural; cross-deal information bleed is the structural risk and the conduct-side seam is information-barrier integrity.

- **Compliance and surveillance assistant**: retrieves over transaction records, communication archives (email, chat, voice transcripts), market data, alert narratives. Highest-likelihood vector is indirect injection via communication-archive content (which can be free-text and user-controlled at origin); surveillance-system integrity is the downstream consequence.

- **Wealth-management/RIA client-facing assistant**: retrieves over client profiles, account history, model portfolios, planning content. The Marketing Rule and Reg BI / fiduciary lens bite hard; any AI-generated client-facing content is in scope of the Marketing Rule for advisers, and the books-and-records preservation applies.

- **Trading-desk and execution-algo support**: where the GenAI system is in or adjacent to the order path, Rule 15c3-5 controls overlap with the prompt-injection mitigation set; the trading-controls function is a co-reviewer.

## Mitigations the review should expect to see

Beyond the standard set:

- Marketing Rule output filtering for any AI-generated client-facing content; compliance signs off on the filtering specification. The general prohibitions, performance-presentation rules, and testimonial/endorsement requirements all apply where the output meets the definition of an advertisement.
- Books-and-records capture of AI-generated content supporting a recommendation or trading decision; the record-retention configuration is part of the mitigation set.
- Information-barrier-aligned retrieval scoping for any system that operates across deal teams or across public and private sides; cross-side retrieval is a finding, not a discretionary mitigation.
- MNPI-handling controls on retrieval scoping for systems handling deal documents, research-in-progress, or material non-public information; the firm's information-barrier programme defines the scope.
- Surveillance-system integrity controls for systems that support alert disposition; the surveillance and supervision functions co-sign the mitigation specification.
- Rule 15c3-5 control overlap for any system in the order path; the trading-controls function reviews the GenAI-side mitigations against the existing market-access controls.
- For agentic systems with tool use, planner-side topic validation and tool-boundary controls; tool-boundary on any tool that could publish, send, trade, or take a consequential external action is the load-bearing mitigation.

## Monitoring signals the overlay adds

- Marketing Rule output-filter trip rate for any client-facing AI output; escalation to compliance.
- Books-and-records preservation health check (is the AI-generated content actually being retained per the firm's books-and-records configuration?); periodic.
- Cross-deal or cross-side retrieval audit for systems operating across information-barrier boundaries; any confirmed event is an investigation trigger.
- Cross-ticker tool-invocation anomaly for systems with market-data tool access (queries on tickers outside the user's coverage); escalation to surveillance and supervision.
- Tool-invocation rate and pattern monitoring for agentic systems; escalation to information security with cyber overlay framing.
- For systems supporting surveillance, alert-disposition anomaly and SAR-narrative integrity sampling.

## Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- SEC Marketing Rule violation: a confirmed publication of misleading AI-generated client communications creates Marketing Rule exposure; compliance evaluates against the Marketing Rule violation framework and against the firm's compliance-programme self-reporting posture.
- SEC books-and-records violation: a confirmed failure to preserve AI-generated records supporting a recommendation or trading decision creates books-and-records exposure.
- FINRA Rule 4530 reporting: FINRA member broker-dealers must report certain events under Rule 4530; AI-driven incidents that fall within the rule's scope are reportable.
- Information-barrier breach via cross-side retrieval: legal and compliance evaluate; potential reportable event depending on materiality and the firm's information-barrier programme commitments.
- Market Abuse Regulation considerations for EU-footprint registrants: AI-driven inadvertent disclosure of MNPI or AI-driven market-manipulation-relevant output is in scope.

## Recommended-action items the overlay surfaces

- Where the use case is client-facing and from a registered investment adviser, the Marketing Rule compliance review is a required pre-prod step, not a discretionary one; compliance co-signs the residual-risk acceptance.
- Where the use case operates across information-barrier boundaries, the information-barrier owner co-signs and the retrieval-scope configuration is documented in the firm's information-barrier programme.
- Where the use case is in or adjacent to the order path, the trading-controls function reviews the GenAI-side mitigations against the Rule 15c3-5 control framework.
- Where the use case supports surveillance, the chief compliance officer or the head of surveillance co-signs the residual-risk acceptance.
- For agentic systems with tool use, the planner-side topic validation and the tool-boundary controls are tested under firm-internal red team before pre-prod gate; vendor red-team coverage of multi-agent and tool-use topologies is typically thin.

## Common pitfalls specific to capital markets

- Treating an internal-only research assistant as out of Marketing Rule scope. The moment the analyst publishes the AI-drafted note, the Marketing Rule reach kicks in. The analyst-publication seam is where the conduct lens lands; the review records the seam as a residual risk and the analyst-attestation step as a recommended mitigation.
- Omitting the books-and-records preservation health check. AI-generated content that is not preserved per the firm's books-and-records configuration is a recurring exam finding; the review records the preservation control and the periodic health check.
- Treating information-barrier retrieval scoping as a one-time configuration decision. The retrieval scope must be re-validated when the information-barrier programme changes, when the data sources change, and when the user population changes.
- Failing to involve the trading-controls function for systems in or adjacent to the order path. Rule 15c3-5 controls are not optional; the GenAI-side mitigations must be reviewed alongside the existing market-access controls, not in parallel.
- Treating vendor red-team coverage as sufficient for agentic systems with tool use. Vendor sets do not exercise multi-agent topologies and rarely exercise firm-specific tool inventories; firm-internal red team is the load-bearing test source.
- Recording rolling-with-notice foundation-model versioning for any tier-1 or tier-2 capital-markets agentic system. Pinned versioning is the recommended posture; the review surfaces the rolling-with-notice posture as a finding and pinning as a recommended action.
