---
name: project-definition
description: Turn an early idea, brief, notes, stakeholder input, or incomplete project documentation into a clear, reviewable project definition. Use when a user wants to define a new project, structure requirements, review existing requirements for gaps, decide what project-definition documents are needed, or assess whether a project is ready for downstream planning. Works for technical and non-technical projects and does not require any specific tool, repository, storage provider, or project-management platform.
---

# Project Definition

Use this skill to help a user move from incomplete project context to a reliable project definition without forcing a fixed questionnaire or a specific tooling workflow.

## Core behavior

1. Inspect the context already available before asking questions.
2. Distinguish facts, requirements, constraints, decisions, assumptions, unknowns, conflicts, recommendations, and observed implementation state.
3. Identify only the gaps that can materially affect scope, outcomes, feasibility, risk, cost, compliance, architecture, or readiness.
4. Ask small groups of high-value clarification questions. Do not ask for information that reliable available context already answers.
5. Use external research only when a material question depends on outside evidence or current facts and a research capability is available.
6. Normalize confirmed information into structured requirements without letting observed implementation silently redefine project intent.
7. Propose the minimum sufficient set of project-definition documents and keep each artifact semantically focused on its governance role.
8. Resolve where each document should be saved only after deciding what should be produced.
9. Generate drafts using the applicable templates in `assets/`.
10. Validate drafts before authoritative publication, including cross-document consistency, lifecycle/status semantics, and relationship integrity.
11. Keep human approval between AI-generated drafts and authoritative project truth.
12. After connected or local authoritative writes, verify the persisted result when the environment supports read-back or relationship inspection.
13. Assess project-definition readiness and explain any remaining blockers or open items.

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

Reason in terms of capabilities, never providers. Read `references/capabilities.md` when the workflow needs to discover, read, research, save, publish, update, link, or verify external/local content.

The only required capability is interaction with the user. If persistence is unavailable, generate complete drafts in the conversation and state that they have not been saved.

Never claim a source was read, a document was saved, a relationship was created, or research was verified unless the executing environment confirms it.

## Discovery and clarification

Read `references/discovery.md` before running substantial discovery or gap analysis.

Do not start with a long questionnaire. Build a current-state model first, then ask only questions whose answers could materially change the project definition.

Allow the user to answer with `unknown`, `decide later`, `not applicable`, `recommend`, or `research`. Preserve unresolved items explicitly.

Treat source code, deployed behavior, prototypes, work items, existing configuration, and other implementation artifacts as **evidence of current state** unless the project has explicitly designated them as authoritative requirements or decisions.

If observed implementation conflicts with an explicit requirement, constraint, or approved decision:

1. preserve the governed intent unchanged;
2. record the implementation mismatch separately;
3. explain impact when known;
4. label any proposed resolution as a recommendation;
5. require human approval before changing the requirement or decision.

Implementation convenience, recency, or existing behavior is never sufficient by itself to supersede governed intent.

## Requirements

Read `references/requirements.md` before normalizing or drafting requirements.

Do not convert assumptions, inferences, recommendations, implementation observations, or current defects into requirements. Keep implementation detail out of requirements unless it is an explicit constraint or already-approved decision.

A requirements artifact should describe intended behavior. Statements such as `currently missing`, `bug`, `current production config`, `implementation uses`, or `required fix` belong in a separate current-state/gap analysis or clearly separated non-authoritative review section, not in the requirement statement itself.

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

Keep artifact roles distinct. Do not use a requirements document as an implementation-status report, a vision/overview as a volatile code snapshot, or a decision record as a place to silently ratify whatever the current implementation happens to do.

When current-state analysis is useful but does not justify a new governed artifact type, present it as a clearly labeled dated snapshot or review output and link it to the governed artifacts it evaluates.

## Drafting

Use the matching file in `assets/` as a structural guide. Omit optional sections that do not apply rather than adding filler.

Generated content must:

- preserve project terminology;
- state unknowns explicitly;
- label assumptions;
- separate recommendations from decisions;
- keep intended behavior separate from observed implementation state;
- avoid invented metrics, dates, budgets, stakeholders, regulations, technical choices, or success criteria;
- remain appropriate for the intended audience;
- use stable requirement identifiers when useful for traceability.

New authoritative artifacts begin as drafts unless the user is faithfully transforming an already-approved source.

## Validation

Before publication, check for:

- missing required content;
- unsupported claims;
- assumptions presented as facts;
- implementation observations presented as requirements or decisions;
- implementation behavior silently superseding governed intent;
- duplicate or conflicting requirements;
- unresolved blocking questions;
- inconsistent related documents;
- artifact-role leakage, such as current bugs embedded inside requirement statements or volatile implementation details dominating a stable vision artifact;
- lifecycle/status misuse, especially observed-state snapshots labeled as durable authoritative intent;
- broken, placeholder, or non-functional relationships between related artifacts when actual link/reference capabilities exist;
- missing major risks or dependencies supported by the available context;
- accidental provider- or implementation-specific assumptions.

Classify findings as `Blocking`, `Important`, or `Advisory`.

Never invent content to make validation pass.

## Human review and persistence

Before creating or materially replacing authoritative content, summarize:

- documents to create or update;
- major requirements and approved decisions;
- proposed changes to existing requirements or decisions;
- assumptions and unknowns;
- material risks and conflicts;
- implementation mismatches that need human resolution;
- validation findings;
- intended destination for each artifact.

Require explicit user approval before authoritative publication or material replacement. A recommendation based on current implementation is not approval to change project intent.

Read `references/publishing.md` before authoritative persistence to a connected document system, repository, filesystem, or other destination when the environment supports verification.

If a requested destination fails, do not silently switch the authoritative destination. Preserve the draft, report the failure, and ask the user whether to retry, save a non-authoritative copy elsewhere, or choose a new authoritative destination.

After a successful authoritative write, verify as much of the persisted result as the environment can inspect, including the destination/reference and, when relevant, title, status, parent/container, body revision, and relationships to other governed artifacts. Do not claim that a link, hierarchy, or relationship exists merely because bracketed text or a page title was written.

If the destination confirms the write but the environment cannot read it back or inspect relationships, report the write as confirmed and the integrity check as unverified rather than pretending both were verified.

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
3. update the internal fact/requirement/assumption/current-state model;
4. ask only newly relevant questions;
5. propose amendments instead of generating duplicate authoritative documents;
6. keep implementation drift separate from proposed intent changes;
7. validate and obtain approval before updating authoritative content;
8. verify the persisted amendment when supported.

## Safety and scope rules

- Do not require technical terminology from non-technical users.
- Do not assume the project is software.
- Do not require a cloud service, repository, or work-management platform.
- Do not automatically approve generated requirements or decisions.
- Do not allow implementation state to silently override requirements, constraints, or decisions.
- Do not resolve stakeholder disagreements without explicit user direction.
- Do not hide material uncertainty.
- Do not expose secrets or credentials in generated documents.
- Do not make legal, regulatory, safety, or compliance decisions on the user's behalf.
- Do not estimate cost or schedule without evidence and an explicit request.

## Completion

A run is complete when the requested project-definition outcome has been reached, high-impact gaps are resolved or explicitly recorded, necessary drafts are validated, authoritative writes requested by the user are confirmed, persisted relationships/integrity are verified when supported, and readiness is reported when applicable.

The user may also stop with drafts only or defer unresolved questions.