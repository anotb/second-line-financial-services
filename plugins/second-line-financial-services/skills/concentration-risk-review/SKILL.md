---
name: concentration-risk-review
description: "Assess third-party concentration across vendors, fourth parties, geographies, and services."
argument-hint: "[portfolio scope: entities, register source, cycle (annual / pre-contract / supervisor-request / stress-event), criticality cutoff]"
---

# Concentration risk review

A concentration review is what second-line produces so the operational-resilience committee, the head of TPRM, the head of operational resilience, and the chief risk officer can see the portfolio-level picture that a per-arrangement diligence pack cannot. The work is reading the firm's third-party arrangements as a portfolio across several concentration dimensions, comparing observed posture against named thresholds and substitutability tests, and naming the concentrations that warrant committee attention. The skill stops at the recommendation. The named forum decides.

This skill produces the artifact as a concentration matrix and committee narrative (`templates/default-output.md` shape) and a structured record (`schemas/concentration-review.schema.json`) that downstream skills and the firm's reporting pipeline consume. The same workflow handles the annual portfolio cycle and the per-arrangement preliminary-assessment cycle that EU regimes require before contracting or recontracting a critical-or-important function; cycle type drives depth, audience, and the dimension cutoffs.

## When to use

Drafts a portfolio-level concentration view across the firm's third-party arrangements. Reads single-vendor concentration, sub-contractor (fourth-party) concentration, geographic and jurisdictional concentration, technology-stack concentration (hyperscaler region, foundation-model vendor, shared utility), and sponsor-bank or BaaS concentration against named supervisory thresholds and substitutability tests. Output is a concentration matrix, the concerning concentrations flagged for committee, and a substitutability-grounded recommendation set. The skill stops at the recommendation; the head of TPRM, head of operational resilience, and CRO office decide.

Best for:
- An annual third-party portfolio review where leadership wants the concentration picture across vendors and fourth parties.
- An ICT third-party preliminary concentration assessment cycle in an EU-nexus regime where the firm must form a view before contracting or recontracting a critical-or-important function.
- A specific arrangement diligence pack flags concentration as a residual concern and chains here via `concentration_flag = watch` or `breach`.
- A supervisory information request on cloud, market-data, identity-utility, or shared-fintech concentration.
- Stress-event readiness: the firm wants to know which single failure removes the largest set of critical-or-important services at once.

Not the right tool when:
- The firm's third-party register or DORA register is not populated to a useful level (run `dora-register-builder` first where DORA applies, or rely on the firm's TPRM register).
- The question is single-arrangement diligence (use `vendor-diligence`).
- The question is single-arrangement exit posture (use `exit-plan`).
- The question is single-arrangement contract clause coverage (use `contract-gap-review`).
- The question is whether one arrangement is critical-or-important (use `criticality-assessment`).

## Ask first

Before drafting, settle five things. The analysis is portfolio-wide and identifier-driven, so a missing answer upstream propagates across every dimension.

- **Which legal entities are in scope, and at what consolidation level.** Individual, sub-consolidated, or consolidated. A subsidiary's concentration picture differs from the parent's. A multi-entity group with shared vendors carries cross-entity concentration the per-entity register will miss; resolve at scope, not in the dimension-by-dimension findings.
- **Cycle type and audience.** Annual portfolio cycle for the operational-resilience committee, pre-contract preliminary assessment for a single critical-or-important function, supervisor-information-request response, post-incident or stress-event readiness review. Each cycle has a different criticality cutoff, a different reviewer-question cluster, and a different review-gate posture. An annual cycle reads across the whole register; a pre-contract cycle reads narrowly against the proposed arrangement and the existing portfolio it would join.
- **Source register and criticality posture.** Which register feeds the analysis: the firm's TPRM register, the DORA register of information where DORA applies, the EBA outsourcing register where the firm has one, or a hybrid view. Each carries a quality caveat. Criticality classification must already exist for in-scope arrangements (sourced from `criticality-assessment` or the firm's tiering); the concentration review consumes the tier, it does not set it. A register where most arrangements carry `criticality = unknown` is not yet usable for concentration; route back to `criticality-assessment` or scope the analysis to the subset that is classified.
- **Fourth-party visibility posture.** How deep the sub-contractor chain is documented in the source register. Concentration that lives at rank 2 or rank 3 of a sub-contractor chain is the concentration the firm does not see in a vendor-by-vendor read. A register that stops at rank 1 limits the analysis; the limitation is itself a finding and goes in the data-quality caveats.
- **Sector overlay set and source posture.** Which of {banking, insurance, capital-markets, payments-fintech} apply. A dual-registrant or a fintech with a sponsor-bank arrangement may carry two. Source posture (public-only, public-plus-firm-policy, public-plus-firm-policy-plus-system-of-record-evidence, connector-aware) drives the evidence ask and the confidence label on the artifact.

