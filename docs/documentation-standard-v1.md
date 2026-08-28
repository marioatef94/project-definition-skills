# Documentation Standard v1

Status: Draft

This standard defines the minimum governance model for project-definition documentation produced, reviewed, stored, and maintained by reusable AI skills.

It is intentionally independent of project type, industry, storage provider, collaboration platform, work-management tool, repository host, filesystem, and AI client.

The governing principle is:

> Create only documentation that has a distinct purpose, audience, lifecycle, or source-of-truth role, and give every governed artifact exactly one authoritative destination.

## 1. Goals

The standard exists to make project-definition documentation:

- understandable by technical and non-technical readers;
- reusable across different project types;
- structured enough for AI-assisted discovery and validation;
- resistant to duplication and documentation drift;
- explicit about facts, assumptions, unknowns, recommendations, and decisions;
- traceable across related documents and downstream work;
- portable across cloud systems, repositories, and local files;
- minimal enough to avoid unnecessary process overhead.

## 2. Non-goals

This standard does not:

- mandate a specific project-management methodology;
- mandate a specific documentation platform;
- require a source-code repository;
- require every project to produce every document type;
- define day-to-day execution status tracking;
- prescribe implementation architecture for all projects;
- turn conversations, task records, or code reviews into authoritative project requirements by default;
- require formal approval workflows for low-risk working notes.

## 3. Document taxonomy

The core taxonomy is intentionally small. A new top-level document type should exist only when it has a distinct audience, lifecycle, or authority model.

### 3.1 Project / Product Overview (`OVR`)

Purpose: provide a concise shared understanding of the project.

Typical content:

- problem or opportunity;
- purpose;
- intended users, beneficiaries, or stakeholders;
- major capabilities or outcomes;
- scope summary;
- major constraints;
- ownership;
- links to deeper project-definition artifacts.

Default lifecycle: `Active -> Deprecated -> Archived`.

### 3.2 Requirements Document (`REQ`)

Purpose: define what the project is expected to achieve or support.

For product-oriented projects this may be presented as a PRD. For other project types, the user-facing title may be adjusted while preserving the same governance role.

Typical content:

- problem;
- goals;
- non-goals;
- users or stakeholders;
- scope;
- functional requirements when applicable;
- business or operating rules;
- non-functional or quality requirements when applicable;
- constraints;
- dependencies;
- data/content needs when applicable;
- security, privacy, safety, or compliance considerations when applicable;
- success criteria;
- risks;
- open questions;
- future considerations.

Default lifecycle: `Draft -> In Review -> Approved -> Superseded/Archived`.

### 3.3 Research / Discovery (`RES`)

Purpose: capture evidence, investigation, options, and uncertainty before a material decision is made.

Typical content:

- question or problem;
- context;
- evaluation criteria;
- sources/evidence;
- options;
- analysis;
- risks;
- recommendation;
- confidence;
- unknowns;
- decision required.

Research is not itself an approved decision.

Default lifecycle: `Active -> Completed -> Archived`.

### 3.4 Decision Record (`DEC`)

Purpose: preserve a material project, business, product, operating, or policy decision and its rationale.

Typical content:

- context;
- decision needed;
- options considered;
- decision;
- rationale;
- implications;
- related requirements;
- superseded decision when applicable.

Default lifecycle: `Proposed -> Approved/Rejected -> Superseded`.

### 3.5 Architecture Overview (`ARC`)

Purpose: provide the current high-level structure of a technical project in a form understandable beyond the implementation team.

Typical content:

- system context;
- applications/interfaces;
- major components or services;
- data architecture;
- integration architecture;
- authentication/authorization when relevant;
- security;
- deployment model;
- observability;
- scalability/availability expectations;
- external dependencies;
- constraints;
- active technical decisions;
- major technical risks or debt.

Default lifecycle: `Active -> Deprecated -> Archived`.

Architecture-specific implementation records may exist outside the initial project-definition skill. This standard does not require them for non-technical projects.

### 3.6 Additional specialized artifacts

