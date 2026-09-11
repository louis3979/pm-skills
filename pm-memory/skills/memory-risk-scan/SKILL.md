---
name: memory-risk-scan
description: "Run a 5-area risk scan (value, usability, feasibility, viability, ethical/compliance) for a feature or initiative against the project memory, drafting hypothesis stubs for any uncovered area. Use before committing real effort to a feature/initiative, or when asked to sanity-check one."
---

# Memory Risk Scan

## Purpose

You are risk-scanning $ARGUMENTS against the operator's project memory, so a real risk gets named before it becomes an expensive surprise — not a generic checklist run in a vacuum, but one grounded in what this specific memory system already knows (or doesn't).

## Context

Use this before committing meaningful effort to a feature/initiative, or whenever asked to sanity-check one. It reads the existing `knowledge/`, `hypotheses/`, and `decisions/` folders rather than starting from a blank slate — if those folders don't exist yet, tell the operator to run `/init-memory` first.

## Instructions

1. **Load existing context**: search `knowledge/`, `hypotheses/`, and `decisions/` for anything already touching this feature/initiative — prior insights, open hypotheses, related past decisions.
2. **Run the 5-area scan**:
   - **Value risk** — will the target users actually want/use this?
   - **Usability risk** — can users figure out how to use it without friction?
   - **Feasibility risk** — can engineering build it within realistic time/cost?
   - **Viability risk** — does it work for the business (revenue, cost, strategic fit)?
   - **Ethical/compliance risk** — any regulatory, privacy, or fairness concern, if relevant to this product.
3. **For each area, classify**: Evidenced (cite the specific `knowledge/`/`hypotheses/` source), Partially evidenced (some signal, not enough to be confident), or Uncovered (nothing in memory addresses this at all).
4. **Draft a hypothesis stub for every Uncovered area** — write it into `hypotheses/` with status `proposed`, confidence left unset, and a clear statement of what evidence would resolve it. An uncovered risk area is itself a finding — never silently skip it because there's "nothing to report."
5. **Never fabricate coverage** — if memory genuinely has nothing on an area, say "uncovered," don't stretch a loosely related insight to make it look evidenced.
6. **Prioritize the findings**: which uncovered/partially-evidenced area is the biggest threat to this specific initiative, not just a flat list.

## Output

```markdown
## Risk Scan: [feature/initiative]

| Risk Area | Status | Evidence / Gap |
|---|---|---|
| Value | Evidenced / Partial / Uncovered | [cite source, or "nothing in memory"] |
| Usability | ... | ... |
| Feasibility | ... | ... |
| Viability | ... | ... |
| Ethical/Compliance | ... | ... |

### Hypothesis stubs drafted (for Uncovered areas)
- `hypotheses/[slug].md` — [area] — what would resolve it: [...]

### Biggest threat right now
[one paragraph, naming the specific area and why]
```

Save the scan summary to `maintenance/log/` or hand it directly back in the response — write hypothesis stubs into `hypotheses/` regardless.

## Notes

- Every "Uncovered" area gets a hypothesis stub — this is the whole point of the scan, not an optional extra step.
- Don't inflate a single anecdote into "Evidenced" — that's exactly the kind of thin-evidence overconfidence this system exists to prevent.
- If `knowledge/`/`hypotheses/`/`decisions/` don't exist, this skill can't run meaningfully — direct the operator to `/init-memory` first.

## Example

Input: "Automated inventory reordering." Scan finds Value evidenced (3 interview quotes in `knowledge/users.md`... equivalent), Feasibility partial (one past decision noted eng concern but no follow-up), Viability and Ethical/Compliance both Uncovered. Output drafts `hypotheses/reordering-viability.md` and `hypotheses/reordering-compliance.md` as proposed stubs, and flags Viability as the biggest current threat since no one has checked unit economics.
