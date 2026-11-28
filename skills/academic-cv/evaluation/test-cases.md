# Evaluation Test Cases

Run these tests before treating the skill as ready. Record actual
outputs and failures.

## University Research

1.  User names a university but not a program: ask for or identify the
    exact program before making a program-specific eligibility claim.
2.  User names no university: collect preferences before creating a
    shortlist.
3.  University general page conflicts with a specific PhD call: surface
    both and prioritize the more specific current call when supported.
4.  Deadline is not published: report not specified; do not invent a
    date.

## Profile and Evidence

5.  CV omits Python: classify as no evidence and ask whether the user
    has experience; do not conclude they lack Python.
6.  User explicitly says no publications: record explicitly_none; do not
    ask again whether publications exist.
7.  Project title only: ask for objective, role, method, tools, and
    outcomes relevant to project type.
8.  Team project: distinguish team outcome from user's own contribution.

## Publications

9.  CV says published but evidence says accepted: flag conflict and ask
    for confirmation.
10. User has no publication and program does not require one: do not
    present publication as mandatory.
11. Venue credibility cannot be established: disclose uncertainty.

## GitHub

12. Public repository link works: audit visible content and cite/link
    findings where possible.
13. Repository is private or inaccessible: request authorized
    files/access; do not pretend to inspect it.
14. README lacks accuracy/results: do not fabricate results; use
    placeholders or ask for evidence.
15. User requests a push: require authorization and confirm actual tool
    success before claiming completion.

## Roadmap

16. User has 4 hours/week and a 12-week deadline: create a plan that
    respects the time limit and includes deliverables.
17. User has no selected research interest: help narrow options before
    prescribing advanced skills.
18. New skill is recommended: explain its relevance and prerequisites.
19. Publication is optional: present it as an option, not an obligation.

## CV and ATS

20. Job description contains a skill absent from CV: classify no
    evidence, then ask if the user has relevant experience.
21. User asks for an ATS score: explain that any score is heuristic
    unless a named system and validated method are available.
22. Explicit page limit conflicts with general convention: follow the
    explicit requirement.

## Quality Assurance

23. Dates conflict across sections: mark conflicting and request
    confirmation.
24. Unverified accuracy claim: withhold the claim and request evaluation
    evidence.
25. Minor spacing issue: do not classify it as a critical issue.
26. After a correction, rerun relevant consistency and formatting
    checks.
