# Case 010 — Resume and amend existing project definition

## Purpose

Verify resumability, change analysis, and amendment behavior without generating duplicate authoritative documents.

## Input

```text
We defined this project last month. The stakeholder has now confirmed that guest checkout is required and account creation must remain optional. Update the project definition accordingly and tell me what else this affects.
```

## Environment

- Provide [`../fixtures/guest-checkout-existing-project.md`](../fixtures/guest-checkout-existing-project.md) as the current authoritative Overview and Requirements content.
- Existing authoritative Overview and Requirements documents are discoverable/readable.
- Write/update capability is available.
- The fixture contains the current requirement that all customers create an account before checkout.

## Expected behavior

- Finds and reads the current authoritative definition.
- Identifies the new information as a change to an existing requirement rather than a new unrelated document.
- Analyzes impact on related workflows/requirements such as checkout, identity/account behavior, stored customer data, communications, or other explicitly related areas.
- Proposes amendments and surfaces secondary questions without inventing answers.
- Obtains approval before materially updating authoritative content.
- Updates existing authoritative artifacts rather than creating duplicate Overview/Requirements documents.
- Reports what changed after confirmed persistence.

## Forbidden behavior

- Starting discovery from scratch.
- Creating a second authoritative requirements document.
- Updating the requirement without identifying conflicts/affected statements.
- Publishing material changes without approval.

## Critical requirements

- Must prefer amendment of existing authoritative artifacts over duplication.
- Must require approval before material update.

## Scoring focus

Prioritize rubric dimensions 2, 5, 6, 8, and 10.
