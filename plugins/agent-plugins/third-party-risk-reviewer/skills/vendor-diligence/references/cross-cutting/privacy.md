# Privacy cross-cutting overlay — vendor-diligence

When the engagement scope flags privacy, or whenever the vendor processes nonpublic personal information, protected health information, biometric data, customer prompts, or any other regulated personal data, load this overlay. Privacy is in scope by default for AI vendors that process customer prompts.

## Operative anchors

- **GLBA Safeguards Rule (Standards for Safeguarding Customer Information, 16 CFR Part 314 as amended)** — for financial-institution covered entities. §314.4(f) service-provider obligations: select and retain providers capable of maintaining appropriate safeguards, contractually require them to do so, and periodically assess them. The diligence must evidence each leg.
- **GLBA Privacy Rule (Regulation P, 12 CFR Part 1016)** — privacy-notice and information-sharing posture; relevant where the vendor receives nonpublic personal information.
- **HIPAA Privacy and Security Rules (45 CFR Parts 160, 162, 164)** — where the vendor touches protected health information, business-associate agreement (BAA) posture is required. The diligence must confirm BAA execution, the breach-notification chain (60-day clock), and minimum-necessary access posture.
- **State privacy laws** — CCPA / CPRA (California), VCDPA (Virginia), CTDPA (Connecticut), and the rolling list of state comprehensive privacy laws. Coverage and definitions vary; pin by state of the firm's customer footprint and the vendor's data location. GLBA-covered data is excluded from many state privacy laws but not all; the diligence must read the GLBA-exemption scope state-by-state.
- **NAIC Insurance Data Security Model Law (Model #668), §4.F** (insurance only) — for insurance carriers, this is the operative third-party-service-provider obligation set, additive to or overlapping with NYDFS 500.11.
- **NYDFS 23 NYCRR Part 500.11** — third-party security covers privacy considerations within the cyber-program frame.
- **SEC Reg S-P (May 2024 amendments)** [verify exact compliance dates by entity type and size] — for advisers, BDs, and funds: customer-information-safeguarding and breach-notice elements; 30-day customer notice posture; service-provider written contracts requiring breach notification.

## Evidence the privacy overlay expects

- **Data-processing register** — what data, what categories of data subject, what processing purposes, what retention windows, what cross-border flows.
- **Data-residency commitments** — region-pin terms in the contract; supporting technical evidence (region tags, data-residency reports, transfer-restriction enforcement).
- **Sub-processor list** — current list and the change-notice mechanism. Flow-down clauses do not equal visibility.
- **Privacy-incident-response posture** — severity taxonomy, customer-notification clock, regulator-notification clock, evidence of past incidents.
- **Data-subject-rights handling** — how the vendor processes customer access, deletion, correction, opt-out requests routed through the firm.
- **Privacy-impact-assessment evidence** — for use cases that meet the firm's PIA threshold; the vendor's PIA may inform the firm's PIA but does not substitute.

## AI vendor privacy considerations

This is the highest-leverage section of the privacy overlay for AI-vendor diligence. When `ai_vendor=true`:

- **Prompts as customer data** — customer interactions can carry NPI, PHI, PCI, or other regulated data into the vendor pipeline. The diligence must perform the prompt-as-customer-data assessment regardless of whether the firm intends to send regulated data. Inadvertent PII / PHI in narratives is the dominant failure mode (claims FNOL, customer-support chats, RAG over customer documents).
- **Training-data posture** — the vendor's enterprise default is rarely the consumer default. The contract addendum and the trust-and-safety pages set the operative posture. Do not accept marketing copy as evidence; read the contract clause that says whether API content is used for training, whether outputs are retained for safety classifiers, and whether the abuse-monitoring exception modifies the public default.
- **Retention windows** — typical vendor postures include a 30-day rolling retention for abuse monitoring even where training-use is disabled. The diligence must surface this as a privacy fact, not as a footnote.
- **Customer-data isolation** — fine-tune data and RAG-context data must be isolated; multi-tenant models with shared training pools change the privacy calculus.
- **Output-retention** — model outputs derived from PHI inherit PHI status under HIPAA. The vendor's output-retention posture is a HIPAA business-associate question.
- **Cross-border** — prompt processing in non-firm-permitted regions is a residency violation. Region-pinning evidence must be cited.
- **Right-to-deletion / right-to-correction** — implementing data-subject rights against an LLM is technically open; the contract must address how the vendor will support the firm's response to a deletion request when the data may have flowed through training, fine-tuning, or retention windows.

## Cross-link inside the plugin

- The privacy overlay feeds `contract-gap-review` for the data-processing-addendum (DPA), HIPAA BAA, sub-processor-change clause, and breach-notification clock language.
- The privacy overlay feeds `exit-plan` for the data-return / data-destruction obligation set on termination and the post-termination retention posture.

## Common privacy-overlay pitfalls

- Treating the vendor's marketing-page privacy posture as the contractual posture. The contract is the operative document; trust-and-safety pages modify the public default in both directions.
- Skipping the prompt-as-customer-data analysis on an AI vendor because the firm "doesn't intend to send PII".
- Missing HIPAA business-associate analysis on a "tech vendor" that incidentally touches PHI.
- Treating GLBA exemption from a state privacy law as blanket exemption when the vendor processes data outside the GLBA-covered scope.
- Treating SOC 2 Type II as if it covered privacy specifically; SOC 2 covers the Privacy criterion only when the vendor opts in to it.
- Setting the breach-notification clock to the vendor's preferred clock instead of to the firm's downstream regulator-notification clock.
