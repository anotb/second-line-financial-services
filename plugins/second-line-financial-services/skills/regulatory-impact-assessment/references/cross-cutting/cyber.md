# Cross-cutting overlay: cyber — regulatory-impact-assessment

Load this overlay when the rule under assessment touches cyber, information security, computer-security incident notification, third-party cyber expectations, or AI-system cyber risk. Cross-cutting overlays do not change the assessment's spine; they tighten the source-anchor list and the named-policy and named-control patterns the assessment reads against.

## Anchored cyber sources

- **NYDFS 23 NYCRR Part 500** — Cybersecurity Requirements for Financial Services Companies. §500.2 cybersecurity programme; §500.3 cybersecurity policy; §500.4 CISO; §500.5 testing; §500.7 access privileges; §500.11 third-party SP security policy; §500.16 incident response; §500.17 notification of cybersecurity events. https://www.dfs.ny.gov/industry_guidance/cybersecurity .
- **SEC cybersecurity disclosure rule** (17 CFR 229.106 — Item 106 of Reg S-K; 17 CFR 240.13a-11 / 15d-11 — Form 8-K Item 1.05) [verify section labels in final adopting release]. https://www.sec.gov/rules/final/2023/33-11216.pdf .
- **SEC Reg S-P amendments** (2024 final rule on customer information protection) [verify final-rule release number, section, and effective date]. https://www.sec.gov/rules/final.shtml .
- **SEC adviser and fund cybersecurity rule** [verify final-rule citation, status, and effective date], where adopted.
- **Federal banking computer-security incident notification rule** — 12 CFR Part 53 (OCC), 12 CFR Part 225 (FRB), 12 CFR Part 304 (FDIC), generally requiring 36-hour notification of qualifying computer-security incidents [verify subsection]. https://www.ecfr.gov/current/title-12/chapter-I/part-53 .
- **GLBA Safeguards Rule** — 15 USC §6801; 16 CFR Part 314 (FTC) [verify subsection]; 12 CFR Part 30 Appendix B (interagency guidelines for federally supervised banks); FTC final rule on safeguards updates effective 2023.
- **FFIEC IT Examination Handbook** (current edition) [verify booklet, section]: Information Security; Outsourcing Technology Services; Business Continuity Management; Architecture, Infrastructure, and Operations; Audit; Development and Acquisition; Management; Operations. https://ithandbook.ffiec.gov/ .
- **NIST Cybersecurity Framework 2.0** (February 2024) [verify section]: Govern, Identify, Protect, Detect, Respond, Recover. https://www.nist.gov/cyberframework .
- **NAIC Insurance Data Security Model Law (#668)** [verify state adoption status and section] for insurance-side cyber-data-security obligations.
- **CISA Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA)** of 2022 [verify final-rule citation when adopted; the CISA notice-of-proposed-rulemaking is the operative document until final]. https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/circia .
- **Federal Trade Commission Health Breach Notification Rule** (16 CFR Part 318) [verify subsection], where applicable to digital-health products.
- **EU DORA (Digital Operational Resilience Act)** for firms with EU operations [verify article reference], including the EBA Implementing Technical Standards on the Register of Information.

## Named-policy and named-control patterns the rule may touch

When the rule is cyber-anchored, the impact assessment's policy-impact section typically references one or more of the policy areas below; the control-impact section reads against the control-objective pattern in the named source:

- **Information Security Programme** (CISO accountability; risk-assessment cadence; access controls; encryption; patching; incident response; testing; awareness and training).
- **Third-Party Cyber Risk Programme** (third-party-risk-assessment of cyber posture; flow-down contractual cyber expectations; subservice-organisation cyber posture; SOC 2 Type 2 reliance with carve-out review).
- **Incident Response Programme** (incident classification; notification-decision rationale; regulator-notification pathways with regulator-specific timing; customer-notification pathways under state breach-notification laws).
- **Resilience and Business Continuity Programme** (RTO/RPO targets; alternate-site or alternate-vendor posture; periodic recovery testing).
- **Vulnerability Management Programme** (vulnerability scanning; penetration testing; bug-bounty posture; remediation SLAs).
- **Identity and Access Management Programme** (privileged-access management; multi-factor authentication; access reviews; SoD).
- **Data Loss Prevention and Data Classification Programme** (data classification scheme; DLP control coverage; egress controls).
- **AI-System Cyber Risk Programme** (prompt-injection controls; model-and-agent-platform isolation; data-leakage controls in LLM use cases; model-supply-chain risk).

## Reporting-and-disclosure-impact patterns

Cyber rules routinely change the reporting-and-disclosure surface:

- **Public disclosures**: SEC Form 8-K Item 1.05 for material cyber incidents (registrants); SEC Form 10-K Item 1C for cyber risk management, strategy, and governance (registrants); state breach-notification statutes for affected-individual notification.
- **Regulator notifications**: 36-hour federal banking notification under Part 53; NYDFS Part 500 §500.17 within 72 hours; HIPAA 60-day breach notification (HHS-CMS); FDIC FIL-30-2024 [verify FIL number] consumer-notification expectations; CISA CIRCIA notification when in force.
- **Board reporting**: NYDFS Part 500 §500.4 and §500.16 [verify subsection] CISO-board reporting cadence; SEC cyber-rule registrant board-oversight description; OCC heightened-standards board-cyber-oversight expectations.
- **Examiner expectations**: FFIEC IT Examination Handbook booklets drive request-list expectations on cyber-programme documentation, testing reports, third-party assessments, and board-reporting cadence.

## Strategy-lens patterns specific to cyber rules

The cyber strategy lens has identifiable patterns:

- **Industry-association alignment**: BPI's BITS arm for bank-side cyber engagement; SIFMA cyber working groups for capital-markets engagement; ICI cyber working groups for fund-side; ACLI cyber working groups for life and annuity; FS-ISAC for cross-sector threat-intelligence engagement; the Cyber Risk Institute (CRI) Profile for cyber-risk-management framework alignment.
- **Examiner-posture-shift signal**: NYDFS Industry Letters (the 2024 GenAI cybersecurity Industry Letter is a reference point); SEC Division of Examinations cyber risk alerts; OCC heightened-standards cyber-programme communications; FRB and FDIC supervisory-priorities communications on operational resilience.
- **Cross-rule coordination**: where multiple cyber rules carry overlapping notification or programme requirements (federal banking 36-hour rule, NYDFS 72-hour rule, SEC 8-K Item 1.05, state breach-notification rules), the firm's incident-response programme reconciles the timing and the recipient list. The impact assessment names the reconciliation.
- **Supply-chain cyber posture**: rule changes affecting third-party-cyber-risk expectations (SEC Reg S-P amendments; NYDFS Part 500 third-party SP security policy; the June 2023 interagency third-party-risk guidance) drive vendor-contract refresh and SOC 2 Type 2 review.
- **AI-system-cyber posture**: AI-rule changes that touch cyber (NYDFS October 2024 GenAI Industry Letter; SEC AI-related rules and adopting releases; state AI-and-cyber rules) drive AI-platform isolation, prompt-injection control, and data-leakage control updates.

## When the cyber overlay applies in part vs full

Load the overlay in full when the rule's primary subject is cyber, information security, computer-security incident notification, or AI-system cyber risk. Load the overlay in part (only the relevant sections above) when the rule has a cyber dimension among other dimensions (e.g., a third-party-risk rule with a cyber-component sub-section). Do not load the overlay when the rule is unrelated to cyber even if it touches data privacy (load the privacy overlay instead) or operational resilience without a cyber primary anchor (the operational resilience read sits in the SKILL.md spine).
