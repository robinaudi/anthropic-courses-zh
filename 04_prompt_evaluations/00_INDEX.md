# Anthropic Prompt Evaluations Course — Lesson Index

Source: [github.com/anthropics/courses/prompt_evaluations](https://github.com/anthropics/courses/tree/master/prompt_evaluations)

| File | Title | Description |
|------|-------|-------------|
| [00_README.md](00_README.md) | Course README | Overview and setup instructions for the full course |
| [01_intro_to_evals.md](01_intro_to_evals.md) | Evaluations 101 | Introduction to what LLM evaluations are, why they matter, and the main approaches (code-graded, human-graded, model-graded) |
| [02_workbench_evals.md](02_workbench_evals.md) | Anthropic Workbench Evaluations | How to use the Anthropic Console Workbench to visually prototype prompts and run human-graded evaluations |
| [03_code_graded.md](03_code_graded.md) | A Simple Code-Graded Evaluation | Build a minimal code-graded eval from scratch (animal leg-count task) to understand the test→score→improve loop |
| [04_code_graded_classification.md](04_code_graded_classification.md) | Code-Graded Eval: Classification Task | More realistic code-graded eval for a multi-label customer complaint classifier (5 categories) |
| [05_promptfoo_intro.md](05_promptfoo_intro.md) | Introducing promptfoo | First look at the promptfoo open-source eval framework; re-implements the animal leg-count eval using promptfoo tooling |
| [06_promptfoo_classification.md](06_promptfoo_classification.md) | Promptfoo: Classification Evaluations | Port the customer complaint classification eval to promptfoo using `exact-match` and `contains-all` built-in graders |
| [07_promptfoo_custom_graders.md](07_promptfoo_custom_graders.md) | Promptfoo: Custom Code Graders | Write custom JavaScript grading logic in promptfoo to verify exact word-count constraints in generated text |
| [08_promptfoo_model_graded.md](08_promptfoo_model_graded.md) | Model-Graded Evaluations with promptfoo | Use a Claude model as the evaluator to grade subjective criteria (tone, age-appropriateness, guideline adherence) |
| [09_custom_model_graded.md](09_custom_model_graded.md) | Custom Model-Graded Evals | Build a custom model-grader function that scores Wikipedia-to-grade-school summaries on Conciseness, Accuracy, and Tone (each 1–5) |

## Course Summary

This 9-lesson course covers the full spectrum of LLM prompt evaluation techniques:

1. **Conceptual foundation** (Lessons 1–2): What evals are, why they matter, and how to use the Anthropic Workbench for quick human-graded testing.
2. **Code-graded evals from scratch** (Lessons 3–4): Building deterministic evaluations using Python for simple and classification tasks.
3. **promptfoo framework** (Lessons 5–9): Progressively advanced use of promptfoo — from basic setup, to built-in graders, to custom code graders, to model-graded evaluations with custom scoring rubrics.
