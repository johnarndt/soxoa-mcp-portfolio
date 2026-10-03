# Dokyumi MCP integration

Extract attached documents with saved schemas and review confidence and validation.

This plugin connects a compatible MCP client to Dokyumi's hosted first-party endpoint and adds a scoped workflow skill. The public distribution files contain configuration, documentation and skill instructions. Product accounts, owner permissions, current plan entitlements and service terms continue to apply.

## Connection

Endpoint: https://dokyumi.com/mcp

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 with PKCE through the MCP client. Account tools use the connected owner identity. Public metadata discovery, where available, does not grant account access.

```json
{
  "mcpServers": {
    "dokyumi": {
      "type": "http",
      "url": "https://dokyumi.com/mcp"
    }
  }
}
```

Use your client's normal remote-MCP authorization flow. This package contains no API keys, bearer tokens, client secrets, reviewer identities or private fixtures. It runs no local shell commands, lifecycle hooks or telemetry collectors.

## Example requests

- List my saved Dokyumi extraction schemas.
- Find my saved invoice schema before extracting this attached invoice.
- Show a saved extraction and identify values that need review.

## Workflow boundaries

Find the user's saved schema before extracting the exact supplied document. Ask for explicit existing-credit approval before a fresh extraction. Preserve its request key on uncertain responses and same-request recovery. Report actual confidence, validation and provider provenance; confidence is not an accuracy guarantee. Never buy or refill credits.

Connection and installation do not themselves authorize paid work, purchases, communication to other people, or arbitrary changes to resources. Follow the user's actual request and the current server schema. Where an action needs confirmation, identify the exact resource and consequence before invoking it.

## Documentation and support

- [Official documentation](https://dokyumi.com/docs/mcp)
- [Support](https://dokyumi.com/docs/mcp)
- [Privacy](https://dokyumi.com/privacy)
- [Terms](https://dokyumi.com/terms)
- [Existing Glama connector](https://glama.ai/mcp/connectors/com.dokyumi/document-extraction)

## License

The distribution metadata, configuration, documentation and skill instructions are licensed under MIT. This license does not license the hosted application implementation or replace the product's service terms.
