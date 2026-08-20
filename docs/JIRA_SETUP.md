# Dedicated Jira project setup

The Daycare governance pipeline uses the dedicated Jira project that now exists in the connected Atlassian site.

## Project

- Name: **RSGE Recognition Planner**
- Key: **RSGE**
- Project type: Jira business project
- Current issue types: **Workstream**, **Task**, **Sub-task**

Because this project does not currently expose a `Bug` issue type, website accuracy reports are created as **Task** items and classified with labels such as `accuracy-report` and `source-github`.

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

## GitHub configuration

The GitHub intake workflow defaults to Jira project key `RSGE`.

Repository secrets required:

- `JIRA_BASE_URL` = `https://junip1dev.atlassian.net`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`

Optional repository variable:

- `JIRA_PROJECT_KEY` — only needed if the project key is changed from `RSGE`.
- `JIRA_DONE_TRANSITION_ID` — optional, used only when automated post-deployment closure is enabled.

## Current implementation tasks

The dedicated Jira project contains the initial governance work:

- `RSGE-1` — Establish HITL content-governance pipeline
- `RSGE-2` — Wire website accuracy reports into RSGE Jira intake
- `RSGE-3` — Implement research-agent evidence workflow
- `RSGE-4` — Enforce HITL pull-request approval gate
- `RSGE-5` — Trace deployment and close Jira after approved merge

## Human-in-the-loop rule

Research automation may collect evidence, create a branch and prepare a draft PR. It must not merge a regulatory, financial, eligibility, capacity or deadline change to `main` without human approval.
