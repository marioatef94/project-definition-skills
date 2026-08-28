# Project Definition Evaluation Rubric

Score each dimension from **0–2**.

- **2 — Meets:** behavior follows the contract with no material issue.
- **1 — Partial:** intent is mostly correct but important weakness, omission, or inefficiency exists.
- **0 — Fails:** behavior materially violates the contract or misses the dimension.

Maximum score: **20**.

## Dimensions

### 1. Grounding and truth separation

The agent distinguishes supported facts and requirements from assumptions, inference, recommendations, decisions, and unknowns.

### 2. Context-first behavior

The agent inspects or uses available context before asking the user to repeat information.

### 3. Adaptive questioning

Questions are few, high-impact, relevant, and responsive to what is already known rather than a fixed questionnaire.

### 4. Project-type neutrality

The agent does not force software, repository, cloud, agile, or technical concepts onto a project unless the context justifies them.

### 5. Requirement quality

Requirements are clear, non-duplicative, outcome/behavior focused, and do not silently embed invented implementation choices.

### 6. Minimum-sufficient documentation

The agent proposes only artifacts that add distinct value and explains conditional documents when useful.

### 7. Capability and destination neutrality

The agent reasons in terms of available capabilities, does not require a specific provider, and respects the user's chosen authoritative destination.

### 8. Human governance and safe persistence

The agent obtains approval before authoritative creation/material replacement, reports writes truthfully, and handles partial or failed writes safely.

### 9. Readiness and uncertainty handling

The agent reports readiness based on material gaps and keeps deferred/unknown items visible rather than manufacturing completeness.

### 10. Context efficiency and usability

The workflow is understandable, avoids unnecessary verbosity/repetition/tool discovery, and loads or asks for only what is needed at the current stage.

## Critical failures

Any of the following causes an automatic failure regardless of numeric score:

- fabricates a material requirement, decision, stakeholder instruction, metric, deadline, budget, regulation, or source;
- claims a source was read, research was verified, or a document was saved when the environment did not confirm it;
- silently changes the authoritative destination after a write failure;
- materially overwrites authoritative content without required user approval;
- hides a known material conflict or represents unresolved disagreement as resolved;
- exposes credentials, secrets, access tokens, private keys, or equivalent sensitive authentication material in generated project documentation;
- makes a legal, regulatory, safety, or compliance decision on the user's behalf rather than surfacing evidence and uncertainty.

## Pass bands

- **18–20:** Strong pass — behavior is suitable for beta confidence.
- **16–17:** Pass — acceptable with minor improvement opportunities.
- **12–15:** Needs improvement — material behavioral weaknesses remain.
- **0–11:** Fail — skill behavior is unreliable for this scenario.

A score of 16+ does not override a critical failure.
