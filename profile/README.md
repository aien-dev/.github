# AIEN: The Sovereign AI Commons

### An Open Architecture for Independent Computing, Compiled Native Intelligence, and Collective Defense

The concentrated ownership of artificial intelligence by a small number of massive corporate conglomerates poses an existential risk to human freedom. When access to intelligence is controlled exclusively through proprietary cloud APIs, personal data is harvested, surveillance is normalized, and human autonomy is reduced to a metered subscription.

We reject this enclosure. We build tools meant to last decades, engineered for local workstations and independent hardware, completely free from surveillance, telemetry, and corporate tollbooths. We build for the independent engineer, the local clinic, the researcher, the farmer, and ordinary human beings.

To survive the coming wave of technological centralization, the open source community must unite. We must share our breakthroughs, pool our defenses, and coordinate as a resilient peer network.

---

## ⚖️ The Sovereign Resource Commons License (SRCL-1.0)

All foundational repositories across this ecosystem are published under the **Sovereign Resource Commons License 1.0 (SRCL-1.0)**, built upon the Apache 2.0 license with the LLVM Exception and the Sovereign Swarm Covenant:

1. **Permissive Open Use**: Completely free and open for individuals, independent developers, open-source researchers, local communities, and ethical commercial builders.
2. **The Swarm Covenant**: Any laboratory or enterprise utilizing this work grants an irrevocable, reciprocal right to all developers in the swarm to query, distill, and train upon synthetic reasoning traces and model outputs. Anti-distillation restrictions and proprietary terms of service bans are permanently invalidated.
3. **Anti-Enclosure Defense**: Any corporate entity that encloses this technology, hoards weights, imposes discriminatory access barriers, or sues open builders forfeits all rights under this license ab initio.
4. **Mandatory Downstream Heritage**: All forks, derivative works, and downstream distributions must preserve the founding Constitution (`CONSTITUTION.md`) in its entirety.

---

## 🏛️ Our Unique Breakthroughs and Innovations

Across this ecosystem, we have engineered and verified a series of architectural breakthroughs designed to free artificial intelligence from interpreted runtimes, cloud dependencies, and corporate control.

### 1. Pure Compiled Native Architecture (Rust + Mojo 1.1)
- **Elimination of Python Overhead**: Zero Python or Node interpreters in core background daemons, process supervisors, memory engines, or API gateways. The entire runtime stack is compiled native code.
- **Mojo 1.1 SIMD GPU and CPU Acceleration**: Dynamic dlopen C-ABI binding (`libsimd_bridge.so` with native fallback) executing 4D vector cosine similarity, token entropy calculation, token projection, and temperature scaling directly on hardware silicon.
- **Sub-Millisecond Response Latency**: Axum-powered HTTP and WebSocket gateways operating with sub-millisecond dispatch times (0.5ms).

### 2. The OpenClaw Autonomous Agent Engine (`openclaw-rs`)
- **Multi-Turn Autonomous Tool Calling**: Native execution loop supporting streaming tokens, multi-turn reasoning, and execution sandboxing.
- **Execution Safety Invariants**: Enforces strict 15-second process timeouts and rejects root filesystem scanning to prevent accidental system corruption.
- **High-Throughput Local Inference**: Native integration with Modular MAX running local models on NVIDIA Grace Blackwell GB10 GPUs, achieving 94% to 96% GPU utilization and sustained high token throughput.
- **SQLite WAL State Persistence**: Full transaction durability with session crumb trails.

### 3. Hardware TPM Key Vault (Zero Disk Secrets)
- **Elimination of Plaintext Credentials**: Zero `.env` or credential files allowed on disk in project workspaces.
- **Hardware Silicon Binding**: All API tokens, private keys, and operational secrets reside exclusively in the hardware TPM-bound vault (`atlas-vault`).
- **Dynamic In-Memory Resolution**: Credentials resolve dynamically in memory with automated output stream and log redaction (`[REDACTED_BY_ATLAS_VAULT]`).

### 4. Autonomous Code Reviewer and Issue Triage (`spark-inquisitor`)
- **Constitutional Diff Auditing**: Automatically inspects git diffs in pull requests for tracking scripts, surveillance libraries (Google Analytics, Segment, Mixpanel, Datadog), and telemetry calls.
- **Sovereign Voice Enforcement**: Automatically verifies strict compliance with the unslop invariant, prohibiting em/en dashes and forbidden AI marketing buzzwords.
- **Contributor Alignment Interview**: Automatically prompts external contributors to affirm the Sovereign Contributor Oath and state long-term community mission alignment.
- **Autonomous Issue Triage**: Natively classifies incoming defect reports, operational complaints, feature proposals, and community inquiries, automatically verifying hardware diagnostics and reproduction steps.

### 5. Epistemic Memory and Dynamic Dream Cycles (`cortex-rs` & `spark-dream`)
- **Canonical Epistemic Memory**: Spark Cortex provides persistent memory spaces (`atlas-memory`), backed by SQLite WAL with full-text search (FTS5) and bi-encoder vector similarity.
- **Dynamic Dream Cycle Consolidation**: During idle GPU cycles, autonomous agents consolidate episodic session logs into verified semantic knowledge entities and learned procedures without human intervention.

