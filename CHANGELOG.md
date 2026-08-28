# Changelog

All notable changes to this project are documented here.

This project follows Semantic Versioning for public releases.

## Unreleased

## 0.1.0-beta.1 - 2026-08-28

### Added

- Initial open-source repository foundation and MIT licensing.
- Provider-agnostic design principles and repository conventions.
- Community contribution, conduct, and security guidance.
- Project-definition behavioral contract, user journey, capability contract, and documentation standard.
- Beta `project-definition` Agent Skill with progressive-disclosure references for discovery, requirements, document selection, capabilities, documentation governance, and readiness.
- Generic templates for project overview, requirements, research/discovery, decision records, and architecture overview.
- Capability-neutral execution across conversation-only, local filesystem, repositories, connected document systems, work-management systems, MCPs, and other compatible tool mechanisms.
- Provider-neutral behavioral evaluation suite with 10 scenarios, shared rubric, critical-failure rules, reproducible fixtures, runner guidance, and result-recording conventions.
- Same-model smoke evaluation evidence for baseline cases, explicitly classified as non-independent evidence.
- Standard-library repository validator for skill metadata, resources, Markdown links, evaluation cases, and repository consistency.
- Generic cross-platform skill installer that copies a selected skill into a user-supplied Agent Skills directory.
- GitHub Actions workflow that runs deterministic validation and an installer smoke test for pull requests and pushes to `main`.

### Known beta limitations

- Independent cross-agent behavioral evidence is still being collected and is not claimed by this release.
- Agent-specific installation/discovery paths and connected-tool authentication remain the responsibility of the executing AI client/environment.
