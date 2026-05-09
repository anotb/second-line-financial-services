# Changelog

## 0.3.0 — 2026-05-08

### Phase 2 editorial review (commit 5fd4cf6)

Per-plugin editorial layer (B1-B6) over Phase 1's mechanical cleanup. Voice principle: in SKILL.md body, regulators are grounding not focus. Heavy citation work (joint-guidance issuance metadata, footnote scope quotes, asset thresholds, supersession language, section / subpart numbers) consolidated into `references/source-anchors.md` and overlay files; skill bodies use natural practitioner framing.

- AI governance and model risk: April 2026 joint guidance verbatim language consolidated into `model-card-builder` source-anchors and banking overlay. OWASP LLM Top 10 refreshed to 2025 numbering (LLM01-LLM08) in `agentic-ai-controls` and `prompt-injection-risk`. EU AI Office Code of Practice refreshed from "in development" to published with 2 August 2025 GPAI effective date in `llm-vendor-evidence-review`. `agentic-ai-controls` regulator-perspective paragraph reordered: cyber regimes binding first, OWASP / MITRE ATLAS / NCSC / CISA primary, joint-guidance demoted to by-analogy. `ai-act-triage` Article numbers retained (legitimate legal-triage exception).
- Third-party and operational resilience: DORA Article 28(1)-(8) and Article 30(2)/(3) canonical structure landed in source-anchors. OCC 2013-29 demoted to historical. Commission Delegated Regs 2025/532 (sub-contracting RTS) and 2025/1190 (TLPT RTS) added. PRA SS1/21 / SS2/21 reframed.
- Compliance testing: OCC PPM 5310-3 framing corrected.
- Financial crime governance: `aml-model-monitoring` reframed as a model-scoping read.
- Risk reporting: SEC climate-rule current-state language refreshed.
- Consumer compliance and fair lending: `section1071-readiness` rebuilt around the May 1 2026 Section 1071 final rule.
- Financial crime governance: `sar-decision-qa` Red-tier reframed per October 9 2025 SAR FAQs.

### Phase 1 cross-cutting cleanup (commit 22dc202)

Six plugin-scoped sweeps (A1-A6) covering all 64 source skills.

- Removed `Anchored to:` paragraph from SKILL.md description blocks. Citations live in `references/source-anchors.md` rather than duplicated in the description.
- Split "What's load-bearing and what flexes" sections into a `Quality bar` block (invariants across every artifact) plus an `Adaptation` block (what flexes by engagement). Editorial folding pass deferred to Phase 2.
- Softened "review gates" terminology outside `human-review-gates` (which keeps the term as the artifact's subject) to decision forum / owner / conditions / attestation block / sign-off question / decision checkpoint by context.
- Format-flexible Output sections for the high-impact artifact skills: `vendor-diligence`, `criticality-assessment`, `contract-gap-review`, `exit-plan`, `resilience-testing-pack`, `control-matrix`, `evidence-binder`, `issue-writeup`, `policy-gap-review`, `control-sampling`, `exception-analysis`, `qa-workpaper`, `workpaper-drafter`. Default-to-template plus Word / Excel / PowerPoint / Markdown rendering per audience; structured record only when a downstream consumer needs it.
- Removed unsupported GenAI scope claims attributed to OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026 (April 17 2026 joint guidance). The bulletin expressly excludes generative AI and agentic AI from its scope (footnote 3); GenAI substantive anchors are NIST AI RMF 1.0, NIST AI 600-1, ISO/IEC 42001:2023, EU AI Act, OWASP LLM Top 10, MITRE ATLAS, NCSC / CISA secure-AI guidance, NYDFS October 2024 letter, and the NAIC AI Bulletin for insurers.
- FinCEN MSB BOI citation corrected from §1010.380 to §1022.380.

### Other

- Renamed `engagement-scoping` to `scoping` and revised as the gold-standard reference for the sharpened v1 rules.
- Switched from Apache 2.0 to MIT.

## 0.2.0

- Removed managed-agent cookbook content.
- Replaced vertical source taxonomy with capability and sector plugin groups.
- Added standalone agent subagents under each agent plugin.
- Replaced example set with public-source-derived regulatory scenarios.
- Added common policy, risk, control, source, review-gate, and output-template references.
- Added validation and sync scripts.

## 0.1.0

- Initial scaffold.
