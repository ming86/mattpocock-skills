# Issue tracker: GitLab

Issues and specs for this repo live as GitLab issues. Use the [`glab`](https://gitlab.com/gitlab-org/cli) CLI for all operations.

## Conventions

- **Create an issue**: `glab issue create --title "..." --description "..."`. Use a heredoc for multi-line descriptions. Pass `--description -` to open an editor.
- **Read an issue**: `glab issue view <number> --comments`. Use `-F json` for machine-readable output.
- **List issues**: `glab issue list -F json` with appropriate `--label` filters.
- **Comment on an issue**: `glab issue note <number> --message "..."`. GitLab calls comments "notes".
- **Apply / remove labels**: `glab issue update <number> --label "..."` / `--unlabel "..."`. Multiple labels can be comma-separated or by repeating the flag.
- **Close**: `glab issue close <number>`. `glab issue close` does not accept a closing comment, so post the explanation first with `glab issue note <number> --message "..."`, then close.
- **Merge requests**: GitLab calls PRs "merge requests". Use `glab mr create`, `glab mr view`, `glab mr note`, etc., the same shape as `gh pr ...` with `mr` in place of `pr` and `note`/`--message` in place of `comment`/`--body`.

Infer the repo from `git remote -v`; `glab` does this automatically when run inside a clone.

## Merge requests as a triage surface

**MRs as a request surface: no.** _(Set to `yes` if this repo treats external merge requests as feature requests; `/triage` reads this flag.)_

When set to `yes`, MRs run through the same labels and states as issues, using the `glab mr` equivalents:

- **Read an MR**: `glab mr view <number> --comments` and `glab mr diff <number>` for the diff.
- **List external MRs for triage**: `glab mr list -F json`, then keep only MRs whose author is not a project member/owner (a contributor's MR, not a maintainer's in-flight work).
- **Comment / label / close**: `glab mr note`, `glab mr update --label`/`--unlabel`, `glab mr close`.

Unlike GitHub, GitLab numbers issues and MRs separately, so `#42` is unambiguous once you know which surface the maintainer means.

## When a skill says "publish to the issue tracker"

Create a GitLab issue.

## When a skill says "fetch the relevant ticket"

Run `glab issue view <number> --comments`.

## Wayfinding storage

When the project chooses GitLab Issues for durable Wayfinder state:

- **Map:** keep one issue or, when appropriate and available, an epic for the effort, using the current Wayfinder sections such as Destination, Established context, Decisions so far, Open questions, Not yet clear enough to decide, and Out of scope.
- **Work units:** use child or linked issues for precise research, prototype, clarification, or enabling work. A `Part of #<map>` line is a portable fallback when no native parent relationship is available. Type labels are optional project conventions.
- **Dependencies:** use native blocking links when the project tier supports them, for example the `/blocked_by #<n>` quick action posted with `glab issue note`. Otherwise record an explicit `Blocked by:` relationship or the project's established dependency notation.
- **Ready frontier:** ready means genuine blockers are resolved. Selection, assignment, claiming, parallelism, and execution order belong to the governing orchestration policy rather than this tracker template.
- **Results:** record outcomes using the project's normal issue conventions and update the canonical map with material decisions, facts, or newly exposed questions. Closing or assigning issues follows project conventions and current authorization.
