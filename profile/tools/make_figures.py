#!/usr/bin/env python3
"""Draw the org README figures (profile/assets/fig/*.svg) for github.com/aien-dev.

Run from the repository root:   python3 profile/tools/make_figures.py
Check they are current:         python3 profile/tools/make_figures.py --check

Every number on the figures is a published receipt; the receipt link sits in
the README beside each figure. The speed chart's numbers are copied from
aien-sovereign-core-mv branch serve/q36-batch-v2 (commit 9c62690a),
evidence/q36-batch-20261021/README.md. Colours are the aienos.com Turing look.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _svgkit import (BG, CARD, CARD2, LINE, LINE2, INK, INK2, INK3, BLUE, BLUE_SOFT,
                     GREEN, AMBER, VIOLET, ROSE, CYAN, MONO, Svg, card)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "assets", "fig")


# ---- the stack: what runs on top of what ------------------------------------
def fig_stack():
    s = Svg(1200, 700, "The AienOS stack",
            "What runs on top of what: Allen on top, the model server, Omega, "
            "CUDA++, the Aienux kernel, and the machines underneath.")
    s.frame()
    s.kicker(48, 60, "the stack")
    s.text(48, 100, "What runs on top of what", size=30, weight=800, ls=-0.5)
    rows = [
        ("Allen", "the presence on the iMac screen: sky, water, the voice of the house", GREEN,
         "his window is about 3,500 lines of C in the kernel"),
        ("Model server", "the 35B model the machines talk to, on the Spark", BLUE_SOFT,
         "runs with zero CUDA libraries loaded"),
        ("Omega", "my language for verified programs, its checker, the GPU engine", VIOLET,
         "kernels are written, checked and encoded here"),
        ("CUDA++", "the GPU toolchain, runtime, libraries and driver client, MIT", CYAN,
         "machine code straight to the chip: no nvcc, no libcuda"),
        ("Aienux", "my operating system kernel in C: iMac, Pi 5, QEMU gates", AMBER,
         "no Linux under it where it runs on metal"),
        ("The machines", "one DGX Spark, one 2017 iMac, one Raspberry Pi 5, one RTX 5070 PC", INK2,
         "hardware I own, not rented"),
    ]
    y, rh, gap = 150, 72, 14
    s.rect(104, y - 14, 832, rh * 6 + gap * 5 + 28, fill=GREEN, rx=20, op=0.03)
    for i, (name, sub, col, note) in enumerate(rows):
        card(s, 120, y, 800, rh, accent=col)
        s.rect(120, y + 10, 4, rh - 20, fill=col, rx=2)
        s.text(146, y + 30, name, size=21, weight=750, fill=col)
        s.text(146, y + 56, sub, size=14.5, fill=INK)
        for j, l in enumerate(_wrap(note, 33)[:2]):
            s.text(944, y + 32 + j * 19, l, size=12.5, fill=INK2)
        if i < len(rows) - 1:
            s.line(520, y + rh + 2, 520, y + rh + gap - 2, stroke=INK2, sw=1.6, arrow=True)
        y += rh + gap
    return s


# ---- the machines -------------------------------------------------------------
def fig_machines():
    s = Svg(1200, 520, "The machines",
            "Five machines: the Spark that judges and serves, the iMac that "
            "boots Aienux, the Pi 5, QEMU, and the Windows PC that is the target for Rig.")
    s.frame()
    s.kicker(48, 60, "the machines")
    s.text(48, 100, "Five machines, all mine", size=30, weight=800, ls=-0.5)
    ms = [
        ("DGX Spark", "GB10, 128 GB unified memory", "development box and the judge. Serves the 35B model on my own engine. Every chip run happens here.", GREEN, "running my stack now"),
        ("Intel iMac 2017", "iMac18,3, Core i5, AMD GPU", "boots Aienux on bare metal. The whole screen is Allen's window.", BLUE_SOFT, "booting my kernel"),
        ("Raspberry Pi 5", "BCM2712, AArch64", "first real hardware for the AArch64 kernel, and the house server for the readings window.", VIOLET, "two jobs"),
        ("QEMU", "AArch64 and x86_64", "every kernel change runs its gates here first. An emulator qualifies nothing physical.", AMBER, "the gate before metal"),
        ("Windows PC", "RTX 5070, 12 GB", "the target for AIEN Rig, a local AI engine in a 12 GB budget. Nothing of mine has run on the card yet.", INK2, "next"),
    ]
    for i, (name, chip, sub, col, st) in enumerate(ms):
        x = 48 + (i % 3) * 376
        y = 150 + (i // 3) * 190
        card(s, x, y, 352, 168, accent=col)
        s.circle(x + 32, y + 34, 7, fill=col)
        s.text(x + 52, y + 40, name, size=20, weight=750)
        s.text(x + 24, y + 72, chip, size=13, fill=col, mono=True)
        for j, l in enumerate(_wrap(sub, 46)[:4]):
            s.text(x + 24, y + 98 + j * 19, l, size=14, fill=INK2)
        s.text(x + 24, y + 152, st, size=13, fill=INK3, mono=True)
    return s


def _wrap(t, n):
    out, line = [], ""
    for w in t.split():
        if len(line) + len(w) + 1 > n:
            out.append(line); line = w
        else:
            line = (line + " " + w).strip()
    if line:
        out.append(line)
    return out


# ---- the speed chart, from the batch receipt ---------------------------------
SPEED = {  # conversations -> (batched door tok/s, one at a time tok/s)
    1: (21.95, 22.65), 2: (20.75, 17.14), 4: (42.27, 30.84),
    8: (57.10, 32.01), 16: (62.42, 31.12), 32: (65.66, 34.83),
}


def fig_speed():
    s = Svg(1200, 560, "Many conversations at once on the 35B",
            "Total decoded tokens per second against the number of simultaneous "
            "conversations: the batched door against serving one row after another.")
    s.frame()
    s.kicker(48, 60, "speed, with receipts")
    s.text(48, 100, "Many conversations at once on the 35B", size=30, weight=800, ls=-0.5)
    s.lines(48, 132, ["The 35B model on the Spark, one chip, two ways of serving it. Tokens are identical either way: the gate",
                      "checks every batched reply against the same request served alone, and the swap control goes red on purpose."],
            size=15, fill=INK2, gap=21)
    px, py, pw, ph = 120, 200, 700, 280
    ymax = 80.0
    X = lambda n: px + (n - 1) / 31 * pw
    Y = lambda v: py + ph - v / ymax * ph
    s.rect(px, py, pw, ph, fill=CARD, rx=10)
    for e in (20, 40, 60, 80):
        s.line(px, Y(e), px + pw, Y(e), stroke=LINE, sw=1)
        s.text(px - 12, Y(e) + 4, str(e), size=12.5, fill=INK3, anchor="end", mono=True)
    s.text(px - 66, py + ph / 2, "", size=1)
    s.add(f'<text transform="translate({px - 64} {py + ph / 2}) rotate(-90)" font-family="{MONO}" font-size="13" '
          f'fill="{INK2}" text-anchor="middle">tokens per second, all rows</text>')
    s.text(px + pw / 2, py + ph + 40, "conversations at once", size=13.5, fill=INK2, anchor="middle")
    ceil = 63.25
    s.line(px, Y(ceil), px + pw, Y(ceil), stroke=GREEN, sw=1.5, dash="5 5")
    s.text(px + pw - 8, Y(ceil) - 10, "one-conversation ceiling 63.25 tok/s", size=13, fill=GREEN, anchor="end", mono=True)
    xs = sorted(SPEED)
    d1 = " ".join(("M" if i == 0 else "L") + f"{X(n):.1f} {Y(SPEED[n][0]):.1f}" for i, n in enumerate(xs))
    d2 = " ".join(("M" if i == 0 else "L") + f"{X(n):.1f} {Y(SPEED[n][1]):.1f}" for i, n in enumerate(xs))
    s.path(d2, stroke=INK3, sw=2.5, dash="7 5")
    s.path(d1, stroke=CYAN, sw=3.5)
    for n in xs:
        s.circle(X(n), Y(SPEED[n][0]), 6, fill=CYAN, stroke=BG, sw=2)
        s.circle(X(n), Y(SPEED[n][1]), 6, fill=INK3, stroke=BG, sw=2)
        s.text(X(n), py + ph + 22, str(n), size=12.5, fill=INK3, anchor="middle", mono=True)
    lx = 880
    s.line(lx, 214, lx + 40, 214, stroke=CYAN, sw=3.5)
    s.circle(lx + 20, 214, 5, fill=CYAN)
    s.text(lx + 52, 219, "the batched door", size=15, weight=700, fill=CYAN)
    s.lines(lx + 52, 243, ["all rows decoded together,", "weight reads shared"], size=13.5, fill=INK2, gap=19)
    s.line(lx, 324, lx + 40, 324, stroke=INK3, sw=2.5, dash="7 5")
    s.circle(lx + 20, 324, 5, fill=INK3)
    s.text(lx + 52, 329, "one row after another", size=15, weight=700, fill=INK2)
    s.lines(lx + 52, 353, ["the old way: same chip,", "same work, a third of the words"], size=13.5, fill=INK2, gap=19)
    s.lines(lx, 450, ["At 32 conversations the batched door", "reaches 65.7 tok/s, past the 63.25", "one-conversation ceiling: all rows", "share the same weight reads."],
            size=13.5, fill=INK2, gap=20)
    s.text(48, s.h - 20, "Receipt: aien-sovereign-core-mv, branch serve/q36-batch-v2 (9c62690a), "
                         "evidence/q36-batch-20261021/README.md. Numbers measured on the Spark, 2026-10-21.", size=13, fill=INK3)
    return s


# ---- how a change gets in -----------------------------------------------------
def fig_merge():
    s = Svg(1200, 400, "How a change gets in",
            "A branch is judged on my own machine: gates, a signed receipt, and "
            "only then a merge. Nothing merges on a green badge alone.")
    s.frame()
    s.kicker(48, 60, "how a change gets in")
    s.text(48, 100, "How a change gets in", size=30, weight=800, ls=-0.5)
    steps = [
        ("1", "A branch", "one change, its gate manifest", BLUE_SOFT),
        ("2", "The Spark judges", "exact commit, only the gates whose inputs changed", GREEN),
        ("3", "A signed receipt", "verdicts, exit codes, logs, into aien-receipts", GREEN),
        ("4", "The hosted check", "one job: confirm the bundle matches the commit", INK2),
        ("5", "ready-to-merge", "the pipeline merges when both agree", AMBER),
    ]
    W, H, y = 196, 150, 160
    for i, (n, t, sub, col) in enumerate(steps):
        x = 48 + i * (W + 29)
        card(s, x, y, W, H, accent=col)
        s.circle(x + 26, y + 30, 14, fill=col)
        s.text(x + 26, y + 35, n, size=14, weight=800, fill=BG, anchor="middle")
        s.text(x + 18, y + 66, t, size=16, weight=700, fill=col)
        for j, l in enumerate(_wrap(sub, 24)[:3]):
            s.text(x + 18, y + 92 + j * 18, l, size=12.5, fill=INK2)
        if i < len(steps) - 1:
            s.line(x + W + 3, y + H / 2, x + W + 26, y + H / 2, stroke=INK2, sw=1.6, arrow=True)
    s.text(48, 356, "Nothing merges on a green badge alone. The design is ADR 0033 in aien-architecture-mv; the receipts are public in aien-receipts.",
           size=13.5, fill=INK3)
    return s


FIGS = {
    "stack.svg": fig_stack,
    "machines.svg": fig_machines,
    "speed.svg": fig_speed,
    "merge-flow.svg": fig_merge,
}


def main():
    check = "--check" in sys.argv
    os.makedirs(OUT, exist_ok=True)
    stale = []
    for name, fn in FIGS.items():
        data = fn().svg()
        path = os.path.join(OUT, name)
        if check:
            if not os.path.exists(path) or open(path).read() != data:
                stale.append(name)
        else:
            with open(path, "w") as f:
                f.write(data)
            print(f"wrote profile/assets/fig/{name} ({len(data)} bytes)")
    if check:
        if stale:
            sys.exit("stale figures (run python3 profile/tools/make_figures.py): " + ", ".join(stale))
        print(f"figures current: {len(FIGS)}")


if __name__ == "__main__":
    main()
