---
name: insurance-outsourcing-review
description: |
  Drafts a second-line oversight pack for an insurance outsourcing or delegated-authority arrangement (MGA, MGU, TPA, claims administrator, underwriting bureau, IT or actuarial outsourcer) read against the NAIC outsourcing and holding-company family and the NAIC Insurance Data Security Model Law. The pack carries the holding-company status, producer-licensing posture, contractual-control review, third-party-service-provider clauses, claims-handling oversight, premium-handling posture, vendor-AI exposure, ORSA fit, named gaps with citations, and a recommended supervisor disposition. The audience is state-DOI exam-grade.

  Best for:
  - A US insurer or reinsurer is onboarding, renewing, or remediating an MGA, MGU, TPA, or claims-administrator arrangement and second-line needs the pre-decision review.
  - A market-conduct exam, ORSA cycle, or internal audit has flagged outsourced-function oversight and the team is preparing the response file.
  - A reinsurer is reviewing a cedent's delegated-underwriting authority arrangement before treaty placement or renewal.

  Not the right tool when:
  - The counterparty is a generic IT or SaaS vendor with no delegated underwriting, claims, premium-handling, or policyholder-data role (use `third-party-operational-resilience/vendor-diligence` with the insurance overlay instead).
  - The work is a cyber-incident response at an outsourced provider (use `risk-reporting/cyber-disclosure-readiness` with the insurance overlay).
  - The exposure is captive-reinsurance or affiliate-reinsurance solvency (different model law family; out of scope).
argument-hint: "[arrangement: counterparty type, delegated functions, states of operation, lines of business]"
---

# Insurance outsourcing review

An insurance outsourcing review is what second-line produces so the named approver — TPRM committee for an operational arrangement, ERM lead where the function is ORSA-material, AI risk committee where vendor-AI is in scope, depending on firm-overlay — can decide on an MGA, MGU, TPA, claims administrator, or other delegated-authority arrangement. The audience downstream is the state insurance department on market-conduct examination. The artifact reads as oversight evidence, not as a contract abstract.

This skill produces the pack as a Word memo following the named sections in `templates/default-output.md`. The skill stops at the recommended disposition; the named approver closes.

## Ask first

Before drafting, get plain answers to a few things. Defaults are fine when an answer is missing; flag the default in the pack.

