# Votera — Database Design

## Database

Votera will use Supabase backed by PostgreSQL.

## Core Entities

```text
users
organizations
organization_members
elections
positions
candidates
election_voters
votes
notifications
payments
audit_logs
```

## Relationships

```text
Organization
  └── Elections
       ├── Positions
       │    └── Candidates
       └── Eligible Voters
              └── Votes

User
  ├── Organization Memberships
  ├── Eligibility Records
  └── Votes

Election
  ├── Positions
  ├── Candidates
  ├── Eligible Voters
  ├── Votes
  └── Audit Events
```

## Important Integrity Rules

- Election must belong to an organization.
- Position must belong to an election.
- Candidate must belong to a valid position.
- Eligibility must reference a valid user and election.
- Vote must reference a valid election and candidate.
- A voter must not submit more than one valid participation record for the same election.
- Recorded votes must not be normally updated or deleted.

## Design Note

The exact schema, columns, indexes, foreign keys, unique constraints, and RLS policies will be finalized before implementation.
