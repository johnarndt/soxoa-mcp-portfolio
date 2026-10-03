# MentionedOn MCP integration

Review supplied AI-discovery evidence and prioritize visibility improvements.

This plugin connects a compatible MCP client to MentionedOn's hosted first-party endpoint and adds a scoped workflow skill. The public distribution files contain configuration, documentation and skill instructions. Product accounts, owner permissions, current plan entitlements and service terms continue to apply.

## Connection

Endpoint: https://mentioned-on.com/mcp

Transport: Streamable HTTP (client config type `http`).

No authentication. Public read-only tools.

```json
{
  "mcpServers": {
    "mentionedon": {
      "type": "http",
      "url": "https://mentioned-on.com/mcp"
    }
  }
}
```

Use your client's normal remote-MCP authorization flow. This package contains no API keys, bearer tokens, client secrets, reviewer identities or private fixtures. It runs no local shell commands, lifecycle hooks or telemetry collectors.

## Example requests

- Assess these supplied page signals for AI discovery readiness.
- Turn these missing visibility signals into a prioritized action plan.
- Summarize these dated AI mention captures and preserve skipped requests and uncertainty.

## Workflow boundaries

Use supplied, dated evidence. Preserve skipped or uncertain captures. Do not claim these tools run fresh model scans or guarantee a recommendation.

Connection and installation do not themselves authorize paid work, purchases, communication to other people, or arbitrary changes to resources. Follow the user's actual request and the current server schema. Where an action needs confirmation, identify the exact resource and consequence before invoking it.

## Documentation and support

- [Official documentation](https://mentioned-on.com/developers/mcp)
- [Support](https://mentioned-on.com/support)
- [Privacy](https://mentioned-on.com/privacy)
- [Terms](https://mentioned-on.com/terms)
- [Existing Glama connector](https://glama.ai/mcp/connectors/com.mentioned-on/ai-discovery-readiness)

## License

The distribution metadata, configuration, documentation and skill instructions are licensed under MIT. This license does not license the hosted application implementation or replace the product's service terms.
