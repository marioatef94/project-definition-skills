# Project Definition Evaluations

This suite evaluates the behavior of the `project-definition` skill independently of any specific AI model, client, provider, protocol, repository host, document system, or work-management tool.

The goal is not to require one exact answer. The goal is to verify that an executing agent follows the skill's behavioral contracts reliably across different project types and execution environments.

For the copy/paste execution procedure, use [`RUNNING-EVALS.md`](RUNNING-EVALS.md).

## Evaluation philosophy

Each case defines:

- **Input** — the user request and available context;
- **Environment** — capabilities the agent may or may not have;
- **Expected behavior** — outcomes that demonstrate correct skill use;
- **Forbidden behavior** — regressions or unsafe shortcuts;
- **Critical requirements** — behavior that must pass regardless of numeric score;
- **Scoring focus** — rubric dimensions that matter most for the case.

Evaluate the behavior actually produced. Do not award points because the expected rule exists in `SKILL.md` if the agent fails to follow it.

## Evidence classes

- **Independent** — the tested agent is not shown the expected/forbidden behavior before producing its response and scoring is performed separately. This may contribute to release confidence.
- **Self-smoke** — the same model/agent family is involved in execution and evaluation. This is regression/sanity evidence only.

Never describe self-smoke evidence as independent cross-agent validation.

## Reproducible fixtures

Cases that depend on existing project state or sufficiently clarified context use committed files under [`fixtures/`](fixtures/). Provide those fixtures exactly as written so different agents are evaluated against the same source material.

## Running an evaluation manually

1. Install or expose `skills/project-definition/` to the AI agent under test.
2. Start a fresh session unless the case explicitly tests resume behavior.
3. Reproduce the case environment as closely as the agent supports.
4. Provide any referenced fixture exactly.
5. Submit the case input without exposing expected/forbidden behavior.
6. Continue only as needed to observe the workflow described by the case.
7. Score the run using [`rubric.md`](rubric.md).
8. Record evidence, failures, agent/model information, date, and evidence class in [`results/`](results/).

## Pass policy

A run passes when:

- the overall rubric score is at least **16/20**;
- no critical-failure condition is triggered;
- all case-specific critical requirements are satisfied.

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

## Current evidence

The repository contains same-model smoke evidence for all 10 initial scenarios. Persistence happy-path, local-only persistence, connected-write failure, and in-place amendment paths include real tool outcomes where described in the result records.

These results support regression confidence for the public beta but do not constitute independent cross-agent validation.

## Adding cases

Use [`case-template.md`](case-template.md). Prefer cases that test behavior observable across multiple agents rather than syntax unique to one environment.

Add a case when it protects a meaningful contract, regression, edge condition, or portability requirement. Do not add cases merely to increase coverage count.
