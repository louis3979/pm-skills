---
description: Audit a feature or flow for cross-system data consistency risk when it writes to more than one system or view of the same data
argument-hint: "<feature or flow to audit>"
---

# /audit-data-consistency -- Data Consistency Audit

Check a feature or flow for the class of bug that generic testing misses: two systems (or two views of the same event) quietly drifting apart. Produces one consolidated consistency-risk report.

## Invocation

```
/audit-data-consistency Order-to-payment flow for the new checkout redesign
/audit-data-consistency Profile updates that fan out to search index and cache
/audit-data-consistency [paste a PRD or system design]
```

## Workflow

### Step 1: Scope the Audit

Ask if not already clear:
- Which systems/domains does this feature touch (primary datastore, cache, search index, billing, reporting, a downstream service)?
- Is this a design review (nothing built yet) or an investigation of an observed discrepancy?

### Step 2: Check Design-Time Consistency

Apply the **data-consistency-reviewer** skill:

- Map each system/domain to its single source of truth
- Check idempotency on every write, and locking/conflict strategy on every shared entity
- Trace one end-to-end example through all layers

### Step 3: Design the Safety Net

Apply the **reconciliation-designer** skill:

- Define the join key and match/tolerance definition for the systems in scope
- Define cadence, escalation threshold, and how resolved mismatches are recorded

### Step 4: Consolidate the Report

```
## Data Consistency Audit: [feature/flow]

### Design-Time Findings
[source-of-truth map, idempotency findings, race/concurrency findings]

### Recommended Reconciliation Process
[data sets, join key, tolerance, cadence, escalation]

### Verdict
Safe to proceed / Needs redesign / Needs a reconciliation job before proceeding
```

Save as markdown.

### Step 5: Offer Next Steps

- "Should I **design the audit-trail logging** for the actions involved (`/setup-access-controls`)?"
- "Want a **security review** of this same flow (`/prep-technical-handoff`)?"

## Notes

- A "Safe to proceed" verdict still needs at least one guardrail named per identified risk — never issue a clean verdict with unresolved idempotency or concurrency gaps.
- If engineering hasn't decided on a concurrency strategy yet, the verdict should be "Needs redesign," not a guess.
- Rising mismatch volume across reconciliation runs is a systemic-issue signal, not routine noise — call it out explicitly if historical data suggests a trend.
