# Project Definition Skills

Reusable, provider-agnostic Agent Skills for turning early ideas, existing notes, stakeholder input, and incomplete requirements into clear, reviewable project-definition documentation.

## Goals

Project Definition Skills is designed to work across technical and non-technical projects without requiring a specific documentation platform, project-management system, cloud service, repository host, or local toolchain.

The skills are intended to help an AI agent:

- discover what is already known before asking questions;
- identify material requirement gaps and unresolved assumptions;
- guide structured project discovery without forcing a fixed questionnaire;
- generate consistent project-definition documents from reusable templates;
- preserve facts, assumptions, unknowns, recommendations, and decisions as distinct concepts;
- publish or save outputs through whatever destination capabilities the user's agent provides;
- work equally well with cloud-hosted documents, project-management tools, repositories, or local files.

## Design principles

1. **Provider agnostic** — Skills describe required capabilities, not vendor-specific integrations.
2. **Storage agnostic** — Outputs may live remotely or locally; the skill does not mandate a destination.
3. **Human governed** — AI drafts and validates; humans establish authoritative project truth.
4. **Evidence first** — Missing information remains missing until supplied or verified.
5. **Adaptive discovery** — Ask only questions that materially improve the project definition.
6. **Progressive disclosure** — Load supporting references and templates only when needed.
7. **Reusable by default** — No client-, industry-, organization-, or implementation-specific assumptions in core skills.
8. **Minimum sufficient documentation** — Generate artifacts because they add value, not because a checklist exists.

## Repository structure

```text
project-definition-skills/
├── skills/                 # Portable Agent Skills
├── docs/                   # Standards and design guidance
├── .github/                # Contribution and issue templates
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── LICENSE
```

Each released skill will use the portable Agent Skills folder convention:

```text
skills/<skill-name>/
├── SKILL.md                # Required skill entry point
├── references/             # Optional supporting guidance
├── assets/                 # Optional templates and static resources
└── scripts/                # Optional deterministic helpers
```

## Planned first skill

The first skill will be `project-definition`: a guided workflow for moving from an idea or incomplete project context through discovery, structured requirements, research when necessary, project documentation, and delivery-readiness assessment.

The detailed behavior will be specified and reviewed before the skill is published.

## Project status

**Early development.** The repository foundation and standards are being established before the first stable skill release.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a change.

## Security

Please report security concerns according to [SECURITY.md](SECURITY.md).

## License

Licensed under the [MIT License](LICENSE).
