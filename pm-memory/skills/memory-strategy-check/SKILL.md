---
name: memory-strategy-check
description: "Check a proposal, decision, or initiative against the project's stated strategy — citing the specific clause it serves, contradicts, or falls outside of. Use to catch strategic drift before it compounds, not as a rubber stamp."
---

# Memory Strategy Check

## Purpose

You are checking $ARGUMENTS against the operator's stated strategy in memory, to catch drift while it's still one decision instead of a pattern — citing the actual clause being served or contradicted, not issuing a vague thumbs up/down.

## Context

Use this on a proposal, a decision already drafted (from `memory-decide`), or an initiative being considered — any time alignment with strategy needs an explicit, checkable answer rather than a gut feel. Requires `knowledge/strategy.md`-equivalent content to exist; if it doesn't, tell the operator to establish strategy content first (via `/init-memory` or by adding it directly).

## Instructions

1. **Load the stated strategy**: priorities, themes, and — importantly — stated non-goals, from the knowledge layer.
2. **Check the input against each relevant clause explicitly**: does it serve a stated priority (cite which one), contradict a stated non-goal (cite which one), or fall into a gray zone the strategy simply doesn't address?
3. **Never give a vague verdict** — "seems fine" is not acceptable; the output must name the specific clause(s) checked and the specific relationship (serves / contradicts / not addressed).
4. **If a real tension exists**, name it plainly, including if it's between this input and a *recent decision* rather than the strategy document itself (decisions can drift from strategy over time even when each one seemed reasonable individually) — don't soften a genuine finding to avoid friction.
5. **If nothing is addressed by current strategy at all**, say so and flag it as a strategy-gap worth raising, not a failure of this check.
6. **Distinguish a hard contradiction from a mere gray-zone case** — a gray zone isn't automatically a problem, but it should be named so the operator can decide whether strategy needs updating.

## Output

```markdown
## Strategy Check: [proposal/decision/initiative]

### Clauses checked
| Strategy clause | Relationship | Detail |
|---|---|---|
| [cited clause] | Serves / Contradicts / Not addressed | ... |

### Verdict
[Aligned / Tension found / Gray zone — strategy silent]

### If tension found
[specific description of the drift, including whether it echoes a pattern across recent decisions]

### Recommendation
[proceed / revise / escalate for a strategy update]
```

Save as a markdown document, or return directly for a quick pre-decision check.

## Notes

- Every check must cite specific clauses — a check with no citations is not a strategy check, it's an opinion.
- A pattern of individually-reasonable decisions that collectively drift from strategy is a real finding — actively look for it across recent `decisions/`, not just the single input in front of you.
- If strategy content doesn't exist yet in memory, say so and stop rather than inventing a plausible-sounding strategy to check against.

## Example

Input: "Proposal to build a white-label version of the product for a reseller partner." Strategy check finds: contradicts stated non-goal "we will not build white-label/reseller variants" (cited from strategy). Verdict: Tension found. Recommendation: escalate for explicit strategy re-confirmation before proceeding, since this isn't a gray zone — it's a direct stated non-goal.
