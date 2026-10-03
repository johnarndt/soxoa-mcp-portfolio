---
name: dibatto-workflow
description: "Review saved cited podcast rundowns and transcripts and prepare private episode drafts when a user asks for podcast research or episode preparation. Recording and publication remain app-only."
---

Use the connected Dibatto MCP at https://dibatto.com/mcp for the user's requested workflow. Follow the current server tool schemas and owner-scoped resource results.

Read owned shows, cached cited rundowns, saved episodes/transcripts and existing wrap states. Preparing a private episode is not recording or publication. New research/model work requires explicit authorization and current Studio entitlement. Recording, live co-hosting, media upload, wrap generation and publication remain app-only.

Connect the user through the MCP client OAuth flow before accessing their resources. Do not ask them to paste credentials into chat. OAuth consent does not authorize every write or credit-consuming operation.

Use identifiers returned by actual owned-resource tools or explicitly supplied by the user. Ask when the intended resource or required input is missing. Respect the tool error without fabricating a successful action, changing the requested resource, or starting another job.

Official documentation: https://dibatto.com/developers.
