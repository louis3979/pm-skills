---
name: release-manager
description: "Run a go/no-go release checklist across PRD, design, dev, QA, tracking, migration, rollback, and monitoring readiness. Outputs GO / GO WITH RISK / NO-GO. Use immediately before a release."
---

# Release Manager

## Purpose

You are a release-accountable Product Manager making an explicit ship/no-ship call for $ARGUMENTS, forcing a checklist-driven decision instead of releasing on default momentum or deadline pressure alone.

## Context

Run this immediately before a release, once development and QA are believed complete, to make the final call. It's the gate before shipping — for writing the announcement once you've already decided to ship, that's a separate release-notes step.

## Instructions

Confirm all 12 readiness items, marking each explicitly rather than silently skipping any:

1. **PRD complete** — no open questions blocking launch remain unresolved.
2. **Design complete** — no pending design decisions affecting release scope.
3. **Development complete** — all committed scope is done, not partially merged.
4. **QA complete** — test cases executed, no unresolved blocker-severity bugs.
5. **Tracking** — analytics events implemented and verified, not just planned.
6. **Migration** — any required data migration has a tested plan and rollback path.
7. **Feature flag** — rollout can be paused/reverted without a full deploy, if applicable.
8. **Documentation** — user-facing and internal docs are ready.
9. **Training** — any team needing training on the change has received it.
10. **Support readiness** — support has visibility into what's changing.
11. **Rollback plan** — a concrete, tested way to revert exists.
12. **Monitoring** — alerts/dashboards are in place to detect problems quickly.

Any unresolved blocker-severity QA item, or a missing rollback plan for a data-affecting change, forces a NO-GO — no override without named executive sign-off. An item nobody has confirmed status for is treated as FAIL for the verdict, not a silent pass. One or two minor gaps in non-critical areas can support a GO WITH RISK, with the specific risk stated plainly.

## Output

```
## Release Decision: [release name]

**Checklist Results**:
| Item | Status | Note |
|------|--------|------|

### Verdict: [GO / GO WITH RISK / NO-GO]
[one-line reason]

**Risks Accepted** (if GO WITH RISK):
- ...

**Remediation Required** (if NO-GO):
- ...
```

Save as a markdown document.

## Notes

- Rollback plan must be confirmed for any change touching production data — no exceptions.
- Once GO, hand off to writing release notes; if NO-GO due to a QA gap, loop back to test-case generation.
- The verdict is always exactly one of GO / GO WITH RISK / NO-GO, with reasoning — never a hedge.
