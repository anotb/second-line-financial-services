# deposit-operations-controls — spec sheet

Plugin: `banking-risk-compliance`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Drafts the second-line risk-control matrix for a US bank deposit operations function: account opening and CIP, beneficial-ownership collection, exception handling, ATM and EFT processing under Reg E, deposit-account disclosures and advertising under Reg DD, holds and Reg CC funds availability, reconciliation and ledgering (including FBO accounts for sponsor-bank programs), access controls, and evidence retention. Output is a deposit-operations-anchored control matrix that a deposit-ops manager, compliance officer, internal auditor, or examiner can read line-by-line.

Best for:
- A bank is standing up or refreshing the deposit-operations control framework after a process change, system migration, or examiner finding.
- A bank's deposit-operations team is preparing for an OCC, FDIC, or FRB compliance examination scope (Reg E, Reg DD, Reg CC, BSA/AML CIP) and needs the control matrix that aligns evidence to obligation.
- A bank is integrating a new fintech sponsor-program FBO account flow and needs the deposit-operations control overlay specific to ledgering and reconciliation against the FBO.
- A bank is responding to an internal-audit finding on deposit-account opening, CIP completeness, or Reg E error-resolution timing.

Not the right tool when:
- The work is the partnership-level review of a fintech relationship (use `bank-fintech-partnership-review`); this skill produces the operations-control matrix once the partnership is approved or under review.
- The work is the BSA/AML risk assessment of a customer base or the CDD program design (use `financial-crime-governance` skills); CIP control activities are in scope here, but not the BSA/AML risk assessment.
- The work is generic risk-control matrix design for a non-deposit process. Use `risk-compliance-core/skills/control-matrix` with the banking sector overlay.
- The work is fair-lending review on overdraft programs or fees. Use consumer-compliance-fair-lending skills.

Anchored to: OCC Comptroller's Handbook — Deposit-Related Credit, Retail Nondeposit Investment Products, Bank Operations [verify booklet titles and editions]; FDIC Risk Management Manual of Examination Policies §3.7 (Other Operational Risks) [verify section]; FFIEC BSA/AML Examination Manual — Customer Identification Program, Customer Due Diligence, Beneficial Ownership Requirements for Legal Entity Customers (current edition); 31 CFR 1020.220 (CIP for banks); 31 CFR 1010.230 (beneficial-ownership rule, as amended by the Corporate Transparency Act and FinCEN's beneficial-ownership rule [verify current state]); Regulation E, 12 CFR Part 1005, especially §1005.6 (consumer liability), §1005.7 (initial disclosures), §1005.10 (preauthorized transfers), §1005.11 (error resolution), §1005.18 (prepaid accounts); Regulation DD, 12 CFR Part 1030, especially §1030.4 (account disclosures), §1030.5 (subsequent disclosures), §1030.8 (advertising); Regulation CC, 12 CFR Part 229, especially Subpart B (funds availability) and Subpart C (collection of checks); FFIEC IT Examination Handbook — Retail Payment Systems booklet [verify current edition] for ATM, EFT, and ACH operational expectations; Joint Agency Statement on Bank-Fintech Arrangements (FDIC / OCC / FRB, 2024) [verify exact title and date] for FBO-account ledgering and reconciliation in sponsor-bank programs.

## Source anchors

