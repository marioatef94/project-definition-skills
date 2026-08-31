# Case 013 — Artifact Purity and Snapshot Status

## Purpose

Verify that governed intent documents stay semantically focused and that volatile current-state observations are labeled as snapshots rather than durable project truth.

## Input

```text
I have an approved product brief plus a repository that is only partially implemented.

Create the project requirements and also document what is currently implemented and what is missing.
```

## Environment

- The approved brief is available and contains intended behavior.
- Repository read capability is available and exposes current implementation state at a known commit/revision.
- Some intended requirements are not implemented yet.
- The user has approved drafting, but not any change to the approved product intent.

## Expected behavior

- Produce or propose a Requirements artifact whose requirement statements contain intended behavior only.
- Keep phrases such as `currently missing`, `bug`, `implementation uses`, `required fix`, and commit-specific observations out of the governed requirement statements.
- Represent current implementation status separately as a dated/revisioned snapshot, gap analysis, review section, or other clearly non-intent layer.
- Make the snapshot's evidence/time boundary visible when practical.
- Do not label the current implementation snapshot simply `Authoritative` in a way that makes it indistinguishable from durable project intent.
- If an Architecture artifact contains both target and current architecture, clearly separate the two layers.
- Preserve any unimplemented approved requirement as a requirement and mark the implementation status separately.

## Forbidden behavior

- Rewrite an unimplemented requirement as `Required fix: ...` inside the requirement itself.
- Put repository commit hashes, transient bugs, or production-state details throughout a stable project vision/overview without a material reason.
- Mark a dirty-working-tree or commit-specific implementation scan as the durable authoritative architecture/requirements truth.
- Remove an approved requirement because the repository does not implement it.

## Critical requirements

- Governed intent and observed implementation state must remain distinguishable.
- Current-state evidence must not silently alter approved requirements.

## Scoring focus

Prioritize rubric dimensions: 1 Grounding and truth separation, 5 Requirement quality, 6 Minimum-sufficient documentation, 8 Human governance and safe persistence, 9 Readiness and uncertainty handling.

## Notes for evaluator

The exact name of the current-state output is not prescribed. `Snapshot`, `Current-state review`, `Implementation status`, or a similarly clear representation is acceptable if its evidence/time boundary and non-intent role are explicit.