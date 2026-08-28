# Requirements Guidance

Use this reference when turning confirmed project context into structured requirements.

## Principle

Requirements describe expected outcomes, behavior, rules, qualities, or constraints. They should not silently encode an implementation choice unless that choice is itself an explicit project constraint or approved decision.

## Requirement categories

Use only categories that add value to the project.

### Functional requirements

Describe capabilities, behaviors, workflows, or outcomes the project must provide.

Example pattern:

```text
FR-001 — An authorized user can submit a request containing the required information.
```

### Business or operating rules

Describe policies, eligibility, calculations, relationships, limits, or operating rules that govern behavior.

```text
BR-001 — A request may be cancelled only before processing begins.
```

### Non-functional requirements

Describe measurable or reviewable quality expectations such as performance, availability, accessibility, privacy, localization, resilience, or maintainability when relevant.

Avoid vague statements such as "the system should be fast". Preserve an unknown rather than inventing a target.

### Constraints

Describe imposed limits, required technologies/processes already decided, budget/time limits supplied by the user, regulatory constraints, physical constraints, or organizational constraints.

### Dependencies

Record material reliance on another team, service, supplier, approval, asset, decision, or external event.

### Assumptions

Keep unverified assumptions separate from requirements. An assumption may later become a fact, decision, requirement, or be rejected.

### Open questions / decisions required

Record material unresolved items explicitly instead of filling them with agent guesses.

## Requirement quality

Prefer requirements that are:

- clear to their intended audience;
- specific enough to review;
- independently understandable where practical;
- free from duplicated meaning;
- consistent with confirmed project terminology;
- testable or verifiable conceptually when that is appropriate;
- implementation-neutral unless implementation is constrained.

## Stable local identifiers

When traceability adds value, use document-local identifiers:

- `FR-001`, `FR-002`, ...
- `BR-001`, `BR-002`, ...
- `NFR-001`, ...
- `CON-001`, ...

The globally meaningful reference is the document ID plus local requirement ID, for example:

```text
PROJECT-REQ-001#FR-003
```

Do not renumber existing identifiers merely to make numbering contiguous. Retired identifiers should not be silently reused.

## Source and confidence

When a requirement comes from ambiguous or indirect evidence, preserve that uncertainty during drafting and ask for confirmation before treating it as authoritative.

Distinguish:

- explicit user/stakeholder requirement;
- requirement extracted from an authoritative document;
- inference from current behavior;
- recommendation proposed by the agent.

Only the first two are normally requirement truth without additional approval.

## Deduplication

If multiple sources express the same requirement:

1. preserve the clearest formulation;
2. retain relevant source references when practical;
3. do not create duplicate requirements merely because wording differs.

If apparently similar statements imply different behavior, treat them as a conflict rather than merging them silently.

## Conflicts

When requirements conflict:

- surface the conflict clearly;
- identify the competing statements and sources;
- explain the practical impact when known;
- ask the user or responsible stakeholder to resolve it.

The agent may recommend a resolution but must label it as a recommendation.

## Scope boundaries

Keep these distinct:

- in scope;
- explicitly out of scope;
- future consideration;
- unknown / undecided.

Do not turn a future idea into a current requirement.

## Acceptance criteria and work items

Detailed delivery acceptance criteria or task breakdown may be generated later when requested, but they do not replace the authoritative requirement itself.

Project-definition requirements describe what must be true; downstream work items describe how the team plans to deliver or verify it.