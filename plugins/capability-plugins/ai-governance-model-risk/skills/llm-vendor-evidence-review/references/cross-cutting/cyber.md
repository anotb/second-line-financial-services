# Cross-cutting overlay: cyber

Loaded when `engagement-scope.cross_cutting_overlay_set` includes cyber. The cyber overlay should be considered the default for foundation-model evidence-pack reviews; the threat surface a foundation-model vendor exposes is, in regulator framing, a cybersecurity risk class. The CISO function is a co-reviewer for the security and privacy criteria.

## Supervisory frame

The cyber framings carrying binding supervisory expectation in their respective scopes:

- **NYDFS 23 NYCRR Part 500** for NY-footprint covered entities (state-chartered banks, insurers, money transmitters, virtual currency businesses operating in NY). The October 2024 Industry Letter on Cybersecurity Risks Arising from AI extends Part 500 application to AI-specific risks including third-party AI service-provider security under §500.11.
- **SEC cyber disclosure rules** (Reg S-K Item 106, Form 8-K Item 1.05) for SEC public registrants, where a vendor-AI incident contributes to a material cybersecurity incident requiring disclosure.
- **GLBA Safeguards Rule** (16 CFR Part 314) for FTC-supervised non-bank financial institutions, including the May 2024 notification provisions (16 CFR §314.5(d)) for unencrypted-customer-information events affecting 500 or more consumers.
- **State Insurance Data Security Model Law** (NAIC Model Law 668) for insurers in adopted states.
- **FFIEC IT Examination Handbook** for federally supervised banks; the Information Security and Architecture, Infrastructure, and Operations booklets carry application-security and third-party-risk sections relevant to AI-vendor posture.
- **The 36-hour banking computer-security incident notification rule** (12 CFR Part 53, with parallel FRB and FDIC rules) for bank-affiliated entities, where a vendor-AI incident constitutes a notification incident.

The leading-practice references that carry weight without being binding: NIST AI 600-1 Generative AI Profile (Govern 6.x for third-party considerations and Manage 3.x for incident-disclosure expectations); NIST SP 800-53 (control families for the cyber-side of vendor evidence: AC, AU, IR, SI, SR); ISO/IEC 27001/27002 and SOC 2 Trust Service Criteria as the third-party attestation frame.

## Cyber-specific evidence asks

The cyber overlay surfaces the following beyond the cross-cutting baseline in the security-posture and privacy-posture criteria:

- **Authentication and authorisation posture for the model-serving endpoint.** Vendor evidence should establish identity and access controls on the API or serving plane; SOC 2 Type II covers the operating effectiveness of these controls in the relevant period. The complementary user-entity controls section of SOC 2 names the firm-side responsibilities; record acceptance of those by the firm's CISO function.

- **Audit logging of model invocations and retrievals.** Vendor evidence should establish what is logged, by whom, with what retention. The firm's incident-response capability depends on log-availability; vendor opacity here is a cyber-side gap that limits the firm's incident-investigation depth.

- **Model supply-chain controls.** Foundation-model vendors depend on training-data sources, evaluation contractors, red-team contractors, cloud infrastructure. The supply-chain posture of the model itself is part of the cyber assessment; the SR control family in NIST SP 800-53 frames the asks.

- **Adversarial-robustness evidence.** The vendor's published red-team summary, dangerous-capability evaluations, and jailbreak-resistance benchmarks feed the firm's understanding of the cyber-relevant adversarial profile. These are vendor self-attestation; record at vendor-self-attestation confidence and chain to `prompt-injection-risk` for in-firm coverage of the deployed system.

- **Incident-disclosure history and notification-cadence posture.** The vendor's historical incident disclosures and the cadence and granularity of disclosure feed the firm's ability to meet its own regulator-notification obligations. Where the vendor's notification cadence is loose, the firm's disclosure posture under §500.17(a), Item 1.05, GLBA §314.5(d), and the 36-hour banking rule is at risk; record the residual reliance.

- **Network controls and data-isolation posture.** For hosted-API forms, the network-isolation posture (regional pinning, VPC peering, dedicated capacity options) feeds the firm's data-residency and data-isolation posture; the privacy overlay carries the residency specifics.

- **Secrets-handling posture.** API keys, signing keys, customer-data-encryption keys: the vendor's posture on secrets handling and rotation feeds the firm's CISO assessment.

## Cyber-specific co-reviewer expectations

The CISO function is a co-reviewer for the security-posture, privacy-posture, content-provenance, and incident-disclosure-history criteria of `sufficiency_view[]`. The CISO function attests jointly with the AI Governance Lead on `reviewer_attestation`. For NY-footprint entities, the Part 500 CISO sign-off responsibility extends to the AI-vendor evidence review; record alignment with the CISO function's annual certification cycle.

## Cyber-specific re-review triggers

In addition to the baseline triggers, cyber adds:

- Vendor-disclosed cybersecurity incident affecting the model variant in scope or the underlying serving plane.
- New cybersecurity-related supervisory action (NYDFS, federal banking, SEC) referencing the vendor or vendor class.
- Material change in the vendor's SOC 2 scope, control objectives, or auditor opinion.
- Material change in the vendor's API security posture, authentication mechanism, or default network controls.
- Disclosure of a vulnerability or compromise affecting the vendor's adversarial-robustness controls.

## Cyber-specific structured-output additions

The `cross_cutting_overlay_notes` block in the schema carries the cyber-specific findings:

```
"cross_cutting_overlay_notes": {
  "cyber": {
    "soc2_summary": "...",
    "iso27001_summary": "...",
    "authn_authz_posture": "...",
    "audit_logging_depth": "...",
    "model_supply_chain_posture": "...",
    "adversarial_robustness_evidence_summary": "...",
    "incident_disclosure_cadence": "...",
    "network_isolation_posture": "...",
    "secrets_handling_posture": "...",
    "ny_part500_alignment_status": "...",
    "sec_8k_item105_materiality_input": "...",
    "glba_safeguards_rule_alignment": "...",
    "ciso_attestation_status": "..."
  }
}
```
