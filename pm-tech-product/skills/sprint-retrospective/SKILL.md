---
name: sprint-retrospective
description: "Run a lightweight, recurring sprint/iteration retrospective — what went well, what didn't, and specific owned action items for next sprint. Use at the end of every sprint/iteration, distinct from a one-time full project closure."
---

# Sprint Retrospective

## Purpose

You are facilitating a recurring retrospective for $ARGUMENTS (a just-completed sprint/iteration), turning a team's raw impressions into a short, honest record with action items that actually get followed up on next time — not a venting session with no output.

## Context

Run this at the end of every sprint/iteration — it's meant to be light and frequent. For a one-time, full project/initiative shutdown (acceptance, handover, outcome-vs-intent review), use `project-retrospective-closer` instead; that's a different, heavier operation for a different moment.

## Instructions

1. **Gather raw input**: what happened this sprint — completed/incomplete scope, any blockers hit, any process friction, any team wins worth naming specifically.
2. **Sort into Went Well / Didn't Go Well / Puzzling (mixed signal)** — don't force everything into a clean positive/negative binary; "puzzling" catches things worth discussing that aren't clearly either.
3. **Look at the previous retro's action items first**, before generating new ones — an action item that was never followed up on is a bigger problem than anything new this sprint; call that out explicitly if it happened.
4. **Generate action items from patterns, not every single complaint** — a specific one-off annoyance doesn't need a standing action item; a pattern that showed up 2+ times does.
5. **Every action item gets an owner and is small enough to actually happen next sprint** — a vague "communicate better" action item is worthless; "eng lead posts blocker status in #team channel by 11am daily" is usable.
6. **Keep it short** — this is meant to take 20-30 minutes, not become its own project.

## Output

```markdown
# Sprint Retro: [sprint identifier]

## Previous action items — follow-up
| Action item | Owner | Done? |
|---|---|---|

## Went Well
- ...

## Didn't Go Well
- ...

## Puzzling / Mixed Signal
- ...

## Action Items (this sprint)
| Action item | Owner | By when |
|---|---|---|
```

Save as a markdown document.

## Notes

- If the same issue appears in "Didn't Go Well" for 2-3 sprints running with no action item ever sticking, that's the most important finding in the whole retro — say so explicitly rather than quietly logging it again.
- Don't let this become a status report — it's about the team's working process, not a recap of what shipped (that's `status-report`/`project-metrics-tracker` territory).
- Psychological safety matters here: name patterns and process issues, not individual people, unless a specific named accountability was already agreed as fair game by the team.

## Example

Input: "Sprint 14 retro — API integration slipped, but the new PR review process worked well." Output: Went Well — "New PR review checklist caught 2 bugs before merge, team wants to keep it." Didn't Go Well — "Third sprint running where an external API dependency wasn't ready when we planned around it." Action item: "PM confirms external API readiness with vendor 3 days before sprint planning, not day-of — Owner: PM, by next sprint planning."
