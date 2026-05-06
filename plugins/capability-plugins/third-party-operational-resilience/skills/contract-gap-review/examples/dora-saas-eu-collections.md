# Example: Digital-operational-resilience-act-in-scope SaaS contract for an EU subsidiary's collections platform

Public-source-derived. No named vendor. The shape mirrors a common matrix at the EU subsidiary of a multinational financial group reviewing a SaaS agreement for a collections-and-recoveries platform that supports the subsidiary's consumer-credit portfolio.

## Input

- **Vendor**: an EU-incorporated SaaS provider (Ireland) offering a collections-and-recoveries workflow platform with hosted analytics, agent-workspace, and customer-communication tooling. Hosted on a hyperscaler's EU regions; sub-processor list includes the hyperscaler, an SMS gateway provider, and an email-deliverability provider.
- **Service**: collections workflow management; debtor segmentation analytics; agent telephony integration; customer-communication channel orchestration. Outputs feed the subsidiary's debt-recovery operations across consumer-credit and SME portfolios.
- **Inputs already on file**: criticality-assessment record (criticality = important under the firm's taxonomy; classified as critical-or-important-function ICT service under the EU digital-operational-resilience act because the platform supports a function whose disruption would materially impair the subsidiary's regulated activity); SOC 2 Type II report; ISO 27001 certificate; the proposed enterprise contract (master agreement, data-processing addendum, security addendum); the parent group's third-party-risk policy referencing the EU digital-operational-resilience act, the European banking authority outsourcing-arrangements guidelines, and the parent's internal contract paper standards.
- **Engagement scope supplied**: institution = EU subsidiary of a multinational banking group, with consumer-credit licence in member state of incorporation and passporting rights across selected EU member states; primary regulators = the local national competent authority and the European banking authority via consolidated supervision; persona = head of operational resilience coordinating with general counsel and the CISO; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **AI vendor**: false. The platform's analytics module uses statistical segmentation, not foundation-model AI. (If the subsidiary later enables the platform's optional AI-summarisation feature for agent-workspace narratives, the matrix is re-opened with `ai_vendor = true`.)
- **Digital-operational-resilience-act in scope**: true. Critical-or-important-function ICT service. The mandatory-clause overlay loads.

## Output sketch

The skill produces a contract gap matrix with the mandatory-clause overlay populated. Headlines:

- **Arrangement and criticality** — important-tier vendor under the firm's taxonomy; critical-or-important-function ICT service under the EU digital-operational-resilience act; collections-platform supports a regulated activity (debt recovery on consumer-credit accounts under the firm's local consumer-credit licence); NPI in scope (debtor identifiers, account balances, communication records); EU-only data residency in the data-processing addendum.

- **Applicable regimes and overlay set** — banking sector overlay loaded; cyber and privacy cross-cutting overlays loaded; mandatory-clause overlay loaded.

- **Mandatory-clause overlay (M1-M6)** — the matrix surfaces the enhanced clause set as `high`-severity-by-source rows:
  - **M1 termination rights tied to supervisory recommendation** — the master agreement includes termination for material breach and insolvency but does not include a right to terminate on the firm's competent authority's recommendation. Marked `absent`. Recommended amendment posture: add the supervisory-recommendation termination trigger; absence is mandatory-by-source. Severity: `high`.
  - **M2 full description of services** — the order form references "the platform" without a defined-services schedule. Marked `partial`. Recommended amendment posture: attach a defined-services schedule covering modules, sub-modules, integration points, and SLAs. Severity: `high`.
  - **M3 locations of data processing and storage** — the data-processing addendum names "EU regions" without specifying the cities or data centres. Marked `partial`. Recommended amendment posture: name the specific regions and data centres in the addendum; require firm consent for any change. Severity: `high`.
  - **M4 sub-outsourcing notification timing and rejection rights** — the addendum requires 60 days' notice for material sub-processor changes but no rejection right. Marked `partial`. Recommended amendment posture: tighten notification timing to align with the firm's competent authority's expectations; add rejection right with termination-for-convenience trip if rejection is sustained. Severity: `high`.
  - **M5 exit-strategy and transitional support** — the master agreement commits to "reasonable cooperation" for up to 6 months post-termination. The European banking authority guidelines and the EU act expect a tested exit strategy with transitional-period support sized to the criticality of the function. Marked `partial`. Recommended amendment posture: extend transitional support to 12 months minimum with named scope, defined cost-allocation, and parallel-run support during the transitional period; require the vendor to support the firm's documented exit-plan workflow. Severity: `high` (exit-plan workflow consumes this row; absence breaks the exit posture).
  - **M6 audit-and-access for the firm and the competent authority** — the security addendum includes audit rights for the firm but conditions competent-authority access on the vendor's process. Marked `partial`. Recommended amendment posture: unconditional access for the firm and the competent authority, with cost-allocation defined and on-site posture preserved. Severity: `high`.

