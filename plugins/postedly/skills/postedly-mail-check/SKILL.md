---
name: postedly-mail-check
description: Prepare a mailed paper check from the user’s own ready US checking account through Postedly, with a service-fee quote and private owner proof, signature and payment approval.
---

# Mail a check

Use the existing Postedly OAuth connection at https://postedly.com/mcp/send when the user asks to mail a paper check. Check current availability with `postedly_services`; use the returned `check` entry and current fee. The fee is separate from the check face value: Postedly does not collect or hold that amount, which leaves the checking account when the payee deposits the check.

## Connect the owner’s account

Call `postedly_bank_accounts` with `{}` to read only the connected owner’s masked bank references and readiness. If no ready account exists, give the owner its returned `setupUrl` and next step. They connect their own US checking account and complete ownership, signing-authority, passkey and signature setup in the secure browser. Do not collect account or routing numbers, bank passwords, verification codes, signatures, passkey prompts or recovery codes in chat or a CLI. Connection alone does not approve a check.

If several ready accounts could match, ask the user which masked account to use. Never substitute another owner or guess a bank reference. If a client has not yet exposed the check tools, provide the normal https://postedly.com/checks browser handoff and explain that this client’s tool availability is unconfirmed; do not route a check through document-upload, generic quote or checkout tools.

## Draft the exact check

Obtain the payee’s name and full US mailing address, the exact USD face value and optional memo. Ask only for missing facts. When the user requests preparation, call `postedly_check_draft` with the returned ready `bankRef`, `payee`, integer `amountCents` and optional `memo` (at most 40 characters), following the current schema. The draft allocates a check number and prepares a fee quote and private `reviewUrl`; it does not sign, approve, pay for or send the check. Do not upload a PDF or signature image for this workflow.

Present the payee, masked bank, allocated check number, face value, service fee, tax, total and expiry as actually returned. Make clear that the total is the Postedly fee and tax, not the check’s face value. Give the returned private `reviewUrl` to the owner. They sign in, inspect the full proof and payee/amount/account/check number, complete the required passkey confirmation and signature, and approve and pay the service fee. Never perform their personal authenticator ceremony or infer signing/payment approval from OAuth consent or a chat message.

If a draft or payment response is uncertain, inspect the existing check/order through the normal owned account before attempting another draft. A retry can reserve another check number; do not create a duplicate to recover a missing response. Use a new quote only when its outcome and the user’s intended correction are established.

## Track evidence

Use the existing owned order ID with `postedly_order_status`, or find it using `postedly_orders` and its returned filters/pagination. Distinguish fee payment, provider acceptance, printing, mailing and delivery. None proves that a check was deposited or cleared: Postedly does not track clearing. Do not claim a successful real mailed-check pilot or payment from synthetic tests. The dedicated synthetic reviewer may inspect availability and the setup handoff but must not connect a real bank, sign, pay or send a check.
