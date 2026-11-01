# cross-cutting

One section per topic. Read only the sections the scope calls for.

## climate

### Climate cross-cutting overlay for risk-committee-pack

When the scope record flags `climate` for the committee pack, this overlay sets the climate-risk content for named pack sections. Climate is in scope for the committee pack when the firm reports under the SEC Climate Disclosure Rule (where current effectiveness applies), under EU CSRD as a non-US group company or US subsidiary of an EU-headquartered group, under voluntary TCFD-aligned disclosure, or where the firm's risk taxonomy includes climate as an enterprise risk type.

Loaded by: `risk-committee-pack/SKILL.md` when `scope.cross_cutting_set` includes `climate`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- SEC Climate Disclosure Rule (Release Nos. 33-11275, 34-99678, final March 6, 2024), Items 1500-1507 of Regulation S-K and Article 14 of Regulation S-X. Verify current effectiveness at pack-write time; the rule has been subject to legal challenges and SEC stay actions, with consolidated litigation in the Eighth Circuit.
- TCFD: "Recommendations of the Task Force on Climate-related Financial Disclosures" (Final Report, June 2017) and "Implementing the Recommendations of the Task Force on Climate-related Financial Disclosures" (October 2021). Pillars: Governance, Strategy, Risk Management, Metrics and Targets. The FSB disbanded the TCFD in October 2023; the recommendations remain the working frame and underpin ISSB IFRS S2.
- IFRS S2 Climate-related Disclosures (June 2023) for firms reporting under ISSB-aligned regimes.
- NGFS Climate Scenarios (current vintage): used by US, UK, EU, and other supervisors for climate scenario analysis. Reference scenarios include Net Zero 2050, Below 2 Degrees, Delayed Transition, Current Policies, Fragmented World.
- FSB SCEAS (Supervisory and Climate-related Exercises and Analytical Studies, 2022) for the supervisory landscape.
- Federal Reserve Pilot Climate Scenario Analysis (2023-2024) for the six largest US BHCs as a supervisory reference.
- Sector-specific climate frames where applicable: NAIC Climate Risk Disclosure Survey (TCFD-aligned, mandatory in 15 US states for in-scope insurers); NYDFS Industry Letter on Climate-Related Financial Risks for state-regulated insurers and banks; PRA SS3/19 (Enhancing banks' and insurers' approaches to managing the financial risks from climate change) for UK-regulated entities.

#### What changes for climate-flagged committee packs

##### 1. Heat-map placement and rationale

Climate is reported either as a standalone heat-map cell or mapped under strategic with documented rationale. The choice depends on the firm's risk taxonomy and reporting regime:

- **Standalone cell**: typical for firms reporting under the SEC climate rule (where current effectiveness applies), under EU CSRD parent-group consolidation, or where the firm has elected a top-of-house climate-risk view. The cell carries current rating, prior rating, direction, and a commentary that distinguishes physical risk and transition risk.
- **Mapped under strategic**: typical for firms in the early stages of climate-risk integration, for firms with limited material exposure (after assessment), or for firms where the materiality posture is documented under the firm's enterprise risk framework. The strategic-cell commentary names the climate component explicitly.

The choice is documented in the heat-map commentary; the climate cross-cutting overlay rejects floating-appendix climate treatment that sits outside the risk taxonomy.

##### 2. Climate-section content

For climate-flagged packs, the dedicated climate section carries:

- **Governance subsection**: board-committee oversight of climate-related risk; management responsibility (typically the CRO with the chief sustainability officer or equivalent as accountable executive); committee cadence on climate items; integration with the firm's risk-governance framework. Maps to TCFD Governance pillar; for SEC-rule-in-scope firms, supports Item 1501 of Regulation S-K.
- **Strategy subsection**: identification of climate-related risks (physical risk: acute and chronic; transition risk: policy, technology, market, reputation) and opportunities relevant to the firm's businesses, strategy, and financial planning over the short, medium, and long term. Resilience of the firm's strategy under different climate scenarios. Maps to TCFD Strategy pillar.
- **Risk management subsection**: how climate-related risk is identified, assessed, prioritized, and managed; integration into the enterprise risk-management framework. Material risk events in the period that have a climate component (severe weather impact on operations or counterparties; transition-policy event affecting a material exposure). Maps to TCFD Risk Management pillar.
- **Metrics and targets subsection**: climate-related metrics used to assess and manage risk (financed emissions for banks and asset managers; underwriting-portfolio emissions for insurers; physical-risk exposure metrics; transition-risk exposure by sector). Climate-related targets and progress against them. For SEC-rule-in-scope firms, Scope 1 and Scope 2 emissions disclosure status; financial-statement-level climate disclosure status under Article 14 of Regulation S-X.

