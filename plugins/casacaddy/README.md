# CasaCaddy MCP integration

Use a paired installation to prepare bounded home-maintenance guides and recover saved requests.

## Connection

Endpoint: https://api.casacaddy.com/mcp

Transport: Streamable HTTP (client config type `http`).

Use native CasaCaddy Assistant pairing and the normal OAuth connection for the eligible installation.

Use the client's normal remote-MCP authorization flow. Credentials stay in the client's secure credential store; do not paste them into chat.

## Included workflows

- [casacaddy-plan-home-maintenance](skills/casacaddy-plan-home-maintenance/SKILL.md): Get bounded maintenance guidance for user-described appliances through a paired CasaCaddy installation, recover a saved guide, or choose a safe next task.

## Example requests

- Show the maintenance guidance available to my paired installation.
- Help me prepare a bounded guide for this appliance.
- Recover the saved guide request I already started.

## Workflow boundaries

Read the maintenance requirements and account/device-owned guide job. Ask for confirmation before preparing a guide, preserve the request key on a retry, and report its actual queued, processing, failed or completed state. Guide preparation is not evidence the maintenance work was performed.

Connection does not authorize unrelated writes, paid work, purchases, or communication. Follow the user's actual request and the current server schema. Recover uncertain jobs and orders before starting another.

Documentation: https://api.casacaddy.com/developers

These MIT-licensed files contain public configuration and skill instructions. Hosted services retain their terms and implementation rights.
