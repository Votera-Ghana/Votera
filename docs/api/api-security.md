# Votera — API Security Rules

## Authentication

Protected endpoints require a valid authenticated identity.

## Authorization

Every protected operation must verify:
- authenticated user
- role
- resource scope
- action permission

## Validation

All request bodies, query parameters, and path parameters must be validated.

## Vote Endpoint

The vote endpoint is security-critical and must verify:
1. authenticated voter
2. valid election
3. active election
4. voter eligibility
5. valid position
6. valid candidate
7. duplicate participation
8. valid voting rules

## Webhooks

Payment webhooks must be verified using the provider's supported signature or verification mechanism before changing payment state.

## Rate Limits

Apply rate limits to:
- login
- registration
- OTP
- password reset
- vote submission
- payment initialization

## CORS

Production CORS must allow only trusted frontend origins.

## Documentation

FastAPI OpenAPI documentation should be available during development and appropriately restricted/configured in production if necessary.
