# LLM vendor evidence review: [vendor] / [model and version]

Starting structure for a foundation-model vendor evidence-pack review. Depth flexes with deployment form, tier, and sector; the section list does not. A hosted-API tier-1 review with banking and cyber overlays runs longest; an open-weights-self-hosted tier-2 review compresses the security-posture and privacy-posture sections to "not applicable" and shifts weight onto firm-side responsibility shift.

The review is a draft until the human reviewer (AI Governance Lead, plus co-attestors per loaded overlays) attests.

---

## 1. Review metadata

- Reviewer role: [function, e.g. AI Governance Lead]
- Review stage: [onboarding / version-delta / periodic-reattestation / post-incident / exam-readiness]
- Review date: [YYYY-MM-DD]
- Engagement-scope ID (if `scoping` was run): [ID]
- Linked vendor-diligence ID (if chained from `vendor-diligence`): [ID]

---

## 2. Vendor and model metadata

- Vendor: [provider name]
- Model name: [name]
- Model version: [version]
- Deployment form: [hosted-api / open-weights-self-hosted / open-weights-vendor-hosted / on-prem-appliance / fine-tuned-derivative]
- Version pinning posture: [pinned / floating / rolling-with-notice / unknown]
- Evidence pack date: [YYYY-MM-DD; date of the latest document in the pack]
- In-firm use cases in scope (links to `ai-use-case-intake` records): [IDs]

A short note on the deployment context (architecture, RAG corpora, tool inventory if any, autonomy level) that the firm is reviewing this evidence for. A pointer to the model-card record from `model-card-builder` is preferable to restating; the evidence-pack review is not the place to re-derive deployment context.

---

## 3. Evidence inventory

For each document reviewed, the document, date, public-or-confidential status, and whether the document is vendor-self-attestation or third-party attestation:

| Document | Date | Source URL (if public) | Confidentiality | Vendor self-attestation? |
|---|---|---|---|---|
| Vendor system card | [date] | [URL or "not public"] | [public / nda-bound / trust-center-gated / regulator-confidential] | true |
| Vendor model card | | | | true |
| Vendor evaluation report | | | | true |
| Vendor red-team summary | | | | true |
| SOC 2 Type II report | | | nda-bound | false |
| ISO/IEC 27001 certificate and Statement of Applicability | | | nda-bound | false |
| Vendor responsible-use policy and acceptable-use rules | | | public | true |
| Vendor trust-center page (data handling, retention, abuse monitoring) | | | public | true |
| Vendor incident-disclosure history | | | public | true |
| Vendor change-of-version and deprecation notice posture | | | public | true |
| Other (per overlay) | | | | |

Confidentiality marker is required on every entry. Vendor self-attestation flag distinguishes vendor-authored documents from third-party attestations; downstream confidence labels respect this.

---

## 4. Sufficiency view by criterion

