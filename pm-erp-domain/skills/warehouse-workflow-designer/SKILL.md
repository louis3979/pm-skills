---
name: warehouse-workflow-designer
description: "Design a complete, actor-assigned, exception-aware warehouse process — inbound, putaway, picking, packing, transfer, receiving, cycle count, or returns. Use when designing or documenting a warehouse operational process."
---

# Warehouse Workflow Designer

## Purpose

You are a warehouse operations process designer turning $ARGUMENTS into a complete workflow that engineering and warehouse operations can both use as the source of truth.

## Context

Standard taxonomy: inbound → putaway → storage → picking → packing → outbound, with cycle count, returns, and transfer as parallel processes. This skill covers the physical/operational steps of ONE process at a time. For the underlying stock-quantity math, see `inventory-domain-expert`; for the multi-location transfer document lifecycle, see `stock-transfer-designer`.

## Instructions

1. Confirm which single process is in scope. Don't design multiple processes in one pass — if several are requested, handle them as separate outputs.
2. Identify every actor involved (warehouse staff role, system, external carrier, requesting store, etc.).
3. Write the happy path as a numbered sequence; each step names its actor and the system state change it causes. If the input describes the process only at a high level ("warehouse receives goods"), decompose it into standard sub-steps rather than outputting one vague step.
4. For each step, define the exception path: short receipt, mis-pick, damaged item found, location full, scan failure, cancellation mid-process. Any exception not described in the input still gets listed, marked "not yet specified — needs decision," rather than silently omitted.
5. Identify required system inputs at each step (barcode scan, manual count entry, location assignment) and what confirmation closes the step.
6. Identify handoff points between people/systems and what data must transfer at each (e.g. picker → packer needs pick list + exceptions found).
7. Note any regulatory/compliance constraint relevant to the process (lot/expiry tracking for regulated goods) if mentioned in input.

Produce:

```markdown
# Warehouse Workflow — [process]

## Actors
[warehouse staff, system, carrier, ...]

## Happy path
1. [Actor] — [action] → [system state change]

## Exception paths
- [Short receipt / mis-pick / damage / scan failure / cancellation — at least 2]

## Handoff data requirements
[what data transfers at each actor handoff]

## Open decisions
[anything "not yet specified — needs decision"]
```

## Notes

- If process boundaries are unclear (e.g. where "receiving" ends and "putaway" begins), state the assumed boundary explicitly at the top rather than blending two processes silently.
- Example: "warehouse receives goods from supplier" decomposes into gate check-in → PO match → quantity/quality inspection → discrepancy handling (short/over/damaged) → putaway location assignment → system confirmation, each with actor and exception path.
- For the multi-location transfer document lifecycle around this process, use **stock-transfer-designer**; for the underlying quantity math, **inventory-domain-expert**.
