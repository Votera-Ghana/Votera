# Votera — API Plan

## API Principles

- RESTful HTTP API
- JSON request/response format
- Authentication on protected endpoints
- Server-side validation
- Consistent error structure
- Versioning when needed

Base path:

```text
/api
```

## Authentication

```text
POST /api/auth/register
POST /api/auth/login
POST /api/auth/logout
POST /api/auth/forgot-password
POST /api/auth/reset-password
GET  /api/auth/me
```

## Organizations

```text
GET  /api/organizations
POST /api/organizations
GET  /api/organizations/{id}
PATCH /api/organizations/{id}
```

## Elections

```text
GET  /api/elections
POST /api/elections
GET  /api/elections/{id}
PATCH /api/elections/{id}
POST /api/elections/{id}/open
POST /api/elections/{id}/close
POST /api/elections/{id}/cancel
```

## Positions

```text
GET    /api/elections/{id}/positions
POST   /api/elections/{id}/positions
PATCH  /api/positions/{id}
DELETE /api/positions/{id}
```

## Candidates

```text
GET    /api/positions/{id}/candidates
POST   /api/positions/{id}/candidates
PATCH  /api/candidates/{id}
DELETE /api/candidates/{id}
```

## Voters

```text
GET  /api/elections/{id}/voters
POST /api/elections/{id}/voters
DELETE /api/elections/{id}/voters/{user_id}
```

## Voting

```text
GET  /api/elections/{id}/ballot
POST /api/elections/{id}/votes
GET  /api/elections/{id}/participation
```

The vote endpoint must perform all critical validation on the backend.

## Results

```text
GET /api/elections/{id}/results
```

## Notifications

```text
POST /api/notifications/email
POST /api/notifications/sms
POST /api/notifications/otp
```

These endpoints should normally be restricted to backend/internal workflows rather than arbitrary public access.

## Payments

```text
POST /api/payments/initialize
GET  /api/payments/{reference}
POST /api/payments/webhook/paystack
```

## Error Format

A consistent structure should be used, for example:

```json
{
  "detail": "Human-readable error message",
  "code": "ERROR_CODE"
}
```
