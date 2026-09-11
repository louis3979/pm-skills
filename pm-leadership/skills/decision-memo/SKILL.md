---
name: decision-memo
description: "Write a structured decision memo — context, options, trade-offs, recommendation, approver and deadline. Use when a bounded decision with multiple options needs sign-off from stakeholders — for a large ambiguous strategic bet needing a full narrative, use a heavier strategy-memo skill instead."
---

# Decision Memo

## Purpose

Force explicit comparison of real options and trade-offs so a decision gets approved (or challenged) on its merits, not on whoever spoke last.

## Context

Check for any past related decisions to avoid contradicting or repeating them.

## Instructions

1. State the context: what's forcing a decision now, and the cost of delaying it.
2. List every viable option, always including "keep the status quo" as a baseline.
3. Analyze each option against the same fixed criteria set (cost, time, risk, long-term impact) for a fair comparison.
4. State the real trade-off of each option explicitly — no option is free of downside; if one looks downside-free, dig deeper before finalizing.
5. Give one clear recommendation, not a menu for the reader to guess from, with the reasoning for why it beats the alternatives.
6. State who must approve, the deadline, and what happens by default if no response arrives.

```markdown
# Decision Memo — <decision name>

## Context
[What's forcing this decision now, and the cost of delaying it]

## Options
1. [Option A, including its underlying assumption]
2. [Option B]
3. [Do nothing / status quo — always included]

## Trade-off Comparison
| Criterion | Option A | Option B | Do nothing |
|---|---|---|---|
| Cost | | | |
| Time | | | |
| Risk | | | |
| Long-term impact | | | |

## Recommendation
[Clear stance, with the reasoning for why it beats the alternatives — not just a restatement of the table]

## Approver & Deadline
[Name/role, and the date a decision is needed by]
```

If the decision is large/strategic enough to need a full narrative and FAQ stress-test, escalate to a strategy-memo skill instead of finalizing here.

## Notes

- An option showing zero downside under every criterion signals the analysis is incomplete — dig for the hidden cost before finalizing.
- "Do nothing" must be in the option list — add it before proceeding if missing; it's the implicit baseline everything else is compared against.
- No named approver means the memo just becomes an unread document — stop and ask if authority is unclear.
