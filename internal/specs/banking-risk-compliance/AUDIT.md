# Plugin audit memo: banking-risk-compliance

Date: 2026-05-06
Status: phase 1 audit, finalized after the lead spec-sheet pass.
Scope: US bank holding companies, national banks, state member banks, state non-member banks, federal and state savings associations, and (where applicable) intermediate holding companies. Primary regulators: OCC, FRB, FDIC, state banking departments, NYDFS for NY-licensed entities.

## v1 skill list (confirmed, no changes)

- `bank-fintech-partnership-review`
- `banking-supervision-readiness`
- `credit-risk-governance`
- `deposit-operations-controls`

All four are genuinely banking-only under the strict sector-overlay rule. Each maps to a workflow shaped by the federal banking statutes and interagency guidance lattice (OCC Comptroller's Handbook, FFIEC manuals, FDIC RMS Manual, FRB BHC Supervision Manual, 12 CFR Parts 30 / 215 / 223 / 229 / 330, Reg E, Reg DD, Bank Service Company Act, Heightened Standards, Joint Agency Statement on Bank-Fintech Arrangements 2024) and not by capability-plugin source material.

## Deletions, renames, additions vs v0.2

None. The v0.2 list was already correctly cut. No skills dropped, no skills added, no renames. The four skills carry forward into v1 unchanged in identity. Spec-sheet content for each was authored fresh in phase 1 against the strict overlay rule.

## Strict overlay rule check

Each skill was tested against the question "is this just a capability skill with banking examples." None are. Reasoning per skill:

- `bank-fintech-partnership-review` — produces the bank's principal-supervised-entity partnership pack: criticality classification under the June 2023 Interagency Guidance, FBO-account governance under the 2024 Joint Agency Statement, Bank Service Company Act §1867(c) examination flow-down, Reg O / Reg W / Reg E / Reg DD applicability split between bank and fintech, and termination / wind-down readiness for sponsor-bank deposit programs. The closest capability analog is `third-party-operational-resilience/vendor-diligence`, but that skill produces generic vendor-diligence output and does not invoke §1867(c), Reg O insider screen on fintech principals, FBO-account ledgering, pass-through deposit-insurance recordkeeping, or the BaaS-program criticality lattice. Pass.
- `banking-supervision-readiness` — produces the CAMELS-component readiness pack, MRA / MRIA closure cross-walk, Heightened Standards (12 CFR Part 30 Appendix D) readiness for covered banks, and BHC supervisory cycle (FRB SR 12-17) preparation. The closest capability analog is `regulatory-change-management/exam-brief`, but that skill is regulator-agnostic and does not organize around CAMELS, BHC rated components, MRA / MRIA aging, or Heightened Standards. The two chain (the capability skill is the generic engagement playbook; this skill is the deeper banking-specific artifact). Pass.
- `credit-risk-governance` — produces the second-line credit-governance memo: credit-policy alignment to Comptroller's Handbook expectations, risk-rating discipline under Interagency Guidance on Credit Risk Review Systems (May 2020), CRE concentration governance under the 2006 Interagency CRE guidance and 2015 statement, ACL / CECL methodology oversight, and Reg O / Reg W applicability. No capability skill covers safety-and-soundness credit governance. Distinct from `consumer-compliance-fair-lending` (different statutory frame: 12 USC §1818 safety-and-soundness vs ECOA / Reg B / FHA). Pass.
- `deposit-operations-controls` — produces the deposit-operations control matrix mapping to Reg E §1005, Reg DD §1030, Reg CC Part 229, CIP under 31 CFR §1020.220, beneficial-ownership under 31 CFR §1010.230, FBO-account ledgering under the 2024 Joint Agency Statement, and pass-through deposit-insurance recordkeeping under 12 CFR Part 330. The closest capability analog is `risk-compliance-core/control-matrix`, but that skill is a generic control-matrix shell. Banking deposit-ops cannot be faithfully produced from generic controls without the regulation-specific row vocabulary. Pass.

All four clear the strict overlay rule: their statutory frame, audience, and artifact are banking-specific and do not duplicate any capability skill.

## Boundary calls documented in spec sheets

- `bank-fintech-partnership-review` vs `payments-fintech-compliance/skills/fintech-partner-controls` — bank-side partnership pack vs fintech-side bank-program controls. Documented in both "Not the right tool when" sections. Each is a distinct artifact with a distinct audience (bank CRO and OCC examiner-in-charge vs fintech CCO and bank-program-management contact).
- `bank-fintech-partnership-review` vs `third-party-operational-resilience/vendor-diligence` (banking overlay) and `exit-plan` (banking overlay) — full partnership pack with §1867(c) and Reg O / Reg W / Reg E / Reg DD coverage vs generic vendor-diligence or exit-plan with banking flavor. The partnership review is the consolidated artifact; the capability skills with overlays are the individual diligence and exit components.
- `banking-supervision-readiness` vs `regulatory-change-management/exam-brief` (banking overlay) — CAMELS-component readiness, MRA / MRIA closure cross-walk, BHC SR 12-17 preparation, Heightened Standards readiness vs generic exam-brief engagement playbook. The capability skill (with banking overlay) covers entry-meeting protocol, document-handling, and request-letter format; this skill carries the deeper readiness substance. The two chain.
- `credit-risk-governance` vs `consumer-compliance-fair-lending` skills — safety-and-soundness lens (underwriting, rating, ALLL, concentration, insider) vs fair-lending lens (ECOA, FHA, Reg B, HMDA, Section 1071). Complementary, not duplicative.
- `credit-risk-governance` vs `ai-governance-model-risk/validation-plan` — second-line oversight of model use within the credit framework (methodology approval, qualitative-factor governance, rating-migration linkage) vs model-validation work itself. Don't replicate validation here.
- `deposit-operations-controls` vs `bank-fintech-partnership-review` — control matrix once a sponsor-bank partnership is approved or under operational review vs partnership-level review of the fintech relationship. Documented.
- `deposit-operations-controls` vs `risk-compliance-core/control-matrix` (banking overlay) — deposit-ops-anchored matrix with full Reg E / Reg DD / Reg CC / CIP / BO / FBO row vocabulary vs generic control-matrix shell with banking row patterns. The capability skill remains generic; the banking flavor lives in the overlay; the deposit-ops matrix is the deep deposit-anchored artifact.

## Banking sector overlays for capability skills

Drafted in `overlay-snippets.md`. Phase 2 builds these as `references/sector-overlays/banking.md` files inside the named capability skills. Coverage:

- `third-party-operational-resilience/vendor-diligence` — Interagency Guidance June 2023 (OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) risk-based lifecycle, OCC Bulletin on Bank-Fintech Arrangements [verify bulletin number], 2024 Joint Agency Statement on Bank-Fintech Arrangements, §1867(c) examination flow-down, Reg O insider screen on vendor principals, Heightened Standards covered-bank evidence, AI-vendor mode tied to OCC Bulletin 2026-13.
- `third-party-operational-resilience/exit-plan` — Interagency Guidance §III.F termination [verify section label], FBO-account wind-down sequence, Reg DD §1030.5 / Reg E §1005.8 customer-notification, §1867(c) examination-access continuity, FDIC consultation in stressed-exit scenarios.
- `risk-compliance-core/control-matrix` — Heightened Standards §III risk-governance-framework integration, FFIEC IT Information Security booklet rows, BSA/AML row expectations (CIP, CDD, BO, suspicious-activity, CTR, OFAC), Call Report / UBPR evidence pointers, CRA-modernization-rule-status caveat for fair-lending and CRA control coverage.
- `risk-reporting/risk-committee-pack` — 12 CFR Part 30 Appendix D §III.B risk-appetite, interagency-defined risk types (credit, market, liquidity, operational, compliance, strategic, reputational, model, plus cyber, third-party, financial crime), BHC SR 12-17 cycle integration, MRA / MRIA standing section, capital-planning content (DFAST / CCAR for applicable BHCs), LCR / NSFR liquidity content, three-lines-of-defense maturity reporting.
- `regulatory-change-management/exam-brief` — banking exam types (OCC full-scope, FRB BHC supervisory, FDIC risk-management, FFIEC BSA/AML, FFIEC IT, OCC and FDIC consumer-compliance, CRA performance evaluation), CAMELS-component organization, BHC rated components vs depository CAMELS, MRA / MRIA framework, examiner entry-meeting protocols, explicit pointer to `banking-supervision-readiness` for full preparation.
- `financial-crime-governance/edd-escalation-pack` (overlay note) — banking-specific escalation paths (BSA officer to CRO to board), fintech-partner customer treatment, sponsor-bank-program end-user-customer treatment, USA PATRIOT Act §326 CIP-program governance integration. Decision on whether to ship stays with the financial-crime-governance lead.
- `financial-crime-governance/sanctions-screening-controls` (overlay note, if present) — banking-specific OFAC examiner expectations, correspondent-banking screening (12 CFR §1010.610 [verify]), sponsor-bank-program OFAC flow.

Phase 2 contract: each capability-skill spec sheet (written by the capability-plugin lead) must reference the corresponding outline in `overlay-snippets.md` so the phase-2 content writer receives the brief. The bank-fintech-arrangement substance is concentrated in `bank-fintech-partnership-review`; the overlays cite back to the sector-plugin skill rather than duplicating the deep artifact.

## Plugin-level shared references plan

Today, `plugins/sector-plugins/banking-risk-compliance/references/` carries the v0.2 inheritance: `output-templates.md`, `policy-control-library.md`, `public-regulatory-scenarios.md`, `review-gates.md`, `source-map.md`. With four banking-only skills retained, posture for phase 2:

- `source-map.md` — keep at plugin level. Curate to the banking-specific anchor list (Interagency Guidance June 2023, OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, OCC Bulletin on Bank-Fintech Arrangements [verify], 2024 Joint Agency Statement on Bank-Fintech Arrangements, Bank Service Company Act 12 USC §1867(c), 12 CFR Part 30 Appendix D, 12 CFR Parts 215 / 223 / 229 / 330, 31 CFR Parts 1010 / 1020, Reg E 12 CFR Part 1005, Reg DD 12 CFR Part 1030, Reg P 12 CFR Part 1016, Comptroller's Handbook booklets, FFIEC BSA/AML Manual, FFIEC IT Examination Handbook, FDIC RMS Manual, FRB BHC Supervision Manual, FRB SR 12-17, FRB SR letters on MRA / MRIA framework [verify SR 13-17 / SR 22-3], Interagency CECL guidance, Interagency CRE Concentration Guidance 2006 + 2015 statement, Interagency Guidance on Credit Risk Review Systems May 2020, NYDFS 23 NYCRR Part 500). Date every citation.
- `policy-control-library.md` — keep at plugin level only if it carries genuinely cross-skill banking controls (e.g., Heightened Standards §III risk-governance-framework rows, three-lines-of-defense scaffolding, BSA/AML CIP / CDD / BO core controls reused across deposit-ops and partnership-review). Otherwise fold into per-skill references in phase 2.
- `output-templates.md` — deprecate at plugin level. Each retained skill carries its own template under `templates/default-output.md` per the v1 anatomy. Keep only if it carries banking-specific cross-cutting boilerplate (disclaimer language, source-trace block format, sign-off block format).
- `review-gates.md` — deprecate at plugin level. Gates are skill-specific in v1; embed in each skill's `SKILL.md`.
- `public-regulatory-scenarios.md` — keep at plugin level as the canonical scenario library. Phase 2 example writing reuses scenarios consistently across the four retained skills and the seven overlay outlines (BaaS sponsor-program scenarios, midsize OCC-regulated national bank under Heightened Standards, state member bank under FRB consent order, community bank with CRE concentration above 300%, FDIC-regulated state non-member bank with sponsor-bank FBO program).

Phase 2 brief: do not copy plugin-level references into per-skill folders. Per-skill folders carry their own `references/source-anchors.md` with skill-specific citations; plugin-level references are the cross-skill canonical list.

## Schema ownership

Borrowed schemas presently in `schemas/` (`obligation`, `control`, `issue`, `ai-use-case`, `vendor`, `test-plan`, `risk-report`) belong to other plugins (`risk-compliance-core`, `ai-governance-model-risk`, `third-party-operational-resilience`, `compliance-testing`, `risk-reporting`) and should be removed in phase 3 once the owning plugins ship them. Banking-specific schemas needed in phase 2:

- `bank-fintech-partnership.schema.json` (wrapper around `vendor.schema.json`)
- `supervision-readiness.schema.json` (reuses `issue.schema.json` and `control.schema.json`)
- `credit-risk-governance-review.schema.json` (reuses `obligation.schema.json`, `control.schema.json`, `issue.schema.json`)
- `deposit-operations-matrix.schema.json` (extends `control.schema.json`)

Phase-3 to-do: confirm the four capability-owned schemas are imported via plugin reference rather than copied.

## Current-state caveats (verify before publishing)

The banking regulatory pipeline carries several moving pieces. Each spec sheet flags `[verify]` markers where confidence is below high. Items the phase-2 author must resolve against current public sources before any SKILL.md ships:

- **CRA modernization rule.** The 2023 final CRA rule has been subject to legal challenge. The plugin source list and overlay outlines reference CRA but flag the modernized rule as `[verify current effective state given litigation history]`. Phase-2 writers must pin the operative rule (1995 framework vs 2023 modernized rule) at write time.
- **OCC Heightened Standards (12 CFR Part 30 Appendix D).** Section labels (II covered bank, III risk governance framework, III.B risk appetite, IV board's role) are referenced throughout but flagged `[verify section labels]` because the published Appendix uses section letters without the III.B-style sub-numbering used colloquially. Phase-2 writers cite the Appendix D text directly.
- **OCC, FDIC, FRB joint statements on bank-fintech.** The 2024 Joint Agency Statement on Bank-Fintech Arrangements is cited across the spec sheets with `[verify exact title and date]` and `[verify bulletin number]` placeholders. The OCC has issued multiple BaaS-relevant bulletins post-2023; phase-2 writers must pin the bulletin number and effective date before publishing. The OCC Bank-Fintech Request for Information (July 2024) and any subsequent guidance also need current-state confirmation.
- **FRB SR letters on MRA / MRIA framework.** SR 13-17 and SR 22-3 are referenced as governing the MRA / MRIA framework with `[verify]`. Phase-2 writers confirm which SR letters define and govern the framework today.
- **Comptroller's Handbook booklet editions.** Multiple booklets cited (Bank Supervision Process, Third-Party Relationships, Loan Portfolio Management, Commercial Lending, Retail Lending, Allowances for Credit Losses, Concentrations of Credit, Rating Credit Risk, Capital and Dividends, Liquidity, Earnings, Interest Rate Risk, Bank Operations, Internal Control, Deposit-Related Credit) carry `[verify current edition]` markers because booklets are revised periodically. Pin edition dates in source traces.
- **FFIEC Examination Modernization Project.** Initiatives evolve. Mark `[verify current state]` when the pack relies on a specific Modernization Project deliverable.
- **CECL implementation guidance.** ASC 326-20 is binding; the 2016 / 2017 / 2019 interagency joint statements need `[verify final post-CECL state]` confirmation.
- **FinCEN beneficial-ownership rule under the Corporate Transparency Act.** 31 CFR §1010.230 (bank BO rule for legal-entity customers) and the FinCEN BO reporting rule under the CTA are distinct regimes; CTA litigation history affects current state. Phase-2 writers carry the `[verify current state of FinCEN BO rule and CTA litigation]` marker.
- **Climate-related financial-risk supervision.** Evolving. The four spec sheets do not embed climate as a v1 cross-cutting overlay; supervision-readiness carries it as a `[verify current state]` reviewer question.
- **Heightened Standards $50B threshold.** Stable threshold but verify against any post-EGRRCPA tailoring framework changes for borderline institutions.

## Source-anchor confidence per skill

| Skill | Confidence | Notes |
|---|---|---|
| bank-fintech-partnership-review | High on Interagency Guidance June 2023 lifecycle, §1867(c) examination authority, Reg O 12 CFR Part 215 sections, Reg W 12 CFR Part 223 sections, Reg E §1005.2 / §1005.6 / §1005.7 / §1005.11, Reg DD §1030.4 / §1030.8. Medium on 2024 Joint Agency Statement title and date, OCC Bulletin number on Bank-Fintech Arrangements, OCC Bank-Fintech RFI subsequent guidance form. Low on the precise mapping between FBO-account expectations and the §330 pass-through deposit-insurance recordkeeping detail at the sponsor-bank-program level (the bank-side recordkeeping path is well-defined; the contractual flow-down to the fintech is supervisory-guidance shaped, not regulation shaped). |
| banking-supervision-readiness | High on CAMELS framework, FDIC RMS Manual §5.1, FRB SR 12-17 consolidated supervision framework. Medium on FDIC Manual section labels (1.1, 4.1, 5.1, 6.1, 7.1, 8.1, 3.7) where section numbering can drift between editions. Medium on FRB SR letter numbers governing MRA / MRIA framework (SR 13-17 / SR 22-3 flagged [verify]). Medium on Comptroller's Handbook current-edition dates across multiple booklets. Medium on FFIEC Examination Modernization Project current effective initiatives. Medium on Heightened Standards §III / §IV section labels. |
| credit-risk-governance | High on Reg O 12 CFR Part 215 section structure (§215.3, §215.4, §215.5, §215.7, §215.8, §215.9), Reg W 12 CFR Part 223 covered-transaction structure (§223.11–§223.16), Interagency CRE Concentration Guidance December 2006 100%/300% trigger, ASC 326-20 CECL standard. Medium on Interagency Guidance on Credit Risk Review Systems May 2020 replacing OCC Bulletin 2006-47 (replacement confirmed; cite text needs phase-2 verification). Medium on continued effectiveness of FRB SR 06-17 post-CECL. Medium on Comptroller's Handbook current-edition dates for Loan Portfolio Management, Commercial Lending, Retail Lending, Allowances for Credit Losses, Concentrations of Credit, Rating Credit Risk. |
| deposit-operations-controls | High on Reg E 12 CFR Part 1005 section structure (§1005.2, §1005.6, §1005.7, §1005.10, §1005.11, §1005.13, §1005.18), Reg DD 12 CFR Part 1030 section structure (§1030.3, §1030.4, §1030.5, §1030.8, §1030.9), Reg CC 12 CFR Part 229 subpart structure, 31 CFR §1020.220 CIP rule. Medium on FFIEC IT Examination Handbook Retail Payment Systems booklet current edition. Medium on 12 CFR Part 330 section labels for pass-through deposit-insurance recordkeeping (§330.5 referenced [verify section]). Medium on 2024 Joint Agency Statement on Bank-Fintech Arrangements title and date. Medium on FinCEN BO rule current state under CTA litigation context. |

## Phase-3 to-do (for the re-bundle pass)

- Confirm the seven capability-skill banking overlays exist as `references/sector-overlays/banking.md` and contain the substance from the corresponding outline in `overlay-snippets.md`.
- Confirm plugin-level shared references in `plugins/sector-plugins/banking-risk-compliance/references/` are tightened per the recommendation above.
- Remove borrowed schemas (`obligation`, `control`, `issue`, `ai-use-case`, `vendor`, `test-plan`, `risk-report`) from `plugins/sector-plugins/banking-risk-compliance/schemas/` once the four owning capability plugins ship them.
- Add the four banking-specific schemas listed above.
- Resolve every `[verify]` placeholder in spec sheets and overlay outlines before any SKILL.md publishes.
- Run `python3 scripts/sync-agent-skills.py` and `python3 scripts/check.py` after the changes.
