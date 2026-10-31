# Contributing to aien-dev

This file applies to every `aien-dev` repository that does not carry its own
`CONTRIBUTING.md`. A repository's own file takes precedence.

## Before you start

- Read the repository's `README.md` and `AGENTS.md`. Most repositories require
  evidence: the commands you ran and their output, attached to the change.
- Read `SECURITY.md` before reporting a vulnerability. Do not open a public
  issue for one.
- For specification changes in `aien-protocols-mv`, follow `GOVERNANCE.md` and
  `VERSIONING.md` there. Specifications are licensed under the Community
  Specification License 1.0, not the Apache License 2.0.

## Human-Directed Agentic Engineering

Development follows Human-Directed Agentic Engineering (HDAE): humans define goals, architecture, constraints, acceptance criteria and stopping points; agents implement, execute checks, diagnose failures and revise within those boundaries. Human review retains responsibility for claims, acceptance and release decisions. This describes the development method, not permission for an agent to merge, publish or operate hardware.

For the documented method and systems-software case study, see Gregory M. Kurtzer, *Ginux: Building an Independent Kernel That Runs Linux Userspace through Human-Directed Agentic Engineering* (2026), [doi:10.5281/zenodo.23682548](https://doi.org/10.5281/zenodo.23682548).

## Pull requests

1. Work on a branch named for what it does.
2. Keep the change to one purpose. Include the commands you ran and their
   output in the description.
3. Add tests that fail without the change and pass with it. Include a negative
   control where the repository's conventions ask for one.
4. Sign off every commit (`git commit -s`, Developer Certificate of Origin
   1.1). The sign-off certifies you wrote the contribution or have the right
   to submit it.
5. Do not include third-party code, binaries or model weights unless you state
   their origin and licence in the pull request and they are compatible with
   this policy.

## Licensing of contributions

Inbound equals outbound: a contribution to a repository licensed under the
Apache License 2.0 is accepted under the Apache License 2.0. You keep the
copyright in your contribution.

## Contributor License Agreement (CLA)

This section is the Individual Contributor License Agreement for
`aien-dev`. It is accepted by submitting a pull request; no separate signature
is required.

By submitting a contribution to any `aien-dev` repository, you represent that:

1. You are the author of the contribution, or you have the authority to submit
   it on behalf of its author or owner.
2. The contribution contains no third-party material that you are not
   authorised to contribute under these terms.

And you grant to Drake Stapleton and AIEN (the "Maintainer"):

1. A perpetual, worldwide, non-exclusive, royalty-free, irrevocable copyright
   licence to reproduce, prepare derivative works of, publicly display,
   publicly perform, sublicense and distribute your contribution and such
   derivative works, under the Apache License 2.0 and under any other terms the
   Maintainer chooses, including commercial or proprietary terms. This is the
   right to relicense your contribution; it is what allows the project to be
   offered under a different licence, or folded into a commercial product, in
   the future.
2. A perpetual, worldwide, non-exclusive, royalty-free, irrevocable patent
   licence to make, have made, use, offer to sell, sell, import and otherwise
   transfer your contribution, where that licence applies only to patent claims
   you can license that are necessarily infringed by your contribution alone or
   by its combination with the repository it was submitted to.
3. No warranty and no support obligation from you, unless you state otherwise
   in writing.

You retain all right, title and interest in your contribution, including the
right to use it elsewhere under any terms you choose. This agreement does not
transfer copyright ownership.

If you contribute on behalf of an employer, you confirm you have permission to
grant these rights. If you cannot accept this section, do not submit a pull
request; open an issue instead and the Maintainer will discuss an alternative.

## Code of conduct

People follow `CODE_OF_CONDUCT.md` (Contributor Covenant 3.0). Autonomous
agents also follow `AGENT_CODE_OF_CONDUCT.md`. How decisions are made, and the
rule that donors do not direct the work, are in `GOVERNANCE.md`. A repository's
own file takes precedence.
