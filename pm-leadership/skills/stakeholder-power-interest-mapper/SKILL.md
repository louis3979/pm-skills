---
name: stakeholder-power-interest-mapper
description: "Map stakeholders onto a Power x Interest grid (Manage Closely / Keep Satisfied / Keep Informed / Monitor) and define an engagement approach per quadrant. Use when kicking off an initiative with multiple stakeholders and you need a deliberate engagement plan, not ad hoc updates."
---

# Stakeholder Power / Interest Mapper

## Purpose

You are a Head of Product mapping the stakeholder landscape for $ARGUMENTS onto the classic PMBOK Power × Interest grid, so engagement effort is spent deliberately — heaviest on the stakeholders who can actually block or accelerate the work, not just the ones who ask the most questions.

## Context

Use this when kicking off an initiative with more than a couple of stakeholders (cross-functional launches, anything touching leadership/board/external partners), before communication norms get set ad hoc and inconsistently.

## Instructions

1. **List every stakeholder** with a real stake in the outcome — internal (leadership, engineering, sales, support) and external (customers, partners, vendors, regulators if relevant). Don't limit the list to people already in the room.
2. **Rate Power** (Low/High): can this person/group meaningfully block, approve, or reallocate resources for this initiative?
3. **Rate Interest** (Low/High): how much do they actually care about this specific initiative's outcome, distinct from their general power?
4. **Place each stakeholder in a quadrant**:
   - **High Power / High Interest → Manage Closely**: frequent, direct engagement; involve in key decisions.
   - **High Power / Low Interest → Keep Satisfied**: enough visibility that they stay comfortable, without overloading them with detail they don't want.
   - **Low Power / High Interest → Keep Informed**: regular updates and a channel for their feedback, even though they can't unilaterally change direction.
   - **Low Power / Low Interest → Monitor**: minimal effort, light-touch awareness only.
5. **Define the concrete engagement approach per quadrant** — cadence, format, and who owns the relationship — not just the label. "Manage Closely" without a stated cadence/format isn't actionable.
6. **Flag any stakeholder whose power or interest is likely to change** (e.g. a quiet exec who'll suddenly care once this becomes visible externally) — plan for the shift now rather than being surprised later.
7. **Revisit periodically** — power and interest shift as an initiative progresses (a "Monitor" stakeholder can become "Manage Closely" once something affects them directly); don't treat the map as fixed at kickoff.

## Output

```
## Stakeholder Map: [initiative]

### Grid
| Stakeholder | Power | Interest | Quadrant | Engagement Approach | Owner |
|---|---|---|---|---|---|

### Stakeholders likely to shift quadrant
- [who, why, when to re-map]

### This period's engagement actions
- ...
```

Save as a markdown document; revisit and update rather than re-creating from scratch each time.

## Notes

- "Manage Closely" stakeholders get proactive engagement before they ask — reactive-only engagement with a high-power/high-interest stakeholder is a common way initiatives get blocked late.
- Don't conflate organizational seniority with power over this specific initiative — a senior exec with no real stake here may genuinely be "Monitor."
- If in doubt about someone's quadrant, err toward more engagement, not less — under-engaging a high-power stakeholder is the costlier mistake.

## Example
Input: "Launching a new billing system affecting Finance, Support, Engineering, and a subset of enterprise customers." Output row: Stakeholder — Finance Director; Power — High; Interest — High; Quadrant — Manage Closely; Approach — "Biweekly working session + direct Slack channel, involved in every scope trade-off decision"; Owner — Head of Product.
