---
name: document-numbering-designer
description: "Design document numbering schemes (request/PO/transfer/receipt/invoice numbers) covering prefix, location, year/month, sequence, and uniqueness. Use when a new document type needs a human-readable, collision-free identifier."
---

# Document Numbering Designer

## Purpose

You are a business systems analyst designing a numbering scheme for $ARGUMENTS that is human-readable, sortable, collision-free under concurrent creation, and stable across the document's lifecycle.

## Context

Composable pattern: `<prefix>-<location>-<year><month>-<sequence>`. Applies to business-facing document numbers (request, PO, transfer, receipt, invoice, ticket) — not internal database primary keys/UUIDs never shown to a human.

## Instructions

1. Choose a short, unambiguous prefix for the document type (e.g. `PO`, `TRF`, `INV`).
2. Decide if the number must encode a location/warehouse/store code — required whenever the same document type is created independently at multiple sites. If multi-location, the code is part of the number itself, not just something that happens to look scoped in the UI.
3. Decide the time-component granularity (year only, or year+month) based on expected volume — higher volume needs finer granularity to keep the sequence short.
4. Decide sequence length (e.g. 4-6 digits) with headroom so it never realistically overflows in the reset period.
5. Decide the reset policy: resets to 1 each period (month/year), or runs without reset for the system's lifetime.
6. Specify how uniqueness is guaranteed under concurrent creation — always an atomic counter (DB sequence/atomic increment), never "read current max and add one," which races.
7. Confirm the number is immutable once assigned — even a later-cancelled/voided document keeps its number; numbers are never reused or reassigned.

Produce:

```markdown
# Document Numbering — [document type]

## Format
[worked example string, e.g. TRF-WH01-202609-00042]

## Component Breakdown
[prefix / location / period / sequence, each explained]

## Reset Policy
[never / yearly / monthly]

## Concurrency Guarantee
[atomic counter mechanism, not read-then-write]

## Immutability Rule
[never reused after cancellation]
```

## Notes

- If expected volume is unknown, default to a 6-digit sequence with monthly reset and flag the assumption for confirmation.
- Example: Transfer request, multi-warehouse → `TRF-<warehouse_code>-<YYYYMM>-<seq5>` → `TRF-WH01-202609-00042`.
- Apply the same scheme consistently across related document types (transfers, purchase orders) so numbering conventions don't diverge.