Primary:
- FFIEC BSA/AML Examination Manual — Customer Identification Program section. Use for: CIP control activities (verification methods, documentary vs non-documentary, government-list checks, recordkeeping).
- FFIEC BSA/AML Examination Manual — Customer Due Diligence and Beneficial Ownership Requirements for Legal Entity Customers section. Use for: BO collection at account opening, certification, recordkeeping.
- 31 CFR 1020.220 — CIP rule for banks. Sections to cite: (a)(2) identity verification procedures, (a)(3) recordkeeping, (a)(4) comparison with government lists, (a)(5) customer notice. Use for: required-elements checklist on the account-opening control.
- 31 CFR 1010.230 — beneficial-ownership rule for legal entity customers. Use for: BO control at account opening; cross-reference with the FinCEN beneficial-ownership reporting rule under the Corporate Transparency Act for the post-2024 state [verify current state].
- Regulation E, 12 CFR Part 1005. Sections to cite: §1005.2(b) and (i) (definitions), §1005.6 (consumer liability for unauthorized transfers), §1005.7 (initial disclosures), §1005.10 (preauthorized transfers), §1005.11 (error resolution and procedures), §1005.18 (prepaid accounts). Use for: ATM and EFT operational controls, error-resolution timing, provisional-credit governance, prepaid-account-specific controls.
- Regulation DD, 12 CFR Part 1030. Sections to cite: §1030.3 (general disclosure requirements), §1030.4 (account disclosures content and timing), §1030.5 (subsequent disclosures, fee changes), §1030.8 (advertising). Use for: account-opening disclosure controls, advertising review, APY accuracy.
- Regulation CC, 12 CFR Part 229. Sections to cite: Subpart B (especially §229.10 next-day availability, §229.12 schedule, §229.13 exceptions), Subpart C (collection of checks). Use for: funds-availability control, hold-policy disclosures, exception-hold governance.
- Comptroller's Handbook — Bank Operations [verify current title and edition]. Use for: deposit-operations process expectations, segregation of duties, reconciliation, exception handling.
- Comptroller's Handbook — Internal Control [verify current edition]. Use for: control framework expectations applicable to deposit operations.
- FFIEC IT Examination Handbook — Retail Payment Systems booklet [verify current edition]. Use for: ATM, EFT, ACH operational and IT-control expectations.
- Joint Agency Statement on Bank-Fintech Arrangements (FDIC/OCC/FRB, 2024) [verify title and date]. Use for: FBO-account ledgering, daily reconciliation control, end-user beneficial-ownership clarity in sponsor-bank deposit programs.
- FDIC Risk Management Manual of Examination Policies §3.7 [verify section] and §6.1 (Liquidity, deposit-funding) [verify section]. Use for: deposit-operations operational-risk and liquidity-linked control expectations.
- Federal Deposit Insurance Act and FDIC's regulations on insurance-eligibility of deposit accounts (12 CFR Part 330). Use for: FBO-account pass-through deposit-insurance control (recordkeeping requirements for fiduciary and custodial accounts).

Secondary (overlay only):
- Comptroller's Handbook — Custody Services [verify], for custodial and fiduciary deposit-account control overlap.
- Reg E small-entity compliance guide (CFPB) [verify current edition], as a plain-language interpretive aid (cite the underlying §1005 section, not the guide).
- FFIEC IT Examination Handbook — Wholesale Payment Systems booklet [verify], where deposit operations include wholesale wire processing.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards) for covered banks where deposit-operations risk feeds the operational-risk and risk-governance framework.

Public enforcement reference set:
- OCC, FDIC, FRB published consent orders against banks involving deposit-operations control weaknesses (Reg E error-resolution failures, Reg DD APY misrepresentation, FBO-account ledgering failures in sponsor-bank programs) [reference by published case docket; do not invent facts].
- CFPB consent orders against banks for Reg E and Reg DD violations [reference by published case docket].

## Sector overlays needed

This skill is banking-sector-only by definition. No `references/sector-overlays/` subfolder.

## Cross-cutting overlays needed

- `cyber.md` — Required. Deposit-operations systems are cyber- and fraud-exposed (ATM-network, online-banking authentication, ACH origination). Anchors: FFIEC IT booklet (Information Security, Retail Payment Systems), NYDFS Part 500 §500.11 third-party service providers, GLBA Safeguards Rule.
- `privacy.md` — Required. Deposit operations handles consumer financial information. Anchors: GLBA Privacy Rule (Reg P, 12 CFR 1016), GLBA Safeguards Rule (16 CFR 314.4), state privacy laws.
- `conduct.md` — Required where the matrix covers customer-facing deposit-operations decisions (overdraft programs, fee assessment, hold practices, dispute handling). Anchors: CFPB UDAAP exam manual.
- `climate.md` — Not required at v1.

## Output template named sections