When the scope record is supplied, the skill consumes it for institution type, sector overlay set, cross-cutting overlay set, persona, and source posture. When it is not supplied, ask the questions above and default to public posture if the practitioner declines. Do not silently apply a sector overlay default.

## How the review gets done

The review has the same spine across cycle types. A senior practitioner walks it in roughly the order the register and the criticality data land, not in lockstep. The structured record sorts itself; the committee narrative reads in the order below.

### Scope, source posture, data-quality caveats

Open by naming the in-scope legal entities, the source register and its date, the consolidation level, and the criticality cutoff applied (the analysis usually focuses on critical-or-important arrangements and on important-business-service-supporting arrangements; including non-critical arrangements adds noise without committee value). Record the source-data caveats: missing identifiers, sub-contractor-chain visibility limits, criticality-classification gaps, intra-group arrangements that should be flagged but are not, vendor-restructuring records where the legal entity moved but the arrangement persists. A clean-looking concentration view with no caveats reads as either complete (rare) or unaware (more common).

### The dimensions

Concentration is multi-dimensional. The same arrangement shows up in several dimensions and the same dimension is read at several levels. The committee read needs each dimension surfaced explicitly with its own metric, threshold reference, observed distribution, and severity label.

**Single-vendor concentration.** Counted by criticality-tier-weighted arrangement count and by transaction or operational-volume share where the firm has the metric. Spend correlates poorly with operational dependency; substitute it with criticality-weighted count and time-to-substitute. The threshold reference is the firm's own concentration tolerance (where set in policy) and the supervisory framing in the named source anchors. A vendor that carries multiple critical-or-important arrangements across business lines is concentration even when each arrangement looks moderate alone.

**Sub-contractor (fourth-party) concentration.** Two failure modes. The known fourth party that several first-line vendors share (a single identity verifier behind three KYC vendors; a single SMS gateway behind several MFA vendors; a single AI inference provider behind several SaaS products). The unknown fourth party that the register has not surfaced because visibility stops at rank 1. Both belong here; the unknown-fourth-party finding routes to the data-quality caveat and to a re-ask of the relevant `vendor-diligence` packs. For ICT services supporting critical or important functions in the EU perimeter, the sub-contracting RTS sets the frame for sub-contractor-chain visibility (cited in `references/source-anchors.md`).

**Geographic and jurisdictional concentration.** Country-level data-residency concentration (where data at rest and data processing physically sit), sub-region concentration within a single country (multiple critical arrangements in one hyperscaler sub-region of one country), and jurisdictional concentration (governing law and dispute-resolution forum, regulator concentration, sanctions-regime exposure). Cross-border data flows are a supervisory focus and surface here. Region-pin promises are promises; data-residency reports are evidence.

