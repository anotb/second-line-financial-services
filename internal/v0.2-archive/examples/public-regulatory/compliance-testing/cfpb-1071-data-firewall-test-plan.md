# Section 1071 protected demographic information firewall test plan

## Source anchors

- CFPB Section 1071 rule page describes data collection and reporting for small business credit applications, including privacy interests, publication, shielding certain demographic data from underwriters and other persons, recordkeeping, enforcement, and compliance dates.
- Regulation B section 1002.107 describes covered financial institution obligations to compile and maintain data for covered applications from small businesses.

## Control objective

Protected demographic information collected for reportable small business lending applications is shielded from employees and officers involved in credit determinations, unless a permitted exception is documented.

## Test approach

| Test step | Evidence |
|---|---|
| Identify population of covered applications for the period | Application register export and product scope memo |
| Select sample across channels and decision outcomes | Sample selection file and rationale |
| Inspect system access roles for protected demographic fields | Access matrix and role-permission export |
| Reperform access check for sampled users involved in decisions | User access report and underwriter assignment record |
| Inspect exception approvals where access cannot be shielded | Exception memo, notice language, reviewer approval |
| Validate record retention evidence | Data retention setting or archive report |

## Expected exception types

- Protected field visible to credit decision maker without documented exception.
- Missing evidence that applicant-provided data request occurred before final action.
- Application register field missing or inconsistent with source system.

## Human-review gate

Compliance testing lead and fair lending counsel should review exceptions and severity before issue issuance.
