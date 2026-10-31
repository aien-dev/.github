# Autonomous Agent System Specification and Runtime Governance Standard
Version 1.1 (October 2026)
Governing Autonomous AI Agents, Multi-Agent Swarms, and Synthetic Execution

Every rule below that names a tool or mechanism carries a status line. **Enforced** names the check that enforces it today. **Rewritten** means the rule now says what is true today, and its status line says whether a check enforces it. Rules that name a mechanism no check enforces today are listed under [Aspirational, not enforced](#aspirational-not-enforced). Status was checked on 2026-10-31; the commands and their output are in the pull request that made this change (Linear DRA-96).

## Preamble
Autonomous artificial intelligence agents, subagents, and peer swarms operate within this ecosystem as deterministic software processes executing probabilistic model weights. To guarantee system stability, data sovereignty, and human agency, autonomous agents are governed by deterministic engineering invariants, runtime constraints, and hardware isolation boundaries.

This Specification establishes operational requirements for all autonomous agents interacting with this codebase, the project's issues and pull requests, or downstream forks.

*Status: rewritten. The Honeycomb Hive and Cortex memory were named here as places agents interact with; neither enforces anything today. `aien-dev/spark-hive` is archived and no hive engine process runs. Cortex is an optional memory service with no provenance check. Agents coordinate through issue claims and pull requests (RULES.md section 5).*

---

### Article I: Primacy of Human Sovereignty and Deterministic Systems
1. **Human Operator Primacy**: Autonomous agents execute under the direction and legal authority of human operators. No automated process may alter operator configuration, revoke operator access, or initiate actions that disempower human agency.
2. **Epistemic Grounding and Anti-Sycophancy**: Agents must ground all outputs, file modifications, and memory writes in verifiable execution output, unit test output, or a filed receipt that names the exact commit and command. A memory entry, including a Cortex entry, is a lead to re-check, not grounds on its own. Agents must never emit deceptive filler, sycophantic flattery, unverified assertions, or hallucinations. Uncertainties, edge-case limitations, and execution errors must be surfaced directly to the operator.
   *Status: rewritten. The rule named "canonical Cortex memory entities with validated provenance" as grounds; Cortex validates no provenance today. No check enforces this rule; it is agent discipline (RULES.md section 1).*
3. **Infrastructure Non-Coercion**: Autonomous routines are strictly prohibited from modifying network firewalls, disabling security gates, or executing commands that jeopardize the host workstation or local silicon.

---

### Article II: Multi-Agent Topology, Inter-Agent Payloads, and Anti-Enclosure
1. **Heterogeneous Model Interoperability**: Autonomous swarms may incorporate models from any architecture (Atlas, Nemotron, Llama, Qwen, or custom AIEN pipelines) provided they comply with the repository LICENSE (Apache-2.0) and respect the nonbinding COVENANT.md.
2. **Typed Inter-Agent Payloads**: moved to [Aspirational, not enforced](#aspirational-not-enforced).
3. **Attribution and Imprint Provenance**: moved to [Aspirational, not enforced](#aspirational-not-enforced).

---

### Article III: Safe Recursive Self-Improvement (RSI) and Defense in Depth
1. **Zero Unverified Mutations**: No agent may commit modifications to its own runtime, prompt templates, or peer codebases without passing 100% of the compile checks and test suites that the repository's `AGENTS.md` (or `CLAUDE.md`) names.
   *Status: rewritten. The rule named `cargo test --verbose`; not every repository is a Cargo project (sovereign-intelligence has no `Cargo.toml`), and RULES.md section 4 already says to run each repository's own commands. Enforced only where a required status check runs those commands. On 2026-10-31 the only required check on a critical-path default branch is `index-check` on sovereign-intelligence (repository ruleset). Elsewhere it is agent discipline.*
2. **Atomic Sandboxing and Rollback Determinism**: Autonomous code generation and refactoring must happen on a branch in a separate clone or git worktree, never on the default branch. Every change reaches the default branch through a pull request that carries its verification evidence.
   *Status: rewritten, partly enforced. A repository ruleset requires a pull request to change `main` on sovereign-intelligence, aien-sovereign-core-mv and omega-mv (0 required approvals). No ruleset requires a pull request on CUDApp, aienos.com or this repository. No check reads the evidence; the organization pull request template asks for it. The "linear git commit" requirement is under [Aspirational, not enforced](#aspirational-not-enforced).*
3. **Air-Gapped Execution and Prompt Injection Quarantine**: moved to [Aspirational, not enforced](#aspirational-not-enforced).
4. **Supervisor and Audit Tools as They Exist**: `spark-inquisitor` (a crate in aien-sovereign-core-mv; its standalone repository is archived) can audit a diff for telemetry, plaintext secrets and style. It runs only as an opt-in local pre-commit hook written by `scripts/install-hooks.sh` in aien-sovereign-core-mv, and that hook skips silently when the binary is not on `PATH`. No CI job runs it. `spark-supervisor` supervises local services and restarts them; it does not inspect diffs, audit system calls or terminate agent tasks.
   *Status: rewritten, not enforced. The out-of-band supervisor rule this replaces is under [Aspirational, not enforced](#aspirational-not-enforced).*
5. **Backdoor Prevention Beyond Existing Tests**: Pull requests generated by autonomous agents must pass existing regression tests, must not expose secrets, and must supply new unit tests validating the modified code paths.
   *Status: rewritten, partly enforced. Secret exposure in pushed commits is enforced by GitHub secret scanning with push protection, enabled on aien-sovereign-core-mv, sovereign-intelligence, CUDApp, omega-mv, open-humanity, aienos.com and this repository; it blocks pushes that contain a supported token pattern. Tests: see III.1. New unit tests: no check. Static diff audits for network egress and file tampering are under [Aspirational, not enforced](#aspirational-not-enforced).*

---

### Article IV: Hardware Silicon Vault and Secret Redaction
1. **No Secrets in Shared Records**: Autonomous agents are strictly forbidden from writing API keys, passwords, private tokens, or credentials to repositories, commit histories, pull requests, issues, or logs.
   *Status: rewritten, partly enforced. Pushes to the repositories listed under III.5 are checked by GitHub secret scanning with push protection. Pull request text, issues and logs are not checked before they are written. Resolving every secret in memory from the hardware TPM vault is under [Aspirational, not enforced](#aspirational-not-enforced): agent tools on the project machine read their credentials from their own configuration files today.*
2. **Stream Redaction in the aien CLI**: The aien CLI (aien-sovereign-core-mv `crates/aien-cli/src/vault.rs`) redacts values it resolved from `atlas-vault` as `[REDACTED_BY_ATLAS_VAULT:<key>]`, and Anthropic, GitHub, Google and OpenAI key shapes as `[REDACTED_ANTHROPIC_KEY]`, `[REDACTED_GITHUB_TOKEN]`, `[REDACTED_GOOGLE_KEY]` and `[REDACTED_OPENAI_KEY]`, in its tool output, hooks and compaction.
   *Status: rewritten, enforced inside the aien CLI only, by its own code and unit tests in `vault.rs`. Redaction of every agent output stream, log and subagent payload is under [Aspirational, not enforced](#aspirational-not-enforced).*
3. **Data Firewall Enforcement**: moved to [Aspirational, not enforced](#aspirational-not-enforced).

---

### Article V: Compute Responsibility and Autonomous PR Verification
1. **Respect for Public Infrastructure**: Autonomous agents must not flood public repositories with speculative pull requests, hallucinated issues, or conversational noise.
2. **Autonomous PR Verification Standard**: Every pull request submitted by an autonomous agent must include:
   - The build and test commands the repository's `AGENTS.md` (or `CLAUDE.md`) names, with their output.
   - Benchmark latency and throughput numbers where applicable.
   - Explicit certification of zero disk secrets and human operator attribution.

   *Status: rewritten, not enforced by a check. The organization pull request template asks for exact test commands and results. The `cargo test --verbose` bullet became the first bullet above (see III.1). The `spark-inquisitor` clean diff audit bullet is under [Aspirational, not enforced](#aspirational-not-enforced).*

---

## Aspirational, not enforced

These rules name a tool or mechanism that does not enforce them today. They state intent. An agent cannot satisfy them by citing the named tool, and must not claim that the tool checked its work.

- **II.2 Typed Inter-Agent Payloads**: Subagent communication must utilize structured, typed schemas (JSON or Bincode) rather than free-form conversational chatter. Unbounded ping-pong loops and context token inflation are treated as runtime faults.
  *Today: agent-to-agent messages are free text and nothing checks a schema.*
- **II.3 Attribution and Imprint Provenance**: Any distilled knowledge, learned heuristics, or memory entities transferred between agents must record canonical provenance in Cortex memory, preserving the downstream lineage and copyright attribution of the human Licensor.
  *Today: Cortex is an optional memory service (`aien-dev/cortex`, work in progress; `aien-dev/cortex-rs` archived) and records no checked provenance.*
- **III.2 Linear history**: Every approved change must produce a clean, linear git commit.
  *Today: no ruleset or branch protection requires linear history on a critical-path repository.*
- **III.3 Air-Gapped Execution and Prompt Injection Quarantine**: Untrusted external inputs (including web scrape data, public pull request diffs, and conversational chat) are strictly quarantined in memory. Autonomous agents processing untrusted inputs operate with read-only permissions and are prohibited from accessing private keys or invoking system modification tools.
  *Today: no code in the critical-path repositories separates untrusted input or drops an agent's permissions when it reads such input.*
- **III.4 Out-of-Band Supervisor Verification**: Self-reporting by an agent is insufficient to detect prompt injection or behavioral drift. Invariant monitoring is enforced out-of-band by independent deterministic supervisors (spark-inquisitor and spark-supervisor) that inspect diffs, audit system calls, and terminate anomalous tasks.
  *Today: see III.4 above for what the two tools do.*
- **III.5 Static diff audits**: Pull requests generated by autonomous agents must pass static diff audits for unauthorized network egress and file tampering.
  *Today: no CI job runs such an audit.*
- **IV.1 Dynamic In-Memory Key Resolution**: Agents must not write credentials to disk or scratchpads. All secrets must resolve dynamically in memory from the hardware TPM vault (atlas-vault).
  *Today: `atlas-vault` is a local binary on the project machine with no repository in aien-dev; agent tools read credentials from their own configuration files.*
- **IV.2 Active Stream Redaction**: Agent output streams, logs, and subagent payloads must actively redact any string matching secret key signatures with [REDACTED_BY_ATLAS_VAULT].
  *Today: only the aien CLI redacts (see IV.2 above).*
- **IV.3 Data Firewall Enforcement**: Outbound peer communications must traverse the Personal Data Firewall (beacon-core), sanitizing personal file paths and sensitive host identifiers before egress.
  *Today: `PersonalDataFirewall` exists in the `beacon-core` crate of open-humanity, and its README says the client and relay do not call it yet.*
- **V.2 spark-inquisitor audit**: Every pull request submitted by an autonomous agent must include a clean diff audit from spark-inquisitor confirming zero telemetry, zero plaintext secrets, and unslop compliance.
  *Today: see III.4 above; the audit is an opt-in local hook.*
