---
name: dokyumi-extract-document
description: "Preflight an authorized document and saved Dokyumi schema, distinguish subscription credits from BYOK provider charges, and extract exact file bytes for source review."
---

# Extract an authorized document

Use https://dokyumi.com/mcp through normal OAuth. If unavailable, retain the document and schema choice and provide https://dokyumi.com/docs/mcp. Use `dokyumi_account` and `dokyumi_list_schemas` to select the actual connected organization and active schema; no suitable schema gets a starter or app handoff rather than an invented definition.

Call `dokyumi_preflight_extraction` with the saved schema_slug and actual page count when known. Preserve returned processing mode, access, page and schema limits, storage availability and credential errors. Preflight does not reserve credits or start work. A lifetime extraction count is not an available balance.

Subscription workspaces use existing credits: obtain any missing authorization for the actual document and applicable credit cost before setting use_existing_credits=true. Current policy uses one credit per up-to-five pages within the account page limit. BYOK lifetime workspaces have no monthly extraction cap and incur separate OpenRouter processing charges: first preflight, disclose that mode, obtain authorization for those provider charges, and set confirm_provider_charges=true. Do not treat existing-credit consent as BYOK consent, purchase credits, top up a key or silently switch processing mode. An already explicit user authorization counts for the agreed work.

Use exactly one of the host-provided file descriptor or file_inline. Native signed attachment transfer requires a real download_url and file_id; never invent either. The inline fallback is canonical base64 computed from the exact selected bytes, at most 32 KiB, with original filename and supported MIME type. Follow current workspace transfer and storage limits; use the product upload handoff when the host cannot transfer. BYOK supports PDF, JPEG, PNG and WebP, subject to storage limits and 30-day originals/results retention. Do not assume every MIME type accepted by the shared schema is available in every processing mode.

Call `dokyumi_extract_document` only for the authorized exact file and schema, preserving request_key across an uncertain result or retry. Processing is not completion: inspect `dokyumi_list_extractions` or the returned existing extraction with `dokyumi_get_extraction`, rather than changing keys and starting another paid job.

Review actual fields, confidence, validation and quality-receipt availability against the source when accessible. Highlight uncertain or invalid fields. Completion and confidence do not establish correctness or authenticity; do not fabricate quotations, source pages, or a business decision.
