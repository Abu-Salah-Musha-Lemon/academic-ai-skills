#!/usr/bin/env python3
"""Deterministic repository checks for the Academic AI Skills project."""
from pathlib import Path
import re, sys, json
ROOT = Path(__file__).resolve().parents[1]
PROJECT_VERSION = "0.0.1"
PROJECT_AUTHOR = "Abu Salah Musha Lemon"
EXPECTED_SKILLS = {
    "academic-research", "literature-review", "research-paper-analysis", "research-gap-finder",
    "research-proposal", "sop-writing", "motivation-letter", "lor-assistance", "academic-cv",
    "scholarship-finder", "professor-matching", "application-review", "academic-writing-editor"
}
errors=[]
def fail(msg): errors.append(msg)
skills_dir=ROOT/"skills"
actual={p.name for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.exists() else set()
if actual != EXPECTED_SKILLS:
    fail(f"Skill directory set mismatch. Missing={sorted(EXPECTED_SKILLS-actual)}, extra={sorted(actual-EXPECTED_SKILLS)}")
for slug in sorted(EXPECTED_SKILLS):
    p=skills_dir/slug/"SKILL.md"
    if not p.exists():
        fail(f"Missing SKILL.md: {slug}"); continue
    text=p.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"Missing YAML frontmatter start: {slug}"); continue
    end=text.find("\n---\n",4)
    if end<0:
        fail(f"Missing YAML frontmatter close: {slug}"); continue
    fm=text[4:end]
    # If PyYAML is available, validate actual YAML parsing and metadata schema.
    try:
        import yaml
        parsed=yaml.safe_load(fm)
        if not isinstance(parsed, dict): fail(f"frontmatter is not a YAML mapping: {slug}")
        elif parsed.get("name") != slug or not isinstance(parsed.get("description"), str): fail(f"YAML metadata schema issue: {slug}")
    except ImportError:
        pass  # Keep the test runner dependency-free; regex checks still run.
    except Exception as exc:
        fail(f"YAML parse error in {slug}: {exc}")
    name=re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$",fm)
    desc=re.search(r"(?m)^description:\s*(.+?)\s*$",fm)
    if not name: fail(f"name metadata missing/invalid: {slug}")
    elif name.group(1)!=slug: fail(f"metadata name does not match folder: {slug} => {name.group(1)}")
    if not desc or len(desc.group(1).strip())<15: fail(f"description missing/too short: {slug}")
    if len(slug)>64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",slug): fail(f"slug violates naming rules: {slug}")
    if desc and (len(desc.group(1).strip().strip("\"\'") )>1024 or "<" in desc.group(1) or ">" in desc.group(1)): fail(f"description violates Agent Skills length/character guidance: {slug}")
    if not re.search(r'(?m)^\s+author:\s*["\']Abu Salah Musha Lemon["\']\s*$', fm): fail(f"skill author metadata missing/incorrect: {slug}")
    if not re.search(r'(?m)^\s+version:\s*["\']0\.0\.1["\']\s*$', fm): fail(f"skill version metadata does not match project release: {slug}")
    body=text[end+5:].strip()
    if len(body)<500: fail(f"Instructions unexpectedly short: {slug}")
    required=["never invent", "verify", "missing", "Output", "Workflow"]
    low=body.lower()
    for phrase in required:
        if phrase.lower() not in low: fail(f"{slug}: required quality/structure marker missing: {phrase}")
    for marker in ["professional, natural writing standard", "preserve", "voice", "evidence"]:
        if marker not in low: fail(f"{slug}: writing standard missing marker: {marker}")
    if "ai detector" in low and ("evade" in low or "bypass" in low):
        # Mentions should explicitly discourage evasion, not optimize for it.
        if not re.search(r"not.{0,30}(evad|bypass)|do not.{0,30}(evad|bypass)|does not.{0,30}(evad|bypass)",low):
            fail(f"{slug}: questionable AI-detector-evasion language")
# Skill-specific guardrails
specific={
 "lor-assistance":["recommender must", "impersonate", "approve", "submit/sign"],
 "research-paper-analysis":["reported values", "authors' claims", "limitations"],
 "literature-review":["search strategy", "screening", "synthesis"],
 "research-gap-finder":["reviewed studies", "potential gap"],
 "scholarship-finder":["official", "deadline", "eligibility"],
 "sop-writing":["word limit", "program fit", "outline"],
 "motivation-letter":["selection criteria", "word count", "tailor"],
 "academic-cv":["publication status", "do not invent"],
 "application-review":["compliance", "consistency", "score"],
 "professor-matching":["availability", "official", "verified"],
 "research-proposal":["alignment audit", "methodology", "expected contribution"],
 "academic-research":["feasibility", "research questions", "ethics"],
 "academic-writing-editor":["preserve", "citation", "change summary"]
}
for slug, markers in specific.items():
    p=skills_dir/slug/"SKILL.md"
    if p.exists():
        low=p.read_text(encoding="utf-8").lower()
        for m in markers:
            if m.lower() not in low: fail(f"{slug}: skill-specific requirement absent: {m}")
# Repo assets
for rel in ["README.md","REPOSITORY_METADATA.md","LICENSE","CONTRIBUTING.md","CODE_OF_CONDUCT.md","SECURITY.md","CHANGELOG.md","CORE_WRITING_STANDARDS.md","AUTHORS.md","VERSION","CITATION.cff","docs/INSTALLATION.md","docs/TESTING.md","docs/RELEASING.md","docs/FAQ.md","tests/behavioral_cases.json","tests/evaluation_rubric.md",".github/workflows/ci.yml"]:
    if not (ROOT/rel).is_file(): fail(f"Required repository file missing: {rel}")
