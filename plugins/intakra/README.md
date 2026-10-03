# Intakra MCP integration

Score supplied buying signals and prepare a review-only why-now brief.

This plugin connects a compatible MCP client to Intakra's hosted first-party endpoint and adds a scoped workflow skill. The public distribution files contain configuration, documentation and skill instructions. Product accounts, owner permissions, current plan entitlements and service terms continue to apply.

## Connection

Endpoint: https://intakra.com/mcp

Transport: Streamable HTTP (client config type `http`).

No authentication. Public read-only tools.

```json
{
  "mcpServers": {
    "intakra": {
      "type": "http",
      "url": "https://intakra.com/mcp"
    }
  }
}
```

Use your client's normal remote-MCP authorization flow. This package contains no API keys, bearer tokens, client secrets, reviewer identities or private fixtures. It runs no local shell commands, lifecycle hooks or telemetry collectors.

## Example requests

- Score these supplied account-fit facts and recent business signals.
- Prepare a why-now review from this supplied tech-stack change and flag unverified intent.
- Flag unsupported budget, authority, or buying-intent claims.

## Workflow boundaries

Use caller-supplied account fit and dated buying-signal evidence. Mark unverified intent and prepare review-only briefs; do not contact prospects.

Connection and installation do not themselves authorize paid work, purchases, communication to other people, or arbitrary changes to resources. Follow the user's actual request and the current server schema. Where an action needs confirmation, identify the exact resource and consequence before invoking it.

## Documentation and support

- [Official documentation](https://intakra.com/mcp-guide)
- [Support](https://intakra.com/contact)
- [Privacy](https://intakra.com/privacy)
- [Terms](https://intakra.com/terms)
- [Existing Glama connector](https://glama.ai/mcp/connectors/com.intakra/buying-signal-review)

## License

The distribution metadata, configuration, documentation and skill instructions are licensed under MIT. This license does not license the hosted application implementation or replace the product's service terms.
