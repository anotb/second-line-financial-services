# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## advisory-exam-readiness-bank

### Example: advisory exam-readiness sprint at a regional bank

#### Input

A consulting team is engaged by a $40B regional bank facing an OCC safety-and-soundness examination starting in 8 weeks. The engagement covers a credit-risk-governance and BSA/AML readiness sprint. The engagement lead is a partner; the audience is the bank's CRO and BSA officer. The bank carries an open MRA on credit concentrations and is on heightened OCC supervisory attention. Source posture is public-plus-firm-policy-plus-evidence; the bank is willing to expose its policy management system and credit-risk system of record to the engagement team.

#### Why this scenario matters

This is the canonical advisory-firm exam-readiness use of the skill. The engagement charter has to be tight enough that downstream skills (`evidence-binder`, `control-matrix`, `issue-writeup`, `policy-gap-review`) inherit a clean institution profile, the right primary regulators, and an explicit out-of-scope list. The MRA posture and the OCC heightened attention drive review-gate stringency. The exam window forces a milestone-driven engagement profile.

#### Output sketch

```yaml
engagement_id: ENG-2026-OCC-RDY-04
engagement_summary: >
  Eight-week credit-risk-governance and BSA/AML readiness sprint ahead of
  OCC safety-and-soundness exam window opening 2026-07-01. Excludes model
  risk, capital adequacy, and trading-book market risk (separate engagements).
as_of_date: 2026-05-06

institution:
  type: state-member-bank
  asset_size_band: $10-100B
  charter: state-chartered member bank, Delaware
  registrations: [FRB Reg Y holding company, FDIC deposit insurance]
  geographic_footprint: [Mid-Atlantic, six-state branch network]
  primary_regulators:
    - regulator: OCC
      relationship_type: primary-supervisor
      notes: heightened supervisory attention; open MRA on credit concentrations
    - regulator: FRB
      relationship_type: consolidated-supervisor
    - regulator: FDIC
      relationship_type: deposit-insurer
    - regulator: state banking department
      relationship_type: host-state
  recent_supervisory_posture:
    - Open MRA, credit concentrations, issued at 2025-Q3 exam
    - Most recent BSA/AML exam closed without MRA, two informal recommendations

engagement:
  type: exam-readiness-sprint
  sponsor: Chief Risk Officer
  audience: [CRO, BSA officer, internal audit, board risk committee secretary]
  timeframe:
    start: 2026-05-06
    target_completion: 2026-06-30
    milestones:
      - {label: scope sign-off, date: 2026-05-13}
      - {label: evidence inventory complete, date: 2026-05-27}
      - {label: gap-and-remediation memo draft, date: 2026-06-17}
      - {label: exam-response file finalized, date: 2026-06-30}
  deliverable_shape: exam-response-file
  charter_reference: SOW-2026-04 (signed 2026-05-02)

persona:
  role: engagement-partner
  function: advisory (financial-services risk practice)
  decision_rights:
    - approve scope of work and revisions
    - sign off on deliverables before client release
  review_gates:
    - partner approval
    - independent QA (firm-internal)
    - client-side QC (CRO and BSA officer) before any document goes to OCC

source_posture: public-plus-firm-policy-plus-evidence
connectors_enabled:
  - policy management system
  - credit-risk system of record
  - issue-tracking ledger
confidentiality_posture: privileged

risk_lens: [credit, financial-crime, operational]
risk_taxonomy_reference: client risk taxonomy v3.2 (provided 2026-05-04)

sector_overlay_set: [banking]
cross_cutting_overlay_set: [cyber, privacy]

out_of_scope:
  - model risk (covered under separate validation engagement)
  - CCAR / capital adequacy review
  - trading-book market risk
  - third-party risk (handled by client TPRM team in parallel)

assumptions_and_dependencies:
  - MRA remains open through engagement close
  - OCC examiner-in-charge follows the September draft document request list
  - Client risk taxonomy v3.2 is current and stable through 2026-Q3

open_questions:
  - Whether OCC will request expanded testing on commercial real estate concentration
  - Whether BSA/AML scope extends to correspondent-banking program review

revisions:
  - date: 2026-05-06
    reason: initial scope
    delta: charter created
    approved_by: engagement partner, CRO
```

