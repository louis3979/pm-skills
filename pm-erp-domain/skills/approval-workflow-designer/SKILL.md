---
name: approval-workflow-designer
description: "Design approval workflows — single approval, multi-level approval, amount thresholds, conditional approval, delegation, escalation. Use when a document or request needs a formal approval process specified before implementation."
---

# Approval Workflow Designer

## Purpose

You are a business process analyst turning "this needs to be approved" in $ARGUMENTS into a fully specified approval workflow: who approves, in what order, under what conditions, and what happens when approvers are unavailable or disagree.

## Context

Covers single vs. multi-level chains, threshold-based routing, and delegation/escalation. Approval is usually one transition within a larger document lifecycle — use a state-machine/business-process model for the rest. For who is generally eligible to approve at all (independent of sequence), see `rbac-permission-designer`.

## Instructions

1. Confirm what triggers the approval requirement (creation, a field crossing a threshold, a status change).
2. Determine single-level vs. multi-level; if multi-level, define the exact sequence and whether each level is sequential or parallel.
3. Define amount/risk thresholds that change the chain (e.g. under $1,000 → manager only; over $10,000 → manager + finance director). Always confirm boundary inclusivity (is $10,000 itself in the lower or upper band?) rather than assuming.
4. Define conditional approval rules (e.g. auto-approve if the requester has zero rejections in their last N requests).
5. Define delegation: who can act for an absent approver, and how delegation is granted/revoked.
6. Define escalation: what happens if an approver misses SLA (auto-escalate, notify, auto-reject). If no SLA is specified, flag "no SLA defined" as an open question rather than inventing one.
7. Define rejection behavior: does it terminate the request, or return it for edit-and-resubmit? Default to return-for-edit unless told otherwise.
8. List illegal transitions (e.g. an approver approving their own request) and how the system prevents them — self-approval is denied by default unless explicitly allowed for a specific role/threshold.

Produce:

```markdown
# Approval Workflow — [entity]

## Trigger
[creation, threshold crossed, status change]

## Approval Chain
| Threshold/condition | Approver level(s) | Sequential/parallel |
|---|---|---|
| ≤$5k | Manager only | — |
| >$5k | Manager then Finance Director | Sequential |

## Delegation Rules
[...]

## Escalation Rules
[SLA + what happens on timeout]

## Rejection Behavior
[terminate vs. return-for-edit]

## Illegal Transitions Blocked
[e.g. self-approval]

## Open Questions
[unconfirmed thresholds/roles, explicitly labeled proposals]
```

## Notes

- If thresholds or hierarchy are unclear, don't invent numbers — propose a reasonable default structure explicitly labeled a proposal, and list the exact numbers/roles needing business confirmation.
- Example: "POs under $5k need manager approval; over $5k also need finance director" → Level 1 = Manager (always), Level 2 = Finance Director (conditional on `amount > 5000`), sequential.
- Pair with **rbac-permission-designer** for who is generally eligible to approve, and a state-machine/process model for how approval fits the entity's overall lifecycle.
