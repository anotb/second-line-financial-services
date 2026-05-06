# Plugin audit memo: payments-fintech-compliance

Date: 2026-05-06
Phase: 1 (scoping pass; no SKILL.md content here).
Status: Spec sheets and overlay snippets drafted. Folder reorganization deferred to phase 3.
Scope: US payments firms, fintechs, money transmitters, sponsor-bank programs, BaaS providers, BIN sponsors, program managers, wallet operators, neobanks, and payments processors.

## v1 skill list (confirmed, no changes from v0.2)

Four retained skills. All four are genuinely sector-unique under the strict sector-overlay rule.

| Skill | Status | Why retained |
|---|---|---|
| `fintech-partner-controls` | Retained | Fintech-side self-evidence pack mapped to Reg E, NACHA, MSB BSA, FBO mechanics, and program-agreement oversight clauses. Different artifact, audience, and statutory frame from the bank-side `third-party-operational-resilience/vendor-diligence` and from `banking/bank-fintech-partnership-review`. |
| `open-banking-data-controls` | Retained | §1033 final rule (October 2024) data-provider and data-recipient duties, FDX-aligned tokenized data sharing, screen-scraping migration. Not produced by any capability skill; payments-fintech-native. |
| `payment-operations-incident-review` | Retained | Rail-specific notification triggers (Reg E timing, NACHA returns / reversals, card-network dispute clocks, FedNow / RTP irrevocability), sponsor-bank-mediated reporting chain, payment-population-denominated customer impact. Distinct from generic incident skills in `risk-compliance-core` / `compliance-testing` and from `risk-reporting/cyber-disclosure-readiness`. |
| `payments-risk-assessment` | Retained | Matrix-shaped artifact denominated by rail, customer segment, and geography with payments-rail-specific failure modes. Different shape from generic enterprise-risk-assessment in `risk-compliance-core/risk-assessment`. |

No deletions. No renames. No additions.

One material content update: `open-banking-data-controls` adds the CFPB Personal Financial Data Rights Final Rule (October 2024, codifying §1033) as the central anchor [verify Federal Register citation, effective date, implementation tiers, and current litigation status as of each engagement date]. The v0.2 spec did not have the final rule; the rule was finalized after v0.2.

## Strict overlay-rule check

Each of the four was tested against the question "is this just a capability skill with payments-fintech examples." None are.

- `fintech-partner-controls`: payments-fintech-only. The closest capability analogs are `third-party-operational-resilience/vendor-diligence` (bank-side, evaluating the fintech) and `banking/bank-fintech-partnership-review` (sponsor-bank principal-side oversight). This skill is the inverse lens: the fintech self-evidencing for production to the sponsor bank or examiner. Boundary call below. Pass.
- `open-banking-data-controls`: payments-fintech-only. No capability skill covers §1033 data-provider / data-recipient duties, FDX-style tokenized data sharing, or screen-scraping migration. The closest capability analogs (`vendor-diligence`, `marketing-claim-review`) do not produce a §1033-aligned controls inventory. Pass.
- `payment-operations-incident-review`: payments-fintech-only. The capability incident pattern in `risk-compliance-core` / `compliance-testing` produces a generic incident write-up; this produces a payments-incident write-up that survives a sponsor-bank notification SLA and a CFPB or state-AG inquiry. Defers cyber-leg disclosure work to `risk-reporting/cyber-disclosure-readiness`. Pass.
- `payments-risk-assessment`: payments-fintech-only. The capability `risk-compliance-core/risk-assessment` is the generic primitive; this produces the rail / segment / geography-denominated matrix. Pass.

All four clear the strict overlay rule.

## Boundary calls documented in spec sheets

