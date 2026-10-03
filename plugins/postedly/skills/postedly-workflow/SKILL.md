---
name: postedly-workflow
description: "Prepare quotes for available handwritten cards, open private review links and read owned order status when a user asks to prepare or check physical correspondence. Payment and sending require separate browser approval."
---

Use the connected Postedly MCP at https://postedly.com/mcp/send for the user's requested workflow. Follow the current server tool schemas and owner-scoped resource results.

Read the live service and card catalog first. Only handwritten cards are currently available. Quoting, document intake and opening private review do not send, charge, or approve payment. Card samples are not a rendered proof of the user's exact message. Payment requires the user's explicit browser review. Report payment and fulfillment separately.

Connect the user through the MCP client OAuth flow before accessing their resources. Do not ask them to paste credentials into chat. OAuth consent does not authorize every write or credit-consuming operation.

Use identifiers returned by actual owned-resource tools or explicitly supplied by the user. Ask when the intended resource or required input is missing. Respect the tool error without fabricating a successful action, changing the requested resource, or starting another job.

Official documentation: https://postedly.com/developers.
