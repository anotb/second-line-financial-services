# Cyber cross-cutting overlay — rule-to-obligation-extraction

Load when the rule under extraction is anchored to cybersecurity, computer-security incident response, ICT risk management, or operational resilience. Cyber rules cross sector boundaries: SEC Item 1.05 lands on registrants; the 36-hour bank notification rule lands on banking organisations; NYDFS Part 500 lands on DFS-regulated entities; DORA lands on EU financial entities; NAIC Model 668 lands on insurance licensees in adopting states. The overlay carries the recurrent extraction patterns specific to incident-reporting timing and to programme obligations.

## Incident-reporting timing — comparative table

The extraction must respect each rule's specific clock; incident-reporting rules are notoriously close in shape and different in detail, and substituting one rule's clock for another is a quiet extraction defect.

| Rule | Trigger | Clock | Action |
|---|---|---|---|
| SEC Form 8-K Item 1.05 (17 CFR 249.308; Reg S-K Item 106) | Materiality determination of a covered cybersecurity incident | Within 4 business days of the determination | File Form 8-K Item 1.05 disclosure; Attorney-General-national-security delay exception under 1.05(c) |
| 12 CFR Part 53 (OCC); 12 CFR Part 225 Subpart N (FRB); 12 CFR Part 304 Subpart C (FDIC) — bank notification rule | Determination of a "notification incident" | As soon as possible and no later than 36 hours after determination | Notify the primary federal regulator |
| Bank-service-provider notification under the same rule | BSP determination of a covered incident materially disrupting or degrading services | As soon as possible | Notify each affected banking-organisation customer |
| 23 NYCRR Part 500.17(a) (NYDFS) | Cybersecurity event | As promptly as possible, no later than 72 hours from determination | Notify the Superintendent |
| NYDFS Part 500.17(c) (ransomware extortion payments, post-2023 amendment) | Extortion-payment determination | Within 24 hours of payment | Notify the Superintendent |
| EU Regulation 2022/2554 (DORA) Article 19 | Major ICT-related incident | Initial notification within hours; intermediate and final reports within deadlines set by RTS | Notify competent authority |
| NAIC Model 668 §6 / state-adopted versions | Determination of a "Cybersecurity Event" | Within 72 hours from determination | Notify Commissioner; affected-consumer and reinsurer notifications follow |
| GLBA Safeguards Rule, 16 CFR 314.5 (FTC; rev. 2023 amendments) | Notification event | As soon as possible, no later than 30 days after discovery (FTC-only; 500-customer threshold) | Notify the FTC |
| HIPAA Breach Notification Rule, 45 CFR 164.404 — 408 (when in scope) | Discovery of a breach of unsecured PHI | Without unreasonable delay; no later than 60 days for individual notice; concurrent HHS notice for breaches of 500+ | Multiple notices |

When extracting an incident-reporting obligation, the extraction row captures: the trigger (carefully — "material incident" is not the same as "notification incident" is not the same as "cybersecurity event" is not the same as "covered cybersecurity incident"); the clock and its starting condition; the recipient; the form of notice; and any exception or delay provision.

## Programme-and-policy obligations

Cyber rules typically also impose standing programme obligations distinct from the incident-reporting timing:

- **Written programme**. The rule requires the regulated party to maintain a written cybersecurity programme covering risk-assessment, access controls, encryption (in transit and at rest), multi-factor authentication, monitoring and detection, incident response, business continuity and disaster recovery, vendor and third-party security, training, and periodic review. Each named domain is potentially its own obligation row depending on the rule's granularity. Examples: NYDFS Part 500 §500.2 (programme), §500.3 (policy), §500.5 (testing), §500.7 (access privileges), §500.11 (third-party); GLBA Safeguards Rule 16 CFR 314.4 elements; NAIC Model 668 §4.
- **Officer designation**. The rule requires designation of a CISO or qualified individual responsible for the programme. NYDFS §500.4; NAIC Model 668 §4(C); GLBA Safeguards Rule §314.4(a). Each is a row.
- **Risk assessment**. Periodic risk assessment that informs the programme. Most rules require it; the cadence varies (annual is common). Each rule has its own row.
- **Third-party security oversight**. The programme must extend to third-party service providers with access to information systems or non-public information. NYDFS §500.11; NAIC Model 668 §4(F); the bank notification rule's BSP-side row.
- **Penetration testing and vulnerability assessment**. NYDFS §500.5 explicitly; other rules implicitly through the programme requirement.
- **Reporting to the board or board committee**. Annual or more-frequent CISO report to the board on the programme. NYDFS §500.4(c); NAIC Model 668 §4(H); FFIEC IT Handbook expectations.

## Defined-term sensitivity

Cyber rules are particularly sensitive to defined-term scope. Definitions to capture verbatim with their source pins:

- "Cybersecurity incident" / "covered cybersecurity incident" (SEC Item 106(a) and the 8-K Item 1.05).
- "Computer-security incident" / "notification incident" (the bank notification rule, Part 53.2).
- "Cybersecurity event" (NYDFS Part 500.1; NAIC Model 668 §3).
- "ICT-related incident" / "major ICT-related incident" (DORA Article 3).
- "Critical or important function" (DORA Article 3).
- "Critical ICT third-party service provider" (DORA Article 31).
- "Information system" (multiple rules; definitions differ).
- "Nonpublic information" (NYDFS Part 500.1; NAIC Model 668 §3).
- "Multi-factor authentication" (NYDFS Part 500.1; NAIC Model 668 §3).

The defined-term differences across rules are the most common source of cross-rule confusion. The extraction's defined-terms section captures each term with its source pin; the obligation row's `defined_terms_used` column records which terms the row depends on.

## DORA worked pattern

Regulation (EU) 2022/2554, OJ L 333/1. Application date January 17 2025. Decomposition:

- **Article 5** ICT governance. Governance row: management-body responsibility for ICT risk management framework approval and oversight.
- **Article 6** ICT risk-management framework. Programme row covering identification, protection, detection, response and recovery, learning and evolving.
- **Article 9** Protection and prevention.
- **Article 10** Detection.
- **Article 11** Response and recovery; business-continuity policy and ICT response and recovery plans.
- **Article 17** ICT-related incident management process. Programme row.
- **Article 18** Classification of ICT-related incidents. Methodology row.
- **Article 19** Reporting of major ICT-related incidents. Reporting rows: initial; intermediate; final; significant cyber-threat voluntary notification.
- **Article 24** Digital operational resilience testing programme. Programme row.
- **Article 28** Management of ICT third-party risk. Programme rows; contract-clause rows (Article 30 specifies minimum contractual provisions).
- **Article 30** Key contractual provisions. Each enumerated provision is a row that the financial entity must obtain in its contracts with ICT third-party service providers.
- **Article 31** Designation of critical ICT third-party service providers. Designation regime; not a direct obligation on the financial entity but a regulatory designation that triggers oversight.

## When to layer with sector overlays

Cyber obligations frequently sit on top of sector-specific rules. When the rule under extraction is the bank notification rule (12 CFR Part 53 / 225 / 304), load both `cross-cutting/cyber.md` and `sector-overlays/banking.md`. When the rule is SEC Item 1.05, load both `cross-cutting/cyber.md` and `sector-overlays/capital-markets.md`. The cross-cutting overlay carries the comparative-table view; the sector overlay carries the rule's procedural and supervisory context.
