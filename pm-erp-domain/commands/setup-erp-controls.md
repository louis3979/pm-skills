---
description: Design the full control layer for a workflow/module — role permissions, approval chain, audit logging, and document numbering
argument-hint: "<workflow/module needing access control>"
---

# /setup-erp-controls -- ERP Controls Setup

Design the complete control layer for a business workflow or module in one pass: who can do what, how approvals route, what gets logged, and how documents are numbered.

## Invocation

```
/setup-erp-controls Purchase order approval and creation
/setup-erp-controls Stock transfer requests between stores and warehouse
/setup-erp-controls [describe the module and its roles]
```

## Workflow

### Step 1: Understand the Workflow

Ask if not already clear:
- What entity/document is this for, and what actions exist on it (create, approve, cancel, export, etc.)?
- What roles are involved, and is there an existing state machine or process model for this entity?
- Are there known dollar/risk thresholds that should change who approves?

### Step 2: Design Access Control

Apply the **rbac-permission-designer** skill:

- Build the full role × action permission matrix, including scoping (org/warehouse/store) and conditional rules
- Flag segregation-of-duties conflicts (e.g. same role creating and approving)

### Step 3: Design the Approval Chain

Apply the **approval-workflow-designer** skill:

- Define single vs. multi-level approval, thresholds, delegation, and escalation
- Define rejection behavior and illegal transitions (e.g. self-approval)

### Step 4: Design Audit Logging

Apply the **audit-trail-designer** skill:

- Define the audit record schema (who/when/before/after/source/reason) for every state-changing action
- Define retention, access, and redaction rules

### Step 5: Design Document Numbering (if the entity has a business-facing number)

Apply the **document-numbering-designer** skill:

- Design the prefix/location/period/sequence format and its concurrency guarantee

### Step 6: Consolidate the Controls Spec

```
## ERP Controls Spec: [workflow/module]

### Permission Matrix
[role × action → allowed/denied/conditional]

### Approval Chain
[trigger, thresholds, sequence, delegation, escalation]

### Audit Trail Schema
[fields, retention, access/redaction]

### Document Numbering (if applicable)
[format, reset policy, concurrency guarantee]

### Open Questions
[anything flagged TBD across the four skills above]
```

Save as markdown.

### Step 7: Offer Next Steps

- "Want me to **design the full inventory/transfer flow** this control layer sits on top of?"
- "Should I **audit cross-system consistency** once this is implemented?"
- "Want me to apply this to the **procurement** or **retail/POS** side specifically?"

## Notes

- Segregation-of-duties conflicts (same role can create and approve) are always flagged, never silently allowed by default.
- Self-approval is denied by default unless the business explicitly says otherwise for a specific role/threshold.
- If roles, thresholds, or numbering volume aren't fully known, don't invent them — fill in what's known and list the rest under Open Questions as explicit proposals needing sign-off.
