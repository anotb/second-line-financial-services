# Spec: engagement-scoping

Plugin: risk-compliance-core
Status: phase 1 spec sheet, pending phase 2 build
Date: 2026-05-06
Origin: added mid-phase-1 per practitioner feedback as the bootstrapping primitive other skills consume.

## Activation-tuned description

Produces a structured engagement-scope record that downstream second-line skills consume to set institution context, persona context, source posture, risk lens, and overlay set. The output is a reusable engagement charter that survives across the engagement and is revised as scope shifts. Replaces the implicit assumptions every skill would otherwise make about regulator constellation, sector overlay, and review-gate set.

Best for:
- An advisory engagement is starting and the engagement lead needs a written scope before any review work begins.
- An internal second-line review is being charted (annual model risk review, periodic third-party risk review, audit support engagement, exam-readiness sprint, regulatory-change implementation, board-pack preparation cycle).
- A new practitioner is joining an engagement mid-flight and needs the engagement context in one document.
- A skill is being invoked and the engagement scope is unclear or contested — running this skill first stops the downstream skill from defaulting to wrong assumptions.

Not the right tool when:
- The skill being invoked is already engagement-scope-aware and an engagement scope is already on file (skip and pass the existing scope).
- The work is a one-off question, not an engagement.
- The institution and persona are already encoded as constants in a firm-overlay reference doc (consume the overlay, do not redo scoping).

Anchored to: COSO ERM 2017 (engagement scoping is part of risk identification and assessment); IIA International Standards (Standards 2010, 2200, 2210 on engagement planning and objectives); AICPA AU-C 300 (audit engagement planning); SR 11-7 (model risk management requires defined scope); OCC Bulletin 2026-13 §III (model risk governance scope); interagency third-party risk management guidance June 2023 (TPRM scope); FFIEC IT Examination Handbook — Audit Booklet on engagement scoping; consulting practice convention (engagement letter, statement of work, engagement charter).

## Source anchors

- IIA International Standards 2010 (planning), 2200 (engagement planning), 2210 (engagement objectives), 2220 (engagement scope), 2240 (engagement work program). [verify exact section labels in the current 2026 standard set]
- AICPA AU-C 300 — Planning an Audit. [verify exact paragraph references]
- COSO Enterprise Risk Management — Integrating with Strategy and Performance (2017), Component 3 (Performance), Principle 10-13.
- SR 11-7 §I-II on scope of model risk management; OCC Bulletin 2026-13 §III on governance scope.
- Interagency Guidance on Third-Party Relationships (June 2023, OCC/FRB/FDIC), §II.A on risk-based scope of TPRM activity. [verify section labels]
- FFIEC IT Examination Handbook — Audit Booklet, "Audit Planning and Engagement" (current edition). [verify section labels]
- Consulting engagement letter and SOW conventions (no single regulator, but reflects practitioner expectation).
- Optional reference (where the engagement is for an exam-readiness sprint): SEC EXAMS engagement scope conventions; OCC Comptroller's Handbook on examination scope; FRB SR 12-17 on consolidated supervision scope.

## Sector overlays needed