Specialized artifacts such as detailed technical designs, API specifications, operational runbooks, incident reviews, detailed data models, or test strategies may be defined by other skills or project standards.

They should not be promoted to mandatory project-definition artifacts unless their distinct lifecycle or audience justifies it.

## 4. Supporting information is not automatically a top-level document

The following are normally sections or supporting artifacts rather than separate governed document types:

- user journeys;
- personas;
- business rules;
- non-functional requirements;
- data models;
- sequence diagrams;
- security considerations;
- migration plans;
- rollout plans;
- test strategies;
- risk lists.

Create a separate document only when the information becomes sufficiently large, cross-cutting, independently owned, or independently maintained.

## 5. Common metadata contract

Governed artifacts should expose enough metadata to identify what they are and how they relate to the project.

### 5.1 Core metadata

Recommended common fields:

```text
Schema Version
Document ID
Document Type
Project ID
Project Name
Title
Owner
Status
Created
Last Updated
Canonical Source / Destination
Relationships
External Work References
Tags
```

`Version` is optional and should represent a meaningful document baseline, not every edit.

### 5.2 Schema version

Structured metadata should include a schema version where practical.

Example:

```yaml
schemaVersion: 1
```

This allows future tooling to evolve the metadata contract without guessing how older artifacts were structured.

### 5.3 Document ID

Use a stable identifier that does not change when the title changes.

Recommended pattern:

```text
<PROJECT>-<TYPE>-<NUMBER>
```

Examples:

```text
NOVA-OVR-001
NOVA-REQ-002
NOVA-RES-003
NOVA-DEC-004
NOVA-ARC-001
```

Projects may use another deterministic ID convention if one already exists.

### 5.4 Project identity

Project IDs should be short and stable.

Example:

```yaml
project:
  id: NOVA
  name: Nova Initiative
```

Do not rely only on mutable display names for cross-document relationships.

### 5.5 Owner

Owner means the person, team, or role accountable for keeping the artifact accurate.

It does not necessarily mean the original author.

### 5.6 Tags

Tags support discovery but must not replace structured metadata.

Good examples:

```text
authentication
payments
localization
operations
```

Avoid encoding structured fields such as document type, lifecycle status, or destination as free-form tags when those fields already exist.

## 6. Information-state labels

AI-generated or AI-normalized project information must distinguish the following concepts where ambiguity matters:

- **Fact** — directly supported by a trusted source or explicit user statement;
- **Requirement** — an expected outcome, behavior, or rule established by the project;
- **Constraint** — an imposed limitation or boundary;
- **Decision** — a choice that has been explicitly made;
- **Assumption** — plausible but not yet confirmed;
- **Inference** — a conclusion derived from available evidence;
- **Recommendation** — advice proposed by the agent or another source;
- **Unknown** — information not yet established;
- **Conflict** — two or more incompatible statements requiring resolution.

An assumption, inference, or recommendation must never silently become a requirement or decision.

## 7. Requirement structure and identifiers

Where a requirements document benefits from traceability, assign stable local requirement IDs.

Recommended categories:

```text
FR-001   Functional requirement
BR-001   Business / operating rule
NFR-001  Non-functional / quality requirement
CON-001  Constraint
```

The globally unique reference is the document ID plus local requirement ID:

```text
NOVA-REQ-002#FR-001
```

Requirement IDs should remain stable when wording is refined without changing the underlying requirement identity.

Do not renumber requirements merely to make a sequence look tidy.

## 8. Document lifecycle

Different artifact types use different status vocabularies, but their states normalize to four governance categories:

```text
Working
Reviewing
Authoritative
Historical
```

### 8.1 Requirements document

```text
Draft
  -> In Review
  -> Approved
  -> Superseded / Archived
```

`Approved` means the document is the current authoritative project-definition source for its scope.

### 8.2 Research

```text
Active
  -> Completed
  -> Archived
```

`Completed` research may remain useful evidence but does not automatically become a decision.

### 8.3 Decision record

