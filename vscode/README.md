# Use Soxoa MCPs in VS Code and GitHub Copilot

Connect one product at a time using its install link, or merge the matching JSON file into your workspace `.vscode/mcp.json`. These files use VS Code's `servers` format, not the portable `mcpServers` format.

Install links open VS Code's review flow. Review the endpoint, trust prompt and any OAuth permissions there. No credentials, pre-approved tools or automatic purchases are included. Account access, subscriptions and processing entitlements remain product-specific.

| Product | VS Code | Configuration | Authentication |
| --- | --- | --- | --- |
| [Soxoa](../plugins/soxoa/README.md) | [Install](https://vscode.dev/redirect/mcp/install?name=soxoa&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fsoxoa.com%2Fmcp%22%7D) | [soxoa.mcp.json](soxoa.mcp.json) | Public planning tools; no account authentication. |
| [MentionedOn](../plugins/mentionedon/README.md) | [Install](https://vscode.dev/redirect/mcp/install?name=mentionedon&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmentioned-on.com%2Fmcp%22%7D) | [mentionedon.mcp.json](mentionedon.mcp.json) | Supplied-evidence tools are public. Connected workspace tools require normal OAuth 2.1 / PKCE consent. |
| [RegSentry](../plugins/regsentry/README.md) | [Install](https://vscode.dev/redirect/mcp/install?name=regsentry&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fregsentry.com%2Fmcp%22%7D) | [regsentry.mcp.json](regsentry.mcp.json) | Public tools; no account authentication. Site inspection still requires the user’s authorization. |
| [Intakra](../plugins/intakra/README.md) | [Install](https://vscode.dev/redirect/mcp/install?name=intakra&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fintakra.com%2Fmcp%22%7D) | [intakra.mcp.json](intakra.mcp.json) | Supplied-evidence tools are public. Connected workspace tools require normal OAuth 2.1 / PKCE consent. |
| [Postedly](../plugins/postedly/README.md) | [Install](https://vscode.dev/redirect/mcp/install?name=postedly&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fpostedly.com%2Fmcp%2Fsend%22%7D) | [postedly.mcp.json](postedly.mcp.json) | OAuth 2.1 / PKCE for connected owner resources. |
| [Portravo](../plugins/portravo/README.md) | [Install](https://vscode.dev/redirect/mcp/install?name=portravo&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fportravo.com%2Fmcp%22%7D) | [portravo.mcp.json](portravo.mcp.json) | OAuth 2.1 / PKCE for connected owner resources. |
| [Dokyumi](../plugins/dokyumi/README.md) | [Install](https://vscode.dev/redirect/mcp/install?name=dokyumi&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fdokyumi.com%2Fmcp%22%7D) | [dokyumi.mcp.json](dokyumi.mcp.json) | OAuth 2.1 / PKCE for connected owner resources. |
| [Afterglow](../plugins/afterglow/README.md) | [Install](https://vscode.dev/redirect/mcp/install?name=afterglow&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapi.withafterglow.com%2Fmcp%22%7D) | [afterglow.mcp.json](afterglow.mcp.json) | OAuth 2.1 / PKCE for connected owner resources. |
| [Dibatto](../plugins/dibatto/README.md) | [Install](https://vscode.dev/redirect/mcp/install?name=dibatto&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fdibatto.com%2Fmcp%22%7D) | [dibatto.mcp.json](dibatto.mcp.json) | OAuth 2.1 / PKCE for connected owner resources. |
| [Ocolta](../plugins/ocolta/README.md) | [Install](https://vscode.dev/redirect/mcp/install?name=ocolta&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapp.ocolta.com%2Fmcp%22%7D) | [ocolta.mcp.json](ocolta.mcp.json) | OAuth 2.1 / PKCE for connected owner resources. |
| [CasaCaddy](../plugins/casacaddy/README.md) | [Install](https://vscode.dev/redirect/mcp/install?name=casacaddy&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapi.casacaddy.com%2Fmcp%22%7D) | [casacaddy.mcp.json](casacaddy.mcp.json) | Use native CasaCaddy Assistant pairing and the normal OAuth connection for the eligible installation. |

## Verify the connection

Use `MCP: Add Server` → HTTP if your browser cannot open an install link. Enter the endpoint from the product guide. Then run `MCP: List Servers` and inspect the server's tools and output. Start with a low-impact read or supplied-evidence review; installation alone does not establish authenticated task completion.

For current Copilot harnesses, the guided flow can offer Global → Copilot Global or a portable workspace configuration. Let VS Code write that format. The files here target the VS Code configuration destination; do not copy the root key unchanged into a portable file.

## Discovery and review

GitHub's curated MCP Registry and the official MCP Registry are separate. All eleven official entries were active and latest when checked on November 2, 2026; none appeared in GitHub's feed. GitHub onboarding has been requested separately; these direct configurations do not imply acceptance or endorsement.

In VS Code, browse the MCP server gallery from the Extensions view with `@mcp`, or use Chat: Open Customizations → Browse → GitHub Feed and `@type:mcp` where available. Preview features, harness support and organization policy affect availability. Search discovery depends on GitHub's curation and feed propagation.

References: [VS Code MCP setup and discovery](https://code.visualstudio.com/docs/agent-customization/mcp-servers), [GitHub curator clarification](https://github.com/github/github-mcp-server/discussions/1257).
