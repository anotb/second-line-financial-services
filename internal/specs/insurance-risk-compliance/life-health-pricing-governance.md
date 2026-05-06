# Spec sheet: life-health-pricing-governance

Plugin: `sector-plugins/insurance-risk-compliance`
Status: v1 retained skill (genuinely insurance-only).
Phase: 1 (spec only; no SKILL.md content here).

## Why this is a sector-only skill

Life and health pricing governance is not the same workflow as `consumer-compliance-fair-lending/fair-lending-test-plan`. The statutory frame is state insurance rate-filing law and the NAIC unfair-discrimination tradition (which is older than fair-lending and reads against a different list of permitted vs prohibited rating factors), the artifact is a rate-filing or rate-review file (SERFF), and the second-line review compares actuarial memoranda and rating-plan exhibits to state DOI bulletins rather than ECOA / Reg B. Capability `fair-lending-test-plan` does not produce an artifact a state DOI rate analyst will accept. This skill does. AI-driven accelerated underwriting and ML-based rating sit on top of the same pricing governance frame, so the skill must absorb the NAIC AI Bulletin December 2023 and state DOI AI bulletins as well.

## Activation-tuned description

```
Drafts a second-line governance review of a US life or health pricing or rating change (new rate filing, refile, accelerated-underwriting model, rating-plan refresh, ML-driven rating factor, post-issue underwriting model) against state insurance rate-filing expectations, NAIC unfair-discrimination standards, and the NAIC AI Bulletin December 2023, with rate-filing summary, rating-factor map, unfair-discrimination analysis, disparate-impact red flags, and named gaps versus state DOI bulletins.

Best for:
- A life or health insurer is preparing or refreshing a rate filing and second-line wants the pricing-governance file before SERFF submission.
- An accelerated-underwriting model or ML-driven rating factor has gone through development and second-line needs the unfair-discrimination and disparate-impact review before deployment.
- A state DOI inquiry on rating factors, AI use, or unfair discrimination has arrived and the carrier is preparing the response file.
- An internal audit or ORSA review is sampling pricing governance for life or health.

Not the right tool when:
- The product is P&C (different rate-regulation model and different unfair-discrimination posture; a P&C-specific skill is out of v1 scope).
- The exposure is fair-lending under ECOA / Reg B for a credit-insurance product underwritten via a bank channel (use consumer-compliance-fair-lending/fair-lending-test-plan with the insurance overlay).
- The use case is claims AI rather than pricing or underwriting (use ai-governance-model-risk/agentic-ai-controls with the insurance overlay).
- The work is reserving, IBNR, or solvency capital rather than pricing.

Anchored to: NAIC Unfair Trade Practices Act (Model #880); NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023); NAIC Principles on Artificial Intelligence (2020); state DOI bulletins on AI in insurance (Colorado SB 21-169 implementing regulation; NY DFS Insurance Circular Letter on AI and ECDIS in life insurance, January 2024; California DOI bulletin on AI use); NAIC Life Insurance Illustrations Model Regulation (Model #582); HIPAA where pricing or underwriting touches PHI; ACA pricing rules where individual or small-group health is in scope; ORSA Model Act (Model #505) where the model is enterprise-material.
```

## Source anchors (skill-specific)

- NAIC Unfair Trade Practices Act, Model #880 — unfair-discrimination prohibition in rates and underwriting; historically the spine of the analysis.
- NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers, December 2023 — AIS Program expectations, vendor accountability, governance, monitoring, transparency, fairness, including for pricing and underwriting AI.
- NAIC Principles on Artificial Intelligence, 2020 — fair / ethical, accountable, compliant, transparent, secure / safe / robust principles.
- NAIC AI Working Group materials, current — Model Bulletin adoption tracker by state.
- Colorado SB 21-169 and the Colorado DOI implementing regulation on governance and risk management of external consumer data and information sources (ECDIS) and predictive models in life insurance underwriting.
- NY DFS Insurance Circular Letter on the Use of AI and External Consumer Data and Information Sources (ECDIS) in Life Insurance Underwriting, January 2024.
- California DOI bulletin on the use of artificial intelligence in insurance.
- NAIC Life Insurance Illustrations Model Regulation, Model #582 — illustration requirements for life pricing.
- HIPAA Privacy Rule (45 CFR Part 164, Subpart E) — PHI use in life and health pricing and underwriting.
- ACA pricing rules (42 USC 300gg; 45 CFR Part 147) — individual and small-group health rating restrictions (community rating, age-band limits, tobacco surcharge).
- ORSA Model Act, Model #505 — pricing-AI exposure in the ORSA Summary Report when material.
- SR 11-7 and OCC Bulletin 2026-13 [verify] — referenced as the model-risk baseline that state DOI exam teams increasingly point to as analogous expectations for ML pricing models.

