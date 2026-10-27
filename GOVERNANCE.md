# Governance

This file applies to every `aien-dev` repository that does not carry its own
`GOVERNANCE.md`. A repository's own file takes precedence; `aien-protocols-mv`
has one for its specifications.

Status: PROPOSED. This is a draft charter for the project while it is hosted by
a fiscal sponsor. Two numbers are deliberately left open (marked **TBD**) for the
maintainer or the Technical Steering Committee to set.

## 1. Charter

**Purpose.** The project builds and maintains open, independently implemented
GPU software (compiler, runtime, driver client and kernels) that any vendor's
hardware can target. It exists to give developers a choice of compute stack.
It does not exist to replace any existing open-source project. Where an open
project already does something, we contribute to it, plug into it or test
against it, and we send fixes upstream to the projects we depend on.

**Licence.** Code is Apache-2.0 unless a repository's `LICENSE` says
otherwise. Anything that becomes in-kernel Linux code is `MIT OR GPL-2.0-only`.
There is no enterprise edition, paid tier, hosted service or token.

**Neutrality.** No company, donor or employer controls the project. Technical
decisions are made in public by the Technical Steering Committee (TSC) under
this charter.

**Amendments.** Changing this file takes a two-thirds TSC vote and a public
comment period of at least 30 days. Sections 1, 3 and 4 cannot be weakened while
a donor is paying any TSC member's salary, and that member recuses from such a
vote.

## 2. Technical Steering Committee

- **Reserved upstream seat.** At least one seat is reserved for a maintainer of
  a project the stack depends on or feeds (for example Mesa, PoCL, the Khronos
  SPIR-V tools, LLVM, the Linux kernel DRM subsystem, ggml or vLLM). That person
  sits in their own right, not as a company representative.
- **No employer majority.** People employed by, or paid under contract by, one
  organisation may hold at most one third of the seats.
- **Chair.** The chair may not be an employee or contractor of a donor that
  funds more than **TBD** percent of the project's income in the current or
  previous year. The threshold is for the maintainer or the TSC to set; no
  figure has been chosen.
- **Founding period.** Drake Stapleton holds the chair until the TSC has at
  least three members, two of them not Drake, and stands for election after the
  first year of the TSC.
- **Decisions.** Lazy consensus on public issues and pull requests. Any TSC
  member may call a vote; a simple majority of seated members decides unless
  this file says otherwise. Minutes and votes are public.
- **Evidence rule.** No release note, website claim or pitch states a
  capability without a re-runnable receipt. Releases label every capability
  PROPOSED, IMPLEMENTED, EXERCISED or QUALIFIED, and host or emulator results
  are never presented as hardware qualification.

Current members: Drake Stapleton (chair, founding period). The reserved
upstream seat is open.

## 3. Donors do not direct the work

1. A donation buys no roadmap item, no feature priority, no seat and no veto.
   Every donation agreement says so.
2. Earmarked gifts are accepted only for work the TSC has already put on the
   public roadmap.
3. Every donor of any size is listed publicly, next to the fiscal host's public
   ledger.
4. **Concentration limit.** If one donor gives more than **TBD** percent of a
   year's income, the TSC says so publicly and starts finding other funders.
   The share is for the maintainer or the TSC to set; no figure has been chosen.
5. Donor staff contribute through the same public review as everyone else.
6. Donors get no exclusive or early access and no private builds.
7. A donor that is also a hardware vendor gets no influence over backend
   priority (section 4).
8. Money the project receives may be passed on to the upstream projects it
   depends on. Those payments appear on the same public ledger.

## 4. Vendor-neutral backend policy

- Every hardware target is a backend with the same interface. No vendor's
  backend is the privileged default in the documentation or the build.
- Backends for any vendor (AMD, Intel, Arm, Qualcomm, NVIDIA or others) are
  accepted on equal terms. This is a commitment to accept them, not a claim
  that they exist today.
- Conformance is public: each backend runs the same test suite against a host
  reference, and results are published per backend.
- Where an open standard exists (SPIR-V, OpenCL, Vulkan, SYCL), the project
  targets it and sends fixes upstream rather than forking it.

## 5. Signed releases

- Release tags are annotated and signed by an accountable maintainer identity.
- The publication workflow verifies the tag signature and refuses lightweight,
  unsigned or unverified tags.
- Release artifacts carry build provenance (GitHub artifact attestations or an
  equivalent) so anyone can check which commit and workflow produced them.

Status of this section: PROPOSED. It describes the required release process; it
is not yet enforced by tooling in every repository.

## 6. Code of conduct, contributing and security

- `CODE_OF_CONDUCT.md`: the Contributor Covenant 3.0 for people.
  `AGENT_CODE_OF_CONDUCT.md` adds rules for autonomous agents.
- `CONTRIBUTING.md`: how changes are accepted and licensed.
- `SECURITY.md`: how to report a vulnerability privately.

Community Moderators for the code of conduct: Drake Stapleton. A second,
independent moderator is appointed by the TSC once it has members other than
Drake.
