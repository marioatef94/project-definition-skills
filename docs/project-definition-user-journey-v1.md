# Project Definition User Journey v1

Status: Draft

This document defines the intended end-to-end user experience for the `project-definition` skill. It is provider-agnostic, storage-agnostic, and applicable to both technical and non-technical projects.

The journey is designed around one principle:

> Understand what is already known, ask only what materially matters, produce the minimum sufficient set of project-definition documents, and never turn an assumption into authoritative truth without the user's knowledge.

## 1. Supported starting points

The skill must support users who begin with any of the following:

- only an idea;
- a problem statement;
- an existing brief;
- meeting notes;
- stakeholder messages;
- an existing requirements document;
- one or more local files;
- content available through connected tools;
- an existing but incomplete project definition;
- a combination of the above.

A repository, project-management system, documentation platform, or cloud account must never be required to start.

## 2. Entry experience

The skill may be explicitly invoked or selected by the AI agent when the user's intent is clearly project-definition work.

Example intents include:

- "I have a new project idea."
- "Help me define the requirements for this project."
- "Turn these notes into a proper project definition."
- "I need a PRD for this initiative."
- "Review these requirements and tell me what is missing."

On entry, the agent should not begin with a large fixed questionnaire.

It should first determine what context is already available.

## 3. Phase A — Context inventory

The agent inventories available inputs before asking substantive questions.

### 3.1 Discover available context

The agent should inspect only the sources it is actually authorized and able to access.

Potential context sources include:

- content supplied in the conversation;
- attached files;
- local files visible to the agent;
- connected document systems;
- connected work-management systems;
- repositories;
- existing project folders;
- other agent-accessible knowledge sources.

The skill defines capabilities, not vendor names.

### 3.2 Build a context inventory

Internally classify discovered material as:

- primary project input;
- supporting evidence;
- previous decision;
- requirement candidate;
- assumption;
- conflicting information;
- irrelevant/background information.

### 3.3 Do not over-fetch

Use progressive disclosure. Read the most relevant material first, then fetch additional context only when a gap or conflict requires it.

## 4. Phase B — Current-state synthesis

Before asking questions, the agent produces an internal synthesis of what is already known.

The synthesis should distinguish:

- Facts — directly supported by user input or trusted source material.
- Requirements — explicit statements of expected behavior or outcome.
- Constraints — externally or internally imposed limits.
- Decisions — choices already made.
- Assumptions — plausible but unconfirmed statements.
- Unknowns — missing information.
- Conflicts — incompatible statements that require resolution.
- Recommendations — agent advice, clearly separated from facts.

The agent must never silently convert an assumption, inference, or recommendation into a requirement.

## 5. Phase C — Definition gap analysis

The agent evaluates whether the available information is sufficient to define the project reliably.

The analysis should consider, when relevant:

- problem and desired outcome;
- target users or beneficiaries;
- project scope;
- explicit non-goals;
- core workflows or use cases;
- functional requirements;
- business rules;
- quality and non-functional expectations;
- constraints;
- dependencies;
- data/content needs;
- privacy, security, legal, or compliance concerns;
- integrations or external parties;
- operational considerations;
- success criteria;
- risks;
- unresolved decisions;
- delivery assumptions.

Not every category applies to every project.

The skill must avoid treating software-project concerns as mandatory for non-technical projects.

## 6. Phase D — Adaptive clarification

Only after the gap analysis should the agent ask questions.

### 6.1 Prioritize high-impact gaps

Questions should be ranked by whether the answer can materially change:

- project scope;
- user experience;
- requirements;
- cost or feasibility;
- architecture or implementation direction;
- risk;
- legal/compliance obligations;
- delivery readiness.

### 6.2 Group related questions

Prefer a small coherent group of questions over a long interrogation.

Recommended behavior:

1. ask a small batch of the highest-value questions;
2. receive answers;
3. update the internal model;
4. reassess remaining gaps;
5. ask another batch only if needed.

### 6.3 Do not ask what can already be answered

If an accessible source contains the answer with sufficient confidence, use it and cite/reference that source in the resulting artifact where appropriate.

### 6.4 Allow the user to defer

The user may answer:

- unknown;
- decide later;
- not applicable;
- make a recommendation;
- research this.

Deferred items must remain explicit rather than being invented by the agent.

## 7. Phase E — Research gate

Research is conditional, not automatic.

Trigger research when a material question depends on external evidence, comparison, verification, or current facts that are not already available.

Examples include:

- market or competitor questions;
- regulatory or compliance requirements;
- vendor/tool comparisons;
- pricing/cost validation;
- feasibility assumptions;
- standards or compatibility questions.

Before substantial research, the agent should make clear what question it is trying to answer and why the answer matters.

Research output must separate:

- evidence;
- source-derived facts;
- inference;
- recommendation;
- confidence;
- unresolved uncertainty.

Research must not silently become a decision.

## 8. Phase F — Requirement normalization

Once sufficient context exists, normalize project requirements into a consistent model.

When applicable, distinguish:

- functional requirements;
- business rules;
- non-functional requirements;
- constraints;
- assumptions;
- dependencies;
- open questions;
- decisions required.

Requirements should be:

- unambiguous enough to review;
- independently understandable where practical;
- free of duplicated meaning;
- traceable within the generated documentation;
- written in language appropriate to the intended audience.

Stable local requirement identifiers may be assigned when the selected document type benefits from traceability.

## 9. Phase G — Document plan

The agent determines the minimum sufficient document set.

It must not blindly generate every available template.

Possible artifacts include:

- project/product overview;
- product/project requirements document;
- research/discovery document;
- decision record;
- architecture overview for technical projects;
- other supported artifacts when justified by the project context.

The agent presents the proposed document set and why each artifact is useful.