Date every external source. Treat each as an anchor, not a substitute for legal interpretation.

## Sector overlays needed

Only `insurance` (this is the sector skill).

## Cross-cutting overlays

- `cross-cutting/privacy.md` — required. HIPAA Privacy Rule for life and health pricing that touches PHI; state insurance-information-and-privacy frameworks; consumer-disclosure expectations under NY DFS Circular Letter and Colorado regulation for ECDIS.
- `cross-cutting/conduct.md` — recommended. Consumer-fair-treatment lens on rating factors and on accelerated-underwriting decline / referral flows.
- (Cyber overlay not material at the pricing layer; cyber sits on `insurance-outsourcing-review` and on the AI-vendor overlay.)

## Output template named sections

1. **Rate filing summary.** Product, state(s), filing channel (SERFF), effective date, rationale for change, prior approval status.
2. **Rating factor map.** Each rating factor: source data, statutory permission status (state-by-state where applicable), interaction with prohibited bases, ECDIS status (is the factor derived from external consumer data).
3. **Unfair discrimination analysis.** Application of Model #880 unfair-discrimination standard to each rating factor and to the rating plan as a whole; statistical and actuarial justification check.
4. **Disparate-impact red flags.** Where applicable under state DOI guidance (Colorado, NY DFS, California): proxy-variable risk, ECDIS provenance, monitoring metrics, consumer-recourse channel.
5. **AI / ML rating factor and accelerated-underwriting governance.** AIS Program alignment with NAIC Bulletin Dec 2023: governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness.
6. **Documentation completeness vs SR 11-7-equivalent expectations.** Model documentation, validation evidence, performance monitoring plan, change-management process, ongoing monitoring metrics. (State DOIs increasingly cite SR 11-7 / OCC 2026-13 as analogous expectations; the artifact treats them as a defensible benchmark.)
7. **State DOI bulletin alignment.** Per state in the filing footprint: NAIC Model Bulletin adoption status, Colorado ECDIS regulation if Colorado is in scope, NY DFS Circular Letter if NY is in scope, California bulletin if CA is in scope, plus the standard state DOI rate-filing checklist points.
8. **Privacy and consumer-disclosure posture.** HIPAA where in scope; ECDIS consumer-recourse and adverse-information disclosure where required.
9. **ACA-pricing checks.** Where individual or small-group ACA health is in scope: community-rating, age-band, tobacco-surcharge, and geographic-area compliance.
10. **Illustrations check.** For life: Model #582 illustration requirements where the change touches illustrated values.
11. **Gaps, issues, and recommended disposition.** (Approve / approve-with-conditions / remediate / decline-and-rework.)
12. **Open items, owners, dates.**
13. **Source citations with date.**

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `filing_id` | string | Internal identifier; SERFF tracking number where available. |
| `product_type` | enum (`life`, `health_individual`, `health_small_group`, `health_large_group`, `annuity`, `disability`, `LTC`, `other`) | Drives which statutory frame applies. |
| `states` | array of string | State DOI overlays trigger from this list. |
| `change_type` | enum (`new_filing`, `refile`, `rate_change`, `factor_change`, `model_change`, `accelerated_underwriting_launch`, `accelerated_underwriting_change`) | Drives review depth. |
| `rating_factors` | array of factor | Each factor: name, data source, ECDIS flag, statutory-permission status by state, interaction-with-prohibited-bases note. |
| `ai_ml_components` | array of component | Each component: tool name, vendor, role (rating, underwriting, triage), training-data summary, monitoring metrics. |
| `unfair_discrimination_findings` | array of finding | Model #880 standard applied; actuarial justification status; severity. |
| `disparate_impact_findings` | array of finding | State-DOI-guidance-driven (CO, NY, CA) red flags. |
| `aip_program_findings` | array of finding | NAIC Bulletin Dec 2023 AIS Program element-by-element status. |
| `documentation_findings` | array of finding | Model-documentation completeness vs SR 11-7-equivalent expectations. |
| `state_doi_alignment` | array of state-record | Per-state checklist status against named bulletins. |
| `privacy_findings` | array of finding | HIPAA, ECDIS-disclosure, state-insurance-privacy posture. |
| `aca_findings` | array of finding | ACA pricing-rules posture where in scope. |
| `illustration_findings` | array of finding | Model #582 status where in scope. |
| `gaps` | array of gap | Each gap: description, source citation with date, severity, owner, target close date. |
| `recommended_disposition` | enum (`approve`, `approve_with_conditions`, `remediate_then_re_review`, `decline_and_rework`) | Second-line recommendation, not a decision. |
| `open_items` | array of item | Description, owner, target date. |
| `source_citations` | array of citation | Source name, section / model reference, retrieval date, URL where public. |

