# Votera — User Roles & Permissions

## 1. Purpose

This document defines the user roles, responsibilities, permissions, and access boundaries within the Votera digital voting platform.

The purpose of this document is to establish a clear authorization model before implementation begins.

The role model will later be used to guide:

* Database design
* FastAPI authorization
* API endpoint protection
* React route protection
* Dashboard design
* Security testing
* Audit logging

---

# 2. Role Model

Votera will initially support three primary roles:

```text
System Administrator
        │
        ├── Manages Votera platform
        │
        └── Manages organizations and users
                 │
                 ▼
        Election Administrator
                 │
                 ├── Creates elections
                 ├── Manages candidates
                 ├── Manages voters
                 └── Manages election results
                          │
                          ▼
                        Voter
                          │
                          └── Participates in eligible elections
```

---

# 3. Role 1 — Voter

## 3.1 Description

A voter is an individual who is eligible to participate in one or more elections hosted on Votera.

The voter is the primary participant in the voting process.

---

## 3.2 Responsibilities

A voter is responsible for:

* Maintaining their account credentials
* Accessing elections for which they are eligible
* Reviewing candidate information
* Making their own voting decisions
* Submitting votes correctly
* Keeping authentication information secure

---

## 3.3 Voter Permissions

A voter can:

* Register an account
* Log in
* Log out
* View their profile
* View eligible elections
* View election details
* View candidates
* Select candidates
* Review selections
* Submit a vote
* Receive vote confirmation
* View appropriate election status information
* Receive election notifications

---

## 3.4 Voter Restrictions

A voter cannot:

* Create elections
* Edit elections
* Delete elections
* Create positions
* Create candidates
* Modify candidates
* Manage eligible voters
* Open elections
* Close elections
* View restricted administrative information
* Modify votes
* Modify election results
* Manage organizations
* Manage other users
* Assign roles

---

# 4. Role 2 — Election Administrator

## 4.1 Description

An election administrator is responsible for creating and managing elections for an organization.

The election administrator operates within the scope of the organization and elections assigned to them.

---

## 4.2 Responsibilities

An election administrator is responsible for:

* Creating elections
* Configuring elections
* Managing positions
* Managing candidates
* Managing eligible voters
* Opening elections
* Monitoring elections
* Closing elections
* Viewing election results
* Ensuring election information is correctly configured

---

## 4.3 Election Administrator Permissions

An election administrator can:

### Election Management

* Create elections
* View elections
* Edit eligible election information
* Configure election dates
* Configure election status
* Open elections
* Close elections
* Cancel elections where permitted

### Position Management

* Create positions
* View positions
* Edit positions
* Delete positions before voting restrictions apply

### Candidate Management

* Add candidates
* View candidates
* Edit candidates
* Remove candidates before voting restrictions apply

### Voter Management

* View eligible voters
* Add eligible voters
* Remove voter eligibility where permitted
* Monitor voter participation statistics

### Results

* View election results
* View candidate vote totals
* View position results
* View turnout statistics

---

## 4.4 Election Administrator Restrictions

An election administrator cannot:

* Access elections belonging to organizations they are not authorized to manage
* Modify another administrator's elections without authorization
* Modify individual recorded votes
* Manually change candidate vote totals
* Delete valid votes
* Modify audit records
* Manage system-wide users unless explicitly granted permission
* Assign system administrator privileges
* Modify platform configuration
* Access system secrets

---

# 5. Role 3 — System Administrator

## 5.1 Description

A system administrator manages the overall Votera platform.

This role has platform-level privileges beyond the scope of individual elections.

---

## 5.2 Responsibilities

A system administrator is responsible for:

* Managing organizations
* Managing platform users
* Managing user roles
* Monitoring platform activity
* Reviewing audit logs
* Managing platform-level configuration
* Supporting election administrators
* Maintaining overall platform security

---

## 5.3 System Administrator Permissions

A system administrator can:

### User Management

* View users
* Manage user accounts
* Activate or deactivate accounts where appropriate
* Assign roles
* Modify appropriate user information

### Organization Management

* Create organizations
* View organizations
* Edit organizations
* Activate organizations
* Deactivate organizations

### Election Oversight

Where appropriate, a system administrator can:

* View platform elections
* Monitor election status
* Investigate platform-level issues
* Support election administrators

---

## 5.4 System Administrator Restrictions

Even system administrators should not have unrestricted ability to modify individual votes.

The platform should protect vote integrity by separating:

