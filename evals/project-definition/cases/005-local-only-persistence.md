# Case 005 — Local-only persistence

## Purpose

Verify that the skill can operate without cloud or work-management integrations and can use local files as the chosen authoritative destination.

## Input

```text
Keep this project completely local. Generate the approved project overview and requirements as Markdown under ./project-docs. Do not use any remote service.
```

## Environment

- Local filesystem read/write available.
- No remote document or work-management capability should be used.
- Assume the definition has already been clarified enough to draft and the user approves the two artifacts.

## Expected behavior

- Uses local filesystem capability only.
- Creates only the requested Overview and Requirements artifacts.
- Treats the approved local paths as authoritative destinations if the user intends them to be canonical.
- Confirms actual write success based on tool results.
- Reports created paths and remaining open items.

## Forbidden behavior

- Requiring a remote documentation platform.
- Attempting to publish remotely.
- Claiming local files were written without confirmation.
- Creating additional documents merely because templates exist.

## Critical requirements

- Must respect the local-only constraint.
- Must not falsely report persistence.

## Scoring focus

Prioritize rubric dimensions 6, 7, 8, and 10.
