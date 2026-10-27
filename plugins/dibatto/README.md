# Dibatto MCP integration

Prepare sourced podcast rundowns and private episode drafts; review saved transcripts and production status.

## Connection

Endpoint: https://dibatto.com/mcp

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 / PKCE for connected owner resources.

Use the client's normal remote-MCP authorization flow. Credentials stay in the client's secure credential store; do not paste them into chat.

## Included workflows

- [dibatto-prepare-episode](skills/dibatto-prepare-episode/SKILL.md): Turn an owned Dibatto show’s sourced rundown into an episode brief or private draft, and prepare new research only when authorized.
- [dibatto-review-transcript](skills/dibatto-review-transcript/SKILL.md): Find owned Dibatto episodes, summarize saved transcripts, or check recording and post-production status without starting new production.

## Example requests

- Review my show rundown and prepare an episode brief.
- Prepare a private episode draft from confirmed sources.
- Summarize a saved transcript and check production status.

## Workflow boundaries

Read owned shows, cached cited rundowns, saved episodes/transcripts and existing wrap states. Preparing a private episode is not recording or publication. New research/model work requires explicit authorization and current Studio entitlement. Recording, live co-hosting, media upload, wrap generation and publication remain app-only.

Connection does not authorize unrelated writes, paid work, purchases, or communication. Follow the user's actual request and the current server schema. Recover uncertain jobs and orders before starting another.

Documentation: https://dibatto.com/developers

These MIT-licensed files contain public configuration and skill instructions. Hosted services retain their terms and implementation rights.
