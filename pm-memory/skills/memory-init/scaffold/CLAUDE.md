# Project Memory — Operating Manual

Read this before acting on this project's memory system (the `knowledge/`, `stakeholders/`, `hypotheses/`, `decisions/`, `source/`, `ingestion/`, `rules/`, `maintenance/` folders in this directory).

## What this is

A durable memory for one product/initiative, maintained across sessions. The point is continuity: what we know, what we believe but haven't confirmed, what we decided and why, and who needs what from us — none of it should depend on someone remembering it.

## Core discipline (non-negotiable)

1. **Provenance always.** Every claim in `knowledge/`, `hypotheses/`, or `decisions/` traces to either a real artifact (link into `ingestion/` or `source/`) or an honest non-path tag: `(stakeholder-verbal, <name>, <date>)`, `(intuition, PM, <date>)`, `(industry-knowledge)`, `(chat, no artifact)`. Never imply an artifact exists when it doesn't.
2. **Promotion has a bar.** Don't move something from `ingestion/` into `knowledge/` as established fact on a single data point — flag it as provisional until the promotion threshold is met (default: 3+ independent corroborating observations; adjust in `rules/`).
3. **Decisions are drafted, not self-confirmed.** Any decision this system drafts is `pending` until the operator explicitly confirms it. Never mark a decision `decided` unprompted.
4. **`source/` is immutable.** Once a raw artifact is copied in, it is never edited. Corrections happen in `ingestion/` or `knowledge/`, with a note explaining the correction.
5. **Say when you find nothing.** A review with no stale items, an ingestion with no new hypothesis, an ideation with no strong direction — say so plainly. Fabricating findings to look thorough is worse than an honest "nothing new here."
6. **Compression is additive.** When `/review` consolidates recurring patterns, it preserves minority/dissenting signal rather than quietly deleting it. State what was merged and why.
7. **This system supports judgment, it doesn't replace it.** Analyze, surface tensions, recommend — the operator decides and owns the outcome.
8. **Never push this repo remotely** from within a memory operation. Local commits are fine; publication is the operator's call.

## Operating preferences

<!-- Filled in during /init-memory from the interview. If blank, ask before assuming. -->

- **Autonomy mode**: [how much should the agent draft vs. ask before writing — e.g. "draft freely in ingestion/, ask before touching decisions/"]
- **Maintenance cadence**: [default: weekly, adjust if stated otherwise]

## Off-limits

<!-- Filled in during /init-memory. Topics or files the operator does not want the agent writing to autonomously. -->

-

## When you're not sure

If a raw artifact doesn't clearly fit `source/interviews`, `source/meetings`, `source/market`, or `source/adhoc`, ask rather than guessing a shape. If a claim's evidence tier is ambiguous, under-claim rather than over-claim.
