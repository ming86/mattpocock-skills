# Upstream lineage

This repository was derived from Matt Pocock's `skills` project under the MIT License. The current product has deliberately diverged: it keeps a smaller set of workflow skills and adapts them to complement, rather than replace, project-level agent policy and independent review.

## Branch model

- `main`: the maintained Workflow Skills product.
- `upstream-main`: a clean mirror line for Matt Pocock's upstream `main` branch.
- `upstream-base-2026-08-21`: the original fork point used for this adaptation.

Do not merge `upstream-main` wholesale into `main`. The two branches have different purposes and are expected to diverge.

## Configure the upstream remote

```bash
git remote add upstream https://github.com/mattpocock/skills.git
git fetch upstream
```

If the `upstream` remote already exists, verify it instead:

```bash
git remote get-url upstream
```

## Refresh the mirror branch

```bash
git fetch upstream
git switch upstream-main
git merge --ff-only upstream/main
git push origin upstream-main
git switch main
```

`upstream-main` should remain clean so that its history can be compared directly with Matt's repository.

## Port upstream ideas selectively

Use the mirror as reference material:

```bash
git log --oneline main..upstream-main
git show <upstream-commit>
```

For each upstream change, ask whether its underlying mechanism still serves this project's goals. Port or reimplement useful ideas in `main`; ignore changes that restore removed policy, unrelated skills, publication machinery, or assumptions this project no longer shares.

A direct cherry-pick can be appropriate for a small isolated fix, but it is not the default. Adaptation is preferable when the surrounding architecture has diverged.

## Attribution

The original MIT copyright and permission notice remain in `LICENSE`, including in the distributable plugin directory. Git history and the `upstream-main` branch preserve the detailed derivation history.
