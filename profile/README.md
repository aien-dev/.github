<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/aienix-wordmark-dark.svg">
  <img src="assets/aienix-wordmark-light.svg" width="560" alt="Aienix: the core tree of AIEN">
</picture>

**Persistent machine intelligence on a machine you own, built in the open.**

### Start here: [aien-dev/aienix](https://github.com/aien-dev/aienix)

</div>

---

AIEN is a sovereign computing stack: an operating system, a language with its own GPU engine, a host runtime and a verification pipeline, written to run as close to the hardware as the hardware allows, with nothing in the trusted base depending on an outside service. It is led by one engineer, Drake Stapleton, working with AI agents as day-to-day collaborators: the agents write, test and review; the engineer decides.

**[Aienix](https://github.com/aien-dev/aienix) is the front door.** Every component is linked into it at a pinned commit, so one clone fetches the whole system at versions that belong together:

```bash
git clone --recurse-submodules --shallow-submodules https://github.com/aien-dev/aienix.git
```

Its front page explains each part, what state it is really in, how a change gets in, and the roadmap. Each component's own README says the same for that part.

**Latest (2026-10-18):** Allen, the resident agent AIENOS is built around, runs full screen on a desktop test computer under the AIENOS kernel, answers from its own local rules with no model and no network, and keeps its memory on that machine's disk. Everything is pre-alpha; what is shown on real hardware and what only in the emulator is spelled out on the [Aienix page](https://github.com/aien-dev/aienix#status).

| Core | Attachments |
| :-- | :-- |
| [AIENOS](https://github.com/aien-dev/aienos): operating system | [synapse](https://github.com/aien-dev/synapse): changeset service, coordination board |
| [Omega](https://github.com/aien-dev/omega): language, semantic substrate, GPU engine | [benchmarks](https://github.com/aien-dev/benchmarks): reproducible measurements |
| [Sovereign core](https://github.com/aien-dev/aien-sovereign-core): host runtime, verification pipeline | [interplane](https://github.com/aien-dev/interplane): model and runtime interoperability |
| [Architecture](https://github.com/aien-dev/aien-architecture): decision records, execution plan | [aegis-runtime](https://github.com/aien-dev/aegis-runtime): agent runtime |
| [Protocols](https://github.com/aien-dev/aien-protocols): specifications and schemas | [spark-rsi](https://github.com/aien-dev/spark-rsi): self-improvement engine |
| [Physics](https://github.com/aien-dev/physics): FORGE realization, boot artefacts | [open-humanity](https://github.com/aien-dev/open-humanity): opt-in assistance network |

Everything is public and licensed AGPL-3.0-or-later. Website: [aienos.com](https://www.aienos.com). Contact: aien@aienos.com.

<sub>Aienix is not a UNIX and makes no such claim. UNIX is a registered trademark of The Open Group. NVIDIA, DGX and Grace Blackwell are trademarks of NVIDIA Corporation.</sub>
