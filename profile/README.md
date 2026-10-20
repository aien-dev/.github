# AIEN

AIEN runs a 27B language model on an NVIDIA DGX Spark through its own engine, Omega, with no CUDA, no libcuda and no cubin files.
One person, Drake Stapleton, who is an engineer and not a programmer, built it by directing Claude agents, with a judge, a ledger and a receipt behind every number.
You can check it on your own Spark with one command.

```
curl -sSLO https://aienos.com/run && less run && sh run
```

| Measured | Result | Share of the 273 GB/s memory wall |
|---|---|---|
| Every memory path loaded at once | 222.3 GB/s | 0.814 ([MACHINE_CEILING.md](https://github.com/aien-dev/omega-mv/blob/3c8ce239/docs/MACHINE_CEILING.md)) |
| Qwen3.8-27B, 4-bit weights (13.65 GB), chip time per token | 14.29 tokens/s | 0.714 ([NOTES.md](https://github.com/aien-dev/aien-sovereign-core-mv/blob/8e43126a/evidence/qwen38-w4default-20261020T0826Z/NOTES.md)) |
| The one-command demo, clean folder, wall clock | 14.15 tokens/s | 0.708 ([demo receipt](https://github.com/aien-dev/aien-receipts/tree/main/demos/l182-one-command/20261020T184322Z)) |

A token is a word piece, the unit a model writes. Each 4-bit token reads all 13.65 GB of weights once.

```
 your prompt
     |
     v
 qwen38_say ............ host side, Rust (aien-sovereign-core-mv): tokens in, 4-bit weights from a store
     |
     v
 Omega ................. the engine, C (omega-mv): writes the GPU command stream and machine code itself
     |
     v
 nvrm.c ................ driver client, 813 lines of C (physics-mv): 8 nvidia.ko + 11 nvidia-uvm.ko commands
     |
     v
 open nvidia.ko and nvidia-uvm.ko  -->  NVIDIA GSP firmware  -->  GB10 GPU
```

- [The proof, in full](https://www.aienos.com/proof/) (also [PROOF.md](PROOF.md)): what it is, what it is not, how it was built.
- [Omega](https://github.com/aien-dev/omega-mv), the engine. [The Omega Program](https://github.com/aien-dev/omega-mv/blob/4aa7d6ca/docs/PROGRAM.md), the plan.
- [Aienux](https://github.com/aien-dev/aienos-mv), the kernel. [AienOS](https://github.com/aien-dev/aienix), the operating system.
- [Receipts](https://github.com/aien-dev/aien-receipts), signed by the Spark judge.
- [The long version](DETAILS.md) of this page: machines, the tree, research and how a change gets in.
