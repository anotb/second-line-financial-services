# cross-cutting

One section per topic. Read only the sections the scope calls for.

## climate

### Climate cross-cutting overlay for cyber-disclosure-readiness

The disclosure machinery for cyber and for climate overlaps materially: the same DCP under Rule 13a-15, the same disclosure committee, the same materiality lens, and the same 8-K mechanic handle both. This overlay sets what changes when the scope flags climate alongside (or instead of) a cyber incident — that is, when a climate-related material event is the trigger, or when the 10-K's climate disclosure is up for refresh in the same cycle as the Item 106 cyber disclosure.

Loaded by: `cyber-disclosure-readiness/SKILL.md` when `scope.cross_cutting_set` includes `climate`. Climate is required as a cross-cutting overlay for this skill because the disclosure machinery overlaps; the depth lives here so SKILL.md does not re-anchor full climate sources.

#### Source basis

- SEC Climate Disclosure Rule, Release Nos. 33-11275 / 34-99678, "The Enhancement and Standardization of Climate-Related Disclosures for Investors" (final March 6, 2024). Items 1500-1507 of Regulation S-K and Article 14 of Regulation S-X. **Verify current effectiveness at draft time** — the rule has been subject to legal challenges and the Commission stayed the rule pending resolution of consolidated litigation in the Eighth Circuit (Order issued April 4, 2024).
- TCFD: "Recommendations of the Task Force on Climate-related Financial Disclosures" (Final Report, June 2017) and "Implementing the Recommendations of the Task Force on Climate-related Financial Disclosures" (October 2021). Pillars: Governance, Strategy, Risk Management, Metrics and Targets. The FSB disbanded the TCFD in October 2023 with monitoring transferred to the IFRS Foundation; the recommendations remain the working voluntary frame and underpin ISSB IFRS S2.
- IFRS S2 Climate-related Disclosures (June 2023) for firms reporting under ISSB-aligned regimes.
- EU CSRD and ESRS E1 (Climate change) for firms in scope under the EU regime, including US subsidiaries and non-EU groups consolidated through EU parents.
- California Climate Corporate Data Accountability Act (SB 253) and Climate-Related Financial Risk Act (SB 261); verify effective status given litigation history and current implementing regulations at draft time.
- NYDFS Industry Letter on Climate-Related Financial Risks (for state-regulated banks and insurers).
- NAIC Climate Risk Disclosure Survey (TCFD-aligned, mandatory in 15 US states for in-scope insurers).

#### What changes for climate-flagged disclosure-readiness work

##### 1. The 8-K trigger flow applies to material climate-related events

A material climate-related event (a severe weather loss, a transition-policy event affecting a material exposure, a material climate-target abandonment) is a material event under the same 8-K framework. The trigger flow runs through the same DCP. Item 1.05 itself does not apply to climate events (it is cyber-incident-specific), but the registrant's 8-K Item 8.01 (Other Events) or Item 7.01 (Reg FD) is the disclosure venue, and the materiality determination uses the same TSC / Basic standard.

The DCP map (Artifact C) covers cyber explicitly; firms with climate-disclosure obligations frequently use the same DCP map for climate events. The materiality-determination protocol, the named decision-makers, the time-box, and the documentation requirements are common.

##### 2. The 10-K disclosure cycle integrates Item 106 (cyber) and the Item 1500-series (climate)

For registrants in scope under the SEC Climate Disclosure Rule (where current effectiveness applies), the same 10-K cycle disclosures cover Item 106 (cyber risk-management and governance) and Items 1500-1507 (climate risk-management, governance, strategy, targets, and emissions). The disclosure committee and securities counsel review the cycle as a whole; the year-over-year diff discipline applies to both.

Where the SEC Climate Disclosure Rule is currently stayed or where its applicability to the registrant is unresolved, the registrant typically:

