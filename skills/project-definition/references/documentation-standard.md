# Runtime Documentation Standard

This is the executable summary used by the `project-definition` skill. The repository-level design source is `docs/documentation-standard-v1.md`.

## Core rules

1. Every governed artifact has one authoritative destination.
2. Derived copies must be clearly non-authoritative.
3. Human approval is required before AI-generated content becomes authoritative project truth.
4. Unknowns, assumptions, recommendations, and decisions remain distinct.
5. Do not silently resolve conflicts between authoritative sources.
6. Do not generate an artifact unless it adds distinct value.
7. Provider-specific storage details must not change document semantics.

## v1 artifact types

- `OVR` — Project / Product Overview
- `REQ` — Requirements Document
- `RES` — Research / Discovery
- `DEC` — Decision Record
- `ARC` — Architecture Overview

## Document identifiers

When governed document IDs are useful, use:

```text
<PROJECT>-<TYPE>-<NUMBER>
```

Examples:

```text
ACME-REQ-001
ACME-DEC-003
```

If no stable project identifier exists yet, do not invent one silently. Ask the user or use a clearly provisional identifier in drafts.

Document IDs remain stable even if titles change.

## Common metadata

Use metadata when the destination and project maturity justify it. Typical fields:

- document ID;
- type;
- project;
- title;
- owner;
- status;
- created / last updated;
- authoritative destination;
- related documents;
- related work items when applicable;
- tags.

Do not force metadata that adds no value to a lightweight local draft.

## Information-state labels

During drafting and validation, distinguish:

- Fact
- Requirement
- Constraint
- Decision
- Assumption
- Unknown
- Conflict
- Recommendation
- Evidence

These labels may be explicit in the document when useful or remain part of the agent's working model.

## Lifecycle

Use lifecycle semantics appropriate to the artifact rather than one universal status list.

### OVR / ARC

Typical lifecycle:

```text
Active → Deprecated → Archived
```

These are living current-state documents.

### REQ

Typical lifecycle:

```text
Draft → In Review → Approved → Superseded / Archived
```

Approved requirements are authoritative current project truth until superseded or amended.

### RES

Typical lifecycle:

```text
Active → Completed → Archived
```

Research may recommend a decision but does not become a decision by itself.

### DEC

Typical lifecycle:

```text
Proposed → Approved / Rejected → Superseded
```

Preserve historical decisions rather than rewriting why an earlier choice was made.

## AI modification permissions

### Working drafts

AI may generate, reorganize, and edit while preserving user-provided facts and uncertainty.

### In review

AI should propose changes clearly and avoid silently replacing reviewed content.

### Authoritative documents

AI may read, analyze, validate, and propose amendments. Material changes require explicit human approval.

### Historical / superseded documents

Treat as read-only by default. Create a new decision or amendment rather than rewriting history.

## Authoritative destination

The destination may be:

- local file;
- repository;
- connected document system;
- work-management record when the user intentionally chooses it;
- another supported store.

The skill does not impose a default provider.

If two representations disagree, use the declared authoritative artifact. If two authoritative artifacts conflict, stop authoritative mutation and ask for human resolution.

## Derived copies

Generated convenience copies are allowed when clearly labeled, for example:

```text
GENERATED / NON-AUTHORITATIVE COPY
Authoritative source: <reference>
Do not edit as project truth.
```

Do not build bidirectional editable synchronization by default.

## Relationships

Use stable references when useful. Common relationship semantics:

- `related to`;
- `derived from`;
- `implements`;
- `depends on`;
- `supersedes`;
- `superseded by`.

Do not duplicate large blocks of authoritative content merely to establish a relationship.

## Requirement identifiers

Use local IDs when traceability adds value:

- `FR-001` — functional requirement;
- `BR-001` — business / operating rule;
- `NFR-001` — non-functional requirement;
- `CON-001` — constraint.

The stable reference combines document ID and local ID when a document ID exists.

Do not reuse retired IDs.

## Template behavior

Template sections are one of:

- **Required** — expected for a valid artifact of that type;
- **Conditional** — include only when the project context makes it relevant;
- **Optional** — include when useful.

Templates provide questions and structure, not canned answers.

Never invent content to populate a required or conditional section. Use `TBD`, `Unknown`, `Decision required`, or an explicit open question when appropriate for a draft.

Omit irrelevant optional sections instead of producing filler.

## Validation

Validate against:

- required template content;
- internal consistency;
- unsupported claims;
- assumption/fact confusion;
- unresolved blocking conflicts;
- duplicated requirements;
- broken relationships;
- source-of-truth ambiguity;
- lifecycle appropriateness.

Validation severity:

- `Blocking`
- `Important`
- `Advisory`

An approved artifact should not contain an unresolved blocker unless the user explicitly accepts and records that risk.

## Publishing

Before authoritative publication, present a change summary and obtain approval.

After the write:

- verify success;
- expose the resulting location/reference when available;
- report partial failures precisely;
- never claim publication occurred without confirmation.

## Deletion and history

Prefer archive or supersede over deletion for governed authoritative records. Never silently delete approved requirements, decisions, or historical project-definition evidence.