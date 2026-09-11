---
description: Plan a delivery from scope breakdown through schedule/critical path to a tracked risk register, in one pass
argument-hint: "<a large deliverable/epic to plan>"
---

# /plan-delivery-risk -- Delivery Planning Pass

Turn a large, unplanned deliverable into a decomposed scope, a scheduled critical path, and a tracked risk register — the PMBOK Planning knowledge areas applied in sequence.

## Invocation

```
/plan-delivery-risk New multi-tenant billing system
/plan-delivery-risk Migrate the legacy auth service to the new identity provider
/plan-delivery-risk [paste a PRD or epic description]
```

## Workflow

### Step 1: Understand the Deliverable

Ask if not already clear:
- What's the target deliverable and its rough scope boundary?
- Is there a target date already committed, or is this planning informing the date?
- What team(s)/skills are available to staff this?

### Step 2: Decompose Scope

Apply the **wbs-scope-decomposer** skill:

- Break the deliverable into a Work Breakdown Structure with in/out-of-scope and acceptance criteria per node
- Flag any ambiguous ownership before moving on

### Step 3: Build the Schedule

Apply the **schedule-critical-path-analyzer** skill:

- Sequence the WBS leaf nodes into activities, estimate durations, identify the critical path
- Compute float for non-critical activities

### Step 4: Build the Risk Register

Apply the **risk-register-manager** skill:

- Identify risks specific to this deliverable (technical, schedule, resource, vendor, data)
- Analyze probability × impact, plan a response, assign an owner and a monitoring trigger

### Step 5: Consolidate the Plan

```
## Delivery Plan: [deliverable]

### Scope (WBS summary)
[top 2 levels of the WBS, link to full breakdown]

### Schedule
Critical path: [chain] — projected finish: [date]

### Top Risks
| Risk | Probability | Impact | Response | Owner |
|---|---|---|---|---|

### Open Questions
- ...
```

Save as markdown.

### Step 6: Offer Next Steps

- "Want me to **set up the access control layer** for this deliverable (`/setup-access-controls`)?"
- "Should I **run a security/technical-impact pass** before engineering starts (`/prep-technical-handoff`)?"
- "Want me to **track delivery metrics** once this is underway (`project-metrics-tracker`)?"

## Notes

- If the target date was already committed before this planning pass, and the critical path doesn't support it, say so plainly — don't quietly reshape the plan to fit a date that isn't realistic.
- Risks discovered during scheduling (e.g. a genuinely unknown estimate) should flow into the risk register, not stay buried in the schedule notes.
- This is a planning pass, not a one-time artifact — re-run the risk register step on a cadence as the deliverable progresses.
