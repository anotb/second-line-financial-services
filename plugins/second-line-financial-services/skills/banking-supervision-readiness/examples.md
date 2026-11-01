# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## frb-consent-order-quarterly-update-state-member-bank

### Example: FRB consent-order quarterly remediation update at a state-member bank with eight articles spanning BSA / AML, third-party risk, and IT

Public-source-derived. No named institution. Roles only. Consent order referenced by docket convention only.

#### Engagement context

A state-member bank (asset size band 10B-50B, approximately $15B in total consolidated assets, FRB-regulated under FRB Commercial Bank Examination Manual cadence and state-banking-department coordination) is operating under an FRB consent order with eight articles. The articles span BSA / AML (three), third-party risk (two), and IT (three). The bank is preparing the quarterly remediation update for the FRB Reserve Bank, including the MRA / MRIA closure cross-walk. Two MRIAs are in sustained-remediation, three are in in-remediation, three are still in action-plan stage. Source posture is public-plus-firm-policy-plus-evidence; the access population is the bank's senior risk leadership, BSA officer, head of vendor management, CIO, and outside counsel.

#### Cover and cycle scope

| Field | Value |
|---|---|
| Pack ID | SR-2026-FRB-CO-Q2-001 |
| Source posture | public-plus-firm-policy-plus-evidence |
| Access population | senior risk leadership, BSA officer, head of vendor management, CIO, outside counsel |
| Confidence label | medium |

| Institution profile | Value |
|---|---|
| Type | state-member-bank |
| Primary federal regulator | FRB |
| State supervisor | (state banking department) |
| Asset size band | 10B-50B |
| Heightened Standards applicability | no (asset band below $50B; FRB applies enhanced expectations under consent order regardless) |

| Cycle profile | Value |
|---|---|
| Cycle type | targeted (consent-order quarterly remediation cadence) |
| Rated framework | CAMELS |
| Examiner-in-charge role | FRB Reserve Bank examiner-in-charge |
| Fieldwork window | quarterly remediation update; FRB on-site for 2-week verification window quarterly |
| Review period | trailing 90 days |
| Topical readiness slices | BSA-AML, IT, third-party-risk |
| Cross-cutting overlays | cyber (IT articles in scope), conduct (not in this consent order) |

#### Executive summary

