# Votera — System Architecture

## Purpose
This document defines the high-level architecture of Votera and how its services communicate.

## Architecture Overview

```text
User
  |
  v
React + Vite + CSS
  |
  | HTTPS / REST API
  v
FastAPI Backend
  |
  +--------------------+
  |                    |
  v                    v
Supabase/PostgreSQL   External Services
                       |-- Resend (Email)
                       |-- Paystack (Payments)
                       `-- Hubtel (SMS)
```

## Responsibilities

### React Frontend
Responsible for presentation, navigation, forms, client-side validation, user feedback, and API consumption.

### FastAPI Backend
Responsible for authentication, authorization, business rules, vote validation, election lifecycle, integrations, and secure API access.

### Supabase/PostgreSQL
Responsible for persistent application data and relational integrity.

### Resend
Responsible for transactional email.

### Paystack
Responsible for payment processing in the payment release.

### Hubtel
Responsible for SMS/OTP functionality in the communication release.

## Security Boundary

The browser is untrusted. Critical rules must be enforced by FastAPI and, where appropriate, PostgreSQL/Supabase policies.

Secrets must never be exposed to React.

## Core Flow

```text
React
  -> FastAPI
  -> authenticate/authorize
  -> validate business rules
  -> Supabase
  -> response
  -> React
```

External integrations must be called from the backend rather than directly from the browser.

## Architectural Principles

1. Separation of concerns
2. Least privilege
3. Backend-first security
4. Database integrity
5. Small incremental releases
6. Testable business logic
7. Minimal dependencies until justified
