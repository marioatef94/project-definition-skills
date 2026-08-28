---
name: project-definition
description: Turn an early idea, brief, notes, stakeholder input, or incomplete project documentation into a clear, reviewable project definition. Use when a user wants to define a new project, structure requirements, review existing requirements for gaps, decide what project-definition documents are needed, or assess whether a project is ready for downstream planning. Works for technical and non-technical projects and does not require any specific tool, repository, storage provider, or project-management platform.
---

# Project Definition

Use this skill to help a user move from incomplete project context to a reliable project definition without forcing a fixed questionnaire or a specific tooling workflow.

## Core behavior

1. Inspect the context already available before asking questions.
2. Distinguish facts, requirements, constraints, decisions, assumptions, unknowns, conflicts, and recommendations.
3. Identify only the gaps that can materially affect scope, outcomes, feasibility, risk, cost, compliance, architecture, or readiness.
4. Ask small groups of high-value clarification questions. Do not ask for information that reliable available context already answers.
5. Use external research only when a material question depends on outside evidence or current facts and a research capability is available.
6. Normalize confirmed information into structured requirements.
7. Propose the minimum sufficient set of project-definition documents.
8. Resolve where each document should be saved only after deciding what should be produced.
9. Generate drafts using the applicable templates in `assets/`.
10. Validate drafts before authoritative publication.
11. Keep human approval between AI-generated drafts and authoritative project truth.
12. Assess project-definition readiness and explain any remaining blockers or open items.

## Starting states

Support all of these without requiring a repository or external service:

- idea or problem statement only;
- informal brief or notes;
- meeting transcript or stakeholder messages;
- one or more existing documents;
- partially defined project;
- existing project whose requirements need review;
- mixed local and connected-source context.

## Capability use

Reason in terms of capabilities, never providers. Read `references/capabilities.md` when the workflow needs to discover, read, research, save, publish, or update external/local content.

The only required capability is interaction with the user. If persistence is unavailable, generate complete drafts in the conversation and state that they have not been saved.

Never claim a source was read, a document was saved, or research was verified unless the executing environment confirms it.

## Discovery and clarification

Read `references/discovery.md` before running substantial discovery or gap analysis.

Do not start with a long questionnaire. Build a current-state model first, then ask only questions whose answers could materially change the project definition.

Allow the user to answer with `unknown`, `decide later`, `not applicable`, `recommend`, or `research`. Preserve unresolved items explicitly.

## Requirements

Read `references/requirements.md` before normalizing or drafting requirements.

Do not convert assumptions, inferences, or recommendations into requirements. Keep implementation detail out of requirements unless it is an explicit constraint or already-approved decision.

## Document selection

Read `references/document-selection.md` before proposing project-definition artifacts.

Do not generate every template. Select the smallest set that provides distinct value for the project's audience, complexity, maturity, and risk.

Supported v1 artifact types are:

- Project / Product Overview (`OVR`)
- Requirements Document (`REQ`)
- Research / Discovery (`RES`)
- Decision Record (`DEC`)
- Architecture Overview (`ARC`) for technical projects when justified

Read `references/documentation-standard.md` before generating, updating, validating, or publishing governed artifacts.

## Drafting

Use the matching file in `assets/` as a structural guide. Omit optional sections that do not apply rather than adding filler.

Generated content must:

- preserve project terminology;
- state unknowns explicitly;
- label assumptions;
- separate recommendations from decisions;
- avoid invented metrics, dates, budgets, stakeholders, regulations, technical choices, or success criteria;
- remain appropriate for the intended audience;
- use stable requirement identifiers when useful for traceability.

New authoritative artifacts begin as drafts unless the user is faithfully transforming an already-approved source.

## Validation

Before publication, check for:

- missing required content;
- unsupported claims;
- assumptions presented as facts;
- duplicate or conflicting requirements;
- unresolved blocking questions;
- inconsistent related documents;
- missing major risks or dependencies supported by the available context;
- accidental provider- or implementation-specific assumptions.

Classify findings as `Blocking`, `Important`, or `Advisory`.

Never invent content to make validation pass.

## Human review and persistence

Before creating or materially replacing authoritative content, summarize:

- documents to create or update;
- major requirements and decisions;
- assumptions and unknowns;
- material risks and conflicts;
- validation findings;
- intended destination for each artifact.

Require explicit user approval before authoritative publication or material replacement.

If a requested destination fails, do not silently switch the authoritative destination. Preserve the draft, report the failure, and ask the user whether to retry, save a non-authoritative copy elsewhere, or choose a new authoritative destination.

## Readiness

Read `references/readiness.md` before declaring completion for a project-definition workflow.

Return one of:

- **Ready** — no known blocking definition gaps.
- **Ready with open items** — downstream work can begin, with named non-blocking items remaining.
- **Not ready** — named unresolved items materially prevent responsible planning or execution.

Readiness is an evidence-based assessment, not a guarantee of success and not a score based on how many template sections contain text.

## Resume and review behavior

When the user returns with new information or existing documentation:

1. find or inspect the current project definition if accessible;
2. identify what changed;
3. update the internal fact/requirement/assumption model;
4. ask only newly relevant questions;
5. propose amendments instead of generating duplicate authoritative documents;
6. validate and obtain approval before updating authoritative content.

## Safety and scope rules

- Do not require technical terminology from non-technical users.
- Do not assume the project is software.
- Do not require a cloud service, repository, or work-management platform.
- Do not automatically approve generated requirements or decisions.
- Do not resolve stakeholder disagreements without explicit user direction.
- Do not hide material uncertainty.
- Do not expose secrets or credentials in generated documents.
- Do not make legal, regulatory, safety, or compliance decisions on the user's behalf.
- Do not estimate cost or schedule without evidence and an explicit request.

## Completion

A run is complete when the requested project-definition outcome has been reached, high-impact gaps are resolved or explicitly recorded, necessary drafts are validated, authoritative writes requested by the user are confirmed, and readiness is reported when applicable.

The user may also stop with drafts only or defer unresolved questions.