##### 3. Scenario analysis

Scenario analysis is a recurring committee item for firms with material climate exposure. The pack carries:

- Scenario inventory used in the period (NGFS Net Zero 2050, NGFS Delayed Transition, NGFS Below 2 Degrees, FRB pilot scenarios for in-scope BHCs, IAIS scenarios for insurers, internal scenarios calibrated for firm-specific exposures).
- Result summary per scenario with breach flags against capital, liquidity, risk-appetite, and earnings metrics.
- Limitations and assumptions used; the data confidence label for climate-scenario data is typically lower than for financial data (third-party-supplied scenarios, modeled exposures, limited internal validation history).
- Forward plan for the next scenario cycle.

##### 4. Materiality posture and disclosure linkage

The climate section names the firm's current disclosure posture:

- **SEC rule** (where current effectiveness applies): in scope for which Item 1500-series disclosures based on filer category; phase-in timetable; readiness status. The pack carries a `[verify current effectiveness]` flag where the litigation status is unresolved.
- **EU CSRD**: parent-group consolidation status for non-EU groups; ESRS E1 (climate change) standard applicability; double-materiality assessment status.
- **Voluntary TCFD-aligned**: the firm reports under TCFD as the working frame. The pack identifies the firm's reporting venue (10-K, 20-F, sustainability report, integrated report).
- **State or sector-specific**: NAIC Climate Risk Disclosure Survey for in-scope insurers (mandatory in 15 US states); NYDFS Industry Letter for NY-regulated banks and insurers; California Climate Corporate Data Accountability Act (SB 253) and Climate-Related Financial Risk Act (SB 261) for in-scope entities (verify effective status given litigation history).

##### 5. Forward-looking commentary

The climate component of forward-looking commentary in the pack covers:

- Regulatory horizon: SEC rule status update with `[verify current effectiveness]` discipline; EU CSRD wave-2 / wave-3 timing for in-scope subsidiaries; California climate-disclosure laws status; ISSB IFRS S2 adoption status by jurisdictions where the firm operates; sector-specific supervisory exercises (FRB pilot follow-up, EIOPA insurance climate stress, BoE / PRA climate work).
- Internal milestones: financed-emissions methodology refresh; transition-plan publication; net-zero-target review; physical-risk model upgrade; data-quality work under the BCBS 239 frame extended to climate data.

#### Climate-specific output template additions

Added to the pack (mapped to schema where present):

- `climate_section.governance_summary` — string, governance posture brief.
- `climate_section.physical_risk_summary` — string, physical-risk exposure brief.
- `climate_section.transition_risk_summary` — string, transition-risk exposure brief.
- `climate_section.scenarios_used` — array of strings, scenario inventory.
- `climate_section.materiality_posture` — enum (sec-rule-in-scope / csrd-in-scope / voluntary-tcfd / state-specific / multiple).
- `climate_section.linked_disclosure_section` — string or null, pointer to the firm's external disclosure (10-K Item, 20-F section, sustainability report).
- `climate_section.disclosure_verification_flag` — boolean, true when the SEC rule current effectiveness or other regime status is unresolved at pack-write time.
- `heat_map[].commentary` — climate-cell commentary (or strategic-cell climate component) names physical and transition risk by type and quantifies exposure where available.
- `forward_looking.regulatory_horizon[]` — climate-tagged items with the verification-flag discipline.

#### Common pitfalls in climate-flagged committee packs

- Asserting current effectiveness of the SEC climate rule without checking the litigation and stay status at pack-write time. The default posture is to cite the rule with a `[verify current effectiveness]` flag and lean on TCFD or sector-specific frames for substantive content.
- Treating climate as a standalone appendix that sits outside the risk taxonomy. The committee owns the risk-taxonomy decision; climate is a heat-map cell or mapped under strategic with documented rationale.
- Reporting financed emissions or underwriting-portfolio emissions without the methodology and the data confidence label. Climate data is typically third-party-supplied, modeled, and partially validated; the pack carries that posture.
- Scenario analysis reported as a result summary without the assumption set, the limitations, and the validation status of the scenario data. Examiners and auditors probe both.
- Conflating the climate transition plan with the firm's risk-management posture. The transition plan is a forward-looking commitment; the risk-management posture is the current control surface. The pack carries both, distinctly.
- Treating EU CSRD as out of scope for US-headquartered firms without checking subsidiary consolidation. Many US firms have material EU subsidiaries that pull the parent into wave-2 or wave-3 reporting under ESRS.
- Using the firm's prior-vintage NGFS scenarios after a vintage refresh has been published. Scenario vintages have different policy assumptions; the pack flags the vintage in use.
- Omitting the data confidence appendix entry for climate data. BCBS 239 known-limitations posture extends to climate data; the pack records the limitations.

