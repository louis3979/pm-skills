---
name: memory-hypothesize
description: "Draft a new hypothesis or update an existing one in project memory — evidence for/against, a confidence score, and an explicit decision trigger. Use when a pattern is worth tracking as a testable belief, or new evidence should update one already tracked."
---

# Memory Hypothesize

## Purpose

You are drafting or updating a hypothesis about $ARGUMENTS in project memory — turning a hunch or pattern into a tracked, evidence-scored belief with a stated condition for when it becomes a decision, instead of a vague feeling that never gets resolved either way.

## Context

Use this standalone when a pattern is worth tracking on its own, or as part of `memory-ingest`'s flow when a new artifact bears on an existing hypothesis. Every hypothesis here eventually resolves into a `memory-decide` action (once its trigger fires) or gets explicitly retired if evidence stops supporting it.

## Instructions

1. **Check if a hypothesis on this topic already exists** in `hypotheses/` before creating a new one — update in place rather than duplicating.
2. **New hypothesis**: assign a topic file + numbered ID, write a clear, falsifiable statement (not "users might like X" but "user segment Y will do Z under condition W"), set an initial confidence (0-1) justified by whatever evidence already exists, and state an explicit **decision trigger** — the condition that would convert this from a tracked belief into a formal decision.
3. **Update existing hypothesis**: add the new evidence row (with a provenance tag per the shared vocabulary), recompute confidence, and show the delta explicitly (old → new) — never silently overwrite the number with no visible reasoning trail.
4. **Weigh evidence independence**, not just count: three data points from the same single customer are weaker support than three from different customers — say so if evidence isn't actually independent yet.
5. **Check the decision trigger after every update**: if new evidence just crossed the stated threshold, flag it clearly and point to `memory-decide` — don't let a crossed trigger sit unnoticed.
6. **If evidence has been trending against the hypothesis**, say so and consider whether it should be weakened or retired rather than only ever adding supporting rows.

## Output

Append/update in `hypotheses/<topic-file>.md`:

```markdown
## H[N]. [Hypothesis statement]

**Confidence**: [old →] [new] ([reasoning for the number])

**Evidence for**:
- [evidence, with provenance tag/link]

**Evidence against** (if any):
- [evidence, with provenance tag/link]

**Decision trigger**: [explicit condition that would convert this to a decision]
**Trigger status**: [not yet met / X% met / met — see memory-decide]
```

## Notes

- A hypothesis without a stated decision trigger isn't finished — it will just sit forever with no path to resolution.
- Confidence changes always show their reasoning (what new evidence, how independent) — a bare number with no trail isn't trustworthy.
- If a decision trigger has been met, say so explicitly and point to `memory-decide` rather than letting it pass silently.

## Example

Input: "New interview supports the idea that ops leads prefer weekly batch over real-time alerts — update H2." Output: H2 confidence 0.4 → 0.7, evidence row added linking the new interview, trigger status updated to "80% met (need 5 independent observations at >0.8 confidence; currently 3 observations at 0.7)."
