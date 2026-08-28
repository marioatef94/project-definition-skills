# Contributing

Thank you for helping improve Project Definition Skills.

## Before contributing

Please keep changes aligned with the repository's core goals:

- provider-agnostic behavior;
- reusable workflows;
- clear human approval boundaries;
- evidence-first reasoning;
- minimal unnecessary documentation;
- portability across compatible AI agents and execution environments.

## Development workflow

1. Open or reference an issue for material changes when practical.
2. Create a focused branch from `main`.
3. Keep each pull request limited to one coherent change.
4. Update documentation when behavior or contracts change.
5. Include examples or validation evidence for changes to skill behavior.
6. Avoid introducing provider-, client-, or project-specific assumptions into core skills.

## Skill changes

For a new or modified skill:

- keep the skill name lowercase and kebab-case;
- ensure `SKILL.md` explains both what the skill does and when it should be used;
- use supporting files for large references or templates;
- preserve explicit distinctions between facts, assumptions, unknowns, recommendations, and decisions;
- define failure behavior when required information or capabilities are unavailable;
- add or update examples for material workflow changes.

## Pull requests

A pull request should explain:

- the problem being solved;
- the proposed behavior;
- compatibility or migration impact;
- how the change was validated.

By contributing, you agree that your contribution is licensed under the repository's MIT License.
