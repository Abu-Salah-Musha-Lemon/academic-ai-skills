# GitHub repository setup metadata

Repository: [Abu-Salah-Musha-Lemon/academic-ai-skills](https://github.com/Abu-Salah-Musha-Lemon/academic-ai-skills)

Initial release: **v0.0.1**  
Project author: **Abu Salah Musha Lemon**

Author/maintainer: **Abu Salah Musha Lemon**

Repository name: `academic-ai-skills`

Suggested short description: `Reusable AI skills for academic research, scholarly writing, and graduate applications with evidence and integrity checks.`

Suggested topics (GitHub):
- `agent-skills`
- `academic-research`
- `literature-review`
- `research-assistant`
- `sop`
- `motivation-letter`
- `recommendation-letter`
- `scholarships`
- `academic-writing`
- `ai-prompts`
- `open-source`

Suggested visibility: Public

Suggested default branch: `main`

Before publishing:
1. The public repository already exists. Upload the project contents to its `main` branch.
2. The README CI badge is configured for `Abu-Salah-Musha-Lemon/academic-ai-skills`.
3. Add the short description and topics above in GitHub repository settings.
4. Enable Issues and Discussions if you want community feedback.
5. Enable private vulnerability reporting if available.
6. Review the license and copyright notice.
7. Run tests, then push the files.

## Publish the prepared project

Because the target GitHub repository already exists, Git is the safest publishing method: clone it, copy the contents of this project into the clone (including the hidden `.github/` directory), then review and push:

```bash
git clone https://github.com/Abu-Salah-Musha-Lemon/academic-ai-skills.git
cd academic-ai-skills
# Copy the prepared project contents into this directory.
git status
python tests/run_static_tests.py
git add .
git commit -m "Publish academic AI skills collection"
git push origin main
```

Do not upload the ZIP as the only repository file. Extract it first, then publish the contents of the `academic-ai-skills/` folder so `README.md`, `skills/`, `docs/`, `tests/`, `.github/`, `VERSION`, and `CITATION.cff` appear at the repository root. The ZIP may optionally be attached to the GitHub Release as a convenience download.

## GitHub settings checklist

- Set the description and topics listed above.
- Confirm the repository license is detected as MIT.
- Confirm GitHub Actions is enabled and the `Skill validation` workflow runs.
- Keep the default branch as `main`.
- Create and publish the initial `v0.0.1` release only after reviewing the published files and confirming CI passes.
