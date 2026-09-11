# Ingestion — Index

Synthesis records — one per artifact ingested from `source/`, mirroring its subfolder (`interviews/`, `meetings/`, `market/`, `adhoc/`).

Each record tags its content using this vocabulary:
- **observation** — a direct quote or factual claim from the source artifact
- **interpretation** — the agent's framing of what an observation means
- **hypothesis** — a testable belief generated from the observation(s)
- **assumption** — an implicit, unvalidated claim the artifact didn't actually confirm

Every interpretation/hypothesis links back to the observation(s) it came from — this folder is the working-memory layer between raw `source/` and the durable `knowledge/`/`hypotheses/`/`decisions/`/`stakeholders/` layer.

This is a sorting bench, not a backlog — items here should get propagated to the durable layer promptly by `/ingest`, not accumulate unresolved.