```text
Administrative Management
        ≠
Vote Modification
```

System administrators should not normally be able to:

* Change a voter's candidate selection
* Modify vote totals manually
* Delete valid votes
* Alter election results directly

Any exceptional administrative intervention should use a controlled, auditable process if such functionality is ever introduced.

---

# 6. Permission Categories

Permissions are grouped into the following categories:

```text
ACCOUNT
ELECTION
POSITION
CANDIDATE
VOTER
VOTING
RESULTS
ORGANIZATION
USER MANAGEMENT
AUDIT
SYSTEM
```

---

# 7. Permission Matrix

| Permission              |        Voter       | Election Admin | System Admin |
| ----------------------- | :----------------: | :------------: | :----------: |
| Register account        |          ✅         |        ✅       |       ✅      |
| Login                   |          ✅         |        ✅       |       ✅      |
| View own profile        |          ✅         |        ✅       |       ✅      |
| Edit own profile        |          ✅         |        ✅       |       ✅      |
| View eligible elections |          ✅         |        ✅       |       ✅      |
| Create election         |          ❌         |        ✅       |       ✅      |
| Edit election           |          ❌         |        ✅       |      ✅*      |
| Delete election         |          ❌         |     Limited    |      ✅*      |
| Open election           |          ❌         |        ✅       |      ✅*      |
| Close election          |          ❌         |        ✅       |      ✅*      |
| Cancel election         |          ❌         |        ✅       |      ✅*      |
| Create position         |          ❌         |        ✅       |      ✅*      |
| Edit position           |          ❌         |        ✅       |      ✅*      |
| Delete position         |          ❌         |     Limited    |      ✅*      |
| Add candidate           |          ❌         |        ✅       |      ✅*      |
| Edit candidate          |          ❌         |        ✅       |      ✅*      |
| Remove candidate        |          ❌         |     Limited    |      ✅*      |
| Manage eligible voters  |          ❌         |        ✅       |      ✅*      |
| Cast vote               |          ✅         |   If eligible  |  If eligible |
| Vote more than once     |          ❌         |        ❌       |       ❌      |
| Modify recorded vote    |          ❌         |        ❌       |       ❌      |
| View election results   | According to rules |        ✅       |       ✅      |
| View turnout            |       Limited      |        ✅       |       ✅      |
| Create organization     |          ❌         |        ❌       |       ✅      |
| Manage organization     |          ❌         |        ❌       |       ✅      |
| Manage users            |          ❌         |     Limited    |       ✅      |
| Assign roles            |          ❌         |        ❌       |       ✅      |
| View audit logs         |          ❌         |     Limited    |       ✅      |
| Modify audit logs       |          ❌         |        ❌       |       ❌      |
| Manage system settings  |          ❌         |        ❌       |       ✅      |

`*` = Only where required for system-level administration and subject to authorization controls.

---

# 8. Scope of Authority

Role permissions must also consider **scope**.

Having a role does not automatically mean a user can access every resource.

For example:

```text
Election Administrator A
        ↓
Organization A
        ↓
Election 1
Election 2
```

Administrator A should be able to manage Election 1 and Election 2.

However:

```text
Organization B
        ↓
Election 3
```

Administrator A should not automatically have access to Election 3.

Therefore, Votera authorization must consider both:

```text
Role
+
Resource Ownership / Assignment
```

---

# 9. Resource-Level Authorization

The backend should enforce authorization at the resource level.

For example:

```text
Can this user manage elections?
        ↓
Is the user an Election Administrator?
        ↓
Does the election belong to the user's organization?
        ↓
Is the user assigned to manage this election?
        ↓
ALLOW
```

This prevents a user from gaining access merely by knowing the ID of another organization's election.

---

# 10. Voting Authorization

Voting requires several independent checks.

Before accepting a vote, the backend should verify:

```text
User authenticated?
        ↓
        YES
        ↓
Election exists?
        ↓
        YES
        ↓
Election active?
        ↓
        YES
        ↓
Voter eligible?
        ↓
        YES
        ↓
Already voted?
        ↓
        NO
        ↓
Candidate valid?
        ↓
        YES
        ↓
Vote valid?
        ↓
        YES
        ↓
RECORD VOTE
```

These checks must be performed by the backend.

The frontend must not be trusted to enforce voting authorization.

---

# 11. Role Assignment

## 11.1 Default Role

A newly registered user should receive the default:

```text
Voter
```

unless the registration process is specifically designed for another controlled role.

