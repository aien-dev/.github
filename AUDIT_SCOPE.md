# Audit scope

Written for an outside, independent security audit. Revision described:
`2a9e2282ef9ac3909109a9aa6cffee5867c08247` on `main`, 2026-10-26. Everything below is taken from
the repository's own files at that revision; items marked NOT_RUN were not executed while writing
this document.

## What this repository is

The special `.github` repository of the `aien-dev` GitHub organization. It holds the organization
profile (`profile/README.md` and its images) and the default community files that GitHub applies
to every `aien-dev` repository without its own copy: `CONTRIBUTING.md`, `SECURITY.md`,
`AGENT_CODE_OF_CONDUCT.md`, the pull request template and an issue template. It also carries
`CONSTITUTION.md`, `COVENANT.md`, `LICENSE` (Apache 2.0) and `NOTICE`. There is no code, no build
and no CI (AGENTS.md).

## What to review, in priority order

1. `SECURITY.md`: the reporting channels inherited by every repository without its own policy.
   Check that the channels are private and that the text does not ask reporters to send secrets.
2. `.github/PULL_REQUEST_TEMPLATE.md` and `.github/ISSUE_TEMPLATE/implementation-initiative.md`:
   fallback templates for every repository. Check they do not ask contributors to paste logs,
   tokens, hostnames or other private detail into public threads.
3. `CONTRIBUTING.md`: pull request rules, inbound licensing and the Contributor License Agreement.
4. `profile/README.md`: the public organization page. Check it carries no private address, secret
   or personal data (AGENTS.md forbids these in the profile and templates).
5. `AGENT_CODE_OF_CONDUCT.md`: the governance standard for autonomous agents across the
   organization.

## What an auditor can and cannot check here

- Can check: the text of the default community files and templates, and whether any public file
  leaks private data.
- Cannot check: code (there is none), organization settings such as branch protection and
  private vulnerability reporting (they live in GitHub, not in the tree), or any other repository.

## Trust boundaries

- Files here are applied by GitHub to every `aien-dev` repository that lacks its own copy. A change
  reaches the whole organization.
- AGENTS.md requires the maintainer's approval before changing `LICENSE`, `NOTICE`, the licensing
  or CLA sections of `CONTRIBUTING.md`, the reporting channels in `SECURITY.md`, or
  `AGENT_CODE_OF_CONDUCT.md`.
- `main` is protected, the protection applies to administrators, and changes merge through a pull
  request (AGENTS.md).

## Threat model summary

- Assets: the integrity of organization-wide policy text; the privacy of reporters and
  contributors.
- Attackers considered: an edit that redirects vulnerability reports to a public channel; a
  template that leads contributors to leak private data.
- Defended: protected `main`, pull-request-only changes, maintainer approval for the files above.
- Not defended / explicitly out of scope: code security of other repositories; GitHub's own
  handling of advisories.

## Build from source at a pin

Nothing to build or install. The files are Markdown, images and licence text.

## Run every test

There is no test suite and no CI. AGENTS.md documents one check (NOT_RUN while writing this
document); it must print nothing:

```sh
grep -rnP '[\x{2013}\x{2014}]' --include='*.md' .
```

## Known limitations and NOT_RUN

- There is no local renderer; AGENTS.md says rendering is checked on github.com after pushing.
- Whether private vulnerability reporting is enabled per repository is not recorded in the tree.

## Dependencies and provenance

No lockfile, no vendored code, no dependencies, no GitHub Actions.

## Evidence

There are no receipts here. The record is the git history of `main` and its merged pull requests.
