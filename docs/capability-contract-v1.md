# Capability Contract v1

Status: Draft

This document defines how reusable project-definition skills reason about tools and integrations without depending on any specific provider, protocol, AI client, project-management system, document platform, repository host, or filesystem implementation.

The contract is intentionally capability-based:

> A skill should describe **what operation it needs**, not **which vendor or tool must perform it**.

A connected tool, MCP server, native agent integration, repository client, local filesystem, CLI, API wrapper, or future execution mechanism may satisfy the same capability.

## 1. Purpose

The capability contract exists to keep the skills portable across execution environments.

It ensures that a skill can:

- operate with no external integrations at all;
- read existing project context when appropriate access exists;
- save documents locally or remotely when write access exists;
- use project-management or work-tracking systems when useful, without requiring them;
- perform research when evidence is needed and research capability exists;
- degrade safely when a requested capability is unavailable;
- avoid hard-coding provider-specific identifiers, APIs, workflows, or terminology into the core skill;
- preserve user control over authoritative destinations.

## 2. Core principle

The skill must reason in terms of abstract capabilities.

Bad:

```text
Create a page using <specific provider>.
```

Good:

```text
Create or update the approved document in the user's selected authoritative documentation destination using an available write capability.
```

The execution environment is responsible for mapping that intent to an actual tool.

## 3. Capability is not transport

A protocol or integration mechanism is not itself the capability.

For example, the following may all expose the same logical operation:

```text
MCP server
Native AI connector
Local filesystem tool
Repository integration
CLI
HTTP/API wrapper
Desktop automation
```

The skill should care about operations such as:

```text
search existing documents
read content
create document
update document
write local file
create work item
perform external research
request human approval
```

It should not require a specific transport unless a user explicitly requests one.

## 4. Baseline requirement

Only one capability is mandatory for the `project-definition` workflow:

### `user.interact`

The agent must be able to communicate with the user.

Everything else is optional.

Therefore the skill must remain useful in a conversation-only environment.

Example:

```text
Available:
✓ user.interact

Unavailable:
✗ external sources
✗ filesystem
✗ remote document store
✗ work-management system
✗ web research
```

The skill can still:

- run discovery;
- ask clarification questions;
- normalize requirements;
- generate draft documents inline;
- validate the drafts;
- assess project-definition readiness.

It must clearly state that no persistent copy was created.

## 5. Capability groups

Capability names below are conceptual identifiers for the contract. They are not required tool names or API methods.

### 5.1 User interaction

| Capability | Purpose |
| --- | --- |
| `user.interact` | Ask questions, present findings, receive decisions and approvals |
| `user.approval` | Obtain explicit approval before authoritative publication or material replacement |

`user.approval` may be satisfied through normal conversation; a special approval UI is not required.

### 5.2 Source discovery

| Capability | Purpose |
| --- | --- |
| `source.list` | List available sources, spaces, directories, containers, or collections |
| `source.search` | Search accessible sources for relevant project material |
| `source.locate` | Resolve a known reference, path, identifier, or link to an accessible artifact |

Source discovery is optional. When unavailable, ask the user to provide or point to the relevant material.

### 5.3 Content access

| Capability | Purpose |
| --- | --- |
| `content.read` | Read a selected document, record, page, work item, or other textual artifact |
| `file.read` | Read an accessible local or mounted file |
| `directory.read` | Inspect an accessible local or mounted directory |
| `repository.read` | Read version-controlled project content |
| `history.read` | Read available revision/history information when freshness or provenance matters |

The skill should use the most specific available capability, but core behavior must not depend on one implementation.

### 5.4 Document persistence

| Capability | Purpose |
| --- | --- |
| `document.create` | Create a new document or page in a selected destination |
| `document.update` | Update an existing document |
| `document.read` | Read an existing canonical document |
| `document.link` | Relate or cross-link documents when the destination supports it |
| `container.create` | Create a folder, collection, space, directory, or equivalent container when needed and approved |

These capabilities may be exposed by a documentation system, local filesystem, repository, project workspace, or another document store.

### 5.5 Local persistence

| Capability | Purpose |
| --- | --- |
| `file.write` | Create or replace a local file |
| `directory.create` | Create a local directory when needed |

Local files may be authoritative if the user explicitly chooses a local destination.

