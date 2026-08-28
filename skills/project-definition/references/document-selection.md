# Document Selection Guidance

Use this reference before proposing which project-definition artifacts should be created or updated.

## Principle

Generate the **minimum sufficient document set**. A document is justified when it has a distinct audience, purpose, lifecycle, or decision value. Do not create documents merely because templates exist.

## Supported v1 artifacts

### OVR — Project / Product Overview

Use when the project needs a concise shared entry point explaining:

- what the project is;
- why it exists;
- who it serves;
- major goals and scope;
- key context;
- where authoritative detailed requirements live.

Usually appropriate for any non-trivial project.

### REQ — Requirements Document

Use when the project needs authoritative requirements, scope, business/operating rules, constraints, quality expectations, risks, and open questions.

This is the primary requirements artifact. The display title may be adapted to the project, for example "Product Requirements", "Project Requirements", or "Initiative Requirements".

Do not generate separate BRD/FRD/NFRD documents by default when the information can live coherently inside one requirements document.

### RES — Research / Discovery

Use only when a material project question depends on investigation, external evidence, comparison, or structured discovery that should remain separately reviewable.

Research is evidence and analysis, not an approved decision.

### DEC — Decision Record

Use when a meaningful product, business, operational, or project-definition choice would be difficult to reconstruct later or materially affects scope, behavior, risk, cost, or future decisions.

Do not create a decision record for every minor preference.

### ARC — Architecture Overview

Use only for technical projects when a shared high-level technical baseline is valuable before downstream planning.

It should explain current/selected system direction at a level understandable across roles. It is not a detailed implementation design.

## Selection factors

Consider:

- project complexity;
- number and diversity of stakeholders;
- amount of existing material;
- uncertainty and risk;
- decision significance;
- technical complexity;
- need for future traceability;
- expected project duration;
- whether multiple audiences need different levels of detail;
- whether an artifact already exists and should be updated instead.

## Typical patterns

### Small or simple initiative

Often sufficient:

```text
OVR
REQ
```

If the overview would simply duplicate a short requirements document, one REQ document may be enough.

### Project with unresolved evidence-dependent choices

```text
OVR
REQ
RES (only for the unresolved investigation)
```

After a decision is made, record a DEC only if the choice is significant enough to preserve separately.

### Complex technical project

Potentially:

```text
OVR
REQ
RES (conditional)
DEC (conditional)
ARC
```

Do not generate ARC until there is enough confirmed technical direction to document meaningfully.

### Existing project-definition review

Prefer:

```text
Update existing OVR/REQ/etc.
```

instead of creating parallel replacements.

## Proposal format

Before drafting, show a compact plan such as:

```text
Proposed documentation

Create
- Requirements Document — authoritative project scope and requirements

Update
- Project Overview — existing overview is missing the newly agreed scope

Conditional
- Research: External dependency options — unresolved evidence-dependent decision

Not needed now
- Architecture Overview — no technical baseline has been selected
```

The user may add, remove, or defer artifacts.

## Anti-patterns

Do not:

- create every supported document for every project;
- split one coherent requirement set across multiple documents without a lifecycle reason;
- create a new document because an existing one uses a different title;
- duplicate authoritative content across local and remote destinations;
- create technical documents for a non-technical project merely because the template exists;
- treat work items or chat history as replacement requirements documents.

## When one document is enough

A single requirements document can include overview context, requirements, risks, decisions, and open questions for a small project if separate artifacts would add no distinct value.

The standard should scale down as well as up.