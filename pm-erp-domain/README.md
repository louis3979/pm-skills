# pm-erp-domain

ERP, retail, and inventory domain intelligence for PMs: stock logic, warehouse workflows, transfers, allocation, procurement, accounting consistency, RBAC, audit trails, and reconciliation for ERP/retail/warehouse systems. Overview: fills the domain gap generic PM frameworks don't cover — the operational and financial correctness rules specific to ERP-style products.

## Install

Add this fork's marketplace to Claude Code, then install the plugin:

```
/plugin marketplace add louis3979/pm-skills
/plugin install pm-erp-domain@pm-skills
```

## Skills (16)

- **inventory-domain-expert** — Validate on-hand/available/reserved stock quantity formulas and state transitions for internal consistency.
- **inventory-transaction-reviewer** — Verify every stock-changing action produces a complete, traceable transaction record.
- **warehouse-workflow-designer** — Design a complete warehouse operational process (inbound, putaway, picking, packing, receiving, cycle count, returns) with actors and exceptions.
- **stock-transfer-designer** — Standardize the Request → Approval → Allocation → Pick → Ship → Receive → Reconcile transfer lifecycle.
- **allocation-rule-designer** — Design the rule that decides who gets how much when demand exceeds supply.
- **procurement-domain-expert** — Validate a purchase-to-pay flow against standard 3-way-match discipline.
- **accounting-logic-reviewer** — Check a requirement's financial logic for gaps before it reaches finance engineering (not a replacement for an accountant).
- **financial-transaction-consistency-reviewer** — Check that a business document, transaction, and accounting entry stay consistent end-to-end.
- **rbac-permission-designer** — Design role-based permission matrices for a business workflow.
- **approval-workflow-designer** — Design multi-level approval chains with thresholds, delegation, and escalation.
- **audit-trail-designer** — Specify what must be logged for every state-changing action.
- **data-consistency-reviewer** — Review cross-domain consistency (inventory/orders/payments/accounting/reports) before shipping.
- **document-numbering-designer** — Design human-readable, collision-free document numbering schemes.
- **reconciliation-designer** — Design a process to detect and resolve drift between two systems.
- **retail-domain-expert** — Apply correct retail domain concepts (store, POS, promotion, price list, cash shift) to a requirement.
- **product-master-data-designer** — Design the product/variant/SKU master data model.

## Commands (3)

- `/pm-erp-domain:design-inventory-flow` — Design a complete inventory/stock-transfer flow from a raw scenario.
- `/pm-erp-domain:audit-erp-consistency` — Audit a feature or flow for cross-system data consistency risk.
- `/pm-erp-domain:setup-erp-controls` — Design the full control layer (permissions, approvals, audit logging, numbering) for a workflow.

## Author

LDJ

## License

MIT
