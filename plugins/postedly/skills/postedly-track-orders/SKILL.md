---
name: postedly-track-orders
description: "Check existing Postedly orders and explain recorded payment, fulfillment, and delivery evidence. Use for order status, a missing confirmation, or an uncertain send; do not create a replacement order or infer a receipt from a quote."
---

Use https://postedly.com/mcp/send through the existing owner’s normal OAuth connection. Documentation: https://postedly.com/developers. If no connected service is available, preserve the known order and provide the setup handoff; do not invent a status.



# Track orders

Reuse the connected Postedly account. If the user supplies an order ID, call `postedly_order_status` with that `orderId`. Otherwise call `postedly_orders` with `{"limit":20,"offset":0}` and identify the intended order from returned recipient, service, date, and amount. Ask the user to choose if several match. Use returned filters and nextOffset pagination when needed. A page contains up to 50 matching owned orders; absence from one page is not proof that no order exists.

When requested, `postedly_delivery_report` returns private plain-text content and available provider evidence for the actual owned order. Save or share it only within the user’s requested scope. Report the order ID, latest recorded payment and fulfillment states, and relevant timeline or provider evidence. Keep their meanings separate:

- A quote, uploaded document, or private review link is preparation, not an order or payment.
- Payment authorization or successful payment does not establish provider acceptance, dispatch, or delivery.
- Submitted, queued, processing, and unknown states do not prove delivery. Say sent or delivered only when the returned record supports that claim.
- Fax delivery concerns transmission to the receiving machine, not whether a person read it. Postal milestones reflect the provider evidence returned; do not infer a signature or return receipt.

Use `receiptEmail` only as the recorded receipt destination. It does not prove an email arrived. Share an existing checkout or tracking link only when returned or already verified; never construct a payment receipt, tracking number, or missing success evidence.

If access is denied or the order is absent, explain that this connection cannot confirm it. Use the intended account or a known order link; do not switch identities, expose another person's records, or create a replacement send. For expired authentication, let the client refresh or reconnect normally. A failed status request leaves the outcome unknown.

After a timeout or uncertain payment/send, check the existing order before retrying anything. Report unresolved uncertainty and the last confirmed state. These tools read recorded status; they do not themselves retry fulfillment, cancel, refund, or contact the recipient.

If the user asks to cancel, report any returned canCancel value as a snapshot, not a guarantee. These tools do not cancel. Give the actual order page at https://postedly.com/orders or https://postedly.com/support with the known order ID; cancellation is confirmed only by the recorded state.