- `fintech-partner-controls` vs `banking/bank-fintech-partnership-review`. Both touch the same relationship; the lens differs. `fintech-partner-controls` is the fintech as service provider self-evidencing for the sponsor bank's TPRM file. `bank-fintech-partnership-review` is the bank as supervised principal evidencing its principal-side oversight to its prudential examiner. Different audience (sponsor bank's TPRM team and examiner vs the bank's prudential supervisor), different artifact (controls inventory and self-evidence pack vs principal-side oversight memo), different statutory weight (program-agreement and Interagency TPRM Guidance applied to the fintech vs the same guidance applied to the bank as principal). Both can be in scope on the same engagement, with the artifacts produced separately and reconciled in a coordination log.
- `fintech-partner-controls` vs `third-party-operational-resilience/vendor-diligence`. The capability skill is the bank-side diligence on a fintech vendor; this is the fintech self-evidencing. They chain.
- `payment-operations-incident-review` vs `risk-reporting/cyber-disclosure-readiness`. The payments-incident skill keeps the cyber-leg disclosure work (SEC 8-K Item 1.05, NYDFS §500.17, state breach clocks) as a cross-reference and stays focused on the payments-operational chain.
- `payments-risk-assessment` vs `risk-compliance-core/risk-assessment`. The payments skill produces the rail-by-rail / segment-by-segment / geography-by-geography matrix; the capability skill produces enterprise-risk-assessment scaffolding with overlays. Use the payments skill when payments rails are the dominant axis; use the capability skill with the payments-fintech overlay when the assessment is enterprise-wide (AI risk, model risk, cyber-only, third-party-only).
- `open-banking-data-controls` vs `third-party-operational-resilience/vendor-diligence`. The capability skill covers the aggregator or developer-portal vendor as a vendor-diligence target; this skill covers the §1033 data-flow controls, which sit alongside diligence and evidence different obligations.

## Cross-cutting overlays per skill

| Skill | cyber | privacy | conduct |
|---|---|---|---|
| `fintech-partner-controls` | required (NYDFS Part 500 if covered, GLBA Safeguards passed through program agreement, FFIEC IT booklets, sponsor-bank breach-notification chain) | recommended (GLBA privacy notices, state privacy laws, §1033 implications) | optional (fee disclosure, account closure / hold UDAAP themes, dark-pattern risk; cross-references `udaap-risk-review`) |
| `open-banking-data-controls` | required (NYDFS Part 500 where applicable, FFIEC IT booklets, GLBA Safeguards §314.4 controls, token / key management, AAL / FAPI assurance reasoning) | required (GLBA Privacy Rule / Reg P, CCPA / CPRA and state privacy laws, secondary-use limits, retention and deletion duties under §1033) | recommended (UDAAP exposure on misleading authorization flows, broken revocation paths, post-authorization scope creep) |
| `payment-operations-incident-review` | required (NYDFS Part 500 §500.17(a), SEC cyber 8-K Item 1.05, sponsor-bank cyber-notification SLA, FFIEC incident-response, cross-link to `cyber-disclosure-readiness`) | required where personal data was touched (state breach clocks, GLBA Safeguards §314.4(h), §1033 implications) | recommended where customer-harm patterns map to UDAAP themes |
| `payments-risk-assessment` | required (rails depend on processors, ledger providers, fraud-decision vendors with cyber exposure; NYDFS Part 500 where applicable, GLBA Safeguards, FFIEC IT booklets, sponsor-bank cyber-notification chain) | recommended (customer-data flows for fraud and AML monitoring create privacy and Safeguards exposure beyond baseline) | required (UDAAP on fee disclosure, account closure, holds, Reg E timing, dark patterns; cross-reference `udaap-risk-review`) |

## Capability-skill payments-fintech overlays (drafted as outlines in `overlay-snippets.md`)

Seven capability skills get payments-fintech overlays in v1:

1. `third-party-operational-resilience/vendor-diligence` — Interagency TPRM, July 2024 joint statement, NACHA Third-Party Sender posture, MSB / MTL diligence, BIN-sponsor diligence, fourth-party register specific to payments.
2. `third-party-operational-resilience/exit-plan` — payments-rail wind-down (ACH, Same Day ACH, wire, FedNow, RTP, card, check, cross-border), sponsor-bank termination, customer-transfer mechanics, in-flight-clock preservation.
3. `third-party-operational-resilience/concentration-risk-review` — three axes (sponsor-bank, processor, BIN-sponsor) plus geography overlay.
4. `financial-crime-governance/aml-model-monitoring` — MSB BSA monitoring, payment-channel-specific scenario library, faster-payments-specific signals, ODFI / RDFI risk monitoring posture.
5. `financial-crime-governance/sanctions-screening-qa` — cross-border corridor screening, correspondent-banking exposure, virtual-currency exposure, vendor-tuning QA.
6. `consumer-compliance-fair-lending/udaap-risk-review` — fintech UDAAP themes (account-closure / hold, fee disclosure, FDIC misrepresentation, BNPL, dark patterns, larger-participant rule applicability).
7. `regulatory-change-management/exam-brief` — three-track exam-prep posture (sponsor-bank-led, CFPB-direct under larger-participant rule, state-MTL via NMLS).

