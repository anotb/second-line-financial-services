# dora-register-builder revision review memo

Date: 2026-05-06
Reviewer: phase-2 reviewer subagent
Subject: `plugins/capability-plugins/third-party-operational-resilience/skills/dora-register-builder/SKILL.md`
Compared against: spec sheet (`docs/specs/third-party-operational-resilience/dora-register-builder.md`), revised reference patterns (`vendor-diligence/SKILL.md`, `engagement-scoping/SKILL.md`, `model-card-builder/SKILL.md`), build contract (`docs/plans/2026-05-06-phase2-build-contract.md`), anti-AI-tells memory (with sequencing nuance), references-first memory, practitioner-lens memory, and the rule-1/2/4 violations from `python3 scripts/check-skill-content.py --plugin third-party-operational-resilience`.

## 1. Top-line judgment

The SKILL.md is the un-rewritten generic stub. The supporting files (`templates/`, `schemas/`, `examples/`, `TROUBLESHOOTING.md`, `references/source-anchors.md`, sector overlays, cross-cutting cyber overlay) all read as the wave-1 build did its job. The SKILL.md did not. It is the placeholder shape that ships with the empty skill scaffold — same body as `concentration-risk-review`, `contract-gap-review`, `criticality-assessment`, `exit-plan`, and `resilience-testing-pack` — and the rule-4 duplicate-content checker confirms: 76–81% body overlap with five sibling skills. The build agent's flag was right; this is not a draft to revise, it is a draft to replace.

The frontmatter description has a single one-line summary plus a "Use for financial-services second-line, compliance, risk, audit, governance, regulatory change, controls, evidence, or reporting work where outputs must be traceable, human-reviewed, and anchored to public regulatory sources" wrapper, which is the rule-2 failure: no `Best for:`, no `Not the right tool when:`, no `Anchored to:`. The body is a "Required process" 7-step ladder followed by an "Output format" 6-section ladder followed by a "Guardrails" bullet list. Every clause that maps to a sibling skill's clause flunks rule-1 because the same boilerplate is in five other SKILL.mds.

The spec sheet has the substance the rewrite needs: ITS-table-aligned spine, two named example scenarios, twelve named structured-output fields, nine pitfalls, three cross-skill chain points (`criticality-assessment` upstream, `vendor-diligence` upstream, `concentration-risk-review` downstream). The `templates/default-output.md`, `schemas/dora-register.schema.json`, examples, and `TROUBLESHOOTING.md` are already aligned to this. The SKILL.md just has not caught up.

Net: this is a near-total replacement, not a five-edit revision memo. The shape below mirrors the vendor-diligence pattern (closest sibling, same plugin, already revised). Fifteen proposed edits, grouped: one full description rewrite (Edit 1), one full body rewrite organized as eight named sections (Edits 2–9), four targeted substance restorations (Edits 10–13), two stylistic cleanups (Edits 14–15).

If the orchestrator can land only one edit, it is Edit 1 plus Edits 2–9 together — the description and the body must be replaced as a unit, otherwise the skill remains rule-1, rule-2, and rule-4 non-compliant.

## 2. What the current SKILL.md drops or gets wrong

### 2.1 Description shape (rule-2 failure)

Current description is a single paragraph followed by `argument-hint`. The rule-2 contract requires `Best for:`, `Not the right tool when:`, `Anchored to:` activation markers. The spec sheet's "Activation-tuned description" block has all three already drafted; the build agent shipped without using them.

The spec sheet's description contains seven `[verify subarticle]` / `[verify section]` markers. Per the references-first memory and the build contract, those go in `references/source-anchors.md`, not in the SKILL.md description's `Anchored to:` line. The description names regs once at the top level; section refs and verification flags live in references.

### 2.2 Body shape and overlap (rule-4 failure)

The body's "Required process" 7-step ladder and "Output format" 6-section ladder are the boilerplate the same plugin uses for `concentration-risk-review`, `contract-gap-review`, `criticality-assessment`, `exit-plan`, and `resilience-testing-pack`. Each pair triggers rule-4 at 76–81% overlap. None of the dora-specific substance — the ITS schema, the table-aligned spine, the LEI/EUID identifier discipline, the sub-contractor-chain visibility for critical-or-important functions, the intra-group flag, the data-quality-findings section, the consolidation-level discipline, the year-on-year delta posture for annual refresh — is in the body. All of it is in the spec sheet, the template, and TROUBLESHOOTING. None of it is in the workflow Claude reads at runtime.

