---
description: Set product strategy from company context, then sequence it into a roadmap and a prioritized near-term backlog
argument-hint: "<company/product context, or the strategic question to resolve>"
---

# /set-strategy -- Strategy to Roadmap Pass

Turn company context into a strategic direction, then sequence that direction into an executable roadmap and a prioritized near-term backlog — strategy that actually reaches the backlog, not a slide that stays in a deck.

## Invocation

```
/set-strategy B2B inventory SaaS expanding into mid-market retail, NPS declining among enterprise accounts
/set-strategy Should our product strategy change given the new competitor entering our core segment?
/set-strategy [paste company context: business model, segments, competitors, current metrics]
```

## Workflow

### Step 1: Gather Strategic Context

Ask if not already clear: business model, current product portfolio, customer segments, competitors, current metrics, company-level goals, and real constraints (budget, headcount, technical debt).

### Step 2: Set Strategy

Apply the **product-strategist** skill: strategic choices, strategic themes, North Star metric, recommended product bets, investment thesis, and named risks/assumptions.

### Step 3: Build the Roadmap

Apply the **roadmap-planner** skill: sequence the recommended bets into an outcome-oriented roadmap by period, checking capacity and dependencies, with confidence stated per period.

### Step 4: Prioritize the Near-term Backlog

Apply the **product-prioritizer** skill to rank the initiatives feeding the nearest roadmap period into Do Now / Do Next / Do Later / Don't Do.

### Step 5: Consolidate

```
## Strategy → Roadmap → Priorities: [product/team]

### Strategic Direction
[summary from product-strategist]

### Roadmap
[period-by-period outcomes and initiatives from roadmap-planner]

### Near-term Priorities
[Do Now / Do Next / Do Later / Don't Do from product-prioritizer]
```

Save as markdown.

### Step 6: Offer Next Steps

- "Want me to **evaluate a specific bet** in more depth (`product-bet-evaluator`)?"
- "Should I **draft the PRD** for the top Do Now item (`/write-prd`)?"
- "Want a **board-level summary** of this strategy (`board-update`)?"

## Notes

- If the strategic question is really about one specific decision already on the table (not setting overall direction), use `decision-memo` or `product-bet-evaluator` directly instead — this command is for setting/resetting direction, not for a single tactical call.
- A roadmap this command produces should always state confidence per period — don't present a far-out period with the same certainty as next quarter.
