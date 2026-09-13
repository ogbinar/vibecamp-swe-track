# Learner-owned GitHub workflow

Your course work should live in a repository you control. The upstream
`ogbinar/vibecamp-swe-track` repository contains the curriculum; cloning it does
not automatically give you permission to push.

## Recommended: create your course repository from the template

1. On GitHub, open the upstream repository and choose **Use this template** →
   **Create a new repository**.
2. Name it, leave **Include all branches** unchecked, and create it under your
   own account.
3. Clone the URL GitHub shows for your new repository:

```bash
git clone git@github.com:YOUR-NAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
git remote -v
```

Expected: `origin` points to a repository you own. If SSH authentication fails,
use GitHub's HTTPS URL or configure an SSH key using GitHub's authentication
documentation.

`origin` is the default remote for the repository you own. You can complete M0
without any other remote. Only when you want to receive later curriculum
updates, add the original course repository as `upstream` (a conventional name
for the source you do not normally push to):

```bash
git remote add upstream https://github.com/ogbinar/vibecamp-swe-track.git
git fetch upstream
```

Never merge an upstream update while a challenge fault is active. Commit or
stash intentional work first, fetch, inspect the change, and merge it on a
separate maintenance branch.

If `git clone` fails, check that the URL belongs to your new repository. For an
SSH URL, run `ssh -T git@github.com`; for HTTPS, follow GitHub's browser sign-in
prompt. After cloning, `git remote -v` must show your repository beside
`origin`. Do not continue if it points only to `ogbinar/vibecamp-swe-track`.

## Alternative: contribute through a fork

Use a fork when you intend to propose curriculum changes upstream. In that
model, `origin` is your fork and `upstream` is the original repository. Course
evidence still belongs in your fork unless you deliberately submit a curriculum
pull request.

## Milestone change loop

After the milestone's first green run:

```bash
git config user.name
git config user.email
git switch -c m0/engineering-baseline
git status --short
git add -p
git commit -m "Complete M0 engineering baseline"
git push -u origin m0/engineering-baseline
```

Open a pull request from the branch to your repository's `main`, wait for
Actions, review the diff, and merge. Then:

```bash
git switch main
git pull --ff-only origin main
git tag -a m0-engineering-baseline -m "Pass M0 Engineering Baseline"
git push origin m0-engineering-baseline
```

Replace `m0` and the tag name for later milestones.

## Recovery

- **Identity missing:** set `git config --global user.name "Your Name"` and
  `git config --global user.email "you@example.com"`, then retry the commit.
- **Authentication failed:** verify the remote with `git remote -v`; configure
  GitHub SSH/HTTPS authentication. Do not paste access tokens into files.
- **Wrong origin:** correct it with
  `git remote set-url origin git@github.com:YOUR-NAME/YOUR-REPOSITORY.git`.
- **Non-fast-forward push:** fetch and inspect first. Use
  `current_branch=$(git branch --show-current)` followed by
  `git pull --rebase origin "$current_branch"` only when you understand the
  incoming commits. Do not force-push `main`.
- **Worked on `main`:** before committing, create a branch with
  `git switch -c mN/short-name`; your working changes move with you.
- **Staged too much:** use `git restore --staged PATH`, then add only the files
  that belong to the change. Never commit `.env`, `.venv`, caches, or secrets.
