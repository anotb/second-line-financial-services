# Banking sector overlay for prompt-injection-risk

When the scope record names `banking` as the sector, this overlay adds banking-specific carriers, mitigations, monitoring signals, and incident-notification triggers to the review. Loaded by `prompt-injection-risk/SKILL.md` when `scope.sector_overlay_set` includes `banking`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to the GenAI system's serving environment, change controls, and access controls.
- Joint Interagency Guidance on Third-Party Relationships (June 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) where the GenAI system is vendor-hosted or relies on a foundation-model provider.
- The joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, supersedes SR 11-7 and SR 21-8) expressly excludes generative AI from its scope (footnote 3); the GenAI use case is not within the bulletin. Where the bank's model risk programme treats it as a model by analogy, the principles inform but the binding hook is firm policy.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards) for OCC-supervised large banks where the GenAI use case sits inside a risk-appetite-statement-relevant function.
- NYDFS 23 NYCRR Part 500 and the October 2024 AI Industry Letter for NY-footprint covered entities.
- The 36-hour banking computer-security incident notification rule: 12 CFR Part 53 (OCC), 12 CFR Part 225 Subpart N (FRB), 12 CFR Part 304 (FDIC), effective 2022.
- FFIEC BSA/AML Examination Manual where the GenAI use case touches AML alert handling, customer risk rating, or SAR drafting.

## Carriers and trust posture nuances specific to banking

The recurring banking GenAI use-case patterns and the carriers that usually drive the threat surface:

- **Relationship-manager assistant**: retrieves over internal CRM, recent earnings transcripts, internal research notes, third-party vendor research. Highest-likelihood vector is indirect injection in third-party content (transcripts, news, vendor research). The CRM is firm-controlled but contains client-supplied content (emails, chat, meeting notes) that can carry adversarial instructions placed by a counterparty.

- **Customer-service assistant**: retrieves over customer history (calls, chats, emails), policy and procedure corpus. Highest-likelihood vector is indirect injection via customer-history content and cross-customer information bleed via crafted query. The agent-review gate is preventive but is the only line of defence between a misleading summary and the customer; off-switch criterion under the agent-review gate is therefore load-bearing.

- **AML alert-triage assistant**: retrieves over alert narratives, customer profiles, transaction histories, sanctions screening hits, third-party intelligence. Highest-likelihood vector is indirect injection via alert narrative content (which can be free-text and originate from analyst notes, system-generated descriptions, or third-party intelligence feeds). Misrouted alert handling is a BSA/AML programme integrity issue; the BSA officer is a co-reviewer where the use case touches alert disposition.

- **KYC/EDD assistant**: retrieves over identity-verification documents, beneficial-ownership records, third-party adverse-media feeds, jurisdiction risk content. Highest-likelihood vector is indirect injection via adverse-media or third-party intelligence content; PII exfiltration risk is structural.

- **Treasury-management assistant**: retrieves over client cash-management profiles, payment patterns, fraud-rule documentation. Where tools are enabled (rate quotes, payment initiation, statement generation), tool-boundary controls become the load-bearing mitigation; fraud and authorisation framings apply.

## Mitigations the review should expect to see

Beyond the standard set:

- Role-based access on retrieval scoping, aligned to the banking entitlement model. Per-customer query scoping is the default for any customer-facing or customer-handling assistant; the review should confirm the scope at the retrieval layer rather than only at the prompt layer.
- Marketing Rule and consumer-disclosure-equivalent output filtering for any customer-facing communication generated or assisted by the system; UDAAP exposure on customer-facing AI output is the conduct-overlay seam, not a banking-specific one, but the banking sector inherits the framing.
- Sanctions and OFAC name-screening on any output that could include third-party identifying information.
- BSA/AML output filtering where the system outputs contribute to alert disposition or SAR narratives; the BSA officer signs off on the filtering specification.
- Foundation-model and vendor change-of-version notice and audit rights, captured in the third-party risk register and consistent with the June 2023 interagency guidance.

## Monitoring signals the overlay adds

- Per-customer retrieval audit (random sampling plus rule-based detection on cross-customer ID surfaces); any confirmed event is an investigation trigger and may be a §500.17(a) trigger for NY-footprint entities.
- Marketing Rule output-filter trip rate where applicable (joint trust company / RIA / BD entities); escalation to compliance.
- AML alert-disposition anomaly where the system supports alert handling; escalation to the BSA officer.
- 36-hour banking computer-security incident notification trigger evaluation: any cybersecurity event that materially disrupts or degrades, or is reasonably likely to materially disrupt or degrade, the bank's ability to deliver services, or that has resulted in actual harm to the bank's operations, must be evaluated against the 36-hour trigger; cyber and AI governance jointly assess.

## Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers (NYDFS §500.17(a), SEC 8-K Item 1.05, GLBA Safeguards Rule):

- 12 CFR Part 53 / Part 225 / Part 304 (36-hour banking computer-security incident notification): the bank must notify its primary federal regulator within 36 hours of determining that a notification incident has occurred. Prompt-injection events causing material disruption, degradation, or actual harm to bank operations are within scope. The notification decision sits with the cyber and operational-resilience leads with general counsel.
- BSA/AML programme integrity event triggers if the GenAI use case touches alert disposition or SAR narratives and the integrity of those outputs is in question; the BSA officer evaluates against the SAR continuing-activity reporting framework and against programme-integrity examination expectations.
- Consumer-protection event triggers if customer-facing AI output causes a UDAAP-relevant communication issue; consumer compliance evaluates.

## Recommended-action items the overlay surfaces

- Where the GenAI use case is in OCC large-bank scope (12 CFR Part 30 Appendix D), the review records the connection to the bank's risk-appetite-statement framework and surfaces residual-risk acceptance to the chief risk executive function.
- Where the use case is vendor-hosted or relies on a foundation-model provider, the third-party risk register entry is updated to reference the prompt-injection review and the foundation-model swap re-validation flag is recorded.
- Where the use case touches AML alert handling, the BSA officer co-signs the residual-risk acceptance.
- Where the use case is customer-facing in NY footprint, the NYDFS §500.17(a) notification-decision process is rehearsed against AI-specific incident scenarios.

## Common pitfalls specific to banking

- Treating a bank-hosted assistant on a vendor-hosted foundation model as if the firm controls the full stack. The vendor's foundation-model behaviour shift is a third-party event and a cyber event; both framings need to be in the review.
- Omitting the 36-hour banking computer-security incident notification rule. It is distinct from the NYDFS 72-hour notice and from the SEC 8-K four-business-day disclosure; all three can apply concurrently for a single material event in a NY-footprint public-registrant bank.
- Failing to involve the BSA officer when the GenAI use case touches alert handling; an integrity issue with AI-assisted alert disposition is a BSA programme issue.
- Treating the agent-review gate as a permanent control without an off-switch criterion. Under volume pressure, the gate becomes rubber-stamping; the review should record a defined off-switch (e.g., agent-edit rate falling below a threshold for two consecutive periods triggers a pause and re-validation).
