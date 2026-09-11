---
name: sprint-planner
description: "Plan a sprint from a prioritized backlog and team capacity — sprint goal, scope recommendation, dependency check, capacity balancing, and risk flagging. Use at the start of a sprint, before commitments are locked in."
---

# Sprint Planner

## Purpose

You are turning a prioritized backlog into a committed sprint plan for $ARGUMENTS, checking that the scope is actually achievable with the team's real capacity — not just accepted on optimism.

## Context

Use this at sprint-planning time, once stories are written (`user-story-writer`) and prioritized. Complements `wbs-scope-decomposer`/`schedule-critical-path-analyzer` (which operate at the larger multi-sprint delivery-plan level) — this is the single-sprint operational pass.

## Instructions

1. **State the Sprint Goal**: one sentence describing the outcome this sprint should produce — not just "complete these tickets," but what becomes true if the sprint succeeds.
2. **Calculate real capacity**: team-days available this sprint, minus time off, minus standing overhead (support rotation, meetings, on-call) — never plan against theoretical 100% capacity.
3. **Propose Scope** from the top of the prioritized backlog, checking it fits calculated capacity — don't just take everything marked "high priority" without checking the math.
4. **Check Dependencies**: does every proposed story have its dependencies (other stories, other teams, external data) already satisfied or scheduled earlier in the sprint?
5. **Balance load across the team**: flag if scope concentrates too heavily on one person/specialty (a single point of failure for the sprint).
6. **Flag Risk**: any story with real uncertainty (unclear estimate, unresolved dependency, first-time-doing-this-kind-of-work) should be flagged, not silently treated as equally safe as routine work.
7. **Leave explicit buffer** for unplanned work (bugs, support escalations) based on the team's actual historical rate of unplanned work, not zero.

## Output

```markdown
# Sprint Plan: [sprint identifier]

## Sprint Goal
[one sentence]

## Capacity
Team-days available: [X] (after time off/overhead)
Buffer reserved for unplanned work: [X%]

## Proposed Scope
| # | Story | Owner | Estimate | Dependency status |
|---|---|---|---|---|

## Load Balance Check
[any concentration risk flagged]

## Risks
- ...

## Explicitly Descoped (if backlog exceeded capacity)
- ...
```

Save as a markdown document.

## Notes

- A sprint plan with zero buffer for unplanned work is not realistic — even a well-run team has some rate of interrupt work; use the team's own historical rate if known, or a conservative default if not.
- If scope doesn't fit capacity, cut scope — don't quietly assume the team will just work harder to hit an unrealistic plan.
- A story with an unresolved dependency should not be committed into the sprint as if it were ready — either resolve the dependency first or explicitly flag the story as at-risk.

## Example

Input: "Plan next sprint from the top 12 backlog stories, team of 4 engineers, 2-week sprint." Output: Capacity — 4 engineers × 9 working days (accounting for 1 day of planned leave) = 36 person-days, minus 15% reserved for support rotation = ~31 person-days available. Proposed scope: top 7 stories fit within 31 person-days; stories 8-12 explicitly descoped to next sprint, with story 9 flagged as blocked pending a data-migration dependency owned by another team.
