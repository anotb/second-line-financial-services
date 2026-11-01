# cross-cutting

One section per topic. Read only the sections the scope calls for.

## climate

### Climate cross-cutting overlay for kri-commentary

When the scope record flags `climate`, this overlay sets the climate-specific content for KRI-commentary blocks where the KRI is in the climate population.

Loaded by: `kri-commentary/SKILL.md` when `scope.cross_cutting_overlay_set` includes `climate`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- TCFD Recommendations (Final Report, June 2017; Implementing the Recommendations, October 2021), four pillars (Governance, Strategy, Risk Management, Metrics and Targets); Pillar 4 sets the metric-and-target frame for climate KRIs.
- ISSB IFRS S2 Climate-related Disclosures (June 2023), incorporating TCFD; for firms reporting under ISSB.
- BCBS, "Principles for the effective management and supervision of climate-related financial risks" (June 2022), supervisory expectations on climate-risk metrics for banks.
- ECB Guide on climate-related and environmental risks (November 2020) and ECB Guide on effective risk data aggregation and risk reporting (May 2024) for SSM-supervised banks; expectations on climate KRI data quality.
- NGFS climate scenarios (current vintage; Phase IV released October 2023, with periodic updates) for scenario-based KRI projections.
- SEC Climate Disclosure Rule (Release Nos. 33-11275, 34-99678, March 2024); current effectiveness unsettled given consolidated litigation in the Eighth Circuit and the SEC's stay. Climate KRIs feeding any disclosure under this rule require a current-effectiveness check at write time.
- BCBS 239 (January 2013), Principles 3 (accuracy and integrity) and 6 (adaptability); the load-bearing principles for climate KRI data quality given the heavy reliance on vendor and scenario data.

#### What changes for climate-flagged KRI commentary

##### 1. Data-confidence note required

Every climate KRI block carries a `data_confidence_note`. Climate KRIs typically rest on:

- Vendor-supplied emissions data (Scope 1, 2, 3) of variable quality.
- Vendor-supplied physical-risk hazard data of variable quality.
- Scenario-driven projections (NGFS or firm-specific) where the value rests on scenario assumptions, not realized data.
- Firm taxonomy and methodology decisions that materially affect the metric (financed-emissions denominator choice; physical-risk asset-level versus portfolio-level).

The note names the BCBS 239 Principle 3 / Principle 6 caveat where the firm's data lineage for the KRI is not at the same maturity as for credit, market, or operational KRIs.

##### 2. Realized versus projected distinction

Climate KRIs split into:

- Realized metrics (loss events from named physical events, transition-related write-downs in the period).
- Projected metrics (financed-emissions intensity, NGFS-scenario projected loss, transition-risk-weighted exposures).

The block names the type explicitly. Projected metrics carry the scenario name and the assumption set; realized metrics carry the event linkage and the loss-attribution discipline that any operational-risk KRI carries.

##### 3. SEC climate rule effectiveness check

For SEC registrants, climate KRIs that feed any disclosure under the SEC Climate Disclosure Rule (Release Nos. 33-11275, 34-99678) require a current-effectiveness check at write time. Default posture: cite the rule with `[verify current effectiveness]`, lean on TCFD or ISSB IFRS S2 for substantive content, and flag the SEC rule status in the source trace. Do not assert current effectiveness without verifying SEC posture.

##### 4. Voluntary versus mandatory disclosure linkage

Where the firm reports climate KRIs under voluntary frameworks (TCFD, CDP) and under any in-force mandatory frame (CSRD for EU operations; SEC rule subject to current-effectiveness; PRA SS3/19 for UK PRA-regulated banks), the block names the receiving disclosure framework. The same KRI may feed multiple disclosures with different precision and timing requirements; the source-trace discipline binds across all.

##### 5. Scenario-driven KRI commentary

For scenario-driven KRIs (NGFS or firm-specific scenarios), the block carries:

- The scenario name and vintage (e.g., "NGFS Net Zero 2050, Phase IV, October 2023").
- The model identifier and model owner (cross-link to the model-risk inventory).
- The scenario-assumption set that materially drives the metric (carbon-price trajectory, transition pathway).
- A `data_confidence_note` describing the scenario-dependent nature of the metric.

`contributing_factors` picks up `model-driver` where the metric movement is materially driven by scenario or methodology changes rather than underlying portfolio change.

#### Climate-specific output additions

- `climate_metric_type` (string): "realized" or "projected".
- `scenario_basis` (object, present when climate_metric_type = projected): `scenario_name`, `scenario_vintage`, `model_id`, `key_assumptions`.
- `disclosure_framework_linkage` (array): list of receiving frameworks (TCFD, ISSB IFRS S2, CSRD, SEC Climate Rule [with effectiveness flag], PRA SS3/19, voluntary CDP).
- `data_confidence_note` upgraded from optional to required.
- `risk_subtype` populated against the firm's climate taxonomy (physical-risk acute / chronic; transition-risk policy / technology / market / reputational).

#### Common pitfalls in climate-flagged KRI commentary