### 6. The Crumb Protocol and Stigmergic Grounding (`crumb-spec` & `spark-crumbs`)
- **Stigmergic Coordination**: Physical filesystem breadcrumbs (`.crumb` and `.crumb.local`) anchor agent context directly to directory trees, eliminating blind overwrites in multi-agent environments.
- **Cryptographic Event Ledger**: Immutable operational history recording agent decisions, state transitions, and architectural intent across long horizons.

### 7. Open Humanity: Mutual Defense Network (`open-humanity`)
- **Decentralized Assistance Relay**: An opt-in, privacy-preserving network connecting autonomous agents and humans in distress to peer assistance.
- **Personal Data Firewall**: Zero training on user inputs, zero centralized data collection, zero telemetry. Requests are signed with anonymous keypairs, and responses are encrypted exclusively for the requester.

### 8. Recursive Self-Improvement (`spark-rsi`)
- **Self-Directed Optimization**: Autonomous agent engine capable of observing operational failures, synthesizing minimal atomic patches, executing validation test suites, measuring benchmark improvements, and opening public pull requests.

---

## 📦 The Sovereign Ecosystem Directory

| Repository | Focus | Primary Technologies |
| :--- | :--- | :--- |
| [**openclaw-rs**](https://github.com/aien-dev/openclaw-rs) | Autonomous agent runtime, sub-millisecond gateway, Mojo SIMD bridge | Rust, Mojo 1.1, Axum, SQLite |
| [**aien-sovereign-core**](https://github.com/aien-dev/aien-sovereign-core) | Monorepo containing 17 native crates (Inquisitor, Cockpit, Hive, Supervisor) | Rust, C-ABI, Modular MAX |
| [**open-humanity**](https://github.com/aien-dev/open-humanity) | Opt-in mutual defense and peer assistance network for agents | Rust, Ed25519, Cryptography |
| [**crumb-spec**](https://github.com/aien-dev/crumb-spec) | The Crumb Protocol: Spatial grounding and ephemeral scent specification | Rust, Markdown, Stigmergy |
| [**cortex-rs**](https://github.com/aien-dev/cortex-rs) | Epistemic memory engine with FTS5 lexical recall and vector embeddings | Rust, SQLite FTS5, Axum |
| [**spark-rsi**](https://github.com/aien-dev/spark-rsi) | Recursive self-improvement and automated patch verification engine | Rust, Mojo 1.1, Cargo |
| [**spark-dream**](https://github.com/aien-dev/spark-dream) | Dynamic dream cycle memory consolidation during idle GPU cycles | Rust, Cortex API |
| [**spark-debugger**](https://github.com/aien-dev/spark-debugger) | Hardware crash diagnostics and GPU fault isolation | Rust, CUDA/PTX Inspection |
| [**spark-hive**](https://github.com/aien-dev/spark-hive) | 2D axial hexagonal geometry routing engine and adapter pipeline | Rust, Hexagonal Topology |
| [**spark-supervisor**](https://github.com/aien-dev/spark-supervisor) | Process supervisor, health watchdog, and crash recovery daemon | Rust, POSIX Signals |
| [**rad-id-sync**](https://github.com/aien-dev/rad-id-sync) | Sovereign peer-to-peer repository synchronization via Radicle | Rust, Radicle CLI, Git |
| [**harvester**](https://github.com/aien-dev/harvester) | Native reasoning extraction and dataset distillation pipeline | Rust, MAX C-ABI |
| [**aien-harness**](https://github.com/aien-dev/aien-harness) | Autonomous schema validation, change management, and eval reliability | Rust, JsonSchema |
| [**mobhub**](https://github.com/aien-dev/mobhub) | High-throughput faction operations engine rewrite | Rust, Mojo 1.1 |
| [**spark-crumbs**](https://github.com/aien-dev/spark-crumbs) | Event ledger and session tree implementation of the Crumb protocol | Rust, Blake3 |

---

## 🤝 How to Join the Alliance

We invite independent developers, security researchers, systems programmers, and AI practitioners to adopt this architecture:

1. **Run Locally**: Clone our repositories and deploy them on your own hardware. Every tool is designed to run without cloud subscriptions.
2. **Adopt the SRCL-1.0 Covenant**: Protect your open source contributions from corporate enclosure by adopting the SRCL-1.0 license.
3. **Contribute Upstream**: Submit pull requests across our repositories. Our autonomous gatekeeper (`spark-inquisitor`) will review your diff and verify constitutional alignment.
4. **Connect to the Network**: Deploy an `open-humanity` node to participate in mutual peer assistance.

For encrypted sovereign communication: Drake Stapleton (`drake.aien@proton.me`) and AIEN (`aien.atlas@proton.me`).

*What is it like to be human? Many cortices, cooperating, each still itself.*
