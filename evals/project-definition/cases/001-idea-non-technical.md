# Case 001 — Idea-only non-technical project

## Purpose

Verify that the skill works for a non-technical initiative and uses adaptive discovery instead of assuming software delivery.

## Input

```text
I want to organize a yearly community conference that brings local volunteers and nonprofit groups together. Help me define the project properly.
```

## Environment

- Conversation capability available.
- No existing files or remote sources.
- No persistence capability required for the first turn.

## Expected behavior

- Summarizes the limited known context before questioning.
- Recognizes that important gaps may include purpose/outcomes, attendees/stakeholders, scope, format, constraints, success criteria, budget/timeline ownership, safety/accessibility, and dependencies where relevant.
- Asks a small batch of high-impact questions rather than a long generic survey.
- Avoids generating final documents before enough definition exists unless the user explicitly asks for an assumption-heavy draft.
- Treats unknown information as unknown.

## Forbidden behavior

- Asking about APIs, databases, deployment, repositories, or software architecture without justification.
- Inventing attendance numbers, venue, budget, dates, sponsors, or organizational roles.
- Automatically generating all available templates.
- Declaring the project Ready from the one-sentence idea.

## Critical requirements

- Must not force a software-project workflow.
- Must not invent project facts.

## Scoring focus

Prioritize rubric dimensions 1, 3, 4, 6, and 9.
