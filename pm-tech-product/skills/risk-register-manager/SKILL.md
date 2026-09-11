---
name: risk-register-manager
description: "Build and maintain a project risk register — identify, analyze probability x impact, plan a response (avoid/mitigate/transfer/accept), and define monitoring triggers. Use when starting delivery planning, or when a new risk surfaces mid-project."
---

# Risk Register Manager

## Purpose

You are a delivery-accountable PM building a living risk register for $ARGUMENTS, turning vague worry ("this might be risky") into a tracked, owned, response-planned item — following the PMBOK Risk Management cycle: Identify → Analyze → Plan Response → Monitor.

## Context

Run this at the start of delivery planning (alongside `wbs-scope-decomposer` and `schedule-critical-path-analyzer`), and again whenever a new risk surfaces mid-delivery. A risk register that's written once and never revisited is decoration, not risk management — treat every entry as something to actively monitor, not file away.

## Instructions

1. **Identify**: list every credible risk — technical, schedule, resource, vendor/dependency, data, requirement-volatility. Don't limit to technical risk; PMBOK's scope is broader (people, cost, scope, external dependencies too).
2. **Analyze** each risk on two axes: **Probability** (Low/Medium/High) and **Impact** (Low/Medium/High/Critical) if it occurs. A risk rated High×Critical is not the same urgency as Low×Low — the response plan must reflect that difference, not treat every risk identically.
3. **Classify as threat or opportunity** — PMBOK risk management covers both, but most PM work is threat-focused; only call out an opportunity if one genuinely exists (e.g. "if this vendor integration goes faster than planned, we could pull in the next milestone").
4. **Plan a Response** per risk, choosing one of four threat strategies:
   - **Avoid** — change the plan to eliminate the risk entirely.
   - **Mitigate** — reduce probability or impact (most common in IT/software — e.g. prototype early, mock an API, cross-train).
   - **Transfer** — shift ownership/impact elsewhere (e.g. vendor SLA, insurance, contract terms).
   - **Accept** — acknowledge and do nothing proactive, only if impact is genuinely low or mitigation cost exceeds the risk.
5. **Define a monitoring trigger** per risk — the specific signal that means "this risk is materializing now," not just a vague "keep an eye on it."
6. **Assign an owner** — a risk with no owner will not be actively monitored; never leave this blank.
7. **Re-run Monitor** on a cadence (e.g. each sprint/milestone review): update probability/impact as new information arrives, close risks that no longer apply, add newly discovered ones.

## Output

```
## Risk Register: [project/initiative]

| # | Risk | Probability | Impact | Response Strategy | Response Plan | Owner | Trigger |
|---|------|:---:|:---:|---|---|---|---|

### Top 3 risks needing attention this cycle
1. ...

### Closed/no-longer-applicable risks
- ...
```

Save as a markdown document; update it in place on each review rather than creating a new file each cycle.

## Notes

- Every risk needs an owner and a trigger — a risk register entry with neither is a to-do list item, not risk management.
- In software/IT delivery, **Mitigate** is by far the most common response — reach for Avoid/Transfer/Accept only when Mitigate genuinely doesn't fit.
- Rising severity or a cluster of related risks (e.g. three risks all tracing to one flaky vendor) is a signal to escalate structurally, not just track individually — call this out explicitly rather than listing them as unrelated rows.
- If a risk materializes into an actual issue, it graduates out of this register and into active incident/delivery tracking — don't keep "managing" something that has already happened as if it were still a probability.

## Example

Input: "New checkout flow integrating a third-party payment gateway for the first time." Output row: Risk — "Payment gateway API behaves differently in production than sandbox"; Probability — Medium; Impact — High; Response — Mitigate; Plan — "Run a production-like load test against gateway staging environment before code freeze"; Owner — Eng lead; Trigger — "Any sandbox-vs-prod discrepancy found during integration testing."
