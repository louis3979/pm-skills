---
name: product-health-reviewer
description: "Produce a periodic (weekly/monthly) product health rollup across KPIs, delivery, incidents, feedback, churn, risks, and strategic progress. Use as a recurring operating-cadence artifact for the product as a system — not for one person's personal activity, and not for a single incident post-mortem."
---

# Product Health Reviewer

## Purpose

Give a recurring, structured view of whether the product overall is healthy, distinct from a personal activity log, so degrading signals are caught early across dimensions that don't naturally get looked at together.

## Context

Pull strategic-progress data (OKRs/roadmap), delivery status, and metrics from the current period, plus the prior health review if one exists for trend comparison.

## Instructions

1. Pull the latest signal for each dimension — KPI health, delivery, incidents, customer feedback, churn, risks, strategic progress. Mark any dimension with no data this period explicitly as "no data," never silently skip it.
2. Score each dimension 🟢/🟡/🔴 based on trend and threshold, not just the current absolute value — a metric still "fine" but trending down 3 periods running is 🟡 at worst, not 🟢.
3. Cross-check dimensions against each other for hidden correlation (e.g. rising incidents correlating with a recent risky release) rather than treating them independently.
4. Compare against the prior review, if available, and call out any dimension whose status changed.
5. Summarize overall health in one paragraph, naming the 1-2 dimensions most needing attention.
6. Recommend concrete next actions tied to specific 🟡/🔴 dimensions, not generic "keep monitoring."

```markdown
# Product Health Review — <period>, <year>

## Overall Summary
[One paragraph naming the 1-2 dimensions most needing attention]

## Dimension Status
| Dimension | Status | Trend | Note |
|---|---|---|---|
| [e.g. Churn] | [🟢/🟡/🔴] | [↑/↓/flat over N periods] | [e.g. "up 0.5pp, correlates with billing incidents"] |

## Cross-Dimension Risks
- [e.g. "Rising incidents + rising churn this period — treat as one combined risk"]

## Recommended Actions
- [Tied to a specific 🟡/🔴 dimension]
```

A recurring 🔴 dimension tied to a specific decision point should get a formal decision memo; a single sharp incident deserves its own dedicated review rather than waiting for the next periodic rollup.

## Notes

- A dimension trending wrong for 2+ consecutive periods is never 🟢, even if its absolute value still looks acceptable.
- Two dimensions showing correlated degradation (e.g. incidents + churn both worsening) count as one combined risk, not two independent footnotes.
- If most dimensions have no data this period, say so plainly and recommend which data source to wire up next, rather than producing a thin report that looks complete.
