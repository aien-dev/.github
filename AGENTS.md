# aien-dev/.github (organization profile and community defaults)

> The special `.github` repository of the `aien-dev` GitHub organization. It holds the organization profile shown at https://github.com/aien-dev (`profile/README.md`) and the default community files that GitHub applies to every `aien-dev` repository without its own copy: `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `GOVERNANCE.md`, the pull request template and the issue template. `AGENT_CODE_OF_CONDUCT.md` sits beside them; GitHub does not apply it automatically, so the others link to it. There is no code, no build and no CI here.

Shared rules: read https://www.aienos.com/agents/RULES.md first. This file adds what is specific to this repository; where the two differ, this file wins here.

## Scope

- Applies to the whole repository.
- A change here reaches every `aien-dev` repository that lacks its own file of the same name. `CONTRIBUTING.md`, `SECURITY.md` and `.github/PULL_REQUEST_TEMPLATE.md` say that a repository's own copy takes precedence; keep that sentence where it exists.
- What each file is:
  - `profile/README.md`: the organization front page. Its images live in `profile/` and `profile/assets/` and are referenced by relative path.
  - `CONTRIBUTING.md`: pull request rules, inbound licensing and the Contributor License Agreement.
  - `SECURITY.md`: private vulnerability reporting.
  - `AGENT_CODE_OF_CONDUCT.md`: the governance standard for autonomous agents.
  - `CODE_OF_CONDUCT.md`: the Contributor Covenant 3.0 for people, with the reporting address filled in.
  - `GOVERNANCE.md`: the project charter, Technical Steering Committee rules, donor policy, vendor-neutral backend policy and release signing. Two thresholds are marked TBD for the maintainer.
  - `.github/PULL_REQUEST_TEMPLATE.md` and `.github/ISSUE_TEMPLATE/implementation-initiative.md`: the fallback templates.
  - `CONSTITUTION.md` and `COVENANT.md`: statements of values. `COVENANT.md` says it grants and restricts no legal rights.
  - `LICENSE` (Apache License 2.0) and `NOTICE` (copyright and trademark notice).

## Installation

```bash
git clone https://github.com/aien-dev/.github.git
cd .github
```

Nothing to build or install. The files are Markdown, images and licence text.

## Configuration

GitHub reads fixed paths in this repository; moving or renaming them silently removes the behaviour:

- `profile/README.md`: the organization profile.
- `.github/PULL_REQUEST_TEMPLATE.md`: the default pull request body.
- `.github/ISSUE_TEMPLATE/`: the default issue forms. The YAML front matter (`name`, `about`, `title`, `assignees`) must stay valid.
- `CONTRIBUTING.md`, `SECURITY.md`: the default community health files.

## Usage

```bash
# Must print nothing: no em dashes or en dashes in any Markdown file
grep -rnP '[\x{2013}\x{2014}]' --include='*.md' .
```

There is no local renderer. To check how a Markdown change renders, push the branch and open the file on github.com; the organization profile itself only updates after the change merges to `main`.

## Conventions

- Profile claims follow the rules the profile states under "Principles": every number links a receipt, numbers are compared only with the machine's physical ceiling and the project's own previous run, never with other people's systems, and a result still on a branch says so.
- When a repository is renamed, archived or added, update its name and link in `profile/README.md` in the same change.
- After editing any aien-dev repository's purpose, status or links, or adding a repository, update aien-dev/sovereign-intelligence `index/curated.yml` (layer, evidence, one-line purpose) in the same piece of work. Its hourly index-sync fails and names any public repository without an entry. Never name a private repository there.
- Plain direct English. No em dashes or en dashes.
- One purpose per pull request, with the commands you ran and their output in the description, as `CONTRIBUTING.md` requires. Sign off commits with `git commit -s`.

## Safety and approvals

- Ask the maintainer before changing `LICENSE`, `NOTICE`, the licensing or Contributor License Agreement sections of `CONTRIBUTING.md`, the reporting channels in `SECURITY.md` or `CODE_OF_CONDUCT.md`, `GOVERNANCE.md`, or `AGENT_CODE_OF_CONDUCT.md`. These bind every repository that falls back to them.
- Never put a secret, a private address or personal data in the profile or a template; this repository is public and its files appear across the organization.
- `main` is protected and the protection applies to administrators. Work on a branch and merge through a pull request; never force-push.

## Further reading

- `CONTRIBUTING.md`: how changes are accepted, licensing, the Contributor License Agreement.
- `SECURITY.md`: how to report a vulnerability.
- `AGENT_CODE_OF_CONDUCT.md`: rules for autonomous agents across `aien-dev`.
- `CODE_OF_CONDUCT.md` and `GOVERNANCE.md`: conduct for people, and how the project is governed.
- `profile/README.md`: what AIEN is, the machines, and how a change gets into the core repositories.
