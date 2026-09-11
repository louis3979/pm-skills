# Project Memory — Index

This is a markdown-native memory system for one product/initiative. It exists so nothing important depends on one person's recall or one chat session's context window.

## How it flows

```
source/        immutable raw artifacts (interview transcripts, meeting notes, market signals)
   ↓
ingestion/     synthesis records — each raw artifact tagged as observation / interpretation / hypothesis / assumption
   ↓
knowledge/     durable, promoted facts and patterns (strategy, product, users, market, org)
hypotheses/    unconfirmed beliefs, tracked with evidence and a confidence score
decisions/     audit-trailed choices — what was decided, why, what would reverse it
stakeholders/  per-person tracking — touchpoints, open asks, cadence
```

`rules/` holds the working conventions this memory system itself follows (evidence standards, prioritization approach, writing style). `maintenance/` holds the dated weekly-sweep reports that keep this system from rotting.

## Folder map

| Folder | Purpose |
|---|---|
| `knowledge/` | `strategy.md`, `product.md`, `users.md`, `market.md`, `org.md` — durable, current-best-understanding facts |
| `stakeholders/` | One file per person who matters to this initiative — see `_SCHEMA.md` |
| `hypotheses/` | Tracked beliefs with evidence and confidence — see `_SCHEMA.md` |
| `decisions/` | Audit-trailed decision log — see `_SCHEMA.md` |
| `source/` | Immutable copies of raw artifacts — never edited after creation |
| `ingestion/` | Tagged synthesis records, one per ingested artifact |
| `rules/` | Working conventions this system follows |
| `maintenance/` | Dated weekly-sweep reports |

## The six operations

| Command | What it does |
|---|---|
| `/ingest` | Classify and file a raw artifact; propagate to knowledge/hypotheses/stakeholders/decisions as warranted |
| `/prep <stakeholder or topic>` | Read-only pre-meeting brief: last touchpoint, open asks, suggested questions |
| `/review` | Weekly maintenance sweep — six checks, dated report |
| `/decide` | Formalize a decision with a full evidence trail |
| `/hypothesize` | Draft or update a tracked belief with evidence and confidence |
| `/risk-scan <feature>` | Five-area risk scan, drafting hypothesis stubs for uncovered areas |
| `/ideate <problem>` | Grounded solution directions from what's actually known |
| `/plan <objective>` | Six-block plan: known, assumed, who to ask, hypotheses to open, experiments, decision points |
| `/strategy-check <proposal>` | Check something against stated strategy, citing the specific clause |

See `CLAUDE.md` for the operating manual future sessions should read before acting on this memory system.
