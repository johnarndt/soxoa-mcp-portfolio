# Dokyumi MCP integration

Prepare saved extraction schemas, preflight exact documents and processing charges, and review or export owned results.

## Connection

Endpoint: https://dokyumi.com/mcp

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 / PKCE for connected owner resources.

Use the client's normal remote-MCP authorization flow. Credentials stay in the client's secure credential store; do not paste them into chat.

## Included workflows

- [dokyumi-schema-starters](skills/dokyumi-schema-starters/SKILL.md): Choose a saved Dokyumi extraction schema or preview and save a document workflow starter with the user’s agreement.
- [dokyumi-extract-document](skills/dokyumi-extract-document/SKILL.md): Preflight an authorized document and saved Dokyumi schema, distinguish subscription credits from BYOK provider charges, and extract exact file bytes for source review.
- [dokyumi-review-export](skills/dokyumi-review-export/SKILL.md): Find saved Dokyumi extractions and exceptions, review uncertain fields, and export selected existing results as CSV or Excel.

## Example requests

- Help me choose a saved schema for this document.
- Check the processing mode, cost authorization and limits before extraction.
- Review uncertain fields and export my existing extraction.

## Workflow boundaries

Preflight before processing. Distinguish existing subscription credits from separate BYOK provider charges and obtain the applicable authorization. Preserve exact source bytes, schema and request key, review uncertain fields, and respect storage and retention limits.

Connection does not authorize unrelated writes, paid work, purchases, or communication. Follow the user's actual request and the current server schema. Recover uncertain jobs and orders before starting another.

Documentation: https://dokyumi.com/docs/mcp

These MIT-licensed files contain public configuration and skill instructions. Hosted services retain their terms and implementation rights.
