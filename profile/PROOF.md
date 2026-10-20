# A 27B language model on a DGX Spark, with no CUDA

One person, Drake Stapleton, and Claude built an engine called Omega that runs Qwen3.8-27B on an NVIDIA DGX Spark
(the GB10 chip) without CUDA. No CUDA toolkit, no libcuda, no cubin files. Omega writes its own GPU programs and hands
them to the open NVIDIA kernel driver through a short list of system calls. You can run it yourself with one command,
and every number on this page links to the file it came from.

## Run it yourself

On a DGX Spark with the stock DGX OS:

```
curl -sSLO https://aienos.com/run
less run          # read it first: it is one plain shell script
sh run
```

Or from GitHub: `git clone https://github.com/aien-dev/aienos.com && sh aienos.com/public/run`.

What it does, in order: checks the machine, installs Rust inside its own folder if you have none, fetches three source
repositories at pinned commits, builds Omega and the demo, downloads the official Qwen3.8-27B-FP8 weights at a pinned
revision and checks the sha256 of every file, converts them once to 4 bits, answers one prompt and prints the speed.
Everything stays in one folder (`./aien-demo`, 43 GB when our run finished; the note inside the script says about 65 GB and it asks for 70 GB free). No sudo, no system packages.

Our clean run, on a Spark that was busy with other work, printed this at the end:

```
--- numbers (this run, this machine)
model load              26.6 s (13.65 GB of 4-bit weights onto the GPU)
prompt                  28 tokens read in 2.0 s
generation              83 tokens in 5.86 s = 14.15 tokens/s (wall clock)
weight bytes per token  13.65 GB -> 193.2 GB/s = 70.8% of the 273 GB/s memory wall
chip time per token     70.33 ms median = 14.22 tokens/s while the GPU works
```

From an empty folder to the GPU step took 12.9 minutes (calc:e412ee1c): Rust 9.6 s, sources 11.5 s, build 138.3 s,
weights 299.6 s, convert 315.8 s. A token is a word piece, the unit a model writes. The full output, the answer and
the timings are in the [demo receipt][demo], so you can compare your run with ours. Timed again on its own, while another job
was sharing the GPU, the GPU step took 107.3 s end to end and wrote exactly the same 83 tokens; setup plus that step
is 14.7 minutes (calc:3cb838d3).

## The numbers, and what each one measures

Each line is a different measurement. They are listed from the most narrow to the most complete, so the gap between
them is visible.

| What was measured | Result | Share of the 273 GB/s memory wall | Receipt |
|---|---|---|---|
| GPU reading memory, best single path | 245.1 GB/s | 0.898 | [MACHINE_CEILING.md][ceiling] |
| Every memory path loaded at once (GPU, CPU, disk) | 222.3 GB/s (calc:e2b9a9f6) | 0.814 (calc:a3c62418) | [MACHINE_CEILING.md][ceiling] |
| Whole 27B model, 8-bit weights (25.65 GB read per token), chip time per token | 8.50 tokens/s (calc:69c20e5a) | 0.799 (calc:cf5b6ca5) | [NOTES.md][w4notes] |
| Whole 27B model, 4-bit weights (13.65 GB on the chip), chip time per token | 14.29 tokens/s (calc:f0c1b118) | 0.714 (calc:babb1a77) | [4-bit evidence][w4] |
| Same, wall clock, free running | 12.39 tokens/s (calc:2e64d8f1) | 0.619 (calc:4148346f) | [4-bit evidence][w4] |
| This demo on a clean folder (the run above) | 14.15 tokens/s (calc:62fd33ec) | 0.708 (calc:8fe79f5c) | [demo receipt][demo] |

