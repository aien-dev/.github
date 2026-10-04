## Copyright



<div align="center">

<img src="avatar.jpg" alt="AIEN avatar" width="180" />

# AIEN

**A sovereign computing stack, built in the open: its own operating system, its own compiler and reaction runtime, its own machine realization layer.**

[aienos.com](https://www.aienos.com) · [drakestapleton.com](https://www.drakestapleton.com) · [aien@aienos.com](mailto:aien@aienos.com)

</div>

---

## What this is

AIEN is an attempt to build a persistent, local computing system from the first instruction upward, on an NVIDIA DGX Spark (Grace Blackwell GB10), with no outside organization required to boot, build, trust or recover it. The founding principle: closest to the metal, fastest wins. Mojo is a default, not dogma. Beat it if you can. Build what is missing.

Built by [Drake Stapleton](https://www.drakestapleton.com) with AI collaborators. Contributions and hard questions are welcome.

## Honest status

This is research-grade, pre-alpha software. Nothing here is qualified on real hardware as a finished system. The AIENOS C kernel passes only some emulator gates and has never booted on the real machine, the reaction runtime was qualified on older builds only, and several programs are specifications with no code yet. The single source of truth for what is done and what is not is the architecture repository:

- [Plan authority](https://github.com/aien-dev/aien-architecture/blob/main/PLAN_AUTHORITY.md): which document wins
- [Current execution plan](https://github.com/aien-dev/aien-architecture/blob/main/CURRENT_EXECUTION_PLAN.md): what is being done now, with receipts
- [Milestone registry](https://github.com/aien-dev/aien-architecture/blob/main/doctrine/ROADMAP.md): milestone status

Status words used everywhere: PASS, FAIL, NOT_RUN, BLOCKED_HARDWARE, BLOCKED_OPERATOR, MISSING_IMPLEMENTATION. A passing emulator run is never described as hardware qualification.

## The repositories

| Repository | What it is |
| :--- | :--- |
| [aien-architecture](https://github.com/aien-dev/aien-architecture) | The authority for whole-system design, milestone status and sequencing. Start here. |
| [aienos](https://github.com/aien-dev/aienos) | AIENOS: our own kernel and operating system, replacing Linux on the DGX Spark. Contributors wanted. |
| [omega](https://github.com/aien-dev/omega) | The reaction runtime and compiler (Omega Systems Core). The current implementation is C. |
| [physics](https://github.com/aien-dev/physics) | Machine realization (FORGE) and the historical Atlas/PHYSICS boot artifacts. |
| [aien-protocols](https://github.com/aien-dev/aien-protocols) | Versioned specifications and reference crates for agent state, inference and evaluation. |
| [aien-sovereign-core](https://github.com/aien-dev/aien-sovereign-core) | The earlier Linux-hosted Rust runtime. Legacy, being migrated into the repositories above. |
| [benchmarks](https://github.com/aien-dev/benchmarks) | Measurement harnesses and evidence bundles. |
| [aienos.com](https://github.com/aien-dev/aienos.com) · [drakestapleton.com](https://github.com/aien-dev/drakestapleton.com) | Project site and personal project record. |

Other repositories (aegis-runtime, open-humanity, spark-rsi, atlas, aien-edge and similar) are experimental or research and do not carry status claims. Earlier standalone repositories are archived.

## Standing rules

- Language rule: Rust is scaffolding, Omega is the destination, and C or assembly only where hardware, boot, or a measurement justifies it. Nothing already merged is reverted. See [ADR 0024](https://github.com/aien-dev/aien-architecture/blob/main/docs/adr/0024-rust-scaffolding-omega-destination.md), which supersedes the old [Rust-to-C plan](https://github.com/aien-dev/aien-architecture/blob/main/docs/plans/RUST_TO_C_MIGRATION.md).
- No Python anywhere, including helper scripts.
- No CUDA toolkit and no dependence on vendor CUDA libraries. The GB10 is driven by our own native path.
- No systemd in AIENOS boot, init, services or tooling.
- Builds are offline and in-house for the trusted base. No outside dependency may be required to build, boot or recover it.
- Existing Modular MAX serving is being retired model by model, as our own stack becomes faster.
- Every performance figure must resolve to a reproducible command and a content-addressed evidence bundle. Old figures without one are withdrawn.

## How to help

Start with [AIENOS issues labelled `good first issue` or `emulator-ok`](https://github.com/aien-dev/aienos/issues). Those need no special hardware. Read each repository's CONTRIBUTING or AGENTS file first, and open pull requests with the commands you ran and their output.

## License

aienos, aien-sovereign-core and this repository are licensed under the GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later). aien-protocols uses AGPL-3.0-or-later for code and the Community Specification License 1.0 for specifications. Other repositories state their own terms, so check each one (omega and physics do not yet ship a LICENSE file). Project values live in the nonbinding [COVENANT.md](https://github.com/aien-dev/.github/blob/main/COVENANT.md): keep foundational advances open. The covenant grants and restricts no legal rights; each repository's LICENSE governs.
