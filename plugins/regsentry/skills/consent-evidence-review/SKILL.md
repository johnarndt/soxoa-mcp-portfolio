---
name: consent-evidence-review
description: Use when a user wants to inspect an authorized public site's static tracking signals, grade consent evidence, or obtain a tracker remediation playbook.
---

# RegSentry consent evidence review

Use RegSentry as a technical evidence aid, not a legal compliance authority.

- Call `inspect_site_tracking` only after the user confirms they own or are authorized to test the public domain.
- Treat a static inspection as an observation; it does not prove whether runtime tracking fired before or after consent.
- Use `interpret_consent_evidence` for redacted, caller-supplied observations.
- Use `get_remediation_playbook` for reviewable guidance; it does not change a website or verify a fix.
- Never characterize a result as legal advice, a compliance certification, or a liability determination.
