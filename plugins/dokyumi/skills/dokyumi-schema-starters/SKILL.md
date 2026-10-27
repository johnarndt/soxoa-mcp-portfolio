---
name: dokyumi-schema-starters
description: "Choose a saved Dokyumi extraction schema or preview and save a document workflow starter with the user’s agreement."
---

# Choose a document schema

Use the connected service at https://dokyumi.com/mcp through normal OAuth. Documentation: https://dokyumi.com/docs/mcp. `dokyumi_account` identifies the connected organization and `dokyumi_list_schemas` lists its actual active saved definitions. Start from the fields the user wants and their real document type.

If no suitable schema exists, `dokyumi_list_starters` searches published workflow starters by use case or supported category and returns fields, review checks and explicitly synthetic examples. A starter’s example data is not extracted user data or evidence that the workflow will be accurate on their document. Show the relevant fields and review checks before saving.

Once the user agrees to save, use `dokyumi_save_starter` with the actual workflow_slug and confirm_create=true. Saving needs `dokyumi:schemas:write`; browsing uses `dokyumi:read`. Existing authorization counts; do not repeat an already answered confirmation. Use the normal additional-consent flow when needed.

A matching slug is reused without overwriting owner edits, so inspect the returned definition. A full allowance or inactive schema needs the supported schema-management handoff; do not replace another schema or invent a slug. Choosing, previewing and saving do not upload a document, use extraction credits or start BYOK processing. Extraction requires its own processing preflight and any missing spend authorization.
