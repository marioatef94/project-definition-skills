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
7. Run deterministic repository validation before opening or updating a pull request.

## Validate locally

The repository validator uses only the Python standard library.

From the repository root:

```bash
python -X utf8 scripts/validate_repo.py
```

The same command runs in CI. See [`docs/validation.md`](docs/validation.md) for the checks it performs and the boundary between deterministic validation and behavioral evaluations.

Deterministic CI must pass before a pull request is considered structurally ready. Changes to observable skill behavior should also include relevant behavioral evaluation evidence before promotion to a stable release.

## Skill changes

For a new or modified skill:

- keep the skill name lowercase and kebab-case;
- ensure `SKILL.md` explains both what the skill does and when it should be used;
- use supporting files for large references or templates;
- preserve explicit distinctions between facts, assumptions, unknowns, recommendations, and decisions;
- define failure behavior when required information or capabilities are unavailable;
- add or update examples for material workflow changes;
- add or update behavioral evaluation cases when a change affects observable skill behavior.

## Pull requests

A pull request should explain:

- the problem being solved;
- the proposed behavior;
- compatibility or migration impact;
- how the change was validated.

For skill behavior changes, include both deterministic validation results and relevant behavioral evaluation evidence when available.

By contributing, you agree that your contribution is licensed under the repository's MIT License.