### 2.3 Placeholder phrasing (rule-1 failures, 24 hits)

The check returns 24 rule-1 hits on this SKILL.md. The phrases that trip rule-1 are the verbatim boilerplate strings the checker maintains as a banned-phrase list (see `scripts/check-skill-content.py`). The fix is not a phrase-by-phrase swap; it is replacing the 7-step "Required process" + 6-section "Output format" + bullet "Guardrails" structure with the practitioner-walk shape vendor-diligence and model-card-builder use. The boilerplate phrases disappear because the boilerplate sections disappear.

### 2.4 Substance the SKILL.md has to carry that the boilerplate cannot

Cross-checking the spec, the supporting files, and the build contract, the named substance the SKILL.md must surface (and currently does not):

- Two valid entry paths: first-cycle build and annual-refresh review. The spec example scenarios are one of each. They have different evidence asks and different headline outputs.
- Upstream chain to `criticality-assessment` for the critical-or-important-function flag. The flag without dated criticality evidence is itself a finding (TROUBLESHOOTING calls this out; SKILL.md does not).
- Upstream chain to `vendor-diligence` for sub-contractor and data-flow inputs.
- Downstream chain to `concentration-risk-review` for the portfolio view.
- The ITS-schema spine: `b_01` general, `b_02` specific, `b_03` ICT third-party providers, `b_04` functions, `b_05` ICT services, `b_06` sub-contractor chain, `b_07` identification codes. The template names them; the SKILL.md should name them as the spine the practitioner walks.
- Identifier discipline: LEI / EUID / national identifier, the `identifier_type` field, what to do when no GLEIF-issued LEI exists. This is the schema's load-bearing relational rule.
- Service-type taxonomy mapping: firm-internal taxonomy → ITS taxonomy, with mapping decisions kept as part of the source trace. (TROUBLESHOOTING #3.)
- Sub-contractor-chain visibility for critical-or-important functions; rank-2+ disclosure as a contract-gap when opaque (route to `contract-gap-review`). Not a silent absence.
- Data-processing-location and data-at-rest-location fields as mandatory for many records and material for the concentration view, not nice-to-haves.
- Intra-group flag in `b_02`: reportable but flagged differently. Both directions of error (flag missing; record omitted) fail the schema.
- Consolidation level (`individual` / `sub-consolidated` / `consolidated`): resolved at scope, not in records. EU sub of non-EU group files individually.
- Data-quality-findings section as part of the build pack: supervisors expect the firm to know its own gaps. The submission-quality register is not a clean-looking register, it is a register with a credible findings section.
- Annual-refresh deltas: silent up-classification, vendor restructuring, year-on-year movement. The annual cycle has its own evidence ask.
- Submission boundary: the skill drafts; the firm files. NCA-specific technical instructions on format, channel, and validation are downstream of this skill.
- Cyber cross-cutting overlay (the completer added this; the SKILL.md should name when it is consulted — typically when ICT-service-type and sub-contractor records intersect cyber-control attestations from `vendor-diligence`).
- Scope-record consumption: when an `engagement-scope` record is supplied, consume it for institution type, primary regulators (the relevant NCA), sector overlay, source posture; otherwise ask the few questions the build needs and default.

None of this is in the current SKILL.md. All of it is in the spec, template, schema, examples, TROUBLESHOOTING, or references.

### 2.5 Engagement-scope integration is missing

Per the build contract, every non-`engagement-scoping` skill carries the two-path engagement-scope integration: consume the record when supplied; ask the few questions when not. The current SKILL.md has no engagement-scope integration at all.

### 2.6 The cyber cross-cutting overlay file exists but is not surfaced

The completer added `references/cross-cutting/cyber.md`. The SKILL.md does not name it in the Pointers section (because the SKILL.md does not have a Pointers section). The file is invisible at runtime.

### 2.7 The `[verify section]` markers in the description (rule from anti-AI-tells memory)

The current description does not have `[verify section]` markers, which is correct. The build agent flagged "activation marker issues" — meaning the rule-2 issue (Best for / Not the right tool when / Anchored to all missing), not verify-section pollution. Edit 1 below restores the three activation markers and explicitly does not carry the spec sheet's seven `[verify…]` flags into the description; those stay in `references/source-anchors.md` only.

## 3. Proposed edits

Fifteen edits. The first nine are the rewrite; the rest are targeted substance restorations and stylistic cleanups against the rewrite.

### Edit 1 — replace the description with the three-marker shape

**Location**: frontmatter `description` field.

**Current** (single paragraph):

> Create DORA-style register entries for ICT third-party contractual arrangements, including supported functions, criticality, subcontractors, and data quality checks. Use for financial-services second-line, compliance, risk, audit, governance, regulatory change, controls, evidence, or reporting work where outputs must be traceable, human-reviewed, and anchored to public regulatory sources such as EBA DORA register of information preparation materials, EBA DORA oversight framework materials.

**Proposed text** (multi-line YAML literal, mirroring vendor-diligence shape; no `[verify section]` markers):

```yaml
description: |
  Drafts the firm's Register of Information for ICT third-party arrangements in the structure the EBA-developed implementing technical standard under DORA defines. Produces register entries across the ITS tables (general arrangements, specific arrangements, ICT third-party providers, functions, ICT services, sub-contractor chain, identification codes) for one or many arrangements, with the relational fields the supervisory submission requires. Drafts only; the firm files.

  Best for:
  - An EU-nexus financial entity preparing the DORA Register of Information for the first or annual submission cycle.
  - An EU subsidiary of a non-EU parent where the group needs visibility into the EU register's data quality before the subsidiary submits.
  - A second-line review of an existing register where data-quality and ITS-schema consistency need a structured check before submission.

  Not the right tool when:
  - The firm has no DORA nexus. Use the firm's own TPRM register and skip this skill.
  - The question is per-arrangement diligence (use `vendor-diligence`) or contract clause coverage (use `contract-gap-review`).
  - The criticality-or-important-function flag has not been set with dated evidence (run `criticality-assessment` first; consume its output here).
  - The submission is governed by NCA technical filing rules that diverge from the ITS. This skill drafts to the ITS schema; route the format-and-channel question to legal and compliance.

  Anchored to: DORA — Regulation (EU) 2022/2554 Articles 28 and 30; the Commission Implementing Regulation adopting the ITS for the Register of Information (developed jointly by the EBA, EIOPA, and ESMA); EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02) §11; EIOPA-coordinated guidance for insurers; ESMA-coordinated guidance for investment firms, trading venues, CSDs, and CCPs; ECB and NCA technical reporting instructions where applicable. Citations and excerpts live in `references/source-anchors.md`.
```

**Why**: rule-2 requires the three activation markers; the current description has none. The spec sheet's draft has seven `[verify…]` markers, which violate the anti-AI-tells memory and the build contract; the rewrite carries the substance without the markers (the section refs sit in source-anchors.md). The "Drafts only; the firm files" line lands the boundary up front so the body does not have to repeat it. The "Not the right tool when" list draws the boundary against `vendor-diligence`, `contract-gap-review`, and `criticality-assessment` — the three siblings most likely to be confused with this skill.

### Edit 2 — replace the body opening with a practitioner-frame paragraph

**Location**: replace the line "Use this skill to create DORA-style register entries for ICT third-party contractual arrangements, including supported functions, criticality, subcontractors, and data quality checks. Produce review-ready second-line work product that a qualified risk, compliance, legal, audit, or control owner can inspect and approve."

**Proposed text**:

> # DORA Register Builder
>
> The DORA Register of Information is the firm's structured account of every ICT third-party arrangement in scope under DORA, in the schema the joint ESAs ITS prescribes. The register is identifier-driven, cross-linked across tables, and the supervisory pipeline relies on the relational integrity. This skill drafts the register: for a first-cycle build, for an annual refresh, or for a second-line review of an existing register's data quality. It does not file. Filing is a regulated submission with NCA-specific technical instructions and accountable-executive sign-off; this skill stops at the draft and the data-quality-findings pack.
>
> Both first-line preparation and second-line review use the same skill. The first-line use case is "build the register from the firm's TPRM register, contract repository, and ICT-asset inventory"; the second-line use case is "read the register against the ITS schema, the firm's other registers, and the criticality evidence, and surface the gaps before submission." The seam between them is the data-quality-findings section and the reconciliations against the firm's existing registers.

**Why**: opens the skill with what the artifact is, what schema it conforms to, what the boundary is (drafts, not files), and what the dual-use pattern is. Mirrors the vendor-diligence and model-card-builder opening shape (one or two paragraphs, no header for the overview).

### Edit 3 — add an "Ask first" section with four practitioner questions

**Location**: new section after the opening paragraphs.

**Proposed text**:

> ## Ask first
>
> Most of what the build needs is on the table by the time someone reaches for this skill. A few things to settle before drafting:
>
> - **What entities are in scope, and at what consolidation level.** A non-EU parent's EU subsidiary files individually to its NCA; a group with multiple EU entities may file consolidated where DORA scope reaches consolidation. `individual`, `sub-consolidated`, `consolidated` is the trichotomy. Resolve here, not in the records.
> - **Is this first cycle or annual refresh.** First cycle leans on input registers and mapping decisions. Annual refresh leans on year-on-year delta — additions, terminations, re-classifications, vendor restructurings — and on dated criticality evidence supporting any upward criticality move.
> - **Which input registers and systems are available.** The firm's existing TPRM register (often the EBA outsourcing register where in place), the contract repository, the ICT-asset inventory, the criticality outputs per arrangement, the sub-processor lists from `vendor-diligence`. Source posture (public-only, public-plus-firm-policy, public-plus-evidence, connector-aware) sets what the build can assert at high confidence and what carries `[evidence needed]`.
> - **Is there a current `criticality-assessment` output for each in-scope arrangement.** The critical-or-important-function flag drives sub-contractor-chain visibility, NCA scrutiny, and oversight-framework relevance. Setting the flag without dated criticality evidence is itself a finding; route to `criticality-assessment` first if the output is not on file.
>
> When the engagement-scope record is supplied, the skill consumes it for institution type, primary regulator (the relevant NCA), sector overlay set, source posture, and persona. Otherwise it asks the questions above and defaults to public posture.

**Why**: the four questions are the load-bearing decisions a senior practitioner makes before drafting. Mirrors the vendor-diligence and model-card-builder pattern (four bullets, prose-friendly, not numbered). The criticality question is not a tier question (this skill does not set criticality), it is an evidence question — does the flag have dated evidence behind it.

### Edit 4 — add the "How the register gets built" section walking the ITS-table spine

**Location**: new section after "Ask first".

**Proposed text**:

> ## How the register gets built
>
> The register has the same spine across builds: ITS table by ITS table, with the relational links carried through. A senior preparer walks them in roughly the order the inputs surface, not in lockstep. The structured output sorts itself.
>
> The build opens with **register metadata and scope**: the financial entity LEI, the reporting reference date, the NCA code, the consolidation level, the reporting currency. The entities-in-scope list is named here, with each entity's role in consolidation. Source-data posture lands here too — which firm registers and systems were used as input and what data-quality caveats apply (the input was a four-month-old TPRM extract; the contract repository was incomplete for one BU).
>
> **`b_01` contractual arrangements (general)** carries the arrangement reference, type (single, complex, master-and-addenda), dates, notice period, governing law, and contract value. `b_02` carries the relational links from the arrangement to the ICT third party and the ICT services, plus the intra-group flag. The intra-group flag is the supervisory expectation for arrangements with group entities — set it correctly; intra-group arrangements remain reportable.
>
> **`b_03` ICT third-party service providers** is identifier-driven: LEI is the primary; EUID and national identifiers come second; `identifier_type` is set on the chosen identifier. Long-tail SaaS and small specialist providers often lack a GLEIF-issued LEI; record the best available with `identifier_type` and raise a `data_quality_findings` entry. Do not invent identifiers. Country of head office, country of registration, ultimate parent identifier, type, criticality designation by competent authority where known, and the EU-presence flag complete the record.
>
> **`b_04` functions** names each function the firm performs that an in-scope ICT third party supports, with the criticality designation (`critical-or-important`, `not-critical-or-important`) and the recovery time and recovery point objectives. The criticality designation is consumed from `criticality-assessment`, with the evidence record ID carried as `criticality_evidence_record_id`. A function with the critical-or-important flag set without an evidence record is a finding, not a clean record.
>
> **`b_05` ICT services** sits at the centre of the relational graph: each service links to the function it supports (`b_04`), the ICT third party providing it (`b_03`), and the contractual arrangement under which it is provided (`b_01`/`b_02`). The ICT-service-type code follows the ITS taxonomy; the firm's internal procurement or TPRM service-type taxonomy will not align one-for-one, so the mapping is built once and the mapping decisions (especially the lossy ones) are recorded as part of the source trace. Location of data at rest and location of data processing are mandatory for many records and material for the concentration view; a single country code where the actual hyperscaler footprint spans multiple regions is wrong, not minimal.
>
> **`b_06` sub-contractor chain** is required for ICT services supporting critical-or-important functions. Stopping at the contracted ICT third party (rank 1) and treating rank-2+ as out of scope is a frequent gap. When the chain is genuinely opaque past rank 1 because the vendor will not disclose, that is a finding and a contract-gap (route to `contract-gap-review`), not an absence to be silently accepted. Sub-processor lists from `vendor-diligence` are an input here.
>
> **`b_07` identification codes** carries the LEI / EUID / national-identifier triplet for cross-checking. Reconcile against the firm's existing registers (TPRM register, ICT-asset inventory, contract repository); each reconciliation conflict is a `data_quality_findings` entry, not a silent overwrite.
>
> The build closes with the **data-quality-findings** section and **reconciliations**. A submission-quality register includes the firm's own quality view; supervisors expect the firm to know its own gaps. A clean-looking register with no findings reads as either complete (rare for first-cycle builds) or unaware (more common). Findings are an asset in supervisory dialogue, not an admission of failure.

**Why**: this is the body the spec calls for, the template structures, the schema fields support, and the TROUBLESHOOTING references. The seven ITS tables are the spine; the relational links between them are the load-bearing architectural fact; the data-quality-findings section is the second-line discipline. Prose paragraphs each opening with a named handle (vendor-diligence pattern), so the runtime reader has the explicit handles without numbered ladder rigidity.

### Edit 5 — add an "Annual refresh" subsection where the year-on-year cycle has its own substance

**Location**: subsection within "How the register gets built", after the closing data-quality-findings paragraph.

**Proposed text**:

> ### Annual refresh
>
> Annual refresh consumes the prior-year register as the base and reports year-on-year delta. The delta is its own finding: additions, terminations, re-classifications, and vendor restructurings each carry supervisory weight. Two patterns recur and warrant explicit attention.
>
> A function moving from `not-critical-or-important` to `critical-or-important` between cycles is an upward classification with consequences. Silent up-classification (the flag flips, no `criticality_evidence_record_id` is updated) reads as the firm not noticing. Surface the change in the build pack's year-on-year delta section; require fresh criticality evidence for the upward move.
>
> When an ICT third party restructures and the contracting entity changes (new LEI, new legal entity, same operational service), preserve the arrangement reference history via `linked_arrangement_references`. A new `b_03` record for the post-restructure entity, a new `b_01` record for the new contractual arrangement, and an audit trail linking the two. Otherwise the year-on-year register reads as termination plus new onboarding rather than continuation.

**Why**: the annual-refresh use case is one of two named scenarios in the spec sheet's examples and has substance the first-cycle build does not. TROUBLESHOOTING covers both patterns. The SKILL.md should name them where Claude reads at runtime, not bury them in TROUBLESHOOTING only.

### Edit 6 — add sector-overlay loading guidance

**Location**: new short subsection after "Annual refresh".

**Proposed text**:

> ### Sector overlays
>
> The DORA register applies across sectors (banking, insurance, capital markets, payments-fintech) but the NCA, the technical reporting channel, and the supervisory expectations differ. Load the overlay the engagement scope names: `references/sector-overlays/banking.md` for ECB SSM banks and EBA-coordinated less-significant institutions; `insurance.md` for EIOPA-coordinated insurers and the US-parent NAIC interplay; `capital-markets.md` for ESMA-coordinated investment firms, trading venues, CSDs, and CCPs; `payments-fintech.md` for payment institutions and e-money institutions. Multi-entity groups straddling sectors load multiple. The overlay's named NCA-specific instructions and submission-channel guidance land in the build pack; treating the overlay as background reading is the failure mode.

**Why**: the spec lists four sector overlays as needed; the build shipped them; the SKILL.md does not name when they load. Pattern follows the vendor-diligence and model-card-builder overlay-loading sections. The "treating the overlay as background reading is the failure mode" line is the same practitioner observation model-card-builder uses (and works there).

### Edit 7 — add a cyber cross-cutting overlay note

**Location**: new short subsection after "Sector overlays".

**Proposed text**:

> ### Cyber cross-cutting overlay
>
> Cyber considerations enter the register through fields the schema already includes (data location, sub-outsourcing, ICT-service-type taxonomy). The deeper cyber-control read sits with `vendor-diligence` and consumes that skill's structured record. Where cyber-attestation gaps in the input register affect the data-quality view of the DORA register — for example, a SOC 2 scope that excludes the data-residency control, or a sub-processor list shorter than the contract addendum — load `references/cross-cutting/cyber.md` and surface the gap as a `data_quality_findings` entry tied to the affected ICT-service record.

**Why**: the completer added the cyber overlay file. Without a SKILL.md mention of when it loads, the file is invisible at runtime. The framing keeps the cyber depth at `vendor-diligence` (per the spec sheet's "deeper treatment lives with vendor-diligence") and uses the overlay only for register-level data-quality consequences.

### Edit 8 — replace the "Output format" ladder with an "Output" section naming the artifact and the structured record

**Location**: replace the existing "## Output format" section (lines 28–40 of current SKILL.md).

**Proposed text**:

> ## Output
>
> Two artifacts: the build pack per `templates/default-output.md`, and the structured register record per `schemas/dora-register.schema.json`. The build pack is the practitioner-readable artifact (scope, source posture, ITS-table summaries, data-quality findings, reconciliations, year-on-year deltas where applicable, open questions for legal and compliance, reviewer questions, source trace, confidence label). The structured record is what downstream skills consume.
>
> Downstream consumers: `concentration-risk-review` reads the `b_03`, `b_05`, and `b_06` records to compute provider-, service-, and country-concentration views; the firm's regulatory-reporting pipeline consumes the structured record (or its NCA-specified export) for the actual filing. Upstream consumers: `criticality-assessment` outputs the function-level critical-or-important flag the register's `b_04` carries; `vendor-diligence` outputs the sub-processor and data-flow data the register's `b_05` and `b_06` carry; `engagement-scope` (when supplied) carries institution, NCA, sector overlay, and source posture.
>
> The schema is the cross-skill contract; additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.
>
> The skill drafts. The submission is a regulated filing requiring legal, compliance, and accountable-executive sign-off, and goes through the firm's regulatory-reporting pipeline with NCA-specific technical instructions on file format, channel, and validation. The skill produces the structured record and the build pack; the firm files.

**Why**: the current "Output format" 6-section ladder is rule-1 boilerplate. Replace with the named-artifact / named-consumer / schema-stability / submission-boundary shape vendor-diligence and model-card-builder use. The schema-stability sentence is the same as the vendor-diligence and model-card-builder pattern (per the corresponding revision memos). The submission boundary moves to one place and stays out of the body.

### Edit 9 — add a "What's load-bearing and what flexes" section (replacing "Guardrails")

**Location**: replace the existing "## Guardrails" bullet list.

**Proposed text**:

> ## What's load-bearing and what flexes
>
> Load-bearing across every build: every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by path; unsupported claims are marked `[evidence needed]`; section references that cannot be confirmed get `[verify section]` in `source-anchors.md`, never in the build pack body or this SKILL; source evidence, firm assertion, public-source obligation, generated inference, and open legal or compliance question stay distinguishable in the build pack; identifiers are not invented; the critical-or-important-function flag carries a dated `criticality_evidence_record_id` or it is a finding; intra-group arrangements are flagged in `b_02`, not omitted; the data-quality-findings section is part of every build pack; no named institutions appear unless they are public defendants in a finalised enforcement action with a published consent order; the skill stops at the draft.
>
> Flexes to the engagement: build pack length scales to scope (single-arrangement annual delta is short; first-cycle multi-entity build is long). Sector overlay set follows engagement scope; multi-sector groups load multiple. Source posture sets the evidence ask. The audience drives the build pack's framing — a head-of-vendor-management pack reads operationally; an EU-subsidiary risk-officer pack reads with the parent-group consolidation lens; a regulator response pack is fully source-traced.

**Why**: the current "Guardrails" bullet list is shared boilerplate (rule-1 and rule-4). Replace with the load-bearing-and-flexes shape vendor-diligence and model-card-builder use. The load-bearing list is dora-specific (identifier discipline, criticality-evidence pointer, intra-group flag, data-quality-findings as mandatory, the named-institutions and stops-at-draft rules that are repo-wide). Flexes are dora-specific too (build length to scope, sector overlay set, audience).

### Edit 10 — add a "Pointers" section

**Location**: new section after "What's load-bearing and what flexes" (i.e. at the end of the body).

**Proposed text**:

> ## Pointers
>
> - `references/source-anchors.md` — citations and excerpts for the named anchors.
> - `references/sector-overlays/banking.md`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific NCA frame loaded per engagement scope.
> - `references/cross-cutting/cyber.md` — cyber overlay loaded where cyber-attestation gaps affect the register's data-quality view.
> - `references/firm-overlay.md` — firm-installed policy, taxonomy, NCA-specific submission rules beyond the regulatory baseline; consumed when present.
> - `templates/default-output.md` — build pack template.
> - `schemas/dora-register.schema.json` — structured-record contract.
> - `examples/critical-cloud-bank.md`, `examples/data-vendor-asset-manager.md` — public-source-derived scenarios.
> - `TROUBLESHOOTING.md` — recurring pitfalls (EBA-outsourcing-register-as-drop-in, identifier gaps, taxonomy mapping, criticality-evidence absence, sub-contractor-chain stopping at rank 1, intra-group flag confusion, consolidation level errors, annual-refresh silent up-classification, vendor restructuring).

**Why**: the current SKILL.md has one "Also consult" line in the Source-anchors section; the references the skill actually ships (sector overlays, cyber overlay, schema, examples, TROUBLESHOOTING) are unmentioned. The Pointers shape mirrors vendor-diligence and model-card-builder. File-path-only, no commentary beyond the brief role.

### Edit 11 — restore the consolidation-level discipline as a load-bearing point

**Already covered in Edit 3 ("What entities are in scope, and at what consolidation level") and Edit 9 (load-bearing list). No separate edit; verifying it lands twice — once at the entry-question stage (where the practitioner resolves it) and once in the load-bearing list (where the discipline is restated).**

### Edit 12 — restore the EBA-outsourcing-register-vs-DORA-register distinction

**Location**: small addition to Edit 3's "Which input registers and systems are available" bullet, or one sentence inside Edit 4's `b_01` paragraph.

**Proposed addition** (one sentence inside Edit 4's `b_01` paragraph, after the contract-value clause):

> The EBA outsourcing register is a frequent input but is a different schema — flatter, narrower scope (outsourcing as defined by EBA/GL/2019/02, not all ICT arrangements), different relational structure. Map, do not copy. Mapping conflicts (data-residency value differs across the two; sub-contractor list shorter on one side) are `data_quality_findings`, not silent overwrites.

**Why**: TROUBLESHOOTING #1 is "EBA outsourcing register treated as drop-in DORA register data" — the most common first-cycle defect. The SKILL.md has to name the distinction once at the spot in the body where the input lands.

### Edit 13 — name the upstream and downstream chain handles explicitly

**Already covered in Edit 1 (description's "Not the right tool when" boundary), Edit 3 (criticality-evidence question), Edit 4 (`vendor-diligence` and `criticality-assessment` consumption points; `contract-gap-review` routing for opaque sub-contractor chain), and Edit 8 (named consumers in the Output section). No separate edit; verifying the chain handles land four times across the body where each chain matters.**

### Edit 14 — drop the spec sheet's `[verify…]` markers when bringing description substance into the rewrite

**Location**: throughout Edit 1.

**Why**: the spec sheet's draft description carries `[verify subarticle]`, `[verify section]`, `[verify ITS reference]`. Per anti-AI-tells memory and references-first memory, those markers belong in `references/source-anchors.md`, not in the SKILL.md description's `Anchored to:` line. Edit 1 names DORA Articles 28 and 30 directly, names the EBA / EIOPA / ESMA joint authorship of the ITS, names `EBA/GL/2019/02 §11` directly. Where a section reference is genuinely uncertain at SKILL.md time, the rewrite drops the reference rather than carrying a `[verify section]` marker that pulls Claude into verification work on every invocation.

### Edit 15 — keep practitioner voice consistent; no fake-precision tells

**Location**: throughout the rewrite.

**Why**: as a discipline note for the rewriter. The rewrite above does not include "three is normal, five is a stretch", "in 5–10 minutes", "Tier-1 builds have 12 sections", "the most common defect", or comfort-precision ranges. Where empirical numbers appear (DORA Article 28, EBA/GL/2019/02 §11, the seven `b_0X` ITS tables) they are empirical. Where adjectives might creep in (comprehensive register, robust diligence, holistic view), the rewrite does not use them. The rewrite uses "load-bearing" once in the section title and once or twice in the body; not as a tic. The rewrite does not stack "must / mandatory / required / non-negotiable"; the load-bearing list is a sentence with semicolons, not a parallel-structure ladder.

## 4. What the build did right and should not be undone

In case the orchestrator over-corrects after this memo:

- **The supporting files are good.** `templates/default-output.md`, `schemas/dora-register.schema.json`, `examples/critical-cloud-bank.md`, `examples/data-vendor-asset-manager.md`, `references/source-anchors.md`, `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md`, `references/cross-cutting/cyber.md`, and `TROUBLESHOOTING.md` all read aligned to the spec sheet. The rewrite consumes them; do not rebuild them. (I have not deeply read the schema or the templates beyond verifying alignment with the spec field list and TROUBLESHOOTING content; the orchestrator should not assume my review covered those files.)
- **The TROUBLESHOOTING content is the right depth.** Eleven pitfalls, each one or two paragraphs of working guidance, sources in `references/source-anchors.md`. The SKILL.md rewrite names the same pitfalls but does not repeat the full TROUBLESHOOTING substance — it points at the file in Pointers.
- **The two example scenarios cover both entry paths** (first-cycle build for an EU sub of a US bank; annual-refresh review for an EU-nexus insurer). Public-source-derived. No named institutions.
- **The sector-overlays directory has all four files** — banking, insurance, capital-markets, payments-fintech. Pattern matches the build contract; the rewrite's "Sector overlays" subsection consumes them.
- **The cross-cutting cyber overlay file exists** — the completer added it. The rewrite surfaces it in the body; the file itself is not changed.
- **The frontmatter `argument-hint`** is fine and survives the rewrite.

## 5. Closing

This is a rewrite, not an edit pass. Edits 1 through 9 replace the description and the body wholesale; Edits 10 through 15 are targeted notes against the rewrite. Rule-1 violations resolve because the boilerplate phrases disappear. Rule-2 resolves because Edit 1 restores the three activation markers. Rule-4 resolves because the body is now dora-specific instead of shared boilerplate; expect the duplicate-content score against the five sibling skills to drop below 50% once those siblings receive the same rewrite treatment.

If the orchestrator can land only one edit, it is Edits 1 through 9 as a unit — the description and the body must be replaced together. Edits 10 (Pointers section) and 12 (EBA-outsourcing-register clause) are the two highest-value targeted additions on top of the rewrite.

None of the proposed edits restore numbered ladders for non-sequential content, fake-precision ranges, repeated must/mandatory/required stacking, "fail the quality bar" prose, marketing adjectives (comprehensive / robust / leverage / ensure / facilitate / streamline / optimize / enhance / holistic), hedge tics ("it is worth noting", "you may want to consider", "important to note"), `[verify section]` markers in the SKILL.md or description, or named institutions outside public consent-order defendants. Numbered sequencing appears nowhere in the rewrite because the ITS-table spine is recoverable at runtime through the named handles in each paragraph (the handles are `b_01` through `b_07` and `register metadata`); a senior preparer reads the tables in input-order, not in lockstep `b_01` → `b_07` order.
