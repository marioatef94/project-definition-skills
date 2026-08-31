# Requirements Guidance

Use this reference when turning confirmed project context into structured requirements.

## Principle

Requirements describe **intended** outcomes, behavior, rules, qualities, or constraints. They should not silently encode an implementation choice unless that choice is itself an explicit project constraint or approved decision.

Observed implementation is evidence of current state. It is not automatically project intent.

## Source authority for requirements

When normalizing requirement truth, distinguish at least:

1. explicit user/stakeholder requirement;
2. requirement extracted from a current authoritative requirements artifact;
3. approved constraint or decision that governs the requirement;
4. observed implementation behavior;
5. inference;
6. recommendation.

The first three may establish governed intent according to project authority. The remaining categories do not become requirements without explicit approval.

If current implementation conflicts with a governed requirement or approved decision:

```text
Governed intent
      ≠
Observed implementation
```

then:

1. keep the governed intent unchanged;
2. record the implementation mismatch separately;
3. explain the impact when known;
4. label proposed changes as recommendations;
5. require human approval before changing the governed requirement or decision.

Do not choose the implementation simply because it is newer, already deployed, easier to preserve, or more complete.

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

## Requirement purity

A governed requirement statement should answer what must be true, not mix the requirement with implementation-status commentary.

Good:

```text
AUT-001 — The service must validate tokens issued by the approved identity provider.
```

Keep separate:

```text
Current implementation: generic token validation exists, but the approved provider is not configured.
Status: Missing / Partial.
```

Do not embed transient current-state phrases inside requirement statements, such as:

- `currently missing`;
- `bug`;
- `required fix`;
- `current production config`;
- `implementation uses`;
- `the repository currently`;
- `not yet implemented`.

Those belong in a separate implementation-status, gap-analysis, review, or evidence section/artifact.

A requirement may legitimately mention an implementation technology when that technology is itself an approved constraint or decision. In that case, make the governing constraint/decision explicit rather than presenting the implementation as self-justifying.

## Requirement quality

Prefer requirements that are:

- clear to their intended audience;
- specific enough to review;
- independently understandable where practical;
- free from duplicated meaning;
- consistent with confirmed project terminology;
- testable or verifiable conceptually when that is appropriate;
- implementation-neutral unless implementation is constrained;
- free from transient implementation-status commentary.

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
- approved constraint/decision affecting the requirement;
- inference from current behavior;
- recommendation proposed by the agent.

Implementation behavior may support a current-state observation, but it does not establish a requirement merely by existing.

## Implementation-driven recommendations

The agent may recommend aligning project intent with an implementation when doing so appears lower-risk, clearer, or more practical.

That recommendation must remain visibly separate until approved.

Correct sequence:

```text
Requirement A
Implementation B
Conflict detected
Recommendation: change requirement to B
Human approval
Approved decision / amended requirement
```

Forbidden sequence:

```text
Requirement A
Implementation B
Therefore requirement = B
```

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

The same rule applies when a requirement conflicts with implementation state. Existing code does not count as the human resolution.

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