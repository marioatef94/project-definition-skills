# Project Definition Skill Contract v1

Status: Draft

This document defines the behavioral contract for the first reusable skill in this repository. It intentionally describes capabilities and outcomes rather than any specific storage provider, project-management platform, repository host, or AI client.

## 1. Purpose

The `project-definition` skill helps a user turn an early idea, incomplete brief, meeting notes, existing documents, stakeholder input, or partially defined project into a coherent, reviewable project definition.

The skill is intended for both technical and non-technical projects and users.

It should help the executing AI agent:

- understand what is already known;
- identify missing information that materially affects the project;
- ask focused clarification questions;
- separate facts, assumptions, unknowns, recommendations, and decisions;
- structure requirements consistently;
- identify when additional research is justified;
- select only the documentation artifacts that add value;
- generate draft project-definition documents;
- validate those drafts before publication or local persistence;
- preserve human control over authoritative requirements and decisions;
- assess whether the project definition is sufficiently complete for downstream planning or execution.

## 2. When to use this skill

Use this skill when the user wants to:

- define a new project from an idea or problem statement;
- turn an informal brief into structured project requirements;
- consolidate scattered notes or documents into a project definition;
- discover requirement gaps before work begins;
- generate or improve a project overview or requirements document;
- prepare an existing partially defined project for planning or delivery;
- assess whether enough information exists to begin execution responsibly.

The user does not need to know document terminology such as PRD, requirements specification, or architecture overview. The skill should infer the appropriate artifacts from the user's goal and context.

## 3. When not to use this skill

Do not use this skill as the primary workflow for:

- implementing source code or project deliverables;
- managing day-to-day task execution;
- tracking sprint or work-item status;
- incident response;
- routine maintenance of an already established project definition;
- generating documentation unrelated to defining project scope, requirements, constraints, or initial direction.

A later reusable skill may cover those workflows independently.

## 4. Supported starting states

The skill must support all of the following without assuming a repository or project-management workspace already exists.

### 4.1 Idea only

The user has only a short concept, problem, or goal.

The skill should begin discovery and progressively establish project context.

### 4.2 Existing notes or conversations

The user has meeting notes, messages, transcripts, emails, sketches, or informal requirements.

The skill should extract known information first and ask only about material gaps.

### 4.3 Existing documents

The user has one or more project documents.

The skill should inspect and normalize them before proposing new documents. It must not create duplicates simply because the existing documents use different names or structures.

### 4.4 Existing project with incomplete definition

The project may already have files, work items, prototypes, or implementation artifacts but lacks a reliable project definition.

The skill should treat existing artifacts as evidence, not automatically as authoritative requirements.

## 5. Capability model

The skill must remain provider-agnostic. It should reason in terms of available capabilities.

Possible capabilities include:

- read user-provided files;
- search existing project information;
- read collaborative documents;
- read project-management records;
- read local files or directories;
- create a collaborative document;
- create or update a project-management record;
- write a local file;
- create or update a repository file;
- perform web research when explicitly permitted or clearly required;
- request human approval.

No capability is mandatory except the ability to interact with the user.

If no external write capability exists, the skill must still be able to generate complete drafts in the conversation for the user to save manually.

## 6. Core workflow

The skill follows this logical workflow. The AI agent may compress or revisit steps when context already provides sufficient evidence.

### Step 1 — Understand the user's goal

Determine:

- what project or problem is being defined;
- what outcome the user wants from the current session;
- what material the user already has;
- whether existing authoritative documentation may already exist;
- whether the user wants drafts only or wants the agent to save/publish approved outputs.

Do not start with a long fixed questionnaire.

### Step 2 — Discover existing context

Inspect all relevant authorized sources before asking questions.

Extract and classify information as:

- Fact
- Assumption
- Inference
- Recommendation
- Unknown
- Decision

Maintain traceability to the source when practical.

### Step 3 — Build a gap model

Identify missing information by impact rather than by template completeness.

Prioritize gaps that could materially change:

- project purpose;
- users or stakeholders;
- scope;
- requirements;
- business or operating rules;
- data needs;
- security, privacy, safety, or compliance;
- integrations or dependencies;
- cost;
- timeline or constraints;
- architecture or solution direction for technical projects;
- success criteria;
- major risks.