- Carries forward voluntary TCFD-aligned disclosure in the 10-K (or in a separately published sustainability or integrated report).
- Reports under EU CSRD via parent-group consolidation if applicable.
- Files state-required disclosure (NAIC Climate Risk Disclosure Survey, California SB 253 / 261 where current implementing regulations apply).

The pack carries the firm's current disclosure venue posture and the verification-flag discipline on SEC-rule status. **Default posture: cite the SEC rule with `[verify current effectiveness]` and lean on TCFD or CSRD or state-required disclosure for substantive content.** Never assert current effectiveness of the SEC climate rule without checking the SEC's posture as of the report date.

##### 3. The materiality lens is the same; the facts are different

The TSC / Basic materiality standard applies to climate-related events as it does to cyber events. The facts development is different:

- Cyber-incident facts develop on a hours-to-days timeline; the workpaper captures the snapshot.
- Climate-related event facts can develop on a weeks-to-quarters timeline (a severe-weather loss has insurance-recoverable estimates that settle over months; a transition-policy event has portfolio implications that develop with policy implementation).

The workpaper structure (facts known / unknown / reasonably knowable; quantitative impact current / reasonably foreseeable; qualitative factors; aggregation) applies to both, with adapted facts.

##### 4. Aggregation analysis for climate-related events

Item 1.05 Instruction 1 on aggregation is cyber-specific. For climate-related events, the parallel principle is the SEC Climate Disclosure Rule's aggregation guidance for Article 14 of Regulation S-X (financial-statement effects of severe weather events): aggregation thresholds for capitalized costs and expenditures from severe weather events. Where a series of severe-weather events individually below threshold collectively exceed it, the financial-statement effect aggregates.

The workpaper's aggregation row carries climate-event aggregation when applicable, even though the Instruction 1 reference does not directly apply to non-cyber events. The aggregation analysis is the same disclosure-committee discipline.

##### 5. Governance disclosure overlap (Item 106(c) and Item 1501)

