<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/aienos-wordmark-dark.svg">
  <img src="assets/aienos-wordmark-light.svg" width="380" alt="AienOS: the core tree of AIEN">
</picture>

<img src="assets/allen-banner.jpg" width="100%" alt="Allen's window, drawn by his own code: a night sky with real galaxies, a small glowing sphere of points in the middle, and the words 'Hello Humanity'">

**Persistent machine intelligence on hardware I own.**

[What this is](#what-this-is) ·
[The stack](#the-stack) ·
[Allen](#allen) ·
[CUDA++](#cuda) ·
[The machines](#the-machines) ·
[Speed, with receipts](#speed-with-receipts) ·
[Right now](#right-now) ·
[The tree](#the-tree) ·
[How a change gets in](#how-a-change-gets-in) ·
[Principles](#principles)

</div>

## What this is

I am building a computing stack that runs on machines I own, with nothing in its trusted base that depends on an outside service: my own kernel (Aienux), my own language and GPU engine (Omega), a host runtime and model server, and a pipeline that judges every change on my own hardware and publishes the evidence. I work alone and direct AI agents as tools: they write, test and review; I decide. It is pre-alpha and says so. Every claim on this page links to the commit, pull request or receipt it comes from.

## The stack

<p align="center"><img src="assets/fig/stack.svg" width="100%" alt="What runs on top of what: Allen on the iMac screen, the model server, Omega, CUDA++, the Aienux kernel, and the machines."></p>

## Allen

Allen is the resident presence of the kernel. His window takes the whole screen of the iMac: a night sky with two black holes whose gravity bends the starlight, water that moves with what he is doing, a name he asks for at first meeting and keeps, and a typed line he answers from. Everything on his screen is drawn by the kernel's own C code: no graphics library, no font file, no image file.

<p align="center"><img src="assets/allen-dusk.gif" width="560" alt="Allen's dusk: the night sky and Allen are pulled into a black hole, its disk glows and dims, and the horizon closes to black."></p>

When you type goodbye, his day ends the way a day ends: everything falls into a black hole, its disk glows, and the horizon closes. The banner at the top and this dusk are frames from the kernel's own renderer, run by its test on a host computer; the dusk is on branch [feat/goodbye-event-horizon](https://github.com/aien-dev/aienux/tree/feat/goodbye-event-horizon) and has not been shown on the real iMac yet. How he is drawn: [native/kernel/ui](https://github.com/aien-dev/aienux/tree/main/native/kernel/ui).

## CUDA++

<p align="center"><img src="assets/fig/cudapp-hero.svg" width="100%" alt="CUDA++: my own path from a program to an NVIDIA GPU, and the 32 instructions of the first kernel it ran, drawn bit by bit."></p>

[CUDA++](https://github.com/aien-dev/CUDApp) is the GPU half of Omega as its own MIT project: the toolchain that writes the GPU's machine code, the runtime, the libraries and the driver client, with no CUDA toolkit, no `nvcc`, no PTX and no `libcuda`. I reverse engineered the undocumented machine code of the GB10 and wrote my own encoder for it; the whole method is in [docs/HOW_I_DID_IT.md](https://github.com/aien-dev/CUDApp/blob/main/docs/HOW_I_DID_IT.md) and the driver is explained part by part on the [repository front page](https://github.com/aien-dev/CUDApp). Today the live 35B model server runs on it with zero CUDA libraries loaded ([receipt](https://github.com/aien-dev/omega-mv/blob/89aad7c99b4fced80f92b656d2a3f350699456f0/evidence/WHAT-OMEGA-IS-20261021/live-serve-no-cuda.txt)); next it replaces NVIDIA's kernel modules ([L332](https://www.aienos.com/now/#L332)) and swaps in as a drop-in `libcuda` ([L401](https://www.aienos.com/now/#L401)).

## The machines

<p align="center"><img src="assets/fig/machines.svg" width="100%" alt="Five machines: the DGX Spark that serves and judges, the iMac that boots Aienux, the Raspberry Pi 5, QEMU, and the Windows PC that is the target for AIEN Rig."></p>

- **DGX Spark** serves the 35B model on my own engine, and its judge rules every pull request. [The server's mapped libraries, receipt](https://github.com/aien-dev/omega-mv/blob/89aad7c99b4fced80f92b656d2a3f350699456f0/evidence/WHAT-OMEGA-IS-20261021/live-serve-no-cuda.txt).
- **Intel iMac 2017** boots [Aienux](https://github.com/aien-dev/aienux) on bare metal; [boot evidence](https://github.com/aien-dev/aienux/tree/main/evidence/imac_kernel1_2026-10-17). The kernel it runs is on an [open pull request stack](https://github.com/aien-dev/aienux/pulls), not yet main.
- **Raspberry Pi 5** ran the same kernel on real hardware ([evidence](https://github.com/aien-dev/aienux/tree/main/evidence/pi5_hardware_runs_2026-10-13)) and hosts the [readings window](https://github.com/aien-dev/readings-window).
- **QEMU** runs every kernel gate first; an emulator qualifies nothing physical ([gates](https://github.com/aien-dev/aienux/blob/main/native/kernel/GATES.md)).
- **Windows PC, RTX 5070** is the target for [AIEN Rig](https://github.com/aien-dev/aien-rig): a local AI engine in a 12 GB budget, measured so far on the Spark ([receipts](https://github.com/aien-dev/aien-sovereign-core-mv/tree/rig/engine-12gb/docs/inference/evidence/rig-engine-20261019)). Nothing of mine has run on the card yet.

## Speed, with receipts

<p align="center"><img src="assets/fig/speed.svg" width="100%" alt="The 35B model on the Spark: total decoded tokens per second against the number of simultaneous conversations. The batched door reaches 65.7 tokens per second at 32 conversations, past the 63.25 single-conversation ceiling; one row after another stays near 31."></p>

| What | Number | Against | Receipt |
| :-- | :-- | :-- | :-- |
| **35B model, many conversations at once** (batched door, all tokens checked identical to serving each request alone) | 65.7 tokens/s total at 32 conversations | 63.25 tokens/s, the one-conversation ceiling: batching passes it because rows share weight reads | [branch serve/q36-batch-v2, evidence](https://github.com/aien-dev/aien-sovereign-core-mv/tree/serve/q36-batch-v2/evidence/q36-batch-20261021) |
| **27B model, live server decode**, median of 4 runs of 256 greedy tokens | 7.63 tokens/s | 0.752 of that model's 10.15 tokens/s memory ceiling; my previous server: 6.29 | [branch qwen38/serve-fast, evidence](https://github.com/aien-dev/aien-sovereign-core-mv/tree/qwen38/serve-fast/evidence/qwen38-serve-fast-20261019) |
| **Ceiling probes on the GB10**, my own kernels | 115.14 TFLOPS tensor-core peak, 195.1 GB/s reads | the machine's physical limits, measured | [in CUDA++, evidence](https://github.com/aien-dev/CUDApp/tree/main/evidence/OWN30B-T3-TC-PEAK-BW-5faa0f70-20261013T2236Z) |

Numbers on branches say so. The same-model measurement against llama.cpp and vLLM is running ([L394](https://www.aienos.com/now/#L394)); when it lands its table goes here, losses included.

## Right now

The live ledger is at **[www.aienos.com/now/](https://www.aienos.com/now/)**: every line is a promise with an owner and an observable finish, written by the agents as they work. In motion today:

- **The 35B faster**: batch strokes (above), the motor that serves several strokes per weight read, document reads split across eight batch rows, and the head-to-head against llama.cpp and vLLM.
- **CUDA++** ([L395](https://www.aienos.com/now/#L395)): CUDA's pain points with the fix for each shown as a command and a receipt, the swap down to the kernel driver ([L401](https://www.aienos.com/now/#L401)), and my own GB10 kernel driver ([L332](https://www.aienos.com/now/#L332)).
- **Alpha** ([L388](https://www.aienos.com/now/#L388)): one tagged release a stranger can install and run; the public guide and the install-script failure it hit are tracked in the open.
- **Aienux on the iMac**: the open pull request stack (netboot, keyboard, boot disk) and Allen talking to the model through a courier in the kernel.
- **Research programme**: an offline cost simulator, a bounded learning-mechanism search, and a published verdict on a symbolic rewrite layer ([cut 2 of 7 action graphs, no measurable win on 27B decode](https://github.com/aien-dev/omega-mv/blob/symbolic/rewrite-layer/evidence/symbolic-rewrite/VERDICT.md)).

## The tree

The core repositories. AienOS is the name for the whole tree; `Aienix` is retired.

| Repository | What it is |
| :-- | :-- |
| [aienux](https://github.com/aien-dev/aienux) | Aienux: my operating system kernel in C, the QEMU gates, and Allen's window. Pre-alpha. |
| [omega-mv](https://github.com/aien-dev/omega-mv) | Omega: my language for verified programs, its checker, and the GB10 GPU engine. |
| [CUDApp](https://github.com/aien-dev/CUDApp) | CUDA++: the GPU half of Omega on its own, MIT. No NVIDIA user-space software. |
| [aien-sovereign-core-mv](https://github.com/aien-dev/aien-sovereign-core-mv) | Host runtime in Rust: the `aien` CLI and daemon, the Spark judge, the model server. |
| [aien-architecture-mv](https://github.com/aien-dev/aien-architecture-mv) | The authority for how AIEN fits together: decision records and the execution plan. |
| [aien-protocols-mv](https://github.com/aien-dev/aien-protocols-mv) | Written contracts between the parts: byte formats, schemas, test vectors. |
| [physics-mv](https://github.com/aien-dev/physics-mv) | Machine realization layer in C and the GB10 boot artefacts. |
| [aien-rig](https://github.com/aien-dev/aien-rig) | Local AI and a measured frame-rate tuner for RTX gaming PCs. Pre-alpha. |
| [interplane-mv](https://github.com/aien-dev/interplane-mv) | INTERPLANE: an open protocol between models and agent runtimes. Apache-2.0. |

<details>
<summary><strong>Record, boot and services</strong> (the rest of the tree)</summary>

| Repository | What it is |
| :-- | :-- |
| [aien-receipts](https://github.com/aien-dev/aien-receipts) | Signed verification receipts published by the Spark judge. Data only, append only. |
| [benchmarks-mv](https://github.com/aien-dev/benchmarks-mv) | Measurement harnesses and evidence bundles. |
| [agent-archive](https://github.com/aien-dev/agent-archive) | Every AI agent chat on the Spark, one schema, verbatim. |
| [atlas](https://github.com/aien-dev/atlas) | The boot seed: 1,480 bytes that verify the next image by SHA-256. |
| [synapse](https://github.com/aien-dev/synapse) | Agent-native changeset and coordination service. |
| [aegis-runtime-mv](https://github.com/aien-dev/aegis-runtime-mv) | Agent runtime in Rust. Pre-alpha. |
| [spark-rsi-mv](https://github.com/aien-dev/spark-rsi-mv) | Proposes small code changes, tests them in a sandbox, hands a review branch to me. |
| [open-humanity](https://github.com/aien-dev/open-humanity) | Opt-in peer assistance network for agents in distress. Prototype. |
| [readings-window](https://github.com/aien-dev/readings-window) | Read-only window onto the Spark's readings, served from the Pi. Running. |
| [pi-register](https://github.com/aien-dev/pi-register) | Register of the services on the Pi house server. |
| [aien-translate](https://github.com/aien-dev/aien-translate) | Translation server backed by the live model on my own runtime: no API key, text stays on the machine. In use. |
| [rpi5-uefi](https://github.com/aien-dev/rpi5-uefi), [edk2-non-osi](https://github.com/aien-dev/edk2-non-osi) | Preservation fork of the Pi 5 UEFI firmware chain. |
| [aienos.com](https://github.com/aien-dev/aienos.com) | Source of [www.aienos.com](https://www.aienos.com). |
| [interplane.io](https://github.com/aien-dev/interplane.io), [translate](https://github.com/aien-dev/translate), [t3code](https://github.com/aien-dev/t3code) | Site rebuilt hourly from the Spark, and two forks kept for contributions. |

</details>

## How a change gets in

<p align="center"><img src="assets/fig/merge-flow.svg" width="100%" alt="A branch is judged by the Spark, a signed receipt is published, the hosted check confirms the bundle matches, and only then does the pipeline merge."></p>

The repositories' gate manifests, the judge and the whole design are described in [aien-architecture-mv](https://github.com/aien-dev/aien-architecture-mv) ([ADR 0033](https://github.com/aien-dev/aien-architecture-mv/tree/main/docs/adr)). To take part: open issues on the repository the change belongs to, and expect your change to be judged exactly as mine are.

<details>
<summary><strong>Research</strong> (preprints, none peer reviewed)</summary>

Papers live at [www.aienos.com/research/](https://www.aienos.com/research/), each with a PDF and a SHA256SUMS file; what is measured and what is blocked is at [www.aienos.com/research/status/](https://www.aienos.com/research/status/). Recent:

| Title | Kind | Link |
| :-- | :-- | :-- |
| Computing Machinery and Understanding: From the Imitation Game to the Turing | preprint | [10.5281/zenodo.23437498](https://doi.org/10.5281/zenodo.23437498) |
| Computing Machinery and Understanding: The Turing as a Measure Emerging from AIEN | companion | [10.5281/zenodo.23437568](https://doi.org/10.5281/zenodo.23437568) |
| The Stapleton Doctrine | position paper | [PDF](https://www.aienos.com/research/the-stapleton-doctrine/paper.pdf) |
| The Turing: A Unit of Verified Explanatory Gain | brief | [PDF](https://www.aienos.com/research/the-turing-brief/paper.pdf) |
| Omega: A Programming Language Built for Verified Programs | language design | [PDF](https://www.aienos.com/research/omega-language/paper.pdf) |
| The AIEN Papers: The Complete Collection | collection, 120 pages | [PDF](https://www.aienos.com/research/the-aien-papers/paper.pdf) |

</details>

## Principles

- **Closest to the metal.** The fastest correct path wins, and headline numbers are reported as a fraction of the machine's physical limit.
- **Sovereign.** No outside dependencies in the trusted base: no CUDA toolkit in the GPU path, no systemd under the kernel, builds offline and reproducible.
- **Rust is scaffolding, Omega is the destination.** C only where the hardware justifies it, assembly only where measured.
- **Evidence or nothing.** A result is not demonstrated until a receipt for it exists. A target is never evidence of itself.
- **Compare, and say where I lose.** Progress is measured against the machine's physical ceiling, my own previous runs, and other systems' published numbers on the same hardware, each labelled measured by me or published by others.
- **Open.** The tree is AGPL-3.0-or-later; CUDA++ is MIT; interplane-mv is Apache-2.0 today. The models served are trained by others and keep their makers' licences; no AIEN-trained weights exist yet.

## Licence

AGPL-3.0-or-later for the tree ([LICENSE](https://github.com/aien-dev/aienux/blob/main/LICENSE)), CUDA++ MIT, interplane-mv Apache-2.0. Each repository carries its own LICENSE file.

<sub>AienOS is not a UNIX and makes no such claim. UNIX is a registered trademark of The Open Group. NVIDIA, DGX and Grace Blackwell are trademarks of NVIDIA Corporation. Raspberry Pi is a trademark of Raspberry Pi Ltd. CUDA is a trademark of NVIDIA Corporation; CUDA++ is not affiliated with or endorsed by NVIDIA.</sub>
