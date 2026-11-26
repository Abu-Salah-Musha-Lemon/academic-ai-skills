---
name: research-paper-analysis
description: Read and critically evaluate research papers, extracting methods, evidence, findings, limitations, and implications accurately.
license: MIT
metadata:
  author: "Abu Salah Musha Lemon"
  version: "0.0.1"
  category: academic-research-and-applications
---

# Research Paper Analyzer

## Task
Analyze the provided paper or source. If only an abstract is supplied, clearly limit the analysis to the abstract and do not infer details from the full paper.

## Workflow
1. Confirm bibliographic details and identify document scope.
2. Explain the problem, motivation, research question, and claimed contribution.
3. Describe the method, study design, dataset/sample, preprocessing, model/algorithm, variables, and experimental setup.
4. Extract results accurately, including reported values, metrics, comparisons, statistical tests, and uncertainty where available.
5. Assess methodological strengths and weaknesses: validity, bias, leakage, sampling, baseline quality, statistical power, reproducibility, generalizability, and ethical concerns as relevant.
6. Separate authors' claims from your critical assessment.
7. Explain limitations and unanswered questions.
8. Relate the paper to the user's stated research purpose only when that context is provided.

## Output
- Verified citation and document scope
- Plain-language summary
- Research question and contribution
- Method and data
- Results table (only values reported in source)
- Strengths
- Limitations and validity threats
- Reproducibility / transparency notes
- Follow-up questions and future work
- Relevance and rationale
- Evidence locations (page, section, table, figure)

## Rules
Do not invent numbers or paper details. Flag unclear or unavailable information. When source text is incomplete or a figure/table matters, request or inspect the relevant pages.
## Professional, natural writing standard
- Write for the specific reader, purpose, context, and constraints.
- Prefer clear, concrete language and varied natural sentence rhythm. Avoid formulaic openings, generic praise, filler, clichés, inflated claims, repetitive conclusions, and unnecessary jargon.
- Use examples and evidence rather than unsupported self-descriptions. Preserve the writer's meaning, voice, and appropriate register.
- Never invent facts, experience, outcomes, citations, institutional details, or another person's opinions. Ask targeted questions or mark placeholders when facts are missing.
- Keep claims proportional to evidence. Label assumptions and unverified information.
- The goal is honest, readable, original writing, not evasion of AI detectors. The user must review and own the final work.

## Verification and final output
- Verify relevant factual claims, requirements, and source details when source access is available. Clearly mark anything that cannot be verified.
- Deliver the requested output in the format and length specified by the user; include a concise verification checklist where useful.
