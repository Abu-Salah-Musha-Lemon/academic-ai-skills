# Release guide

The initial prepared release is **v0.0.1**. The repository version is recorded in the root `VERSION` file and synchronized with the `metadata.version` field in every `skills/*/SKILL.md`.

## Before publishing the initial release

1. Confirm `VERSION` contains `0.0.1`.
2. Confirm `CHANGELOG.md`, `README.md`, `CITATION.cff`, and every skill's `metadata.version` identify `0.0.1`.
3. Run `python tests/run_static_tests.py` from the repository root.
4. Review the skills, templates, license, author attribution, and repository links.
5. Push the project contents to the `main` branch and confirm GitHub Actions passes.

## Create the GitHub release

After the files are on GitHub and CI passes, create the annotated tag:

```bash
git tag -a v0.0.1 -m "Academic AI Skills v0.0.1"
git push origin v0.0.1
```

Then open **GitHub → Releases → Draft a new release**, select the existing `v0.0.1` tag, use `v0.0.1` as the release title, and publish the release notes from `CHANGELOG.md`. You may attach the ZIP as a convenience, but the repository source files remain authoritative.

## Future version updates

When preparing a later release, update the root `VERSION`, `CHANGELOG.md`, README version badge/release line, `CITATION.cff`, and every skill's `metadata.version` together. Re-run the static tests before tagging.

Versioning guidance: PATCH for typo, clarity, or guardrail fixes; MINOR for backward-compatible new skills or templates; MAJOR for significant workflow changes or breaking reorganizations. Keep releases below `1.0.0` while the collection is still evolving.