## Two example scenarios (public-source-derived, anonymous)

1. **Life carrier launching an accelerated-underwriting program using ECDIS in Colorado and New York.** Public anchors: Colorado SB 21-169 implementing regulation on ECDIS and predictive models in life-insurance underwriting; NY DFS Insurance Circular Letter on AI and ECDIS in life insurance (January 2024); NAIC Bulletin Dec 2023; Model #880. Scenario: AU model uses third-party prescription-history data and a ML-derived score; the governance memo covers AIS Program elements, ECDIS provenance and consumer recourse, unfair-discrimination application of #880, disparate-impact monitoring metrics, and state-by-state alignment for CO and NY.
2. **Health insurer refiling small-group rates with a new geographic-area factor and a vendor-supplied ML risk-adjustment input.** Public anchors: ACA small-group rating rules (45 CFR Part 147); NAIC Model #880; NAIC Bulletin Dec 2023; SR 11-7 / OCC 2026-13 [verify] as analogous model-risk baseline. Scenario: rating-factor map flags the geographic factor as compliant under 45 CFR §147.102; the ML risk-adjustment input is from a vendor; AIS Program third-party-vendor accountability is the open item; documentation against SR 11-7-equivalent expectations is partial; gaps list two state-DOI follow-ups and one privacy clarification.

Both scenarios use only public sources (NAIC Model text, federal regulations, state DOI bulletins, generic carrier and vendor descriptions). No named institutions.

## Common pitfalls

- Treating unfair-discrimination under Model #880 as if it were ECOA / Reg B disparate-treatment analysis. The statutory test is different (actuarial justification matters; permitted vs prohibited rating factors differ; protected classes are defined by state insurance code, not by ECOA).
- Letting the actuarial memorandum stand in for the governance review. The actuarial work justifies the rates; the second-line file justifies the governance over the actuaries and the model.
- Skipping ECDIS provenance for any rating factor that touches third-party consumer data. CO and NY DFS guidance is explicit.
- Forgetting the AIS Program structure from NAIC Bulletin Dec 2023. Carriers are increasingly being asked for an AIS Program document by state DOI; the artifact should map findings to its sections.
- Treating SR 11-7 as a banking thing. State DOIs cite it as analogous model-risk expectation language. Better to address it explicitly than to leave the gap implicit.
- Missing the ACA layer when individual or small-group health is in scope. Community rating, age bands, and tobacco surcharges are bright-line rules.
- Conflating illustration governance (Model #582) with rate-filing governance. Both can apply on a life pricing change; they are different tests.
- Drafting the artifact as a model-validation report. The artifact is a pricing-governance review; validation is one input, not the deliverable.
