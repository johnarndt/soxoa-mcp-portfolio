# Soxoa MCP portfolio

Public first-party connection configurations and workflow skills for eleven Soxoa LLC products. Each plugin has its own hosted endpoint, documentation, privacy/terms links, owner-aware workflow instructions and truthful account requirements.

| Product | Remote MCP endpoint | Authentication |
| --- | --- | --- |
| [Soxoa](plugins/soxoa/README.md) | `https://soxoa.com/mcp` | No auth |
| [MentionedOn](plugins/mentionedon/README.md) | `https://mentioned-on.com/mcp` | Public evidence; OAuth for connected business tools |
| [RegSentry](plugins/regsentry/README.md) | `https://regsentry.com/mcp` | No auth |
| [Intakra](plugins/intakra/README.md) | `https://intakra.com/mcp` | Public evidence; OAuth for workspace tools |
| [Postedly](plugins/postedly/README.md) | `https://postedly.com/mcp/send` | OAuth 2.1 / PKCE |
| [Portravo](plugins/portravo/README.md) | `https://portravo.com/mcp` | OAuth 2.1 / PKCE |
| [Dokyumi](plugins/dokyumi/README.md) | `https://dokyumi.com/mcp` | OAuth 2.1 / PKCE |
| [Afterglow](plugins/afterglow/README.md) | `https://api.withafterglow.com/mcp` | OAuth 2.1 / PKCE |
| [Dibatto](plugins/dibatto/README.md) | `https://dibatto.com/mcp` | OAuth 2.1 / PKCE |
| [Ocolta](plugins/ocolta/README.md) | `https://app.ocolta.com/mcp` | OAuth 2.1 / PKCE |
| [CasaCaddy](plugins/casacaddy/README.md) | `https://api.casacaddy.com/mcp` | OAuth 2.1 / PKCE |

All endpoints use Streamable HTTP. Compatible clients normally call that transport `http`. Use the individual plugin's `.mcp.json` or its official documentation. Soxoa and RegSentry provide public tools. MentionedOn and Intakra combine public supplied-evidence tools with OAuth account workflows. Other products require their normal owner or installation connection; consult the product guide for current entitlements.

These files include no hosted application source, private accounts, credentials, payment keys, internal reviewer cases, recordings, or test fixtures. Installation does not authorize arbitrary writes, paid processing or purchases. Server capabilities and plan entitlements remain authoritative.

The local marketplace index is `.claude-plugin/marketplace.json`; individual plugin folders are under `plugins/`. The [complete skill list](SKILLS.md) contains 30 customer outcome skills across all eleven products and a separate 15-skill Soxoa Ops package. Directory review and search discovery depend on their maintainers and do not guarantee recommendations.

## Distribution status

Postedly 1.4.0 source adds the paper-check preparation workflow and preserves all six earlier skills. Its current ZIPs are prepared locally; upload, review and publication states require their own release or portal receipts. Bank connection, passkeys, signature and fee payment stay in the owner’s browser, and Postedly does not track check clearing.

The source and [versioned ZIP packages](https://github.com/johnarndt/soxoa-mcp-portfolio/releases/tag/agent-skills-2026-10-27) are public. OpenAI review, blocked drafts and curated catalog proposals have separate states; see the [dated distribution status](DISTRIBUTION_STATUS.md) before treating a package as approved.

## Hermes

Hermes can install the standalone skills from this public GitHub tap. This is separate from the OpenClaw plugin bundles.

```sh
hermes skills tap add johnarndt/soxoa-mcp-portfolio
hermes skills search postedly --source github
hermes skills install johnarndt/soxoa-mcp-portfolio/skills/postedly-mail-letter
```

Connect the product through Hermes's native MCP OAuth flow as a separate step:

```sh
hermes mcp add postedly --url https://postedly.com/mcp/send --auth oauth
hermes mcp login postedly
```

The [Hermes catalog submission](https://github.com/NousResearch/hermes-agent/pull/145658) proposes Postedly, MentionedOn and Intakra. It requires maintainer review and merge; publication of this repository is not Nous approval. Add custom servers by URL while review is pending. Never place tokens in a skill or chat.

## Gemini CLI

[Postedly for Gemini CLI](https://github.com/johnarndt/postedly-gemini-extension) packages five task skills and its native remote MCP connection:

```sh
gemini extensions install https://github.com/johnarndt/postedly-gemini-extension
```

Native package validation passed; authenticated task completion and gallery indexing are tracked separately.

## Build packages

```sh
python3 scripts/build-distribution.py --output /tmp/soxoa-product-packages
```

For a single product, add `--only afterglow`. When an OpenAI entry has a different package identity, `platform-packages.json` preserves its plugin name, version and MCP server key separately from the native plugin.

This builds public plugin archives without network calls. Existing platform submissions and reviewed versions are separate from these new source packages.

## Practical workflow evaluation guides

[2027 planning guides and editable checklists](resources/2027/README.md) cover selecting an automation pilot, measuring AI visibility, reviewing account buying evidence, checking a complete construction takeoff and approving agent-assisted physical correspondence. Each explains the evidence to collect before relying on an output. These resources are published by Soxoa, which operates the products discussed.

MIT applies to these distribution files. Hosted services retain their product terms and implementation rights.
