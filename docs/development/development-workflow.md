# Votera — Development Workflow

## Branch Strategy

The project will use:

```text
main
  └── feature branches
```

Feature branches should use descriptive names such as:

```text
feature/authentication
feature/election-management
feature/voting
fix/duplicate-vote
docs/database-design
test/vote-validation
```

## Development Cycle

```text
Requirement
  ↓
GitHub Issue
  ↓
Branch
  ↓
Implementation
  ↓
Test
  ↓
Review
  ↓
Merge
  ↓
Release
```

## Commit Convention

Use meaningful conventional-style commits:

```text
feat: add election creation
fix: prevent duplicate voting
test: add vote validation tests
docs: document database schema
refactor: simplify election service
chore: update dependencies
```

## Before Commit

Run the relevant:
- frontend lint/tests
- backend tests
- formatting checks
- manual verification

## Pull Requests

A PR should explain:
- what changed
- why it changed
- how it was tested
- related issue
- known limitations

## Rule

One meaningful change should be easy to understand and trace back to a requirement.
