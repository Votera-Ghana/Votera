# Votera — Architecture Essentials

## Stack

- Frontend: React + Vite + normal CSS
- Backend: Python + FastAPI
- Database: Supabase PostgreSQL
- Email: Resend
- Payment: Paystack
- SMS: Hubtel

## Request Path

```text
Browser -> React -> FastAPI -> Supabase
                       |
                       +-> Resend
                       +-> Paystack
                       `-> Hubtel
```

## Rules

- React never owns security decisions.
- FastAPI validates every sensitive request.
- Database constraints protect data integrity.
- Secrets stay in environment variables.
- External services are isolated behind backend service modules.
- Vote recording must be transaction-safe.
