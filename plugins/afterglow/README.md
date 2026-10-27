# Afterglow MCP integration

Turn connected separation checklists into practical next steps and save confirmed item progress.

## Connection

Website: https://withafterglow.com

Endpoint: https://api.withafterglow.com/mcp

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 / PKCE for connected owner resources.

Use the client's normal remote-MCP authorization flow. Credentials stay in the client's secure credential store; do not paste them into chat.

## Included workflows

- [afterglow-practical-next-steps](skills/afterglow-practical-next-steps/SKILL.md): Turn a linked Afterglow checklist into manageable next steps, review saved progress, or update an exact confirmed item. Use for practical separation, moving, money and coparenting tasks.

## Example requests

- Help me choose manageable next steps from my connected checklist.
- Show what is still open without changing it.
- Save the exact checklist status I confirm.

## Workflow boundaries

Read the user's applicable legal, money, home or coparenting checklist and preserve its returned disclaimer, audience filter, onboarding and plan limits. Save only the exact item and todo, done or not-applicable state the user confirms. Repeating the same item and state preserves its completion timestamp. These practical breakup/separation checklists do not expose the user's story, coaching history or private check-ins.

Connection does not authorize unrelated writes, paid work, purchases, or communication. Follow the user's actual request and the current server schema. Recover uncertain jobs and orders before starting another.

Documentation: https://api.withafterglow.com/developers

These MIT-licensed files contain public configuration and skill instructions. Hosted services retain their terms and implementation rights.

The public website and API use separate hosts. OAuth discovery, authorization and the protected MCP resource use `https://api.withafterglow.com`; a legacy-host connection needs fresh authorization for the API resource. The API documentation page may still show the older hostname; the current connection URL above is verified.
