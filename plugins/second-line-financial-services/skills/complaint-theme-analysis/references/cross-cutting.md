# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay for complaint-theme-analysis

This overlay is mandatory on this skill. Complaints are the canonical conduct-risk surveillance signal in US consumer financial services; theme analysis is what the conduct function does with that signal at population scale. Every theme analysis carries a conduct-risk implications block per theme. The overlay names what changes when the scope record flags `conduct` (which it does by default for this skill).

Loaded by: `complaint-theme-analysis/SKILL.md` whenever invoked. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### What changes for conduct-flagged theme analysis

##### 1. Themes are the surveillance signal, not the alert

In conduct framework vocabulary, individual complaints are alerts; themes are the population-scale signal. The conduct function consumes the signal, not the alert; the alert handling is the case-management workflow. The seam matters because the conduct committee's reading window is on the theme movement, not on the count of any single complaint. A theme that holds at 3 percent of period complaints across four periods is a chronic conduct concern; a theme that spikes from 1 percent to 8 percent in one period is an acute conduct concern. The memo is explicit about which posture each top theme is in.

##### 2. Per-theme conduct-risk taxonomy tie-back

Per theme, the memo records the conduct-risk taxonomy categories the theme touches. Common categories:

- *Incentives* — sales, LO, CSR, or marketing-team compensation design that drives the conduct under the theme.
- *Product design* — fee architecture, disclosure design, default-state design, choice-architecture design, friction design.
- *Communication* — marketing copy, in-product messaging, AI-generated communication, dynamic disclosure, complaint-handling script content.
- *Sales practices* — branch and digital sales conduct, retention-offer conduct, account-opening conduct, cross-sell mechanics.
- *Customer outcome* — outcome disparity across policy-relevant segments (rural, low-balance, digital-only, English-as-second-language, recent-immigrant cohorts, age-related cohorts).
- *Complaint linkage* — whether the underlying signal already surfaced in a prior period and what was done with it. A theme that the prior period flagged at watch-list grade and that has now grown is a process failure, not just a substantive failure.
- *Vendor or third-party* — where a theme traces to a service provider, sponsor-bank arrangement, or fintech partner.
- *AI / algorithmic surface* — where a theme traces to algorithmic decisioning, AI agents, AI-generated communication, or dynamic disclosure.

The memo lists each category that the theme touches; the conduct committee reads against the taxonomy.

##### 3. Customer-outcome lens supplements the protected-class lens

For themes with a `fair_lending_flag`, the customer-outcome lens extends the analysis beyond the protected-class lens. Customer-outcome disparity across policy-relevant segments is a conduct concern even where the protected-class disparity tests pass, and even where the protected-class disparity tests have not yet been run. The memo records:

- Whether policy-relevant segments are affected by the theme, in addition to or instead of protected-class segments.
- Whether the theme raises a parallel ECOA / FHA theory (cross-reference `fair-lending-test-plan` for finding-grade analysis).
- Whether the BISG and geographic enrichment is signal-grade or watch-list-grade evidence in this period.

The fair-lending finding is not the theme analysis's job. The theme analysis surfaces the signal; the fair-lending workstream confirms or rejects.

##### 4. Named conduct-accountable manager per theme

For each top theme, the memo names the conduct-accountable manager role under the firm's conduct framework. For UK-licensed firms in SMCR scope, this is the senior manager with the prescribed responsibility for the relevant business; for non-UK firms, the firm's conduct framework names a manager (often the head of the relevant business or the head of consumer / customer). The name is a role, not an individual.

The role named on the theme is distinct from the decision forum that acts on the recommended actions. The conduct committee reads the theme; the consumer compliance committee or the product committee acts on the action; the conduct-accountable manager is the role with named accountability for the underlying conduct outcome.

##### 5. Conduct-event taxonomy classification recommendation

Where the firm operates a conduct-event taxonomy, the memo names whether each top theme is a conduct-event candidate. The classification is not the memo's job to finalise; the conduct-risk function classifies. The memo carries the recommendation per theme.