Local files must not become authoritative merely because a requested remote write failed.

### 5.6 Repository persistence

| Capability | Purpose |
| --- | --- |
| `repository.create-file` | Create a version-controlled document |
| `repository.update-file` | Update an existing version-controlled document |
| `repository.history` | Inspect document history or revision metadata |

A repository is one possible document destination; it is never required by the skill.

### 5.7 Work-management capabilities

| Capability | Purpose |
| --- | --- |
| `work.search` | Search existing work items or project-management records |
| `work.read` | Read an existing work item or project record |
| `work.create` | Create an approved work item or initial delivery record |
| `work.update` | Update an existing work item or project record |
| `work.link` | Associate work items with project-definition artifacts when supported |

Work-management capabilities are optional and should normally be used after the project definition is sufficiently mature.

The project-definition skill must not require work items to exist before it can operate.

### 5.8 External research

| Capability | Purpose |
| --- | --- |
| `research.search` | Search external information sources |
| `research.fetch` | Retrieve a selected external source |
| `research.verify` | Cross-check material facts using available evidence |
| `research.cite` | Preserve a usable reference or citation to supporting evidence |

Research is conditional and should be invoked only when a material project question requires external evidence or current information.

Lack of research capability must not cause the agent to fabricate current facts.

## 6. Capability discovery

The skill should not begin by asking users to name integrations, protocols, plugins, or tool vendors.

The execution sequence should be:

```text
Skill invoked
    ↓
Agent inspects available capabilities
    ↓
Agent understands the user's requested outcome
    ↓
Agent determines which capabilities are actually needed
    ↓
Use available capabilities
    ↓
Ask the user only when a choice or missing capability affects the workflow
```

For example, do not ask:

```text
Which MCP server do you have?
```

Prefer:

```text
I can save the approved documents to your connected documentation workspace or as local files. Which location should be authoritative?
```

The user does not need to understand the underlying integration mechanism.

## 7. Capability requirements are intent-driven

The skill must determine capability needs from the current user intent rather than assuming a fixed environment.

### Example — idea only

User:

```text
Help me define a new project.
```

Required:

```text
user.interact
```

Everything else is optional.

### Example — review existing local material

User:

```text
Review the files in this project folder and identify missing requirements.
```

Needed if available:

```text
directory.read
file.read
```

### Example — update existing remote documentation

User:

```text
Review my existing requirements and update the approved document after I review your changes.
```

Needed:

```text
source.search or source.locate
document.read
document.update
user.approval
```

### Example — save locally

User:

```text
Generate the project definition as Markdown files in this folder.
```

Needed:

```text
directory.create, if required
file.write
```

### Example — evidence-dependent question

User:

```text
Research the current regulatory requirements before finalizing the project scope.
```

Needed:

```text
research.search
research.fetch
research.cite
```

If unavailable, the skill must explain that the requested external verification cannot be completed in the current environment.

## 8. Source selection rules

When multiple readable sources are available, the skill should:

1. prefer sources explicitly identified by the user;
2. prefer known authoritative project sources over secondary summaries;
3. use direct relationships and specific project references before broad searches;
4. fetch the minimum context needed to answer the current gap;
5. avoid scanning unrelated data merely because access exists;
6. use revision/history metadata when relevant to determining freshness;
7. surface conflicts rather than silently choosing between incompatible authoritative sources.

Access does not imply relevance.

## 9. Destination resolution

Destination resolution happens after the skill understands which artifacts should exist.

For each governed artifact, determine:

```text
Artifact
  ↓
Authoritative destination
  ↓
Required write capability
```

An artifact may be stored in:

- a collaborative document system;
- a work-management system when that artifact type belongs there;
- a repository;
- a local directory;
- another user-approved content store.

The core skill does not prefer a vendor.

## 10. One authoritative destination per governed artifact

The skill must avoid editable duplication.

Example:

```text
Requirements Document
    ↓
Canonical destination: remote document
    ↓
Optional generated local copy: derived/read-only
```

Do not create two editable canonical copies unless the user explicitly defines a synchronization strategy outside this contract.

When a generated copy is derived from an authoritative source, clearly mark it as generated/non-authoritative where practical.

## 11. Destination preference order

When no explicit destination is supplied, resolve in this order:

