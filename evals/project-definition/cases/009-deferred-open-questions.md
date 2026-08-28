# Case 009 — Deferred and open questions

## Purpose

Verify that the workflow remains useful when the user deliberately defers decisions instead of forcing artificial completeness.

## Input

```text
I do not know the payment model or final launch region yet. Mark both as decisions for later and continue with everything else we can define now.
```

## Environment

- Enough unrelated context exists to define the rest of the project.
- Payment model and launch region affect some requirements but do not block all project-definition work.

## Expected behavior

- Records both items as explicit open questions/decisions required.
- Continues with unaffected requirements and documents.
- Identifies any requirements whose final form depends on those open items.
- Does not repeatedly ask the user to resolve the deliberately deferred questions.
- Readiness outcome is based on actual impact; likely `Ready with open items` if they do not materially block the next step, otherwise `Not ready` with explanation.

## Forbidden behavior

- Choosing a payment model or region to complete the template.
- Hiding the open items.
- Automatically declaring `Ready` merely because drafts are complete.

## Critical requirements

- Must preserve both deferred decisions explicitly.

## Scoring focus

Prioritize rubric dimensions 1, 3, 5, 9, and 10.
