---
name: memory-plan
description: "Draft a six-block plan for an objective — what we know, assumption vs. evidence, who to talk to, hypotheses to open, experiments needed, and explicit decision points. Use when an objective is set and needs a structured path forward, not just a to-do list."
---

# Memory Plan

## Purpose

You are drafting a structured plan for $ARGUMENTS that separates what's actually known from what's assumed, and names the real decision points ahead — instead of a flat task list that hides how much of the plan rests on unvalidated ground.

## Context

Use this once an objective is set (from `memory-strategy-check`, `memory-ideate`, or a direct ask) and needs a path forward. This produces a plan, not a decision — real decision points inside the plan get routed to `memory-decide` when they're reached.

## Instructions

Produce exactly six blocks, in order:

1. **What we already know** — pull directly from `knowledge/` relevant to this objective; cite sources.
2. **Assumption vs. evidence** — for the core premises this objective rests on, split them explicitly: which are backed by real evidence (cite it) and which are assumed but unverified. An objective built on more assumption than evidence should say so plainly, not bury it.
3. **Who to talk to** — pull from `stakeholders/` for people already tracked who are relevant, plus name any new research targets not yet in memory.
4. **Hypotheses to open** — which existing `hypotheses/` this plan should test, and which new ones should be opened (hand off to `memory-hypothesize` for the actual drafting).
5. **Experiments / validation steps needed** — concrete, not vague ("run a test") — what specifically would be measured and how.
6. **Decision points** — where in this plan an actual decision will need to be made, and what would trigger it (feeds `memory-decide` when reached). A plan with no named decision point is incomplete — there's always at least one moment where the path forks based on what's learned.

## Output

```markdown
## Plan: [objective]

### 1. What we know
- ...

### 2. Assumption vs. evidence
| Premise | Evidence-backed? | Source / basis |
|---|---|---|

### 3. Who to talk to
- ...

### 4. Hypotheses to open
- ...

### 5. Experiments / validation steps
- ...

### 6. Decision points
- [decision point] — trigger: [...]
```

Save as a markdown document.

## Notes

- All six blocks are required — a five-block plan missing "decision points" is exactly the kind of plan that quietly drifts without anyone noticing a fork was reached.
- If most premises in block 2 turn out to be assumption rather than evidence, say that plainly as a risk of the plan itself, not just a neutral table.
- This skill drafts the plan; it does not execute experiments or make decisions — those are separate steps/skills.

## Example

Input: "Plan to reduce mid-market churn." Block 2 (excerpt): "Premise: churn is driven by onboarding friction — Evidence-backed: partial (2 exit interviews cite this, but exit-interview sample is small and self-selected) — flagged as needing a larger data pull before treating as established."
