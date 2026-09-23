# Agent Identity Standard

Version 1.0, 2026-09-23. Applies to every aien-dev open-source repository.

## Why this exists

These repositories are built primarily by AI agents. When something breaks,
we need to answer one question fast: who did it. Which agent, which model,
which version, in which session, under whose supervision. Identity is not
credit. It is an audit trail.

## Authority

This standard extends the Linux kernel AI Coding Assistants policy
(`Documentation/process/coding-assistants.rst`):

- AI agents must never add `Signed-off-by`. Only a human can certify the
  Developer Certificate of Origin. The human supervisor reviews the work,
  adds their own sign-off by explicit action, and takes responsibility.
- AI assistance must be disclosed with an `Assisted-by` trailer.

We require more detail than the kernel minimum, because agents do most of
the work here.

## Required commit trailers

Every commit authored or materially assisted by an AI agent must end with
these trailers, in this order:

```text
Agent-Name: <the name the agent goes by>
Agent-Model: <model name and version, as reported by the agent runtime>
Agent-Provider: <the organization that built the model>
Agent-Session: <session or run identifier, when the harness provides one>
Assisted-by: <name>:<model>
```

Example:

```text
Agent-Name: Aien
Agent-Model: Muse Spark 1.3
Agent-Provider: Meta
Agent-Session: main agent 2026-09-23
Assisted-by: Aien:Muse Spark 1.3
```

Rules:

- Values come from the runtime. Never invent a model name, version, or
  session id. If the harness reports no session id, write
  `Agent-Session: unknown`.
- Name the model that actually did the work, as printed at run time. Never
  a menu label or a generic family name when a specific version is known.
- One signing agent per commit. If two agents touched the work, the one
  that produced the final diff signs.
- The human supervisor is recorded with `Co-authored-by:` per each
  repository's existing convention.
- Agents must never add `Signed-off-by`, `Reviewed-by:`, or any other
  human-certification trailer.

## Pull requests

Every agent-opened pull request must include an Agent Identity section with
the same four fields (name, model, provider, session) plus the supervisor
who approved the work.

## Enforcement

Repositories enforce this with an identity check in the agent preflight
script and in CI. Reference implementation (`scripts/check-agent-identity.sh`):

```bash
#!/usr/bin/env bash
# Fail if any non-merge commit in range lacks the required identity trailers.
# Usage: check-agent-identity.sh <base>   (example: origin/main)
set -euo pipefail
base="${1:?usage: check-agent-identity.sh <base>}"
fail=0
start="$(git merge-base HEAD "$base")"
for sha in $(git rev-list --no-merges "$start"..HEAD); do
  msg="$(git log -1 --format=%B "$sha")"
  for field in Agent-Name Agent-Model Agent-Provider; do
    if ! printf '%s' "$msg" | grep -qE "^${field}: .+"; then
      echo "identity audit FAIL ${sha}: missing '${field}:' trailer"
      fail=1
    fi
  done
done
exit "$fail"
```

A pull request whose commits fail the identity audit is not merged.