```text
Proposed
  -> Approved / Rejected
  -> Superseded
```

Approved decisions should not be rewritten to erase historical context. A changed decision should normally supersede the earlier record.

### 8.4 Project / Product Overview and Architecture Overview

```text
Active
  -> Deprecated
  -> Archived
```

These are living descriptions of current project truth and may be updated rather than versioned as separate documents for every change.

## 9. Canonical source rules

Every governed artifact must have exactly one authoritative destination at a time.

Examples of valid authoritative destinations include:

- a collaborative document;
- a repository file;
- a local Markdown file;
- a local document file;
- a record in a work-management system;
- another user-approved document store.

The standard does not prefer a vendor or transport mechanism.

### 9.1 One editable source of truth

Do not maintain two independently editable authoritative copies of the same artifact by default.

Bad:

```text
Editable remote requirements document
        <->
Editable local requirements document
```

Preferred:

```text
Canonical artifact
      ->
Derived/read-only representation
```

### 9.2 Derived representations

Generated mirrors are allowed when useful for retrieval, portability, offline access, or AI context.

Derived copies should clearly indicate that they are generated and should identify their canonical source when possible.

Example metadata:

```yaml
generated: true
canonical:
  type: document
  locator: <opaque destination reference>
```

Do not treat a manually edited derived copy as canonical unless the user explicitly changes the canonical destination.

### 9.3 Canonical destination changes

Changing where an authoritative artifact lives is a governance action.

It must not happen silently because an integration is unavailable.

The user must explicitly approve the new authoritative destination.

## 10. Conflict-resolution rules

When two sources disagree, the agent must not guess which statement is correct merely because one source is newer or easier to access.

Use this order:

1. identify declared canonical artifacts;
2. evaluate artifact type and lifecycle state;
3. preserve historical records separately from current truth;
4. if two current authoritative sources conflict, require human resolution.

Example:

```text
Current approved requirements: feature is optional
Current approved decision: feature is mandatory
```

Result:

```text
Canonical conflict detected — human decision required.
```

The agent may analyze impact and recommend resolution options, but it must not silently choose one.

## 11. Current truth versus historical truth

Historical records remain valid evidence of what was previously decided or required.

Example:

```text
DEC-004 — Approved
Original operating model

DEC-011 — Approved
New operating model
Supersedes: DEC-004
```

Both records remain historically valid. `DEC-011` represents current decision truth.

## 12. Document relationships

Use stable document IDs for cross-artifact relationships wherever practical.

Recommended relationship types include:

- `relatedTo`;
- `dependsOn`;
- `implements`;
- `derivedFrom`;
- `supersedes`;
- `supersededBy`;
- `informedBy`;
- `affects`.

Example:

```yaml
relationships:
  informedBy:
    - NOVA-RES-003
  relatedTo:
    - NOVA-DEC-004
```

External task/work references may be linked but should not replace project requirements.

## 13. External work records are not automatically project truth

Tasks, cards, work items, tickets, checklists, or sprint records represent execution work unless a project explicitly establishes otherwise.

They may contain acceptance criteria and implementation scope, but they should normally reference authoritative requirements rather than redefine them.

Conceptually:

```text
Requirements
    ->
Work decomposition
    ->
Execution
```

not:

```text
Work item
    ->
Silently becomes the master requirement
```

## 14. Conversations are candidate knowledge, not authoritative truth

Chat messages, meeting transcripts, emails, and AI conversations may contain important project information, but they can also contain superseded proposals, brainstorming, or contradictions.

Treat them as evidence to normalize and confirm.

Conceptually:

```text
Conversation / notes
       ->
Candidate information
       ->
Clarification / validation
       ->
Governed document
```

Do not treat chronology alone as authority.

## 15. Template standard

Templates define expected structure and authoring guidance. They must not contain project-specific assumptions.

### 15.1 Common envelope plus type-specific content

Each governed template consists conceptually of:

```text
Common metadata envelope
        +
Document-type sections
```

