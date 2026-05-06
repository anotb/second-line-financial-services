# vendor-diligence — Phase 1 spec sheet

Plugin: `third-party-operational-resilience`
Phase: 1 (per-skill scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Activation-tuned description

```
Drafts a second-line vendor diligence pack for a single ICT, fintech, cloud, data, or AI service provider. Captures inherent risk, criticality input, due-diligence evidence read against named regulatory criteria, residual risk, exit posture, and the gaps a control owner needs to close before onboarding or recertification.

Best for:
- A first-line owner has proposed a new ICT, fintech, cloud, data, or AI vendor and second-line needs the pre-onboarding diligence pack.
- A vendor risk team is recertifying an existing critical or important vendor on its annual cycle and the prior pack is stale or thin.
- An AI vendor (foundation-model API, AI SaaS, embedded-AI feature in an existing platform) needs diligence and the firm wants the second-line lens, not a procurement checklist.

Not the right tool when:
- The criticality tier has not been set (use criticality-assessment first; vendor-diligence consumes its output).
- The job is a portfolio-level concentration view across many vendors (use concentration-risk-review).
- The job is contract clause coverage only (use contract-gap-review).
- The vendor evidence is a published system card or model report and the question is "is this evidence pack sufficient" (use llm-vendor-evidence-review in ai-governance-model-risk for that narrower question; vendor-diligence is the firm-side wrapper around it).

Anchored to: Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023) §III due-diligence and selection [verify section]; OCC Bulletin 2013-29 (predecessor; still cited in supervisory practice) due-diligence and selection sections [verify section]; FFIEC IT Examination Handbook — Outsourcing Technology Services, vendor-management sections [verify section]; DORA (Regulation (EU) 2022/2554) Articles 28-30 ICT third-party risk; EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02) §13 pre-outsourcing due diligence [verify section]; NYDFS 23 NYCRR 500.11 third-party service provider security policy; NIST AI RMF 1.0 Govern and Map functions for the AI-vendor scenario.
```

## Source anchors

Named, dated, with section refs. `[verify section]` where unsure.

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, issued June 6, 2023). Sections used: planning, due diligence and third-party selection, contract negotiation, ongoing monitoring, termination [verify section numbering]. OCC release: https://www.occ.gov/news-issuances/news-releases/2023/nr-ia-2023-53.html. FDIC release: https://www.fdic.gov/news/press-releases/2023/pr23047.html.
- OCC Bulletin 2013-29 — Third-Party Relationships: Risk Management Guidance (still cited as predecessor framing in supervisory practice). Due-diligence and selection criteria [verify section].
- FFIEC IT Examination Handbook — Outsourcing Technology Services booklet. Risk assessment, due diligence, contract issues, ongoing monitoring sections [verify section].
- DORA — Regulation (EU) 2022/2554, Articles 28 (general principles), 29 (preliminary assessment of ICT concentration risk), 30 (key contractual provisions). Cross-referenced for any EU-nexus or in-scope subsidiary. Article 28(2) requires firms to maintain ICT third-party risk management proportionate to size and risk profile [verify subarticle].
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02). Pre-outsourcing due diligence guideline [verify section number]; sub-outsourcing guideline [verify section]; outsourcing register guideline (cross-referenced; primary anchor for that artifact is `dora-register-builder`).
- NYDFS Part 500 — 23 NYCRR 500.11 Third-Party Service Provider Security Policy. Identification, risk assessment, minimum cybersecurity practices, due diligence, periodic assessment.
- For AI-vendor scenario: NIST AI RMF 1.0 Govern function (third-party considerations) and Map function (context); NIST AI RMF Generative AI Profile (NIST AI 600-1) for GenAI-specific vendor diligence considerations [verify subsection]; ISO/IEC 42001:2023 §7.4 communication and §8.4 third-party AI considerations [verify subclause]; OCC/FRB supervisory letters on AI use in banking where applicable.
- Cross-references inside this plugin: criticality-assessment (criticality input is consumed here), contract-gap-review (contract coverage findings are consumed here), exit-plan (exit posture summarised here, fully developed there), concentration-risk-review (concentration flag raised here, full analysis there).

## Sector overlays needed

All four. Vendor diligence is sector-shaped because the supervisory frame and the "what counts as critical" call differ by sector.

