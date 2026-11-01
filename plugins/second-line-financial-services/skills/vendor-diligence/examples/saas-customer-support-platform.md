# Example: SaaS customer-support platform at a regional bank

Public-source-derived. No named vendor. The shape mirrors a common diligence pattern at $50-100B regional banks evaluating a SaaS customer-support platform that surfaces depositor and small-business-borrower inquiries to call-centre agents.

## Input

- **Vendor**: a US-incorporated SaaS provider offering a customer-support and ticketing platform with telephony integration. Hosted on a single hyperscaler, two regions in scope.
- **Service**: customer-support agent workspace; customer-call recording; ticket management; agent-side knowledge-base search.
- **Business process supported**: contact-centre operations covering deposit-account servicing, debit-card disputes, and consumer-loan servicing.
- **Inputs already on file**: criticality-assessment record (criticality = important; not critical because deposit account servicing has paper-and-IVR fallback within tolerance); SOC 2 Type II report covering 12 months; ISO 27001 certificate (current); annual pen-test executive summary; the vendor's published BCDR plan; the proposed contract draft; firm's third-party-risk-policy citing the interagency third-party guidance and OCC Heightened Standards.
- **Engagement scope supplied**: institution = state member bank; primary regulators = FRB, state DFI; persona = head of TPRM; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = cyber, privacy.
- **AI vendor**: false. The platform has an embedded summarisation feature flagged as "optional"; the firm has not yet enabled it. Treated as not-AI for this pass; if the firm enables the feature, the diligence pack is re-opened with `ai_vendor=true` and the AI overlay is applied.

## Output sketch

The skill produces a vendor diligence pack. Headlines:

- **Service description and risk classification** — important-tier vendor; consumer-facing impact via the contact-centre channel; NPI in scope (account numbers, balances, dispute narratives); call recordings carry voice biometrics.
- **Risk-based diligence summary** — interagency-guidance-aligned: planning, due-diligence, contract, ongoing-monitoring posture all summarised. Reviewer questions clustered for the TPRM forum.
- **Operational resilience evidence** — vendor RTO of 4 hours and RPO of 15 minutes claimed; BCDR test report covers the primary region but not the failover region tabletop; firm impact tolerance for the contact-centre channel is 4 hours, so the claim meets tolerance only if the failover-region tabletop is evidenced. `bcdr_meets_firm_tolerance = false` until that gap closes.
- **Cyber and information-security evidence** — SOC 2 Type II clean opinion; scope excludes the telephony module; CUEC list includes customer-managed encryption keys (not enabled by the firm in the proposed configuration); ISO 27001 statement of applicability not provided. Pen-test executive summary cites two medium findings open at report date with vendor remediation commitments. `cyber_evidence_status = partial`.
- **Financial-condition evidence** — vendor is a public-company subsidiary; parent-level audited financials and most-recent 10-K reviewed; status `sound`. Going-concern qualifier absent.
- **Concentration and sub-contractor footprint** — single hyperscaler in two regions; same hyperscaler is the firm's primary IaaS for several other vendors. `concentration_flag = watch` and pointer to concentration-risk-review for portfolio analysis.
- **AI-specific findings** — section omitted (`ai_vendor = false`).
- **Contract gap summary** — pointer to the contract-gap-review record. Headline gaps: missing examiner-access clause under Bank Service Company Act, missing breach-notification clock at the platform-incident level (only at the customer-data-incident level), and silence on subcontractor change consent.
- **Recommended onboarding decision and review gates** — `approve-with-conditions`. Conditions: failover-region BCDR tabletop evidenced before go-live; examiner-access clause inserted; breach-notification clock added; subcontractor change consent added; firm enables customer-managed keys before NPI flows to the platform. Review gates: scope, evidence, authority, impact, decision. Decision sits with the head of TPRM and the business-owner SVP per the firm's policy for important-tier vendors. Annual recertification scheduled.

The pack stops at the recommendation. It does not approve the vendor.

## Why this scenario matters

- **Boundary check on AI-vendor mode**: the platform has an embedded AI feature, but it is off. The skill must avoid pulling the AI overlay in by reflex. The right answer is `ai_vendor = false` now, with a note that re-review is triggered if the feature is enabled.
- **Boundary check on cyber overlay**: cyber overlay applies even though the vendor is not categorised as a "cyber vendor". The skill must apply cyber by default to a vendor that touches NPI.
- **Boundary check on banking sector overlay**: examiner-access under Bank Service Company Act is a banking-only contract clause. Without the banking overlay, the skill misses the gap.
- **Boundary check on impact tolerance**: vendor RTO meets tolerance on paper. The skill must read whether the BCDR test evidence covers the failover scenario, not just the steady-state recovery objective.
- **Boundary check on concentration**: a single-vendor diligence pack is the right place to raise the flag, not to do the portfolio analysis.

## Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023).
- Bank Service Company Act, 12 USC §1867(c).
- 12 CFR Part 30 Appendix D (OCC Heightened Standards).
- FFIEC IT Examination Handbook — Outsourcing Technology Services.
- GLBA Safeguards Rule (16 CFR Part 314 as amended).

See `references/source-anchors.md` for full citations.
