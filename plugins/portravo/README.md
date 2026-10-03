# Portravo MCP integration

Review construction plan takeoffs and download estimates after review and pricing.

This plugin connects a compatible MCP client to Portravo's hosted first-party endpoint and adds a scoped workflow skill. The public distribution files contain configuration, documentation and skill instructions. Product accounts, owner permissions, current plan entitlements and service terms continue to apply.

## Connection

Endpoint: https://portravo.com/mcp

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 with PKCE through the MCP client. Account tools use the connected owner identity. Public metadata discovery, where available, does not grant account access.

```json
{
  "mcpServers": {
    "portravo": {
      "type": "http",
      "url": "https://portravo.com/mcp"
    }
  }
}
```

Use your client's normal remote-MCP authorization flow. This package contains no API keys, bearer tokens, client secrets, reviewer identities or private fixtures. It runs no local shell commands, lifecycle hooks or telemetry collectors.

## Example requests

- Show my construction takeoffs and which lines need review.
- Create an estimate project and attach this plan PDF.
- Download my reviewed, priced estimate as an Excel workbook.

## Workflow boundaries

Use the exact uploaded PDF bytes or an actual permitted attachment descriptor. Ask for explicit existing-credit approval before a fresh takeoff. Preserve the documented idempotency key on an uncertain response; a retry is not approval for another job. Quantities and mappings need human review. Export only a reviewed, priced or final estimate as documented.

Connection and installation do not themselves authorize paid work, purchases, communication to other people, or arbitrary changes to resources. Follow the user's actual request and the current server schema. Where an action needs confirmation, identify the exact resource and consequence before invoking it.

## Documentation and support

- [Official documentation](https://portravo.com/developers/mcp)
- [Support](https://portravo.com/support)
- [Privacy](https://portravo.com/privacy)
- [Terms](https://portravo.com/terms)
- [Existing Glama connector](https://glama.ai/mcp/connectors/com.portravo/construction-takeoff)

## License

The distribution metadata, configuration, documentation and skill instructions are licensed under MIT. This license does not license the hosted application implementation or replace the product's service terms.
