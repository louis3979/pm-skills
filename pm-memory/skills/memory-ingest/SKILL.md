---
name: memory-ingest
description: "Ingest a raw artifact (interview transcript, meeting notes, market signal, or ad-hoc note) into the project memory — copy it to source/, tag observations in ingestion/, and propagate to knowledge/hypotheses/stakeholders/decisions as warranted. Use whenever new PM-relevant input arrives that shouldn't be forgotten."
---

# Memory Ingest

## Purpose

You are processing $ARGUMENTS — a raw artifact just handed to you (an interview transcript, meeting notes, a market signal, or an ad-hoc note) — into the project's durable memory, so nothing said or observed gets lost between sessions.

## Context

This is the workhorse of the memory system. Run it every time new PM-relevant input arrives: after a customer call, after a meeting, when a competitor does something notable, or when a stray but important thought needs a home. It assumes `memory-init` has already scaffolded `source/`, `ingestion/`, `knowledge/`, `hypotheses/`, `decisions/`, and `stakeholders/` in this project.

## Instructions

1. **Detect the artifact's shape**: interview, meeting, market signal, or ad-hoc note — based on structure (speaker labels and Q&A read as interview; agenda/attendees read as meeting; external news/competitor content reads as market; anything else is ad-hoc).
2. **Copy verbatim into `source/<shape>/<yyyy-mm-dd>-<slug>.md`.** This copy is immutable — the audit anchor. Never edit it after creation.
3. **Create a synthesis record in `ingestion/<shape>/<yyyy-mm-dd>-<slug>.md`.** Walk the artifact and tag each notable line:
   - **observation** — a direct quote or factual claim from the source.
   - **interpretation** — your framing of what an observation means. Must link back to the observation(s) it's built on.
   - **hypothesis** — a testable belief this suggests. Must link back to the interpretation(s) behind it.
   - **assumption** — an implicit, unvalidated claim the artifact rests on but doesn't prove.
4. **Check the promotion threshold before writing to `knowledge/`.** An observation only gets promoted to a durable fact/pattern in `knowledge/` once independently corroborated (e.g. 3+ independent observations of the same pattern from different sources). If this is the first or second time you've seen it, note it as provisional in the ingestion record and say explicitly what's still missing for promotion — do not write it into `knowledge/` yet.
5. **Update `hypotheses/`** if this artifact bears on an existing hypothesis (add an evidence row, recompute confidence, show the old → new delta) or clearly suggests a new one (draft it via the same process as `memory-hypothesize`).
6. **Log a stakeholder touchpoint** in `stakeholders/<person>.md` if a named person was involved — date, artifact link, one-line summary of what's new (concern, ask, sentiment shift).
7. **Check whether any hypothesis's stated decision trigger just fired.** If so, draft a `pending` decision in `decisions/` per the `memory-decide` process — never mark it `decided` yourself.
8. **Close the loop**: report exactly what was touched. Never leave it ambiguous.

## Output

Files created/updated (not a single new standalone doc):
- `source/<shape>/<date>-<slug>.md` (new, immutable)
- `ingestion/<shape>/<date>-<slug>.md` (new, tagged synthesis)
- `knowledge/...` (updated only if promotion threshold met this round)
- `hypotheses/<topic>.md` (updated or created)
- `stakeholders/<person>.md` (touchpoint appended, if applicable)
- `decisions/<date>-<slug>.md` (new, status `pending`, only if a decision trigger fired)

Closing report format:
```
Resolved: [source copied], [ingestion record created], [insight promoted / not yet — needs X], [hypothesis strengthened Y→Z or created], [stakeholder touchpoint logged / n/a].

Drafted for your confirmation (if any): decisions/<file> — [why, what trigger fired].

Surfaced (if anything stale/notable came up while ingesting): ...
```

## Notes

- Never promote to `knowledge/` on a single observation — provisional notes stay in the ingestion record until corroborated.
- Every hypothesis/decision evidence row needs a provenance tag: a real path link, or an explicit non-path tag like `(stakeholder-verbal, <name>, <date>)`, `(intuition, PM, <date>)`, `(industry-knowledge)`, `(chat, no artifact)` — never imply a document exists when it doesn't.
- If nothing in the artifact is durable/notable, say so plainly rather than manufacturing a promotion or a hypothesis to look productive.
- No `git push` — local commits are fine if the project convention is to commit memory changes, but publication stays with the operator.

## Example

Input: a 45-minute customer interview transcript with an Ops Lead. Output: source copied to `source/interviews/2026-04-22-acme-ops.md`; ingestion record tags the quote "we batch our compliance reviews on Fridays" as an observation, links an interpretation ("mid-market ops leads may prefer batch over real-time"), and flags this as the 3rd independent observation of the same pattern — promoted to `knowledge/users.md` with links to all 3 sources; hypothesis H2 (real-time alerts may have negative value for this persona) strengthened 0.4 → 0.7 with the decision trigger noted as 80% met; stakeholder touchpoint logged in `stakeholders/acme-ops.md`.