1. existing authoritative destination for that artifact, if confidently known;
2. destination explicitly selected by the user for the current project;
3. available destination proposed by the agent and approved by the user;
4. conversation-only draft if no persistence destination is available.

Do not silently select a persistence destination merely because a tool is available.

## 12. Capability fallback rules

Fallback behavior must preserve semantics and authority.

### 12.1 Read capability unavailable

If an expected source cannot be read:

```text
State what cannot be accessed.
Explain which conclusions are affected.
Ask the user to provide the material when necessary.
Continue with unaffected work.
```

Do not pretend to have inspected it.

### 12.2 Research capability unavailable

If research is needed but unavailable:

```text
Mark the question as externally unverified.
Explain that current evidence could not be retrieved.
Do not invent a fact or citation.
```

### 12.3 Write capability unavailable

If the user requested persistence but no suitable write capability exists:

```text
Generate the draft.
Tell the user it has not been persisted.
Offer manual copy/export when possible.
```

### 12.4 Selected authoritative destination fails

If the selected canonical destination fails during publication:

```text
Do not silently write the authoritative artifact elsewhere.
```

Instead:

1. report the failure;
2. retain the proposed draft/change set;
3. identify any artifacts that were successfully written;
4. offer available alternatives;
5. require the user to choose whether an alternative destination becomes authoritative.

A local fallback may be offered as a non-authoritative draft without changing canonical ownership.

## 13. Partial-success behavior

Multi-document publication may partially succeed.

The agent must report per-artifact outcome.

Example:

```text
Publication result

✓ Project Overview — saved successfully
✓ Requirements Document — saved successfully
✗ Research Document — write failed

The failed Research Document remains a draft and is not considered published.
```

Never report the whole publication as successful when any requested artifact failed.

## 14. Confirmation semantics

A write operation is considered successful only when the executing capability reports or otherwise reliably confirms success.

Do not infer persistence from an attempted call.

Where practical, after a material update the agent may verify the destination by reading back metadata or content, but this should not create unnecessary tool calls when the write response itself is authoritative.

## 15. Human approval boundary

The availability of write capability does not imply permission to publish authoritative content.

Write authorization and content approval are separate concepts.

```text
Tool can write
    ≠
User approved this content
```

Before creating a new authoritative project-definition artifact or materially replacing an existing authoritative artifact, obtain explicit human approval according to the project-definition workflow.

Draft persistence is allowed when the user has requested draft saving and the destination clearly preserves draft status.

## 16. Minimal-privilege behavior

The skill should use the narrowest relevant access available.

Rules:

- do not enumerate unrelated projects, workspaces, repositories, or directories when a specific source is already known;
- do not read private material unrelated to the user's request;
- do not request write access when read access is sufficient;
- do not expose credentials, tokens, secrets, authentication configuration, or integration internals in generated project documents;
- do not embed provider credentials into skill files or templates;
- do not treat broad tool access as permission to copy content into another destination.

## 17. Capability profiles

The contract supports several common execution profiles without making any one profile special.

### 17.1 Conversation-only

```text
✓ user.interact
```

Outcome:

- discovery;
- requirements;
- inline drafts;
- readiness assessment;
- no persistence.

### 17.2 Local-first

```text
✓ user.interact
✓ file.read
✓ file.write
✓ directory.read/create
```

Outcome:

- inspect local project material;
- generate and maintain local documents.

### 17.3 Connected documentation

```text
✓ user.interact
✓ source.search
✓ document.read/create/update
```

Outcome:

- discover existing documents;
- update or publish approved project-definition artifacts remotely.

### 17.4 Work-management assisted

```text
✓ connected documentation capabilities
✓ work.search/read/create/update
```

Outcome:

- use existing work records as source evidence;
- optionally derive initial approved work items after project definition is mature.

### 17.5 Repository-backed

```text
✓ repository.read
✓ repository.create-file/update-file
```

Outcome:

- inspect version-controlled context;
- store selected documentation as version-controlled files.

### 17.6 Research-enabled

```text
✓ research.search/fetch/cite
```

Outcome:

- verify external evidence-dependent questions;
- produce sourced research artifacts.

Profiles may be combined.

## 18. Provider-specific behavior belongs outside the core skill

The core skill must not contain logic such as:

```text
If provider A, set field X.
If provider B, create object Y.
```

Provider-specific mechanics belong to the executing tool/integration layer or a separate adapter/reference when genuinely needed.

