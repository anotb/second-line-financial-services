# Example: model card refresh for an in-house consumer auto-loan decisioning model

Public-source-derived. No named institution. Framing patterns drawn from CFPB Circular 2022-03 (adverse action notification requirements when using AI or complex algorithms) and the public CFPB statements on algorithmic discrimination in credit. No firm-specific facts asserted.

## Input description

A US mid-size bank holding company runs a gradient-boosted classifier to score consumer auto-loan applications in the indirect channel. The model has been in production for 18 months. Annual model inventory exercise is in motion. Card was first written at pre-prod gate; today's task is the refresh ahead of the model risk committee review.

Engagement scope provided by `scoping`:
- Institution type: bank holding company, asset size mid-cap, primary regulators OCC and CFPB.
- Persona: model risk validator, second line, reporting to the head of model risk.
- Sector overlay set: banking. Cross-cutting overlays: privacy (regulated NPI), conduct (consumer credit decisioning).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2 (material, customer-facing, ECOA/Reg B exposure, not enterprise-defining).

## Output sketch

Card sections produced (abbreviated):

- **Card metadata** — model ID `auto-uw-gbm-v3.2`; tier-2; lifecycle stage prod; second-line reviewer named in the scope record.
- **Intended use** — auto-loan underwriting decisioning, US-only, indirect dealer channel only. Out of scope: refinance, lease, direct-to-consumer, pre-approval marketing scoring.
- **System description** — gradient-boosted decision tree on bureau attributes plus application data; no foundation model, no RAG, no tools. Production on internal model serving platform v4.
- **Training and reference data** — bureau attributes from named bureau (regulated NPI, GLBA in scope), application form data (regulated NPI), no alternative data, no social media data. Training window 2022-01 to 2024-12. Excluded fields: ZIP proxies for protected class flagged in 2024 fair-lending review (lineage cited in source trace).
- **Performance summary** — AUC overall and by FICO band, by state, by indirect dealer segment. Deployed-environment metrics from monthly performance pack, not lab-only. Approval rate by FICO band reported alongside.
- **Robustness and stress testing** — out-of-time backtest, recession scenario backtest using internal stress framework, dealer-segment robustness test.
- **Fairness and explainability** — adverse action coding rate by ECOA protected class, disparity ratios calculated per the firm's fair-lending test plan, explainability via SHAP at decision level for adverse action notice generation. Method limitations recorded (SHAP for non-linear interaction effects).
- **Limitations and known failure modes** — concrete list:
  - Thin-file applicants (fewer than three bureau tradelines): model undermargined, override rate elevated. Example: 2025-Q2 monitoring showed override rate of 14% on thin-file segment versus 3% portfolio average.
  - Post-bankruptcy applicants in the 24-to-48-month window: model treats as high-risk despite recovery patterns; second-look process required.
  - Out-of-state applicants in three named states with thin training coverage: AUC drop measured, segment-flag fires at decision time.
- **Monitoring plan** — PSI on top input features (threshold 0.25, monthly, owner: model owner, escalation to MRMO at breach); score drift (KS against reference distribution, threshold per firm policy); decisioning-rate drift (state-level and dealer-level, monthly); complaint-rate drift (CFPB complaint database plus internal complaint feed, monthly, owner: consumer compliance, escalation to fair lending committee at breach). Each entry has threshold, owner, and escalation path filled.
- **Controls** — challenger model in shadow mode (preventive, owner: model owner); 5% random override sampling for second-line review (detective, owner: validator); monthly performance pack review (detective, owner: model risk committee); adverse action notice quality sampling (detective, owner: consumer compliance).
- **Change management** — re-validation triggers: feature add or remove, training data window shift > 6 months, performance trigger breach for two consecutive months, new state added to operating footprint, regulatory change in adverse action notification standard. Approver: head of model risk for tier-2.
- **Sign-off questions** — six concrete questions tagged to sections: (i) what is the trigger to re-fit, who approves; (ii) policy for proxy variables identified after deployment; (iii) thin-file segment treatment plan and timeline; (iv) integration with consumer-compliance fair-lending test plan, frequency; (v) monitoring escalation path when complaint-rate drift breaches; (vi) override pattern monitoring across dealer segments for unfair-treatment risk.
- **Source trace and confidence** — every claim cited to source: validation report 2025-Q2, monitoring pack 2025-09, fair-lending test plan 2025-Q1, adverse action notice review 2025-08. Two `[evidence needed]` flags carried forward to the issue log: foundation-model dependence statement (n/a here) and prompt-injection exposure (n/a here).

## Why this scenario matters

- It exercises the segment-level performance reporting requirement: an overall AUC is acceptable but the segment table reveals the thin-file exposure and the post-bankruptcy exposure that drive the limitations section.
- It exercises the conduct cross-cutting overlay: complaint-rate drift in monitoring, adverse action notice quality in controls, integration with consumer-compliance fair-lending test plan in sign-off questions. The model card and the fair-lending test plan are different artifacts but they reference each other.
- It exercises the banking sector overlay: ECOA/Reg B adverse action surface, OCC primary regulator framing, model risk committee as the sign-off body. Tier-2 depth, not tier-1: the card is reviewable in a single committee session.
- It exercises the lifecycle distinction: refresh is not a first draft. Most fields carry forward; the fields that move are performance (new monitoring period), limitations (new evidence from the segment table), controls (new override sampling), and sign-off questions (new ones raised by this period's evidence).
