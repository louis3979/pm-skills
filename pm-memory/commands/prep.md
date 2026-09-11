---
description: Read-only prep brief for a stakeholder or topic before a meeting or task
argument-hint: "<stakeholder name or topic>"
---

# /prep -- Memory Prep

Pull a read-only brief on a person or topic from project memory before you walk into a meeting — last touchpoint, open asks, and what to ask this time.

## Invocation

```
/prep acme-ops
/prep the Q3 pricing decision before tomorrow's leadership sync
/prep [stakeholder name] — 1:1 in 10 minutes
```

## Workflow

### Step 1: Pull the Brief

Apply the **memory-prep** skill:

- Read the relevant `stakeholders/`, `knowledge/`, open `decisions/` and `hypotheses/` entries
- Surface last touchpoint (with a staleness flag if relevant), open asks, unresolved concerns, and 2-4 suggested questions

### Step 2: Offer Next Steps

- "After this conversation, run `/ingest` on your notes so this stays current."
- If the stakeholder came up stale: "Want to flag this in the next `/review`?"

## Notes

- Read-only — this command never writes to memory. The write happens afterward via `/ingest`.
- If there's no history on file, it says so plainly rather than inventing context.
