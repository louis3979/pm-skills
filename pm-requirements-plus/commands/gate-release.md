---
description: Generate adversarial QA test scenarios and run the go/no-go release checklist in one pass
argument-hint: "<a feature/PRD approaching release>"
---

# /gate-release -- QA Coverage + Go/No-Go

Generate adversarial test scenarios from a PRD, then run the full release-readiness checklist against it — one consolidated gate before a feature ships.

## Invocation

```
/gate-release Stock transfer approval feature, dev and QA report complete
/gate-release [paste the PRD] — releasing to production next Tuesday
/gate-release Customer refund flow — third release candidate
```

## Workflow

### Step 1: Generate Test Scenarios

Apply the **product-qa-reviewer** skill:

- Happy path, negative path, boundary, permission, state transition, concurrency, and data-consistency cases
- Weight concurrency and data-consistency cases higher for anything touching inventory, payments, or approvals

### Step 2: Run the Release Checklist

Apply the **release-manager** skill:

- Confirm all 12 readiness items (PRD, design, dev, QA, tracking, migration, feature flag, docs, training, support, rollback, monitoring)
- Render an explicit GO / GO WITH RISK / NO-GO verdict

### Step 3: Consolidate

```
## Release Gate: [feature name]

## QA Test Cases
[full test-case set from Step 1]

## Release Checklist
[checklist table and verdict from Step 2]
```

Save as a markdown document.

### Step 4: Offer Next Steps

- If NO-GO: "Want me to re-run this once the flagged gap is fixed?"
- If GO: "Should I prep the release notes next?"
- "Want a **persona**-grounded sanity check on whether these test cases cover the actors who'll actually feel this change?"

## Notes

- An unresolved blocker-severity QA finding, or a missing rollback plan for a data-affecting change, forces NO-GO — no silent override.
- An item nobody has confirmed status for counts as FAIL for the verdict, not a pass by default.
- The verdict is always exactly one of GO / GO WITH RISK / NO-GO, never a hedge.
