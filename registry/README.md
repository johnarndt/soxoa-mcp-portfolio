# Official MCP Registry metadata

These files describe the existing first-party registry namespaces. The November 2, 2026 metadata refresh preserves namespaces and older immutable versions, and updates six stale entries to describe their current supported workflows. No hosted application code or secret is included.

Afterglow now points to `https://api.withafterglow.com/mcp` and its canonical developer documentation. Version 1.0.2 is a registry metadata revision; its hosted MCP initialize version remains 1.0.1. The other five refreshed records use the currently advertised MCP server version. Registry versions and client plugin package versions need not be equal.

Review a server's live initialize/tools list, documentation, authentication and ownership before revising its metadata. Validate against the declared official schema and publish with the existing namespace ownership identity. Never include signing keys or bearer tokens in this repository. Confirm exact version and latest-version readback after publication. Registry ingestion is distinct from approval or discovery in downstream curated stores.