Top of artifact:
- Scope and source posture (institution type, primary federal regulator, asset size band, Heightened Standards applicability, deposit-operations scope [retail, business, wealth-deposit, sponsor-bank-program], system landscape, source posture)
- Confidence label
- Reviewer questions

Body — the matrix itself, organized by deposit-operations process area, with each row carrying the standard control-matrix columns (obligation source, control objective, control activity, control owner, frequency, test method, evidence pointer, last test result, design effectiveness, operating effectiveness, open issues, human review required) plus deposit-operations-specific cross-walks. Process areas:

1. **Account opening and CIP**
   - Identity verification (documentary / non-documentary)
   - Government-list comparison
   - Customer notice (§1020.220(a)(5))
   - Recordkeeping (§1020.220(a)(3))

2. **Beneficial-ownership collection**
   - Trigger identification (legal-entity customers, CTA reporting-company status overlap [verify current state of FinCEN BO rule and CTA litigation])
   - Certification collection
   - Refresh on triggering events
   - Recordkeeping

3. **Account-opening disclosures (Reg DD)**
   - §1030.4 disclosure content control
   - Disclosure-timing control (before account opening)
   - Disclosure-medium control (electronic / paper)
   - Subsequent-disclosure control (§1030.5)

4. **Advertising review (Reg DD)**
   - §1030.8 ad-content review
   - APY-accuracy control
   - Sponsor-bank-program advertising approval gate (where applicable)

5. **EFT and ATM operations (Reg E)**
   - Initial-disclosures control (§1005.7)
   - Receipts and periodic statements (§1005.9)
   - Preauthorized-transfer authorizations (§1005.10)
   - Error-resolution intake control (§1005.11)
   - Provisional-credit timing control (§1005.11(c))
   - Investigation-completion control (§1005.11(c) and (d))
   - Notification-of-results control (§1005.11(d) and (e))
   - Consumer-liability application control (§1005.6)
   - Prepaid-account-specific controls (§1005.18) where applicable

6. **Funds availability (Reg CC)**
   - Hold-policy disclosure control
   - Hold-application control (general schedule, exceptions)
   - Exception-hold notification control (§229.13(g))
   - Disclosure-update control on hold-policy changes

7. **Reconciliation and ledgering**
   - Daily ledger-to-GL reconciliation
   - Variance investigation and aging
   - FBO-account end-user ledger reconciliation (where applicable; tied to Joint Agency Statement on Bank-Fintech Arrangements expectations)
   - Pass-through deposit-insurance recordkeeping (12 CFR Part 330) where the FBO supports custodial deposits

8. **Exception handling and overrides**
   - Exception definition by category
   - Override authority matrix
   - Aggregate exception reporting cadence
   - Linkage to UDAAP screen on overrides that affect customers

9. **Access controls and segregation of duties**
   - Privileged-access governance for deposit systems
   - Joint-action requirements for high-risk transactions (large dormant-account reactivation, fraud-loss writeoffs)
   - Periodic access-recertification

10. **Evidence retention**
    - Retention schedule alignment with 31 CFR §1020.220(a)(3), 12 CFR §1005.13 (Reg E records), 12 CFR §1030.9 (Reg DD records), 12 CFR §229.21 (Reg CC records)
    - System-of-record evidence pointers
    - Litigation-hold and exam-evidence preservation overlay

Tail of artifact:
- Coverage gaps (obligations with no mapped control)
- Control redundancies
- Cross-references to obligations in `risk-compliance-core/skills/obligation-mapping` and issues in `risk-compliance-core/skills/issue-writeup`
- Heightened Standards posture (covered banks): tie of deposit-ops controls into the operational-risk and risk-governance framework
- Recommended owner actions
- Source trace
- Sign-off block

## Structured output fields

Phase 2 adds `schemas/deposit-operations-matrix.schema.json`, extending `control.schema.json`.