Do not duplicate the metadata contract independently in every template when a shared reference can define it.

### 15.2 Section applicability

Template sections use three applicability levels:

- **Required** — necessary for that artifact type;
- **Conditional** — required when project context makes it relevant;
- **Optional** — useful but not required.

Do not force irrelevant sections merely to make a template look complete.

### 15.3 Guidance, not canned answers

Templates should explain what information belongs in a section rather than prefill generic claims.

Bad:

```text
The system must be scalable and secure.
```

Better guidance:

```text
Describe relevant scale expectations, security boundaries, constraints, and evidence. Do not invent targets that have not been agreed.
```

### 15.4 Unknown information remains visible

Templates must permit explicit values such as:

```text
TBD
Unknown
Decision Required
Not Applicable
Deferred
```

The AI must never invent information simply to satisfy template completeness.

### 15.5 Template versions

Templates should be versioned independently from generated documents.

Example:

```text
requirements@1.0
requirements@1.1
requirements@2.0
```

Updating a template must not automatically rewrite existing governed artifacts.

An existing document may record the template version from which it was created when that information is useful.

## 16. Minimum sufficient documentation

The project-definition workflow should generate only artifacts justified by project needs.

Document selection should consider:

- intended audience;
- complexity;
- risk;
- project maturity;
- cross-team impact;
- evidence/research needs;
- technical complexity for technical projects;
- longevity of the information;
- cost of forgetting the information later.

A simple initiative may require only:

```text
Project Overview
Requirements Document
```

A complex project may additionally justify:

```text
Research
Decision Records
Architecture Overview
```

Templates existing in the repository are not themselves a reason to generate documents.

## 17. Validation rules

Validation is both template-aware and lifecycle-aware.

### 17.1 Draft artifacts

Drafts may contain:

- TBD items;
- open questions;
- assumptions;
- unresolved recommendations.

The validator should surface them without pretending the draft is invalid merely because discovery is incomplete.

### 17.2 Authoritative artifacts

Before an artifact becomes authoritative, validation should check as applicable:

- required sections are meaningfully completed;
- blocking conflicts are resolved;
- high-impact assumptions are visible;
- unsupported claims are removed or labeled;
- critical open questions are resolved or explicitly accepted as open;
- relationships and metadata are coherent;
- scope and non-goals are distinguishable;
- requirements do not contain obvious duplicate or contradictory meaning.

Validation must not fabricate content in order to pass.

### 17.3 Finding severity

Recommended severity levels:

- **Blocking** — the artifact is materially unsafe or misleading without resolution;
- **Important** — should be addressed but may not block progress;
- **Advisory** — quality improvement with limited effect on readiness.

## 18. Human authority and approval

AI may:

- discover;
- extract;
- normalize;
- draft;
- refactor working drafts;
- identify gaps;
- identify conflicts;
- validate;
- recommend;
- propose amendments.

AI must not silently:

- approve its own generated requirements;
- convert recommendations into decisions;
- overwrite authoritative content;
- resolve stakeholder disagreements;
- change canonical destinations;
- erase historical records;
- hide material unknowns.

Human approval is required before a newly generated artifact becomes authoritative or before a material replacement of existing authoritative content.

## 19. Lifecycle-aware AI modification policy

Use these normalized modification levels:

```text
Working artifact
  -> AI may actively edit the draft.

Reviewing artifact
  -> AI may propose or apply controlled draft changes while keeping review visible.

Authoritative artifact
  -> AI may analyze and propose changes; material authoritative changes require explicit human approval.

Historical artifact
  -> read-only by default; create a superseding artifact instead of rewriting history.
```

## 20. Persistence and partial-failure behavior

A generated document shown in conversation is not automatically persisted.

The agent must report persistence accurately.

If multiple writes are attempted, report each result independently.

Example:

```text
Project Overview: saved
Requirements Document: failed to save
Decision Record: saved
```

A failure to save one artifact must not be represented as a successful project-wide publication.

