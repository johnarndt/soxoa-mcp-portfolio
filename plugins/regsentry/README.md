# RegSentry MCP integration

Inspect authorized static tracking signals and review supplied consent evidence.

This plugin connects a compatible MCP client to RegSentry's hosted first-party endpoint and adds a scoped workflow skill. The public distribution files contain configuration, documentation and skill instructions. Product accounts, owner permissions, current plan entitlements and service terms continue to apply.

## Connection

Endpoint: https://regsentry.com/mcp

Transport: Streamable HTTP (client config type `http`).

No authentication. Public read-only tools.

```json
{
  "mcpServers": {
    "regsentry": {
      "type": "http",
      "url": "https://regsentry.com/mcp"
    }
  }
}
```

Use your client's normal remote-MCP authorization flow. This package contains no API keys, bearer tokens, client secrets, reviewer identities or private fixtures. It runs no local shell commands, lifecycle hooks or telemetry collectors.

## Example requests

- Inspect the tracking setup on a public domain I am authorized to test.
- Grade these consent-flow observations and show what still needs verification.
- Give me the remediation playbook for this tracker.

## Workflow boundaries

Inspect only sites the user is authorized to review. Static markup is evidence of signals, not proof that tracking ran or a legal compliance determination.

Connection and installation do not themselves authorize paid work, purchases, communication to other people, or arbitrary changes to resources. Follow the user's actual request and the current server schema. Where an action needs confirmation, identify the exact resource and consequence before invoking it.

## Documentation and support

- [Official documentation](https://regsentry.com/mcp-guide)
- [Support](https://regsentry.com/support)
- [Privacy](https://regsentry.com/privacy)
- [Terms](https://regsentry.com/terms)
- [Existing Glama connector](https://glama.ai/mcp/connectors/com.regsentry/tracking-inspector)

## License

The distribution metadata, configuration, documentation and skill instructions are licensed under MIT. This license does not license the hosted application implementation or replace the product's service terms.