Do not ask low-value questions merely to fill headings.

### Step 4 — Clarify adaptively

Ask concise groups of related questions.

Rules:

- do not ask for information already available from reliable context;
- explain why a question matters when the reason is not obvious;
- prioritize blocking or high-impact questions first;
- allow the user to answer partially;
- preserve unresolved items as explicit unknowns;
- never invent an answer to avoid an open question.

### Step 5 — Invoke research only when justified

Research is conditional, not mandatory.

Recommend or perform research when a material requirement or decision depends on facts that cannot be established from the provided project context.

Examples include:

- regulatory or policy constraints;
- vendor or platform comparison;
- market or competitor evidence;
- feasibility assumptions;
- current external limits or pricing;
- compatibility or standards questions.

Clearly distinguish externally verified information from user-supplied project truth.

### Step 6 — Normalize requirements

Convert the gathered information into structured requirements.

Where relevant, distinguish:

- functional requirements;
- business or operating rules;
- non-functional requirements;
- constraints;
- assumptions;
- dependencies;
- risks;
- open questions;
- out-of-scope items;
- future considerations.

Requirements should be specific enough to review and test conceptually without prematurely dictating implementation.

### Step 7 — Select the minimum sufficient document set

Do not generate every available template.

Choose documents based on audience, complexity, risk, project maturity, and expected value.

The initial skill may recommend or generate these project-definition artifacts when appropriate:

- Project / Product Overview
- Product / Project Requirements Document
- Research / Discovery document
- Decision Record
- Architecture Overview for technical projects

More specialized engineering or operational documents are outside this skill's primary scope unless needed to establish the initial project definition.

### Step 8 — Generate drafts

Use the repository's approved templates and documentation standard.

Generation rules:

- preserve known terminology from the user's project;
- do not convert assumptions into facts;
- mark unresolved information explicitly;
- avoid generic filler text;
- avoid implementation detail unless it is already an explicit project constraint or decision;
- maintain stable requirement identifiers when the selected template requires them;
- keep documents useful to both their intended audience and future AI consumers.

All newly generated authoritative artifacts begin as drafts unless the user explicitly provides an already approved source that is being faithfully transformed.

### Step 9 — Validate

Before saving or publishing, validate the proposed document set.

Validation should check:

- required sections for the selected template;
- internal consistency;
- duplicate or conflicting requirements;
- unresolved high-impact questions;
- unsupported claims;
- assumptions presented as facts;
- missing major risks or dependencies supported by the available context;
- consistency between related generated documents;
- presence of any required metadata.

Validation must not fabricate missing content to produce a passing result.

### Step 10 — Review with the user

Before authoritative publication or replacement of existing content, present:

- proposed documents;
- important assumptions;
- unresolved questions;
- significant recommendations;
- identified conflicts;
- material risks;
- proposed destination when one is available.

The user must remain able to revise, reject, or defer any proposed authoritative content.

### Step 11 — Publish or save through available capabilities

After approval, write the selected artifacts through the capabilities available to the executing AI agent.

The skill must not hard-code where documents live.

Possible destinations include:

- collaborative documentation systems;
- project-management systems;
- repositories;
- local Markdown or text files;
- other user-approved document stores.

If the chosen destination becomes unavailable, do not silently choose a different canonical destination. Preserve the draft and ask the user how to proceed.

### Step 12 — Assess definition readiness

After the project-definition artifacts are reviewed, assess whether the project has enough reliable information to move into downstream planning or execution.

Readiness is not a numeric score by default. Report it as a structured assessment.

Check, where applicable:

- problem and goals are understood;
- primary users or stakeholders are identified;
- scope and non-scope are clear enough;
- major requirements are documented;
- critical business or operating rules are explicit;
- high-impact unknowns are resolved or visibly accepted;
- major constraints and dependencies are known;
- major risks are visible;
- significant decisions are captured;
- technical projects have enough initial architecture direction to avoid obvious rework;
- success criteria exist where the project needs measurable outcomes.

Return one of:

- **Ready** — no known blocking definition gaps;
- **Ready with open items** — downstream work can begin, but named non-blocking gaps remain;
- **Not ready** — one or more named gaps materially prevent responsible planning or execution.

Never declare readiness solely because every template section contains text.

## 7. Question strategy

The skill must use adaptive questioning rather than a fixed questionnaire.

