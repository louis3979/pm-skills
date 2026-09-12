---
name: course-correction-planner
description: "Assess the impact of a significant unexpected issue during active delivery and produce a structured change proposal — options to continue, adjust, pivot, or stop, with a clear recommendation. Use when something material has gone off-plan mid-delivery, not for a routine planned scope-change request."
---

# Course Correction Planner

## Purpose

You are navigating a significant, unplanned disruption to $ARGUMENTS mid-delivery (a blocking technical discovery, a market shift, a key dependency falling through, a wrong assumption surfacing late) — turning "something's gone wrong" into a structured proposal instead of an ad hoc scramble.

## Context

Use this when something material and unplanned has knocked the current plan off track. For a routine, planned scope-change request going through normal approval, use `change-control-manager` instead — that's a formal request process; this is triage for a real disruption already in progress.

## Instructions

1. **Name the triggering issue precisely**: what happened, when it was discovered, and how it differs from what the current plan assumed.
2. **Assess impact across everything the current plan touches**: scope (what's now in question), schedule (does the critical path move — use `schedule-critical-path-analyzer` if uncertain), team/resourcing, and any dependent decisions already made on the old assumption (check `decisions/` in project memory if `pm-memory` is in use — a decision made on a now-invalid assumption needs to be flagged, not silently left standing).
3. **Generate options**, not just one path forward:
   - **Continue** — the disruption doesn't actually change the plan; proceed as-is (state why it doesn't, don't just assert it).
   - **Adjust** — modify scope/timeline/approach while keeping the same overall goal.
   - **Pivot** — change the approach materially; the original goal may still hold but the path there changes.
   - **Stop** — the goal itself no longer holds; recommend halting and redirecting effort.
4. **Recommend one option explicitly**, with the trade-off reasoning — never leave this as an unweighted list for someone else to figure out.
5. **Specify what changes concretely** if the recommendation isn't "Continue": updated scope, updated timeline, what gets communicated to whom (pairs with `stakeholder-power-interest-mapper` for who needs to know first).
6. **Name the decision owner and the deadline for deciding** — a course-correction proposal that sits undecided is its own new problem.

## Output

```markdown
# Course Correction: [initiative]

## Triggering Issue
[what happened, when discovered, how it differs from the plan's assumption]

## Impact Assessment
- **Scope**: ...
- **Schedule**: ...
- **Team/Resourcing**: ...
- **Affected prior decisions**: [any decisions made on the now-invalid assumption]

## Options
### Continue
[why this might still be right, or why it's not viable]
### Adjust
[what changes]
### Pivot
[what changes]
### Stop
[what changes]

## Recommendation
[one option, with reasoning]

## Concrete Changes (if not Continue)
- Updated scope: ...
- Updated timeline: ...
- Who needs to know, and in what order: ...

## Decision Owner & Deadline
[who decides, by when]
```

Save as a markdown document.

## Notes

- Always generate all four option types even if one is obviously going to win — a proposal that skips "Continue"/"Stop" without addressing them looks like it never considered the full range.
- If a prior decision was made on an assumption this issue just invalidated, flag it explicitly (and consider running `memory-decide` to formally revisit it if project memory is in use) — don't let a stale decision quietly stand uncorrected.
- This is triage, not blame — name the process gap that let the disruption go unnoticed longer than it should have, if there is one, without turning it into a target-a-person exercise.

## Example

Input: "The third-party data provider we planned the whole Q2 roadmap around just announced they're shutting down in 60 days." Impact: schedule — Q2's two lead initiatives both depend on this provider; prior decision `2026-02-10-defer-in-house-data-pipeline.md` was made assuming this provider would be stable — now invalid, flagged for `memory-decide` revisit. Recommendation: Pivot — accelerate the in-house data pipeline decision, re-scope Q2 initiatives to a reduced dataset in the interim.