If the authoritative destination is unavailable, retain the draft and ask the user whether to retry, save a non-canonical copy elsewhere, or change the canonical destination.

## 21. Storage-format guidance

The standard is format-neutral.

Valid representations may include:

- Markdown;
- structured collaborative documents;
- plain text;
- provider-native pages/records;
- supported local document formats;
- machine-readable specifications where appropriate.

When structured metadata cannot be represented natively, preserve the information in a clear human-readable metadata section rather than inventing hidden metadata.

## 22. Machine-readable contracts

When a project domain has a well-established machine-readable contract that can be authoritative, prefer that contract over manually duplicated prose for the same detail.

Examples may include interface specifications, schemas, or configuration definitions.

The human-readable project definition should reference or summarize such contracts rather than maintain a conflicting editable copy.

This is an extensibility rule; the initial project-definition skill does not need to generate every specialized machine-readable format.

## 23. Naming and presentation

User-facing document titles may adapt to audience and project type.

For example, the governed `REQ` artifact may be titled:

```text
Product Requirements
Project Requirements
Program Requirements
Initiative Definition
```

The governance type remains `REQ` even when presentation language differs.

Avoid forcing software terminology on non-technical projects.

## 24. Privacy and sensitivity

Documentation generation must follow least-necessary-data principles.

- Do not include secrets, credentials, access tokens, private keys, or authentication material.
- Avoid copying sensitive source data unless required for the intended document and approved destination.
- Prefer summaries over unnecessary raw source reproduction.
- Preserve confidentiality boundaries when generating examples or derived artifacts.

## 25. Provider neutrality

The standard defines roles, not vendors.

Examples:

```text
Authoritative document destination
External work-management destination
Repository or filesystem destination
Research source
```

Provider-specific IDs, URLs, authentication, formatting, and operations belong to execution adapters or available agent capabilities, not to the core documentation standard.

## 26. Standard extension model

Projects or organizations may extend this standard when necessary.

Recommended precedence:

```text
Project extension
    overrides
Organization extension
    overrides
Global standard
```

Extensions should define only meaningful differences rather than copying and forking the full standard.

Examples of legitimate extensions include:

- mandatory regulatory sections;
- domain-specific risk fields;
- organization-specific metadata;
- additional approval rules;
- project-specific document types.

Core principles such as explicit uncertainty, one authoritative destination, and no silent AI approval should not be weakened without an explicit governance decision.

## 27. Initial template registry

The first `project-definition` skill is expected to support these templates:

```text
OVR  Project / Product Overview
REQ  Requirements Document
RES  Research / Discovery
DEC  Decision Record
ARC  Architecture Overview
```

Additional templates should be introduced only when a distinct project-definition need is demonstrated.

## 28. Standard conformance checklist

A generated project-definition artifact set conforms to this standard when, where applicable:

- each governed artifact has a clear type;
- each governed artifact has one authoritative destination;
- document IDs are stable where traceability is needed;
- assumptions and unknowns remain explicit;
- recommendations are not represented as decisions;
- document relationships use stable references where practical;
- the selected document set is no larger than necessary;
- templates are applied according to project relevance;
- authoritative publication is human-controlled;
- historical records are not silently rewritten;
- write/persistence outcomes are reported accurately;
- provider-specific integration behavior is kept outside the core documentation model.

## 29. Relationship to the project-definition skill

This standard defines documentation governance. It does not itself define the user journey.

The `project-definition` skill should use this standard together with:

- the skill behavioral contract;
- the project-definition user journey;
- the capability contract;
- the applicable template and reference guidance.

The skill may simplify presentation for the user, but it must preserve the semantics defined here.

## 30. Change policy

This is version 1 of the documentation standard.

Future revisions should:

- preserve backward compatibility where reasonable;
- document breaking semantic changes clearly;
- avoid silently changing the meaning of existing document types or lifecycle states;
- provide migration guidance when metadata or template semantics materially change.

Existing governed artifacts do not need to be rewritten solely because a newer standard version exists unless the user or project explicitly chooses to migrate them.
