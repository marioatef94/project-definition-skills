# Evaluation Results

Store reproducible evaluation records here when results are intended to be committed publicly. Private or sensitive project content must not be added to this repository.

A result record should include:

- date;
- case ID;
- agent/client;
- model/version when known;
- skill commit SHA or release version;
- relevant capability setup;
- rubric scores by dimension;
- total score and pass/fail;
- critical failures, if any;
- concise evidence/observations;
- links to sanitized transcripts or artifacts when appropriate.

## Evidence classes

Use one of these labels for every result:

- **Independent** — the executing agent is evaluated by a separate evaluator or otherwise run without the evaluator shaping the response from the case expectations. This evidence may contribute to release/merge confidence.
- **Self-smoke** — the same agent/model executes and evaluates the case, or the evaluator has direct knowledge of the expected behavior while producing the response. This is useful for sanity/regression checks but must not by itself satisfy an independent behavioral merge gate.

When in doubt, classify the result as `Self-smoke`.

Do not publish credentials, proprietary prompts, private source documents, client data, or other sensitive evaluation material.