- **Which counterparty type and which functions are delegated.** The model laws that apply key off both. An MGA with binding authority pulls Producer Licensing in; a TPA without producer activity does not. A claims-touching TPA pulls the Unfair Claims Settlement Practices Act (NAIC Model #900) plus the relevant state acts in; an IT outsourcer does not.
- **Which states is the function operating in.** State-by-state model adoption (Insurance Data Security Model Law, AI Bulletin, TPA Acts, state-DOI bulletins) drives which named anchors load. Operating footprint also drives the per-state per-individual producer-licensing read.
- **Is the counterparty an affiliate.** The Form D filing trigger under the Holding Company Model Regulation depends on the answer. The procedural filing is the line the exam picks up first.
- **Has the counterparty deployed AI on the carrier's policies.** The vendor-AI line in the pack is explicit. The negative answer is also a finding.
- **What is the carrier's ORSA materiality threshold.** The ORSA-fit answer reads against the carrier's threshold, not against feel.

When `engagement-scope` is supplied, the skill consumes it (institution type, sector overlay set, cross-cutting overlay set, persona, source posture). When it is not supplied, ask the questions above, default to public posture if the practitioner declines, and note in the pack that scope was not formalised.

## How the pack gets built

The pack has the same spine across counterparty types. A senior reviewer fills it in roughly in the order the engagement and the evidence offer, not in lockstep. Cite a source for every material claim into `references/source-anchors.md`; mark unsupported claims `[evidence needed]`; mark unconfirmed model-law subsections `[verify section]` rather than fabricating.

The arrangement summary opens the pack: counterparty type, functions delegated, states of operation, lines of business, premium and claims volumes, and the inherent-risk read on what the carrier is exposed to if the function fails or misperforms. This is what later sections read against.

Holding-company status and Form D posture are next. Affiliate or non-affiliate; ultimate controlling person where affiliate; Form B filing reference; Form D applicability with citation. The negative answer is carried explicitly. A non-affiliate posture with the citation in place is itself the evidence the exam looks for.

Producer-licensing and binding-authority posture sits alongside. Per-state per-individual licensing where binding, quoting, issuance, premium-collection, or producer authority is exercised. Appointment status by state runs alongside licensing. Where authority is not delegated, the section reads "not applicable" with a note rather than being omitted.

Contract-control review against NAIC outsourcing expectations runs the clause families: audit rights and books-and-records access by the carrier, commissioner / state-DOI examination access flow-through, sub-delegation restrictions and consent, indemnification, termination and transition assistance, performance-standards and SLA reporting. Each clause family takes a present / partial / absent status with a citation. Commissioner access is the insurance-specific clause that the bank-flavoured generic skill does not name; carry it as its own line.

The Insurance Data Security Model Law §4.F third-party-service-provider review is the cyber-and-data spine. Due-diligence file before contract; the §4.F written-contract clause set; ongoing monitoring posture; incident-response cooperation language; the breach-notification chain from the counterparty up to the carrier and onward to the carrier's regulators against the carrier's downstream notification clocks; sub-processor visibility and the change-notice mechanism; state-by-state §4.F adoption status in the operating footprint with citation to the NAIC adoption tracker. Where the operating footprint includes a non-adopting state, pivot to the operative state-specific cyber frame; the cross-cutting cyber overlay carries the read.

Claims-handling oversight runs against the NAIC Unfair Claims Settlement Practices Act (Model #900) and the relevant state unfair-claims-settlement-practices acts. Acknowledgement, investigation, and decision timing; reasoned-denial drafting and the named human-review checkpoint; complaint flow from policyholder through TPA back to the carrier; denial-letter sample review with scope, sample size, and findings. UDAP exposure attaches to the carrier of record; the TPA's letters are the carrier's letters for that purpose. Where the function is not claims-touching, the section reads "not applicable" with a note.

Premium-handling and fiduciary-account posture is its own section, not a subline under claims. Fiduciary-account structure, segregation, reconciliation cadence, exception register, state TPA-act fiduciary requirements applied. Where the counterparty does not collect or hold premium, the section reads "not applicable" with a note.

Vendor-AI exposure is an explicit named line, not a footnote. AI tools deployed by the counterparty on the carrier's policies (underwriting AI, rating ML, claims-AI, FNOL chatbot, severity prediction, fraud-indicator routing, agent-AI co-pilot, OCR / document-AI, marketing-AI to policyholders); carrier notice and contractual coverage of each tool; AIS Program elements evidenced (governance, risk management, testing, validation, third-party-AI accountability, monitoring, documentation, transparency, fairness); cross-link to AI evidence-pack review where the deeper "is this evidence pack sufficient" question chains to `ai-governance-model-risk/llm-vendor-evidence-review`. The negative answer is recorded with a citation; the next-review trigger includes any change in AI-use posture.

ORSA fit reads against the carrier's own materiality threshold. The pack records included / recommended / not-recommended / not-applicable, cross-links to the ORSA cycle and the ERM lead, and where the threshold is not in evidence flags ORSA-fit as `[evidence needed]` rather than answering from feel.

The pack closes with gaps, issues, and a recommended disposition: approve, approve-with-conditions, remediate-then-re-review, or decline. Conditions are specific and verifiable. The skill stops at the recommendation; the named sign-off owner closes. Open items name owner and target date. Source trace cites by section into `references/source-anchors.md` and the loaded overlays.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/insurance.md` — the insurance frame this skill walks; load with every invocation.
- `references/cross-cutting/cyber.md` — Model #668 cyber components, NYDFS 500.11 where applicable; load whenever the function touches information systems or policyholder data.
- `references/cross-cutting/privacy.md` — HIPAA business-associate posture for life and health flows; state insurance information-and-privacy framework; load whenever PHI or NPI is in scope.
- `references/firm-overlay.md` — firm-installed policy, taxonomy, named approvers, ORSA materiality threshold, internal AI register; consumed when present.
- `templates/default-output.md` — pack template.
- `examples/` — binding-authority MGA renewal across 12 states; life carrier renewing a TPA for closed-block claims administration.
- `TROUBLESHOOTING.md` — recurring defects.

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/public-regulatory-scenarios.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Output

Default to drafting against `templates/default-output.md`. Render as Word, Excel, PowerPoint, or Markdown when the audience or workflow asks for it; the typical deliverable is a Word memo via the `docx` skill in the `document-skills` plugin. Downstream consumers: `risk-reporting/risk-committee-pack` reads the disposition and the ORSA-fit line where the function is enterprise-material; `ai-governance-model-risk/llm-vendor-evidence-review` reads the linked record where vendor-AI is chained.
