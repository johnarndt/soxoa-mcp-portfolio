---
name: postedly-saved-correspondence
description: "Save or reuse private Postedly contacts and correspondence drafts, find prior orders, or export recorded delivery evidence."
---

Use the connected service at https://postedly.com/mcp/send. If unavailable, provide https://postedly.com/developers for normal OAuth setup. Saving and deleting use the exact record and current version; restarting a draft does not approve payment.



# Reuse correspondence safely

Use normal Postedly OAuth. New saved-contact and draft permissions require consent; existing tokens do not silently gain access. Never ask for verification codes or credentials in conversation.

For first use, read `postedly_services` for current availability and required service details. Automated preparation covers fax, letters, certified letters, postcards and handwritten cards only when currently available. A manual quote link is a browser handoff, not a new automated channel.

Use `postedly_contacts` and `postedly_drafts` with a specific key or search and paginate with returned nextOffset. Empty lists are valid. Save only when the user requests storage: `postedly_save_contact` or `postedly_save_draft` needs a chosen key, label, exact details and confirmedSave=true. expectedVersion=0 creates; updating requires the version just read. An identical retry reuses the record. On a version conflict, reread and reconcile instead of overwriting blindly.

Contacts are retained one year after their last save; drafts 30 days. A PDF can expire before its draft. A saved address is not verified deliverability, and a draft is not a quote, approval or order. Read the draft, recheck live service availability and PDF ownership/expiry, then make a new exact quote and private browser review link. The person approves payment in Postedly. Do not infer payment approval from a request to save or resume a draft.

Use `postedly_orders` filters and pagination to locate the owned order before `postedly_order_status`. `postedly_delivery_report` returns plain-text file content and available provider evidence; save privately when requested. Distinguish payment, acceptance, transmission and delivery. Do not call a provider milestone legal proof or independent receipt confirmation.

Delete only the exact contact or draft the user requests using confirmedDelete=true and its current expectedVersion. Deletion does not cancel delivery or change an existing order. On uncertain paid actions, check existing orders before continuing; never create duplicate orders to recover a timeout.
