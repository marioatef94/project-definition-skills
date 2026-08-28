# Project Definition Skills

Reusable, provider-agnostic Agent Skills for turning early ideas, existing notes, stakeholder input, and incomplete requirements into clear, reviewable project-definition documentation.

The repository is designed for both technical and non-technical projects. It does not require a specific documentation platform, project-management system, repository host, cloud provider, or local toolchain.

## What this project is for

Project Definition Skills helps an AI agent guide a user from incomplete project context to a structured definition that is ready to review, share, and eventually execute.

The skills are intended to help an agent:

- discover what is already known before asking questions;
- identify material requirement gaps and unresolved assumptions;
- guide structured project discovery without forcing a fixed questionnaire;
- normalize requirements, constraints, decisions, risks, and open questions;
- determine the minimum useful set of documents for the project;
- generate consistent project-definition documents from reusable templates;
- preserve facts, assumptions, unknowns, recommendations, and decisions as distinct concepts;
- validate drafts before they become authoritative;
- publish or save outputs through whatever destination capabilities the user's agent provides;
- resume later and update an existing project definition instead of starting over.

## Example

A user can start with something as small as:

```text
I have an idea for a service that helps small businesses manage appointments.
Help me define the project properly.
```

The AI agent uses the `project-definition` skill to first understand what is already known, then asks only questions that materially affect the definition.

A simplified interaction might look like:

```text
Agent
I can help define this project. From your description I currently know:

- Problem area: appointment management
- Target audience: small businesses
- Project type: not yet confirmed

The highest-impact gaps are:

1. Who will create and manage appointments?
2. Will customers book directly, or will staff create bookings?
3. Are payments part of the first release?
4. Are reminders or notifications required?
5. Is this intended as software, a business process, or both?

I will not choose technologies or invent missing requirements unless you ask me to recommend options.
```

After clarification, the agent may propose a minimum documentation set:

```text
Proposed project definition

1. Project Overview            Required
2. Requirements Document       Required
3. Research                    Not currently required
4. Decision Record             Only if major choices are made
5. Architecture Overview       Only if the project requires a technical solution

Open items
- Payment scope is not decided
- Reminder channels are not decided

Readiness
READY WITH OPEN ITEMS
```

After human review, the same content can be saved to whatever destination is available and approved by the user.

## Example output

The exact files or remote documents depend on the project and destination. A local-file workflow could produce:

```text
project-definition/
├── project-overview.md
├── requirements.md
├── decisions.md
└── research/
    └── payment-options.md
```

A connected document or work-management system could instead receive equivalent pages, records, or work items without changing the core project-definition workflow.

The skill should never create duplicate editable sources of truth by default. The user chooses which destination is authoritative.

## Works with connected tools, MCPs, or local files

The skills are capability-based rather than provider-based.

An executing AI agent may use any available mechanism that can provide the required capability, including:

- MCP servers;
- native agent tools or connectors;
- document-management systems;
- project or work-management systems;
- repository integrations;
- cloud file storage;
- local filesystem access;
- plain Markdown or other document files.

The skill does **not** require any of these integrations. It should adapt to the capabilities actually available in the user's environment.

For example:

```text
Connected environment

User
  ↓
AI Agent + project-definition skill
  ↓
Capability discovery
  ├── Search existing documents
  ├── Read existing requirements
  ├── Create/update documents
  ├── Create work items, if requested
  └── Perform external research, if required
  ↓
User review
  ↓
Approved destination
```

Or completely locally:

```text
Local environment

User
  ↓
AI Agent + project-definition skill
  ↓
Read local notes / files
  ↓
Discovery + clarification
  ↓
Generate project definition
  ↓
Write local .md or document files
```

Provider-specific authentication, credentials, URLs, commands, and API behavior belong to the executing agent or integration layer, not to the core skill.

## Supported starting points

The skill is intended to handle more than greenfield ideas. A user may begin with:

- a one-sentence idea;
- an existing proposal;
- meeting notes or transcripts;
- stakeholder feedback;
- existing requirements;
- local documents;
- remote documents exposed through an agent tool;
- an existing project that needs a requirements review;
- several conflicting sources that need to be analyzed before clarification.

The agent should inspect available context first and avoid asking the user to repeat information that is already supported by the provided sources.

## Typical workflow

```text
Idea / existing material
        ↓
Context inventory
        ↓
Current-state synthesis
        ↓
Gap analysis
        ↓
Adaptive clarification
        ↓
Research, only when needed
        ↓
Requirement normalization
        ↓
Document selection
        ↓
Destination resolution
        ↓
Draft generation
        ↓
Validation
        ↓
Human review
        ↓
Publish / save
        ↓
Readiness assessment
```

See [`docs/project-definition-user-journey-v1.md`](docs/project-definition-user-journey-v1.md) for the detailed journey and [`docs/project-definition-skill-contract-v1.md`](docs/project-definition-skill-contract-v1.md) for the behavioral contract currently under design.

## Design principles

1. **Provider agnostic** — Skills describe required capabilities, not vendor-specific integrations.
2. **Storage agnostic** — Outputs may live remotely or locally; the skill does not mandate a destination.
3. **Human governed** — AI drafts and validates; humans establish authoritative project truth.
4. **Evidence first** — Missing information remains missing until supplied or verified.
5. **Adaptive discovery** — Ask only questions that materially improve the project definition.
6. **Progressive disclosure** — Load supporting references and templates only when needed.
7. **Reusable by default** — No client-, industry-, organization-, or implementation-specific assumptions in core skills.
8. **Minimum sufficient documentation** — Generate artifacts because they add value, not because a checklist exists.
9. **Safe failure** — Missing integrations or unavailable destinations must not silently change where authoritative information is stored.
10. **Resumable workflows** — Existing project definitions should be amended rather than regenerated unnecessarily.

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

The detailed behavior is being specified and reviewed before the first skill implementation is published.

## Project status

**Early development.** The repository foundation, behavioral contract, user journey, capability model, and documentation standards are being established before the first stable skill release.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a change.

## Security

Please report security concerns according to [SECURITY.md](SECURITY.md).

## License

Licensed under the [MIT License](LICENSE).
