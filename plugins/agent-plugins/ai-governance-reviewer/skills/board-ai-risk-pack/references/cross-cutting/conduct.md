# Cross-cutting overlay: conduct — board AI risk pack

Loaded when the scope flags conduct (consumer compliance, fair-lending, fair-pricing, claims-handling fairness, consumer-facing AI generally). The overlay carries content that lands in the pack body, not background reading.

## Where it lands in the pack

The conduct overlay threads through several pack sections:

- **Inventory state**: customer-facing AI use cases surface as a separate line in the by-architecture or by-business-line breakdown. The committee's standing question is what fraction of in-production AI directly touches customers (decisioning, customer-service assistant, complaint handling, marketing, lead generation), and how that fraction has moved.
- **Top AI risks**: customer-impact and fairness exposure named explicitly when elevated. Adverse-action notice quality on AI-driven credit decisions, fairness-metric drift on AI-driven underwriting, claims-handling AI fairness and accuracy, complaint-rate drift on AI-touched products.
- **Incidents and near-misses**: customer-impact incidents named explicitly. Fairness exposure events (disparate-impact pattern detected by monitoring), customer harm events from AI failures (incorrect decisioning, incorrect customer-facing communication), complaint surges on AI-touched products.
- **Model performance trends**: fairness-metric drift on customer-facing use cases is the standing line. Disparity ratio trending across protected and policy-relevant dimensions on tier-1 and tier-2 customer-facing AI.
- **AI governance maturity posture**: conduct program integration is one of the standing maturity dimensions. Coverage of AI in the consumer compliance program, integration with the firm's complaint-handling process, integration with adverse-action notice generation pipeline for credit decisioning AI.

## Top AI conduct risks (catalogue for selection, not all-required)

- Adverse-action notice quality on AI-driven credit decisioning. CFPB Circular 2022-03 and 2023-03 set the framing; the principal-reasons standard under ECOA / Reg B applies to AI-driven decisions. Specificity is the recurring exam topic.
- Fairness exposure on AI-driven underwriting (credit, life and health insurance). The conduct overlay carries the firm-side fairness testing posture; depth lives in `validation-plan` outputs and the model card fairness sections.
- Claims-handling AI fairness and accuracy. Multistate market-conduct exam focus on claims AI; consumer-protection enforcement on claims-AI accuracy and recourse.
- AI-generated client communications quality and accuracy where the firm is an investment adviser (Marketing Rule scope) or a broker-dealer (FINRA communications standards). Capital-markets sector overlay carries the depth.
- Customer-facing GenAI assistant accuracy and harm risk: hallucination on policy questions, incorrect statements about products or fees, refusal patterns that block legitimate customer requests.
- Complaint-rate drift on AI-touched products. The complaint-rate metric is a standing detective signal for conduct exposure that the model card monitoring section calls out; the pack carries the population view.

## Sign-off questions tagged to conduct

Surface in the reviewer-questions section of the pack when applicable:

- For consumer-credit AI: how does the firm assure principal-reasons specificity in adverse-action notices, and what was the most recent quality review finding.
- For life or health insurance underwriting AI: what is the firm's unfair-discrimination testing cadence, and what is the most recent test finding (NAIC Bulletin fairness element; NYDFS Circular Letter; CO SB 21-169 framework where applicable).
- For customer-facing GenAI assistants: how does the firm monitor accuracy and harm, and what is the trend in customer complaints classified to AI-touched paths.
- How does the firm assure that the adverse-action notification pipeline for AI-driven credit decisions remains compliant when the underlying model is updated, swapped, or migrated to a foundation model.

## Linkage

The depth on conduct-AI controls lives in the model card fairness and explainability section, the validation-plan fairness scope, and outputs from `consumer-compliance-fair-lending` skills (where the firm has run them). The board AI risk pack consumes briefs from those outputs rather than re-anchoring the conduct sources.
