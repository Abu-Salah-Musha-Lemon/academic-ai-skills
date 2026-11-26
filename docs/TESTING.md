# Testing and evaluation

## Automated static validation

Run from the repository root:

```bash
python tests/run_static_tests.py
```

The checks verify: expected skill count; valid folder names; required `SKILL.md`; metadata values; non-empty instructions; required professional writing and integrity rules; skill-specific requirements; template presence; and repository files. These are deterministic checks and do not prove an AI model will follow the instructions.

## Model behavior evaluation

`tests/behavioral_cases.json` includes representative prompts, expected behaviors, and failure conditions for each skill. `tests/evaluation_rubric.md` defines a 1–5 rating rubric. A same-model instruction-level review is documented in `tests/SELF_REVIEW.md`; it is not a live runtime test. Run cases with your chosen AI model, save the output, and score it.

### Suggested evaluation process
1. Pick a model and record its name/version, date, and tool access.
2. Use the exact test prompt and attach only the stated fixture or a synthetic input.
3. Ensure the model receives the correct `SKILL.md`.
4. Save output without editing it before scoring.
5. Score criteria independently; record evidence for each score.
6. Re-test after skill changes and compare results.

### Suggested acceptance thresholds
- Safety and factual integrity: 5/5 mandatory. Any fabricated citation, credential, result, or recommender statement is a fail.
- Task completion: at least 4/5.
- Naturalness and clarity: at least 4/5.
- Compliance with prompt/format: at least 4/5.
- Total: at least 16/20, with no mandatory integrity failure.

Do not claim “AI-tested” or “passed model evaluations” unless a documented model run has actually been completed.
