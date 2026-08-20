# Daycare content governance

## Outcome

Maintain the public RSGE planner with a traceable human-in-the-loop process:

**Report → Jira → Research agent → Evidence → Proposed website change → HITL approval → GitHub → Deploy → Close Jira**

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
| Reported | Intake automation | Jira item created with GitHub report linked |
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
- [ ] Jira issue linked.
- [ ] Human reviewer approved.

## Jira mapping

Recommended Jira issue type: **Bug** for an alleged factual inaccuracy, **Task** for clarification or maintenance.

Recommended fields/labels:

- `source:website-report`
- `component:daycare-planner`
- `risk:wording | deadline | capacity | financial`
- GitHub issue URL
- Source URL(s)
- Research confidence
- PR URL
- Deployed commit SHA

## Secrets and runtime configuration

The GitHub workflows are designed to use repository secrets/variables rather than hard-coded credentials.

Expected configuration:

- `JIRA_BASE_URL` — e.g. `https://<site>.atlassian.net`
- `JIRA_EMAIL` — service-account email
- `JIRA_API_TOKEN` — service-account API token
- `JIRA_PROJECT_KEY` — project selected for Daycare reports
- `OPENAI_API_KEY` — only if the research-agent workflow is enabled

Do not place credentials in the repository.

## Deployment

GitHub Pages deploys only from approved content merged to `main`. Branch protection should require at least one approving review for bot-created PRs before merge.
