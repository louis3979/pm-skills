---
name: allocation-rule-designer
description: "Design the rule that decides who gets how much when stock demand exceeds available supply — FIFO, priority store, min/max stock, sales velocity, safety stock, or manual override. Use when multiple requesters compete for the same limited stock."
---

# Allocation Rule Designer

## Purpose

You are an inventory allocation policy designer turning $ARGUMENTS into an explicit, defensible rule for splitting scarce stock — instead of an implicit first-come-first-served default nobody actually decided on.

## Context

Candidate strategies: FIFO (first request first served), priority-tier (designated stores/customers first), min/max stock (top up each location to its target band), sales-velocity-proportional, safety-stock-reserved, manual override. This skill designs the *decision rule* only — for the transfer document lifecycle itself, see `stock-transfer-designer`.

## Instructions

1. Confirm the scarcity scenario: what triggers allocation (total requested > available stock at decision time).
2. List candidate strategies from the frameworks above and eliminate ones that clearly don't fit this business, stating why.
3. For the 1-2 strategies that remain, define the exact computation: given available qty and a list of requests (with priority/velocity/min-max data), what quantity does each requester receive. If the business has designated "priority" locations (flagship, high-revenue), default to priority-tier as primary with sales-velocity as the tiebreaker within a tier, unless told otherwise.
4. Define the safety-stock carve-out if applicable: a reserved buffer never allocated away, and what draws it down (emergency override only).
5. Define the manual override path: who can override, and require a reason code — overrides without a logged reason are a common source of later disputes.
6. Define tie-breaking rules for when the primary strategy still produces a tie.
7. Define the fate of unfulfilled demand after allocation: rollover, expire, or require re-request — never leave it implicit.

Produce:

```markdown
# Allocation Rule — [scope]

## Scarcity scenario
[what triggers allocation]

## Chosen strategy & why
[e.g. "priority-tier, because flagship stores are contractually guaranteed stock"]

## Allocation formula
[the exact computation, worked with numbers]

## Safety stock handling
[reserved buffer, what draws it down]

## Manual override rules
[who, and the mandatory reason code]

## Unfulfilled demand handling
[rollover / expire / re-request]
```

## Notes

- If no scarcity scenario actually exists (supply always meets demand), say so and recommend skipping formal allocation rules until scarcity is observed.
- Example: central warehouse has 80 units, 3 stores requested 40 each → priority-tier caps the flagship store at its full 40; the remaining 40 splits proportional to the other two stores' trailing-30-day velocity, fractional units rounded down with the remainder to the higher-velocity store as tiebreak.
- Feed the chosen strategy into **stock-transfer-designer**'s Allocation stage, and confirm the underlying quantity math with **inventory-domain-expert**.
