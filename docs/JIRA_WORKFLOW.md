# DAYCARE Jira workflow

This project uses a dedicated Jira space/project named **Daycare** with key **DAYCARE**.

## Recommended management model

Use a **team-managed Kanban** space for the initial implementation. It is self-contained, quick to configure, and suitable for a small governance workflow. If Daycare governance later needs shared enterprise schemes or centralized Jira administration, it can be reconsidered.

## Status model

Minimum viable board:

- Reported
- Researching
- Needs evidence
- Change proposed
- HITL review
- Approved
- Deployed
- Done

Alternate terminal states:

- Rejected
- Duplicate
- No change required

## Automation contract

1. A website accuracy report creates a GitHub issue.
2. GitHub Actions creates a DAYCARE Jira Bug.
3. Research automation gathers authoritative evidence.
4. The agent records evidence and prepares a proposed change.
5. The agent opens a draft GitHub pull request.
6. A human reviewer approves or rejects the change.
7. Approved changes are merged to `main` and deployed by GitHub Pages.
8. Deployment evidence is written back to the Jira issue before closure.

## HITL boundary

The research agent may create branches, evidence files and draft pull requests. It may not merge changes affecting regulatory requirements, eligibility, deadlines, capacity, fees, funding or financial-calculator logic without explicit human approval.
