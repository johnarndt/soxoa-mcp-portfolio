# Ocolta MCP integration

Explain categorical document-review signals and prepare neutral human follow-up questions.

## Connection

Endpoint: https://app.ocolta.com/mcp

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 / PKCE for connected owner resources.

Use the client's normal remote-MCP authorization flow. Credentials stay in the client's secure credential store; do not paste them into chat.

## Included workflows

- [ocolta-review-document-signals](skills/ocolta-review-document-signals/SKILL.md): Explain categorical signals from an existing purchased Ocolta document review, compare accessible summaries, or recover a recent result without exposing document text.
- [ocolta-verification-follow-up](skills/ocolta-verification-follow-up/SKILL.md): Prepare neutral human follow-up questions from an Ocolta categorical result or user-described concern, without deciding authenticity or eligibility.

## Example requests

- Explain the categorical signals in my existing review.
- Recover my recent review using the connected purchase.
- Draft neutral follow-up questions for a human reviewer.

## Workflow boundaries

Read only owner-scoped existing review summaries. Preserve categorical signals, confidence and counts without exposing original document text. These are review signals; do not turn them into legal, medical or psychological diagnoses or create a new document assessment through these tools.

Connection does not authorize unrelated writes, paid work, purchases, or communication. Follow the user's actual request and the current server schema. Recover uncertain jobs and orders before starting another.

Documentation: https://app.ocolta.com/workspace/integrations

These MIT-licensed files contain public configuration and skill instructions. Hosted services retain their terms and implementation rights.
