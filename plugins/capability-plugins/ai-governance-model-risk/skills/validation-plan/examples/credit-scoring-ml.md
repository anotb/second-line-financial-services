# Example: annual revalidation plan for an in-house consumer credit-scoring model

Public-source-derived. No named institution. Framing patterns drawn from SR 11-7 §V validation pillars, OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026), CFPB Circular 2022-03 on adverse action notification with complex algorithms, and the public ECOA / Reg B fair-lending exam record. No firm-specific facts asserted.

## Input description

A US mid-size bank holding company runs a gradient-boosted classifier for indirect-channel auto-loan underwriting. Tier-2 model, 18 months in production, prior validation completed at pre-prod gate. Annual revalidation is the next required cycle. Engagement is staffed by the model risk function in the second line; the model owner sits in the consumer-lending business.

Engagement scope provided by `engagement-scoping`:
- Institution type: bank holding company, mid-cap, primary regulators OCC and CFPB.
- Persona: head of model risk (validator, second line). Model owner: head of consumer credit (1.5 line).
- Sector overlay set: banking. Cross-cutting overlays: privacy (regulated NPI), conduct (consumer credit decisioning).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2, carried forward from prior `ai-risk-tiering` output.
- Validation type: annual-revalidation.

## Output sketch

Plan sections produced (abbreviated):

- **Plan metadata** — model ID `auto-uw-gbm-v3.2`; tier-2; validator: head of model risk; validation type: annual-revalidation; scope date set; use-case ID and engagement-scope ID cited.

- **Validation depth** — set per pillar, not as a single label. Conceptual soundness: targeted (no theory change, segmentation review only because the firm added two states to its operating footprint). Outcomes analysis: full (12 months of new deployed-environment evidence to read against prior validation). Ongoing monitoring: targeted (review the validator-trigger thresholds against the year's monitoring pack). Tier justification documents why the depths land where they do.

- **Conceptual soundness scope** — segmentation review for the two added states; review of the override policy update applied in 2025-Q2; alternatives-considered note carried from prior validation (no new alternatives evaluated this cycle); foundation-model selection rationale: not applicable.

- **Data review scope** — bureau attribute fitness (named bureau, GLBA in scope); training-window check (2022-01 through 2024-12, plus Q1-Q3 2025 monitoring data used for outcomes analysis); exclusions check (ZIP-proxy fields removed in 2024 fair-lending review confirmed still excluded); lineage to system of record verified.

- **Outcomes analysis scope** — KS and AUC overall and by FICO band; capture rate by FICO band and by region; override outcomes versus policy (a control point that escaped the prior validation cycle); comparison against challenger model run in shadow over the same period; deployed-environment metrics dominate, lab-only metrics labelled separately. Each test names dataset, success criterion, owner.

- **Robustness scope** — out-of-time backtest on the 12 months since prior validation; recession-scenario backtest using the firm's internal stress framework; segment robustness on the two added states (sample size flagged as a constraint).

- **Fairness, explainability, transparency scope** — ECOA / Reg B disparity testing across protected classes per the firm's fair-lending test plan; disparity ratios calculated; SHAP-based adverse action reason generation reviewed for accuracy against a sample of recent declines; CFPB Circular 2022-03 and 2023-03 expectations on specific-and-accurate adverse action reasons read into the explainability success criterion.

- **Ongoing monitoring scope** — review of PSI thresholds on top input features (monthly), score drift (KS on score distribution), decisioning-rate drift (state-level and dealer-level), complaint-rate drift (CFPB complaint database plus internal feed). Each monitoring entry declares whether breach triggers re-validation; the validator's view and the model owner's monitoring view are aligned but distinct (operational alerts versus revalidation triggers).

- **Effective challenge questions** — six concrete questions, each tagged to a design choice or assumption: (i) the segmentation cuts pre-date the two added states; what evidence supports their continued validity post-expansion; (ii) the override policy update in 2025-Q2 shifted human approval rate by an unnamed amount; what was the analysis behind the threshold change; (iii) the training-window cutoff at 2024-12 means 2025 data has not entered training; what is the policy on training-window refresh, and at what cadence; (iv) thin-file applicants are flagged in the prior limitations section; what is the trigger to re-fit the thin-file segment treatment; (v) post-bankruptcy applicants in the 24-to-48-month window are noted as undermargined; what evidence does the validator need to see to retire that limitation; (vi) the SHAP-based adverse action notice generation has a sampling QC; what is the accuracy threshold and what is the escalation if accuracy drifts.

- **Dependencies** — bureau attribute extract for the validation window; performance-pack data feed access; fair-lending test plan output (cross-reference to consumer-compliance test cycle); override decision log access; complaint-rate data feed access.

- **Timeline** — 8-week revalidation cycle with milestones (data assembly, conceptual soundness review, outcomes analysis, fairness testing, draft validation report). Deliverables: validation report (phase 3 skill), refreshed model card via `model-card-builder`, MRA / issue log entries where defects are found.

- **Source trace and confidence** — every scope item cited to the source artifact (prior validation report, firm fair-lending test plan, monitoring pack 2025-09, override policy update memo 2025-Q2, engagement-scope record). Two `[evidence needed]` flags carried forward to the engagement issue log: 2025-Q2 override policy threshold change rationale (memo refers to a quantitative analysis the validator has not yet seen); two-added-states sample size for segment robustness testing (whether the sample is large enough to support a credible test).

## Why this scenario matters

- It exercises the per-pillar depth setting. Setting validation depth as a single label misses that conceptual soundness, outcomes analysis, and ongoing monitoring scope independently for an annual revalidation. The plan reads CS at targeted, OA at full, OM at targeted, and explains why.
- It exercises effective challenge that probes design choices, not generic policy compliance. Each question names the choice or assumption it interrogates, with expected evidence and an owner of response.
- It exercises the conduct cross-cutting overlay: SHAP-based adverse action reason generation with sampling QC, complaint-rate drift in monitoring, ECOA / Reg B disparity testing in fairness scope.
- It exercises the banking sector overlay: ECOA / Reg B adverse action surface, OCC primary regulator framing, CFPB consumer-protection authority over a large bank.
- It exercises the validator-vs-model-owner monitoring distinction: each monitoring entry declares whether breach is a revalidation trigger or a routine operational alert. The two views overlap but are not the same.
- The plan stops at draft. The head of model risk signs off. The validation report (phase 3) consumes this plan as its scope contract.
