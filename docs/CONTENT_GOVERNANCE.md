# Daycare content governance

## Outcome

Maintain the public RSGE planner with a traceable human-in-the-loop process:

**Report → Jira → Research agent → Evidence → Proposed website change → HITL approval → GitHub → Deploy → Close Jira**

## Dedicated Jira project

Daycare content governance uses the dedicated Jira project that now exists in the connected Atlassian site:

- **Project name:** RSGE Recognition Planner
- **Project key:** `RSGE`
- **Purpose:** website accuracy reports, regulatory research, proposed content changes, HITL approvals, deployment traceability and closure.
- **Current issue types:** Workstream, Task, Sub-task.

Do not mix RSGE planner governance work into unrelated Jira projects such as EAID or PCA.

Because the current RSGE project does not expose a `Bug` issue type, factual/regulatory inaccuracy reports are represented as **Task** items with classification labels.

## Control principles

1. **Primary-source first.** Legal or regulatory claims must be supported by Québec legislation, Québec government guidance, or the responsible Bureau coordonnateur where applicable.
2. **No autonomous production edits.** The research agent may prepare a branch and pull request, but it must not merge to `main`.
3. **Human approval for consequential content.** Any change that affects eligibility, capacity, deadlines, required credentials, money, or calculator logic requires explicit human approval.
4. **Traceability.** Every change must retain the original report, Jira key, evidence URLs, research notes, PR, reviewer decision, and deployed commit.
5. **Smallest safe change.** The agent should modify only the content or logic required to correct the verified issue.
6. **Uncertainty is visible.** If sources conflict or the rule is not clear, the page should say that confirmation is required rather than presenting a guess as fact.

## Workflow states

| State | Owner | Exit condition |
| --- | --- | --- |
| Reported | Intake automation | RSGE Jira Task created with GitHub report linked |
| Researching | Research agent | Sources collected and claim assessed |
| Needs evidence | Human / reporter | Missing or conflicting authoritative evidence resolved |
| Change proposed | Research agent | Draft PR created with evidence and impact statement |
| HITL review | Human reviewer | Accuracy and implementation reviewed |
| Approved | Human reviewer | PR approved for merge |
| Deployed | GitHub Pages | Approved PR merged and deployment succeeds |
| Closed | Automation / human | Jira contains deployed commit and final resolution |

Alternate terminal states: **Rejected**, **Duplicate**, **No change required**.

## Required evidence package

Every proposed correction must contain:

- Jira issue key.
- Original GitHub accuracy report URL.
- Exact statement or behaviour being challenged.
- Proposed correction.
- One or more authoritative source URLs.
- Source publication/effective date when relevant.
- Research agent confidence: `high`, `medium`, or `low`.
- Impact classification:
  - wording only;
  - deadline/task;
  - legal eligibility/capacity;
  - financial/calculator;
  - other.
- Files and logic affected.
- Test/verification notes.

## Pull request gate

A research-agent PR must include the following checklist and remain unmerged until a human reviewer approves it:

- [ ] Claim reproduced from the current site.
- [ ] Primary source checked.
- [ ] Effective/current date checked where relevant.
- [ ] Conflicting sources disclosed.
- [ ] Calculator/deadline implications assessed.
- [ ] Change is the minimum necessary correction.
- [ ] RSGE Jira issue linked.
- [ ] Human reviewer approved.

## Jira mapping

Current intake issue type: **Task**.

Recommended labels:

- `daycare-planner`
- `accuracy-report`
- `source-github`
- `risk-wording`
- `risk-deadline`
- `risk-capacity`
- `risk-financial`

Evidence should also retain:

- GitHub issue URL
- Source URL(s)
- Research confidence
- PR URL
- Deployed commit SHA

## Initial implementation backlog

- `RSGE-1` — Establish HITL content-governance pipeline
- `RSGE-2` — Wire website accuracy reports into RSGE Jira intake
- `RSGE-3` — Implement research-agent evidence workflow
- `RSGE-4` — Enforce HITL pull-request approval gate
- `RSGE-5` — Trace deployment and close Jira after approved merge

## Secrets and runtime configuration

The GitHub workflows use repository secrets rather than hard-coded credentials.

Expected configuration:

- `JIRA_BASE_URL` — `https://junip1dev.atlassian.net`
- `JIRA_EMAIL` — service-account email
- `JIRA_API_TOKEN` — service-account API token
- `JIRA_PROJECT_KEY` — optional override; defaults to `RSGE`
- `RESEARCH_AGENT_WEBHOOK_URL` — optional research-agent integration endpoint
- `OPENAI_API_KEY` — only if an OpenAI-backed research-agent runtime is enabled

Do not place credentials in the repository.

## Deployment

GitHub Pages deploys only from approved content merged to `main`. Branch protection should require at least one approving review for bot-created PRs before merge.
