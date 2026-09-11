---
name: schedule-critical-path-analyzer
description: "Sequence activities, estimate durations, and identify the critical path for a delivery timeline — then assess how a specific delay actually affects the release date. Use when building a schedule, or when a task slips and you need to know if the release date is really at risk."
---

# Schedule / Critical Path Analyzer

## Purpose

You are a delivery-accountable PM building or stress-testing a schedule for $ARGUMENTS, so "is the release date at risk?" gets answered with the actual dependency chain instead of a gut feeling.

## Context

Use this when building a delivery schedule (after `wbs-scope-decomposer` has broken down the work) to find the sequence of dependent tasks that actually determines the finish date — the Critical Path. Also use it reactively: when one task slips, to determine whether that slip touches the critical path (real schedule risk) or has float (no impact on the release date).

## Instructions

1. **Define Activities**: list the discrete tasks needed, at a granularity fine enough to estimate and sequence (reuse a WBS if one exists rather than re-deriving it).
2. **Sequence Activities**: identify true dependencies — which tasks must finish before another can start (finish-to-start), versus tasks that can run in parallel. Don't assume sequential order by default; parallelizable work should be marked as such.
3. **Estimate Duration** per activity — a single estimate is fine for straightforward tasks; for uncertain ones, capture a range (optimistic/likely/pessimistic) rather than false precision.
4. **Build the Schedule**: lay out the full dependency graph with durations, and compute the **Critical Path** — the longest sequence of dependent activities, which sets the minimum possible completion date.
5. **Compute Float** for every non-critical-path activity — how much it can slip before it affects the finish date. Tasks with zero float are effectively on the critical path even if not obviously so.
6. **When a specific delay is reported**, don't reflexively assume the release date moves: check whether the delayed task is on the critical path or has float that absorbs it. Only a critical-path delay (beyond its float) moves the finish date — state the actual new date, not a vague "this might push things back."
7. **Recommend compression options** if the critical path needs to shrink: fast-tracking (running normally-sequential tasks in parallel, at added coordination risk) or crashing (adding resources to shorten a task, at added cost) — name the specific trade-off, don't just say "compress the schedule."

## Output

```
## Schedule Analysis: [project/release]

### Activity List & Dependencies
| # | Activity | Depends on | Duration | Float |
|---|---|---|---|---|

### Critical Path
[Activity A] → [Activity B] → ... → [Activity N]
Total duration: [X days] → Projected finish: [date]

### Delay Impact (if analyzing a specific slip)
Activity affected: [name]
On critical path? [Yes/No]
Float available: [X days]
New projected finish date: [date, or "unchanged"]

### Compression Options (if finish date needs to move earlier)
- Fast-track: [which tasks, what coordination risk]
- Crash: [which task, what added cost/resource]
```

Save as a markdown document.

## Notes

- A delay to a task with float does not move the release date — say so explicitly rather than defaulting to alarm.
- Never present a schedule with a single-point finish date and no critical path called out — the whole point of this analysis is knowing which task actually controls the date.
- If durations are pure guesses with no basis (no historical velocity, no engineering estimate), say so and flag the schedule as low-confidence rather than presenting it with false authority.

## Example

Input: "Backend integration slipped 5 days. Does our launch date move?" Output: "Backend integration is on the critical path (Requirement → Design → Backend → Frontend → QA → UAT → Production) with 0 days of float. The 5-day slip pushes the projected finish date from March 10 to March 15, unless Frontend/QA/UAT can be fast-tracked to partially absorb it."
