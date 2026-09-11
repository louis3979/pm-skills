---
name: weekly-digest
description: "Roll up a personal weekly digest from scattered updates across every domain (strategy, delivery, data, stakeholder). Use when reviewing a week of work before planning the next one or sharing status upward — not for a single-topic executive summary."
---

# Weekly Digest

## Purpose

Turn a whole week's scattered activity into one compact digest, for personal review and/or sharing upward, covering every domain rather than one requested topic.

## Context

Pull from any outputs generated this week by other skills/tools (status reports, experiment readouts, decision memos) and, if it exists, last week's digest for continuity.

## Instructions

1. Bucket every input by domain (strategy, discovery, requirements, design, tech, delivery, analytics, growth, stakeholder, ops, and any domain-specific area like ERP). Skip domains with nothing to report — don't pad with a placeholder line.
2. Within each active domain, keep only what actually changed state (a decision made, a measured result, a new risk) — drop routine activity that didn't move anything.
3. Lead with the 3-5 most important points of the whole week, regardless of domain, before per-domain detail (Pyramid Principle: conclusion first).
4. Tag each item's status: 🟢 On track, 🟡 Needs attention, 🔴 Blocker/risk.
5. Give Blockers & Risks their own prominent section — don't bury them in domain detail.
6. Propose 3-5 priorities for next week based on what's unfinished or at risk.

```markdown
# Weekly Digest — Week <number>, <year>

## Highlights this week
1. [Decision/result that changed something, e.g. "Pricing experiment B beat control by 8%"]
2. [...]

## By domain
### 🟢/🟡/🔴 <domain with activity, e.g. Delivery>
- [One concrete line per item — a decision made, a number moved, a risk that appeared]

## Blockers & risks needing help
- [What's stuck, who/what could unstick it]

## Focus for next week
- [The 3-5 things that matter most]
```

If a blocker needs a formal decision, draft it with this plugin's `decision-memo`. If this digest is headed to leadership, consider condensing it further as a targeted executive update.

## Notes

- An item unresolved since last week's digest gets its status tag escalated (e.g. 🟡 → 🔴), not silently repeated.
- If the week is genuinely quiet, say "quiet week, nothing decision-worthy" rather than inflating routine work into false highlights.
