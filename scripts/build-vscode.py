#!/usr/bin/env python3
"""Generate credential-free VS Code connection files from the product catalog."""
import json
from pathlib import Path
from urllib.parse import quote, urlencode

ROOT = Path(__file__).resolve().parents[1]


def main():
    products = json.loads((ROOT / "skills-catalog.json").read_text())["products"]
    dest = ROOT / "vscode"
    dest.mkdir(exist_ok=True)
    lines = [
        "# Use Soxoa MCPs in VS Code and GitHub Copilot", "",
        "Connect one product at a time using its install link, or merge the matching JSON file into your workspace `.vscode/mcp.json`. These files use VS Code's `servers` format, not the portable `mcpServers` format.", "",
        "Install links open VS Code's review flow. Review the endpoint, trust prompt and any OAuth permissions there. No credentials, pre-approved tools or automatic purchases are included. Account access, subscriptions and processing entitlements remain product-specific.", "",
        "| Product | VS Code | Configuration | Authentication |",
        "| --- | --- | --- | --- |",
    ]
    for p in products:
        slug = p["slug"]
        config = {"type": "http", "url": p["endpoint"]}
        (dest / f"{slug}.mcp.json").write_text(json.dumps({"servers": {slug: config}}, indent=2) + "\n")
        link = "https://vscode.dev/redirect/mcp/install?" + urlencode({
            "name": slug, "config": json.dumps(config, separators=(",", ":"))
        }, quote_via=quote)
        lines.append(f"| [{p['name']}](../plugins/{slug}/README.md) | [Install]({link}) | [{slug}.mcp.json]({slug}.mcp.json) | {p['authDescription']} |")
    lines += ["", "## Verify the connection", "",
              "Use `MCP: Add Server` → HTTP if your browser cannot open an install link. Enter the endpoint from the product guide. Then run `MCP: List Servers` and inspect the server's tools and output. Start with a low-impact read or supplied-evidence review; installation alone does not establish authenticated task completion.", "",
              "For current Copilot harnesses, the guided flow can offer Global → Copilot Global or a portable workspace configuration. Let VS Code write that format. The files here target the VS Code configuration destination; do not copy the root key unchanged into a portable file.", "",
              "## Discovery and review", "",
              "GitHub's curated MCP Registry and the official MCP Registry are separate. All eleven official entries were active and latest when checked on November 2, 2026; none appeared in GitHub's feed. GitHub onboarding has been requested separately; these direct configurations do not imply acceptance or endorsement.", "",
              "In VS Code, browse the MCP server gallery from the Extensions view with `@mcp`, or use Chat: Open Customizations → Browse → GitHub Feed and `@type:mcp` where available. Preview features, harness support and organization policy affect availability. Search discovery depends on GitHub's curation and feed propagation.", "",
              "References: [VS Code MCP setup and discovery](https://code.visualstudio.com/docs/agent-customization/mcp-servers), [GitHub curator clarification](https://github.com/github/github-mcp-server/discussions/1257).", ""]
    (dest / "README.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
