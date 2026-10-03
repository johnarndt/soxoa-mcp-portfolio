# Ocolta MCP integration

Read your existing categorical document review signals, confidence and indicator counts.

This plugin connects a compatible MCP client to Ocolta's hosted first-party endpoint and adds a scoped workflow skill. The public distribution files contain configuration, documentation and skill instructions. Product accounts, owner permissions, current plan entitlements and service terms continue to apply.

## Connection

Endpoint: https://app.ocolta.com/mcp

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 with PKCE through the MCP client. Account tools use the connected owner identity. Public metadata discovery, where available, does not grant account access.

```json
{
  "mcpServers": {
    "ocolta": {
      "type": "http",
      "url": "https://app.ocolta.com/mcp"
    }
  }
}
```

Use your client's normal remote-MCP authorization flow. This package contains no API keys, bearer tokens, client secrets, reviewer identities or private fixtures. It runs no local shell commands, lifecycle hooks or telemetry collectors.

## Example requests

- Show my recoverable Ocolta review summaries.
- What are this saved review’s categorical signals and confidence?
- Show indicator counts without revealing document text.

## Workflow boundaries

Read only owner-scoped existing review summaries. Preserve categorical signals, confidence and counts without exposing original document text. These are review signals; do not turn them into legal, medical or psychological diagnoses or create a new document assessment through these tools.

Connection and installation do not themselves authorize paid work, purchases, communication to other people, or arbitrary changes to resources. Follow the user's actual request and the current server schema. Where an action needs confirmation, identify the exact resource and consequence before invoking it.

## Documentation and support

- [Official documentation](https://app.ocolta.com/workspace/integrations)
- [Support](https://app.ocolta.com/workspace/integrations)
- [Privacy](https://app.ocolta.com/legal/privacy)
- [Terms](https://ocolta.com/legal/terms)
- [Existing Glama connector](https://glama.ai/mcp/connectors/com.soxoa/ocolta-review-summaries)

## License

The distribution metadata, configuration, documentation and skill instructions are licensed under MIT. This license does not license the hosted application implementation or replace the product's service terms.
