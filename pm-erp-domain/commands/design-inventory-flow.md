---
description: Design a complete inventory/stock-transfer flow — quantity logic, transfer lifecycle, and allocation rule — from a raw scenario
argument-hint: "<inventory or stock-transfer scenario>"
---

# /design-inventory-flow -- Inventory Flow Design

Turn a raw inventory or stock-transfer scenario into a complete, implementation-ready design: correct quantity logic, a full transfer lifecycle, and (if supply can fall short of demand) an explicit allocation rule.

## Invocation

```
/design-inventory-flow Stores request stock from the central warehouse; warehouse approves or rejects
/design-inventory-flow Warehouse-to-warehouse transfer for slow-moving SKUs
/design-inventory-flow [paste a rough inventory requirement]
```

## Workflow

### Step 1: Understand the Scenario

Ask if not already clear:
- Which two location types are transferring stock, and in which direction(s)?
- Is approval required, and by whom?
- Can demand exceed available supply for any SKU in scope?

### Step 2: Validate the Quantity Logic

Apply the **inventory-domain-expert** skill:

- Extract every stock-state bucket in play (on-hand, reserved, in-transit, damaged, etc.)
- Write the exact available-quantity formula and check it for double-counting or negative-quantity paths
- Confirm concurrency/locking is addressed for simultaneous requests against the same SKU

### Step 3: Design the Transfer Lifecycle

Apply the **stock-transfer-designer** skill:

- Walk Request → Approval → Allocation → Pick → Ship → Receive → Reconcile
- Design partial approval, partial receipt, over/short shipment, damage, and post-shipment cancellation explicitly

### Step 4: Design Allocation (if demand can exceed supply)

Apply the **allocation-rule-designer** skill:

- Choose and justify a strategy (FIFO, priority-tier, min/max, velocity-proportional, safety-stock-reserved)
- Define the exact allocation formula, tie-breaking rule, and the fate of unfulfilled demand

### Step 5: Consolidate the Design

```
## Inventory Flow Design: [scenario]

### Quantity Logic
[buckets, formula, transition table, negative-quantity findings]

### Transfer Lifecycle
[stage table: actor, data, next states, per stage]

### Allocation Rule (if applicable)
[strategy, formula, safety stock, override, unfulfilled-demand handling]

### Open Questions
[anything flagged as needing a business decision]
```

Save as markdown.

### Step 6: Offer Next Steps

- "Want me to **verify every transaction is traceable** with a transaction-record review?"
- "Should I **check cross-system consistency** (orders/payments/accounting) with an ERP consistency audit?"
- "Want me to **design the access-control rules** for this flow (RBAC, approvals, audit logging)?"
- "Should I look at the **procurement side** if this involves purchasing from a supplier, or the **retail/POS side** if stores are involved?"

## Notes

- Partial approval and partial receipt are the two most commonly under-specified parts of a transfer flow — always design them explicitly, never assume 100%-or-0%.
- If demand never exceeds supply for this scenario, skip Step 4 and say so rather than forcing an allocation rule nobody needs yet.
- Flag any negative-quantity or race-condition risk as a blocker, not a nice-to-have fix.
