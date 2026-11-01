# Troubleshooting: best-execution-surveillance

Recurring defects in best-execution surveillance artifacts. Each is a finding pattern an examiner or independent reviewer is likely to surface; the skill is structured to make each visible rather than letting it pass.

## Treating "best execution" as best price

The duty is a multi-factor analysis. Rule 5310 .01 lists the BD factors (character of the market, size and type of transaction, number of markets checked, accessibility of the quotation, terms and conditions of the order); the IA fiduciary factor list runs price, speed, likelihood of execution, size, market impact, accessibility, total transaction costs, and customer instructions. Both lists are non-exhaustive. A surveillance read that scores trades only on price (or only on price improvement vs NBBO) misses the duty.

Fix: the trade-exception sheet's `factor_analysis` column walks the full applicable factor list per row, with the rule lattice keyed by `firm_registration`. Do not collapse the factor walk into a single price-comparison line.

## Confusing the BD regular-and-rigorous review with the IA fiduciary review

Rule 5310 .09 requires a regular-and-rigorous review of execution quality at the venue level for BDs not running an order-by-order review. The IA fiduciary review under §206 is a separate duty with overlapping factors but different documentation expectations. Dual registrants commonly run one operational process and produce one document, then face an examiner who reads it under either lattice and finds gaps.

Fix: dual registrants explicitly produce both reads in the artifact. The trade-exception sheet's factor_analysis column walks both factor lists per row; the memo carries separate aggregate-quality summaries for the BD limb (5310 .09 frame) and the IA limb (§206 frame). The committee record references both rule lattices.

## Treating Rule 606 as the best-execution review

Rule 606 is a routing-disclosure obligation under 17 CFR 242.606. It does not, by itself, satisfy the Rule 5310 or §206 review obligation. Surveillance artifacts that consist of a 606 summary plus a confirmation of routing match the disclosure are insufficient; the substantive review is what 5310 / §206 require beyond.

Fix: the 605 / 606 reconciliation sheet is a cross-check on operational data quality and on the firm's own measurement, not the surveillance itself. The trade-exception sheet, the venue-level aggregate-quality sheet, and the conflict-review sheet carry the substantive review.

## Skipping the conflict-as-input step

PFOF, principal trades, agency crosses, affiliated brokerage, soft dollars, commission-sharing arrangements: each must be weighed in the best-execution determination, not just disclosed alongside it. An artifact that lists conflicts in a disclosure block but does not show how the conflict factored into routing or execution decisions misses the substantive review.

Fix: the conflict-review sheet's `weighed_in_determination` column is required for every present conflict, with reference to the committee minutes that captured the weighing. The disclosure-consistency check is a separate column; disclosure does not cure conflict if the underlying conduct does not match.

## Soft-dollar mixed-use without proportional allocation

§28(e) and the 2006 interpretive release require that mixed-use products be allocated between research-eligible and non-research portions based on a reasonable methodology, with contemporaneous documentation. Default-to-100%-research-eligible is wrong; relying on the original eligibility memo years after the actual-usage pattern has shifted is also wrong.

Fix: the conflict-review sheet's soft-dollar row records the mixed-use allocation methodology and pulls the contemporaneous utilisation data; the surveillance reads the methodology against actual usage and surfaces a finding where they diverge. The fund-adviser variant escalates the finding into the §15(c) board materials.

## Affiliated-broker §17(e) treated as "we used them" without comparable-rate benchmark

ICA §17(e)(1) requires reasonable-and-fair compensation; Rule 17e-1 sets the procedural framework. Practice expects a peer-set benchmark refreshed periodically. Affiliated-broker usage shown in the surveillance without the comparable-rate evidence on file is a finding regardless of whether the rates appear acceptable.

Fix: the conflict-review sheet's affiliated-brokerage row pins the comparable-rate evidence file. The fund-adviser variant carries the peer-set refresh date and surfaces a finding when the peer-set is stale.

## Sample sizes calibrated for the median trade, not for the tail

Best-execution issues concentrate in block trades, illiquid securities, after-hours fills, principal trades, agency crosses, and conflicted-routing flow. A sample drawn proportionally from total volume under-samples the tail and misses the issues.

Fix: the sample method is stratified, with the strata over-representing the tail. The scope sheet records the stratification explicitly. A sample stated without an identification method is an assertion, not a finding.

## Fund §15(c) section copy-pasted year-on-year

The §15(c) brokerage and best-execution discussion expects period-specific data and exception detail. Boilerplate attestations are themselves a finding pattern in EXAMS sweeps, regardless of whether the underlying execution quality is acceptable.

Fix: the fund-adviser variant's `fund_15c_attestation` block is per-fund per-period, with the surveillance findings, the §17(e) and §28(e) blocks, and the period-specific data pulled in. Boilerplate language is flagged.

## Committee minutes with no dissents, no questions, no follow-ups across multiple periods

The conduct overlay reads committee minutes for substantive challenge. A multi-period run of meetings where the minutes record only attendance, materials reviewed, and a generic approval (no dissents recorded, no questions noted, no follow-ups assigned) is itself a culture finding even if every individual meeting passed.

Fix: the committee_pack block's `dissents_recorded` field carries an explicit "no dissents recorded" string when none occurred, so the field is not silently empty. The follow-ups field carries the prior-period follow-up status, so an examiner can read the rolling action discipline. The memo's Section 9 surfaces the absence of substantive challenge as a culture observation if the pattern persists.

## Firm-set thresholds and appetite missing from the artifact

Aggregate-quality metrics shown without a threshold against which to read them produce read-outs no committee can act on. The skill default is to mark `[evidence needed]` rather than fabricate a threshold.

Fix: the aggregate_metrics rows record `threshold` and `breach_flag` explicitly; missing thresholds carry `[evidence needed]` and the memo flags the absence. The firm-overlay file is the place to install firm-specific appetite levels; the skill consumes them when present.

## Crypto and FX scope claimed without honest evidence framework

For asset classes lacking a consolidated tape (FX, crypto, fixed income) the surveillance can only rely on the evidence framework that asset class supports: competitive-quote logs for fixed income; price-versus-mid-at-execution and last-look reads for FX; venue-by-venue execution data with the limitations explicitly named for crypto. Claiming NBBO-style coverage in these asset classes overstates the surveillance.

Fix: the asset-class flavour in the capital-markets sector overlay sets the evidence framework per class; the surveillance documents the limitations rather than claiming a coverage it cannot support.
