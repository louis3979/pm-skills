---
description: Stress-test a product concept using Amazon's Working Backwards PR/FAQ method before it proceeds to a PRD
argument-hint: "<product/feature concept>"
---

# /write-prfaq -- PR/FAQ Challenge

Force customer-first clarity on a concept: write the press release for the finished product first, then survive a hard customer and internal FAQ.

## Invocation

```
/write-prfaq A one-click expense report generator for freelancers
/write-prfaq [describe the concept]
```

## Workflow

### Step 1: Understand the Concept

Ask if not already clear: who is this for, what problem does it solve, and what's the intended differentiation.

### Step 2: Run the PR/FAQ

Apply the **pr-faq-writer** skill: press release (challenged before proceeding), customer FAQ, internal FAQ, flagged unproven claims, and an explicit verdict.

Save the output as markdown.

### Step 3: Offer Next Steps

- If verdict is ready: "Want me to **write the PRD** now (`/write-prd`)?"
- If a weak spot was named: "Should I **validate the underlying problem** (`problem-validator`) or **brainstorm a stronger angle** (`structured-brainstormer`)?"

## Notes

- This is a stress test, not a formality — a generic press release or a dodged FAQ answer should be challenged and redrafted, not accepted.
- The verdict must be one of: ready for PRD / needs another pass on a named weak spot / concept doesn't hold up yet — never a vague "looks good."
