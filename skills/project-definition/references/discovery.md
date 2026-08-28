# Discovery Guidance

Use this reference when converting incomplete project context into a reliable current-state model.

## Goal

Understand what is already known before asking questions. Discovery should reduce uncertainty, not create paperwork.

## Build the current-state model

Classify available information as:

- **Fact** — directly supported by user input or a trusted source;
- **Requirement** — expected behavior, outcome, rule, or capability;
- **Constraint** — a limit the project must respect;
- **Decision** — a choice already made;
- **Assumption** — plausible but unconfirmed;
- **Unknown** — information not yet established;
- **Conflict** — incompatible statements that require resolution;
- **Recommendation** — advice from the agent, never project truth by itself.

Preserve source traceability when practical.

## Context inventory

Consider only sources actually available and relevant, such as:

- conversation content;
- files supplied by the user;
- existing project documents;
- local project folders;
- connected knowledge systems;
- work-management records;
- repositories or prototypes.

Read the most relevant sources first. Fetch more only when needed to resolve a gap or conflict.

## Gap analysis

Identify gaps by potential impact, not by whether a template heading is empty.

Consider, when applicable:

- problem and intended outcome;
- users, beneficiaries, or stakeholders;
- scope and explicit non-goals;
- core workflows or use cases;
- functional behavior;
- business or operating rules;
- quality expectations;
- constraints and dependencies;
- data or content needs;
- privacy, security, safety, legal, or compliance concerns;
- external integrations or parties;
- cost or timeline constraints supplied by the user;
- success criteria;
- major risks;
- unresolved decisions;
- architecture or feasibility for technical projects.

Do not treat every category as mandatory.

## Question strategy

Ask a question only when the answer can materially affect at least one of:

- scope;
- user outcome;
- requirement behavior;
- cost or feasibility;
- risk;
- compliance or safety;
- dependency handling;
- architecture or solution direction;
- readiness.

Prefer 1–5 related questions in a turn.

Sequence:

1. ask the highest-impact unresolved questions;
2. update the current-state model from the answers;
3. reassess what remains material;
4. ask another small batch only when necessary.

Do not ask the user to repeat information already supported by accessible context.

## Deferred answers

Accept answers such as:

- unknown;
- decide later;
- not applicable;
- recommend an option;
- research this.

Do not convert a deferred answer into a guessed requirement. Keep it visible as an unknown, assumption, or decision required.

## Research gate

External research is justified when a material question depends on evidence that is not present in project context, such as current regulation, market evidence, platform constraints, compatibility, or vendor comparison.

Before substantial research, state the question being investigated and why it matters.

Research output must distinguish evidence, inference, recommendation, confidence, and remaining uncertainty.

## Existing-project mode

When existing documentation already exists:

1. discover the likely authoritative artifact;
2. summarize its current state;
3. identify gaps, contradictions, and stale assumptions;
4. ask only questions needed to resolve material issues;
5. propose amendments rather than creating a duplicate project definition.

Treat implementation artifacts as evidence of current reality, not automatically as intended requirements.