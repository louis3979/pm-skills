# Security Policy

This repository contains markdown prompt files (Claude Code skills and commands) and a small dependency-free Python validation script (`scripts/validate.py`). There is no runtime service, no user data handling, and no network-facing component here.

## Scope of concern

The realistic risk surface is:
- A skill/command file containing instructions that could cause an installing agent to take an unsafe or unintended action.
- `scripts/validate.py` behaving unexpectedly (it only reads local files under this repo and never writes, executes user input, or makes network calls).

## Reporting a concern

Please open a GitHub issue on this repository describing the concern. Do not include real credentials, personal data, or details of an active exploit against a third-party system in the report.

## Supported versions

Only the latest version on the `main` branch (see `CHANGELOG.md` for the current release) is supported.
