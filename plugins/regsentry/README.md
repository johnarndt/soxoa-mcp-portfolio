# RegSentry MCP integration

Inspect authorized tracking and consent evidence, compare observations, and prepare remediation and evidence exports.

## Connection

Endpoint: https://regsentry.com/mcp

Transport: Streamable HTTP (client config type `http`).

Public tools; no account authentication. Site inspection still requires the user’s authorization.

Use the client's normal remote-MCP authorization flow. Credentials stay in the client's secure credential store; do not paste them into chat.

## Included workflows

- [regsentry-consent-evidence-review](skills/regsentry-consent-evidence-review/SKILL.md): Inspect an authorized public website's tracking signals, compare observed consent phases, and prepare a practical evidence report and retest plan.

## Example requests

- Review tracking signals on this public site I am authorized to test.
- Compare these before-and-after consent observations.
- Prepare an evidence report and retest plan.

## Workflow boundaries

Inspect only sites the user is authorized to review. Static markup is evidence of signals, not proof that tracking ran or a legal compliance determination.

Connection does not authorize unrelated writes, paid work, purchases, or communication. Follow the user's actual request and the current server schema. Recover uncertain jobs and orders before starting another.

Documentation: https://regsentry.com/mcp-guide

These MIT-licensed files contain public configuration and skill instructions. Hosted services retain their terms and implementation rights.