- **Cybersecurity-event-notification clock (cyber cluster, C1)** — the security addendum sets vendor-to-firm notification at "without undue delay and in any event within 72 hours". The firm's incident-reporting timetable under the EU act is the operative upstream clock; the vendor's 72-hour window does not give the firm enough margin for triage and onward reporting. Marked `partial`. Recommended amendment posture: tighten to vendor-to-firm notification within 24 hours of vendor confirmation. Severity: `high`.

- **Sub-processor list and change-notice (privacy cluster, P2; subcontracting findings)** — current sub-processor list is referenced in the addendum and published on the vendor's portal; change-notification by portal-update plus email; rejection right is present but conditioned on the firm proposing an alternative sub-processor. Marked `partial`. Recommended amendment posture: remove the alternative-proposal condition on rejection; align change-notice timing with the M4 row. Severity: `medium`.

- **Cross-border-transfer mechanism (privacy cluster, P5)** — the data-processing addendum addresses cross-border-transfer through standard contractual clauses for any onward transfer outside the EEA, but does not include a transfer-impact-assessment cooperation commitment. Marked `partial`. Recommended amendment posture: add transfer-impact-assessment cooperation; define the firm's audit reach into onward-transfer chains. Severity: `medium`.

- **Termination findings** — termination-for-convenience present with 90-day notice; termination-for-cause triggers include SLA-failure, security-incident, insolvency, and material-breach; missing the supervisory-recommendation trigger (covered by M1) and the regulatory-action trigger more broadly. Recommended amendment posture: add the regulatory-action trigger; align with M1.

- **Liability findings** — limit of liability capped at one year of fees; carve-outs include confidentiality breach, data breach, IP infringement, gross negligence, and willful misconduct; insurance evidence sufficient. The cap is below the firm's expected loss in a sustained-outage scenario; risk-acceptance documentation required. Severity: `high` for the cap-below-expected-loss flag.

- **Audit findings** — audit rights present for the firm; competent-authority access conditional (covered by M6); performance reporting cadence defined (monthly); problem-reporting posture present.

- **Summary severity** — `high`. The mandatory-clause overlay raises six `high`-severity-by-source rows; the cyber and privacy clusters raise additional rows. Recommended posture: `redline-and-defer-decision`. Conditions: all six mandatory-clause rows redlined to satisfaction; cybersecurity-event-notification clock tightened to 24 hours; sub-processor rejection right unconditioned; cross-border transfer-impact-assessment cooperation added; risk-acceptance documentation on the liability cap. Counsel-of-record: the EU subsidiary's general counsel plus the parent group's external counsel on the digital-operational-resilience-act compliance read. Approver: head of operational resilience and general counsel jointly per the firm's policy for critical-or-important-function ICT services.

The matrix stops at the recommended posture and the conditions. Counsel drafts language; the named approver decides.

## Why this scenario matters

- **Boundary check on the digital-operational-resilience-act in-scope flag**: any contract supporting a critical-or-important-function ICT service in scope of the act picks up the mandatory-clause overlay regardless of the firm's internal criticality taxonomy. The matrix surfaces the M1-M6 rows as `high`-severity-by-source.
- **Boundary check on the cybersecurity-event-notification clock**: the act's incident-reporting timetable is operative. A 72-hour vendor-to-firm window does not give the firm enough margin; the cyber overlay tightens.
- **Boundary check on the exit-strategy commitment**: the M5 row is mandatory-by-source. A 6-month "reasonable cooperation" clause is not enough for a critical-or-important-function service; the matrix surfaces the row to the exit-plan workflow.
- **Boundary check on competent-authority access**: the audit-rights row for the firm is distinct from the competent-authority access row. Both must be unconditional under M6.
- **Boundary check on transfer-impact-assessment cooperation**: cross-border-transfer mechanism is a privacy-overlay row; transfer-impact-assessment cooperation is a separate sub-row that the addendum often misses.

## Anchors

- DORA — Regulation (EU) 2022/2554, Articles 28-30 key contractual provisions.
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02).
- GDPR (Regulation (EU) 2016/679) where the data-processing addendum reaches.
- The European banking authority's guidelines on ICT and security risk management.

See `references/source-anchors.md` for full citations and `references/cross-cutting/cyber.md` and `references/cross-cutting/privacy.md` for the overlay-specific anchors.
