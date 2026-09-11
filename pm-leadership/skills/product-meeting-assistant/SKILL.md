---
name: product-meeting-assistant
description: "Extract decisions, actions, owners, deadlines, risks, and open questions from a raw meeting transcript or notes, enforcing that discussion is not decision and a suggestion is not a commitment. Use right after a product, tech, leadership, or customer meeting — not for pre-meeting prep."
---

# Product Meeting Assistant

## Purpose

Prevent discussion from being mistaken for decisions, and suggestions from being mistaken for commitments, by extracting only what was actually confirmed in the transcript.

## Context

Operates directly on the provided transcript/notes; an attendee list with roles helps attribute ownership correctly if available.

## Instructions

1. Read the full transcript/notes once before extracting anything, to understand context and who has authority in the room.
2. Extract candidate Decisions: something is a Decision only if the transcript shows explicit confirmation ("let's go with X," "agreed," a stated approval) — not merely proposed or debated.
3. Extract candidate Actions: each needs an owner and, if stated, a deadline. If either is missing from the transcript, mark it "not stated" rather than guessing.
4. Extract Risks raised during discussion, even if unresolved.
5. Extract Open Questions: anything raised but not answered by meeting's end.
6. Re-scan every extracted Decision and Action specifically for two failure modes: a "decision" that was actually just a suggestion, and a "decision" discussed at length but never confirmed by someone with authority.

```markdown
# Meeting Notes — <meeting name>, <date>

## Decisions
| Decision | Confirmed by | Note |
|---|---|---|
| [e.g. "Default new field to zero"] | [Person with authority, from transcript] | ["revisit after launch"] |

## Actions
| Action | Owner | Deadline |
|---|---|---|
| [e.g. "Update onboarding copy"] | [Named owner, or "not stated — flagged"] | [Date, or "not stated"] |

## Risks Raised
- [Anything flagged as a concern, even if unresolved]

## Open Questions
- [Anything raised but not answered by meeting's end]
```

A Decision needing formal sign-off should be promoted to this plugin's `decision-memo`. Unresolved risks belong in a project risk log.

## Notes

- Disagreement or "let's think about it" in the transcript means it's NOT a Decision — file it under Open Questions no matter how much discussion it got.
- No clear owner in the transcript means leave the action explicitly unassigned — never infer an owner from role alone.
- If the same topic appears as both "decided" and later still debated, trust the later state — it was reopened.
