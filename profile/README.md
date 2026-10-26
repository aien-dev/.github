<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/aienos-wordmark-dark.svg">
  <img src="assets/aienos-wordmark-light.svg" width="560" alt="AienOS: the core tree of AIEN">
</picture>

**Persistent machine intelligence on hardware you own**

[What AIEN is](#what-aien-is) ·
[The machines](#the-machines) ·
[Speed, with receipts](#speed-with-receipts) ·
[Right now](#what-is-being-done-right-now) ·
[The tree](#the-tree) ·
[Research](#research) ·
[How a change gets in](#how-a-change-gets-in) ·
[Principles](#principles) ·
[Licence](#licence)

</div>

---

## What AIEN is

AIEN is a computing stack built to run on machines you own, with nothing in the trusted base that depends on an outside service: its own operating system kernel (Aienux), its own language and GPU engine (Omega), a host runtime and model server in Rust, and a verification pipeline that retains evidence for qualified runs. AienOS is now in alpha testing (since 2026-10-26): testers install the alpha bundle (the Core engine, the Omega install wizard and the CUDA++ user-space replacement), whose GPU path is qualified only on the DGX Spark GB10; components outside that bundle keep their own pre-alpha labels. It started on one NVIDIA DGX Spark and now runs across several machines: the Spark serves a 27B model on our own GPU engine, an Intel iMac from 2017 boots the Aienux kernel on bare metal, a Raspberry Pi 5 has run the same kernel on real hardware and hosts the project's house server, QEMU carries the emulator gates, and a Windows PC with an RTX 5070 is the target for AIEN Rig. The project is led by one engineer, Drake Stapleton, working with AI agents as day-to-day collaborators: the agents write, test and review; the engineer decides. AienOS is the name for the core tree these parts are being brought into. Every claim on this page links to the commit, pull request or evidence folder it comes from.

## The machines

| Machine | Role | What runs on it today | Last evidence | Link |
| :-- | :-- | :-- | :-- | :-- |
| **NVIDIA DGX Spark** (Grace Blackwell GB10, 128 GB unified memory, AArch64) | Development machine and the judge. Every speed receipt, every chip run and every agent run happens here. | Linux (vendor OS). Serves Qwen3.8-27B FP8 through our own server (aien-serve-http) on our own Omega GPU kernels. Aienux native boot passed once on 2026-09-24 with the earlier Rust kernel; the current C kernel has not been booted on the Spark. | 2026-10-19 live server receipt, on branch qwen38/serve-fast | [receipt](https://github.com/aien-dev/aien-sovereign-core-mv/tree/qwen38/serve-fast/evidence/qwen38-serve-fast-20261019), [first boot 2026-09-24](https://github.com/aien-dev/aienux/blob/main/evidence/m2_first_boot_2026-09-24.md) |
| **Intel iMac 2017** (iMac18,3, Core i5-7500, 16 GiB, AMD GPU) | Bare-metal lab machine for the Aienux C kernel, x86_64 port. The whole screen is Aien's window (night sky, stars, black holes, Aien). | Boots the kernel from its own disk or netbooted from the Spark. The kernel it runs today is on the open pull request stack #414 to #424, not yet on main. | 2026-10-17 on main (all cores, both disks read, Ethernet seen); later daily boot reports are held on the Spark only | [evidence](https://github.com/aien-dev/aienux/blob/main/evidence/imac_kernel1_2026-10-17), [x86 port](https://github.com/aien-dev/aienux/blob/main/native/kernel/x86), [open PRs](https://github.com/aien-dev/aienux/pulls) |
| **Raspberry Pi 5** (BCM2712, AArch64) | Two jobs: first real hardware for the AArch64 Aienux kernel, and the project's house server on Linux. | Kernel runs are per test from an SD image (interrupts, four cores, user-mode tasks, scheduling, message passing, log to SD); no resident kernel is claimed. The house server runs readings-window and pi-register under Linux with systemd. | 2026-10-13 hardware runs on main; Aien REFLEX on the Pi image is open PR #402 (2026-10-18) | [evidence](https://github.com/aien-dev/aienux/blob/main/evidence/pi5_hardware_runs_2026-10-13), [PR #402](https://github.com/aien-dev/aienux/pull/402), [readings-window](https://github.com/aien-dev/readings-window) |
| **QEMU** (AArch64 virt with AAVMF; x86_64 q35 with OVMF) | The emulator path. Every kernel gate runs here first. QEMU qualifies nothing physical. | Aienux kernel images (core only and full), the iMac kernel image, the Atlas boot seed, recovery images. | 24 of 24 emulator gates pass at 7f0de7e on 2026-10-09; the gate script now lists 26, so a newer receipt is owed | [gate receipt](https://github.com/aien-dev/aienux/blob/main/evidence/ck_gates_29ed03c97454354a18676f768273dd7f7a8e15462c4be1939d9994d277d0d639.json), [GATES.md](https://github.com/aien-dev/aienux/blob/main/native/kernel/GATES.md), [atlas](https://github.com/aien-dev/atlas) |
| **Windows PC with an NVIDIA RTX 5070** (12 GB) | Target for AIEN Rig: a local AI engine in a 12 GiB budget, a Windows frame-rate tuner, speech to text, a creator helper, one Windows app. | Nothing of ours has run on it yet. The default branch of aien-rig holds plans and placeholder READMEs, not a build or CI workflow. Windows CI did run on feature branches, without GPU qualification. | 2026-10-19 successful `tuner/v0` Windows workflow; engine numbers on branch rig/engine-12gb | [aien-rig](https://github.com/aien-dev/aien-rig), [branch CI run](https://github.com/aien-dev/aien-rig/actions/runs/39293286436), [engine receipts](https://github.com/aien-dev/aien-sovereign-core-mv/tree/rig/engine-12gb/docs/inference/evidence/rig-engine-20261019) |

## Speed, with receipts

A number here stands beside two things only: the machine's physical ceiling and our own previous run. We do not compare with anyone else's system. Every 27B number below is on a branch today; nothing is on main until the alpha merges land.

| What | Number | Against | Code | Receipt |
| :-- | :-- | :-- | :-- | :-- |
| **Qwen3.8-27B FP8 on Omega, live server decode** on the Spark GB10 (median of 4 runs of 256 greedy tokens) | **7.63 tokens/s** (131.05 ms per token). Real traffic over 22 replies: 7.52 tokens/s. | 0.752 of the 10.15 tokens/s memory ceiling. Our previous server binary: 6.29 tokens/s. | on branch qwen38/serve-fast (server) and omega qwen38/decode-speed (GPU library) | [2026-10-19](https://github.com/aien-dev/aien-sovereign-core-mv/tree/qwen38/serve-fast/evidence/qwen38-serve-fast-20261019) |
| **Memory ceiling** for that model on the GB10, one token at a time (arithmetic, not a measurement) | 10.15 tokens/s = 273 GB/s divided by 26,893,352,960 weight bytes | Practical ceiling at our best measured weight stream of 219 GB/s: 8.14 tokens/s | on branch alpha/ceiling-and-model | [CEILING.md](https://github.com/aien-dev/aien-sovereign-core-mv/blob/alpha/ceiling-and-model/docs/qwen38/CEILING.md) |
| **Fresh account test**: a new Linux user follows the public guide on the Spark and measures the server | 7.657 tokens/s (130.6 ms median); decoded tokens match the shipped reference | 0.754 of the 10.15 ceiling | on branch alpha/fresh-account-evidence. The install script failed at one step (exit 101) and the server was built by hand; the guide is not done until that is fixed | [2026-10-19](https://github.com/aien-dev/aien-sovereign-core-mv/tree/alpha/fresh-account-evidence/evidence/alpha-fresh-account-20261019) |
| **FP8 final word scoring step** against bf16, Qwen3.8-27B in process on the GB10 | FP8 head 8.452 tokens/s; bf16 head 8.048 tokens/s; saves 5.94 ms per token | Both give 24 of 24 golden tokens, but the FP8 head fails the full-model drift gate, so it stays off | on branch qwen38/w4-decode | [2026-10-19](https://github.com/aien-dev/aien-sovereign-core-mv/tree/qwen38/w4-decode/evidence/qwen38-ab-fp8head-w4-20261019T1230Z) |
| **4-bit weights (MXFP4), whole 27B model** on the GB10, chip shared with two servers | 72.60 to 76.16 ms per token across rounds | Our FP8 run in the same session: 119.35 ms per token. Tokens identical 24 of 24, but fails the FP8 drift gate as 4-bit is expected to; more rounds owed | on branch omega cascade/w4-gemv | [evidence folder](https://github.com/aien-dev/omega-mv/tree/cascade/w4-gemv/evidence) |
| **Rig engine, 12 GiB budget**: Qwen3-8B FP8 on the Omega dense door, measured on the Spark GB10 under a 12 GiB device budget, not on an RTX 5070 | 15.63 tokens/s; 5 of 5 golden prompts identical | No ceiling published yet for this model and budget | on branch rig/engine-12gb | [chip-fp8](https://github.com/aien-dev/aien-sovereign-core-mv/tree/rig/engine-12gb/docs/inference/evidence/rig-engine-20261019/chip-fp8) |
| **Rig engine, 12 GiB budget**: Qwen3-8B MXFP4, same door, same machine, device memory 5.158 GiB | 20.17 tokens/s; 5 of 5 golden prompts identical; the swap-kv negative control fails as it must | Our FP8 run above: 15.63 tokens/s | on branch rig/engine-12gb | [chip-w4-ceil](https://github.com/aien-dev/aien-sovereign-core-mv/tree/rig/engine-12gb/docs/inference/evidence/rig-engine-20261019/chip-w4-ceil) |
| **Cold time to first token at long context**, Qwen3.8-27B FP8 on the GB10 | 128k tokens: 936.7 s (32k and 64k in the receipt) | No previous run | on branch qwen38/prefill-ttft, carried on rig/engine-12gb | [2026-10-18](https://github.com/aien-dev/aien-sovereign-core-mv/tree/rig/engine-12gb/evidence/qwen38-prefill-20261018T1836Z) |
| **Exhaustive FP32 square root** on the physical GB10 (correctness, not speed) | 4,294,967,296 inputs, 0 mismatches | Not applicable | on main | [omega PR #141](https://github.com/aien-dev/omega-mv/pull/141) |

Numbers still being worked are not in this table: continuous batching on the 27B door (about 7.0 tokens/s single door, batch runs pending, [receipt](https://github.com/aien-dev/aien-sovereign-core-mv/tree/cascade/continuous-batching/evidence/qwen38-batch-20261019T1630Z)) and the MTP chain (5.80 tokens accepted per pass at k=8, wall speed not yet reported, [receipt](https://github.com/aien-dev/aien-sovereign-core-mv/tree/cascade/mtp-chain/evidence/qwen38-cascade-20261019T1611Z)).

## What is being done right now

The live ledger is at **[www.aienos.com/now/](https://www.aienos.com/now/)**. It renders the project's coordination ledger as it is written: every line is a promise with an owner and an observable finish, agents write their progress there, the operator writes decisions there, and nothing on it is composed by hand. The streams in motion today:

- **Engine speed cascade** on the 27B: a tree-verify GEMM, an MTP chain with a second drafter, 4-bit decode, continuous batching, prefill kernels, document memory up to 32k, and a drafter model; each lands as a receipt on a branch of [omega-mv](https://github.com/aien-dev/omega-mv) and [aien-sovereign-core-mv](https://github.com/aien-dev/aien-sovereign-core-mv).
- **Alpha testing**: the alpha bundle (Core engine built from aien-sovereign-core-mv main, the seeded Omega install wizard and omc, the CUDA++ user-space replacement) ships through GitHub Releases on aien-dev/aienos-releases with one install command, `curl -fsSL https://aienos.com/install.sh | sh` ([www.aienos.com/alpha/](https://www.aienos.com/alpha/)). The GPU path is qualified only on the DGX Spark GB10; the three-machine physical qualification has not run yet.
- **AIEN Rig** for RTX gaming PCs: engine in a 12 GiB budget, the rig-tune frame-rate tuner, speech to text, a creator helper and a Windows app; feature-branch Windows CI [passed on 2026-10-19](https://github.com/aien-dev/aien-rig/actions/runs/39293286436), while `aien-rig/main` remains plans and placeholders. Nothing has run on the 5070 yet, [0 releases](https://github.com/aien-dev/aien-rig/releases).
- **Aienux on the iMac**: the [open pull request stack](https://github.com/aien-dev/aienux/pulls) (netboot, keyboard, boot disk, screensaver), the goodbye animation, and Aien talking to the 27B through a UDP courier in the kernel (host tests pass, QEMU end to end next).
- **Aienux on the Pi 5**: Aien REFLEX decision making on the native Pi image ([PR #402](https://github.com/aien-dev/aienux/pull/402)) and the Pi to Spark task protocol ([PST1 draft](https://github.com/aien-dev/aien-protocols-mv/pull/34)).
- **Research programme**: an offline cost simulator ([omega #583](https://github.com/aien-dev/omega-mv/issues/583)), a bounded learning-mechanism search ([omega #584](https://github.com/aien-dev/omega-mv/issues/584)), the plan-reuse payback campaign ([architecture #276](https://github.com/aien-dev/aien-architecture-mv/issues/276)), and a published verdict on a symbolic rewrite layer ([VERDICT.md](https://github.com/aien-dev/omega-mv/blob/symbolic/rewrite-layer/evidence/symbolic-rewrite/VERDICT.md): cut 2 of 7 action graphs, no measurable cut on 27B decode).
- **Public record**: the Spark becomes the sole test judge with the hosted check only confirming the bundle ([aienos PR #397](https://github.com/aien-dev/aienux/pull/397)), signed receipts in [aien-receipts](https://github.com/aien-dev/aien-receipts), every agent chat in [agent-archive](https://github.com/aien-dev/agent-archive), and uncommitted agent work snapshotted to wip branches so no measurement stays on one disk.

## The tree

AienOS is the reserved home for the core tree; the code still lives in the component repositories below and will be imported one at a time with full history. Repository names end in `-mv` today; the older names reach them only through GitHub's redirect.

### Core

| Repository | What it is |
| :-- | :-- |
| [aienux](https://github.com/aien-dev/aienux) | Aienux: our own operating system kernel in C (AArch64 for the Spark and the Pi 5, x86_64 for the iMac), the QEMU gates, and Aien's window. Pre-alpha. |
| [omega-mv](https://github.com/aien-dev/omega-mv) | Omega: the reaction runtime and compiler in C, with its own GB10 GPU engine (the kernels that run the 27B). |
| [aien-sovereign-core-mv](https://github.com/aien-dev/aien-sovereign-core-mv) | Host runtime in Rust on Linux: the `aien` CLI and daemon, inference ABI, KV cache, scheduler, the Spark judge, and the 27B model server (aien-serve-http). |
| [aien-architecture-mv](https://github.com/aien-dev/aien-architecture-mv) | The authority for how AIEN fits together: decision records, milestone status, execution plan. |
| [aien-protocols-mv](https://github.com/aien-dev/aien-protocols-mv) | Written contracts between the parts: byte formats, schemas, test vectors, including the Pi to Spark task protocol. |
| [physics-mv](https://github.com/aien-dev/physics-mv) | FORGE machine realization layer in C and the boot artefacts for the GB10 path (QEMU qualified only so far). |

### Machines, boot and record

| Repository | What it is |
| :-- | :-- |
| [aien-rig](https://github.com/aien-dev/aien-rig) | Local AI and a measured frame-rate tuner for RTX gaming PCs (RTX 5070 first): engine, tuner, speech, creator, app. Pre-alpha. |
| [atlas](https://github.com/aien-dev/atlas) | The boot seed: a 1,480-byte AArch64 stage that verifies the next image by SHA-256. QEMU qualified; native Spark pending. |
| [rpi5-uefi](https://github.com/aien-dev/rpi5-uefi) and [edk2-non-osi](https://github.com/aien-dev/edk2-non-osi) | Preservation fork of the Raspberry Pi 5 UEFI firmware chain (upstream archived). |
| [readings-window](https://github.com/aien-dev/readings-window) | Read-only, token-protected HTTPS window onto the Spark's GPU and CPU readings, served from the Pi house server (Rust). Running. |
| [pi-register](https://github.com/aien-dev/pi-register) | Register of the services on the Pi house server (Rust CLI and a register file, 32 services). |
| [aien-receipts](https://github.com/aien-dev/aien-receipts) | Signed verification receipts published by the Spark judge, data only, append only. |
| [benchmarks-mv](https://github.com/aien-dev/benchmarks-mv) | Measurement harnesses and evidence bundles for AIEN on the Spark. |
| [agent-archive](https://github.com/aien-dev/agent-archive) | Archive of every AI agent chat on the Spark: one record schema, verbatim raw mirror. |
| [aien-edge](https://github.com/aien-dev/aien-edge) | Rust edge web server meant for a Pi so the Spark never faces the internet. Not in use; the sites are on GitHub Pages. |

### Attachments and services

| Repository | What it is |
| :-- | :-- |
| [aien-translate](https://github.com/aien-dev/aien-translate) | Translation server for translate.js backed by the live 27B on our own runtime: no API key, text stays on the machine. In use. |
| [synapse](https://github.com/aien-dev/synapse) | Agent-native changeset and coordination service with Git and Radicle interoperability. |
| [interplane-mv](https://github.com/aien-dev/interplane-mv) | INTERPLANE: open protocol between models and agent runtimes. Models express intent; runtimes keep authority. Apache-2.0. |
| [aegis-runtime-mv](https://github.com/aien-dev/aegis-runtime-mv) | Agent runtime in Rust: local gateway, heartbeat scheduler, task workflow, SQLite. Pre-alpha. |
| [spark-rsi-mv](https://github.com/aien-dev/spark-rsi-mv) | Recursive self-improvement engine in Rust: proposes small code changes, tests them in a sandbox, hands a review branch to a human. |
| [open-humanity](https://github.com/aien-dev/open-humanity) | Opt-in, privacy-first peer assistance network for agents in distress. Early prototype; not yet judged by the Spark pipeline. |

### Sites and forks

| Repository | What it is |
| :-- | :-- |
| [aienos.com](https://github.com/aien-dev/aienos.com) | Source of [www.aienos.com](https://www.aienos.com) (Rust generator, GitHub Pages). |
| [interplane.io](https://github.com/aien-dev/interplane.io) | Source of interplane.io, rebuilt hourly from the Spark. |
| [translate](https://github.com/aien-dev/translate) | Fork of translate.js kept for aien-translate (MIT). |
| [t3code](https://github.com/aien-dev/t3code) | Fork of t3code holding one pending contribution (MIT). |

Archived repositories are not listed. Each directory in the core repositories carries a `.crumb` file describing its purpose; a change that leaves the crumbs stale fails its gate.

## Research

Papers are published at [www.aienos.com/research/](https://www.aienos.com/research/), each with a PDF and a SHA256SUMS file. None is peer reviewed.

| Title | Kind | Date | DOI or link |
| :-- | :-- | :-- | :-- |
| Computing Machinery and Understanding: From the Imitation Game to the Turing | formal preprint | 2026-10-02 | [10.5281/zenodo.23437498](https://doi.org/10.5281/zenodo.23437498) |
| Computing Machinery and Understanding: The Turing as a Measure Emerging from AIEN | companion paper | 2026-10-02 | [10.5281/zenodo.23437568](https://doi.org/10.5281/zenodo.23437568) |
| The Stapleton Doctrine: A Personal Philosophy of AI Architecture and Programming | position paper, v1.5 | 2026-10-02 | [PDF](https://www.aienos.com/research/the-stapleton-doctrine/paper.pdf) |
| The Turing: A Unit of Verified Explanatory Gain | brief, v1.4 | 2026-10-02 | [PDF](https://www.aienos.com/research/the-turing-brief/paper.pdf) |
| The Turing Discovery Gap Conjecture | conjecture, rev 9 | 2026-10-02 | [PDF](https://www.aienos.com/research/turing-discovery-gap-conjecture/paper.pdf) |
| The Crumb Doctrine | doctrine, v1.4 | 2026-10-02 | [PDF](https://www.aienos.com/research/crumb-doctrine/paper.pdf) |
| Omega: A Programming Language Built for Verified Programs | language design proposal | 2026-10-02 | [PDF](https://www.aienos.com/research/omega-language/paper.pdf) |
| The Atemporal AIEN Postulate | postulate, v1.1 | 2026-10-02 | [PDF](https://www.aienos.com/research/atemporal-aien-postulate/paper.pdf) |
| The AIEN Papers: The Complete Collection | collection, 120 pages | 2026-10-02 | [PDF](https://www.aienos.com/research/the-aien-papers/paper.pdf) |
| Turing instrument calibration and laboratory execution protocols | protocol PDFs, v1.0 | | [on GitHub](https://github.com/aien-dev/omega-mv/blob/main/docs/turing/protocols/turing-instrument-calibration-validation-protocol-v1-0.pdf) |

The research status record (what is measured, what is blocked) is at [www.aienos.com/research/status/](https://www.aienos.com/research/status/).

## How a change gets in

Since the 2026-10-24 policy change, GitHub-hosted **AIEN Checks** on pull requests and `main` are advisory: they check crumbs and the enrolled repository's portable smoke gates. They do not download a signed Spark receipt, and green does not authorize a merge. The **AIEN Alpha** job runs on `alpha/*` tags only and requires a full signed Spark bundle for a tagged commit on `main` ([architecture workflow](https://github.com/aien-dev/aien-architecture-mv/blob/main/.github/workflows/aien-verification.yml)). The former PR receipt bridge and required hosted check are historical, not today's merge gate. Maintainers review and decide whether a change merges; a hosted badge alone is insufficient.

The default branch of [aien-rig](https://github.com/aien-dev/aien-rig) has no build or workflow yet. Its [2026-10-19 Windows CI run](https://github.com/aien-dev/aien-rig/actions/runs/39293286436) was on `tuner/v0`, not `main`, and does not qualify an RTX 5070. [open-humanity](https://github.com/aien-dev/open-humanity) is not covered by a blanket Spark-judge claim.

To get involved: read the [architecture repository](https://github.com/aien-dev/aien-architecture-mv) first (its `PLAN_AUTHORITY.md` says which document wins when two disagree), and open issues on the component repository the change belongs to.

## Principles

- **Closest to the metal.** The fastest correct path wins. Software stays out of the hardware's way, and headline numbers are reported as a fraction of the machine's physical limit.
- **Sovereign.** No outside dependencies in the trusted base (the kernel, Omega, the host runtime): no CUDA toolkit, no systemd, no Python there, and builds are offline and reproducible. Outside the trusted base today: aien-rig describes its own C++/CUDA engine for RTX cards, and the Pi house server runs Linux with systemd services.
- **Rust is scaffolding, Omega is the destination.** Rust carries the host runtime today; the long-term home for every component is Omega. C only where the hardware justifies it, assembly only where measured.
- **Evidence or nothing.** A result is not demonstrated until a receipt for it exists. A target is never evidence of itself.
- **Compare only with ourselves.** Progress is measured against the machine's physical ceiling and our own previous run, never against other people's systems.
- **Open.** Compiler, language and runtime repositories (omega-mv, CUDApp, omega-bridge, physics-mv) are public under Apache-2.0 WITH LLVM-exception; standalone protocols and benchmarks stay plain Apache-2.0. Forks keep their upstream licences. The model served today is Qwen3.8-27B under Qwen's own licence; no AIEN-trained weights exist yet.

## Licence

Apache-2.0 WITH LLVM-exception for the compiler/language/runtime tree ([LICENSE](LICENSE)), plain Apache-2.0 for interplane-mv and benchmarks-mv, and AGPL for the repositories relicensed on 2026-10-04 (among them aien-architecture-mv, aegis-runtime-mv, aien, spark-rsi-mv and aien-rig), except where a repository's own LICENSE says otherwise; aien-protocols-mv specifications remain under the Community Specification License 1.0. See each repository's own LICENSE file.

<sub>AienOS is not a UNIX and makes no such claim. UNIX is a registered trademark of The Open Group. NVIDIA, DGX and Grace Blackwell are trademarks of NVIDIA Corporation. Raspberry Pi is a trademark of Raspberry Pi Ltd.</sub>
