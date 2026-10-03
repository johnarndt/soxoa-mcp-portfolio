# Soxoa MCP integration

Estimate illustrative automation ROI and prioritize user-described recurring workflows.

This plugin connects a compatible MCP client to Soxoa's hosted first-party endpoint and adds a scoped workflow skill. The public distribution files contain configuration, documentation and skill instructions. Product accounts, owner permissions, current plan entitlements and service terms continue to apply.

## Connection

Endpoint: https://soxoa.com/mcp

Transport: Streamable HTTP (client config type `http`).

No authentication. Public read-only tools.

```json
{
  "mcpServers": {
    "soxoa": {
      "type": "http",
      "url": "https://soxoa.com/mcp"
    }
  }
}
```

Use your client's normal remote-MCP authorization flow. This package contains no API keys, bearer tokens, client secrets, reviewer identities or private fixtures. It runs no local shell commands, lifecycle hooks or telemetry collectors.

## Example requests

- Estimate illustrative accounting automation value from my invoice-entry workflow assumptions.
- Rank these workflows by automation readiness and explain the guardrails.

## Workflow boundaries

Results are illustrative planning estimates. Preserve supplied assumptions, ask for required missing inputs, and distinguish an estimate from a guarantee.

Connection and installation do not themselves authorize paid work, purchases, communication to other people, or arbitrary changes to resources. Follow the user's actual request and the current server schema. Where an action needs confirmation, identify the exact resource and consequence before invoking it.

## Documentation and support

- [Official documentation](https://soxoa.com/mcp-guide)
- [Support](https://soxoa.com/support)
- [Privacy](https://soxoa.com/privacy)
- [Terms](https://soxoa.com/terms)
- [Existing Glama connector](https://glama.ai/mcp/connectors/com.soxoa/automation-planning)

## License

The distribution metadata, configuration, documentation and skill instructions are licensed under MIT. This license does not license the hosted application implementation or replace the product's service terms.