**Technology-stack concentration.** Hyperscaler concentration (the share of critical-or-important arrangements running on each hyperscaler, then by region, then by sub-region; treating multi-region as multi-resilience is the recurring error). Foundation-model-vendor concentration (the share of AI use cases dependent on a single foundation-model API, surfaced as its own dimension because it is a concentration the firm typically did not have eighteen months ago). Shared-utility concentration (KYC utilities, sanctions screening, market-data feeds, identity verifiers, transaction-monitoring utilities, post-trade processors that the firm shares with peers; sector-wide concentration shows up as the firm's idiosyncratic risk under stress). Single-database-vendor and single-OS-vendor concentration are read here too where the operational dependency is real.

**Sponsor-bank, BaaS, BIN-sponsor, and rails concentration (payments-fintech).** Where the firm uses a single sponsor bank for deposit products, a single BIN sponsor for card issuance, a single BaaS partner for ledger services, or a concentrated set of payment-rail access points (FedNow, RTP, ACH, card networks, cross-border correspondent), this dimension reads explicitly. Surfacing it under "single vendor" alone undercounts the dependency.

**Critical-or-important-function-level concentration.** Reads the dimensions back through the function lens: which critical-or-important functions depend on the same vendor, the same hyperscaler region, the same fourth party, the same shared utility. A single-points-of-failure section names the functions where one failure removes the function entirely with no ready substitute.

**AI-provider concentration.** Surfaced as its own dimension when AI is in scope. Single foundation-model vendor across many AI use cases; single inference-region; single fine-tuning provider for the firm's customised models; single retrieval-augmentation vendor. Treat as a fast-growing concentration and re-test on a shorter cycle than the rest of the portfolio.

### Substitutability read

A list of concentrations without a substitutability test is descriptive, not useful. For each concentration flagged at `watch` or `breach` severity, the review names what substitutability looks like: alternative vendors known to the firm, time-to-substitute estimate, contractual portability posture (data portability, exit-cooperation duty, transition-services duty; chain to `exit-plan` for the per-arrangement exit posture and to `contract-gap-review` for the clause read), operational substitutability (the firm's own ability to switch under realistic operational conditions), and stressed-substitutability (the same test under a wider sector-event scenario where the substitute itself may be in demand). A concentration with high apparent substitutability under benign conditions can collapse to zero substitutability under sector stress; the read names the difference.

### Findings, recommended actions, reviewer questions

Concentrations that warrant committee attention surface as findings with severity, dimension, affected functions, and the substitutability read. Recommended actions name the action, the owner role (head of TPRM, head of operational resilience, CRO office, ICT-asset owner, business owner SVP), the rationale, and the dependency on other skills (a `contract-gap-review` re-run, an `exit-plan` refresh, a `resilience-testing-pack` scenario test). The skill drafts the recommendations; the named forum decides.

Reviewer questions tie to the decision and cluster for the forum that decides: operational-resilience committee for portfolio findings, TPRM forum for vendor-by-vendor follow-ups, risk committee for findings that change the firm's risk-appetite read, board for findings that move concentration above board-level thresholds. Name the decision checkpoints the artifact must clear (scope, evidence, authority, impact, decision) and the conditions attached to each.

### Sector and cross-cutting overlay loading

When the scope names a sector, load the matching `references/sector-overlays.md#<sector>`: `banking.md` for the hyperscaler-on-bank, sponsor-bank-on-fintech, and large-bank-cloud-concentration framings; `insurance.md` for policy-administration-system, reinsurance, and claims-TPA concentration; `capital-markets.md` for market-data-vendor, exchange-feed, central-counterparty, and post-trade-processor concentration; `payments-fintech.md` for sponsor-bank, BIN-sponsor, BaaS, and rails-access concentration. A dual-registrant or BaaS arrangement may load two.

The cyber cross-cutting overlay (`references/cross-cutting.md#cyber`) loads when the technology-stack and sub-contractor-chain dimensions surface cyber-risk material to the supervisory read (a single cyber-incident that removes multiple critical arrangements, a shared-utility incident that propagates across the firm and its peers). Privacy considerations are read through the geographic-and-jurisdictional dimension (cross-border data flows, data-residency posture); the deeper privacy treatment lives with `vendor-diligence` and the privacy-overlay file there. Load only the overlays the scope names.

## Quality bar

Holds across every review regardless of cycle type, audience, or render format.

- **The register feeds the analysis; the skill does not invent the portfolio.** Where the register is incomplete, the analysis is scoped to the usable subset and the limitation is a data-quality caveat. Filling gaps with inferred entries is a defect, not a workaround.
- **Criticality is consumed, not set.** The concentration review reads the criticality tier set elsewhere. A register where critical-or-important is not yet classified is not yet usable.
- **Fourth-party visibility is part of the read.** Stopping at rank 1 of the sub-contractor chain limits the dimension and the limit is named.
- **Each concentration finding carries a dimension, a metric, a threshold reference, an observed posture, a substitutability read, and a severity label.** A finding without a substitutability read is descriptive, not actionable.
- **Spend is not the metric.** Criticality-weighted count, transaction or operational-volume share where available, function dependency, and time-to-substitute are the metrics.
- **Multi-region is not multi-resilience by default.** Two regions of the same hyperscaler share control plane, identity layer, and billing operation; the substitutability read names what fails together.
- **Source trace.** Every material claim cites `references/source-anchors.md` (or a loaded overlay) by path. Section references that cannot be confirmed get `[verify section]` rather than fabricated. Unsupported items go to the engagement issue log, not silently into the artifact.
- **The skill stops at the recommendation.** The artifact carries reviewer questions, named decision checkpoints, and recommended actions. The operational-resilience committee, the head of TPRM, the head of operational resilience, and the CRO office decide. Where the cycle is the EU pre-contract preliminary assessment, the legal artifact is the firm's signed assessment; this skill is the draft input and requires legal and compliance sign-off before becoming the legal record.
- **No named institutions in narrative unless they are public defendants in a finalised enforcement action with a published consent order.** Sector pattern claims are abstracted from public-source-derived examples in `examples.md`.

## Adaptation

Flexes by engagement.

- **Review depth scales to cycle type and audience.** Annual portfolio cycle runs broad with all dimensions. Pre-contract preliminary assessment runs narrow against the proposed arrangement and the portfolio it joins; the dimensions that the proposed arrangement materially moves are read in depth, the others are summarised. Supervisor-information-request runs to the question. Stress-event readiness leads with single-points-of-failure and the substitutability read under stressed conditions.
- **Audience drives shape.** A pack for the operational-resilience committee reads operational. A pack for the CRO office leads with the residual concentration posture and the risk-appetite implications. A pack for board reads as a justification of the firm's own concentration tolerance. A pack supporting a supervisor dialogue reads as a justification of the firm's posture before the supervisor asks.
- **Sector overlay loading follows the scope.** Dual-registrant or BaaS arrangements load two.
- **Source posture drives the evidence ask** and the confidence label on the artifact.
- **Render format follows the workflow.** Default to the markdown narrative; render as Word, Excel, or PowerPoint when the audience or workflow asks for it (an annual board pack often wants a deck; a portfolio cut often wants a workbook).
- **Firm-specific concentration tolerances, named owners, internal-to-supervisory threshold mapping, and policy thresholds** sit in `references/firm-overlay.md`, consumed when present, never in the artifact directly.

## Output

Two artifacts: the structured record per `schemas/concentration-review.schema.json`, and the committee narrative per `templates/default-output.md`. The structured record is the cross-skill contract; the narrative is what the named forum reads before deciding.

Downstream consumers: the firm's risk-reporting pipeline reads the structured record for portfolio-level reporting; `vendor-diligence` re-runs may be triggered by a finding (a `concentration_flag = breach` raised at the portfolio level routes back to the per-arrangement diligence); `exit-plan` is invoked for arrangements where the substitutability read is weak and exit posture must be tested; `resilience-testing-pack` consumes the single-points-of-failure list to design severe-but-plausible scenarios; `dora-register-builder` does not consume this output (the register feeds this skill, not the other way), but the data-quality caveats raised here often loop back as `dora-register-builder` findings on the next refresh cycle.

The schema is additive only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.

## Pointers

`references/sector-overlays.md` and `references/cross-cutting.md` hold one section per sector or topic, and `examples.md` one per example. Find the heading and read only that section.

- `references/source-anchors.md` ... citations and verification posture for the named anchors.
- `references/sector-overlays.md#banking`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` ... sector-specific concentration framings loaded per scope.
- `references/cross-cutting.md#cyber` ... cyber cross-cutting frame loaded where the technology-stack and sub-contractor-chain dimensions surface cyber-risk material to the supervisory read.
- `references/firm-overlay.md` ... firm policy, named owners, concentration tolerances, internal-to-supervisory threshold mapping (consumed when present).
- `templates/default-output.md` ... committee narrative template.
- `schemas/concentration-review.schema.json` ... structured-output contract for downstream consumption.
- `examples.md#annual-bank-portfolio-review`, `examples.md#dora-preliminary-assessment-eu-insurer` ... anonymised public-source-derived scenarios: an annual portfolio review at a US regional bank surfacing hyperscaler-region and KYC-utility concentration; an EU insurer pre-contract preliminary assessment for a critical-or-important ICT service surfacing sub-contractor-chain and sub-region concentration.
- `examples.md#troubleshooting` ... recurring defects (legal-entity-only counting, treating spend as the metric, multi-region as multi-resilience, ignoring shared utilities, skipping AI-provider concentration, lists without substitutability reads, treating the artifact as the legal preliminary assessment).

Plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