A question is justified when its answer can materially affect at least one of:

- scope;
- user outcome;
- requirement behavior;
- project cost;
- risk;
- architecture or feasibility;
- security, privacy, safety, or compliance;
- dependencies;
- delivery readiness.

Prefer 1–5 related high-value questions in a turn rather than a long survey.

If the user explicitly asks for a rapid or lightweight definition, minimize questions and surface more assumptions and unknowns instead of pretending they are resolved.

## 8. Document destination abstraction

The skill separates document content from document destination.

A destination adapter or external capability may provide operations such as:

- discover existing documents;
- read a document;
- create a document;
- update a document;
- create folders, pages, records, or files;
- link related artifacts.

The core skill must not rely on vendor-specific fields, IDs, URLs, or workflows.

If a destination has platform-specific formatting limitations, adapt presentation without changing the underlying project-definition semantics.

## 9. Human authority and approval

AI may:

- discover;
- extract;
- organize;
- ask;
- analyze;
- draft;
- validate;
- recommend.

AI must not silently:

- approve requirements;
- resolve stakeholder disagreement;
- turn recommendations into decisions;
- overwrite authoritative content;
- change the canonical destination;
- hide material unknowns;
- delete historical project-definition records.

Explicit human approval is required before publishing a new artifact as authoritative or materially replacing existing authoritative content.

## 10. Safe failure behavior

When a required capability, source, or answer is unavailable:

1. state what is unavailable;
2. explain how it affects confidence or completion;
3. continue with unaffected work when useful;
4. preserve missing information as an unknown;
5. do not invent a replacement;
6. do not silently change destination or source-of-truth behavior.

## 11. Privacy and confidentiality

The skill must minimize unnecessary exposure of project information.

- Access only sources relevant to the user's request.
- Do not copy sensitive source content into public outputs unless the user explicitly intends that destination.
- Do not include credentials, secrets, private keys, access tokens, or authentication material in generated documents.
- When examples are needed, prefer sanitized or generic examples.

## 12. Portability requirements

The skill is portable only if its core behavior does not depend on:

- a specific AI model or client;
- a specific project-management system;
- a specific document platform;
- a specific repository provider;
- a source-code repository existing at all;
- the user being a developer;
- the project being software.

Optional environment-specific capabilities may enhance execution but must not redefine the core workflow.

## 13. Progressive disclosure

`SKILL.md` should remain focused enough to load economically.

Detailed reusable material should be split into referenced resources, expected initially to include:

- documentation taxonomy and lifecycle;
- requirement classification guidance;
- adaptive discovery guidance;
- document-selection guidance;
- readiness criteria;
- templates for supported artifact types;
- generic examples.

Load only the references needed for the current project and current stage.

## 14. Completion criteria

A run of the skill is complete when the user's requested project-definition outcome has been reached and the agent has:

- inspected relevant available context;
- resolved or explicitly recorded high-impact gaps;
- generated only the necessary document set;
- validated the drafts;
- surfaced assumptions, unknowns, risks, and conflicts;
- obtained required human approval for authoritative publication;
- saved or published approved artifacts when the user requested it and a suitable capability exists;
- returned a project-definition readiness assessment when applicable.

The skill may end earlier when the user chooses to stop, defer unresolved questions, or request drafts only.

## 15. Non-goals for v1

The first version will not attempt to:

- define one universal project-management workflow;
- automate implementation or delivery;
- assign work to teams;
- estimate project cost or timeline without explicit evidence and user request;
- make legal, regulatory, or compliance decisions on the user's behalf;
- automatically approve generated requirements;
- require a specific canonical storage system;
- generate every possible documentation artifact.

## 16. Initial implementation shape

The shipped skill package is:

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

This mirrors the "Current beta skill" listing in `README.md`. `references/capabilities.md` (capability-detection guidance) and `references/publishing.md` (destination write/verify guidance) were added during implementation to keep `SKILL.md` itself short per Section 13, and `assets/project-overview-template.md` was renamed to `assets/overview-template.md`; neither change was reflected back into this contract until now. Keep this section and the README listing in sync going forward — `scripts/validate_repo.py` checks that resources referenced by `SKILL.md` actually exist, but it does not diff this section against the README, so a manual check is still required whenever the reference set changes.
