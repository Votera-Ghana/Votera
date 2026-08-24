# Votera Authentication & Authorization Architecture

## 1. Overview

Votera uses Supabase Auth for user identity and authentication while FastAPI provides the application API and authorization layer.

The React frontend communicates with Supabase Auth for authentication and with the FastAPI backend for Votera application functionality.

## 2. Technology

- Frontend: React
- Backend: FastAPI
- Authentication: Supabase Auth
- Database: Supabase PostgreSQL
- Email: Resend

## 3. User Roles

### Voter

A voter can:

- Access elections they are eligible for.
- View election information.
- View candidates.
- Cast votes.
- Receive voting confirmation.

### Organization Admin

An organization admin can:

- Create elections.
- Configure elections.
- Manage positions.
- Manage candidates.
- Manage eligible voters.
- View election results.

## 4. Registration

Public registration creates a standard voter account.

Organization administrator accounts are not created through unrestricted public registration. Administrator access must be granted through an authorized administrative process.

## 5. Authentication Flow

1. User submits authentication information through the React frontend.
2. Supabase Auth validates the authentication request.
3. Supabase creates and manages the authentication session.
4. React maintains the authenticated state.
5. Authenticated requests to FastAPI include the user's authentication credentials.
6. FastAPI verifies the authenticated identity.
7. FastAPI determines the user's Votera role.
8. FastAPI allows or rejects access based on authorization rules.

## 6. Authorization

Authentication determines the identity of the user.

Authorization determines whether the user is allowed to perform a requested operation.

FastAPI is responsible for enforcing Votera application authorization.

## 7. Protected Resources

Examples of protected operations include:

- Election management.
- Candidate management.
- Voter management.
- Voting.
- Results management.

## 8. Security Principles

- Passwords must never be stored directly by Votera.
- Authentication credentials must never be committed to Git.
- Supabase credentials must be stored using environment variables or secure platform secrets.
- Protected API endpoints must verify authentication.
- Administrative operations must verify the user's role.
- Sensitive authentication information must not be returned in API responses.
- Authentication failures must not reveal unnecessary information.

## 9. Future Considerations

The authentication architecture may later be extended with:

- Password recovery.
- Email verification.
- Multi-factor authentication.
- Additional organization roles.
- Account suspension.
- Audit logging.