- `references/sector-overlays/banking.md` — interagency guidance (June 2023) is the primary frame. Capital, deposits, payments, lending dependencies. OCC heightened-standards considerations for large banks. Fed third-party guidance for FBOs.
- `references/sector-overlays/insurance.md` — NAIC Model Law on insurance outsourcing; state department of insurance expectations; AI-vendor diligence under the NAIC Model Bulletin on the use of AI by insurers (2023) for the AI-vendor scenario; Form B and Form F holding-company filings where the vendor is an affiliate.
- `references/sector-overlays/capital-markets.md` — SEC Regulation SCI for SCI entities; FINRA Notices on vendor management (e.g., 21-29) for broker-dealers; CFTC system safeguards for DCMs/SEFs; market-data vendor specifics (consolidated tape, exchange feeds).
- `references/sector-overlays/payments-fintech.md` — interagency third-party risk management guidance applies to community banks engaging fintech partners (joint statement, August 2023, "Conducting Due Diligence on Financial Technology Companies"); BSA/AML inheritance through banking-as-a-service relationships; payments-network rules (card-network compliance, NACHA originator due diligence).

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — NYDFS Part 500.11; SEC cyber disclosure rule (Item 1.05 8-K and Reg S-K Item 106) where the vendor sits on the disclosure path; CISA shared-responsibility model for cloud; FFIEC IT Handbook Information Security booklet; SOC 2 Type II read-through expectations; pen-test and vulnerability-management evidence read.
- `references/cross-cutting/privacy.md` — GLBA Safeguards Rule (Standards for Safeguarding Customer Information, 16 CFR Part 314 as amended) where the vendor processes nonpublic personal information; state privacy laws (CCPA/CPRA, VCDPA, CTDPA, etc.) where the vendor handles consumer personal information; HIPAA business-associate posture where the vendor touches PHI; for AI vendor, training-data-provenance and model-input-retention questions.

## Output template named sections

`templates/default-output.md` should produce a vendor diligence pack with these sections (practitioner headings):

1. Vendor and arrangement
2. Service description and business process supported
3. Inherent risk and criticality input (from `criticality-assessment`)
4. Data scope (categories, volumes, locations, retention, cross-border flows)
5. Subcontractor and fourth-party landscape
6. Financial condition and going-concern read
7. Information security and resilience evidence read
8. Privacy and data protection evidence read
9. Business continuity and disaster recovery evidence read (RTO/RPO claimed vs evidenced)
10. Regulatory and legal posture (sanctions, litigation, enforcement, jurisdictional posture)
11. Contract coverage summary (link to `contract-gap-review` output)
12. Exit and substitutability posture (link to `exit-plan` output)
13. Concentration considerations (link to `concentration-risk-review` output)
14. AI-specific considerations (only when AI vendor; otherwise omit)
15. Residual risk after controls
16. Open questions and evidence gaps
17. Reviewer questions for human approver
18. Source trace and confidence labels

The AI-specific section (14) covers: model provenance and training-data posture; evaluation evidence (intended use, benchmarks, red-team results); shared-responsibility model for safety, content moderation, and abuse handling; fine-tuning, RAG, and customer-data-isolation posture; system-card or model-report read for fitness against the firm's deployment context; agent-tool-use posture if the vendor offers agentic capabilities.

## Structured output fields

Anchor: `schemas/vendor.schema.json` (existing; extends in phase 2 to carry the AI-vendor fields).

Fields produced by this skill (type, purpose):

- `arrangement_id` (string) — stable ID for the vendor arrangement
- `vendor_legal_name` (string) — counterparty legal entity name
- `service_type` (string) — concise service description (e.g., "cloud IaaS", "core banking SaaS", "foundation-model API")
- `business_process_supported` (string) — name of the firm's business process or important business service supported
- `criticality` (enum: `not-critical | important | critical | unknown`) — sourced from `criticality-assessment`
- `data_access` (array of string) — categories of firm/customer data the vendor accesses (NPI, PHI, PCI, prompts, model outputs, etc.)
- `subcontractors` (array of string) — material fourth parties known
- `subcontractor_visibility` (enum: `full | partial | none`) — how much of the chain is visible
- `cyber_evidence_status` (enum: `sufficient | partial | missing`) — read-through status of SOC 2, ISO 27001, pen-test, vuln scan
- `bcdr_rto_claimed` (string), `bcdr_rpo_claimed` (string), `bcdr_evidence_status` (enum) — claimed vs evidenced recovery objectives
- `privacy_evidence_status` (enum) — read-through of privacy program evidence
- `financial_condition_status` (enum: `sound | watch | concern | unknown`) — financial-condition read
- `regulatory_posture_flags` (array of string) — sanctions, enforcement, litigation, jurisdictional risk
- `contract_gap_summary` (string) — pointer to or summary of `contract-gap-review` output
- `exit_plan_status` (enum: `complete | draft | missing | not-applicable`) — pointer to `exit-plan` output
- `concentration_flag` (enum: `none | watch | breach`) — pointer to `concentration-risk-review` output
- `ai_vendor` (boolean) — whether the AI-vendor mode applies
- `ai_specific_findings` (object, conditional on `ai_vendor=true`) — sub-fields: `model_provenance`, `training_data_posture`, `eval_evidence_status`, `shared_responsibility_clarity`, `fine_tune_data_isolation`, `agent_tool_posture`, `system_card_fit_to_deployment`
- `residual_risk` (enum: `low | medium | high | unacceptable`)
- `open_evidence_gaps` (array of string)
- `reviewer_questions` (array of string)
- `confidence_label` (enum: `high | medium | low | unknown`) — per `references/review-gates.md`
- `owner` (string) — role, not person
- `source_trace` (array of object: `claim`, `source`, `section`, `date`)

