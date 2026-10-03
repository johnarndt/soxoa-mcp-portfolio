# Afterglow MCP integration

Read applicable breakup and separation checklists and save confirmed task progress.

This plugin connects a compatible MCP client to Afterglow's hosted first-party endpoint and adds a scoped workflow skill. The public distribution files contain configuration, documentation and skill instructions. Product accounts, owner permissions, current plan entitlements and service terms continue to apply.

## Connection

Endpoint: https://afterglow-lime.vercel.app/mcp

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 with PKCE through the MCP client. Account tools use the connected owner identity. Public metadata discovery, where available, does not grant account access.

```json
{
  "mcpServers": {
    "afterglow": {
      "type": "http",
      "url": "https://afterglow-lime.vercel.app/mcp"
    }
  }
}
```

Use your client's normal remote-MCP authorization flow. This package contains no API keys, bearer tokens, client secrets, reviewer identities or private fixtures. It runs no local shell commands, lifecycle hooks or telemetry collectors.

## Example requests

- What is left in my Afterglow home checklist?
- Show my remaining money checklist tasks.
- Mark the exact task I selected done after I confirm.

## Workflow boundaries

Read the user's applicable legal, money, home or coparenting checklist and preserve its returned disclaimer, audience filter, onboarding and plan limits. Save only the exact item and todo, done or not-applicable state the user confirms. Repeating the same item and state preserves its completion timestamp. These practical breakup/separation checklists do not expose the user's story, coaching history or private check-ins.

Connection and installation do not themselves authorize paid work, purchases, communication to other people, or arbitrary changes to resources. Follow the user's actual request and the current server schema. Where an action needs confirmation, identify the exact resource and consequence before invoking it.

## Documentation and support

- [Official documentation](https://afterglow-lime.vercel.app/developers)
- [Support](https://afterglow-lime.vercel.app/support)
- [Privacy](https://afterglow-lime.vercel.app/privacy)
- [Terms](https://afterglow-lime.vercel.app/terms)
- [Existing Glama connector](https://glama.ai/mcp/connectors/com.soxoa/afterglow-checklists)

## License

The distribution metadata, configuration, documentation and skill instructions are licensed under MIT. This license does not license the hosted application implementation or replace the product's service terms.
