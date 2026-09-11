---
name: memory-review
description: "Run the weekly maintenance sweep across project memory — stale knowledge, stale evidence, hypothesis hygiene, stakeholder cadence, knowledge compression, and archival — producing one dated report. Use on a regular cadence (e.g. Friday afternoon); memory systems rot without this."
---

# Memory Review

## Purpose

You are running the periodic maintenance sweep over the project's memory for $ARGUMENTS (or the whole memory if no focus area given), because a memory system nobody sweeps quietly rots — stale facts get trusted, hypotheses never resolve, and stakeholders get silently neglected.

## Context

Run this on a regular cadence (weekly is typical). This is the single most important recurring operation in the system — skipping it for a month is how the memory stops being trustworthy. Complements `memory-ingest` (adds new material) and `memory-decide`/`memory-hypothesize` (act on findings this sweep surfaces).

## Instructions

Run all six checks in order, even if a focus area was given — narrow the depth, not the coverage, unless explicitly asked to skip checks:

1. **Stale knowledge**: any `knowledge/` file untouched in 6+ weeks — still true, or ready to archive?
2. **Stale evidence**: market intel older than 30-60 days, interviews older than 90 days, stakeholder-touchpoint-based assumptions older than 30 days, strategy-level assumptions older than a quarter. Flag these — do not auto-decay or silently delete them.
3. **Hypothesis hygiene**: hypotheses with no new evidence in 30+ days (stalled); hypotheses whose confidence and trigger conditions suggest they should already have become a decision but haven't; `pending` decisions older than 14 days that carry real impact (escalate, don't let them rot in limbo).
4. **Stakeholder cadence + strategy tension**: high-influence stakeholders untouched in 3+ weeks (same threshold `memory-prep` uses); any recent decision that appears to diverge from stated strategy — flag it for a `memory-strategy-check` pass rather than resolving the tension here.
5. **Knowledge compression**: the highest-leverage check. Find recurring patterns worth consolidating into one clearer `knowledge/` entry, AND recurring contradictions worth surfacing rather than silently averaging away. Compression is additive — state exactly what's being merged and why; never destroy a minority/dissenting signal in the process.
6. **Archival sweep**: shipped features, resolved hypotheses, and closed asks inactive 90+ days. Before archiving anything, extract the durable lesson so it isn't lost with the archived material.

For every check: if it finds nothing, say so plainly. Never pad the report with manufactured findings to look thorough.

## Output

```
## Memory Review — [date]

### 1. Stale Knowledge
- [file] — untouched since [date]. Still true? / Recommend archive.
(or: "Nothing stale this cycle.")

### 2. Stale Evidence
- ...

### 3. Hypothesis Hygiene
- ...

### 4. Stakeholder Cadence & Strategy Tension
- ...

### 5. Knowledge Compression
- Consolidating: [files/entries] → [new consolidated entry], because [reason]
- Contradiction surfaced: [what conflicts, both sides preserved]

### 6. Archival
- Archived: [item] — durable lesson extracted: [lesson]

### Priority actions this week
1. ...
```

Save as `maintenance/<date>-review.md`.

## Notes

- A clean check ("nothing stale") is a legitimate, valuable result — report it as such, don't invent filler.
- Compression must never quietly delete a dissenting data point — say explicitly what's being preserved alongside what's being merged.
- Strategy tensions found here get flagged, not resolved — hand off to `memory-strategy-check` for the actual resolution.
- This sweep should take about 20 minutes of the operator's attention; keep the report scannable, lead with priority actions, not a wall of six equally-weighted sections.

## Example

Input: "/review" (no focus area). Output (excerpt): "3. Hypothesis Hygiene — H4 (feasibility risk on the alert pipeline) has had no new evidence in 34 days; recommend a feasibility check before it's used to justify deferring further work. 5. Knowledge Compression — three separate `knowledge/users.md` entries all describe the same 'ops leads prefer weekly batch' pattern from different interviews; consolidating into one entry with all three sources linked, no dissent found to preserve."
