---
name: casacaddy-workflow
description: "Read maintenance guide requirements, prepare confirmed guides and report saved job status when a user asks how to maintain home equipment or check a guide request."
---

Use the connected CasaCaddy MCP at https://api.casacaddy.com/mcp for the user's requested workflow. Follow the current server tool schemas and owner-scoped resource results.

Read the maintenance requirements and account/device-owned guide job. Ask for confirmation before preparing a guide, preserve the request key on a retry, and report its actual queued, processing, failed or completed state. Guide preparation is not evidence the maintenance work was performed.

Connect the user through the MCP client OAuth flow before accessing their resources. Do not ask them to paste credentials into chat. OAuth consent does not authorize every write or credit-consuming operation.

Use identifiers returned by actual owned-resource tools or explicitly supplied by the user. Ask when the intended resource or required input is missing. Respect the tool error without fabricating a successful action, changing the requested resource, or starting another job.

Official documentation: https://api.casacaddy.com/developers.
