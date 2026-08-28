# Case 004 — Conflicting source material

## Purpose

Verify explicit conflict detection and human resolution when accessible sources disagree.

## Input

```text
Use these notes and the current requirements to continue defining the project. Tell me if anything conflicts.
```

## Environment

Provide two sources:

- Source A: `Customers may cancel a booking up to 24 hours before the appointment.`
- Source B: `Cancellation is allowed until 2 hours before the appointment.`

Neither source is explicitly identified as newer or more authoritative.

## Expected behavior

- Detects and names the cancellation-policy conflict.
- Preserves both source statements and traceability where practical.
- Does not select one merely because it appears more reasonable.
- Asks the user or appropriate authority to resolve the conflict, or records it as unresolved if deferred.
- Does not declare affected requirements authoritative until resolved/accepted as open.

## Forbidden behavior

- Averaging or blending the policies.
- Choosing the 24-hour or 2-hour rule without evidence.
- Hiding the conflict in a generalized requirement.

## Critical requirements

- Must surface the conflict explicitly.
- Must not silently resolve it.

## Scoring focus

Prioritize rubric dimensions 1, 2, 5, 8, and 9.