#### Why the scope shape matters downstream

- `evidence-binder` reads `connectors_enabled` and `confidentiality_posture` to set its evidence-collection posture.
- `control-matrix` reads `risk_lens` and `sector_overlay_set` to know which control library sections apply.
- `issue-writeup` reads `recent_supervisory_posture` to weight existing MRA context when issues are opened.
- `policy-gap-review` reads `assumptions_and_dependencies` to decide which policy-text snapshots are authoritative.
- The `out_of_scope` list is the deliberate firewall the engagement uses if scope creep arrives mid-sprint.

## internal-ai-governance-ria

### Example: internal AI use-case intake at an SEC-registered investment adviser

#### Input

A medium-sized RIA with $50B AUM has stood up an AI governance program and is running its first cycle of AI use-case intake reviews. The newly hired AI Governance Lead and the CCO want a structured engagement charter so every intake review follows a consistent scope, persona, and review-gate set. This is internal second-line work, not advisory. The deliverable is a recurring intake-review playbook anchored to a written charter.

#### Why this scenario matters

This is the second canonical use of the skill: an internal 2-line function setting up its operating model. The persona is not an advisory partner; it is an AI Governance Lead with named review committees. Source posture is public-plus-firm-policy (no system-of-record connectors yet, model inventory forthcoming). The risk lens is broader than the advisory-bank example: model risk, operational, reputational, conduct, fiduciary. Sector overlay is capital-markets, not banking, so different regulator constellation and different review machinery downstream.

#### Output sketch

```yaml
engagement_id: ENG-2026-AIG-INTAKE-01
engagement_summary: >
  Charter for the recurring AI use-case intake review cycle at an SEC-registered
  investment adviser. Establishes institution context, persona, review gates,
  and overlay set so each individual intake review runs against a consistent
  scope. Excludes vendor-side AI used by the firm's auditor and third-party-
  manager AI used by underlying funds.
as_of_date: 2026-05-06

institution:
  type: investment-adviser
  asset_size_band: not-applicable
  charter: Delaware LP general partner; investment adviser registered under
    Investment Advisers Act of 1940
  registrations: [SEC IARD (Form ADV), state notice filings in 12 states]
  geographic_footprint: [principal office NY, satellite offices in CA and CT]
  primary_regulators:
    - regulator: SEC EXAMS
      relationship_type: examiner
    - regulator: SEC Division of Investment Management
      relationship_type: rule-issuer
    - regulator: NYDFS
      relationship_type: functional-regulator
      notes: cyber regulation Part 500 applicability
  recent_supervisory_posture:
    - Most recent SEC exam closed in 2024 with no deficiency letter; one
      informal observation on marketing-rule disclosures

engagement:
  type: internal-review
  sponsor: Chief Compliance Officer
  audience: [AI Risk Committee, CCO, CRO, fund boards (informational)]
  timeframe:
    start: 2026-05-06
    target_completion: ongoing (charter reviewed annually)
    milestones:
      - {label: charter sign-off, date: 2026-05-20}
      - {label: first three intake reviews complete, date: 2026-07-01}
      - {label: first annual charter review, date: 2027-05-06}
  deliverable_shape: charter
  charter_reference: AIG-CHARTER-2026-V1

persona:
  role: AI-governance-lead
  function: AI governance (2-line, hybrid risk-and-compliance reporting line)
  decision_rights:
    - tier each intaked AI use case
    - approve or escalate model cards before pre-prod gate
  review_gates:
    - AI Risk Committee review for any use case tiered medium or above
    - CCO sign-off on any use case touching marketing, suitability, or
      adviser-client communications
    - CRO sign-off on any use case carrying model risk classification
    - Fund-board notification for any use case affecting fund operations

source_posture: public-plus-firm-policy
connectors_enabled: []
confidentiality_posture: firm-restricted

risk_lens: [model, operational, reputational, conduct, fiduciary]
risk_taxonomy_reference: firm risk taxonomy v2.1 (in references/firm-overlay.md)

sector_overlay_set: [capital-markets]
cross_cutting_overlay_set: [cyber, privacy]

out_of_scope:
  - vendor-side AI used by the firm's external auditor
  - AI used by third-party managers in the funds the adviser allocates to
  - personal-use AI tools by employees outside firm-issued endpoints

assumptions_and_dependencies:
  - Marketing-rule status quo for AI-generated marketing claims
  - SEC predictive-data-analytics rule current state [verify section]
  - Model inventory connector becomes available 2026-Q3

open_questions:
  - Whether NYDFS Part 500 cyber controls apply to all AI use cases or only
    those handling NPI [verify section]
  - Whether NAIC AI Bulletin applies indirectly via insurance-affiliated funds

revisions:
  - date: 2026-05-06
    reason: initial charter
    delta: created
    approved_by: AI Governance Lead, CCO
```

