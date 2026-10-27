---
name: casacaddy-plan-home-maintenance
description: "Get bounded maintenance guidance for user-described appliances through a paired CasaCaddy installation, recover a saved guide, or choose a safe next task."
---

Use CasaCaddy at https://api.casacaddy.com/mcp through its supported pairing and OAuth flow. Documentation: https://api.casacaddy.com/developers.



# Plan home maintenance

Start with the actual item and the user's question. Ask only for missing category, brand or model details needed by `get_maintenance_guide`; do not claim access to the phone's appliance library, photos or task schedule. The connection reads user-supplied item details and its own saved guide requests.

Use `get_connected_installation` for the paired installation and current allowance. If pairing is missing, direct the user to CasaCaddy 1.0.1 or later → Settings → Connected tools → Assistant pairing, then the normal browser consent flow. Active eligible product access is required. Do not ask the user to paste pairing codes, installation secrets or payment details into chat.

Use `get_maintenance_guide` only after the user's request authorizes use of existing allowance. Preserve the same request key and exact item/question on a retry. After an uncertain response, recover with `get_saved_guide_request`; do not start another guide. Report the actual saved result and keep its cautions, professional-help boundaries and scope limits.

Honor a visual-only or non-disassembly request in both the tool question and the final guidance. If returned steps exceed that boundary, identify and exclude them from the proposed action rather than treating them as approved. A guide is not a diagnosis or proof that equipment is safe.

Saved MCP requests are recoverable for up to 30 days. Exact-input cached guides can be unmetered; use the returned allowance and status rather than assuming a fresh charge. For return use, recover the known saved request and help choose the next safe action. If the user does not have a request key, explain that this connection cannot list the phone's library or all past guides. A conversation plan does not create a CasaCaddy schedule or reminders.