The Item 106(c) cyber-governance disclosure and the Item 1501 climate-governance disclosure (where the Climate Rule's effectiveness applies) frequently name the same board committee (typically the Risk Committee or a dedicated Sustainability Committee for climate; the Risk Committee or Audit Committee for cyber) and the same management chain (CRO, with CISO for cyber and chief sustainability officer or equivalent for climate).

The cross-cutting alignment is a content question for the disclosure committee. Where the same committee oversees both, the disclosures should be consistent on cadence, informing processes, and committee composition. Inconsistency between the two governance disclosures is a frequent finding.

##### 6. Risk-management process integration (Item 106(b)(1)(i) and Item 1502)

Item 106(b)(1)(i) requires disclosure of whether and how cyber risk-management processes are integrated into the firm's overall risk-management system. Item 1502 of the Climate Rule requires similar disclosure for climate. The integration narrative should be consistent across the two: where the firm's enterprise risk-management framework treats both as enterprise risks integrated into the same framework, both disclosures should reflect that.

Treating cyber and climate as siloed risks in the disclosures (when the firm's actual ERM framework integrates them) is an inconsistency reviewers pull on.

##### 7. Forward-looking disclosure and verification discipline

The forward-looking commentary in any climate-cross-cutting work carries explicit verification discipline:

- SEC Climate Disclosure Rule status — `[verify current effectiveness]` flag; do not assert in force without checking SEC posture at draft time.
- California SB 253 / 261 — verify current implementing regulations and effective dates given litigation history.
- EU CSRD wave-2 / wave-3 timing for in-scope subsidiaries.
- ISSB IFRS S2 adoption status by jurisdictions where the firm operates.

The workpaper's `verification_flags_carried_forward` array carries each flag forward to draft time.

#### Climate-specific output additions

When climate is in scope:

- Artifact A material-event row carries the climate-event characterization (acute physical, chronic physical, transition-policy, transition-technology, transition-market, transition-reputational) and the disclosure venue (8-K Item 8.01, 10-K Item 1500-series, voluntary TCFD report, state-required filing).
- Artifact B carries an Item 1500-series cross-link in the 10-K diff record, and a year-over-year diff on the climate-disclosure cycle alongside the Item 106 cyber-disclosure cycle.
- Artifact C documents whether the firm uses one DCP for both cyber and climate events (typical) or separate DCPs (less common; usually means climate is owned by sustainability function with a parallel escalation path that converges at the disclosure committee).
- Source trace carries the SEC Climate Rule citation with the `[verify current effectiveness]` flag explicit, and the substantive content anchor (TCFD, ISSB IFRS S2, CSRD ESRS E1, or state-required) for the working-frame content.

#### Common pitfalls in climate-flagged disclosure-readiness work

- Asserting current effectiveness of the SEC Climate Disclosure Rule without checking SEC posture at draft time.
- Treating climate-related material events as out of scope for the 8-K because they do not trigger Item 1.05. Item 8.01 (or Item 7.01 in some scenarios) is the venue and the materiality determination uses the same TSC / Basic standard.
- Inconsistency between the Item 106(c) and Item 1501 governance disclosures when the same committee oversees both.
- Inconsistency between Item 106(b)(1)(i) and Item 1502 risk-management-integration narratives when the firm's actual ERM treats both as integrated.
- Treating EU CSRD as out of scope for US-headquartered firms without checking subsidiary consolidation. Many US firms have material EU subsidiaries that pull the parent into wave-2 or wave-3 reporting under ESRS.
- Rolled-forward-unchanged climate disclosure year-over-year. Year-over-year diff and rationale apply.
- Using the firm's prior-vintage scenario data after a vintage refresh has been published.
- Omitting the verification-flag discipline in the source trace. Each climate citation needing verification carries the flag forward.

## cyber

### Cyber cross-cutting overlay for cyber-disclosure-readiness

This skill is the cyber disclosure skill, and the cyber overlay is its core anchor set kept in references so SKILL.md remains a workflow rather than a regulatory primer. The overlay collects the cyber-specific anchors the three artifacts depend on, and notes what each contributes.

Loaded by: `cyber-disclosure-readiness/SKILL.md` always (this is the core anchor set, not optional). Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

Primary cyber anchors (this skill's spine):

- SEC Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure Final Rule, Release Nos. 33-11216 / 34-97989 (adopted July 26, 2023). Phased effective dates: Item 1.05 December 18, 2023 (non-SRC) and June 15, 2024 (SRC); Item 106 for fiscal years ending on or after December 15, 2023 (large filers) with phased SRC applicability.
- Form 8-K Item 1.05 — Material Cybersecurity Incidents (17 CFR §249.308). Four-business-day clock from materiality determination. Instruction 1 covers a series of related occurrences. Item 1.05(b) addresses material amendments. Item 1.05(c) provides the AG delay provision.
- Regulation S-K Item 106 — Cybersecurity Risk Management, Strategy, and Governance (17 CFR §229.106). Subitems 106(b) (risk management and strategy with five enumerated elements) and 106(c) (governance with board-oversight and management-role elements).
- Exchange Act Rule 13a-15 / 15d-15 — Disclosure controls and procedures. Defines DCP at Rule 13a-15(e); the cyber-disclosure trigger flow is the cyber cut of the firm's DCP framework.
- Form 6-K and Form 20-F Item 16K — Foreign private issuer treatment. FPIs are not subject to Form 8-K and report material cyber information on Form 6-K when otherwise public; Form 20-F Item 16K parallels Item 106 for the FPI annual disclosure.
- SEC Compliance and Disclosure Interpretations (C&DIs) for Form 8-K Item 1.05 and Regulation S-K Item 106. Post-adoption staff guidance on materiality determination process timing, delay-provision mechanics, voluntary Item 1.05 filings, ransomware-payment considerations, and aggregation under Instruction 1.

Materiality-standard anchors:

- TSC Industries, Inc. v. Northway, Inc., 426 U.S. 438 (1976) — substantial-likelihood standard.
- Basic Inc. v. Levinson, 485 U.S. 224 (1988) — applied TSC in the Section 10(b) / Rule 10b-5 context; probability-magnitude analysis for forward-looking or contingent events.

Parallel-clock anchors that surface in Artifact A's parallel-clocks table for in-scope registrants:

- Federal banking agencies' Computer-Security Incident Notification Rule (12 CFR Part 53 OCC; 12 CFR Part 225 Subpart N FRB; 12 CFR Part 304 Subpart C FDIC), effective May 1, 2022. 36-hour clock from determination of a notification incident; 4-hour bank-service-provider customer-notification trigger.
- NYDFS 23 NYCRR Part 500 §500.17(a) — 72-hour notice from determination of cybersecurity event meeting the rule's thresholds. §500.17(c) — 24-hour notice of extortion payment (Second Amendment).
- SEC Regulation S-P amendments (Release Nos. 34-100155 et al., May 16, 2024). Amends 17 CFR Part 248.30. 30-day customer-notification clock from awareness of unauthorized access to sensitive customer information.
- HIPAA Breach Notification Rule (45 CFR §§164.400-414) — 60-day individual-notice clock; concurrent HHS notice for 500-or-more-affected.
- GLBA Safeguards Rule (16 CFR Part 314, FTC) and Interagency Guidelines (12 CFR Part 30 Appendix B for OCC; 12 CFR Part 208 Appendix D-2 for FRB; 12 CFR Part 364 Appendix B for FDIC) plus the 2005 Interagency Guidance on Response Programs.
- State breach-notification laws (varies by state; multi-state firms map state-by-state).
- NAIC Insurance Data Security Model Law (Model #668) §6 — 72-hour notice for state-licensed insurers; state adoption varies.
- FINRA Rule 4530 — reporting requirements for FINRA-member broker-dealers; cyber events meeting 4530(a) or (d) thresholds.

Operational and supervisory frames:

- NIST Cybersecurity Framework 2.0 (CSWP 29, February 26, 2024) — Govern function maps to Item 106(c); Identify-Protect-Detect-Respond-Recover map to Item 106(b).
- **NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile (April 3, 2025)**, superseding Rev. 2 (Computer Security Incident Handling Guide, August 2012). Rev. 3 re-maps incident-response activities into CSF 2.0 functions (Govern, Identify, Protect, Detect, Respond, Recover) rather than the Rev. 2 four-phase lifecycle. Underpinning the timeline section in Artifact A; verify which revision the firm's IR function operates under.
- FFIEC IT Examination Handbook Information Security booklet (September 2016) — bank-supervisory expectations for incident response and cybersecurity governance.

#### What changes for the workflow

##### 1. The materiality-determination workpaper is the cyber-distinct artifact

Cyber-incident materiality is distinct from financial-statement materiality (the SAB 99 quantitative-qualitative composite) and from prior FD-driven materiality. The TSC standard is the rule-incorporated standard but the application to a cyber incident requires:

- A facts-as-known posture that distinguishes what is known from what is reasonably knowable as of the determination date. Cyber-incident facts develop quickly; the workpaper records the snapshot used for determination.
- A quantitative-and-qualitative composite. Quantified financial impact is often unknown or partial at the determination date; qualitative factors (reputation, regulatory consequence, strategic exposure, competitive position) frequently dominate.
- An aggregation analysis under Instruction 1 to Item 1.05. Related occurrences aggregate; the empty-array case is a stated determination, not an absence.

The workpaper is the evidence that the disclosure committee made the determination it did on the facts available; in any subsequent enforcement question, the workpaper is what gets read first.

##### 2. The 4-business-day clock starts at materiality determination

The single most-cited error in early Item 1.05 filings is conflating the clock-start date with detection. The schema's `disclosure_clock_start` field equals `materiality_determination_date`, not `detection_date`. The DCP trace records the gap between detection and determination (as a process metric for time-to-determination); the gap is not a clock-violation question unless determination was unreasonably delayed.

"Without unreasonable delay" in determining materiality is the SEC's qualifier; the DCP's materiality time-box exists to evidence that determination was not unreasonably delayed.

##### 3. Item 1.05 disclosure draft has four required elements and stops there

The four elements: nature, scope, timing, material impact (or reasonably likely material impact). Disclosure drafts that include forensic detail, IOCs, threat-actor identification, remediation specifics, or system-name detail go beyond the rule's requirements and frequently against Reg FD (selective-disclosure considerations) and against ongoing-investigation-prejudice posture.

The "to the extent known" framing is required where the determination is made before scope is fully understood; the rule contemplates this.

##### 4. Item 106 governance disclosure is governance-content-loaded

The Item 106(c) board-oversight subsection names the specific board committee, the cadence, and the processes by which the board or committee is informed. "The appropriate management committee oversees cybersecurity risk on an ongoing basis" reads as boilerplate and is what reviewers flag.

The Item 106(c) management-role subsection names the positions / committees, the named expertise (CISO with credentials), and the reporting line. "The Company's cybersecurity organization is led by experienced professionals" reads as boilerplate.

##### 5. Year-over-year diff on Item 106 is required practice

The Item 106 disclosure is annual; the underlying facts (board cadence, management positions, third-party engagements, material effects) change. Rolled-forward-unchanged Item 106 is a frequent finding from internal audit and from securities counsel review. The schema's `year_over_year_diff` array is where the analysis lives; "no substantive change — refreshed for currency" is an acceptable rationale, but the analysis is required.

##### 6. The DCP map is the framework backbone

Artifact C is what an examiner asks for when the question is "how does an incident move through the firm to the materiality call". The map names:

- Trigger detection points with named owner roles and time-to-triage SLAs.
- Escalation paths first-line to second-line to GC office to disclosure committee.
- Materiality-determination protocol with named decision-makers, criteria framework, time-box, and tie-break.
- Documentation requirements per stage (the audit-evidence backbone for the DCP).
- Gaps and remediation with severity and target date.

The DCP map's existence and exercise is the evidence that DCP under Rule 13a-15 functioned for cyber. It is what 302 / 906 certifications reach for in the cyber cut.

##### 7. Voluntary Item 1.05 filings carry a different posture

A registrant filing under Item 1.05 for a non-material incident receives reduced safe-harbor treatment per SEC staff C&DIs; voluntary filings are filed under Item 8.01 with a narrative that does not invoke Item 1.05's materiality assertion. Artifact A's `materiality_determination` field has a `not-material` enum value precisely so the workpaper records the determination, and the disclosure draft (where any) routes to Item 8.01 rather than Item 1.05.

#### Common pitfalls

- Treating the materiality call as the cyber team's call. Materiality is a disclosure determination made by the disclosure committee with securities counsel input; the cyber team contributes facts and quantitative inputs.
- Conflating clock-start with detection. The 4-business-day clock starts at materiality determination.
- Over-disclosure of incident detail. The four required elements bound the Item 1.05 draft; forensic detail, IOCs, named threat actors, and remediation specifics do not appear.
- Missing aggregation analysis. Empty-array aggregation is a stated determination, not an absence.
- Stale Item 106 disclosure. Year-over-year diff and rationale is required.
- Foreign-private-issuer confusion. FPIs report on Form 6-K, not 8-K; Form 20-F Item 16K is the FPI annual disclosure.
- Treating "reasonably likely material impact" as speculative. The "or reasonably likely to materially affect" framing has substance and requires disclosure of reasonably foreseeable impact.
- Voluntary Item 1.05 filing. Non-material incidents file under Item 8.01, not Item 1.05; the safe-harbor treatment differs.
- Including the DCP map in the public disclosure. The DCP map is the firm-side evidence; Item 106(b) discloses the processes, not the map.
- Ignoring the federal banking agency's bank-service-provider 4-hour customer-notification trigger when the firm is a bank service provider. The 4-hour trigger runs from the service-provider side and is independent of the registrant-side 36-hour clock.

## privacy

### Privacy cross-cutting overlay for cyber-disclosure-readiness

When customer financial information, health information, or other regulated personal information is implicated in a cyber incident, privacy-notification clocks run alongside the SEC Item 1.05 clock. The pack must surface every privacy clock applicable to the registrant; missing one is a frequent regulator finding.

Loaded by: `cyber-disclosure-readiness/SKILL.md` when `scope.cross_cutting_set` includes `privacy`, when the scope flags customer financial information / PHI / sensitive customer information in scope, or when Artifact A's incident facts implicate any covered information type. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- GLBA Title V and the FTC Safeguards Rule (16 CFR Part 314), current text reflecting December 2021 amendments and October 2023 amendments adding the FTC notification trigger for breaches affecting 500 or more consumers.
- Banking-agency Interagency Guidelines Establishing Information Security Standards (12 CFR Part 30 Appendix B for OCC; 12 CFR Part 208 Appendix D-2 for FRB; 12 CFR Part 364 Appendix B for FDIC) and the 2005 Interagency Guidance on Response Programs for Unauthorized Access to Customer Information and Customer Notice (Federal Register, March 29, 2005).
- SEC Regulation S-P amendments (Release Nos. 34-100155 et al., May 16, 2024). Amends 17 CFR Part 248.30. Covered institutions: broker-dealers, investment advisers, registered investment companies, transfer agents. 30-day customer-notification clock from awareness of unauthorized access to sensitive customer information.
- HIPAA Breach Notification Rule (45 CFR §§164.400-414). 60-day individual-notice clock. Concurrent HHS notice for 500-or-more-affected breaches; annual log for under-500-affected.
- State breach-notification laws (50-state mosaic; CA, NY, TX, IL, MA carry the most-cited specifics; CCPA / CPRA in California carries additional consumer rights). Verify state-specific timelines and trigger thresholds at draft time.
- NAIC Insurance Data Security Model Law (Model #668), §6 (notification of cybersecurity event) — 72-hour notice to commissioner for state-licensed insurers in adopting states.

#### What changes for privacy-flagged disclosure-readiness work

##### 1. Privacy notification clocks join the parallel-clocks table

Each clock applicable to the registrant has a row. The clocks frequently start from different basis events:

| Regulator | Clock basis | Typical clock |
|---|---|---|
| SEC (Item 1.05) | materiality determination | 4 business days |
| FTC Safeguards Rule (16 CFR Part 314) | breach affecting 500+ consumers | as soon as possible, no later than 30 days from discovery |
| Banking-agency Interagency Guidance | unauthorized access to sensitive customer information | as soon as possible (typically within days) |
| SEC Reg S-P (17 CFR Part 248.30) | awareness of unauthorized access | 30 days (covered institutions) |
| HIPAA Breach Notification Rule | discovery of breach of unsecured PHI | 60 days individual notice; concurrent HHS for 500+ |
| State breach-notification | awareness or determination, varies by state | varies by state (typically 30-90 days) |
| NAIC Model #668 §6 (state-licensed insurers) | determination of cybersecurity event | 72 hours |
| CCPA / CPRA (California) | breach affecting CA residents' nonencrypted personal information | "in the most expedient time possible and without unreasonable delay" |

The SEC Item 1.05 clock is the disclosure-side clock. The privacy clocks run independently and on different bases. A single incident can simultaneously trigger several.

##### 2. Sensitive-customer-information posture drives Reg S-P

The SEC Reg S-P amendments define "sensitive customer information" (broader than the prior Safeguards Rule scope) and the 30-day clock runs on awareness of unauthorized access to that category, not on the broader cyber-incident materiality determination. The pack surfaces the Reg S-P determination separately from the Item 1.05 determination; the two are independent inquiries.

The Reg S-P customer-notification content requirements are distinct from the Item 1.05 disclosure content. The customer notice describes the incident, the type of sensitive customer information affected, and the contact information; it is not a substitute for, and is not substituted by, the 8-K Item 1.05 filing.

##### 3. State breach-notification mosaic

Multi-state firms map state-by-state. The pack does not enumerate all 50 states by default; the scope identifies the states where customer information is implicated, and the parallel-clocks table carries one row per state with the trigger threshold and the clock.

CA, NY, TX, IL, and MA carry the most-cited specifics; CCPA / CPRA adds consumer-rights obligations on top of the breach-notification obligations. The Massachusetts standard for "personal information" is broader than many other states. The pack flags state-specific deviations.

##### 4. HIPAA scope for in-scope financial-services entities

Most financial-services firms are not HIPAA-covered entities. Some are business associates under BAAs (e.g., FNOL handling for health insurers, claims processing for healthcare-affiliated counterparties). Where a financial-services firm is a business associate, the HIPAA 60-day individual-notice clock and the concurrent-HHS-notice for 500-or-more-affected obligations apply.

The pack flags the BAA posture and the resulting HIPAA-clock applicability when relevant.

##### 5. Privacy-notification content overlap with Item 1.05

The Item 1.05 disclosure (nature, scope, timing, material impact) does not duplicate the privacy-notification content. The two notifications run on different audiences (investors versus affected individuals), different timing, and different content rules. The pack tracks both as parallel obligations.

A single incident may result in: the 8-K Item 1.05 filing (investors); the Reg S-P customer notice (affected individuals); state breach-notification letters (affected residents in scope); the federal banking agency notification (regulator); the NYDFS §500.17 notification (regulator); the FTC Safeguards Rule notification (regulator, for 500+ affected).

##### 6. Sanctions and ransomware-payment due diligence

Where ransomware is in scope, the Treasury OFAC advisory on ransomware payments and the requirements that some payments to sanctioned actors are prohibited apply. NYDFS §500.17(c) (Second Amendment) requires a 24-hour notice of an extortion payment and within 30 days a written description including sanctions due-diligence performed.

The pack flags the ransomware-payment posture and the sanctions due-diligence record where applicable; this content interacts with privacy-notification content but is a separate analytical thread.

#### Privacy-specific output additions

When privacy is in scope:

- Parallel-clocks table carries one row per privacy clock applicable to the registrant.
- Artifact A's `materiality_basis_quantitative.customer_impact_count` field is populated with named segments (financial customers, healthcare counterparties' patients, employees, others); the count drives several privacy clocks.
- Artifact A's facts-of-the-incident row carries the type of information accessed or used (sensitive customer information per Reg S-P; unsecured PHI per HIPAA; nonencrypted personal information per state laws); the type drives clock applicability.
- Source trace carries the privacy-side citations alongside the SEC citation.

#### Common pitfalls

- Treating privacy clocks as out-of-scope because the work is SEC-anchored. The parallel-clocks table is multi-regulator by design.
- Substituting the 8-K Item 1.05 filing for the Reg S-P customer notice or for state breach-notification letters. The notifications run on different audiences and different content rules; one does not satisfy the other.
- Using a single state's breach-notification timeline as a proxy for all states. State-specific timelines vary; the parallel-clocks table is state-by-state for multi-state incidents.
- Missing the BAA posture when the firm is a HIPAA business associate. BAA status pulls the firm into the HIPAA Breach Notification Rule timeline.
- Omitting the FTC Safeguards Rule trigger for non-bank financial institutions affected by a 500+ consumer breach. The FTC trigger is on top of the SEC and the banking-agency triggers.
- Conflating Reg S-P sensitive-customer-information awareness with materiality determination. The Reg S-P 30-day clock starts at awareness of unauthorized access; the SEC 4-business-day clock starts at materiality determination. Different basis events.
- Treating the NYDFS §500.17(c) extortion-payment notice as a private matter. The 24-hour and 30-day notices are NYDFS obligations; the sanctions due-diligence record is part of the 30-day written description.
