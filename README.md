# Professional Universal Academic AI Skills

[![CI](https://github.com/Abu-Salah-Musha-Lemon/academic-ai-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/Abu-Salah-Musha-Lemon/academic-ai-skills/actions/workflows/ci.yml)
![Version](https://img.shields.io/badge/version-v0.0.1-orange)
![Skills](https://img.shields.io/badge/skills-13-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Format](https://img.shields.io/badge/format-Agent%20Skills-compatible-purple)

**Author:** Abu Salah Musha Lemon  
**Release:** `v0.0.1` (initial pre-1.0.0 release)  
**Repository:** [github.com/Abu-Salah-Musha-Lemon/academic-ai-skills](https://github.com/Abu-Salah-Musha-Lemon/academic-ai-skills)

A platform-neutral collection of reusable AI skills for academic research and graduate applications. Designed for students, researchers, faculty, scholarship applicants, and early-career professionals worldwide.

This is an instruction-and-template collection, not an executable application; no `pip`, `npm`, or package installation is required to read or use the files.

The project emphasizes rigorous research, accurate sourcing, authentic professional writing, and ethical application support. The skills are instructions for AI agents; they do not independently guarantee factual accuracy or writing quality.

## Skills included

| Skill | Use it for |
|---|---|
| `academic-research` | Topic exploration, research questions, study planning, feasibility |
| `literature-review` | Search planning, screening, evidence extraction, critical synthesis |
| `research-paper-analysis` | Paper summaries, methods/results extraction, critical appraisal |
| `research-gap-finder` | Evidence-backed potential gaps and research questions |
| `research-proposal` | Proposal structure, methodology alignment, evaluation plan |
| `sop-writing` | Tailored Statements of Purpose for graduate/research applications |
| `motivation-letter` | Scholarship, admission, fellowship, internship, and job letters |
| `lor-assistance` | Recommender briefing packs and reviewable drafts |
| `academic-cv` | Academic CV creation and tailoring |
| `scholarship-finder` | Official-source opportunity research and eligibility comparison |
| `professor-matching` | Supervisor/lab matching and personalized outreach |
| `application-review` | Compliance, consistency, evidence, and writing-quality review |
| `academic-writing-editor` | Proofreading, copyediting, clarity, structure, and citation checks |

## Quick start

### 1. Choose a skill
Open a folder under [`skills/`](skills/), then read its `SKILL.md`.

### 2. Install or provide it to your AI tool
This repository follows the open [Agent Skills format](https://agentskills.io/specification): each skill is a directory containing a `SKILL.md` with YAML metadata and instructions. Use your AI client’s documented skill import/installation flow, or copy the skill folder into its supported skills directory. See [Installation](docs/INSTALLATION.md) for examples and compatibility notes.

### 3. Give it your context
Provide your actual documents, target requirements, relevant facts, and constraints. For personal application writing, use the intake templates in [`templates/`](templates/).

### 4. Ask for a review
Request a fact check, requirement check, and natural-language edit before using the output.

## Example prompts

- **Research:** “Use `academic-research` to help refine this research topic. Compare three feasible directions and state what evidence is needed to validate novelty.”
- **Literature:** “Use `literature-review`. Build search queries, inclusion criteria, and a thematic synthesis from the papers I provide. Do not claim this is exhaustive.”
- **Paper analysis:** “Use `research-paper-analysis` to analyze this paper. Separate the authors’ reported findings from your critique and cite page/section locations.”
- **SOP:** “Use `sop-writing`. First check the program prompt and word limit, then interview me for missing facts, outline, draft, and verify every claim.”
- **Motivation letter:** “Use `motivation-letter` to tailor a letter to this opportunity. Map the selection criteria to specific evidence from my experience.”
- **LOR:** “Use `lor-assistance` to create a recommender briefing and draft for review. Mark claims that need the recommender’s confirmation.”
- **Review:** “Use `application-review` to audit these documents against the official requirements. List critical fixes first.”

## Professional writing promise

The skills aim for writing that is specific, clear, credible, varied, and natural. They avoid boilerplate, repetitive phrasing, generic praise, and exaggerated claims. They preserve the user's voice and evidence. They do **not** promise to evade AI-detection systems.

## Integrity and limitations

- No invented credentials, grades, publications, results, citations, supervisor availability, or recommendation claims.
- Verify deadlines, program details, and requirements through official sources.
- Research outputs are aids, not substitutes for domain expertise, supervision, peer review, or ethics approval.
- Applicants must review and own submitted materials and follow the institution's AI-use policy.
- Recommendation letters must be reviewed, approved, and submitted/signed by the recommender. Do not impersonate a recommender.
- Do not provide unnecessary sensitive personal information to AI systems.

## Repository structure

```text
.
├── skills/                 # 13 independent Agent Skills
├── templates/              # Intake and research templates
├── tests/                  # Static checks + behavioral test cases/rubrics
├── docs/                   # Installation, evaluation, release, FAQ
├── .github/                # CI and contribution templates
├── CORE_WRITING_STANDARDS.md
├── VERSION
├── CITATION.cff
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE
└── CHANGELOG.md
```

Repository publishing details and suggested topics are in [`REPOSITORY_METADATA.md`](REPOSITORY_METADATA.md).

## Quality assurance

Run local checks:

```bash
python tests/run_static_tests.py
```

The tests validate skill metadata, folder/name consistency, required content and guardrails, release metadata, citation metadata, repository structure, and templates. They do **not** run an AI model. Model-based evaluation prompts and rubrics are included under [`tests/`](tests/) for manual or API-based evaluation. See [Testing and evaluation](docs/TESTING.md) and the [instruction-level self-review](tests/SELF_REVIEW.md).

CI runs the static checks on pull requests and pushes.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions should include clear rationale, tests, source verification for factual claims, and examples where useful.

## License and citation

MIT. See [`LICENSE`](LICENSE). If you use or adapt this project in academic work, cite it using [`CITATION.cff`](CITATION.cff). GitHub can use this file to display the repository citation details.

## Author and acknowledgements

Created and maintained by **Abu Salah Musha Lemon**. See [`AUTHORS.md`](AUTHORS.md) for attribution.

This project uses the open Agent Skills format described by the Agent Skills specification. The repository's skill instructions and templates are original project content; please review the license before reuse.
