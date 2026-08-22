# Votera — Initial Database Schema

## users

Stores application user identity and profile information.

Suggested fields:
- id
- email
- full_name
- role
- is_active
- created_at
- updated_at

## organizations

Stores organizations using Votera.

Suggested fields:
- id
- name
- description
- contact_email
- is_active
- created_at
- updated_at

## organization_members

Links users to organizations.

Suggested fields:
- id
- organization_id
- user_id
- membership_role
- created_at

## elections

Suggested fields:
- id
- organization_id
- name
- description
- starts_at
- ends_at
- status
- created_by
- created_at
- updated_at

## positions

Suggested fields:
- id
- election_id
- name
- description
- display_order
- created_at

## candidates

Suggested fields:
- id
- position_id
- full_name
- photo_url
- biography
- manifesto
- created_at
- updated_at

## election_voters

Suggested fields:
- id
- election_id
- user_id
- has_voted
- voted_at
- created_at

## votes

Suggested fields:
- id
- election_id
- position_id
- candidate_id
- voter_reference
- created_at

The final voter reference design must preserve the required ballot-secrecy model.

## audit_logs

Suggested fields:
- id
- actor_user_id
- action
- resource_type
- resource_id
- metadata
- created_at

## notifications

Suggested fields:
- id
- user_id
- type
- channel
- status
- provider_reference
- created_at

## payments

Suggested fields:
- id
- user_id
- organization_id
- amount
- currency
- provider
- provider_reference
- status
- created_at
- updated_at
