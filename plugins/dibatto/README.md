# Dibatto MCP integration

Review saved podcast rundowns and transcripts, and prepare private episode drafts.

This plugin connects a compatible MCP client to Dibatto's hosted first-party endpoint and adds a scoped workflow skill. The public distribution files contain configuration, documentation and skill instructions. Product accounts, owner permissions, current plan entitlements and service terms continue to apply.

## Connection

Endpoint: https://dibatto.com/mcp

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 with PKCE through the MCP client. Account tools use the connected owner identity. Public metadata discovery, where available, does not grant account access.

```json
{
  "mcpServers": {
    "dibatto": {
      "type": "http",
      "url": "https://dibatto.com/mcp"
    }
  }
}
```

Use your client's normal remote-MCP authorization flow. This package contains no API keys, bearer tokens, client secrets, reviewer identities or private fixtures. It runs no local shell commands, lifecycle hooks or telemetry collectors.

## Example requests

- Show my podcast show’s saved rundown and citations.
- Find my episode and its saved transcript.
- Prepare a private episode draft from my selected rundown.

## Workflow boundaries

Read owned shows, cached cited rundowns, saved episodes/transcripts and existing wrap states. Preparing a private episode is not recording or publication. New research/model work requires explicit authorization and current Studio entitlement. Recording, live co-hosting, media upload, wrap generation and publication remain app-only.

Connection and installation do not themselves authorize paid work, purchases, communication to other people, or arbitrary changes to resources. Follow the user's actual request and the current server schema. Where an action needs confirmation, identify the exact resource and consequence before invoking it.

## Documentation and support

- [Official documentation](https://dibatto.com/developers)
- [Support](https://dibatto.com/about)
- [Privacy](https://dibatto.com/legal/privacy)
- [Terms](https://dibatto.com/legal/terms)
- [Existing Glama connector](https://glama.ai/mcp/connectors/com.soxoa/dibatto-podcast)

## License

The distribution metadata, configuration, documentation and skill instructions are licensed under MIT. This license does not license the hosted application implementation or replace the product's service terms.
