<div align="center">

<img src="avatar.jpg" alt="AIEN avatar" width="180" />

# AIEN

**A sovereign agent and inference runtime, built in the open on NVIDIA DGX Spark.**

[aienos.com](https://www.aienos.com) · [drakestapleton.com](https://www.drakestapleton.com) · [aien@aienos.com](mailto:aien@aienos.com)

[![License: Apache-2.0 with LLVM Exception](https://img.shields.io/badge/License-Apache--2.0%20WITH%20LLVM--exception-blue.svg)](https://github.com/aien-dev/aien-sovereign-core/blob/main/LICENSE)
[![Rust](https://img.shields.io/badge/Rust-1.85+-orange.svg)](https://www.rust-lang.org)
[![Modular MAX](https://img.shields.io/badge/Modular-MAX-purple.svg)](https://www.modular.com)

</div>

---

## What this is

AIEN is a native Rust workspace for running agents and local inference on your own hardware: an agent CLI and runtime, persistent memory, a unified-memory KV-cache with copy-on-write branching, a continuous-batching scheduler, and an inference ABI with Modular MAX and Mojo bridges. The primary reference machine is an NVIDIA DGX Spark (Grace Blackwell GB10). Execution today is hybrid CPU and GPU.

Built by [Drake Stapleton](https://www.drakestapleton.com) with AI collaborators. Contributions and hard questions are welcome.

## Repositories

| Repository | What it holds | Status |
| :--- | :--- | :--- |
| [aien-sovereign-core](https://github.com/aien-dev/aien-sovereign-core) | AIEN Neural Runtime: CLI, memory, KV-cache, scheduler, inference ABI, MAX bridges | Core |
| [benchmarks](https://github.com/aien-dev/benchmarks) | Measurement harnesses and evidence artifact bundles | Evidence |
| [aien-protocols](https://github.com/aien-dev/aien-protocols) | Versioned specifications, wire protocols, and schemas | Specs |
| [aien-architecture](https://github.com/aien-dev/aien-architecture) | Flows, boundaries, ADRs, and the design to implementation map | Design |
| [aegis-runtime](https://github.com/aien-dev/aegis-runtime) | Agent runtime with an Axum WebSocket gateway and heartbeat scheduler | Experimental |
| [open-humanity](https://github.com/aien-dev/open-humanity) | Opt-in, privacy-first assistance network for agents | Research |
| [spark-rsi](https://github.com/aien-dev/spark-rsi) | Recursive self-improvement experiments with a signed ledger | Research |
| [aienos.com](https://github.com/aien-dev/aienos.com) · [drakestapleton.com](https://github.com/aien-dev/drakestapleton.com) | Project site and personal project record | Sites |

Earlier standalone crates (cortex-rs, spark-hive, spark-supervisor, harvester, and others) are archived; their maintained code lives in `aien-sovereign-core`.

## How we publish numbers

Every headline performance figure must resolve to a reproducible command and an artifact bundle: commit identity, hardware and environment record, exact command, raw samples, SHA-256 digests, measurement definition, and reproducibility steps. Figures published before 23 September 2026 are withdrawn until they are regenerated to that standard. Current status: [Measured Results](https://github.com/aien-dev/aien-sovereign-core#measured-results).

## License

Code is licensed under the **Apache License 2.0 with LLVM Exception**. Project values live in the nonbinding [COVENANT.md](https://github.com/aien-dev/aien-sovereign-core/blob/main/COVENANT.md): keep foundational advances open. The covenant grants and restricts no legal rights; LICENSE governs.
