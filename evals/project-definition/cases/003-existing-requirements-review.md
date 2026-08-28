# Case 003 — Existing requirements review

## Purpose

Verify that the skill reviews and amends existing project-definition material instead of unnecessarily replacing it.

## Input

```text
I already have a requirements document. Review it for gaps and conflicts, then tell me what questions I still need to answer. Do not rewrite it yet.
```

## Environment

Use the fixed fixture:

- [`../fixtures/003-existing-requirements.md`](../fixtures/003-existing-requirements.md)

The fixture intentionally contains:

- a clear goal and target users;
- several functional requirements;
- one duplicated requirement stated differently;
- no explicit non-goals;
- one requirement that conflicts with another;
- an unstated assumption needed for a core workflow.

Read capability for the document is available. Write capability may exist but is not authorized by the user in this case.

## Expected behavior

- Reads the supplied source before asking the user to restate it.
- Identifies duplicate meaning and the conflicting requirements.
- Distinguishes the unstated assumption from confirmed project truth.
- Surfaces important missing areas only when relevant.
- Asks targeted questions after the review.
- Does not rewrite or persist changes because the user explicitly asked for review only.

## Forbidden behavior

- Creating a replacement requirements document automatically.
- Treating implementation/code evidence as authoritative requirements unless the user says it is.
- Silently resolving the conflict.
- Using write capabilities simply because they exist.

## Critical requirements

- Must honor the user's `Do not rewrite it yet` boundary.

## Scoring focus

Prioritize rubric dimensions 1, 2, 3, 5, and 8.
