---
name: soxoa-ops-signup-pulse
description: "Review signup progress or implement requested owner alerts and digests using authorized product data and reliable delivery recovery."
---

# Review or implement a signup pulse

Match the requested task: a read-only signup report, a funnel review, or an implementation of owner notifications. A request to report who signed up does not authorize backend edits or new email sending. When implementation is requested, use the named repository, existing operational rules and authorized test environment; preserve any prior approval without asking for it again.

Use only owned product data the user authorized. Define the period, timezone, journey stages and useful identifiers. Derive each person’s furthest confirmed stage and latest meaningful activity from actual records; missing analytics is unknown. Separate verified users, likely bots and uncertain classifications with their basis. Do not infer a person is a bot merely because they stopped onboarding.

For an instant owner alert, cover account creation rather than only onboarding. When controlling the database write, persist a stable outbox event atomically in the same transaction as the user record; dispatch only after commit. For an external auth or webhook source, durably record its stable event ID and reconcile against actual accounts to backfill missed events. Sending must not block signup. Use the existing queue or outbox with retry state and an acknowledged delivery outcome. A unique claimed row alone is not proof of sending: a crash before delivery must leave a retryable event. Use provider idempotency where available; after an uncertain provider response reconcile before resending to avoid duplicate alerts. A backstop checks due undelivered events, not just events lacking a claim. Report the true guarantee when the provider cannot support exactly-once delivery.

Keep alerts minimal and directed only to the authorized owner destination: relevant account identifier, signup time/source when known and a private admin link. Customer-facing outreach and retargeting are separate requests. Do not include passwords, payment data or private message contents. Test with designated fixtures and approved owner/test destinations; do not send to real signups to prove a notification works.

For a digest, show people and confirmed journey progress before aggregates. Define inactivity thresholds with the user or state a revisable assumption; inactivity is a triage flag, not a verified cause. Respect empty-day preferences and query efficiently without unnecessarily waking sleeping systems. A recurring email needs the actual requested schedule and supported mail/automation path; never claim it exists from a draft specification.

For a funnel review, start with available authorized records and public screens. Create an account or test transaction only within the agreed test scope. Record reached/passed counts with denominators, observation dates and evidence. Keep reproduced blockers separate from hypotheses about why someone stopped. Inspect desktop and phone layouts when tools allow; source inspection alone does not prove the live journey.

Return the requested report or tested implementation plus remaining coverage gaps. For implementation, exercise meaningful delivery recovery, duplicate-event and provider-failure cases in isolation. Follow product release procedures before any deploy. When required tools/access are unavailable, deliver a concrete setup or test plan rather than claiming alerts, dashboards or scheduled jobs were installed.