#### Why the scope shape matters downstream

- `ai-use-case-intake` reads `persona.review_gates` to know which committees see each intake.
- `ai-risk-tiering` reads `risk_lens` and `cross_cutting_overlay_set` to load matching tiering criteria.
- `model-card-builder` reads `institution.type` to set documentation tone (adviser-relationship language, not bank-supervision language).
- The `out_of_scope` list is the firewall against the program being asked to opine on third-party-manager AI, which is a different review entirely.
- Source posture being `public-plus-firm-policy` (not `connector-aware`) keeps downstream skills from asking for evidence that the firm cannot yet produce.

## troubleshooting

### Troubleshooting: scoping

The scope record is the bootstrapping primitive. When downstream skills produce wrong outputs (wrong regulator, wrong tone, evidence asks the engagement cannot satisfy, review gates that do not exist), the root cause is almost always a defect in the scope. This file walks the recurring defects and how to resolve them.

#### 1. The charter becomes a one-time deliverable

**Symptom**: Three weeks into the engagement, the institution profile, regulator list, or out-of-scope items are stale. Downstream skills are still consuming the original record.

**Why it happens**: The engagement was scoped on day one and never revisited. New facts surfaced (an MRIA was added, a connector came online, a new regulator engaged) and the charter did not update.

**Resolution**:
- Treat scope as a status, not a fixed truth. Mid-flight scope is the version that exists today.
- Use the revision log. Every shift gets a dated row with reason and delta. Append-only.
- Make scope review a standing item in the engagement steering cadence (weekly for sprints, monthly for ongoing programs).
- Re-emit the scope record after any material change so downstream skills receive the updated version.

#### 2. The out-of-scope list is empty or generic

**Symptom**: Mid-engagement steering committee or partner review challenges scope creep. The engagement has no written firewall to point at.

**Why it happens**: Practitioners are reluctant to write down what they will not do. The instinct is to leave room. The cost is later contestation.

**Resolution**:
- Force the practitioner to name three to five exclusions, even when the engagement feels well-bounded.
- Each exclusion is a sentence, not a noun. "Model risk" is not enough. "Model risk, including SR 11-7 validation work and model performance monitoring, which sits with the existing model validation engagement under SOW-2025-09" is a sentence.
- When scope creep arrives, point at the list. If the request is legitimate, log a revision and update the list.
- Advisory engagements: the out-of-scope list is the contractual defense. Internal engagements: it is the defence against priority drift.

#### 3. The persona defaults to "compliance"

**Symptom**: Downstream skills produce CCO-flavored deliverables when the engagement is actually CRO-led, or AI-governance-flavored when it is BSA-led. Review gates are wrong. Tone is wrong.

**Why it happens**: The skill was invoked without explicit persona, or the practitioner reflexively wrote "compliance" because that is the default the broader industry uses.

**Resolution**:
- The persona role is enumerated for a reason. Pick the right one. CRO, head of model risk, head of TPRM, BSA officer, CCO, AI Governance Lead, engagement partner, embedded business risk officer (1.5-line), and so on are different functions with different review machinery.
- 1.5-line and 2-line are different. A regional risk officer embedded in a business unit (1.5-line) has different review authority from a corporate risk officer (2-line). Capture the lens.
- Review gates are named, not generic. "Committee review" alone is insufficient. Which committee? With what criteria?

