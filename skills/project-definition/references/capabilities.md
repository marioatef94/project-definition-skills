# Capability Guidance

Use this reference when the workflow needs access to sources, research, persistence, relationship management, or work-management systems.

## Principle

Describe the operation needed, not the provider expected to perform it.

Possible execution mechanisms include native agent tools, connected apps, MCP servers, APIs, CLIs, repositories, local filesystems, or future integrations. The skill must not require any one mechanism.

## Capability groups

### Source discovery

Useful operations:

- search available project sources;
- list accessible containers or collections;
- locate existing project-definition artifacts;
- discover likely authoritative material.

Do not search broadly when the user has already identified the relevant source.

### Content access

Useful operations:

- read a supplied or attached file;
- read a local file;
- read a remote document or record;
- read repository content;
- read a work item or structured project record;
- inspect a persisted document's metadata, parent/container, revision, or relationships when supported.

Treat access as read-only unless a separate write capability is confirmed.

### Documentation persistence

Useful operations:

- create a document or file;
- update an existing document or file;
- create a container or folder when required;
- preserve relationships between artifacts;
- create actual links/references supported by the destination;
- confirm the resulting location or identifier;
- read back or inspect the persisted result when supported.

Never report success unless the destination confirms the write.

A create/update success does not automatically prove that hierarchy, lifecycle status, formatting, or cross-document relationships were persisted correctly. Verify those separately when the capability exists.

### Relationship / integrity verification

When governed artifacts should be related or navigable, useful operations may include:

- inspect parent/child hierarchy;
- inspect stored hyperlinks or document references;
- resolve stable IDs/locators;
- read the persisted body to confirm a reference rendered as an actual link;
- inspect lifecycle/status and revision metadata.

Do not claim `linked`, `cross-linked`, `related`, `child of`, or equivalent destination state from decorative text alone.

If the environment can write but cannot inspect the result, distinguish:

```text
Write confirmed
Integrity verification unavailable
```

from:

```text
Write and relationship integrity verified
```

### Work management

Optional operations:

- search work items;
- read work items as supporting evidence;
- create or update work items only when the user explicitly wants delivery decomposition or tracking output.

Work items are not automatically the authoritative project requirements.

### Research

Useful operations:

- search current external information;
- retrieve authoritative evidence;
- compare options;
- cite or preserve source references.

Research is conditional. Do not browse merely to fill a template.

### Repository or filesystem

Useful operations:

- read directories and files;
- create directories;
- write or update local documents;
- inspect saved content after a write;
- validate relative links/paths when practical;
- use versioned repository storage when available.

A local file may be the authoritative document if the user chooses it.

## Capability discovery

Discover capabilities lazily. Do not start the workflow by asking users technical questions such as which integration protocol or server they use.

When a capability becomes necessary:

1. inspect what the environment can already do;
2. use an available authorized capability if it clearly satisfies the need;
3. ask the user only when destination, authorization, or intent is ambiguous;
4. explain limitations if the capability is unavailable.

For publication, discover read-back/relationship-inspection capability only when it is useful to validate the intended persisted result. Do not enumerate every provider-specific API up front.

## Required vs optional

The only universally required capability is interaction with the user.

Everything else is optional:

- reading existing sources improves discovery;
- persistence enables saving or publishing;
- post-write read-back improves persistence confidence;
- research enables external verification;
- work-management access enables optional downstream decomposition.

If a capability is missing, continue with unaffected work when useful.

## Safe failure

When a requested operation fails:

1. state what failed;
2. state what was and was not changed;
3. preserve the draft or proposed change;
4. do not claim success;
5. do not silently change the authoritative destination;
6. offer only alternatives the environment can actually perform.

If a multi-document write partially succeeds, report success or failure per artifact.

If the write succeeds but post-write verification reveals an integrity defect, report the write and the integrity defect separately. Do not describe the publication as fully complete until material integrity problems are repaired or explicitly accepted.

## Canonical destination rule

Each governed artifact has one authoritative destination.

Derived or convenience copies may exist only when clearly labeled non-authoritative. Never create two independently editable sources of truth by default.

If the authoritative destination is unavailable, a local or alternate copy may be offered as a draft only unless the user explicitly chooses to change the authoritative destination.