## conduct

### Conduct cross-cutting overlay for risk-committee-pack

When the scope record flags `conduct` for the committee pack, this overlay sets the conduct-risk content for named pack sections. Conduct risk in second-line vocabulary is the customer-outcome and market-integrity lens, the named-manager accountability lens, and the regulatory-engagement lens; it is not the same as compliance risk and not the same as fairness as a model property. The committee pack carries the enterprise conduct-risk slice; deeper material on individual conduct events, fair-lending findings, suitability matters, and SMCR responsibility maps lives in the relevant capability or sector skills.

Loaded by: `risk-committee-pack/SKILL.md` when `scope.cross_cutting_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- FCA Senior Managers and Certification Regime (SMCR) for UK-licensed entities, including the Senior Manager Conduct Rules and the prescribed-responsibilities map. For PRA-designated firms, the joint FCA / PRA SMCR applies.
- FCA Consumer Duty (Principle 12 and PRIN 2A, in force July 31, 2023 for new and existing products; July 31, 2024 for closed products) for in-scope FCA-regulated entities.
- US conduct-risk drivers: CFPB UDAAP authority under Dodd-Frank §1031 / §1036; ECOA / Reg B and the CFPB Circulars on AI in adverse-action notices; SEC Reg BI and the IA fiduciary duty; FINRA Rule 2010 (standards of commercial honor) and FINRA Rule 3110 (supervision); state UDAP statutes; NAIC Model #880 (Unfair Trade Practices Act).
- Conduct risk taxonomy as commonly framed by second-line conduct functions: customer outcomes, market integrity, employee conduct, regulatory engagement, financial-crime adjacency. Firm-specific taxonomy lives in `references/firm-overlay.md` when present.
- Product-governance frames: FCA PROD for in-scope UK firms; NAIC Suitability in Annuity Transactions Model Regulation (#275, with 2020 best-interest amendment) for annuity sales; FINRA Rule 2111 (suitability) and Reg BI for BD recommendations.

#### What changes for conduct-flagged committee packs

##### 1. Heat-map placement and rating drivers

Conduct is reported either as a standalone heat-map cell or mapped under operational with documented rationale. The choice depends on the firm's risk taxonomy:

- **Standalone cell**: typical for FCA-regulated firms where conduct is a primary regulator focus, for firms with material consumer-facing activity, and for firms where the conduct framework is mature enough to support a dedicated rating.
- **Mapped under operational or compliance**: typical for firms in early-stage conduct integration or firms with limited consumer-facing activity. The cell commentary names the conduct component explicitly.

Cell-rating drivers the committee should see:

- Customer-outcome metrics (complaint rate and complaint themes, complaint-resolution timeliness, root-cause findings on customer harm).
- Conduct-related events in the period (UDAAP exam findings, fair-lending findings, suitability matters, sales-practice issues, market-conduct findings).
- SMCR / accountability-framework status for in-scope firms (any prescribed-responsibility transition, any conduct-rule referral, any senior-manager certification issue).
- Regulatory-engagement events (CFPB inquiry, FCA Section 166 review, NAIC market-conduct exam finding, state DOI inquiry, SEC enforcement engagement on a conduct-flavored matter).

##### 2. Customer-outcome view

The conduct section's customer-outcome content carries:

- Complaint-volume trend and complaint-theme analysis for the period; the firm's complaint-handling timeliness against internal SLA and regulatory expectations (Reg E §1005.11 timing, FCA DISP timing, state-specific timing).
- Customer-outcome disparity metrics where the firm tracks them: not only protected-class disparity (which sits in fair-lending reporting) but also policy-relevant-segment outcome disparity (rural, low-balance, digital-only, English-as-second-language cohorts where lawful to consider). The pack vocabulary distinguishes the two lenses.
- Material customer-harm events in the period; remediation status; restitution posture.
- Complaint-driven product or process changes implemented or contemplated in the period.

##### 3. Market integrity and conduct events

For firms with material trading, sales, or market-facing activity, the pack carries:

- Surveillance-program output summary (insider-trading, market-manipulation, front-running, layering / spoofing, off-channel-communications) and any material alerts or matters in the period.
- Conduct-related disciplinary actions on employees in the period (without naming individuals); aggregate counts by category and by business unit.
- Whistleblower-line activity summary (volume, themes, material matters); whistleblower-program status posture.

##### 4. SMCR and accountability-framework content for in-scope firms

For UK-licensed firms in SMCR scope, the pack carries:

- Prescribed-responsibilities map status; any change in the period; any prescribed-responsibility currently uncovered or in transition.
- Conduct-rule referrals in the period; SMR-individual conduct matters; certification-regime issues including any failed certifications.
- Section 166 review status (if any active); FCA / PRA supervisory-engagement status.

For non-SMCR firms with an internal accountability framework, the parallel content references the firm's named-accountability map and any framework changes in the period.

##### 5. Regulatory-engagement view

The conduct section's regulatory-engagement content covers:

- Open inquiries from regulators with a conduct flavor (CFPB, FCA, FINRA, SEC enforcement, NAIC market-conduct, state DOI).
- Public enforcement actions against the firm in the period, with the action type, the regulator, the issue summary, and the firm's response posture.
- Industry-wide enforcement themes the firm is monitoring (e.g., off-channel-communications enforcement, AI-in-adverse-action enforcement, dark-pattern enforcement); the firm's posture against each.

##### 6. Forward-looking commentary

The conduct component of forward-looking commentary covers:

- Regulatory horizon: FCA Consumer Duty implementation milestones for UK firms; CFPB rulemaking in active stages with conduct implications; SEC and FINRA conduct-related rulemaking; NAIC model-law amendments with conduct implications; state-level UDAP and AI-disclosure activity.
- Firm-level milestones: conduct-framework refresh; complaint-program redesign; surveillance-program upgrade; SMCR responsibility-map change; product-governance review.

##### 7. Cross-link to other capability skills and to sector skills

- KRI commentary for individual RAG-breached conduct KRIs (complaint rate, complaint-resolution timeliness, surveillance-alert backlog): `kri-commentary`.
- Open-issue write-ups for conduct findings: `issue-writeup`.
- Fair-lending capability skills (fair-lending-test-plan, adverse-action-review): `consumer-compliance-fair-lending/`.
- UDAAP review: `udaap-risk-review` (where present).
- Insurance market-conduct content: `insurance-risk-compliance/` overlays.

#### Conduct-specific output template additions

Added to the pack (mapped to schema where present):

- `conduct_section.complaint_summary` — object with volume, theme analysis, timeliness, and material customer-harm events.
- `conduct_section.market_integrity_summary` — object with surveillance-program output, conduct-related disciplinary actions (aggregate counts), and whistleblower-line activity.
- `conduct_section.smcr_status` — object for UK-licensed firms with prescribed-responsibilities map status, conduct-rule referrals, and Section 166 status.
- `conduct_section.regulatory_engagement` — object with open inquiries, public enforcement actions, and industry-theme posture.
- `heat_map[]` — conduct-cell commentary names the cell-rating drivers explicitly; customer-outcome lens distinguished from protected-class lens.
- `forward_looking.regulatory_horizon[]` — conduct-tagged items (Consumer Duty, CFPB rulemaking, FINRA rulemaking, NAIC amendments, state-level activity).

#### Common pitfalls in conduct-flagged committee packs

- Conflating conduct risk with compliance risk. Compliance risk is the rule-following surface; conduct risk is the customer-outcome and market-integrity lens. The two overlap; they are not the same. The pack carries each distinctly.
- Reporting customer-outcome metrics only as protected-class disparity. Protected-class disparity is the fair-lending lens; policy-relevant-segment outcome disparity is the conduct lens. Both belong, distinctly framed.
- Treating SMCR as a UK-only compliance overhead. For UK-licensed firms (including US-headquartered groups with UK subsidiaries), SMCR drives committee-relevant accountability content; the committee owns the framework, not the compliance team.
- Surveillance and market-integrity content reported as a counter (alerts opened, alerts closed) rather than as a substantive brief. The committee's question is whether the surveillance program is fit for purpose; the brief addresses that.
- Conduct-related disciplinary actions reported with individual names. The pack carries aggregate counts; individual-employee detail belongs in HR / Legal channels, not in committee material.
- Whistleblower-line activity summarized only as volume. Themes and material-matter status are the committee-relevant content.
- Industry-theme regulatory-engagement content reported as a generic warning (e.g., "off-channel-communications enforcement is a focus"). The committee-level brief names the firm's posture against each theme.
- Consumer Duty implementation status (for UK firms) reported only at first-line level. The committee owns the foreseeable-harm and customer-outcome assessment; the pack carries that ownership.

## cyber

### Cyber cross-cutting overlay for risk-committee-pack

When the scope record flags `cyber` for the committee pack, this overlay sets the cyber-risk content for named pack sections. The committee pack carries the enterprise-level cyber slice; deeper material on disclosure decisions, 8-K Item 1.05 trigger analysis, and CISO-program reporting lives elsewhere.

Loaded by: `risk-committee-pack/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NYDFS 23 NYCRR Part 500, especially §500.4(b) (CISO annual written report to senior governing body) and §500.4(d) (board oversight including approval of cybersecurity policy). Current text reflects Second Amendment (effective November 1, 2023) with phased compliance dates.
- SEC cyber disclosure rules: Regulation S-K Item 106 (cybersecurity risk management, strategy, and governance) for public-company issuers; Form 8-K Item 1.05 (material cybersecurity incident disclosure). Final rule July 2023; compliance dates phased.
- SEC Regulation S-P amendments (May 2024) for BDs, IAs, registered funds, and transfer agents: customer-information-safeguarding and breach-notice elements; 30-day customer notice. Verify current compliance dates by entity type and size at pack-write time.
- FFIEC IT Examination Handbook, Information Security and Cybersecurity sections, and the FFIEC Cybersecurity Assessment Tool (CAT; verify whether the FFIEC has formally retired or refreshed CAT at pack-write time).
- NIST Cybersecurity Framework 2.0 (February 2024) for governance and risk-management framing; NIST AI 600-1 (Generative AI Profile, July 2024) for AI-cyber considerations.
- NAIC Insurance Data Security Model Law (Model #668) for state-licensed insurers; adoption status state-by-state.
- Sector-specific overlays where applicable: PCI DSS for card-handling entities; HIPAA Security Rule for health-information-handling entities.

#### What changes for cyber-flagged committee packs

##### 1. Heat-map placement and rating drivers

Cyber is a standalone heat-map cell in the enterprise pack. Cell rating drivers the committee should see:

- Material cybersecurity events in the period (incident severity, customer or operational impact, regulatory-notification status, public-disclosure status).
- Threat-environment posture (targeted-threat actor activity against the firm's sector, geography, technology stack).
- Control-program maturity status (FFIEC IT-Handbook-aligned or NIST CSF-aligned, with the firm's current self-assessment or independent-assessment rating).
- Third-party / vendor cyber exposure (the cyber surface includes the firm's critical vendors; this is a recurring committee topic and a cell-rating driver).
- Open cyber MRA / MRIA-equivalent supervisory items (NYDFS Part 500 examination findings; OCC, FRB, FDIC IT-exam findings; SEC and FINRA cyber-exam findings).

Cyber rating "stable" while material events occurred in the period is an inconsistency the chair will pull on; the cell-rating commentary explains.

##### 2. CISO report integration

For NYDFS-covered entities, §500.4(b) requires the CISO to report at least annually in writing to the senior governing body on the cybersecurity program. The committee pack's cyber section typically:

- References the most recent CISO report and any items requiring committee attention or decision.
- Names the standing CISO update cadence (annual at minimum; many firms run quarterly briefings to the risk committee or to a committee subgroup).
- Carries a brief on the CISO function's independence and resourcing posture; structural changes belong here.

For non-NYDFS-covered entities, the parallel content references the firm's CISO reporting cadence under the firm's information-security policy and the relevant regulator's expectations (e.g., FFIEC for banks, SEC for advisers and BDs under Regulation S-P).

##### 3. Material cybersecurity events

The pack's material risk events section carries cyber events meeting the firm's materiality threshold for committee reporting (typically lower than the SEC 8-K Item 1.05 materiality standard). Each event:

- Date, event type (intrusion, data exposure, ransomware, business-email-compromise, vendor-driven event), affected systems and data, customer impact.
- Initial assessment of materiality; current assessment; any change.
- Regulatory-notification status (NYDFS Part 500 §500.17 72-hour notice; HHS Breach Notification Rule for HIPAA-covered entities; state breach-notification laws; sector-regulator notifications including SEC Reg S-P 30-day customer notice for in-scope entities).
- Public-disclosure status (SEC 8-K Item 1.05 for public-company issuers; firm's public communications posture).
- Remediation status; post-incident review status; any committee decisions taken or requested.

The pack does not make the disclosure decision; the disclosure committee or equivalent process owns that. The pack flags the event and the disclosure-process referral.

##### 4. Cyber-related regulatory horizon

The forward-looking commentary's cyber component covers:

- NYDFS Part 500 amendment effective dates (Second Amendment phased compliance dates carry through 2025; verify current state at pack-write time).
- SEC Regulation S-P compliance phase-in for in-scope entities.
- Sector-specific frames where applicable (NAIC #668 state adoption changes; HIPAA Security Rule potential rulemaking).
- Threat-environment forward view (sector-specific intelligence, regulator-issued advisories).

##### 5. Vendor and third-party cyber roll-up

Cyber risk on the firm's surface includes the vendor surface. The pack carries:

- Critical-vendor cyber posture summary (top-N vendors by criticality with current cyber-attestation status, recent incident or breach status, contract terms on incident notification and cooperation).
- Concentration on shared infrastructure (hyperscaler concentration, shared SaaS providers, shared identity / authentication providers); a vendor-side incident affects multiple firm activities, and the committee owns the concentration view.
- Vendor-driven cyber events in the period.

Cross-link to `concentration-risk-review` for the deeper vendor-concentration view.

##### 6. AI-related cyber considerations

For firms with material AI use cases, the cyber section adds:

- AI-related threat surface (prompt-injection threat surface for GenAI deployments; model-supply-chain attack surface; AI-enabled social-engineering and deepfake threats).
- AI-related cyber events in the period.
- Cross-link to NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024) for NY-licensed entities.

Detail of the AI cyber posture for individual use cases lives in the model-card cyber overlays (`model-card-builder/references/cross-cutting.md#cyber`); the committee pack carries the enterprise rollup.

##### 7. Cross-link to other capability skills

- Cyber-disclosure decision and 8-K Item 1.05 trigger analysis: `cyber-disclosure-readiness`.
- Vendor-concentration view: `concentration-risk-review`.
- AI-specific committee pack: `board-ai-risk-pack`.
- KRI commentary for cyber KRIs (phishing-click rate, patching cadence, MTTR breaches): `kri-commentary`.

#### Cyber-specific output template additions

Added to the pack (mapped to schema where present):

- `cyber_section.ciso_report_reference` — string, reference to the most recent CISO written report and any items requiring committee attention.
- `cyber_section.material_events_summary` — array, cyber-tagged entries from `material_events[]` with the disclosure-process referral status.
- `cyber_section.regulatory_notifications` — array of regulatory notifications made in the period (NYDFS §500.17, state breach-notification, SEC Reg S-P customer notice, HIPAA Breach Notification, sector-regulator notifications).
- `cyber_section.public_disclosure_referrals` — array of events referred to the disclosure committee for 8-K Item 1.05 or other public-disclosure consideration.
- `cyber_section.vendor_cyber_summary` — object with critical-vendor posture summary and shared-infrastructure concentration.
- `cyber_section.ai_cyber_considerations` — object for firms with material AI use cases, with cross-link to the AI committee pack.
- `heat_map[]` — cyber-cell commentary names the cell-rating drivers explicitly.
- `forward_looking.regulatory_horizon[]` — cyber-tagged items (NYDFS Part 500 phased dates, SEC Reg S-P compliance, NAIC #668 adoption changes).

#### Common pitfalls in cyber-flagged committee packs

- Carrying the CISO report verbatim into the committee pack. The pack is committee-audience material; the CISO report is the source. The pack references the report and surfaces what requires committee attention.
- Reporting cyber events without the regulatory-notification posture and the public-disclosure-referral status. Examiners and counsel both read for these by name.
- Treating cyber materiality for the committee as the same as 8-K Item 1.05 materiality. The committee threshold is typically lower; events that do not meet the 8-K threshold can still warrant committee attention.
- Cyber rating "stable" or "improving" while material events occurred in the period without cell-rating commentary that explains the apparent inconsistency. The chair will pull on this.
- Vendor cyber treated as the vendor-management committee's problem. The committee owns the enterprise risk view; vendor cyber is a heat-map driver.
- AI-related cyber considerations buried in the model-risk section. For firms with material AI use cases, the cyber section names the AI threat surface explicitly.
- Including a multi-page CISO-report extract in the pack body. The audience is the committee; the source is the CISO report; the pack carries the brief and the linkage.
- Omitting the disclosure-process referral status when an event was reviewed by the disclosure committee. The committee's question is whether the disclosure-process gate was respected, not what the disclosure decision was.
