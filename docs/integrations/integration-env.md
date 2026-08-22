# Votera — Integration Environment Variables

## Supabase

```text
SUPABASE_URL=
SUPABASE_KEY=
```

## Resend

```text
RESEND_API_KEY=
```

## Paystack

```text
PAYSTACK_SECRET_KEY=
PAYSTACK_PUBLIC_KEY=
```

## Hubtel

```text
HUBTEL_CLIENT_ID=
HUBTEL_CLIENT_SECRET=
```

## Rules

- Never commit real credentials.
- Use `.env.example` for variable names only.
- Use different credentials for development and production where appropriate.
- Rotate credentials if exposed.
