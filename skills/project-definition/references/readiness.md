# Readiness Guidance

Use this reference before declaring a project definition complete enough for downstream planning or execution.

## Principle

Readiness is an evidence-based judgment about whether unresolved definition gaps are likely to invalidate or materially disrupt the next stage of work. It is not a completeness score and not a guarantee of success.

## Outcomes

Return exactly one top-level status:

### Ready

Use when no known unresolved definition issue is expected to materially block or invalidate downstream planning or execution.

### Ready with open items

Use when the project definition is sufficient to proceed, but named non-blocking questions, assumptions, or improvements remain.

### Not ready

Use when one or more unresolved items materially affect scope, feasibility, compliance, safety, architecture, cost constraints, dependencies, or expected outcomes and should be resolved before responsible downstream work begins.

## Readiness dimensions

Evaluate only dimensions relevant to the project.

### Purpose and outcome

- Is the problem or opportunity understood?
- Are intended outcomes clear enough to evaluate proposed scope?

### Users and stakeholders

- Are primary users, beneficiaries, customers, operators, or decision-makers identified where relevant?
- Are material stakeholder conflicts visible?

### Scope

- Is in-scope work clear enough?
- Are major non-goals or exclusions explicit where ambiguity would create risk?

### Requirements

- Are the major requirements documented?
- Are important business or operating rules explicit?
- Are critical quality expectations defined when they materially matter?

### Unknowns and assumptions

- Are blocking unknowns resolved?
- Are remaining assumptions visible and acceptable for the next stage?

### Constraints and dependencies

- Are major constraints known?
- Are external dependencies or approvals visible?

### Risk

- Are major project risks visible?
- Are security, privacy, safety, legal, or compliance concerns identified when relevant?

### Decisions

- Have decisions that materially constrain downstream work been made or explicitly deferred with acceptable risk?

### Technical direction

For technical projects only:

- Is there enough initial technical direction to avoid obvious incompatible planning?
- Are unresolved architecture choices explicitly visible if they can be safely deferred?

Do not require detailed technical architecture when the project definition does not need it yet.

### Success criteria

Where measurable outcomes matter, are success criteria defined or explicitly unresolved?

Do not invent metrics merely to improve readiness status.

## Blocking vs non-blocking

A gap is **blocking** when a reasonable answer could materially change the next stage of work.

Examples may include:

- unknown target users when user needs define the product;
- unresolved legal permission where the project may not be allowed to operate;
- mutually contradictory core requirements;
- unknown required integration that determines feasibility;
- missing scope boundary that could double the project;
- unresolved physical or budget constraint that may make the plan impossible.

A gap may be **non-blocking** when it can be resolved safely during downstream planning without invalidating current scope.

## Output format

Use a compact structure:

```text
Readiness: Ready with open items

Why
- Core problem, users, scope, and requirements are defined.
- No unresolved issue currently changes overall feasibility.

Open items
- Confirm final reporting format before detailed planning.
- Decide whether the optional secondary audience is included in the first release.

Risks to carry forward
- External approval timing remains uncertain.
```

For `Not ready`, identify the blockers explicitly and state what must be resolved.

## Confidence

If the agent could not access important sources or verify a key fact, say so. Do not declare high confidence merely because the available documents are internally consistent.

## Do not use template completion as readiness

The following are not valid reasons on their own to declare readiness:

- every section has text;
- the document is long;
- all placeholders were removed;
- a project-management workspace exists;
- an architecture diagram exists;
- the AI found no more questions to ask.

Readiness depends on material uncertainty, not document cosmetics.