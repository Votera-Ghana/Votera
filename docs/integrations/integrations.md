# Votera — External Integrations

## Resend — Email

Purpose:
- account verification
- password reset
- election notifications
- vote confirmation

Integration rule:
Resend is called by the backend.

## Paystack — Payments

Purpose:
- payment initialization
- payment verification
- payment webhooks

Integration rule:
Payment secrets stay on the backend.

## Hubtel — SMS

Purpose:
- OTP
- SMS notifications
- vote confirmation

Integration rule:
SMS operations are handled by the backend service layer.

## Integration Failure Rule

External service failure must not corrupt core voting records.

For example, if an email fails after a vote succeeds, the vote remains valid and the notification can be retried separately.