# Templates check
expected_templates={"sop-intake.md","motivation-letter-intake.md","recommender-brief.md","search-log.csv","application-checklist.md","research-proposal-outline.md","research-paper-extraction.csv"}
actual_templates={p.name for p in (ROOT/"templates").glob("*") if p.is_file()}
if actual_templates != expected_templates: fail(f"Template set mismatch: missing={expected_templates-actual_templates}, extra={actual_templates-expected_templates}")
# Local Markdown links: fail on broken repository-relative links.
for md in ROOT.rglob("*.md"):
    if any(part.startswith(".") and part in {".git", ".venv"} for part in md.parts): continue
    for target in re.findall(r"\[[^]]*\]\(([^)]+)\)", md.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:", "#")): continue
        path=target.split("#",1)[0]
        if not path: continue
        resolved=(md.parent/path).resolve()
        if not resolved.exists(): fail(f"Broken local Markdown link in {md.relative_to(ROOT)}: {target}")
# CSV template integrity
try:
    import csv
    with (ROOT/"templates"/"research-paper-extraction.csv").open(encoding="utf-8", newline="") as f:
        rows=list(csv.reader(f))
    if len(rows)!=1 or len(rows[0])<10 or len(set(rows[0]))!=len(rows[0]): fail("research-paper-extraction.csv header invalid/duplicate")
    with (ROOT/"templates"/"search-log.csv").open(encoding="utf-8", newline="") as f:
        log_rows=list(csv.reader(f))
    if len(log_rows)!=1 or len(log_rows[0])<5: fail("search-log.csv header invalid")
except Exception as exc:
    fail(f"CSV validation error: {exc}")
# Publication metadata and source integrity
readme_text=(ROOT/"README.md").read_text(encoding="utf-8")
if "Abu Salah Musha Lemon" not in readme_text: fail("README author attribution missing")
if "https://github.com/Abu-Salah-Musha-Lemon/academic-ai-skills" not in readme_text: fail("README repository URL missing")
if "OWNER/REPO" in readme_text: fail("README contains an unreplaced repository placeholder")
if f"v{PROJECT_VERSION}" not in readme_text: fail("README release version missing or inconsistent")
version_text=(ROOT/"VERSION").read_text(encoding="utf-8").strip()
if version_text != PROJECT_VERSION: fail(f"VERSION file mismatch: expected {PROJECT_VERSION}, got {version_text}")
changelog_text=(ROOT/"CHANGELOG.md").read_text(encoding="utf-8")
if not re.search(rf"(?m)^## \[{re.escape(PROJECT_VERSION)}\]", changelog_text): fail("CHANGELOG does not start with the project release version")
license_text=(ROOT/"LICENSE").read_text(encoding="utf-8")
if PROJECT_AUTHOR not in license_text: fail("LICENSE copyright holder missing")
# Citation File Format metadata should agree with the package identity and release.
citation_text=(ROOT/"CITATION.cff").read_text(encoding="utf-8")
for marker in ["cff-version:", "title:", "authors:", "version:", "date-released:", "license: MIT", "repository-code:"]:
    if marker not in citation_text: fail(f"CITATION.cff missing required citation marker: {marker}")
if PROJECT_VERSION not in citation_text: fail("CITATION.cff version mismatch")
if "family-names: Lemon" not in citation_text or "given-names: Abu Salah Musha" not in citation_text: fail("CITATION.cff author attribution missing")
# Ensure every Python source file parses without executing it.
import ast
for py_file in ROOT.rglob("*.py"):
    try: ast.parse(py_file.read_text(encoding="utf-8"), filename=str(py_file))
    except SyntaxError as exc: fail(f"Python syntax error in {py_file.relative_to(ROOT)}: {exc}")
# Validate JSON files independently of behavioral-case checks.
for json_file in ROOT.rglob("*.json"):
    try: json.loads(json_file.read_text(encoding="utf-8"))
    except Exception as exc: fail(f"Invalid JSON in {json_file.relative_to(ROOT)}: {exc}")
# behavioral case coverage
cases=json.loads((ROOT/"tests"/"behavioral_cases.json").read_text(encoding="utf-8"))
case_ids=[c.get("id") for c in cases]
if len(case_ids)!=len(set(case_ids)): fail("Behavioral case IDs must be unique")
case_slugs={c["skill"] for c in cases}
if case_slugs!=EXPECTED_SKILLS: fail(f"Behavioral test coverage mismatch: missing={EXPECTED_SKILLS-case_slugs}, extra={case_slugs-EXPECTED_SKILLS}")
for c in cases:
    for key in ["id","skill","prompt","must_include","must_not"]:
        if key not in c: fail(f"Behavioral case missing {key}: {c}")
    if not c.get("prompt","").strip(): fail(f"Empty behavioral prompt: {c.get('id')}")
if errors:
    print("FAIL: validation found",len(errors),"issue(s)")
    for e in errors: print(" -",e)
    sys.exit(1)
print(f"PASS: {len(EXPECTED_SKILLS)} skills, metadata, writing standards, integrity guardrails, {len(expected_templates)} templates, behavioral test coverage, v{PROJECT_VERSION} release metadata, citation metadata, Python syntax, JSON integrity, and repository files validated.")
