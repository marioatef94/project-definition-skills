# Project Definition Skills

[![Validate repository](https://github.com/marioatef94/project-definition-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/marioatef94/project-definition-skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Public Beta** — reusable, provider-agnostic Agent Skills for turning early ideas, existing notes, stakeholder input, and incomplete requirements into clear, reviewable project-definition documentation.

The repository is designed for technical and non-technical projects. The core skill does not require a specific documentation platform, project-management system, repository host, cloud provider, MCP server, or local toolchain.

## What it does

`project-definition` helps an AI agent move from incomplete context to a reliable project definition. It inspects what is already known, identifies material gaps, asks only high-value questions, normalizes confirmed requirements, proposes the minimum useful documentation set, validates drafts, keeps humans in control of authoritative content, and reports readiness without inventing missing information.

It can start from a one-sentence idea, proposal, meeting notes, transcript, stakeholder feedback, existing requirements, local files, connected documents, or an existing project that needs review and amendment.

## Quick start

Clone the repository:

```bash
git clone https://github.com/marioatef94/project-definition-skills.git
cd project-definition-skills
```

Install the skill into the directory your Agent Skills-compatible client uses:

```bash
python scripts/install_skill.py --skill project-definition --target /path/to/your/agent/skills
```

The target path is intentionally supplied by you because personal, global, workspace, and project skill directories differ between AI clients.

You can also copy `skills/project-definition/` manually.

Then ask the agent to use the skill, for example:

```text
Use the project-definition skill.
I have these meeting notes and a rough project idea. Review what I already have, ask me only the important missing questions, and prepare the minimum project-definition documents. Keep them local as Markdown files.
```

Or:

```text
Use the project-definition skill to review my existing requirements. Read the project documents available through my connected tools, identify gaps and conflicts, and propose updates. Do not publish anything until I approve the changes.
```

## Example

A user can start with:

```text
I have an idea for a service that helps small businesses manage appointments.
Help me define the project properly.
```

A good first response should synthesize the limited known context, identify the highest-impact unknowns, and avoid premature implementation choices. It might determine that the target audience is known but booking ownership, customer self-service, payments, reminders, and the exact project type still need clarification.

After clarification, the agent may propose a minimum documentation set such as:

```text
Proposed project definition

1. Project Overview            Required
2. Requirements Document       Required
3. Research                    Not currently required
4. Decision Record             Only if a major choice needs a durable record
5. Architecture Overview       Only if a technical solution justifies it

Open items
- Payment scope is not decided
- Reminder channels are not decided

Readiness
READY WITH OPEN ITEMS
```

The skill does not generate every template just because a template exists.

## Example output

For a local workflow:

```text
project-docs/
├── project-overview.md
├── requirements.md
├── decisions.md
└── research/
    └── payment-options.md
```

A connected documentation or work-management system may receive equivalent pages or records instead. The project-definition behavior remains the same.

The skill should not create duplicate editable sources of truth by default. The user chooses the authoritative destination.

## MCPs, connected tools, repositories, and local files

The skill is capability-based rather than provider-based.

An executing AI agent may satisfy required capabilities through MCP servers, native connectors, document systems, work-management systems, repository integrations, cloud storage, local filesystem access, or another compatible mechanism.

Provider-specific authentication, credentials, URLs, API behavior, and setup stay in the executing environment rather than the core skill.

The skill also works with **no persistence integration at all**. In that case it can generate complete drafts in the conversation and must state clearly that they were not saved.

```text
User
  ↓
AI Agent + project-definition
  ↓
Inspect available context
  ↓
Gap analysis + adaptive clarification
  ↓
Research only when needed
  ↓
Normalize requirements
  ↓
Select minimum useful documents
  ↓
Draft + validate
  ↓
Human review
  ↓
Save through an approved capability, if available
  ↓
Read back / verify persisted integrity when supported
  ↓
Readiness assessment
```

## Current beta skill

The first skill is [`skills/project-definition/`](skills/project-definition/):

```text
skills/project-definition/
├── SKILL.md
├── references/
│   ├── capabilities.md
│   ├── discovery.md
│   ├── requirements.md
│   ├── document-selection.md
│   ├── documentation-standard.md
│   ├── publishing.md
│   └── readiness.md
└── assets/
    ├── overview-template.md
    ├── requirements-template.md
    ├── research-template.md
    ├── decision-template.md
    └── architecture-overview-template.md
```

Supported v1 governed artifact types are Project/Product Overview (`OVR`), Requirements (`REQ`), Research/Discovery (`RES`), Decision Record (`DEC`), and Architecture Overview (`ARC`) when technically justified.

## Core behavior

The beta is built around these rules: inspect context before questioning; distinguish facts, assumptions, inferences, recommendations, unknowns, decisions, and observed implementation state; never manufacture requirements; never let current implementation silently supersede governed intent; keep requirements focused on intended behavior; distinguish target architecture from current-state snapshots; do not force software concepts onto non-technical work; generate minimum-sufficient documentation; use capability abstractions instead of providers; require human approval before authoritative material changes; verify connected-document hierarchy/links after publication when supported; never silently move the canonical source after a write failure; and amend existing authoritative documents instead of creating unnecessary duplicates.

The detailed contracts are in [`docs/project-definition-skill-contract-v1.md`](docs/project-definition-skill-contract-v1.md), [`docs/project-definition-user-journey-v1.md`](docs/project-definition-user-journey-v1.md), [`docs/capability-contract-v1.md`](docs/capability-contract-v1.md), [`docs/documentation-standard-v1.md`](docs/documentation-standard-v1.md), and the additive [`docs/project-definition-governance-hardening-v1.md`](docs/project-definition-governance-hardening-v1.md).

## Validation and evaluations

Run deterministic validation locally:

```bash
python -X utf8 scripts/validate_repo.py
```

CI runs the same validator and also smoke-tests the generic installer. Deterministic checks cover skill structure/frontmatter, resource references, relative Markdown links, evaluation-case structure, and repository consistency without third-party Python dependencies.

Behavioral quality is tested separately under [`evals/project-definition/`](evals/project-definition/). The suite contains **13 provider-neutral scenarios**, reproducible fixtures, a 10-dimension rubric, critical-failure rules, result-recording guidance, and a copy/paste runner guide at [`evals/project-definition/RUNNING-EVALS.md`](evals/project-definition/RUNNING-EVALS.md).

The original 10 scenarios retain their same-model smoke evidence. Cases 011–013 are governance regressions derived from real connected-document usage and do not claim independent passes until they are actually executed and recorded.

Initial same-model smoke results are committed only as regression evidence. They are explicitly marked `Self-smoke`; they are not represented as independent cross-agent validation.

See [`docs/validation.md`](docs/validation.md) for the validation boundary.

## Repository structure

```text
project-definition-skills/
├── skills/                 # Portable Agent Skills
├── evals/                  # Provider-neutral behavioral evaluations
├── scripts/                # Generic installer + deterministic validation
├── docs/                   # Standards, contracts, and design guidance
├── .github/                # Issues, PR template, and CI
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── LICENSE
```

## Beta status

The repository is usable as an open-source public beta. Deterministic validation is enforced in CI and the core behavioral suite is in place. Independent cross-agent evaluation is tracked as additional release-confidence work before a future stable `1.0` claim; lack of that evidence does not prevent users from evaluating and using the beta today.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), run the validator locally, and add or update behavioral cases when changing skill behavior.

## Security

Report security concerns according to [SECURITY.md](SECURITY.md). Do not include credentials, secrets, private client data, or sensitive evaluation material in issues or committed fixtures.

## License

Licensed under the [MIT License](LICENSE).