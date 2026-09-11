---
description: Design the full control layer for a feature or module — role permissions, approval chain, audit logging, and document/record numbering
argument-hint: "<feature or module needing access control>"
---

# /setup-access-controls -- Access Control Setup

Design the complete control layer for a feature or module in one pass: who can do what, how approvals route, what gets logged, and how records are numbered/identified.

## Invocation

```
/setup-access-controls Expense report submission and approval
/setup-access-controls Admin console user management
/setup-access-controls [describe the module and its roles]
```

## Workflow

### Step 1: Understand the Feature

Ask if not already clear:
- What entity/record is this for, and what actions exist on it (create, approve, cancel, export, etc.)?
- What roles are involved, and is there an existing state machine or process model for this entity?
- Are there known risk thresholds that should change who approves (amount, scope, sensitivity)?

### Step 2: Design Access Control

Apply the **rbac-permission-designer** skill:

- Build the full role × action permission matrix, including scoping (org/tenant/resource) and conditional rules
- Flag segregation-of-duties conflicts (e.g. same role creating and approving)

### Step 3: Design the Approval Chain

Apply the **approval-workflow-designer** skill:

- Define single vs. multi-level approval, thresholds, delegation, and escalation
- Define rejection behavior and illegal transitions (e.g. self-approval)

### Step 4: Design Audit Logging

Apply the **audit-trail-designer** skill:

- Define the audit record schema (who/when/before/after/source/reason) for every state-changing action
- Define retention, access, and redaction rules

### Step 5: Design Record Numbering (if the entity has a user-facing identifier)

Apply the **document-numbering-designer** skill:

- Design the prefix/scope/period/sequence format and its concurrency guarantee

### Step 6: Consolidate the Controls Spec

```
## Access Control Spec: [feature/module]

### Permission Matrix
[role × action → allowed/denied/conditional]

### Approval Chain
[trigger, thresholds, sequence, delegation, escalation]

### Audit Trail Schema
[fields, retention, access/redaction]

### Record Numbering (if applicable)
[format, reset policy, concurrency guarantee]

### Open Questions
[anything flagged TBD across the four skills above]
```

Save as markdown.

### Step 7: Offer Next Steps

- "Should I **audit cross-system data consistency** once this ships?"
- "Want me to **run this alongside a security review** (`/prep-technical-handoff`)?"
- "Should I **write the PRD** for this feature now that the control layer is defined?"

## Notes

- Segregation-of-duties conflicts (same role can create and approve) are always flagged, never silently allowed by default.
- Self-approval is denied by default unless the business explicitly says otherwise for a specific role/threshold.
- If roles, thresholds, or volume aren't fully known, don't invent them — fill in what's known and list the rest under Open Questions as explicit proposals needing sign-off.
