# Source — Index

Immutable copies of raw artifacts. Once a file lands here, it is never edited — it's the audit anchor everything else in this system links back to.

## Subfolders
- `interviews/` — customer/user interview transcripts
- `meetings/` — internal meeting notes/transcripts
- `market/` — competitor pages, analyst reports, market signals
- `adhoc/` — anything that doesn't fit the above (a Slack thread, a stray email, a one-off note)

`/ingest` files new artifacts here automatically, named `<date>-<slug>.md`, then creates the corresponding synthesis record in `ingestion/`.

If you need to correct something that turns out to be wrong, don't edit the file here — note the correction in the corresponding `ingestion/` record or in `knowledge/`, with a link back to this file for context.
