# Postedly MCP integration

Prepare correspondence and owner-funded paper checks with private browser approval; track orders and reuse saved correspondence.

## Connection

Endpoint: https://postedly.com/mcp/send

Transport: Streamable HTTP (client config type `http`).

OAuth 2.1 / PKCE for connected owner resources.

Use the client's normal remote-MCP authorization flow. Credentials stay in the client's secure credential store; do not paste them into chat.

## Included workflows

- [postedly-saved-correspondence](skills/postedly-saved-correspondence/SKILL.md): Save or reuse private Postedly contacts and correspondence drafts, find prior orders, or export recorded delivery evidence.
- [postedly-track-orders](skills/postedly-track-orders/SKILL.md): Check existing Postedly orders and explain recorded payment, fulfillment, and delivery evidence. Use for order status, a missing confirmation, or an uncertain send; do not create a replacement order or infer a receipt from a quote.
- [postedly-fax-document](skills/postedly-fax-document/SKILL.md): Fax the user’s actual finished PDF to one supported US number through Postedly, with final proof, quote and separate browser approval.
- [postedly-mail-letter](skills/postedly-mail-letter/SKILL.md): Write and mail a finished letter or mail an existing PDF through Postedly, including supported US certified mail with tracking and browser review.
- [postedly-send-postcard](skills/postedly-send-postcard/SKILL.md): Prepare two-sided postcard artwork from Postedly’s live template and obtain a quote and private browser approval for one US recipient.
- [postedly-handwritten-card](skills/postedly-handwritten-card/SKILL.md): Choose an available Postedly card and handwriting style, prepare the exact message and closing, and obtain private review and payment approval.
- [postedly-mail-check](skills/postedly-mail-check/SKILL.md): Prepare a mailed paper check from the user’s own ready US checking account through Postedly, with a service-fee quote and private owner proof, signature and payment approval.

## Example requests

- Prepare a quote and private review link for mailing this finished PDF.
- Help me connect my own checking account and prepare a check for private review. Do not sign, pay or mail it.
- Check whether my existing order was paid, sent and delivered.

## Workflow boundaries

Check postedly_services or the live catalog before quoting fax, letters, certified mail, postcards, handwritten cards or checks; availability is determined by the current response. Check the product catalog for handwritten cards. Use the connected OAuth owner and the actual intended document: preserve provided PDF bytes unless changes were requested; finish and inspect every page of a newly requested letter before upload. Intentional forms and test documents remain valid when requested. Review every page of the final proof; card samples are not a rendered proof of the exact message. Uploading, quoting and opening private review do not approve, charge or send. Payment requires the user's explicit browser review. Report payment and fulfillment separately. The object beta uses a separate manual request and is not an automated document order. For checks, use only masked ready bank references with postedly_bank_accounts and postedly_check_draft; owner bank connection, verification, passkeys, signatures and full-proof approval stay in the secure browser. Never collect bank numbers, credentials or signatures in chat or CLI input. Check face value is separate from the service fee and tax; Postedly does not track clearing. The dedicated synthetic reviewer stops before real bank enrollment, signing, payment or fulfillment.

Connection does not authorize unrelated writes, paid work, purchases, or communication. Follow the user's actual request and the current server schema. Recover uncertain jobs and orders before starting another.

Documentation: https://postedly.com/developers

These MIT-licensed files contain public configuration and skill instructions. Hosted services retain their terms and implementation rights.