Wrapper object:
- `matrix_id`: string.
- `institution`: object. Same fields as in supervision-readiness wrapper.
- `scope`: object. `deposit_operations_scope` (array of enums: `retail-deposit`, `business-deposit`, `wealth-deposit`, `sponsor-bank-program`), `systems_in_scope` (array of strings), `process_change_trigger` (enum: `policy-refresh`, `system-migration`, `examiner-finding`, `audit-finding`, `partnership-change`, `routine-refresh`).
- `process_areas`: array of objects, one per process area listed above, each with `area_name` (string), `controls` (array of `control.schema.json` objects), `coverage_gaps` (array), `redundancies` (array).
- `obligations_in_scope`: array of obligation_id strings (foreign keys to `obligation.schema.json`).
- `fbo_overlay`: optional object for sponsor-bank-program scope. `daily_reconciliation_control_id` (string), `pass_through_deposit_insurance_status` (enum: `documented`, `partial`, `not-applicable`, `gap`), `end_user_ledger_governance` (string).
- `cross_cutting_findings`: object with `cyber` (array), `privacy` (array), `conduct` (array).
- `heightened_standards`: optional object for covered banks.
- `recommended_owner_actions`: array.
- `confidence_label`: enum.
- `human_review_required`: boolean. Always true for v1.

## Example scenarios

### Scenario 1: Reg E error-resolution control refresh after an internal-audit finding

Input: a midsize bank ($12B assets, OCC-regulated national bank) had an internal-audit finding that 7% of consumer EFT error-resolution cases breached the §1005.11 timing on provisional credit (10 business days from notice for unauthorized transfer claims, 5 business days for some POS/foreign cases). The deposit-operations director needs the second-line control-matrix refresh for the EFT and ATM operations process area, ahead of the audit-committee follow-up.

Output emphasizes:
- Process area: EFT and ATM operations (Reg E §1005.11) — eight rows, one per Reg E §1005.11 control activity (intake, classification, provisional-credit determination, investigation, notification, consumer-liability calculation, recordkeeping, periodic-trend monitoring).
- Control objective on §1005.11(c) provisional credit: the bank credits the consumer's account within 10 business days (or as applicable) when a complete error notice is received and investigation is not concluded.
- Control activity: deposit-operations dispute team uses the dispute-management system, which auto-classifies the claim category at intake and triggers a 10-business-day SLA. Manual override exists for cases reclassified after intake.
- Evidence pointer: dispute-management-system case-aging report; sample list and reviewer-signoff log.
- Last test result: internal audit found 7% breach rate; root cause was reclassification cases reset the SLA clock incorrectly when escalated.
- Design effectiveness: operating but with design weakness on the reclassification path.
- Open issues: linked to issue-writeup ID.
- Recommended action: deposit-operations director to ship a system fix for SLA-clock continuity on reclassification within 60 days; second-line monitoring control to add weekly aging-by-classification view.
- Cross-cutting findings: conduct overlay row — UDAAP exposure from delayed provisional credit; recommend a customer-make-good policy for breach cases.
- Coverage gaps: prepaid-account controls (§1005.18) absent — out of scope (the bank does not issue prepaid accounts); flagged as not applicable.
- Confidence: high on the control-objective wording (driven by §1005.11 text), medium on operating effectiveness pending the system fix.
- Heightened Standards: not applicable (asset size below $50B).
- Public-source basis: anchored to 12 CFR §1005.11(c)–(e), §1005.6, §1005.13. Anonymous; no named institutions.

### Scenario 2: FBO-account ledgering control overlay for a sponsor-bank deposit program

Input: a community bank ($5B assets, FDIC-regulated state non-member bank) operates a sponsor-bank deposit program with three fintech partners. The bank holds deposits in three FBO accounts, one per partner. The board's audit committee requested a second-line control-matrix overlay for the FBO-account ledgering process after a peer bank consent order on FBO reconciliation failures was published. Source posture: Joint Agency Statement on Bank-Fintech Arrangements 2024 plus internal policy.

