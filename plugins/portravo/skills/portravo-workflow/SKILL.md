---
name: portravo-workflow
description: "Review construction plan takeoff quantities and export reviewed, priced estimates when a user asks to estimate materials from a PDF plan or inspect a saved takeoff."
---

Use the connected Portravo MCP at https://portravo.com/mcp for the user's requested workflow. Follow the current server tool schemas and owner-scoped resource results.

Use the exact uploaded PDF bytes or an actual permitted attachment descriptor. Ask for explicit existing-credit approval before a fresh takeoff. Preserve the documented idempotency key on an uncertain response; a retry is not approval for another job. Quantities and mappings need human review. Export only a reviewed, priced or final estimate as documented.

Connect the user through the MCP client OAuth flow before accessing their resources. Do not ask them to paste credentials into chat. OAuth consent does not authorize every write or credit-consuming operation.

Use identifiers returned by actual owned-resource tools or explicitly supplied by the user. Ask when the intended resource or required input is missing. Respect the tool error without fabricating a successful action, changing the requested resource, or starting another job.

Official documentation: https://portravo.com/developers/mcp.
