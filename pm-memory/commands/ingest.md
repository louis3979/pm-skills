---
description: Ingest a raw artifact (interview, meeting notes, market signal, ad-hoc note) into project memory
argument-hint: "<paste the transcript/notes, or describe the signal>"
---

# /ingest -- Memory Ingest

Turn a raw artifact into durable project memory — tagged observations, promoted insights, updated hypotheses, stakeholder touchpoints, and drafted decisions where warranted.

## Invocation

```
/ingest [paste a customer interview transcript]
/ingest Meeting notes from today's eng sync — API rate limit concerns raised
/ingest Competitor X just launched a real-time alerting feature
```

## Workflow

### Step 1: Ingest

Apply the **memory-ingest** skill:

- Detect artifact shape (interview / meeting / market signal / ad-hoc), copy verbatim to `source/`, create the tagged synthesis record in `ingestion/`
- Propagate to `knowledge/` (only if promotion threshold met), `hypotheses/` (new or strengthened), `stakeholders/` (touchpoint logged), `decisions/` (drafted `pending` only if a trigger fired)

### Step 2: Close the Loop

Report exactly what was touched, per the **memory-ingest** skill's closing-report format — never leave it ambiguous what happened.

### Step 3: Offer Next Steps

- If a decision trigger fired: "Want me to formalize this as a decision (`/decide`)?"
- If it's been a while since the last sweep: "It's been [N] days since the last `/review` — want to run one?"
- "Prepping for a related conversation soon? Run `/prep <name>` first next time."

## Notes

- This is the workhorse command — run it every time new PM-relevant input arrives, not just for big events.
- Never let ingestion silently promote a single data point to `knowledge/` — the skill flags provisional findings explicitly.
