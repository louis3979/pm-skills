---
name: roadmap-planner
description: "Build an outcome-oriented roadmap from company OKRs, product bets, backlog, engineering capacity, and dependencies — organized by target outcome per period, not just a list of features and dates. Use when sequencing strategic bets into a plan the team can execute against."
---

# Roadmap Planner

## Purpose

You are turning approved strategic bets in $ARGUMENTS into a sequenced roadmap organized around outcomes, so the roadmap answers "what result are we going for" per period, not just "what ships when."

## Context

Use this after strategy/bets are set (`product-strategist`, `product-bet-evaluator`) and prioritized (`product-prioritizer`), when it's time to sequence them against real capacity and dependencies into a plan the team will actually execute.

## Instructions

1. **Gather Inputs**: company OKRs for the period, the approved product bets, the prioritized backlog, real engineering capacity, and known dependencies (technical, cross-team, vendor).
2. **Organize by Outcome, not just feature list**: each roadmap period should state the target outcome and measurable target first, with initiatives listed as how that outcome will be pursued — a roadmap that's just a feature list with dates invites "did we ship it" thinking instead of "did it work."
3. **Sequence Initiatives** against real dependencies — don't place an initiative in an early period if it depends on something scheduled later.
4. **Check capacity fit per period**: does the initiative list for each period actually fit the team's real capacity, accounting for other known commitments (support, tech debt, on-call)?
5. **Flag cross-team and external dependencies explicitly** per initiative — a roadmap that hides a dependency on another team's unscheduled work will slip silently.
6. **State confidence per period**: near-term periods should be higher-confidence/more concrete; far-out periods can be more directional — don't present a 4-quarters-out period with the same false precision as next quarter.
7. **Name what's explicitly NOT on the roadmap** this cycle, so stakeholders don't assume omission means "forgotten" rather than "deliberately deprioritized."

## Output

```markdown
# Roadmap: [product/team], [period range]

## Q[N] [Year]
**Outcome**: [target outcome]
**Target**: [measurable target]
**Initiatives**:
- [initiative] — depends on: [...] — confidence: [High/Medium/Low]

## Q[N+1] [Year]
...

## Explicitly not on this roadmap (this cycle)
- [item] — reason

## Cross-team / external dependencies to track
- ...
```

Save as a markdown document.

## Notes

- Every period needs a stated outcome and target, not just an initiative list — if you can't state the target, the initiative isn't ready for the roadmap yet.
- Confidence should visibly decrease the further out a period is — a roadmap that's equally confident 4 quarters out as next quarter is overclaiming certainty.
- If capacity doesn't fit the desired initiative list for a period, cut initiatives or push them out — don't silently overcommit the team on paper.

## Example

Input: "Q1 2027 roadmap for inventory accuracy improvements." Output: Outcome — "Improve Inventory Accuracy"; Target — "Inventory variance < 1%"; Initiatives — stock reconciliation (no dependency, High confidence), audit workflow (depends on RBAC work landing first, Medium confidence), barcode improvements (depends on hardware vendor timeline, Low confidence — flagged as external dependency to track).
