---
description: Audit a feature or flow for cross-system data consistency risk across inventory, orders, payments, and accounting
argument-hint: "<feature or flow to audit>"
---

# /audit-erp-consistency -- ERP Consistency Audit

Check a feature or flow for the class of bug that generic testing misses: two systems (or two views of the same event) quietly drifting apart. Produces one consolidated consistency-risk report.

## Invocation

```
/audit-erp-consistency Order-to-payment flow for the new checkout redesign
/audit-erp-consistency Inventory adjustments made from the mobile warehouse app
/audit-erp-consistency [paste a PRD or system design]
```

## Workflow

### Step 1: Scope the Audit

Ask if not already clear:
- Which domains does this feature touch: inventory, orders, transfers, payments, accounting, reports?
- Is this a design review (nothing built yet) or an investigation of an observed discrepancy?

### Step 2: Check Design-Time Consistency

Apply the **data-consistency-reviewer** skill:

- Map each domain to its single source of truth
- Check idempotency on every write, and locking/conflict strategy on every shared entity
- Trace one end-to-end example through all layers

### Step 3: Check the Financial Chain

Apply the **financial-transaction-consistency-reviewer** skill (skip if the feature has no financial layer):

- Map Business Document → Operational Transaction → Financial Transaction → Accounting Entry
- Check atomicity of every transition and idempotency of every retryable financial operation

### Step 4: Design the Safety Net

Apply the **reconciliation-designer** skill:

- Define the join key and match/tolerance definition for the domains in scope
- Define cadence, escalation threshold, and how resolved mismatches are recorded

### Step 5: Consolidate the Report

```
## ERP Consistency Audit: [feature/flow]

### Design-Time Findings
[source-of-truth map, idempotency findings, race/concurrency findings]

### Financial Chain Findings (if applicable)
[four-layer map, atomicity findings, idempotency findings]

### Recommended Reconciliation Process
[data sets, join key, tolerance, cadence, escalation]

### Verdict
Safe to proceed / Needs redesign / Needs a reconciliation job before proceeding
```

Save as markdown.

### Step 6: Offer Next Steps

- "Want me to **check the inventory quantity math specifically** with an inventory flow design pass?"
- "Should I **design the audit-trail logging** for the actions involved?"
- "Want me to **review the accounting treatment** itself, not just cross-system agreement?"

## Notes

- A "Safe to proceed" verdict still needs at least one guardrail named per identified risk — never issue a clean verdict with unresolved idempotency or concurrency gaps.
- If engineering hasn't decided on a concurrency strategy yet, the verdict should be "Needs redesign," not a guess.
- Rising mismatch volume across reconciliation runs is a systemic-issue signal, not routine noise — call it out explicitly if historical data suggests a trend.
