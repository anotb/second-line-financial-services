# Capital markets sector overlay for ai-risk-tiering

When the engagement-scope record names sector `capital-markets`, this overlay tells the tier rubric what is adviser-, broker-dealer-, and fund-specific. Tier names and cutoffs are firm policy; this overlay names which factors elevate, which gates trigger by default, and which re-tiering events to name.

Loaded by: `ai-risk-tiering/SKILL.md` when `engagement_scope.sector_overlay_set` includes `capital-markets`. Source content derived from the capital-markets lead's overlay snippets, mapped here into the tiering context. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- SR 11-7 reach is partial for non-bank registrants (advisers and BDs that are not part of a BHC); the rubric falls back on NIST AI RMF and ISO/IEC 42001 as the primary anchor and uses SR 11-7 / OCC Bulletin 2026-13 only where the parent BHC inherits the model risk through a banking subsidiary.
- SEC Investment Advisers Act Rule 206(4)-7 (compliance program) and Rule 206(4)-1 (Marketing Rule).
- FINRA Rule 3110 (supervisory system); FINRA Rule 5310 (best execution); SEC Reg BI for BDs.
- SEC Rule 15c3-5 (Market Access Rule) for execution algos and order-routing models.
- SEC Investment Adviser Books-and-Records Rule 204-2 and BD Rules 17a-3 / 17a-4.
- Investment Company Act Rule 38a-1 for fund context, including sub-adviser oversight under §38a-1(a)(4).
- SEC proposed rules on conflicts of interest in the use of predictive data analytics (proposed July 2023) [verify current state — proposal, withdrawal, or further action].
- SEC Division of Examinations risk alerts on AI / predictive analytics in adviser practices [verify current state and exact reference].

## Capital-markets tier criteria

The tier rubric's regulatory and conduct factors absorb capital-markets-specific elevation factors. The use-case categories below are the most-frequent shapes; tier values remain firm policy.

### Execution algorithms and order-routing models

- The model directs or influences routing, order-placement, or order-handling decisions; SEC Rule 15c3-5 controls are operative and the regulatory factor scores high.
- Market integrity exposure (FINRA Rule 5310 best execution; spoofing, layering, and other market-abuse surfaces) elevates the conduct factor.
- For the largest BDs, the model risk pedigree feeds into the firm's market-access controls; the tier decision flags Rule 15c3-5 control overlap as a triggered gate.
- Default tier elevation: tier-1 or tier-2 in firm-policy-typical mappings.

### Surveillance models (insider trading, market manipulation, layering, spoofing)

- The model triages or scores potentially unlawful conduct; FINRA Rule 3110 supervisory expectations apply.
- False-negative cost is doctrinally distinct from false-positive cost (missed surveillance hit vs analyst time); the tier decision names both as monitoring metrics.
- Default tier elevation: tier-2 in firm-policy-typical mappings, with conduct factor high.

### AI in marketing materials and client communications

- For investment advisers, Rule 206(4)-1 (Marketing Rule) reaches AI-generated client communications, AI-generated hypothetical performance, and AI-generated testimonials/endorsements.
- The tier decision flags Marketing Rule reach when output reaches clients or prospective clients; required disclosures are a triggered control gate.
- Books-and-records reach under Rule 204-2 (advisers) or Rule 17a-3 / 17a-4 (BDs) applies to AI-generated content supporting recommendations.
- Default tier elevation: tier-2 in firm-policy-typical mappings; tier-1 if the AI is unreviewed before client receipt.

### Research summarisation and analyst-facing GenAI

- Where the use case is internal-only and ingests public material, tier holds at tier-3 by default; Marketing Rule reach is the dominant re-tiering trigger.
- Reg AC research independence and MAR-adjacency apply where forward-looking content is generated; conduct factor scores at minimum medium.
- Books-and-records reach applies to AI-generated content that supports an analyst recommendation.
- Default tier: tier-3, elevating to tier-2 if any client-facing path opens or scope expands to non-public material.

### Sub-adviser-operated AI and fund-board reporting

- Where the model is operated by a sub-adviser on the registrant's funds, sub-adviser oversight under 38a-1(a)(4) applies.
- Fund-board reporting posture is a triggered gate; the fund's CCO is an audience.
- Default tier elevation: at least tier-2 when the model touches fund operations, fund-board materials, or fund-side recommendations.

### Reg BI care obligation

- For BDs, where the AI surfaces a recommendation to a retail customer, Reg BI's care obligation applies; the tier decision flags the care-analysis documentation as a triggered control gate.
- Default tier elevation: tier-1 or tier-2 depending on the directness of the AI's role in the recommendation.

## Cross-cutting tier modifiers

- **EU client base**: AIFMD / MiFID II overlay extends; the AI Act overlap factor flags Article 6 / Annex III routing to `ai-act-triage`.
- **Predictive-analytics rulemaking**: where the SEC proposal is in non-final state, the tier records the firm's monitoring posture rather than asserting compliance with a non-final rule. A re-tiering trigger fires on SEC final action.
- **Books-and-records reach**: any model whose output supports a recommendation or trading decision elevates the regulatory factor on books-and-records grounds; the tier records the firm's books-and-records system of record for AI-generated content (a frequent gap in GenAI use cases).

## Capital-markets-specific tier-elevation factors

In addition to the capability rubric:

- Market access AI (Rule 15c3-5 controls) → regulatory factor high.
- Marketing Rule reach (Rule 206(4)-1) → conduct factor at minimum medium; high if disclosures are not operationalised.
- Sub-adviser-operated AI on registrant's funds → fund-board reporting posture as a triggered gate; CCO audience.
- Reg BI care obligation (BDs) → conduct factor high when AI surfaces recommendations to retail customers.
- Books-and-records preservation gap on GenAI output → regulatory factor elevated; control gate triggered.

## Capital-markets-specific re-tiering triggers

Add to the re-tiering trigger block for capital-markets sector use cases:

- Output reaches a client-facing surface for the first time (research note published, client letter, marketing material, RFP response). Owner: research compliance with CCO. Detection: change-management notice and quarterly Marketing Rule reach review.
- Sub-adviser scope change (new sub-adviser added, AI capability extended). Owner: fund administration. Detection: 38a-1(a)(4) oversight cycle.
- SEC final action on the predictive-data-analytics rulemaking (where in scope). Owner: regulatory change function. Detection: regulatory horizon scan.
- Annual Rule 206(4)-7 review where scope or risk profile has materially changed. Owner: CCO. Detection: annual review calendar.
- New Annex III overlap surfaces (EU client base added, cross-border activity triggers MiFID II reach). Owner: regulatory change function. Detection: business expansion notice and regulatory horizon scan.

## Common pitfalls in capital-markets tiering

- Importing SR 11-7 vocabulary into an adviser/BD tier decision without confirming SR 11-7 reach; it does not directly apply to non-bank registrants.
- Omitting books-and-records reach for AI-generated client content; Rule 204-2 catches the firm at exam time and the tier should reflect that exposure now.
- Treating the SEC predictive-analytics proposal as binding when it is currently in non-final state; the tier records monitoring posture, not assumed compliance.
- Missing Marketing Rule reach on an AI tool that drafts investment-letter content or RFP responses; advisor-side AI is the high-frequency gap.
- Forgetting fund-board reporting posture for sub-adviser-operated AI on the registrant's funds; sub-adviser oversight under §38a-1(a)(4) is the gate that audits will probe.
- Treating execution-algo Rule 15c3-5 controls as engineering controls rather than tier-decision controls; market access controls are governance controls and the tier elevation has to reflect them.