Phase 2 contract: each capability-skill spec sheet (written by the capability-plugin lead) must reference the corresponding outline in `overlay-snippets.md` so the phase-2 content writer receives the brief.

## Plugin-level shared references plan

Today, `plugins/sector-plugins/payments-fintech-compliance/references/` holds the boilerplate set common to all sector plugins (output templates, policy control library, public regulatory scenarios, review gates, source map). With four retained skills, the plugin-level references should be tightened.

Recommended posture for phase 2:

- `source-map.md`: keep at plugin level. Curate to the payments-fintech anchor list — Interagency Guidance on Third-Party Relationships (June 6, 2023); OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 2024) [verify date]; Reg E (12 CFR Part 1005) §1005.6 / §1005.11 / §1005.18 / §1005.31 (remittance subpart B); Reg DD (12 CFR Part 1030); Reg II (12 CFR Part 235); Reg Z (12 CFR Part 1026) where credit-side products are in scope; NACHA Operating Rules (current edition, paywalled); card-network rulebooks (current edition, paywalled, conceptual); FedNow Service Operating Procedures; RTP Operating Rules; FFIEC BSA/AML Examination Manual; FinCEN MSB rules at 31 CFR Part 1022; OFAC Compliance Commitments (May 2019) and 31 CFR Part 501; CFPB Personal Financial Data Rights Final Rule under §1033 (October 2024) [verify Federal Register citation and current state]; CFPB larger-participant rule for digital wallets and payment apps (December 2024) [verify Federal Register citation and current state including any litigation or congressional review]; CFPB Circular series [verify current circulars]; CFPB Supervisory Highlights (current cycles); FDIC misrepresentation rule (12 CFR Part 328 Subpart B, May 2022) [verify exact citation]; state Money Transmitter Modernization Act adoption status via NMLS [verify state-by-state]; FFIEC Authentication and Access Guidance (August 2021); GLBA Safeguards Rule (16 CFR Part 314); GLBA Privacy Rule (16 CFR Part 313 / Reg P at 12 CFR Part 1016); NYDFS Part 500; SEC cyber disclosure (Item 1.05 of Form 8-K) [verify exact citations]; state breach-notification statutes; FDX API specification (current major version) [verify version]; NIST SP 800-63B; OAuth 2.0 (RFC 6749) and FAPI 1.0 Final / current profile [verify].
- `policy-control-library.md`: keep at plugin level only if it carries genuinely cross-skill payments-fintech controls (Reg E error-resolution control families, NACHA return-rate-monitoring control families, FBO subledger reconciliation patterns, sponsor-bank-notification SLA patterns, §1033 authorization stack patterns). Otherwise, fold into per-skill references in phase 2.
- `output-templates.md`: deprecate at plugin level. Each retained skill carries its own template under `templates/default-output.md` per the v1 anatomy. Keep this file only if it carries payments-fintech-specific cross-cutting boilerplate (citation block format including the "current edition; verify against firm's licensed copy" disclaimer for paywalled rulebooks; §1033 status note repeating block).
- `review-gates.md`: deprecate at plugin level. Gates are skill-specific; embed in each skill's `SKILL.md`.
- `public-regulatory-scenarios.md`: keep at plugin level as the canonical scenario library so phase 2 example writing reuses scenarios consistently across the four retained skills and the seven overlay snippets. Anchor scenarios to public CFPB consent orders, public OCC / FRB / FDIC enforcement actions, public CFPB Supervisory Highlights, and the 2023-24 sponsor-bank consent-order wave; never name a specific institution as a fact-pattern source.

Phase 2 brief: do not copy plugin-level references into per-skill folders. Per-skill folders carry their own `references/source-anchors.md` with skill-specific citations. Plugin-level references are the cross-skill canonical list.

## Schema ownership

Today, `plugins/sector-plugins/payments-fintech-compliance/schemas/` holds the boilerplate set common to all sector plugins (`obligation`, `control`, `issue`, `ai-use-case`, `vendor`, `test-plan`, `risk-report`). Those schemas are borrowed and belong to other plugins. Recommended posture:

- Move the borrowed schemas back to their owning plugins in phase 3 (`obligation`, `test-plan`, `risk-report` to `risk-compliance-core` or wherever they are owned; `vendor` to `third-party-operational-resilience`; `ai-use-case` to `ai-governance-model-risk`; `control` and `issue` to whichever plugin owns the control / issue primitive). The payments-fintech plugin should reference them, not own them.
- Payments-specific schemas needed in phase 2:
  - `fintech-partner-controls.schema.json`
  - `open-banking-data-controls.schema.json`
  - `payment-operations-incident-review.schema.json`
  - `payments-risk-assessment.schema.json`
- Each is drafted as a `Structured output fields` table in the corresponding spec sheet. Phase 2 turns those tables into JSON schemas.

## Current-state caveats (verify before publishing)

The payments-fintech regulatory pipeline has been unusually active in 2023-2026. Each of the following must be re-verified at engagement-time and the artifact must date-stamp the verification.

- **CFPB Personal Financial Data Rights Final Rule under §1033** — finalized October 2024 [verify Federal Register publication date and exact citation]. The rule has been subject to litigation; tier dates and any stays may have shifted [verify current docket status, any compliance-date relief, and the firm's tier as of each engagement date]. The `open-banking-data-controls` skill carries a mandatory `s1033_status_note` field; this caveat is the operational reason.
- **State Money Transmitter Modernization Act (MTMA) adoption** — state-by-state. NMLS is the licensing system of record for most states. Adoption status varies materially [verify state-by-state adoption status as of each engagement date]. The Multistate MSB Licensing Agreement is the multistate processing channel.
- **OCC / FRB / FDIC Joint Statements on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** — the operative document is the July 25, 2024 joint statement [verify exact date and title]. The 2023 RFI is not the binding statement. Phase 2 cite-checks must catch this conflation.
- **CFPB larger-participant rule for digital wallets and payment apps** — CFPB final rule, December 2024 [verify Federal Register citation, effective date, and current state including any litigation or congressional review]. Direct CFPB supervision applies to designated covered cohort. The `exam-brief` overlay and the `udaap-risk-review` overlay both carry an applicability check.
- **NACHA Operating Rules** — paywalled. Rules cited at conceptual level (return-reason codes, return-rate thresholds, Same Day ACH limits, WEB Debit account-validation, Third-Party Sender registration) require confirmation against the firm's licensed copy of the current edition. The plugin-level boilerplate disclaimer for paywalled rulebooks must be in every artifact.
- **Card-network rules (Visa Core Rules, Visa Product and Service Rules, Mastercard Rules)** — paywalled. Same disclaimer pattern as NACHA.
- **FedNow Service Operating Procedures and RTP Operating Rules** — current versions; verify version date.
- **CFPB Circular series** — supervisory signaling on account-closure / hold, Reg E timing, junk-fees, BNPL, dark patterns, FDIC misrepresentation [verify which circulars are current and which numbers / dates apply on each engagement date].
- **FinCEN MSB rules and administrative rulings** — categorical money-transmitter-status assertions are wrong. The right answer is configuration-specific against the FinCEN administrative-ruling library; phase 2 must hold that discipline.
- **SEC cyber disclosure (Form 8-K Item 1.05)** — relevant where the program operator or its sponsor bank is a public registrant; verify exact citation and the firm's reporting status.
- **Travel Rule threshold** — 31 CFR §1010.410(f) for transmittals of $3,000 or more [verify current threshold; FinCEN has had a proposed rule to lower the threshold; verify status].

## Structural concerns

1. **Sponsor-bank concentration coverage triple-overlap.** Sponsor-bank concentration appears in `payments-risk-assessment` (concentration views section), in `fintech-partner-controls` (program-agreement control map), and in the `concentration-risk-review` payments-fintech overlay. This is correct (different artifacts, different audiences) but phase 2 needs to keep the language consistent across the three so the program operator can see the same metric in three places without contradiction.
2. **§1033 status note repeating block.** The `open-banking-data-controls` skill has a mandatory `s1033_status_note` field plus a "Current-state regulatory frame" output section. The same status-note discipline should propagate into any other artifact that touches §1033 (e.g., a vendor-diligence pack on an aggregator, a §1033-related incident review). Phase 2 should make the status note a shared snippet.
3. **The "fintech UDAAP themes" library is moving fast.** CFPB Supervisory Highlights and consent orders ship continuously. The `udaap-risk-review` overlay should not freeze a theme list; it should cite current cycles and let the plugin's `public-regulatory-scenarios.md` carry the canonical theme library refreshed each cycle.
4. **Money-transmitter-vs-not is configuration-specific.** A common phase-2 failure mode: drafting `fintech-partner-controls` or `payments-risk-assessment` with a categorical "this firm is / is not an MSB" assertion. The right answer is fact-pattern-specific against the FinCEN administrative-ruling library and the state-by-state MTL footprint. The skill outputs must hold that discipline.
5. **Faster-payments rails (FedNow, RTP) change the playbook.** Real-time settlement finality, no chargeback, request-for-return-of-funds as the recovery mechanic, ISO 20022 message-field handling. The four spec sheets all hold this discipline; phase 2 SKILL.md content must carry it through.

## Voice and source-confidence summary

Voice: senior, terse, regulator-aware, practitioner vocabulary. Audience is payments compliance officers, BSA officers at fintechs and MSBs, third-party payment risk teams at sponsor banks, BaaS oversight teams, and payment operations compliance leads. The spec sheets and overlay snippets read like a Big Four payments-regulatory practice or a sponsor-bank TPRM brief, not like product copy.

### Source-anchor confidence per skill

| Skill | Confidence | Notes |
|---|---|---|
| `fintech-partner-controls` | High on Reg E §1005.6 / §1005.11 / §1005.18, Reg DD, Reg II, GLBA Safeguards, Interagency TPRM Guidance (June 2023), and the structural reference to the OCC / FRB / FDIC joint statement. Medium on the exact title / date of the July 2024 joint statement, on NACHA article numbering and current return-rate thresholds (paywalled), on MTMA state-by-state adoption status, and on FinCEN administrative-ruling fact-patterns (configuration-specific). |
| `open-banking-data-controls` | High on GLBA Safeguards (16 CFR Part 314), GLBA Privacy / Reg P, FFIEC Authentication Guidance (August 2021), NIST SP 800-63B, OAuth 2.0 (RFC 6749). Medium on §1033 final-rule details (Federal Register citation, exact tier dates, current litigation status — these must be re-verified each engagement; the rule was finalized October 2024 but the docket has been active). Medium on FAPI profile version cited and FDX major version cited. Medium on which CFPB Circulars in the 2024-26 series directly address §1033 implementation. |
| `payment-operations-incident-review` | High on Reg E §1005.6 / §1005.11 / §1005.18 timing windows, on Interagency TPRM Guidance (June 2023), on NYDFS Part 500 §500.17(a) 72-hour clock. Medium on NACHA return / reversal mechanics and current return-rate thresholds (paywalled, current edition only). Medium on the exact FedNow Service Operating Procedures version and on RTP Operating Rules section references. Medium on SEC 8-K Item 1.05 citation specificity and on which CFPB enforcement actions / Supervisory Highlights are current. Medium on state MTL incident-reporting requirements (state-by-state). |
| `payments-risk-assessment` | High on Reg E, Reg II, Reg DD, FFIEC BSA/AML Examination Manual structure, OFAC framework. Medium on NACHA article numbering and current thresholds (paywalled). Medium on RTP Operating Rules version. Medium on which CFPB enforcement actions, Circulars, and Supervisory Highlights are current. Medium on Reg E §1005.31 remittance-transfer-rule subpart B (high on the rule itself; medium on engagement-time disclosure-timing specifics). Medium on MTMA state-by-state adoption. |

Confidence on the overlay snippets (seven capability skills) is medium-high: the public-source list is well-established, but the live-state caveats (§1033 litigation, larger-participant rule status, MTMA adoption, joint-statement dates) require re-verification at engagement-time and date-stamping in the artifact.

## Phase-3 to-do (for the re-bundle pass)

- Confirm the seven capability-skill payments-fintech overlays exist as `references/sector-overlays/payments-fintech.md` files and contain the substance from the corresponding outline in `overlay-snippets.md`.
- Move borrowed schemas back to their owning plugins; ship the four payments-specific schemas in this plugin.
- Tighten plugin-level shared references in `plugins/sector-plugins/payments-fintech-compliance/references/` per the recommendation above.
- Run `python3 scripts/sync-agent-skills.py` and `python3 scripts/check.py` after the changes.
- Re-verify every `[verify]` marker against the live regulatory state on the date of phase-2 publication. The §1033 status note, the MTMA state-by-state adoption status, the larger-participant rule status, and the OCC / FRB / FDIC joint-statement date are the most-likely points of drift.
