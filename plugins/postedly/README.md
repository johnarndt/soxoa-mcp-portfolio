# Postedly MCP integration

Prepare fax, letter, certified mail, postcard and handwritten card quotes, open private review links, and read owned order status.

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
- Prepare mailing this finished PDF and give me the private link to review every page and the total. Do not pay or send yet.
- Show handwritten card designs and writing styles for a thank-you note.
- Check the recorded status of my existing Postedly order.

## Workflow boundaries

Check `postedly_services` or the [live catalog](https://postedly.com/api/catalog) before preparing a fax, letter, certified mail, postcard or handwritten-card quote. Use the returned availability and requirements; for handwritten cards, also check the product catalog. The object beta has a separate manual request path and does not support automated document orders.

Use the actual intended document. Preserve a provided PDF's exact bytes unless changes were requested. For a newly requested letter, finish its actual wording, export it to PDF, and render and inspect every page before uploading. Do not substitute a sample, placeholder or writing instructions; intentional forms, templates and test documents remain valid when requested. If the intended file is missing or inaccessible, use a private upload handoff or explain what is missing. A checksum verifies byte integrity, not content correctness.

Review every page of the final proof, including the actual body and any generated cover or postal layout. Card samples are not a rendered proof of the user's exact message. Uploading, quoting and opening private review do not approve, charge or send. Payment requires the user's explicit browser review of the exact proof or item, recipient, total and terms. Report payment and fulfillment separately.

Connection and installation do not themselves authorize paid work, purchases, communication to other people, or arbitrary changes to resources. Follow the user's actual request and the current server schema. Where an action needs confirmation, identify the exact resource and consequence before invoking it.

## Documentation and support

- [Official documentation](https://postedly.com/developers)
- [Agent file-transfer, content and recovery guide](https://postedly.com/agent-guide.md)
- [Support](https://postedly.com/support)
- [Privacy](https://postedly.com/privacy)
- [Terms](https://postedly.com/terms)
- [Existing Glama connector](https://glama.ai/mcp/connectors/com.postedly/send)

## License

The distribution metadata, configuration, documentation and skill instructions are licensed under MIT. This license does not license the hosted application implementation or replace the product's service terms.
