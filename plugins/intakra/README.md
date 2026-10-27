# Intakra MCP integration

Review supplied buying evidence and owned account opportunities, and configure explicitly requested workspace changes.

## Connection

Endpoint: https://intakra.com/mcp

Transport: Streamable HTTP (client config type `http`).

Supplied-evidence tools are public. Connected workspace tools require normal OAuth 2.1 / PKCE consent.

Use the client's normal remote-MCP authorization flow. Credentials stay in the client's secure credential store; do not paste them into chat.

## Included workflows

- [intakra-buying-signal-review](skills/intakra-buying-signal-review/SKILL.md): Use when a user wants to score supplied account-fit and buying-signal evidence or prepare a review-only why-now brief.
- [intakra-account-opportunities](skills/intakra-account-opportunities/SKILL.md): Prioritize owned Intakra accounts, review dated buying signals and changes, find relevant contact evidence, or prepare a daily account brief.
- [intakra-workspace-setup](skills/intakra-workspace-setup/SKILL.md): Set an Intakra offering, add explicitly chosen company domains, or request and review account suggestions for the user’s workspace.

## Example requests

- Prioritize my owned accounts using their dated evidence.
- Prepare a why-now review from these supplied facts.
- Help me review account suggestions before I choose what to add.

## Workflow boundaries

Use dated supplied or owned-workspace evidence; do not infer verified buying intent or contact prospects. Obtain authorization for the actual account additions, offering changes or suggestion requests. Saved lists and job status do not prove a fresh research result.

Connection does not authorize unrelated writes, paid work, purchases, or communication. Follow the user's actual request and the current server schema. Recover uncertain jobs and orders before starting another.

Documentation: https://intakra.com/mcp-guide

These MIT-licensed files contain public configuration and skill instructions. Hosted services retain their terms and implementation rights.