## Example scenarios (two, public-source-derived)

Both are anchored to public regulatory sources and avoid named institutions.

1. **Cloud IaaS for a regional bank's core deposit and loan platform.** Inputs: vendor public certifications (SOC 2 Type II summary, ISO 27001 statement of applicability), the firm's draft criticality output (critical), the proposed data flow (NPI in transit and at rest, region-pinned), and the fourth-party hyperscaler sub-region used. Anchored to: interagency guidance (June 2023) due-diligence and contract sections; FFIEC IT Handbook Outsourcing Technology Services booklet; NYDFS 500.11. The output identifies evidence gaps on key-management posture (BYOK vs vendor-managed), defines the BCDR evidence read against the firm's RTO/RPO, and flags the hyperscaler sub-region for concentration analysis.

2. **AI vendor — foundation-model API used by a property-and-casualty insurer for first-notice-of-loss triage.** Inputs: the vendor's published system card, the vendor's evaluation report, the proposed deployment architecture (the insurer routes claim narratives to the API and uses outputs to suggest a triage tier), claims-handling regulatory context. Anchored to: NAIC Model Bulletin on the use of AI by insurers (2023) third-party-AI section; interagency third-party guidance (June 2023) at the insurer's bank affiliate if applicable; NIST AI RMF 1.0 Govern function; NIST AI 600-1 GenAI profile [verify subsection]. The output identifies that the published system card does not address claim-narrative inputs containing PII and PHI, that the vendor's evaluation report does not cover the insurer's use case (FNOL triage), and that the shared-responsibility model on prompt-injection abuse handling is unclear. It does not approve the vendor; it produces the diligence pack and the reviewer questions for the AI committee and the chief risk officer.

## Common pitfalls

1. **Treating a published system card as a substitute for vendor-specific evidence on the firm's deployment context.** A system card describes the model on the vendor's benchmarks and intended use. It does not describe how the model performs on the firm's prompts, the firm's customer data, the firm's regulatory context, or the firm's downstream decisioning. The diligence pack must call this out explicitly and request deployment-context evidence.
2. **Conflating SOC 2 Type II coverage with control sufficiency.** SOC 2 reports cover the auditor's selected criteria over the auditor's selected period. Read scope, exceptions, and complementary user entity controls. A clean SOC 2 with critical complementary user entity controls unaddressed by the firm is not a green light.
3. **Skipping fourth-party visibility because the contract has flow-down clauses.** Flow-down does not equal visibility. The pack must show what the firm actually knows about the subcontractor chain and where visibility stops.
4. **Treating procurement-led RFP responses as evidence.** RFP responses are vendor self-attestation. Diligence requires inspectable artifacts (audit reports, pen-test summaries, BCDR test reports, breach notification logs).
5. **Setting RTO/RPO to the vendor's claim instead of the firm's tolerance.** The vendor's claim is the ceiling on what the vendor delivers. The firm's impact-tolerance for the supported important business service is the test the vendor must meet.
6. **AI-vendor pitfall — accepting "we do not retain training data from API calls" without reading the API contract and the vendor's published retention/abuse-monitoring posture.** The vendor's privacy and trust-and-safety pages often modify the public default. The pack must cite the vendor's contractual data-handling commitment and the abuse-monitoring exception, not the marketing default.
7. **AI-vendor pitfall — treating a single foundation-model evaluation as coverage for a fine-tuned or RAG-augmented deployment.** The deployed system is not the base model. Evaluation must cover the deployed system, including retrieval quality and grounding behavior.
8. **Missing the cross-cutting privacy lens on AI vendors that process customer prompts.** Customer prompts can carry NPI, PHI, or other regulated data the firm did not intend to share. Privacy overlay must be applied to AI vendors by default.
9. **Skipping the concentration consideration because the vendor "is just one vendor".** Concentration risk is sector-wide, not vendor-by-vendor. Flag it here and pass to `concentration-risk-review`.
10. **Forgetting the exit-plan handoff.** The diligence pack should always reference the exit-plan status. A critical or important vendor without a current exit plan is itself a finding.