- Eight consent-order articles in flight; two MRIAs in sustained-remediation (4 and 6 months observed), three in in-remediation, three in action-plan stage.
- BSA / AML articles are the most mature on the closure curve; IT articles are the most exposed.
- Aging analysis: oldest open action item is 14 months old, against the bank's internal target of 12 months; escalation risk flagged medium.
- Reviewer question whether earlier validation (under the bank's 12-month sustained-operation policy) is acceptable to the FRB given the consent-order context.
- Overall confidence medium.

#### Part A: CAMELS preparation by component (concise, with consent-order context)

For a consent-order quarterly remediation update, the CAMELS section is condensed; the spine of the pack is Parts B and C. The Management component carries the consent-order remediation cadence narrative.

- **C — Capital adequacy.** Capital position adequate; well-capitalised threshold maintained throughout the consent-order period under 12 CFR Part 208 Subpart D [verify subpart]. Confidence: high.
- **A — Asset quality.** Stable; not directly implicated in any consent-order article. Confidence: high.
- **M — Management.** Consent-order remediation cadence is the primary M-component evidence. Board oversight cadence increased to monthly during the consent-order period; risk committee receives the consent-order remediation status as a standing agenda item; internal audit's independence of MRIA closure validation evidenced in the audit charter. Public criteria: FDIC Manual section 4.1 [verify section]; FRB SR 12-17 governance expectations; OCC Comptroller's Handbook Internal and External Audits booklet (current edition) [verify edition] for evidence pattern even though the bank is not OCC-regulated (the booklet's framework is widely used). Confidence: medium.
- **E — Earnings.** Stable. Confidence: high.
- **L — Liquidity.** Stable; not directly implicated. Confidence: high.
- **S — Sensitivity to market risk.** Stable. Confidence: high.

#### Part B: Examiner-letter response readiness (eight-row table)

| Item ID | Source | Category | Component / topical link | Action plan summary | Owner role | Closure status | Aging | Escalation risk |
|---|---|---|---|---|---|---|---|---|
| CO-ART-1 | FRB consent order, Article 1 | consent-order-article | BSA-AML | Independent BSA-program assessment commissioned and complete; remediation roadmap in execution | BSA officer | sustained-remediation | within target | low |
| CO-ART-2 | FRB consent order, Article 2 | consent-order-article | BSA-AML | Suspicious-activity-monitoring tooling enhancement in production; backlog cleared | BSA officer | sustained-remediation | within target | low |
| CO-ART-3 | FRB consent order, Article 3 | consent-order-article | BSA-AML | CDD program enhancement in execution; sustained-operation period 6 months | BSA officer | in-remediation | within target | medium |
| CO-ART-4 | FRB consent order, Article 4 | consent-order-article | third-party-risk | Vendor-inventory criticality classification refresh complete; lifecycle-controls upgrade in build | head of vendor management | in-remediation | 14 months | medium |
| CO-ART-5 | FRB consent order, Article 5 | consent-order-article | third-party-risk | §1867(c) examination-access flow-down clauses inserted across critical-vendor contracts | head of vendor management | in-remediation | within target | medium |
| CO-ART-6 | FRB consent order, Article 6 | consent-order-article | IT (FFIEC IT Handbook Information Security booklet) | Information-security-program enhancement; vulnerability-management process redesign in build | CIO | action-plan | within target | high |
| CO-ART-7 | FRB consent order, Article 7 | consent-order-article | IT (FFIEC IT Handbook Management booklet) | IT-governance enhancement; CIO charter and IT-steering-committee mandate refreshed | CIO | action-plan | within target | medium |
| CO-ART-8 | FRB consent order, Article 8 | consent-order-article | IT (FFIEC IT Handbook Outsourcing Technology Services booklet) | Outsourced-technology oversight enhancement | CIO | action-plan | within target | high |

#### Part C: MRA / MRIA closure cross-walk (sample rows)

| Finding ID | Regulator | Date issued | Action taken | Evidence type | Sustained-operation months | Closure readiness | Owner role |
|---|---|---|---|---|---|---|---|
| CO-ART-1 | FRB | (consent-order date) | Independent BSA-program assessment, remediation roadmap, controls operational | policy-update + control-implementation + training + sustained-operation | 6 | medium | BSA officer |
| CO-ART-2 | FRB | (consent-order date) | Suspicious-activity-monitoring tooling enhanced; backlog cleared | system-change + control-implementation + sustained-operation | 4 | medium | BSA officer |
| CO-ART-3 | FRB | (consent-order date) | CDD program enhanced | policy-update + control-implementation + training | 0 | low | BSA officer |
| CO-ART-4 | FRB | (consent-order date) | Vendor inventory and lifecycle controls upgraded | policy-update + control-implementation | 0 | low | head of vendor management |
| CO-ART-6 | FRB | (consent-order date) | Information-security-program redesign in build | (none yet — action-plan stage) | 0 | low | CIO |

#### Tail

##### Heightened Standards readiness

Not applicable at current asset size band ($15B; threshold $50B under 12 CFR Part 30 Appendix D). Reviewer note that the FRB applies enhanced expectations under the consent order regardless of asset size; the M-component evidence for the consent-order period reads to the same risk-governance-framework expectations.

##### Topical readiness slice: BSA / AML, IT, third-party risk

- **BSA / AML.** FFIEC BSA/AML Examination Manual (current edition) [verify section] is the primary anchor for the three BSA articles. Independent-testing report dated within the consent-order period; BSA-officer attestation refreshed quarterly.
- **IT.** FFIEC IT Examination Handbook (Information Security, Management, Outsourcing Technology Services booklets, current editions) [verify edition] is the anchor for the three IT articles. Most recent IT audit and penetration test (dated; carried in the firm-overlay).
- **Third-party risk.** Interagency Guidance on Third-Party Relationships: Risk Management (June 6, 2023, FRB SR 23-4 [verify FRB SR number]) is the anchor for the two third-party-risk articles. Bank Service Company Act 12 USC §1867(c) examination-access flow-down clauses inserted across critical-vendor contracts.

##### Recommended owner actions before next quarterly update

| Action | Owner role | Target |
|---|---|---|
| Formalise sustained-operation evidence package for CO-ART-1 and CO-ART-2 (request examiner validation under bank's 12-month policy with carve-out request to FRB) | BSA officer + outside counsel | within 30 days |
| Accelerate CO-ART-4 lifecycle-controls upgrade target by 60 days | head of vendor management | within 60 days |
| Confirm CIO IT-roadmap dependencies for CO-ART-6, -7, -8 are de-risked; escalate to risk committee | CIO + chief risk officer | within 14 days |
| Confirm independent-validation cadence with chief audit executive for all in-flight articles | chief audit executive | within 14 days |

##### Source trace headline

FRB Bank Holding Company Supervision Manual (current edition) [verify edition and section]; FRB Commercial Bank Examination Manual (current edition) [verify edition]; FRB SR letters governing the MRA / MRIA framework (SR 13-17 / SR 22-3 [verify both operative]); FFIEC BSA/AML Examination Manual (current edition) [verify section]; FFIEC IT Examination Handbook (Information Security, Management, Outsourcing Technology Services booklets, current editions) [verify edition]; Interagency Guidance on Third-Party Relationships: Risk Management (June 6, 2023, FRB SR 23-4 [verify]); Bank Service Company Act 12 USC §1867(c). Anonymous; consent order referenced by docket convention only.

## occ-full-scope-midsize-national-bank

### Example: OCC full-scope safety-and-soundness exam, midsize national bank approaching the Heightened Standards threshold

Public-source-derived. No named institution. Roles only.

#### Engagement context

A midsize national bank (asset size band 10B-50B, approximately $35B in total consolidated assets, OCC-regulated, not yet a covered bank under 12 CFR Part 30 Appendix D but trending toward the $50B threshold) is six weeks out from an OCC full-scope safety-and-soundness examination. The cycle is a 12-month supervisory plan with a 6-week on-site fieldwork window. The chief risk officer needs the entry-meeting pack and the CAMELS-component preparation; the head of supervisory affairs runs the examination coordination. Source posture is public-plus-firm-policy-plus-evidence; the access population is the bank's senior risk and compliance leadership plus outside counsel.

#### Cover and cycle scope

| Field | Value |
|---|---|
| Pack ID | SR-2026-OCC-FS-001 |
| Source posture | public-plus-firm-policy-plus-evidence |
| Access population | senior risk and compliance leadership plus outside counsel |
| Confidence label | medium |

| Institution profile | Value |
|---|---|
| Type | national-bank |
| Primary federal regulator | OCC |
| Asset size band | 10B-50B |
| Heightened Standards applicability | approaching |
| Geographic footprint | northeastern US, branch-and-digital |

| Cycle profile | Value |
|---|---|
| Cycle type | full-scope |
| Rated framework | CAMELS |
| Examiner-in-charge role | OCC EIC, Northeastern district |
| Fieldwork window | (dated, six-week window starting in week seven) |
| Review period | trailing 18 months |
| Topical readiness slices | none topical-led; BSA-AML and IT covered as part of full-scope |
| Cross-cutting overlays | cyber (IT scope inside full-scope) |

#### Executive summary

- Capital and earnings strong; CRE concentration is the watch item with the ratio at 280% of total capital, below the 300% interagency screen but trending up.
- Two open MRAs from the prior cycle: one closed-pending-examiner-confirmation, one in remediation with a 60-day milestone; CECL methodology back-testing scheduled inside the fieldwork window.
- Liquidity well-positioned but the contingency funding plan was last tabletop-tested 14 months ago; CFP test recommended pre-entry.
- Heightened Standards forward-looking readiness section included given the bank is approaching the $50B threshold; OCC examiners will probe in advance.
- Overall confidence medium; high on Capital and Earnings, medium on Asset Quality, Management, and Liquidity, low on Sensitivity (one open IRR-model validation finding).

#### Part A: CAMELS preparation by component (component-by-component summary)

- **C — Capital adequacy.** CET1 ratio above well-capitalised threshold under 12 CFR Part 6 [verify subpart]; capital-action history clean for the review period; capital-planning document updated within the last 12 months. Reviewer question on capital-planning maturity given threshold proximity. Public criteria: OCC Comptroller's Handbook Capital and Dividends booklet (current edition) [verify edition]; well-capitalised threshold under 12 CFR Part 6 [verify subpart]. Confidence: high.
- **A — Asset quality.** CRE concentration ratio at 280% of total capital, below the 300% interagency screen under the December 2006 Interagency CRE Concentration Guidance and the 2015 Interagency Statement, but trending up over the review period. Classified-asset trend stable. CECL methodology back-testing scheduled inside the fieldwork window. Reviewer question on whether the concentration-risk management framework satisfies the Interagency Guidance §III.B [verify section] for a bank approaching the screen. Public criteria: OCC Comptroller's Handbook Asset Quality booklets (current editions) [verify edition dates]; Interagency CRE Concentration Guidance (December 12, 2006); 2015 Interagency Statement on Prudent Risk Management for CRE Lending. Confidence: medium.
- **M — Management.** Two open MRAs: MRA-2025-001 closed-pending-examiner-confirmation, with a 60-day open-on-record window; MRA-2025-002 in remediation with a 60-day milestone covering a vendor-management-program enhancement. Internal-audit independence intact; risk-committee minutes refreshed quarterly. Reviewer question on independence of internal audit's MRA closure validation. Public criteria: FDIC Manual section 4.1 [verify section]; FRB SR 12-17 governance expectations (referenced for context although the bank is not a BHC under separate FRB cycle); OCC Comptroller's Handbook Internal and External Audits booklet (current edition) [verify edition]. Confidence: medium.
- **E — Earnings.** NIM under pressure given rate environment but stable on a 12-month trailing basis; fee-income mix unchanged; expense trend within budget; dividend coverage strong. No flag. Public criteria: OCC Comptroller's Handbook Earnings booklet (current edition) [verify edition]. Confidence: high.
- **L — Liquidity.** LCR not applicable at current asset band [verify part by charter]; brokered-deposit reliance below internal cap; CFP last tabletop-tested 14 months ago, against the bank's internal target of 12 months. Recommended owner action to schedule a CFP tabletop within 30 days. Public criteria: OCC Comptroller's Handbook Liquidity booklet (current edition) [verify edition]; Interagency Policy Statement on Funding and Liquidity Risk Management (March 17, 2010, OCC OCC-2010-13). Confidence: medium.
- **S — Sensitivity to market risk.** IRR exposure within board-approved limits; one open model-validation finding on the EVE model (a traditional model) dating from the most recent MRM annual review. Reviewer question on model-validation closure cadence. Public criteria: OCC Comptroller's Handbook Interest Rate Risk booklet (current edition) [verify edition]; **Joint Interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026)** for traditional-model expectations. Confidence: low.

#### Part B: Examiner-letter response readiness (sample rows)

| Item ID | Source | Category | Component link | Action plan summary | Owner role | Closure status | Aging vs target | Escalation risk |
|---|---|---|---|---|---|---|---|---|
| MRA-2025-001 | OCC, prior-cycle supervisory letter | MRA | M | Vendor-management-program enhancement closed; awaiting examiner validation | head of TPRM | closed-pending-examiner-confirmation | within target | low |
| MRA-2025-002 | OCC, prior-cycle supervisory letter | MRA | M | Vendor-management-program enhancement in remediation; 60-day milestone in flight | head of TPRM | in-remediation | within target | medium |
| FIND-IRR-MODEL-001 | internal MRM annual review | supervisory-recommendation (internal-elevated, not yet examiner-issued) | S | EVE model validation finding; remediation underway | head of model risk | in-remediation | within target | medium |

#### Part C: MRA / MRIA closure cross-walk (sample rows)

| Finding ID | Regulator | Date issued | Action taken | Evidence type | Sustained-operation months | Closure readiness | Owner role |
|---|---|---|---|---|---|---|---|
| MRA-2025-001 | OCC | (prior-cycle date) | Vendor-management-program controls enhanced; quarterly attestations now in place | policy-update + control-implementation + sustained-operation | 7 | high | head of TPRM |
| MRA-2025-002 | OCC | (prior-cycle date) | TPRM tooling enhancement in build | system-change + control-implementation | 0 | low | head of TPRM |

#### Tail

##### Heightened Standards readiness (forward-looking)

The bank is approaching the $50B threshold under 12 CFR Part 30 Appendix D §II covered-bank scope [verify section labels]. The pack carries a forward-looking readiness section: risk-governance-framework draft attestation under §III, board independent-risk-committee evidence in place for the last four quarters, risk-appetite-statement cross-walk under build, three-lines-of-defense maturity assessment showing 1L and 2L mature, 1.5L being formalised, 3L mature. Forward-looking only; framework not yet binding.

##### Recommended owner actions before entry meeting

| Action | Owner role | Target |
|---|---|---|
| Schedule and complete CFP tabletop test | head of treasury | within 30 days |
| Close MRA-2025-001 internal-validation memo | chief audit executive | within 14 days |
| Refresh CRE concentration management memo for the audit committee | head of credit risk | within 21 days |
| Confirm IRR-model-validation closure timeline | head of model risk | within 14 days |

##### Source trace headline

OCC Comptroller's Handbook (Capital and Dividends, Asset Quality, Earnings, Liquidity, Interest Rate Risk, Internal and External Audits booklets, current editions) [verify edition dates]; FDIC Manual sections 4.1 and 5.1 [verify section]; Interagency CRE Concentration Guidance (December 12, 2006 and 2015 Statement); 12 CFR Part 30 Appendix D §§II–IV [verify section labels]; Interagency Policy Statement on Funding and Liquidity Risk Management (March 17, 2010, OCC OCC-2010-13); **Joint Interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026)** for traditional-model expectations. Anonymous; no named institutions.

## troubleshooting

### Troubleshooting: banking-supervision-readiness

Recurring defects in supervision-readiness packs. Read the corresponding section of `SKILL.md` and `references/source-anchors.md` first; the guidance here is for cases where the pack reads off-tone or fails on review.

#### CSI access-population breach in the prep population

Symptom: prior supervisory letters, draft examiner-letter responses, or verbatim MRA / MRIA text sit in a shared drive readable by individuals not on the CSI access list. The pack circulates to the credit risk committee or the audit committee with full prior-letter excerpts inline. A name on the cover sheet that does not appear on the regulator-acknowledged distribution list reads the verbatim finding.

Cause: the access-population constraint is read as a labelling rule for the document, not as a population control on every individual who handles, reads, or stores it. CSI travels with the file; the constraint travels with the population.

Fix: confidential supervisory information is governed by 12 CFR Part 4 Subpart C (OCC), 12 CFR Part 261 (FRB), and 12 CFR Part 309 (FDIC). The pack header names the access population at the cover; verbatim CSI text only sits in pack copies whose distribution matches that population. For a broader-population copy, summarise the finding without verbatim quotation. Verbatim CSI cannot leave the bank without the regulator's written authorisation. Where the access list is uncertain, default to the narrowest plausible population and flag the broader-distribution version as `[CSI redaction required before distribution]`.

#### MRA treated as MRIA (or vice versa)

Symptom: a Matter Requiring Attention is escalated as if it were a Matter Requiring Immediate Attention — board-meeting agenda time burned, executive remediation cadence stood up, regulatory-affairs escalation track triggered — for an item the regulator did not label MRIA. Or the inverse: an MRIA is tracked on the same monthly cadence as ordinary MRAs with no immediate-attention board-reporting hook.

Cause: the bank's tracker uses one label, the regulator's letter uses another, and the pack reconciles to the tracker rather than to the letter. Or the two categories are conflated as "supervisory findings" without preserving the regulator's distinction.

Fix: defer to the regulator's label on the source letter, not the bank's tracker. MRAs are matters requiring attention; MRIAs are matters requiring immediate attention. Aging tolerance, escalation cadence, board-reporting expectation, and closure-readiness threshold all differ between the two. Where the bank's tracker and the regulator's letter disagree, the cross-walk row uses the regulator's label and flags the tracker discrepancy as an owner action. The pack's executive summary surfaces the open MRIA population separately from the open MRA population; collapsing them into a "findings count" loses the signal the pack is meant to carry.

#### CAMELS-component scope drift

Symptom: a targeted IT examination pack carries six full CAMELS-component subsections; a quarterly consent-order remediation update carries the BHC rated framework. The pack reads as a generic enterprise risk register rather than as the response to the cycle scope.

Cause: the spine is built from the template rather than from the cycle profile. The full-scope template is reused for targeted, point-in-time, or topical cycles without trimming. Or the depository-institution spine is reused for a BHC supervisory cycle that needs the BHC rated-component framework.

Fix: confirm the cycle type and the rated framework on the cover before drafting Part A. A targeted IT exam reads the FFIEC IT Examination Handbook spine plus the IT-relevant CAMELS components (typically Management and Sensitivity, with the IT-specific request list in the topical readiness slice); the other components do not get full subsections. A BHC supervisory cycle reads the BHC rated-component framework (RFI/C(D) or successor) per FRB SR 12-17, not CAMELS. A quarterly consent-order update reads the cross-walk plus the article-by-article evidence section, not the full Part A. Component depth scales to scope; over-built sections read as not-ready, not as thorough.

#### Reg YY cited at a state-member bank

Symptom: the prudential-framework section cites 12 CFR Part 252 (Reg YY) as the binding regime for a state-member bank or a state non-member bank.

Cause: confusing the bank-level supervisory regime with the holding-company-level enhanced prudential standards regime. Reg YY is the FRB's enhanced prudential standards for bank holding companies and savings-and-loan holding companies above defined size and risk thresholds, plus US intermediate holding companies of foreign banking organisations. It does not run at the depository-institution level.

Fix: at the depository-institution level (national bank, state-member bank, state non-member bank, federal or state savings association), the prudential framework runs through 12 CFR Part 6 / Part 208 / Part 324 (capital), 12 CFR Part 50 / Part 249 / Part 329 (LCR / NSFR where applicable), and the safety-and-soundness regime under 12 USC 1818. Reg YY runs at the holding-company and IHC level under FRB jurisdiction. A state-member bank's exam pack cites Part 208 (the FRB's regulation for state-member banks) and the consolidated supervisory frame from FRB SR 12-17 for the holding-company connection; it does not cite Reg YY as the bank-level regime. Where the holding-company organisation has both a depository-institution cycle and a BHC cycle running, build the pack for the cycle in scope, not for both.

#### OCC Heightened Standards cited at a non-OCC-supervised bank

Symptom: the readiness tail carries a 12 CFR Part 30 Appendix D Heightened Standards section for a state-member bank, a state non-member bank, or a savings-and-loan holding company. The risk-governance-framework attestation references "OCC heightened-standards expectations" at an FRB-supervised or FDIC-supervised institution.

Cause: treating Heightened Standards as the federal large-bank governance regime rather than as the OCC's regime for OCC-supervised covered banks.

Fix: 12 CFR Part 30 Appendix D applies to OCC-supervised covered banks (national banks, federal savings associations, federal branches and agencies of foreign banks) at $50B+ avg total consolidated assets. It does not run at FRB-supervised state-member banks or FDIC-supervised state non-member banks. At an FRB-supervised institution, the analogous frame is the FRB's consolidated supervision regime (SR 12-17 for large institutions, SR 14-1 for risk-management standards on large and complex BHCs, the LFI rating system per SR 19-3 where the threshold applies); at an FDIC-supervised institution, the FDIC's enhanced supervisory expectations under the Risk Management Manual. Cite the regime that runs on the chartering and supervisory regulator, not the OCC's regime by analogy. A holding-company organisation may have an OCC-supervised national bank subsidiary that does fall under Heightened Standards; the section runs on that subsidiary and not on the broader holding-company organisation.

#### LFI rating framework applied below the LFI threshold

Symptom: the BHC supervisory section applies the Large Financial Institution rating framework (SR 19-3) at a regional BHC well under the $100B asset threshold, or applies LFI-aligned governance, capital-planning, and liquidity-risk-management ratings to a non-LFI BHC.

Cause: the LFI framework is the most recent FRB BHC rating frame and gets used as the default; the predecessor frames (RFI/C(D) for non-LFI BHCs) are remembered as legacy.

Fix: SR 19-3 establishes the LFI rating system for FRB-supervised firms with $100B+ in total consolidated assets and certain other criteria. BHCs below that threshold are rated under RFI/C(D) (or its successor non-LFI frame) per FRB SR 04-18 and successors. The pack cites the rating frame that applies at the BHC's size band; applying LFI rating components (Capital Planning and Positions, Liquidity Risk Management and Positions, Governance and Controls) at a non-LFI BHC misreads the supervisory expectation and overstates the framework's reach. Where the BHC is approaching the $100B threshold, run an LFI-readiness forward-looking section in the tail; do not collapse the current rating frame into the LFI frame.

#### Closure-readiness `high` without sustained-operation evidence

Symptom: every row in the MRA / MRIA cross-walk carries closure-readiness `high`. Action plans were dated within the last 30 to 60 days; the sustained-operation column is empty or carries "in progress".

Cause: closure-readiness is treated as a status assertion rather than as a sustained-operation claim. Or the pack reads closure-readiness as the bank's confidence in its remediation rather than as the examiner's likely assessment of evidence sufficiency.

Fix: closure-readiness `high` requires a documented sustained-operation period in months. Banks typically use 6 to 12 months internally; the examiner applies judgement on the period and on the evidence quality. Default to `medium` when the sustained-operation period is below the bank's policy threshold; default to `low` when the action plan is dated within the last 30 days. A pack that marks every item closure-ready without sustained-operation evidence triggers examiner skepticism on the entire population, not just on the over-claimed rows. The cross-walk's sustained-operation column carries the period in months and the evidence type (policy update, control implementation, training, system change, sustained-operation observation); empty entries cap the closure-readiness rating at `low`.
