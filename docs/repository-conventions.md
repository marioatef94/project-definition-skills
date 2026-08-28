# Repository Conventions

## Skill layout

A skill lives under `skills/<skill-name>/` and must contain `SKILL.md`.

Skill names use lowercase kebab-case and should describe a reusable capability rather than a vendor, client, or implementation.

Supporting resources may be organized as:

- `references/` — standards, checklists, domain-neutral guidance;
- `assets/` — templates and static resources used in outputs;
- `scripts/` — deterministic helpers when instructions alone are insufficient.

## Scope rules

Core skills must not contain:

- provider credentials or connection details;
- organization- or client-specific requirements;
- hard-coded project names or identifiers;
- assumptions about one project-management workflow;
- assumptions that a source-code repository already exists;
- assumptions that the user is technical.

## Writing rules

Skill instructions should:

- use imperative, testable language;
- define when the skill should and should not run;
- define required inputs and acceptable missing inputs;
- describe discovery before clarification;
- specify validation and completion criteria;
- identify safety and anti-hallucination constraints;
- keep examples generic.

## Versioning

Repository releases follow Semantic Versioning once the first public release is made. Breaking changes to skill behavior or documented contracts require a major version increment after `1.0.0`.

Until then, the project may use `0.x` releases while the public contracts are still evolving.
