---
description: Translate a requirement into technical impact areas and run a product-level security pass before engineering starts
argument-hint: "<a requirement or PRD ready for engineering>"
---

# /prep-technical-handoff -- Technical Impact + Security Handoff

Turn an approved requirement or PRD into a structured technical-impact map, then run a product-level security review over the same scope — a single handoff packet for engineering to start from.

## Invocation

```
/prep-technical-handoff [paste the PRD for "store-to-warehouse stock request"]
/prep-technical-handoff Customers can now export their full transaction history as CSV
/prep-technical-handoff [upload the approved PRD]
```

## Workflow

### Step 1: Map Technical Impact

Apply the **technical-product-analyst** skill:

- Frontend, backend, API, database, events, permissions, integration, and data-migration impact
- Performance, security, and observability notes worth raising before build starts

### Step 2: Run the Security Pass

Apply the **security-product-reviewer** skill over the same requirement:

- Authentication, authorization, RBAC completeness
- Sensitive data exposure, audit trail, export permission
- Tenant isolation, session/security edge cases

### Step 3: Consolidate

```
## Technical Handoff: [feature name]

[technical impact map from Step 1]

## Security Review

[findings table and launch blockers from Step 2]

## Open Items Before Engineering Starts
[anything flagged as needing more detail or a decision]
```

Save as a markdown document.

### Step 4: Offer Next Steps

- "Any state/permission gaps here should probably go through **model-business-process** first — want me to run that?"
- "Ready to **gate this for release** once development and QA are done?"

## Notes

- A data migration on a table with real production data is always a required discussion item, not something to wave through silently.
- Any launch-blocker security finding (tenant isolation, sensitive data exposure) should be resolved before this packet is considered ready to hand off.
- If the requirement is too vague to derive concrete technical impact, name exactly which sections need more detail rather than guessing.