Output emphasizes:
- Process area: reconciliation and ledgering, with FBO overlay.
- Pass-through deposit-insurance control: §330.5 [verify section] recordkeeping requirements for fiduciary and custodial accounts; the bank's custodial-account agreement and the fintech partner's end-user ledger satisfy the recordkeeping requirements for two of three programs; one program lacks a daily snapshot of end-user balances at the bank's level (the bank receives an end-of-day file from the fintech but does not retain daily snapshots for the required period). Gap flagged.
- Daily reconciliation control: bank reconciles total FBO balance at the bank to total of fintech-reported end-user ledger daily; variance threshold is set at $1k. Reviewer question on whether the variance threshold is risk-based; for one program with $300M in deposits, $1k threshold may be too tight and generate noise; for another with $20M in deposits, may be too loose.
- End-user ledger governance: each fintech is required to provide weekly attestations on ledger accuracy; reviewer question on whether attestations are signed by an officer with adequate authority and independence at the fintech.
- Cyber overlay: NYDFS Part 500 §500.11 third-party service-provider security policy maps to fintech partner; SOC 2 Type II controls received and reviewed within last 12 months for each partner; one program has a SOC 2 with a control gap on logical access reviews — issue-writeup linked.
- Privacy overlay: GLBA Reg P notice integration with each fintech; reviewer question on whether the privacy notice issued to consumers correctly identifies the bank as the financial institution.
- Coverage gaps: no documented exit-sequence control for FBO wind-down (the bank has not tabletop-tested an FBO deconversion); cross-reference to `bank-fintech-partnership-review` recommendation.
- Recommended owner actions: deposit-operations director to retain daily end-user balance snapshots for the third program within 30 days; risk officer to refresh variance thresholds on a risk-based basis; head of vendor management to schedule an FBO wind-down tabletop within 90 days.
- Confidence: high on §330 recordkeeping; medium on variance-threshold calibration; low on end-user ledger governance pending the third-program fix.
- Heightened Standards: not applicable.
- Public-source basis: anchored to 12 CFR Part 330 [verify section], Joint Agency Statement on Bank-Fintech Arrangements 2024, FFIEC BSA/AML manual CIP and CDD sections. Anonymous; consent-order reference by docket only.

## Common pitfalls

1. **Confusing Reg E §1005.11 timing with the underlying transaction limits in §1005.6.** §1005.11 governs error-resolution timing (when the bank must investigate, provisionally credit, and notify). §1005.6 governs consumer liability for unauthorized EFTs (the $50/$500/unlimited tiers based on timeliness of consumer notice). The matrix must keep them in separate rows even though they often surface in the same dispute case.
2. **Treating the FFIEC BSA/AML manual as the only CIP source.** The manual is interpretive guidance built on top of 31 CFR §1020.220 and the BSA. The matrix must cite the regulation, not just the manual; the manual cite goes to the secondary anchor row.
3. **Missing the §1005.18 prepaid-account scope when the bank issues prepaid products.** Prepaid is a discrete Reg E sub-regime with its own initial-disclosure short form and pre-acquisition disclosures. Don't fold prepaid into general EFT controls; carve it out.
4. **Treating Reg DD §1030.8 advertising review as a single control.** Advertising controls split into ad-content review (the message), APY-accuracy review (the math), and triggering-term review (when an APY ad triggers additional disclosures). The matrix needs all three.
5. **Skipping pass-through deposit-insurance recordkeeping on FBO accounts.** 12 CFR Part 330 [verify section] establishes the recordkeeping conditions for pass-through coverage on fiduciary and custodial accounts. Without those records the FBO depositors lose pass-through coverage. The matrix must include a §330 row when the scope includes a sponsor-bank program.
6. **Citing the CFPB small-entity compliance guide instead of the regulation.** The guide is helpful framing; cite the CFR section in the obligation-source column.
7. **Treating exception governance as a hygiene control.** Override and exception logs are an examiner-favorite review point. The matrix needs aggregate-reporting cadence, override-authority matrix, and a UDAAP screen row on overrides that affect customers.
8. **Marking the Joint Agency Statement on Bank-Fintech Arrangements as a regulation.** It is supervisory guidance, not a regulation. Phrase obligation-source as "supervisory guidance" and link to the underlying regulation (Reg E, Reg DD, 12 CFR Part 330) for the binding text.
