# MentionedOn MCP integration

Review supplied discovery evidence and connected visibility reports, prepare website fixes, and organize actual AI-answer captures.

## Connection

Endpoint: https://mentioned-on.com/mcp

Transport: Streamable HTTP (client config type `http`).

Supplied-evidence tools are public. Connected workspace tools require normal OAuth 2.1 / PKCE consent.

Use the client's normal remote-MCP authorization flow. Credentials stay in the client's secure credential store; do not paste them into chat.

## Included workflows

- [mentionedon-discovery-evidence](skills/mentionedon-discovery-evidence/SKILL.md): Use when a user wants to assess supplied AI-discovery signals, prioritize visibility gaps, or summarize dated model-capture evidence.
- [mentionedon-visibility-review](skills/mentionedon-visibility-review/SKILL.md): Review a connected MentionedOn business’s saved AI visibility, competitors and comparable changes, or identify the next action from its existing report.
- [mentionedon-website-fixes](skills/mentionedon-website-fixes/SKILL.md): Inspect an owned business website, save schema and copy from confirmed facts, and verify that reviewed MentionedOn fixes were installed.
- [mentionedon-answer-capture](skills/mentionedon-answer-capture/SKILL.md): Prepare a repeatable log and prompt set for actual AI-answer captures supplied by the user, preserving assistant surface, date and missing results.

## Example requests

- Review my latest saved visibility report and show its capture dates.
- Prepare website fixes from my confirmed business facts.
- Help me capture and compare actual AI answers consistently.

## Workflow boundaries

Public evidence is supplied and dated. Connected reports are saved history, not a new model scan. Website tools save reviewed revisions for owned businesses; they do not publish a website. Respect current monitoring entitlements.

Connection does not authorize unrelated writes, paid work, purchases, or communication. Follow the user's actual request and the current server schema. Recover uncertain jobs and orders before starting another.

Documentation: https://mentioned-on.com/developers/mcp

These MIT-licensed files contain public configuration and skill instructions. Hosted services retain their terms and implementation rights.
