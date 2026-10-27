---
name: dokyumi-review-export
description: "Find saved Dokyumi extractions and exceptions, review uncertain fields, and export selected existing results as CSV or Excel."
---

# Review and export saved extraction data

Use the connected service at https://dokyumi.com/mcp with normal OAuth `dokyumi:read` access. Documentation: https://dokyumi.com/docs/mcp. `dokyumi_account` identifies the intended organization. Reading and exporting existing results do not start extraction or incur extraction credits or provider processing charges.

Use `dokyumi_list_extractions` with actual filename/query, schema, status or review_only=true. Follow returned pagination. Empty, expired or failed records are valid outcomes; do not invent history or treat a failure as a clean document. Retention and ownership determine what is recoverable.

Read selected records with `dokyumi_get_extraction`. Preserve extracted fields, confidence, validation errors and quality-receipt availability. Compare material or uncertain values with source bytes when accessible; never invent a quotation or page reference. Data requiring review remains unverified even when exported. Reading it does not correct a field, mark it verified, prove authenticity or authorize a lending, employment or other consequential decision.

`dokyumi_export_extractions` accepts 1–50 distinct completed or review-needed extraction IDs and csv or xlsx. Use the actual returned download link, opened while signed into the same Dokyumi browser account; ownership is checked again. Nested values remain JSON text. Reduce an oversized selection when the 5 MiB export limit is exceeded, without silently truncating fields. A download link is not proof the file was downloaded; preserve any sign-in handoff.

Recover the same request or saved result after an uncertain response. Do not retry a failed extraction, change request keys, buy credits or approve BYOK charges to satisfy a read/export request.
