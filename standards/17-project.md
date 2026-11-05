# 17 · Project and client management

**Why it matters:** Most website projects fail on scope, budget, missing content or unclear decisions, not on code. A written scope, a priced estimate, named decision-makers, change control and a clean handover keep the project on time and the client relationship healthy after launch. Guide: steps 1, 8, 35 and 41.

Scope: scope, estimate and running costs, timeline, roles and decisions, change requests, status and risks, phase acceptance, handover, maintenance agreement, contracts, post-launch review. Templates: [`project-plan.md`](../templates/project-plan.md), [`handover.md`](../templates/handover.md), [`maintenance-agreement.md`](../templates/maintenance-agreement.md). Goals and audiences: [`01-strategy.md`](01-strategy.md).

Last verified: 2026-11

| ID | Level | Rule | Verify |
|---|---|---|---|
| PRJ-01 | MUST | A written scope lists deliverables, what is in and out of scope, assumptions, client inputs (content, photos, access) with due dates, and acceptance criteria per deliverable. It is signed before design starts, together with the brief (STR-01). | Signed scope in `project-plan.md` |
| PRJ-02 | MUST | [house] The estimate is broken down by phase (discovery to maintenance) with ranges, assumptions and a contingency of ≥ 15 %. Yearly running costs are listed separately: hosting, domains, licenses (fonts, images, plugins), tools, third-party services (TEC-20) and maintenance. | Estimate and cost table reviewed with the client |
| PRJ-03 | SHOULD | The timeline sets milestones per phase and approval gates (brief, design, content, launch). Items that block others (content delivery, legal review, DNS and account access) have an owner and a date. | Timeline in `project-plan.md` |
| PRJ-04 | MUST | Roles are named: one decision-maker on the client side, who approves what (a simple RACI), and owners for content, legal pages and every account (TEC-13). | Roles table filled |
| PRJ-05 | MUST | Every change after sign-off is a change request with written impact on scope, cost and time, approved before work starts and logged. | Change log |
| PRJ-06 | SHOULD | A short status goes out at a fixed rhythm (e.g. weekly): done, next, risks, decisions needed. Risks sit in a log with owner and mitigation. | Status history; risk log |
| PRJ-07 | MUST | Each phase ends with written acceptance against its acceptance criteria and checklist (QA-11, [`2-launch.md`](../checklists/2-launch.md) for launch). Open items are listed with owner and date. | Acceptance record per phase |
| PRJ-08 | MUST | Handover: documentation (TEC-26, TEC-27), all accounts and credentials transferred to the owner (TEC-13), editor training (TEC-37), and a warranty period with defined scope ([house]: 30 days, P0–P2 defects per QA-10 fixed free of charge). | Signed [`handover.md`](../templates/handover.md) |
| PRJ-09 | SHOULD | Ongoing care runs under a maintenance agreement: updates (TEC-25), security patch times (SEC-15), backups and restore tests (TEC-12), monitoring (MSR-21), the reporting rhythm (MSR-25), included content hours, response times by severity (QA-10), price, term and exit (data, code and access returned). | Agreement from [`maintenance-agreement.md`](../templates/maintenance-agreement.md) |
| PRJ-10 | SHOULD | [EU] Contracts settle who owns the design and code, the licenses for fonts, images and plugins (TEC-27), a data processing agreement where personal data is processed (PRV-05), and liability. Flag for legal review. | Contract checklist reviewed |
| PRJ-11 | SHOULD | After launch, a short retrospective records what to keep and change; at 90 days, results are compared with the baseline and targets (STR-10, MSR-25). | Retrospective and 90-day review notes |

## Sources

- [GOV.UK Service Manual: Agile delivery](https://www.gov.uk/service-manual/agile-delivery) (phases, roles, assessments)
- [EU GDPR Art. 28 (processors)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