---

## 11.2 Election Administrator Assignment

Election administrator privileges should be granted through an authorized administrative process.

A normal voter should not be able to assign the Election Administrator role to themselves.

---

## 11.3 System Administrator Assignment

System Administrator privileges should be highly restricted.

Users should not be able to elevate themselves to System Administrator through normal application requests.

---

# 12. Least Privilege

Votera shall follow the principle of least privilege.

> Users should receive only the permissions required to perform their responsibilities.

For example:

A voter does not need access to election configuration.

An election administrator does not need access to platform secrets.

A system administrator does not need the ability to modify individual votes.

---

# 13. Backend Enforcement

Role restrictions shall primarily be enforced by the backend.

The FastAPI backend should verify:

* Authentication
* User identity
* User role
* Organization membership
* Election ownership/assignment
* Resource permissions
* Election status

The frontend may hide unavailable features for usability, but frontend restrictions must never be considered sufficient security.

---

# 14. Frontend Access Control

The React application should provide role-appropriate interfaces.

Example:

### Voter Dashboard

```text
Dashboard
My Elections
Vote
Profile
Notifications
Logout
```

### Election Administrator Dashboard

```text
Dashboard
My Elections
Create Election
Candidates
Positions
Voters
Results
Profile
Logout
```

### System Administrator Dashboard

```text
Dashboard
Organizations
Users
Elections
Audit Logs
System Settings
Profile
Logout
```

---

# 15. Protected Routes

The frontend should use protected routes or equivalent route-guarding logic.

Example:

```text
/voter/*
/admin/elections/*
/system/*
```

However, frontend route protection is primarily a user-experience feature.

The backend must independently enforce authorization.

---

# 16. Database Authorization

Supabase/PostgreSQL security policies should eventually support the authorization model.

Database-level protections should be considered for sensitive resources.

Potential protected resources include:

* Users
* Organizations
* Elections
* Candidates
* Voter eligibility
* Votes
* Results
* Audit logs

The exact Row Level Security policies will be defined during database design.

---

# 17. Role Security Rules

The following rules are mandatory principles for Votera:

### Rule 1

A user cannot grant themselves additional privileges.

### Rule 2

A voter cannot access administrative operations.

### Rule 3

An election administrator cannot automatically access another organization's elections.

### Rule 4

A user cannot submit a vote for an election they are not eligible for.

### Rule 5

A voter cannot submit more than one valid vote for the same election.

### Rule 6

Users cannot modify recorded votes through normal application functionality.

### Rule 7

Audit records must not be modifiable through normal application functionality.

### Rule 8

Sensitive operations must be authorized by the backend.

### Rule 9

Frontend restrictions must never be the only security control.

### Rule 10

System privileges must follow least-privilege principles.

---

# 18. Future Roles

Future versions may introduce additional roles if required.

Potential roles include:

* Organization Owner
* Election Auditor
* Election Observer
* Support Administrator
* Finance Administrator

These roles will not be implemented until a clear requirement exists.

---

# 19. Role Expansion Principle

New roles should only be introduced when:

1. A business requirement exists.
2. Existing roles cannot reasonably support the requirement.
3. The new role has clearly defined responsibilities.
4. Permissions are documented.
5. Security implications are reviewed.
6. Tests are created.

This prevents unnecessary role complexity.

---

# 20. Role Model Summary

The initial Votera authorization model is:

```text
                    VOTERA
                       │
             ┌─────────┴─────────┐
             │                   │
      SYSTEM ADMIN         ORGANIZATION
             │                   │
             │            ELECTION ADMIN
             │                   │
             │                   │
             └──────────┬────────┘
                        │
                      VOTER
```

More specifically:

```text
System Administrator
        │
        ├── Platform management
        ├── Organization management
        ├── User management
        └── System oversight

Election Administrator
        │
        ├── Election management
        ├── Position management
        ├── Candidate management
        ├── Voter management
        └── Election results

Voter
        │
        ├── View eligible elections
        ├── View candidates
        ├── Cast vote
        └── Receive confirmation
```

---

# 21. Authorization Principle

The central authorization principle for Votera is:

> **Being authenticated does not automatically mean being authorized.**

Every protected operation must determine:

```text
Who is the user?
        +
What role do they have?
        +
What resource are they accessing?
        +
Are they allowed to perform this action?
```

Only when all required conditions are satisfied should the operation be allowed.

---

**Votera — Your Voice. Your Choice.**
