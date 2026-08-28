# Skills

This directory contains reusable Agent Skills.

Each skill lives in its own kebab-case directory and includes a `SKILL.md` entry point. Skills should remain provider-agnostic and project-agnostic; integrations are expressed as capabilities that the executing agent may satisfy with tools available in its environment.

## Available

| Skill | Status | Purpose |
|---|---|---|
| [`project-definition`](project-definition/) | Beta | Turn ideas, briefs, notes, or incomplete requirements into a structured, reviewable project definition with adaptive discovery and readiness assessment. |

No stable v1 skill has been released yet. Beta skills should be evaluated across multiple project types and execution environments before being promoted to stable.