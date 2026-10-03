---
name: dokyumi-workflow
description: "Extract PDF or image fields using saved document schemas and review confidence and validation when a user asks to process an invoice or inspect a saved extraction."
---

Use the connected Dokyumi MCP at https://dokyumi.com/mcp for the user's requested workflow. Follow the current server tool schemas and owner-scoped resource results.

Find the user's saved schema before extracting the exact supplied document. Ask for explicit existing-credit approval before a fresh extraction. Preserve its request key on uncertain responses and same-request recovery. Report actual confidence, validation and provider provenance; confidence is not an accuracy guarantee. Never buy or refill credits.

Connect the user through the MCP client OAuth flow before accessing their resources. Do not ask them to paste credentials into chat. OAuth consent does not authorize every write or credit-consuming operation.

Use identifiers returned by actual owned-resource tools or explicitly supplied by the user. Ask when the intended resource or required input is missing. Respect the tool error without fabricating a successful action, changing the requested resource, or starting another job.

Official documentation: https://dokyumi.com/docs/mcp.
