---
name: memory-decide
description: "Formalize a decision into the project memory with a full evidence trail and an explicit reversal condition, drafted as pending until the operator confirms it. Use when a hypothesis's decision trigger fires, or the operator explicitly needs to record a decision."
---

# Memory Decide

## Purpose

You are drafting a formal decision record for $ARGUMENTS into project memory, so that months later, "why did we decide this" has a two-click-deep answer instead of relying on someone's memory of a conversation.

## Context

Use this when a hypothesis's stated decision trigger fires (from `memory-ingest` or `memory-review` surfacing it), or when the operator explicitly wants a decision formally recorded. This always produces a `pending` draft — the operator, not the agent, confirms it.

## Instructions

1. **State what's being decided** concretely — not a vague direction, a specific choice ("ship weekly batch alerts only for v1; defer real-time to v2").
2. **State the driver**: which hypothesis, evidence, or event triggered this decision now — link directly to the hypothesis/ingestion chain.
3. **Assemble the full evidence trail**: every supporting data point, each with its provenance tag (a path link to `ingestion/`/`source/`, or an explicit non-path tag like `(stakeholder-verbal, ...)`, `(intuition, PM, ...)`, `(industry-knowledge)`, `(chat, no artifact)`). Don't cherry-pick only the supporting evidence — note any evidence that argues against the decision too, if it exists.
4. **State the reversal condition explicitly**: what would have to become true for this decision to be revisited — a decision with no stated reversal condition is a decision nobody can responsibly challenge later.
5. **Set status to `pending`** always. Present the draft to the operator and ask for explicit confirmation before it is ever treated as `decided`.
6. **Never self-confirm.** If the operator doesn't respond, the decision stays `pending` — do not assume silence means agreement.

## Output

Save/append to `decisions/<date>-<slug>.md`:

```markdown
# [Decision title]

**Status**: pending (drafted by agent, awaiting confirmation)
**Date**: [date]
**Driver**: [hypothesis/evidence/event that triggered this]

**What we're deciding**: [concrete statement]

**What would reverse this**: [explicit condition]

**Evidence trail**:
- [supporting evidence, with provenance tag/link]
- [evidence against, if any, with provenance tag/link]
```

## Notes

- Status is never anything but `pending` when this skill drafts it — confirmation is a separate, explicit operator action.
- A decision with no reversal condition is incomplete — always include one, even if it's a high bar ("revisit only if 2+ enterprise customers demonstrate intent-to-buy contingent on this").
- If the evidence is thinner than it should be for a decision this consequential, say so instead of dressing it up as more solid than it is.

## Example

Input: "Draft the decision to defer real-time alerts — H2 just crossed 0.7 confidence." Output: Status pending; Driver: "H2 confidence raised to 0.7, recurring pattern across 3 mid-market ops interviews"; Reversal condition: "2+ enterprise customers (team size >50) explicitly request real-time and show intent-to-buy contingent on it"; Evidence trail links to the 3 supporting interviews plus the hypothesis file.