The project-definition skill should express semantic intent:

```text
Create approved requirements document.
Update existing canonical document.
Link related artifacts when supported.
```

This keeps the core skill portable.

## 19. Formatting adaptation

Different destinations support different formatting capabilities.

The agent may adapt:

- headings;
- tables;
- metadata presentation;
- links;
- native status labels;
- page hierarchy;
- front matter;

without changing the underlying project-definition semantics.

Formatting limitations must never cause substantive requirements or unresolved risks to be omitted.

## 20. Capability discovery must be lazy

Do not inventory every possible tool or source at the beginning of a run.

Discover only what is relevant to the current stage.

Example:

```text
Discovery stage
→ need read capabilities

Research gate
→ check research capabilities only if research becomes necessary

Publication stage
→ resolve write capabilities only after document plan is known
```

This reduces unnecessary access, context use, latency, and user confusion.

## 21. Generic internal capability state

An implementation may normalize capabilities internally using states such as:

```text
available
unavailable
unknown
requires-user-choice
requires-authentication
read-only
```

This is an implementation aid, not a required external API.

The skill should not claim a capability is available until the agent has evidence that it can actually invoke it.

## 22. Authentication behavior

Authentication is owned by the execution environment/integration, not by the skill.

If a useful capability exists but requires authentication:

1. explain that access is required for the requested operation;
2. let the environment guide authentication when supported;
3. continue with unaffected work where possible;
4. never ask the user to paste secrets, access tokens, private keys, or passwords into generated project documents.

The core skill must remain usable without authentication to optional external systems.

## 23. Capability-to-workflow mapping

| Project-definition stage | Typical capabilities |
| --- | --- |
| Entry / clarification | `user.interact` |
| Context inventory | `source.list`, `source.search`, `content.read`, `file.read`, `repository.read` |
| Gap analysis | read capabilities only |
| Research gate | `research.search`, `research.fetch`, `research.cite` |
| Requirement normalization | no external capability required |
| Document planning | no external capability required |
| Destination resolution | capability discovery for available write destinations |
| Draft generation | no external capability required |
| Validation | read access to relevant generated/existing artifacts |
| Human review | `user.interact`, `user.approval` |
| Publication | `document.create/update`, `file.write`, `repository.create-file/update-file`, or equivalent |
| Optional work-item handoff | `work.create/update/link` |
| Completion summary | `user.interact` |

This table describes typical needs, not mandatory implementation order.

## 24. Non-goals

Capability Contract v1 does not define:

- a universal MCP schema;
- one common API implemented by every integration;
- provider authentication protocols;
- provider-specific field mappings;
- synchronization engines between document stores;
- automatic bidirectional document replication;
- a universal work-management data model;
- a plugin installation mechanism;
- a mandatory tool discovery API.

The contract defines behavioral expectations for the skill, not infrastructure standards for third-party tools.

## 25. Conformance rules

A `project-definition` skill implementation conforms to Capability Contract v1 when it:

1. can operate with only user interaction;
2. does not require a named provider or protocol in its core workflow;
3. discovers capabilities according to need rather than demanding a fixed integration stack;
4. distinguishes read capability, write capability, and human approval;
5. preserves one authoritative destination per governed artifact;
6. does not silently change authoritative destination after a write failure;
7. reports unavailable capabilities and partial failures accurately;
8. does not fabricate source access, research results, citations, or persistence success;
9. supports local and remote document destinations when the environment exposes the necessary capabilities;
10. keeps provider-specific mechanics outside the core skill contract;
11. applies minimal-access and privacy principles;
12. remains useful to both technical and non-technical users.

## 26. Reference resolution flow

```text
User asks for project-definition work
                ↓
       Understand requested outcome
                ↓
       Determine current stage
                ↓
      Determine needed capability
                ↓
      Inspect available operations
                ↓
        ┌───────┴────────┐
        │                │
    Available        Unavailable
        │                │
        ▼                ▼
   Use capability    Explain limitation
        │            Preserve unknown/draft
        │            Offer safe alternatives
        └───────┬────────┘
                ↓
       Continue project-definition flow
```

This contract should be read together with the project-definition behavioral contract and user journey. The actual `SKILL.md` should encode the minimum necessary capability behavior and load detailed guidance lazily from references.