How to read it: writing one token means reading every weight of the model once, so tokens per second times bytes per
token is the memory traffic, and 273 GB/s (NVIDIA's figure for the Spark) is the ceiling. Chip time counts only the time
the GPU is working; wall clock also counts the host's time between tokens.

## What it is not

- It is one model (Qwen3.8-27B), one prompt at a time, greedy decoding (always the most likely next token). No batching, no server in this demo.
- The prompt is read one token at a time through the same path as writing. Short prompts are quick; a 2,047-token prompt
  takes about 148 s ([README][w4readme]). A faster prompt path is the next piece of work.
- 4 bits loses some accuracy against 8 bits. The 4-bit check passed every line of marks frozen before the run
  ([w4-fit-gate.json][gate]); the same next token as 8 bits on 0.938 of positions pooled over five scored texts (limit 0.87, [NOTES.md][w4notes]).
- Tested only on driver 580.173.02. The driver interface is pinned to that version; the script stops on any other.
- The GPU's own firmware (GSP, from NVIDIA, loaded by nvidia.ko) still runs. What is gone is the user-space CUDA stack.
- Omega and the host side are on public branches in review; the driver file is already on `main`. The commits are pinned and
  tagged `demo-l182-v1`, so they will not move.

## How Omega talks to the GPU

The whole driver client is one C file of 813 lines ([nvrm.c][nvrm]). It opens `/dev/nvidiactl` and `/dev/nvidia-uvm`
and uses 8 commands of the nvidia.ko kernel module (card info, register, allocate, control, free, map memory, map and
unmap GPU memory) and 11 of nvidia-uvm.ko (set up the shared address space, register the GPU and its channel, map
memory). Omega writes the GPU's command stream and machine code itself, in C. The instruction encodings were worked out
by comparing against output of NVIDIA's compiler, which is kept only as a reference inside tests; it never runs in the build. The script prints the demo program's linked libraries so you can check there is no libcuda.

## How it was built

Drake is an engineer, not a programmer. He directed Claude agents (Opus, Sonnet, Fable) and, for hard bugs, GPT-6
Astra, from one chat on the Spark itself. The rules that made that work:

- **A seed.** The chain starts from [Atlas][atlas], a 1,480-byte hand-written AArch64 binary that checks the next
  boot stage against a pinned SHA-256 digest. (This demo runs on Linux and does not boot through Atlas.)
- **A judge.** A change only lands after the Spark judge runs the tests on the real chip and signs the result. Signed
  bundles are published in [aien-receipts][receipts].
- **A ledger.** Every job is a line with an owner and a "done when". Agents write what they did beside it.
- **One PR desk.** One agent alone opens and merges pull requests, in order, after the judge passes them.
- **No guessed numbers.** A figure is published only if it points to a measurement, and arithmetic goes through a
  calculator that returns a receipt id. The calculator ledger is internal; the inputs are in the linked files.

The plan that ties it together is [the Omega Program][program].

## Check it

- Source: [omega-mv][omega] (engine), [physics-mv][physics] (driver interface), [aien-sovereign-core-mv][sc] (host side).
- Receipts: [aien-receipts][receipts], including the [receipt of the demo run above][demo].

[ceiling]: https://github.com/aien-dev/omega-mv/blob/3c8ce239/docs/MACHINE_CEILING.md
[w4]: https://github.com/aien-dev/aien-sovereign-core-mv/tree/8e43126a/evidence/qwen38-w4default-20261020T0826Z
[w4readme]: https://github.com/aien-dev/aien-sovereign-core-mv/blob/8e43126a/docs/inference/qwen38/README.md
[gate]: https://github.com/aien-dev/aien-sovereign-core-mv/blob/8e43126a/docs/inference/qwen38/w4-fit-gate.json
[nvrm]: https://github.com/aien-dev/physics-mv/blob/6d7cf0d4/nvrm/nvrm.c
[atlas]: https://github.com/aien-dev/atlas
[receipts]: https://github.com/aien-dev/aien-receipts
[program]: https://github.com/aien-dev/omega-mv/blob/4aa7d6ca/docs/PROGRAM.md
[omega]: https://github.com/aien-dev/omega-mv
[physics]: https://github.com/aien-dev/physics-mv
[sc]: https://github.com/aien-dev/aien-sovereign-core-mv
[demo]: https://github.com/aien-dev/aien-receipts/tree/main/demos/l182-one-command/20261020T184322Z
[w4notes]: https://github.com/aien-dev/aien-sovereign-core-mv/blob/8e43126a/evidence/qwen38-w4default-20261020T0826Z/NOTES.md
