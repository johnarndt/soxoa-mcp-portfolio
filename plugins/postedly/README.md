# Postedly MCP integration

Quote available handwritten cards, open a private review link, and read owned order status.

This plugin connects a compatible MCP client to Postedly's hosted first-party endpoint and adds a scoped workflow skill. The public distribution files contain configuration, documentation and skill instructions. Product accounts, owner permissions, current plan entitlements and service terms continue to apply.

## Connection

Endpoint: https://postedly.com/mcp/send

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 with PKCE through the MCP client. Account tools use the connected owner identity. Public metadata discovery, where available, does not grant account access.

```json
{
  "mcpServers": {
    "postedly": {
      "type": "http",
      "url": "https://postedly.com/mcp/send"
    }
  }
}
```

Use your client's normal remote-MCP authorization flow. This package contains no API keys, bearer tokens, client secrets, reviewer identities or private fixtures. It runs no local shell commands, lifecycle hooks or telemetry collectors.

## Example requests

- What can Postedly send right now? Show available options.
- Show handwritten card designs and writing styles for a thank-you note.
- Prepare my card quote and private review link. Do not pay or mail yet.

## Workflow boundaries

Read the live service and card catalog first. Only handwritten cards are currently available. Quoting, document intake and opening private review do not send, charge, or approve payment. Card samples are not a rendered proof of the user's exact message. Payment requires the user's explicit browser review. Report payment and fulfillment separately.

Connection and installation do not themselves authorize paid work, purchases, communication to other people, or arbitrary changes to resources. Follow the user's actual request and the current server schema. Where an action needs confirmation, identify the exact resource and consequence before invoking it.

## Documentation and support

- [Official documentation](https://postedly.com/developers)
- [Support](https://postedly.com/support)
- [Privacy](https://postedly.com/privacy)
- [Terms](https://postedly.com/terms)
- [Existing Glama connector](https://glama.ai/mcp/connectors/com.postedly/send)

## License

The distribution metadata, configuration, documentation and skill instructions are licensed under MIT. This license does not license the hosted application implementation or replace the product's service terms.
