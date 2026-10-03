---
name: ocolta-workflow
description: "Summarize existing categorical document-review signals, confidence and indicator counts when a user asks to inspect a saved assessment. Excludes new analysis or diagnosis."
---

Use the connected Ocolta MCP at https://app.ocolta.com/mcp for the user's requested workflow. Follow the current server tool schemas and owner-scoped resource results.

Read only owner-scoped existing review summaries. Preserve categorical signals, confidence and counts without exposing original document text. These are review signals; do not turn them into legal, medical or psychological diagnoses or create a new document assessment through these tools.

Connect the user through the MCP client OAuth flow before accessing their resources. Do not ask them to paste credentials into chat. OAuth consent does not authorize every write or credit-consuming operation.

Use identifiers returned by actual owned-resource tools or explicitly supplied by the user. Ask when the intended resource or required input is missing. Respect the tool error without fabricating a successful action, changing the requested resource, or starting another job.

Official documentation: https://app.ocolta.com/workspace/integrations.
