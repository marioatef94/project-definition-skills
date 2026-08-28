# Repository Validation

The repository includes deterministic validation for structural and consistency checks that do not require an AI model.

The validator is intentionally dependency-light: it uses only the Python standard library.

## Run locally

From the repository root:

```bash
python -X utf8 scripts/validate_repo.py
```

You may also validate another checkout explicitly:

```bash
python -X utf8 scripts/validate_repo.py --root /path/to/project-definition-skills
```

A successful run exits with code `0`. Validation errors exit with code `1`.

## What is validated

The validator currently checks:

- required open-source repository files exist;
- each directory under `skills/` has a `SKILL.md`;
- skill directory names use lowercase kebab-case;
- `SKILL.md` contains YAML frontmatter with `name` and `description`;
- the frontmatter `name` matches the skill directory;
- basic skill metadata length constraints;
- local `references/`, `assets/`, and `scripts/` paths named by `SKILL.md` exist;
- relative Markdown links resolve to existing repository files or directories;
- the project-definition evaluation suite contains its required support files;
- evaluation case filenames follow the numbered kebab-case convention;
- evaluation cases contain the required behavioral sections and those sections are not empty.

The validator emits a warning when a `SKILL.md` grows beyond 500 lines so detailed guidance can be moved into progressive-disclosure resources.

## What is not validated

Deterministic validation cannot prove that an AI agent will follow the skill correctly.

It does not evaluate:

- quality of clarification questions;
- hallucinated project requirements in model output;
- whether an agent respects human approval boundaries at runtime;
- behavioral portability across models or clients;
- semantic quality of generated project documents;
- research quality or evidence selection.

Those concerns belong to the behavioral evaluation suite under `evals/project-definition/`.

## CI

`.github/workflows/validate.yml` runs the validator for pull requests, pushes to `main`, and manual workflow dispatches.

The workflow uses the supported major versions of the official checkout and Python-setup actions and runs Python 3.12. CI intentionally uses the same validation command contributors run locally so local and hosted validation behavior stay aligned.

## Adding new deterministic checks

A new check should be added only when all of the following are true:

1. the rule is objectively testable without an AI model;
2. the rule is generic enough to protect repository or Agent Skill consistency;
3. a failure message can explain exactly what the contributor needs to fix;
4. the check does not hard-code a particular execution provider unless the repository itself explicitly adopts that provider-specific convention.

Behavioral expectations should normally be added to the evaluation suite instead of encoded as brittle text-matching rules.
