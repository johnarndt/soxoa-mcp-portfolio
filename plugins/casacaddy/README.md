# CasaCaddy MCP integration

Read maintenance requirements, prepare confirmed guides and check device-owned guide jobs.

This plugin connects a compatible MCP client to CasaCaddy's hosted first-party endpoint and adds a scoped workflow skill. The public distribution files contain configuration, documentation and skill instructions. Product accounts, owner permissions, current plan entitlements and service terms continue to apply.

## Connection

Endpoint: https://api.casacaddy.com/mcp

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 with PKCE through the MCP client. Account tools use the connected owner identity. Public metadata discovery, where available, does not grant account access.

```json
{
  "mcpServers": {
    "casacaddy": {
      "type": "http",
      "url": "https://api.casacaddy.com/mcp"
    }
  }
}
```

Use your client's normal remote-MCP authorization flow. This package contains no API keys, bearer tokens, client secrets, reviewer identities or private fixtures. It runs no local shell commands, lifecycle hooks or telemetry collectors.

## Example requests

- Show CasaCaddy guide requirements for my device.
- Check the status of my maintenance-guide job.
- Review my saved guide before preparing another.

## Workflow boundaries

Read the maintenance requirements and account/device-owned guide job. Ask for confirmation before preparing a guide, preserve the request key on a retry, and report its actual queued, processing, failed or completed state. Guide preparation is not evidence the maintenance work was performed.

Connection and installation do not themselves authorize paid work, purchases, communication to other people, or arbitrary changes to resources. Follow the user's actual request and the current server schema. Where an action needs confirmation, identify the exact resource and consequence before invoking it.

## Documentation and support

- [Official documentation](https://api.casacaddy.com/developers)
- [Support](https://api.casacaddy.com/support)
- [Privacy](https://api.casacaddy.com/privacy)
- [Terms](https://api.casacaddy.com/terms)
- [Existing Glama connector](https://glama.ai/mcp/connectors/com.soxoa/casacaddy-maintenance)

## License

The distribution metadata, configuration, documentation and skill instructions are licensed under MIT. This license does not license the hosted application implementation or replace the product's service terms.
