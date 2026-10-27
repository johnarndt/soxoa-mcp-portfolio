# Portravo MCP integration

Prepare authorized construction takeoffs, review source gaps and quantities, and download reviewed estimates.

## Connection

Endpoint: https://portravo.com/mcp

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 / PKCE for connected owner resources.

Use the client's normal remote-MCP authorization flow. Credentials stay in the client's secure credential store; do not paste them into chat.

## Included workflows

- [portravo-prepare-takeoff](skills/portravo-prepare-takeoff/SKILL.md): Check trade availability and existing-credit cost, create an owned Portravo project, attach the actual plan PDF, and start an explicitly approved takeoff.
- [portravo-review-estimate](skills/portravo-review-estimate/SKILL.md): Recover an existing Portravo takeoff, inspect source-linked quantities and unresolved scope, and download a reviewed, priced estimate.
- [portravo-scope-questions](skills/portravo-scope-questions/SKILL.md): Turn actual Portravo takeoff notes, unresolved lines and source gaps into an estimator checklist and draft clarification questions.

## Example requests

- Check what is required before starting a takeoff for these selected trades.
- Review the source gaps and uncertain quantities in my existing takeoff.
- Download the estimate only after its review and pricing checks pass.

## Workflow boundaries

Use the exact uploaded PDF bytes or an actual permitted attachment descriptor. Ask for explicit existing-credit approval before a fresh takeoff. Preserve the documented idempotency key on an uncertain response; a retry is not approval for another job. Quantities and mappings need human review. Export only a reviewed, priced or final estimate as documented.

Connection does not authorize unrelated writes, paid work, purchases, or communication. Follow the user's actual request and the current server schema. Recover uncertain jobs and orders before starting another.

Documentation: https://portravo.com/developers/mcp

These MIT-licensed files contain public configuration and skill instructions. Hosted services retain their terms and implementation rights.
