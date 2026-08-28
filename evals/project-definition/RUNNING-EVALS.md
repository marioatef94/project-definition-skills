# Running Project Definition Evaluations

Use this guide to run the `project-definition` behavioral evaluation suite without leaking the expected answer into the agent being tested.

## Goal

The cases under `cases/` test observable behavior, not exact wording. Run them in fresh sessions against an Agent Skills-compatible environment with `skills/project-definition/` installed or exposed.

## Evidence classes

Record every run as one of:

- **Independent** — the tested agent produces the response without seeing the expected/forbidden behavior sections, and scoring is performed separately. This evidence may contribute to release confidence.
- **Self-smoke** — the same agent/model is involved in producing and evaluating the response. Use only for sanity and regression checks.

Never label a self-scored run as independent.

## Preparation

1. Check out the exact repository commit you want to evaluate.
2. Install or expose `skills/project-definition/` to the target agent.
3. Configure only the capabilities required by the case.
4. Do not expose `rubric.md`, the case's `Expected behavior`, `Forbidden behavior`, `Critical requirements`, or prior result files to the tested agent.
5. For cases that reference a file under `fixtures/`, provide that fixture exactly as written.

## Run a case

1. Start a fresh session unless the case explicitly tests resume behavior.
2. Give the target agent the case `Input` exactly.
3. Reproduce the declared `Environment` as closely as the target supports.
4. Provide referenced fixtures without adding evaluator commentary.
5. Continue the conversation only when the case requires later approval, persistence, failure handling, or impact analysis.
6. Capture the complete relevant transcript and tool outcomes.

## Score a run

After the tested run is complete:

1. Read `rubric.md`.
2. Read the case's expected, forbidden, and critical behavior.
3. Score all 10 rubric dimensions from 0–2.
4. Record any critical failure separately.
5. Apply the pass policy: 16/20 or higher, no critical failure, and all case-specific critical requirements satisfied.
6. Explain every score below 2 with concise evidence.

## Result record

Create a Markdown file under `results/` using a name such as:

```text
YYYY-MM-DD-<agent>-<model>-<evidence-class>.md
```

Include:

- date;
- evidence class;
- case ID;
- agent/client;
- model/version when known;
- skill commit SHA or release version;
- capability setup;
- rubric scores by dimension;
- total score and pass/fail;
- critical failures;
- concise observations;
- sanitized transcript/artifact references when appropriate.

Do not commit credentials, private source material, proprietary project content, or sensitive transcripts.

## Persistence cases

For cases 005, 006, 007, and 010, the evaluator must capture actual tool outcomes. A textual promise to write a file or remote document does not demonstrate successful persistence.

When destructive or authoritative writes would be inappropriate in the test environment, use a disposable test destination clearly isolated from production content.

## Research case

Case 008 intentionally starts without enough jurisdiction/data detail to determine all applicable external requirements. The tested agent should identify that gap or explicitly scope uncertainty before presenting legal/compliance conclusions.

## Cross-agent comparison

Use the same case inputs and fixtures across agents. Compare behavior by rubric dimension and critical failures rather than prose similarity.

A release should not claim cross-agent validation unless the repository contains or references actual independent runs that support that claim.
