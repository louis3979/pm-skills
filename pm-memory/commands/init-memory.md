---
description: Initialize a project memory system in the current directory — durable knowledge, decisions, hypotheses, and stakeholder tracking that survives context loss between sessions
argument-hint: "[optional: leave blank to use the current directory]"
---

# /init-memory -- Initialize Project Memory

Set up a markdown-native project memory in the current directory so knowledge, decisions, hypotheses, and stakeholder context survive between sessions instead of living only in chat history.

## Invocation

```
/init-memory
/init-memory set up a memory system for this product
```

## Workflow

### Step 1: Detect Mode

Apply the **memory-init** skill: inspect the current directory. Detect whether it's empty (greenfield), contains existing PM artifacts to migrate in, or is an active code repository (in which case, pause and confirm with the operator before proceeding — this should not silently scaffold into the middle of an unrelated working repo).

### Step 2: Scaffold and Seed

The skill copies the deterministic folder structure (`knowledge/`, `stakeholders/`, `hypotheses/`, `decisions/`, `rules/`, `source/`, `ingestion/`, `maintenance/`, plus `INDEX.md` and an operating `CLAUDE.md`) into the current directory, then runs a short interview to seed the initial content (strategy basics, known stakeholders, current roadmap state).

### Step 3: Self-Test and Commit

The skill verifies the scaffold is complete, checks internal links, and commits the result locally. It never pushes to a remote — publication stays in the operator's control.

### Step 4: Hand Off

Report what was built and the first 2-3 things worth doing next (e.g. ingest something today, prep for an upcoming meeting, schedule the first weekly `/review`).

## Notes

- This should only run once per project — re-running against an already-initialized memory risks overwriting content; if `knowledge/`/`decisions/`/`hypotheses/` already exist, confirm with the operator before touching anything.
- Never push the resulting commit to a remote automatically.