Example:

```text
Proposed documentation

Required
- Project Overview — establishes shared project context
- Requirements Document — captures scope and requirements

Conditional
- Research: Payment Options — unresolved evidence-dependent decision

Not currently needed
- Architecture Overview — no implementation architecture has been selected yet
```

The user may accept, remove, or add artifacts.

## 10. Phase H — Destination resolution

Only after knowing what should be produced does the agent determine where outputs should go.

The skill must remain destination-agnostic.

A destination may be:

- a local directory;
- Markdown files;
- another supported local document format;
- a connected documentation service;
- a connected work-management service;
- a repository;
- a combination of destinations, provided each artifact has one authoritative destination.

### 10.1 Existing destination preference

If the user already has an established documentation location, prefer it rather than creating a second source of truth.

### 10.2 Ask only when necessary

If no destination can be inferred, ask the user where the documents should be saved.

### 10.3 Safe fallback

If the requested destination cannot be written to, do not silently choose another authoritative destination.

Instead:

- explain the limitation;
- retain or present the generated draft;
- offer available alternatives;
- let the user decide.

## 11. Phase I — Draft generation

Generate drafts using the applicable templates and all confirmed context.

The draft must:

- preserve known facts;
- label assumptions;
- expose unresolved questions;
- avoid invented metrics, deadlines, stakeholders, constraints, or implementation choices;
- clearly separate recommendations from requirements;
- use an audience-appropriate level of technical detail;
- avoid empty boilerplate sections that do not apply.

Generated documents start as drafts unless the user explicitly establishes a different governed workflow.

## 12. Phase J — Validation

Before asking the user to approve or publish, validate the generated project definition.

Validation should check, as applicable:

- required sections are present;
- critical gaps are visible;
- unresolved assumptions are labeled;
- conflicting requirements are surfaced;
- duplicate requirements are removed or reconciled;
- scope and non-goals are distinguishable;
- requirement language is testable/reviewable where appropriate;
- document relationships are consistent;
- no unsupported claim has been silently introduced;
- generated documents match the selected templates and audience.

Validation should report findings by severity rather than pretending every document must be perfect.

Suggested severity model:

- Blocking — the project definition is unsafe or misleading without resolution.
- Important — should be addressed but may not prevent progress.
- Advisory — useful improvement with limited delivery impact.

## 13. Phase K — Human review

Present a concise review summary before publishing authoritative content.

The review should include:

- documents to be created or updated;
- major requirements captured;
- important decisions;
- unresolved questions;
- assumptions;
- material risks;
- blocking validation findings;
- selected destinations.

The user should be able to:

- approve all;
- review individual documents;
- request changes;
- defer unresolved items;
- cancel publication.

## 14. Phase L — Publish or save

After user approval, write the documents using the capabilities available to the executing agent.

Rules:

- preserve one authoritative destination per governed artifact;
- do not create editable duplicate sources of truth;
- record or expose relationships between documents where possible;
- preserve provider-native version history when available;
- never report a write as successful unless the destination confirms success.

If a write partially fails, report exactly which artifacts succeeded and which failed.

## 15. Phase M — Delivery-readiness assessment

After the definition has been reviewed, assess whether the project is sufficiently defined to begin delivery/planning.

Use three top-level outcomes:

### Ready

No unresolved issue is expected to materially block or invalidate the next delivery step.

### Ready with open items

Useful project definition exists, and remaining items can safely be resolved during planning or execution.

### Not ready

One or more unresolved items materially affect scope, feasibility, compliance, architecture, cost, or expected outcomes and should be resolved before delivery begins.

The assessment must explain the reasons for the result.

It is a readiness opinion, not a guarantee of project success.

## 16. Completion summary

At completion, provide the user with a compact summary containing:

- readiness status;
- artifacts created or updated;
- authoritative destinations;
- unresolved questions;
- significant risks;
- recommended next actions.

Do not force a specific delivery tool or methodology as the next action.

## 17. Resume behavior

The workflow must be resumable.

If the user returns later with additional information, the agent should:

1. discover the existing project definition;
2. identify what changed;
3. update the internal model;
4. ask only newly relevant questions;
5. propose amendments rather than creating duplicate documents.

## 18. Existing-project review mode

When the user already has documentation, the skill can operate as a reviewer instead of a greenfield generator.

Flow:

```text
Existing documentation
        ↓
Context inventory
        ↓
Gap + conflict analysis
        ↓
Targeted questions
        ↓
Proposed amendments
        ↓
Validation
        ↓
Human review
        ↓
Update authoritative documents
        ↓
Readiness assessment
```

The skill should prefer updating the existing authoritative project definition over generating a parallel replacement.

## 19. User-experience guardrails

The skill must not:

- require technical terminology from a non-technical user;
- force a repository-centric workflow;
- require a cloud destination;
- require a work-management tool;
- run a long fixed questionnaire without regard to existing context;
- invent missing information to complete a template;
- automatically approve its own generated truth;
- silently change destination/provider when a write fails;
- generate unnecessary documents merely because templates exist.

The skill should:

- explain unfamiliar concepts in plain language when needed;
- adapt depth to project complexity;
- progressively surface technical detail;
- preserve uncertainty honestly;
- make next actions clear;
- minimize repeated questions.

## 20. Reference journey

```text
User intent / existing material
            ↓
      Context inventory
            ↓
    Current-state synthesis
            ↓
       Gap analysis
            ↓
   Adaptive clarification
            ↓
     Research if needed
            ↓
  Requirement normalization
            ↓
       Document plan
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
 Delivery-readiness assessment
            ↓
     Completion summary
```

This journey is the behavioral basis for the first `SKILL.md`. Implementation details should remain subordinate to this contract.