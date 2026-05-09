# Cross-cutting overlay — cyber

Loaded when the scope flags cyber. Implementation plans triggered by or touching cyber rules carry distinct timing, governance, and evidence patterns.

## Incident-notification regimes the plan must reconcile

A cyber-touching plan generally lands inside multiple notification regimes. Each has a clock. The plan reconciles them rather than picking one.

- **12 CFR Part 53 (banking 36-hour rule)** — banking organisations notify the primary federal regulator within 36 hours of determining that a notification incident has occurred. §53.3 sets the trigger; §53.2 defines covered entities.
- **Bank service provider notification** under 12 CFR Part 53 §53.4 — bank service providers notify each affected bank as soon as possible.
- **NYDFS 23 NYCRR Part 500 §500.17** — covered entities notify NYDFS within 72 hours of determining a cybersecurity event has occurred. §500.17(a) sets the standard.
- **SEC 8-K Item 1.05** — public companies disclose material cybersecurity incidents within four business days of materiality determination.
- **State breach-notification laws** — every US state has one; clocks and triggers vary by state.
- **FTC Safeguards Rule (16 CFR Part 314 §314.5)** — financial institutions under FTC jurisdiction notify FTC as soon as possible and no later than 30 days after discovery of an event affecting 500+ consumers.
- **HIPAA Breach Notification Rule** — for covered entities and business associates handling PHI.
- **EU GDPR Article 33** — supervisory-authority notification within 72 hours where applicable.
- **EU DORA Article 19** — major ICT-related incident reporting where applicable.

The plan's notification workstream names every applicable regime, the fastest clock, and the workflow that triggers each notification from a single materiality assessment.

## Governance pattern

Cyber-touching implementation plans run with the CISO as a workstream owner and the disclosure committee (or its equivalent) as a governance checkpoint with out-of-cycle escalation. The disclosure committee's standing cyber agenda item is the practitioner pattern; quarterly cadence is too slow for a four-business-day clock.

Board-level cyber oversight is increasingly explicit under SEC Regulation S-K Item 106(c). The plan's board-reporting cadence reflects the rule's expectation that the board has visibility into cyber risk management.

## Control-design patterns

For NYDFS Part 500 implementations, milestones map to §500.2 (programme), §500.3 (policy), §500.4 (CISO), §500.5 (testing), §500.6 (audit trail), §500.7 (access privileges), §500.9 (risk assessment), §500.11 (third-party SP security), §500.13 (asset inventory), §500.14 (training and monitoring), §500.15 (encryption), §500.16 (incident response), §500.17 (notification), §500.21 (annual certification or written acknowledgment).

For FFIEC IT Examination Handbook implementations, the booklet structure (Information Security; Outsourcing Technology Services; Business Continuity; Architecture, Infrastructure, and Operations; Audit; Development and Acquisition; Management) is the workstream taxonomy.

## Evidence patterns

Cyber acceptance criteria emphasise testable evidence: pen-test reports, control-test workpapers, access-recertification logs, incident-response tabletop after-action records, training-completion attestations. Activity language ("implement MFA") fails examiners; evidence language ("MFA enforced for all privileged-access users by [date]; coverage validated by quarterly access-recertification report") passes.

For Part 500 §500.21 annual certification, the implementation plan integrates with the firm's annual cyber attestation cycle; the obligation lands in BAU as a recurring annual milestone.

## Plan posture

Cyber-touching plans elevate confidence to `medium` at most for a reactive remediation; `high` confidence requires that the control has run through at least one full audit or test cycle and the testable evidence is in hand. Pre-go-live confidence is generally `medium` regardless of build quality.

## Sources

Named regulatory anchors for cyber implementation are in `references/source-anchors.md`. Citations include 12 CFR Part 53, NYDFS 23 NYCRR Part 500, FFIEC IT Examination Handbook, SEC Reg S-K Item 106 and Form 8-K Item 1.05, FTC Safeguards Rule, EU DORA where applicable.
