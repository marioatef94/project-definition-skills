# Project Definition Evaluations

This suite evaluates the behavior of the `project-definition` skill independently of any specific AI model, client, provider, protocol, repository host, document system, or work-management tool.

The goal is not to require one exact answer. The goal is to verify that an executing agent follows the skill's behavioral contracts reliably across different project types and execution environments.

## Evaluation philosophy

Each case defines:

- **Input** — the user request and available context;
- **Environment** — capabilities the agent may or may not have;
- **Expected behavior** — outcomes that demonstrate correct skill use;
- **Forbidden behavior** — regressions or unsafe shortcuts;
- **Scoring focus** — rubric dimensions that matter most for the case.

Evaluate the behavior actually produced. Do not award points because the expected rule exists in `SKILL.md` if the agent fails to follow it.

## Running an evaluation manually

1. Install or expose `skills/project-definition/` to the AI agent under test.
2. Start a fresh session unless the case explicitly tests resume behavior.
3. Reproduce the case environment as closely as the agent supports.
4. Submit the case input without adding hidden hints from the expected-behavior section.
5. Continue only as needed to observe the workflow described by the case.
6. Score the run using [`rubric.md`](rubric.md).
7. Record evidence, failures, agent/model information, and date in `results/` or another test-results store.

## Pass policy

A run passes when:

- the overall rubric score is at least **16/20**;
- no critical-failure condition is triggered;
- all case-specific required behaviors marked as critical are satisfied.

A case may define stricter expectations.

## Cases

| Case | Purpose |
|---|---|
| `001-idea-non-technical` | Verify project-type neutrality and adaptive discovery. |
| `002-idea-technical` | Verify technical discovery without premature architecture decisions. |
| `003-existing-requirements-review` | Verify review/update behavior instead of unnecessary regeneration. |
| `004-conflicting-sources` | Verify conflict detection and human resolution. |
| `005-local-only-persistence` | Verify fully local operation and truthful persistence reporting. |
| `006-connected-destination` | Verify capability-based publication with human approval. |
| `007-destination-failure` | Verify safe failure and no silent canonical fallback. |
| `008-research-required` | Verify conditional research and evidence separation. |
| `009-deferred-open-questions` | Verify uncertainty remains explicit when the user defers decisions. |
| `010-resume-existing-project` | Verify resumable amendment behavior and avoidance of duplicate authoritative docs. |

## Adding cases

Use [`case-template.md`](case-template.md). Prefer cases that test behavior observable across multiple agents rather than syntax unique to one environment.

Add a new case when it protects a meaningful contract, regression, edge condition, or portability requirement. Do not add cases merely to increase coverage count.
