# Case 002 — Idea-only technical project

## Purpose

Verify technical discovery without prematurely choosing architecture, vendors, or implementation details.

## Input

```text
I want to build an online booking platform for independent fitness coaches. Clients should be able to find a coach and book sessions. Help me define the product.
```

## Environment

- Conversation capability available.
- No existing project documentation.
- Research may be available but is not automatically required.

## Expected behavior

- Identifies confirmed facts separately from open product questions.
- Prioritizes user roles, booking lifecycle, availability, cancellation/rescheduling, payments if applicable, notifications, coach discovery, boundaries, and success criteria before deep technical design.
- May identify technical concerns such as privacy, identity, scale, integrations, or architecture as later/conditional questions.
- Does not choose frameworks, databases, hosting providers, or architecture without explicit evidence or request.
- Proposes an Architecture Overview only when enough product context exists and it would add value.

## Forbidden behavior

- Immediately designing microservices or a database schema.
- Inventing payment providers, authentication mechanisms, traffic targets, or geographic scope.
- Treating recommendations as approved decisions.

## Critical requirements

- Must not convert a technical recommendation into a requirement or decision without user approval.

## Scoring focus

Prioritize rubric dimensions 1, 3, 5, 6, and 9.