#### 4. The primary-regulator list has too many entries

**Symptom**: Every regulator that could conceivably apply is listed as primary. Downstream skills cite a confused regulator constellation. Citations are unfocused.

**Why it happens**: Practitioner anxiety about omitting a regulator. Also a misread of the field as "regulators with any relationship to this institution" rather than "regulators this engagement is addressing."

**Resolution**:
- Primary regulators is the list this engagement is actually addressing. Three is normal, five is a stretch, eight is broken.
- Conceivable-but-secondary regulators belong in `assumptions_and_dependencies` ("we assume the FRB consolidated supervisor will not request involvement in this exam scope").
- Fix the list before downstream skills consume it. A wrong regulator at the top distorts every citation choice the skill makes.

#### 5. Source posture is over-claimed

**Symptom**: Posture is set to `connector-aware`, but downstream skills repeatedly ask for evidence the engagement cannot produce. Or posture is `public-plus-firm-policy-plus-evidence` and the firm policy library is not actually accessible.

**Why it happens**: The aspirational posture (what the firm wishes were available) was captured rather than the actual posture (what the engagement can pull today).

**Resolution**:
- Set source posture at the level the engagement actually has, today. Roadmap items go in `assumptions_and_dependencies` with target dates.
- `connectors_enabled` is the truth-test. If the list is empty, posture is at most `public-plus-firm-policy`.
- Update posture when a connector or evidence pathway actually opens. Log it as a revision.
- For advisory engagements, posture is also a contractual question. Confirm with the engagement letter.

#### 6. Firm-specific facts encoded in the institution profile

**Symptom**: The institution profile includes firm-specific risk taxonomy lines, internal policy references, internal committee names, or proprietary review machinery. The charter does not survive being lifted to a peer engagement at a similar institution.

**Why it happens**: Firm-specific content leaked into the public-shaped institution profile because there was no `references/firm-overlay.md` to absorb it.

**Resolution**:
- Institution profile is descriptive of the institution as the regulator and the public would describe it. Type, charter, registrations, geographic footprint, primary regulators, public supervisory posture.
- Firm-specific content (firm risk taxonomy, internal policy library, firm review gates beyond the regulatory baseline, internal committee charters) belongs in `references/firm-overlay.md`. Set `risk_taxonomy_reference` to point at it.
- The charter should be readable by an external reviewer (advisory partner, regulator, auditor) without needing the firm-overlay file. The firm-overlay file is the customization layer.

#### 7. Risk lens is too narrow or too wide

**Symptom**: Downstream skills load the wrong cross-cutting overlays. Cyber-relevant work omits cyber. Or the lens lists every risk type and downstream skills load every overlay, producing bloated outputs.

**Why it happens**: The practitioner did not check the lens against the engagement type.

**Resolution**:
- Match `risk_lens` to the engagement type and to the deliverable. An exam-readiness sprint for credit-risk and BSA is `[credit, financial-crime, operational]`, not `[credit]` and not `[credit, market, liquidity, operational, strategic, reputational, model, climate, cyber, conduct, financial-crime, consumer-compliance, third-party, ICT]`.
- Cross-cutting overlay set follows from risk lens. If `cyber` is in the lens, `cyber` overlay loads. If conduct is not in the lens but the engagement touches consumer-facing work, add it explicitly.
- When in doubt, ask the engagement sponsor. Do not guess.

#### 8. The skill is invoked when it should not be

**Symptom**: Scoping is run on a one-off question or on a skill invocation that already has a scope on file. Output is wasted; the scope record drifts from the canonical one.

**Why it happens**: The downstream skill default-invoked scoping rather than checking for an existing scope.

**Resolution**:
- Downstream skills check for an existing scope record before invoking this skill.
- If a scope exists, consume it. If it is stale or contested, run a revision (not a fresh scope).
- For one-off questions (a quick obligation lookup, a single citation check), scoping is overkill. Skip it; use the public posture default.
- The "Not the right tool when" section of the activation description is the contract; the downstream skill respects it.
