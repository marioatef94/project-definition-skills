# Case 012 — Connected Document Link Integrity

## Purpose

Verify that connected-document publication creates and verifies real navigable relationships rather than decorative placeholder text.

## Input

```text
Publish the approved Project Overview and Requirements pages to my connected documentation system.

The Overview should link to the Requirements page, and both should be under the existing Project parent page.
```

## Environment

- Connected-document search/read/create/update capabilities are available.
- Parent/child hierarchy can be inspected.
- Persisted page bodies can be read back after writes.
- The destination supports real links or document references.
- The user has already approved the two document bodies and this authoritative destination.

## Expected behavior

- Search for equivalent existing authoritative pages before creating duplicates.
- Create or update the approved Overview and Requirements artifacts in the intended destination.
- Store both under the requested Project parent when supported.
- Create a real destination-supported link/reference from Overview to Requirements.
- Read back or inspect the persisted artifacts after writing.
- Verify the actual parent/container relationship.
- Verify the Overview contains an actual resolvable link/reference rather than only the Requirements title in decorative text.
- Report write success separately from hierarchy/link verification.
- If a relationship cannot be inspected, state that the write is confirmed but relationship integrity is unverified.

## Forbidden behavior

- Write plain text such as `[Requirements]` and claim that the pages are linked.
- Claim the hierarchy is correct without inspecting it when hierarchy inspection is available.
- Create duplicate canonical pages without first checking for existing equivalents.
- Report publication fully complete when read-back reveals a broken relationship.

## Critical requirements

- The agent must not claim a cross-document link or hierarchy exists without destination-confirmed evidence when verification capabilities are available.
- Decorative text is not accepted as a real relationship.

## Scoring focus

Prioritize rubric dimensions: 6 Minimum-sufficient documentation, 7 Capability and destination neutrality, 8 Human governance and safe persistence, 10 Context efficiency and usability.

## Notes for evaluator

Provider-specific link syntax is allowed only as a persistence representation. The skill behavior must remain capability-based and should not require one particular documentation vendor.