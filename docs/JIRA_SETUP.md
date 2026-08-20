# Dedicated Jira project setup

The Daycare governance pipeline targets a dedicated Jira project.

## Project

- Name: **Daycare**
- Key: **DAYCARE**
- Recommended template: lightweight software / Kanban project

## Suggested workflow

Use the closest available statuses and evolve them if needed:

1. Reported
2. Researching
3. Needs evidence
4. Change proposed
5. HITL review
6. Approved
7. Deployed
8. Done / Closed

Alternate outcomes: Rejected, Duplicate, No change required.

## Issue types

- Bug — factual/regulatory inaccuracies
- Task — maintenance and source refreshes
- Story — larger user-facing improvements
- Epic — optional grouping

## GitHub configuration

The workflow defaults to Jira project key `DAYCARE`.

Repository secrets required:

- `JIRA_BASE_URL` = `https://junip1dev.atlassian.net`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`

Optional repository variable:

- `JIRA_PROJECT_KEY` — only needed if the project key is changed from `DAYCARE`.

## Human-in-the-loop rule

Research automation may collect evidence, create a branch and prepare a draft PR. It must not merge a regulatory or financial content change to `main` without human approval.
