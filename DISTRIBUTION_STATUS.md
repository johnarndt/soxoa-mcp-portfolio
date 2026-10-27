# Distribution status — 2026-10-27

Source and the [versioned release archives](https://github.com/johnarndt/soxoa-mcp-portfolio/releases/tag/agent-skills-2026-10-27) are public. The release contains 29 customer workflow skills across eleven products and the separate 15-skill Soxoa Ops package. Source publication and downloadable packages do not establish platform review approval or search discovery.

## OpenAI directory

The following states were observed in the Soxoa organization’s submission portal on 2026-10-27. Nine updated submissions covering 22 customer skills are in review. ChatGPT and Codex share the public directory; review does not establish approval.

| Product | Version | Observed state |
| --- | --- | --- |
| Soxoa | 1.2.1 | In review |
| Intakra | 1.2.2 | In review |
| MentionedOn | 1.2.1 | In review |
| RegSentry | 1.2.1 | In review |
| Portravo | 1.1.1 | In review |
| Ocolta | 1.0.3 | In review |
| Dibatto | 1.0.6 | In review |
| Dokyumi | 1.1.2 | In review |
| Afterglow | 1.0.6 (`afterglow-checklists`) | In review; canonical entry configured |
| Postedly | 1.2.4 | Existing In review entry preserved |
| CasaCaddy | 1.0.3 | Existing In review, Configured entry preserved |
| Soxoa Ops | 0.2.0 | Draft saved; all 15 skill checks passed; intake blocked |

Earlier Dokyumi and Afterglow draft attempts returned “The attached app is not eligible for review”. Dokyumi 1.1.2 has since entered review. Afterglow required a new OpenAI entry after the portal instructed “Create a new plugin to change MCP servers”. The new entry is `afterglow-checklists` 1.0.6, display name Afterglow, server key `afterglow-api`, technical ID `plugin_asdk_app_6ae0f64a661c8191a817385b15c81c5a`. Its MCP resource is `https://api.withafterglow.com/mcp`; it is configured and in review after ownership verification, dedicated OAuth authorization, three-tool discovery and skill checks. The earlier Afterglow 1.0.4 entry remains Unavailable/Configured and retained. Postedly 1.3.1 and CasaCaddy 1.0.5 ZIPs are public; they do not replace the earlier reviews listed above.

Soxoa Ops submission returned “We are not accepting more skills-only submissions at this time.” Its public source and ZIP remain available independently of that intake restriction. No directory approval is claimed for the Ops draft.

## Hermes and direct installation

Native Hermes direct-tap checks passed for all 29 customer skills. This verifies the tested skill discovery/install path, not a fresh customer OAuth connection or paid fulfillment.

[Hermes catalog PR #145658](https://github.com/NousResearch/hermes-agent/pull/145658) proposes Postedly, MentionedOn and Intakra. It is pending maintainer review and merge. The direct setup in the [README](README.md#hermes) is available while the proposal is pending; the proposal is not Nous approval.

The Postedly Gemini CLI extension and direct MCP configurations are also public. Gallery indexing, normal account acceptance and paid delivery remain separate checks. This dated snapshot does not promise rankings, recommendations or signups.

The native/Claude Afterglow plugin remains `afterglow` 1.0.5. The OpenAI identity override in `platform-packages.json` keeps future archives aligned with the new entry. The public OpenAI-format companion is sanitized; private reviewer cases and credentials are not distributed. Earlier release assets remain unchanged.