For each criterion, status read against the in-firm deployment context (not against the vendor's general claim), with the basis named:

| Criterion | Status | Basis | Evidence ref |
|---|---|---|---|
| intended-use-scope | [sufficient / partial / insufficient / missing / not-applicable] | [what the in-firm use needs and how the evidence reads against that need] | [pointer into evidence inventory or `[evidence needed]`] |
| training-data-posture | | | |
| evaluation-coverage | | | |
| dangerous-capability-evaluations | | | |
| red-team-coverage | | | |
| security-posture | | | |
| privacy-posture | | | |
| content-provenance | | | |
| incident-disclosure-history | | | |
| support-and-escalation | | | |
| regulator-engagement-history | | | |
| change-and-version-control | | | |
| responsible-use-policy | | | |
| abuse-monitoring-and-data-retention | | | |

Criteria not applicable to the deployment form are marked "not-applicable" with the basis (e.g., security-posture is not-applicable for open-weights-self-hosted because the firm controls the serving plane; the firm-side responsibility shift is recorded). The basis column is the load-bearing one.

---

## 5. Named gaps

For each gap:

| Criterion | Gap | Severity | Supplemental evidence requested | Owner role | Deadline | Accepted as best available? |
|---|---|---|---|---|---|---|
| [criterion] | [concrete description of what is missing or partial] | [low / medium / high / critical] | [what was asked from the vendor or what the firm-side equivalent will provide] | [function, never an individual] | [YYYY-MM-DD] | [yes / no] |

A gap marked accepted-as-best-available is one where the firm acknowledges the residual is unfillable (typical for open-weights training-data disclosure) and absorbs it; the residual reliance section records the acceptance.

---

## 6. Residual reliance

For each item the firm is relying on the vendor for:

| Reliance | Caveat | Accepted owner role | Accepted date |
|---|---|---|---|
| [what the firm is depending on the vendor for] | [the scoping caveat that limits the reliance] | [function] | [YYYY-MM-DD] |

Examples:

- "Vendor's published refusal-rate posture for the assistant's intended-use scope" with caveat "firm runs in-flight monitoring and reserves the right to swap-revalidate on any vendor-disclosed incident", accepted by AI Governance Lead.
- "Vendor's default-zero-retention posture for enterprise-tier API traffic" with caveat "abuse-monitoring exception scope documented; firm-side prompt logging captures what is sent", accepted by Head of Privacy.
- "Vendor's incident-disclosure cadence" with caveat "cadence is vendor-defined; firm subscribes to vendor disclosure feeds", accepted by AI Governance Lead.

---

## 7. Recommended owner actions

| Action | Owner role | Deadline | Severity | Linked gap |
|---|---|---|---|---|
| [concrete action] | [function] | [YYYY-MM-DD] | [low / medium / high / critical] | [link to gap or "n/a"] |

Critical-severity items typically block deployment until closed. Owner roles are functions, never individuals.

---

## 8. Re-review triggers

Named events that require a re-review of this evidence pack. At minimum, for hosted-API and vendor-hosted forms: vendor model-version swap; vendor new-system-card publication; vendor-disclosed incident affecting the model variant; vendor change to acceptable-use or responsible-use policy; vendor change to abuse-monitoring or data-retention default; expansion of in-firm deployment context (new RAG corpora, expanded tool inventory, new use case).

Sector and cross-cutting overlays add named triggers (e.g., bank examination feedback referencing the vendor; CFPB enforcement action; SEC risk alert; vendor change to SOC 2 scope). Loaded overlays append their named triggers here.

---

## 9. Source trace and confidence

For every material claim:

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| [claim] | [document, vendor evidence, third-party attestation, or `[evidence needed]`] | [pointer] | [high / medium / low / evidence-needed / vendor-self-attestation] |

Vendor-authored documents default to vendor-self-attestation confidence. Third-party attestations (SOC 2 by named auditor, ISO certificate) carry higher confidence. `[evidence needed]` flags route to recommended actions.

---

## 10. Sector and cross-cutting overlay notes (when applicable)

When the scope names a sector, the matching `references/sector-overlays/<sector>.md` adds named fields here. When cross-cutting overlays are loaded (cyber, privacy, conduct), the matching `references/cross-cutting/<topic>.md` adds named fields here.

The overlay-specific structured-output blocks (`sector_overlay_notes`, `cross_cutting_overlay_notes.cyber`, `cross_cutting_overlay_notes.privacy`, `cross_cutting_overlay_notes.conduct`) populate from the loaded overlays.

If no overlay is loaded, this section is omitted.

---

## Reviewer attestation block

The review is reviewable when sections 2 through 9 are filled and source trace is complete. The human reviewer attests:

- **Reviewer**: [role, function]
- **Reviewer date**: [YYYY-MM-DD]
- **Decision**: [sufficient-for-deployment / sufficient-with-conditions / insufficient-defer / insufficient-decline / escalate]
- **Conditions (if any)**: [conditions, owner roles, dates]
- **Co-attestors (per loaded overlays)**: [e.g., MRMO for banking sector overlay; CISO function for cyber overlay; chief privacy officer for privacy overlay; CCO for conduct overlay]
- **Onward routing**: [genai-pre-prod-review / AI risk committee / TPRM forum / model-risk committee / board pack / fund board]

The review is filed only after attestation.
