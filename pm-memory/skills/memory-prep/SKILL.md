---
name: memory-prep
description: "Read-only prep brief for a stakeholder or topic ahead of a meeting or task — last touchpoint, open asks, unresolved concerns, suggested questions, pulled from project memory. Use right before a 1:1, customer call, or meeting so nothing important gets forgotten."
---

# Memory Prep

## Purpose

You are preparing a read-only brief on $ARGUMENTS (a stakeholder or topic) so whoever is about to walk into a meeting or task has full continuity — what was last discussed, what's still open, what to ask — without re-reading everything themselves.

## Context

Run this immediately before a meeting, call, or task involving a specific person or topic. This skill never writes anything — it only reads. After the meeting happens, run `memory-ingest` on the notes/transcript to feed the loop forward.

## Instructions

1. **Read the relevant `stakeholders/<person>.md`** (or the relevant `knowledge/` area if the input is a topic rather than a person) — last touchpoint date, history of concerns, influence/friction notes.
2. **Read open items that reference this person/topic**: `decisions/` entries with status `pending`, `hypotheses/` with evidence rows tied to this person/topic.
3. **Compute staleness the same way `memory-review` does**: flag if the last touchpoint is old enough to be a cadence concern (e.g. 3+ weeks for a high-influence stakeholder) — use consistent thresholds so this skill and `memory-review` never disagree about what counts as stale.
4. **Surface the last unresolved concern** — the most recent open thread that never got closed, stated plainly, not buried among older resolved ones.
5. **Draft 2-4 suggested questions** for this session, grounded in what's actually open (a pending decision needing their input, a hypothesis needing their confirmation/denial, an old ask never followed up on) — not generic relationship-building questions.
6. **Remind the user this is prep, not a substitute for ingestion** — the meeting that's about to happen still needs its own `memory-ingest` pass afterward.

## Output

```
## Prep: [stakeholder name / topic]

**Last touchpoint**: [date] — [one-line summary] [cadence flag if stale]

**Open asks / unresolved concerns**:
- ...

**Relevant open decisions/hypotheses**:
- [decisions/hypotheses entries referencing this person/topic, with status]

**Suggested questions for this session**:
1. ...
```

Present this directly in chat — no file is created or edited by this skill.

## Notes

- This skill is read-only — if it finds itself wanting to update a file, that's `memory-ingest`'s job after the meeting, not this skill's job before it.
- If there's no history at all for this person/topic, say so plainly ("no prior touchpoints on file") rather than inventing plausible-sounding context.
- A stale cadence flag here should match what `memory-review`'s stakeholder-cadence check would also flag — don't silently use a different threshold.

## Example

Input: "Prep me for my call with the Acme Ops Lead." Output: Last touchpoint 2026-04-22 (18 days ago, not yet stale for a medium-influence stakeholder). Open concern: SOC2 evidence cadence preference for weekly batch, tied to Hypothesis H2 (confidence 0.7, decision trigger 80% met). Suggested question: "Since our last call, has the Friday-batch workflow held up, or has anything about your team's cadence changed?"
