# Issue tracker: GitHub

Issues and specs for this repo live as GitHub issues. Use the `gh` CLI for all operations.

## Conventions

- **Create an issue**: `gh issue create --title "..." --body "..."`. Use a heredoc for multi-line bodies.
- **Read an issue**: `gh issue view <number> --comments`, filtering comments by `jq` and also fetching labels.
- **List issues**: `gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'` with appropriate `--label` and `--state` filters.
- **Comment on an issue**: `gh issue comment <number> --body "..."`
- **Apply / remove labels**: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **Close**: `gh issue close <number> --comment "..."`

Infer the repo from `git remote -v`; `gh` does this automatically when run inside a clone.

## Pull requests as a triage surface

**PRs as a request surface: no.** _(Set to `yes` if this repo treats external PRs as feature requests; `/triage` reads this flag.)_

When set to `yes`, PRs run through the same labels and states as issues, using the `gh pr` equivalents:

- **Read a PR**: `gh pr view <number> --comments` and `gh pr diff <number>` for the diff.
- **List external PRs for triage**: `gh pr list --state open --json number,title,body,labels,author,authorAssociation,comments` then keep only `authorAssociation` of `CONTRIBUTOR`, `FIRST_TIME_CONTRIBUTOR`, or `NONE` (drop `OWNER`/`MEMBER`/`COLLABORATOR`).
- **Comment / label / close**: `gh pr comment`, `gh pr edit --add-label`/`--remove-label`, `gh pr close`.

GitHub shares one number space across issues and PRs, so a bare `#42` may be either: resolve with `gh pr view 42` and fall back to `gh issue view 42`.

## When a skill says "publish to the issue tracker"

Create a GitHub issue.

## When a skill says "fetch the relevant ticket"

Run `gh issue view <number> --comments`.

## Wayfinding storage

When the project chooses GitHub Issues for durable Wayfinder state:

- **Map:** keep one issue for the effort, optionally labelled `wayfinder:map`, using the current Wayfinder sections such as Destination, Established context, Decisions so far, Open questions, Not yet clear enough to decide, and Out of scope.
- **Work units:** use child issues or ordinary linked issues for precise research, prototype, clarification, or enabling work. GitHub sub-issues can be linked through the sub-issues API; where they are unavailable, a task list in the map plus `Part of #<map>` in the child is sufficient. Labels such as `wayfinder:research` or `wayfinder:prototype` are optional project conventions, not required by the method.
- **Dependencies:** prefer GitHub native issue dependencies when available. An edge can be added with `gh api --method POST repos/<owner>/<repo>/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-db-id>`, where `<blocker-db-id>` is the blocker's numeric database id from `gh api repos/<owner>/<repo>/issues/<n> --jq .id`. Where native dependencies are unavailable, record an explicit `Blocked by:` line or another project-standard relationship.
- **Ready frontier:** ready means the unit's genuine blockers are resolved. Selection, assignment, claiming, parallelism, and execution order belong to the governing orchestration policy rather than this tracker template.
- **Results:** record the result where the project normally keeps ticket outcomes and update the canonical map with material decisions, facts, or newly exposed questions. Closing, assigning, or commenting on issues follows project conventions and current authorization.