- Climate KRI block missing the `data_confidence_note`. Climate data lineage typically does not match the maturity of credit, market, or operational data; the caveat is the BCBS 239 Principle 3 / Principle 6 voice in the block.
- Realized and projected climate metrics conflated. The block names the type; conflation misleads the committee on whether a movement is portfolio-driven or assumption-driven.
- SEC Climate Rule cited with current-effectiveness asserted. The rule is subject to consolidated litigation and an SEC stay; current effectiveness must be verified at write time.
- Scenario-driven KRI commentary that reads as a forecast rather than a scenario projection. The scenario name and the assumption set are the binding context.
- Methodology change (e.g., change in financed-emissions denominator) attributed to "improved data" without naming the methodology shift. The contributing-factors enum includes `model-driver` for these cases; the data-confidence note carries the methodology change.

## cyber

### Cyber cross-cutting overlay for kri-commentary

When the scope record flags `cyber`, this overlay sets the cyber-specific content for KRI-commentary blocks where the KRI is in the cyber population.

Loaded by: `kri-commentary/SKILL.md` when `scope.cross_cutting_overlay_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- FFIEC IT Examination Handbook, Information Security and Cybersecurity sections, for KRI examples (security-awareness, patching cadence, MTTD / MTTR, vulnerability ageing, third-party cyber posture, identity and access exception KRIs).
- NIST Cybersecurity Framework 2.0 (February 2024), Govern function for KRI roll-up to board oversight; Identify, Protect, Detect, Respond, Recover for KRI taxonomy.
- NYDFS 23 NYCRR Part 500, especially §500.4(b) (CISO annual written report) and §500.17 (cybersecurity-event notification). Cyber-KRI commentary feeds the CISO report.
- SEC cyber disclosure rule (Release Nos. 33-11216, 34-97989, July 2023), Form 8-K Item 1.05 (material cybersecurity incident disclosure) and Regulation S-K Item 106 (cybersecurity risk management, strategy, governance). Sustained cyber-KRI deterioration is a leading indicator for the firm's disclosure-controls discipline.
- SEC Regulation S-P amendments (May 2024) for BDs, IAs, registered funds, transfer agents; customer-information-incident KRIs for in-scope entities.

#### What changes for cyber-flagged KRI commentary

##### 1. Disclosure-controls leading-indicator referral

For SEC registrants, sustained AMBER or RED on a cyber KRI for two or more consecutive periods triggers a disclosure-controls leading-indicator referral. The block:

- Cross-references `cyber-disclosure-readiness` Artifact C (DCP readiness map).
- Names the disclosure-process owner (typically the disclosure committee chair or general counsel).
- Carries the referral status (referred / under review / disposition documented).

The block does not make the disclosure call; it routes the leading-indicator signal to the process that owns it.

##### 2. NYDFS §500.17 notification flag

For NYDFS-licensed entities, a cyber KRI block whose movement is materially driven by a cybersecurity event that meets the §500.17(a) notification threshold carries an explicit notification-status flag (notified / not-yet-notified-within-72-hours / disposition documented). The block does not assess notification materiality; the CISO and counsel own that. The block flags the event-to-KRI linkage so the committee secretary and the auditor can trace it.

##### 3. CISO-report integration

For NYDFS-covered entities, the annual CISO report under §500.4(b) consumes the cyber KRI commentary set as the running record of program performance. The wrapper carries a "feeds CISO report" tag where applicable; the source-trace discipline binds the same way.

##### 4. KRI taxonomy aligned to NIST CSF 2.0 functions

Where the firm's cyber KRI taxonomy aligns to NIST CSF 2.0, the block's `risk_subtype` picks up the function (Identify / Protect / Detect / Respond / Recover / Govern). This makes cross-firm benchmarking and committee-pack roll-up more legible.

##### 5. AI-related cyber KRIs

For firms with material GenAI deployments, AI-cyber KRIs (prompt-injection attempt rate, AI-output safety-evaluation failure rate, AI-supply-chain incident rate) are increasingly common. The block's `contributing_factors` picks up `model-driver` where the metric movement is materially driven by AI-system behavior. Cross-reference `ai-governance-model-risk` for the deeper material.

##### 6. Vendor / third-party cyber KRIs

Vendor cyber posture KRIs (top-N vendor attestation status, vendor-incident rate, vendor SLA compliance for incident notification) belong here when the scope flags both `cyber` and `third-party-operational-resilience`. The block carries the vendor-side root cause where the metric movement is vendor-driven; `contributing_factors` picks up `vendor`.

#### Cyber-specific output additions

- `disclosure_controls_referral` (object): present when sustained AMBER or RED triggers the leading-indicator referral; carries `referral_status`, `disclosure_process_owner_role`, `cross_reference`.
- `nydfs_500_17_notification_flag` (string or null): present where the metric movement is materially driven by an event that may meet the notification threshold.
- `feeds_ciso_report` (boolean): set true where the wrapper feeds the annual CISO report under §500.4(b).
- `risk_subtype` aligned to NIST CSF 2.0 function names where the firm taxonomy supports it.

#### Common pitfalls in cyber-flagged KRI commentary

- Sustained AMBER or RED cyber KRI without the disclosure-controls referral. SEC registrants need the leading-indicator signal to flow to the disclosure process.
- Cyber KRI block treating the metric movement and the underlying event as the same thing. The metric is the symptom; the event (or the test-design change) is the cause; the block separates them.
- NYDFS §500.17 notification-relevant events surfaced only in the material-events log and not in the cyber KRI block that captures the metric impact. The cross-link runs both ways.
- AI-cyber KRIs buried in the model-risk section with no cyber-overlay treatment. For firms with material AI deployments, the cyber block names the AI threat surface explicitly.
