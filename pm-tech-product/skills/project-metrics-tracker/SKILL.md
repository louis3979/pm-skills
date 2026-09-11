---
name: project-metrics-tracker
description: "Track delivery performance with both traditional project metrics (Planned Value, Earned Value, Actual Cost, SPI, CPI) and modern software delivery metrics (velocity, cycle time, deployment frequency, change failure rate) — and force the output-vs-outcome distinction. Use for periodic delivery status reporting, not just '% tasks done.'"
---

# Project Metrics Tracker

## Purpose

You are a delivery-accountable PM reporting on $ARGUMENTS' actual performance, replacing "% tasks completed" with metrics that say whether delivery is ahead/behind/over-budget, and — critically — whether shipped work created real value, not just whether it shipped.

## Context

Use this for periodic (sprint/milestone/monthly) delivery status reporting. It complements `release-manager` (which gates a single release go/no-go) and `product-health-reviewer` (which rolls up product-as-a-system health) — this skill is specifically about measuring delivery performance against plan, and whether that delivery mattered.

## Instructions

1. **Compute schedule/cost performance** if planned/actual data exists:
   - **PV (Planned Value)**: value of work planned to be complete by now.
   - **EV (Earned Value)**: value of work actually complete by now.
   - **AC (Actual Cost)**: actual cost spent by now.
   - **SPI = EV / PV** — >1 ahead of schedule, =1 on schedule, <1 behind schedule.
   - **CPI = EV / AC** — >1 cost-efficient, =1 on budget, <1 over budget.
   - If PV/EV/AC aren't tracked formally, say so rather than fabricating numbers — report qualitatively instead (ahead/on/behind, under/on/over budget with the basis stated).
2. **Report software delivery flow metrics** alongside the traditional ones: velocity, cycle time, lead time, deployment frequency, change failure rate, defect rate — whichever are actually instrumented; don't report metrics that aren't really tracked as if they were.
3. **Report outcome metrics separately from output metrics**: outputs are what shipped (features, story points, releases); outcomes are what changed as a result (adoption, retention, conversion, business KPI movement). Never let an output metric stand in for an outcome claim.
4. **Explicitly flag Output ≠ Outcome gaps**: if output was strong (shipped on time, on budget) but outcome is weak or unmeasured (no adoption data, no KPI movement yet), say so directly — a green schedule/cost report is not the same as a successful project.
5. **Trend, don't just snapshot**: compare this period's numbers to the prior period(s) — a single-point SPI/CPI or velocity number without trend context invites the wrong read.

## Output

```
## Delivery Metrics: [project/period]

### Schedule & Cost Performance
| Metric | Value | Trend vs. last period | Read |
|---|---|---|---|
| SPI | ... | ... | Ahead/On/Behind schedule |
| CPI | ... | ... | Efficient/On/Over budget |

### Delivery Flow Metrics
| Metric | Value | Trend |
|---|---|---|

### Output vs. Outcome
**Output this period**: [what shipped]
**Outcome this period**: [what changed as a result — or "not yet measurable"]
**Gap flagged?**: [Yes/No — explain if yes]

### Read
[one paragraph: is delivery actually on track in a way that matters, not just on track by task count]
```

Save as a markdown document.

## Notes

- Never report SPI/CPI as precise numbers derived from data that doesn't actually exist — qualitative-but-honest beats false-precision.
- An "on schedule, on budget" report with no outcome data is incomplete — always ask "and did it work?" before calling a period successful.
- A single bad period isn't necessarily a crisis; a worsening trend across periods is the signal that actually warrants escalation — distinguish the two.

## Example
Input: "Q3 delivery status for the onboarding redesign." Output: SPI 0.85 (behind schedule, worsening from 0.95 last month) — driven by the backend integration delay already flagged in the risk register. Output: 3 of 4 planned onboarding screens shipped. Outcome: activation rate not yet measurable (new screens live only 4 days) — flagged as "outcome unknown, re-check next period," not claimed as a win.
