# Soxoa MCP integration

Discover recurring workflows, estimate illustrative automation value, and prepare a practical pilot and business case.

## Connection

Endpoint: https://soxoa.com/mcp

Transport: Streamable HTTP (client config type `http`).

Public planning tools; no account authentication.

Use the client's normal remote-MCP authorization flow. Credentials stay in the client's secure credential store; do not paste them into chat.

## Included workflows

- [soxoa-automation-planning](skills/soxoa-automation-planning/SKILL.md): Choose an automation pilot, estimate illustrative capacity savings, or turn a supplied workflow into a practical prompt and acceptance plan.
- [soxoa-process-discovery](skills/soxoa-process-discovery/SKILL.md): Interview the user about recurring manual work and turn confirmed workload facts into an automation intake before estimating value.
- [soxoa-automation-business-case](skills/soxoa-automation-business-case/SKILL.md): Turn confirmed workflow assumptions and Soxoa calculations into a decision memo with illustrative capacity value and a bounded pilot proposal.

## Example requests

- Help me identify a worthwhile recurring task to automate.
- Turn this workflow into a pilot with acceptance checks.
- Prepare a decision memo using these workload assumptions.

## Workflow boundaries

Results are illustrative planning estimates. Preserve supplied assumptions, ask for required missing inputs, and distinguish an estimate from a guarantee.

Connection does not authorize unrelated writes, paid work, purchases, or communication. Follow the user's actual request and the current server schema. Recover uncertain jobs and orders before starting another.

Documentation: https://soxoa.com/mcp-guide

These MIT-licensed files contain public configuration and skill instructions. Hosted services retain their terms and implementation rights.
