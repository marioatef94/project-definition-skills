# Design Principles

These principles apply to every skill published in this repository.

## 1. Capability-based integrations

Skills describe the capability they need, such as:

- read existing project documentation;
- search project information;
- create or update a document;
- read work items;
- save a local file.

They must not require one named provider in order to function. When a capability is unavailable, the agent should explain the limitation and choose only an explicitly approved fallback.

## 2. Destination independence

A document's structure and quality rules must not depend on where it is stored. The same project-definition workflow should be usable when the final artifact is saved to a collaborative workspace, project-management system, repository, local Markdown file, or another supported destination.

## 3. Facts are not assumptions

Skills must keep the following concepts distinct:

- **Fact** — supplied directly or verified from an authoritative source.
- **Assumption** — temporarily accepted but not verified.
- **Inference** — reasoned from available evidence.
- **Recommendation** — proposed course of action.
- **Unknown** — information not currently available.
- **Decision** — an option explicitly chosen by an authorized human or authoritative source.

An assumption, inference, or recommendation must never be silently converted into a requirement or decision.

## 4. Discover before asking

Before asking the user for information, the agent should inspect the context and available sources it is authorized to access. It should not ask for information that is already available and sufficiently reliable.

Questions should be grouped and prioritized by their impact on scope, requirements, architecture, risk, cost, security, compliance, operations, or delivery.

## 5. Human authority

AI can discover, organize, draft, analyze, validate, and recommend. Humans remain responsible for approving authoritative project requirements and significant decisions.

## 6. Minimum sufficient documentation

Do not generate every possible artifact for every project. Select documents according to project complexity, risk, audience, lifecycle, and expected value.

## 7. Progressive disclosure

Keep `SKILL.md` focused on workflow and rules. Large templates, examples, and detailed standards belong in referenced resources so agents load them only when relevant.

## 8. Portable core, optional extensions

Core skills must remain reusable across industries and project types. Organization-, domain-, client-, or project-specific rules should extend the core rather than modify or fork it unnecessarily.

## 9. Safe failure

If a required capability or authoritative source is unavailable, do not silently substitute another destination, invent missing content, or declare completion. Surface the limitation and preserve any generated content as a draft until the user chooses what to do.
