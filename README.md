# Soxoa MCP portfolio

Public first-party connection configurations and workflow skills for eleven Soxoa LLC products. Each plugin has its own hosted endpoint, documentation, privacy/terms links, owner-aware workflow instructions and truthful account requirements.

| Product | Remote MCP endpoint | Authentication |
| --- | --- | --- |
| [Soxoa](plugins/soxoa/README.md) | `https://soxoa.com/mcp` | No auth |
| [MentionedOn](plugins/mentionedon/README.md) | `https://mentioned-on.com/mcp` | No auth |
| [RegSentry](plugins/regsentry/README.md) | `https://regsentry.com/mcp` | No auth |
| [Intakra](plugins/intakra/README.md) | `https://intakra.com/mcp` | No auth |
| [Postedly](plugins/postedly/README.md) | `https://postedly.com/mcp/send` | OAuth 2.1 / PKCE |
| [Portravo](plugins/portravo/README.md) | `https://portravo.com/mcp` | OAuth 2.1 / PKCE |
| [Dokyumi](plugins/dokyumi/README.md) | `https://dokyumi.com/mcp` | OAuth 2.1 / PKCE |
| [Afterglow](plugins/afterglow/README.md) | `https://afterglow-lime.vercel.app/mcp` | OAuth 2.1 / PKCE |
| [Dibatto](plugins/dibatto/README.md) | `https://dibatto.com/mcp` | OAuth 2.1 / PKCE |
| [Ocolta](plugins/ocolta/README.md) | `https://app.ocolta.com/mcp` | OAuth 2.1 / PKCE |
| [CasaCaddy](plugins/casacaddy/README.md) | `https://api.casacaddy.com/mcp` | OAuth 2.1 / PKCE |

All endpoints use Streamable HTTP. Compatible clients normally call that transport `http`. Use the individual plugin's `.mcp.json` or its official documentation. The first four integrations expose public read-only planning/evidence tools; the remaining seven use OAuth and connected owner permissions for account operations.

These files include no hosted application source, private accounts, credentials, payment keys, internal reviewer cases, recordings, or test fixtures. Installation does not authorize arbitrary writes, paid processing or purchases. Server capabilities and plan entitlements remain authoritative.

The local marketplace index is `.claude-plugin/marketplace.json`; individual plugin folders are under `plugins/`. A live source repository is established during the authorized distribution release. Directory review and search discovery depend on their maintainers and do not guarantee recommendations.

MIT applies to these distribution files. Hosted services retain their product terms and implementation rights.
