# Runtime Documentation Standard

This is the executable summary used by the `project-definition` skill. The repository-level design source is `docs/documentation-standard-v1.md`.

## Core rules

1. Every governed artifact has one authoritative destination.
2. Derived copies must be clearly non-authoritative.
3. Human approval is required before AI-generated content becomes authoritative project truth.
4. Unknowns, assumptions, recommendations, decisions, implementation observations, and requirements remain distinct.
5. Do not silently resolve conflicts between authoritative sources.
6. Do not let observed implementation silently supersede governed intent.
7. Do not generate an artifact unless it adds distinct value.
8. Keep each artifact focused on its governance role.
9. Provider-specific storage details must not change document semantics.
10. After authoritative persistence, verify the stored result when the environment supports read-back or relationship inspection.

## v1 artifact types

- `OVR` — Project / Product Overview
- `REQ` — Requirements Document
- `RES` — Research / Discovery
- `DEC` — Decision Record
- `ARC` — Architecture Overview

## Artifact-role purity

Each governed artifact has a primary semantic job.

### OVR

Stable shared understanding of purpose, users/stakeholders, scope, outcomes, major constraints, and links to deeper artifacts.

Avoid letting volatile repository revisions, bug lists, current deployment trivia, or temporary implementation state dominate the overview. Such observations may be linked or briefly noted when they materially affect understanding.

### REQ

Governed intended behavior, outcomes, rules, qualities, and constraints.

Do not embed transient implementation-status commentary into requirement statements. Keep `bug`, `currently missing`, `implementation uses`, `current production config`, `required fix`, and similar observations in a separate current-state or gap-analysis output.

### RES

Evidence, investigation, options, uncertainty, and recommendations. Research may inform a requirement or decision but does not become one by itself.

### DEC

An explicit choice and its rationale. A current implementation choice is not automatically an approved decision. If implementation and intent differ, record a proposed decision only after surfacing the conflict; approval is required before the decision becomes authoritative.

### ARC

High-level technical structure appropriate to the project's audience and purpose.

Be explicit about whether an architecture artifact describes:

- **target/intended architecture** — governed direction;
- **current/observed architecture** — a dated implementation snapshot;
- or both, with clearly separated sections.

Do not merge intended and observed architecture into one indistinguishable truth layer.

## Observed-state snapshots

Current implementation reviews, audits, repository scans, deployment observations, and requirement-vs-implementation matrices are evidence about a point in time.

When represented as a standalone or supporting artifact, label them with snapshot semantics such as:

```text
Status: Snapshot
As of: <date or source revision>
Evidence: <source references>
```

A snapshot can be authoritative evidence of what was observed at that time, but it must not be mislabeled as durable project intent.

Prefer lifecycle/status language that makes volatility visible:

- `Snapshot`
- `Current-state review`
- `Active gap analysis`
- `Completed audit`

rather than using `Authoritative` alone for transient observed state.

## Source authority

Distinguish:

- governed project intent;
- observed implementation state;
- historical decisions;
- work/execution records;
- recommendations/inference.

Source code, configuration, prototypes, deployed behavior, work items, and tests can establish current-state evidence. They do not automatically establish intended requirements or approved decisions.

If observed implementation conflicts with an authoritative requirement/decision, preserve the governed intent and record the mismatch. Changing intent requires human approval.

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

For observed-state content, include an `as of` date/source revision when practical.

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
- Observed implementation state

These labels may be explicit in the document when useful or remain part of the agent's working model.

## Lifecycle

Use lifecycle semantics appropriate to the artifact rather than one universal status list.

### OVR / target ARC

Typical lifecycle:

```text
Active → Deprecated → Archived
```

These are living governed descriptions of project direction/current agreed structure.

### Current/observed ARC or implementation review

Use snapshot semantics with an explicit observation date/revision. Do not imply that an old implementation snapshot remains current after its evidence changes.

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

### Observed-state snapshots

AI may refresh the snapshot from new evidence, but must preserve or clearly replace the prior `as of` reference. Refreshing observed state does not authorize changing requirements or decisions.

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

When the destination supports real hyperlinks, typed relations, or parent/child references, use the actual destination mechanism rather than decorative placeholder text.

Plain text such as:

```text
[Requirements]
```

is not evidence that a relationship or hyperlink exists.

After publishing connected artifacts, verify important relationships when the environment supports inspection. Do not report documents as `linked`, `cross-linked`, or `navigable` without destination-confirmed evidence.

## Requirement identifiers

Use local IDs when traceability adds value:

- `FR-001` — functional requirement;
- `BR-001` — business / operating rule;
- `NFR-001` — non-functional / quality requirement;
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
- implementation-state/requirement confusion;
- implementation behavior silently superseding intent;
- artifact-role leakage;
- lifecycle/status appropriateness;
- unresolved blocking conflicts;
- duplicated requirements;
- broken, placeholder, or unresolved relationships;
- source-of-truth ambiguity.

Validation severity:

- `Blocking`
- `Important`
- `Advisory`

An approved artifact should not contain an unresolved blocker unless the user explicitly accepts and records that risk.

## Publishing

Before authoritative publication, present a change summary and obtain approval.

Read `publishing.md` for the full persistence-integrity procedure.

After the write:

- verify success;
- expose the resulting location/reference when available;
- read back/inspect the persisted artifact when supported;
- verify important title/status/parent/content/relationship properties when relevant;
- report any unverified integrity dimension explicitly;
- report partial failures precisely;
- never claim publication or linking occurred without confirmation.

## Deletion and history

Prefer archive or supersede over deletion for governed authoritative records. Never silently delete approved requirements, decisions, or historical project-definition evidence.