A theme is typically a conduct-event candidate when the severity is `high` or `critical`, the population is meaningful, the conduct-risk taxonomy tie-back is non-trivial, and the conduct-accountable manager role is named. A theme rated `medium` or `low` is typically not a conduct-event candidate but may surface as a watch-list item.

##### 6. Complaint-monitoring loop closure per theme

The memo names the downstream complaint-monitoring posture per theme:

- Which complaint codes the firm will watch for re-emergence after the recommended actions execute.
- The cadence of the read (weekly, monthly, quarterly).
- The escalation trigger if the theme persists or recurs.
- The threshold for off-cycle re-review.

Theme analysis without loop closure is incomplete; the conduct function is responsible for tracking whether the theme stays remediated, and the loop closure is the operational instruction the conduct function consumes.

##### 7. Regulatory-engagement intersection

Where a theme is responding to a regulatory-engagement event (CFPB inquiry on a specific theme; OCC Matter Requiring Attention on complaint management; FDIC corrective action; state AG inquiry; FCA Section 166 review for UK-licensed entities), the conduct overlay records:

- The event that triggered the inclusion of the theme.
- The regulator-engagement counsel posture (privilege, work-product, response-file management).
- Whether the conduct committee receives a read alongside the consumer compliance committee.
- Whether the firm's conduct-event reporting to the regulator is implicated.

##### 8. Customer-outcome dark-pattern themes

Conduct-flagged theme analysis specifically watches for dark-pattern themes: friction-design themes (cancellation difficulty, complaint-channel friction, fee-dispute friction); choice-architecture themes (default opt-in; pre-checked consents; misleading default-state); urgency-and-scarcity themes (false urgency in retention offers; fabricated scarcity in promotional fees); confirm-shaming themes (cancellation paths designed to discourage). Where complaints surface dark-pattern themes, the conduct overlay loads the dark-pattern frame in addition to the substantive theme; the memo records both.

The CFPB has discussed dark patterns in supervisory highlights and in policy framing; the FTC's September 2022 dark-patterns report is the cross-agency anchor. The memo cites both where dark-pattern themes are in the population.

#### Conduct-specific memo template additions

Per top theme:

- `conduct_risk_taxonomy_tie_back[]` — list of conduct-risk taxonomy categories the theme touches.
- `conduct_accountable_manager_role` — named role under SMCR or the firm's conduct framework.
- `conduct_committee_read` — boolean.
- `conduct_event_candidate` — boolean (recommendation only; conduct-risk function classifies).
- `customer_outcome_segments_affected[]` — policy-relevant segments where the theme has disparate impact.
- `regulator_engagement_trigger` — string; named regulator-engagement event if any.
- `complaint_monitoring_loop_closure` — string; post-action monitoring posture, cadence, and escalation trigger.
- `dark_pattern_frame[]` — friction-design / choice-architecture / urgency-scarcity / confirm-shaming / other; populated where the theme matches a dark-pattern frame.

#### Common pitfalls in conduct-flagged theme analysis

- Treating themes as a noise source rather than as the canonical conduct signal; complaint-rate and complaint-code drift are signal, not noise.
- Conflating individual complaint handling (the alert) with theme analysis (the signal); the conduct committee reads the signal, not the alert population.
- Missing the named conduct-accountable manager per theme; the conduct framework names a role separate from the product owner and separate from the CCO.
- Recommending actions without naming the complaint-monitoring loop-closure posture; remediation that does not close the loop is incomplete and re-emerges.
- Treating BISG signal as evidence of disparate impact; BISG is signal, not proof, and the conduct overlay is explicit about the signal-vs-finding distinction.
- Watching the same complaint code for too short a window after remediation; conduct concerns recur on a quarterly or annual cadence even after a successful action.
- Reading the customer-outcome lens as a relabelling of the protected-class lens; the two are different framings and the legal regimes differ.
- Missing dark-pattern themes because the firm's complaint taxonomy does not have a dark-pattern code; the memo applies the dark-pattern frame across substantive themes where the journey design is the issue.
