# Publishing and Persistence Verification

Use this reference before authoritative persistence when the workflow writes governed artifacts to a connected document system, repository, filesystem, work-management store, or another user-approved destination.

## Principle

A successful write response proves only what the destination actually confirms.

Do not infer that titles, relationships, hierarchy, links, lifecycle status, or rendered content are correct merely because a create/update operation returned success.

When the environment supports read-back or relationship inspection, authoritative publication is a two-stage operation:

```text
Write
  ↓
Read back / inspect
  ↓
Verify persisted integrity
```

## Before writing

Confirm:

- the intended authoritative destination;
- whether an equivalent authoritative artifact already exists;
- whether the operation is create, update, amend, supersede, or archive;
- the intended parent/container when hierarchy matters;
- the intended lifecycle/status;
- the relationships that should exist between governed artifacts;
- that required human approval has been obtained for authoritative creation or material replacement.

Do not use persistence as a substitute for unresolved governance decisions.

## Write outcome

Record the destination-confirmed outcome per artifact:

- success;
- partial success;
- failure.

For successful writes, preserve the returned stable identifier, locator, revision/version, or equivalent reference when available.

For partial failure, report exactly what changed and what did not.

## Post-write verification

When supported, re-read or inspect the persisted artifact and verify the dimensions relevant to the destination.

### Identity

Verify:

- expected title/name;
- stable identifier or locator;
- correct project/container/space/folder;
- no unintended duplicate canonical artifact.

### Lifecycle and authority

Verify:

- intended status/lifecycle value where supported;
- authoritative vs draft/non-authoritative labeling;
- observed-state snapshots are not mislabeled as durable project intent.

### Content

Verify enough of the persisted body/revision to establish that:

- the intended content was saved;
- no material truncation or formatting conversion changed meaning;
- requirement/decision semantics still match the approved draft.

Do not silently rewrite content to accommodate destination formatting.

### Hierarchy

If a parent/child or folder relationship matters, inspect the actual stored relationship.

Writing a title under a heading or mentioning a page name does not create a hierarchy.

### Cross-document relationships

If related artifacts should be navigable, verify the destination stored a real relationship supported by that destination, such as:

- hyperlink;
- document reference;
- parent/child relationship;
- stable ID relationship;
- typed relation supported by the destination.

Plain text such as:

```text
[Requirements]
```

is not proof that a clickable or resolvable relationship exists.

When a provider requires destination-specific syntax to create a real relationship, adapt only the persistence representation. Do not introduce provider-specific semantics into the core project-definition model.

### Links

For links created during publication, verify when possible that:

- the destination is the intended artifact;
- the link/reference is stored as an actual link/reference rather than decorative text;
- relative links resolve in repository/filesystem destinations;
- connected-document links use destination-supported references.

Do not claim `linked`, `cross-linked`, `related`, or `navigable` unless the destination or read-back confirms that relationship.

## Verification unavailable

Sometimes a destination confirms a write but exposes no read-back or relationship-inspection capability.

Report this precisely:

```text
Write confirmed.
Post-write integrity verification unavailable in this environment.
```

Do not downgrade a confirmed write to failure, but do not promote unverified relationship or rendering assumptions to confirmed facts.

## Safe repair

If read-back reveals a publishing defect such as a broken link, wrong parent, incorrect status, truncated body, or placeholder relationship:

1. classify the artifact write itself separately from the integrity defect;
2. do not claim publication is fully complete;
3. prepare the minimum repair;
4. obtain approval again only if the repair materially changes governed meaning or authority;
5. apply the repair when authorized;
6. verify again.

Formatting-only or relationship-only repairs may follow the user's already-approved intent when they do not alter governed content and the environment permits the write.

## Completion evidence

For an authoritative persistence workflow, completion reporting should distinguish:

- content approved;
- write confirmed;
- location/reference confirmed;
- hierarchy verified, when relevant;
- relationships/links verified, when relevant;
- any unverified dimensions;
- any partial failures or repair actions.

The goal is truthful persistence evidence, not maximum ceremony.