- `banking` — bank holding company, national bank, state member bank, savings association, large-bank Heightened Standards scoping context (12 CFR Part 30 Appendix D), CCAR/DFAST in-scope determination, supervisory-letter posture (MRA / MRIA). [verify section labels]
- `insurance` — NAIC ORSA scope alignment, state DOI engagement context, P&C / life / health distinction, captive/reinsurer differences, holding-company-act scope (NAIC Model #440/#450). [verify model numbers]
- `capital-markets` — IA / BD / dual registrant / fund classification, Form ADV / Form CRS / Form BD baseline, FINRA membership, EXAMS examination type (routine / focused / for-cause).
- `payments-fintech` — sponsor-bank vs MTL vs both; primary regulator triangulation (CFPB direct, banking agency through sponsor, FinCEN, state); BaaS arrangement type.

## Cross-cutting overlays needed

- `cyber` — when the engagement scope includes cyber risk, capture cyber risk taxonomy alignment, NYDFS Part 500 applicability, SEC cyber 8-K applicability (public company), Reg S-P applicability.
- `privacy` — when in scope, capture GLBA Safeguards applicability, state privacy law applicability (CCPA/CPRA, VCDPA, CTDPA, etc.), HIPAA applicability for life/health insurance.
- `climate` — when in scope, capture SEC climate disclosure status (current state), TCFD-aligned reporting, state insurance climate risk disclosure.
- `conduct` — when the engagement is conduct-flavored, capture FCA SMCR applicability for UK-licensed entities, US enforcement themes.

## Output template named sections

The artifact is the engagement charter. Sections:

1. **Engagement summary** — one-paragraph statement of what the engagement covers, why now, and what is excluded.
2. **Institution profile**
   - Type (drop-down list above)
   - Asset size and complexity tier
   - Charter type
   - Registrations (federal, state, FINRA, NMLS, other)
   - Geographic footprint and licenses
   - Primary regulators (with relationship type — supervisor, examiner, registration authority)
   - Recent supervisory posture (MRAs, MRIAs, consent orders, enforcement actions, recent exams) where known
3. **Engagement profile**
   - Type (advisory / internal review / exam-readiness sprint / audit support / model validation engagement / regulatory-change implementation / board-pack preparation / vendor onboarding review / other)
   - Sponsor and accountable executive
   - Audience for the deliverable
   - Timeframe (start, target completion, milestones)
   - Deliverable shape (memo, workpaper set, board pack, exam-response file, register, model card)
   - Engagement letter or charter reference
4. **Persona profile**
   - Role of the practitioner running the engagement (CRO, head of model risk, head of TPRM, head of operational resilience, CCO, BSA officer, AI governance lead, head of regulatory affairs, head of internal audit, partner / engagement lead at advisory firm, embedded business risk officer 1.5-line, other)
   - Decision rights (what this practitioner can sign off; what they escalate)
   - Review gates (committee review, board review, regulator review, customer-facing approval, independent challenge requirement)
5. **Source posture**
   - Public-only / public-plus-firm-policy / public-plus-firm-policy-plus-system-of-record / connector-aware
   - Specific connectors enabled (GRC platform, policy management system, document management, model inventory, vendor inventory, ticketing, data-lineage)
   - Confidentiality posture
6. **Risk lens** — list of risk types in scope from the firm's risk taxonomy; include the firm's risk taxonomy reference if available.
7. **Sector overlay set** — which sector overlays apply and which sector-overlay reference docs the engagement loads.
8. **Cross-cutting overlay set** — which cross-cutting overlays apply.
9. **Out of scope** — explicit list of topics, entities, products, and functions excluded. Important for advisory engagements and audit support.
10. **Assumptions and dependencies** — facts being treated as fixed (institution structure, regulator constellation, source posture); what could change them.
11. **Revision log** — engagement scopes shift; each revision is dated with reason.

## Structured output fields

- `engagement_id`: string — unique ID for this engagement.
- `engagement_summary`: string — one-paragraph plain English.
- `institution`: object
  - `type`: enum — bank-holding-company / national-bank / state-member-bank / savings-association / broker-dealer / investment-adviser / registered-fund / insurance-company / money-transmitter / fintech / sponsor-bank-program / mutual / credit-union / public-company / other.
  - `asset_size_band`: enum — < $10B / $10-100B / $100B-$700B / $700B+ / not-applicable.
  - `charter`: string.
  - `registrations`: array of strings (federal, state, FINRA, NMLS).
  - `geographic_footprint`: array of strings.
  - `primary_regulators`: array of objects (`regulator`: string, `relationship_type`: enum).
  - `recent_supervisory_posture`: array of strings (MRA, MRIA, consent order references where public).
- `engagement`: object
  - `type`: enum — advisory / internal-review / exam-readiness-sprint / audit-support / model-validation / regulatory-change-implementation / board-pack-preparation / vendor-onboarding / other.
  - `sponsor`: string (role, not name).
  - `audience`: array of strings (roles).
  - `timeframe`: object (`start`: date, `target_completion`: date, `milestones`: array).
  - `deliverable_shape`: enum — memo / workpaper-set / board-pack / exam-response-file / register / model-card / other.
  - `charter_reference`: string (engagement letter / SOW reference).
- `persona`: object
  - `role`: enum — CRO / head-of-model-risk / head-of-TPRM / head-of-operational-resilience / CCO / BSA-officer / AI-governance-lead / head-of-regulatory-affairs / head-of-internal-audit / engagement-partner / engagement-lead-advisory / embedded-business-risk-officer-1.5-line / other.
  - `decision_rights`: array of strings.
  - `review_gates`: array of strings.
- `source_posture`: enum — public-only / public-plus-firm-policy / public-plus-firm-policy-plus-evidence / connector-aware.
- `connectors_enabled`: array of strings.
- `confidentiality_posture`: enum — public / firm-restricted / privileged / regulator-confidential.
- `risk_lens`: array of strings.
- `sector_overlay_set`: array of enum — banking / insurance / capital-markets / payments-fintech.
- `cross_cutting_overlay_set`: array of enum — cyber / privacy / climate / conduct.
- `out_of_scope`: array of strings.
- `assumptions_and_dependencies`: array of strings.
- `revisions`: array of objects (`date`: date, `reason`: string, `delta`: string).

## Two example scenarios

**Example 1 — Advisory engagement, exam-readiness sprint at a regional bank.**

Input: A consulting team is engaged by a $40B regional bank facing an OCC examination starting in 8 weeks. The engagement covers a credit-risk-governance and BSA/AML readiness sprint. The engagement lead is a partner; the audience is the bank's CRO and BSA officer. The bank has a recent MRA on credit concentrations and is on heightened OCC supervisory attention.

What the output emphasizes:
- Institution profile names OCC as supervisor, FRB as consolidated supervisor (state-chartered or national depending), state regulator if state-chartered, FDIC as deposit insurer.
- Engagement type: exam-readiness-sprint. Deliverable: exam-response file plus gap-and-remediation memo.
- Persona: engagement partner; review gates include partner approval, independent QA, internal QC at the bank before delivery to OCC examiner.
- Source posture: public-plus-firm-policy-plus-evidence; connectors enabled would include policy management system and credit-risk system of record.
- Risk lens: credit, BSA, operational; conduct optional.
- Sector overlay: banking. Cross-cutting overlays: cyber if in scope, privacy if relevant.
- Out of scope: model risk (separate engagement), capital adequacy review (CCAR-related), trading-book market risk.
- Assumptions: MRA remains open at engagement close; OCC examiner will request the document set per the September draft list.

**Example 2 — Internal second-line review at an SEC-registered investment adviser, AI use-case intake assessment.**

Input: A medium-sized RIA with $50B AUM has stood up an AI governance program and is running its first cycle of AI use-case intake. The CCO and the new AI Governance Lead want a structured engagement charter so the intake reviews follow a consistent scope.

What the output emphasizes:
- Institution profile: SEC-registered investment adviser; Form ADV registration; principal place of business one state; primary regulator SEC EXAMS, secondary SEC Division of Investment Management.
- Engagement type: internal-review (recurring AI use-case intake cycle).
- Persona: AI Governance Lead (2-line) is the practitioner; review gates are AI Risk Committee, CCO sign-off on regulatory implications, CRO sign-off on enterprise risk implications.
- Source posture: public-plus-firm-policy. Connectors: model inventory once available.
- Risk lens: model risk, operational risk, reputational risk, conduct, fiduciary risk specific to RIAs.
- Sector overlay: capital-markets. Cross-cutting overlays: cyber (RIA cyber rule + Reg S-P), privacy.
- Out of scope: vendor-side AI used by the firm's auditor, third-party manager AI used by the funds the adviser invests in (different review).
- Assumptions: Marketing Rule status quo for AI-generated marketing claims; SEC predictive-analytics rule current state [verify].

## Common pitfalls

1. **Treating the charter as a one-time deliverable.** Engagement scope shifts. The revision log exists for a reason — record every shift. A scope mid-flight is a status, not a fixed truth.
2. **Skipping the out-of-scope list.** Every engagement that gets contested in steering committee or in court traces back to an under-specified out-of-scope. Force the practitioner to name what is excluded.
3. **Defaulting the persona to "compliance."** This is the trap the broader repo is correcting. The engagement persona drives review gates and decision rights. CRO-function engagements have different review gates from compliance-function engagements; advisory-firm engagements have different gates from internal engagements.
4. **Listing every regulator that could conceivably apply.** The primary-regulators list is "who is this engagement actually addressing"; secondary regulators go in the assumptions. Keeping the primary list short forces clarity on engagement audience.
5. **Over-claiming source posture.** Saying "connector-aware" without confirming connector availability leads downstream skills to ask the wrong evidence questions. Set source posture at the level the engagement actually has, not the aspirational level.
6. **Encoding firm-specific facts as institution profile.** Institution profile is descriptive of the institution. Firm-specific overlays (firm risk taxonomy, firm policy library, firm review gates beyond the regulatory baseline) belong in a `references/firm-overlay.md`, not in the engagement charter.
