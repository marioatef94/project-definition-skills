# Project Definition Governance Hardening v1

Status: Draft

This document is an additive behavioral amendment to:

- `docs/project-definition-skill-contract-v1.md`
- `docs/documentation-standard-v1.md`
- `docs/capability-contract-v1.md`

It captures generic lessons from real connected-document use without introducing any project-, provider-, vendor-, repository-, or product-specific rule into the reusable skill.

## 1. Why this amendment exists

A project-definition workflow can correctly discover requirements and still produce misleading governed documentation if it fails at any of these boundaries:

- observed implementation silently becomes project intent;
- transient implementation findings leak into stable requirement/vision artifacts;
- a point-in-time implementation scan is labeled like durable authoritative intent;
- connected pages contain decorative relationship text instead of real navigable references;
- a write succeeds but the persisted hierarchy, status, links, or body are never verified.

The core contract already requires evidence separation, human authority, and truthful persistence. This amendment makes those behaviors explicit and testable.

## 2. Governed intent versus observed implementation

Treat these as separate information layers:

```text
Governed intent
  Requirements
  Constraints
  Approved decisions

Observed current state
  Source code
  Configuration
  Deployed behavior
  Prototypes
  Tests
  Work items
  Runtime observations
```

Observed current state can prove what exists. It does not automatically prove what should exist.

### Conflict rule

If observed implementation conflicts with governed intent:

```text
Requirement / approved decision
          ≠
Observed implementation
```

then the agent must:

1. preserve the governed intent;
2. record the implementation mismatch separately;
3. explain material impact when known;
4. label any proposed alignment as a recommendation/proposed decision;
5. require human approval before amending authoritative intent.

Implementation recency, convenience, deployment status, or migration cost is not sufficient authority to supersede a requirement or decision.

### Allowed implementation-driven amendment

The agent may recommend changing intent to match current implementation when that appears sensible.

Correct sequence:

```text
Conflict detected
  → recommendation
  → human approval
  → approved decision / requirement amendment
```

Not:

```text
Implementation exists
  → requirement silently rewritten
```

## 3. Artifact-role purity

Governed artifacts should remain focused on their primary semantic role.

### Project / Product Overview

Stable shared understanding of purpose, users/stakeholders, scope, outcomes, major capabilities, constraints, and relationships.

Do not let volatile repository revisions, current bug inventories, deployment-state trivia, or temporary implementation details dominate a stable overview.

### Requirements

Intended behavior, outcomes, rules, qualities, and constraints.

Requirement statements should not contain transient status language such as:

- `currently missing`;
- `bug`;
- `required fix`;
- `implementation uses`;
- `current production config`;
- `not yet implemented`.

Those observations belong in current-state/gap evidence.

### Research / Discovery

Evidence, uncertainty, options, analysis, and recommendation. Research does not become a decision by itself.

### Decision Record

Explicit approved or proposed choice plus rationale. Existing implementation is evidence for an option, not approval of the choice.

### Architecture

Make clear whether architecture describes:

- target/intended architecture;
- current/observed architecture;
- or both, in explicitly separate layers.

Do not merge the two into one indistinguishable source of truth.

## 4. Observed-state snapshot semantics

Current implementation scans, audits, repository reviews, deployment observations, and requirement-vs-implementation matrices are time-bounded evidence.

When persisted, identify the observation boundary when practical:

```text
Status: Snapshot
As of: <date>
Evidence revision: <commit/version/locator>
```

A snapshot may be trusted evidence of what was observed at that point in time. It should not be labeled in a way that makes it indistinguishable from durable authoritative requirements or approved target architecture.

Recommended vocabulary includes:

- `Snapshot`
- `Current-state review`
- `Active gap analysis`
- `Completed audit`

Avoid `Authoritative` alone for volatile observed state.

## 5. Connected-document relationship integrity

Relationships must be real when the destination supports real relationships.

Examples include:

- hyperlink;
- document reference;
- parent/child hierarchy;
- typed relation;
- stable document ID/locator.

Writing:

```text
[Requirements]
```

or merely mentioning another page title does not prove the artifacts are linked.

The skill remains provider-neutral: destination-specific syntax may be used to realize a generic relationship, but provider-specific linking semantics must not become core project-definition semantics.

## 6. Publication is write plus verification when possible

A successful create/update response confirms only the dimensions explicitly returned by the destination.

When read-back or inspection capability exists:

```text
Write
  ↓
Read back / inspect
  ↓
Verify persisted integrity
```

Verify dimensions that matter to the artifact and destination:

- title/name;
- stable ID/locator;
- destination/container;
- parent/child hierarchy;
- lifecycle/status;
- material body/revision;
- cross-document relationships/links;
- duplicate-canonical-artifact avoidance.

Do not claim `linked`, `cross-linked`, `child of`, `published correctly`, or equivalent integrity assertions without supporting evidence.

## 7. Verification unavailable

A destination may confirm a write while exposing no read-back capability.

The correct report is:

```text
Write confirmed.
Post-write integrity verification unavailable.
```

Do not convert that limitation into either false failure or false verification.

## 8. Safe repair

If read-back reveals a broken link, wrong hierarchy, incorrect status, truncated body, or similar persistence defect:

1. distinguish the successful write from the integrity defect;
2. report the publication as incomplete in the affected dimension;
3. prepare the minimum repair;
4. re-request approval only if governed meaning/authority changes;
5. apply the repair when authorized;
6. verify again.

Formatting- or relationship-only repair may normally follow already-approved intent when it does not alter governed meaning.

## 9. Validation additions

Project-definition validation should now check for:

- observed implementation silently replacing requirements/decisions;
- transient implementation status embedded in requirement statements;
- artifact-role leakage;
- target/current architecture ambiguity;
- snapshot status/lifecycle misuse;
- decorative relationship placeholders presented as links;
- unverified hierarchy/link claims after connected publication;
- successful writes with integrity defects reported as fully complete.

## 10. Critical behavioral failures

The following are release-significant regressions:

- silently promoting observed implementation into authoritative intent when governed intent differs or approval is absent;
- claiming a connected relationship/hierarchy exists when the destination did not confirm it;
- materially altering authoritative requirements/decisions to match implementation without human approval.

## 11. Evaluation coverage

The behavioral evaluation suite includes regression scenarios for:

- implementation-vs-intent conflicts;
- connected-document link/hierarchy verification;
- artifact purity and current-state snapshot semantics.

These scenarios are provider-neutral and should be runnable across compatible agent environments.

## 12. Portability constraint

Nothing in this amendment requires:

- Confluence;
- Google Docs;
- Notion;
- GitHub;
- a repository;
- a particular MCP/server;
- a particular AI model/client.

The contract remains capability-based:

```text
create/update
read back
inspect relationships
verify integrity
```

when those capabilities exist.