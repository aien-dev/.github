#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Draw the README figures (docs/img/*.svg) from this repository's own data.

Run from the repository root:   python3 tools/figures/make_figures.py
Check they are current:         python3 tools/figures/make_figures.py --check

Nothing here is drawn by an image generator. The machine-code figures read the
instruction words straight out of src/omega_blackwell_encoder.c and decode them
with the field positions my encoder uses (src/omega_blackwell_codegen.c,
"Control words"). The numbers on the other figures are the receipts named on
each figure. Colours are the aienos.com "Turing look" tokens.
"""
import os
import re
import sys
from html import escape

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "assets", "fig")

# ---- Turing look tokens (aienos.com public/assets/turing-look.css) ----------------
BG, CARD, CARD2 = "#08090c", "#0e1219", "#131822"
LINE, LINE2 = "#1c2536", "#2a3648"
INK, INK2, INK3 = "#f1f5f9", "#94a3b8", "#64748b"
BLUE, BLUE_SOFT, GREEN = "#2d7ff9", "#7db4ff", "#00e599"
AMBER, VIOLET, ROSE, CYAN = "#f59e0b", "#a78bfa", "#fb7185", "#22d3ee"

SANS = "Inter, ui-sans-serif, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"


# ---- tiny SVG writer ---------------------------------------------------------------
class Svg:
    def __init__(self, w, h, title, desc):
        self.w, self.h = w, h
        self.parts = []
        self.title, self.desc = title, desc

    def add(self, s):
        self.parts.append(s)

    def rect(self, x, y, w, h, fill="none", stroke="none", rx=0.0, sw=1.0, op=1.0, dash=None, extra=""):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' opacity="{op}"' if op != 1 else ""
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}{o}{extra}/>')

    def text(self, x, y, s, size=16.0, fill=INK, weight=400, anchor="start", mono=False, op=1.0, ls=None, italic=False, strike=False):
        fam = MONO if mono else SANS
        size = max(size, 12.5)  # README width scales figures to about 0.73: keep the smallest text readable
        o = f' opacity="{op}"' if op != 1 else ""
        l = f' letter-spacing="{ls}"' if ls is not None else ""
        it = ' font-style="italic"' if italic else ""
        it += ' text-decoration="line-through"' if strike else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-size="{size}" font-weight="{weight}" '
                 f'fill="{fill}" text-anchor="{anchor}"{o}{l}{it}>{escape(s)}</text>')

    def lines(self, x, y, rows, size=15.0, fill=INK2, gap=None, **kw):
        gap = gap or size * 1.4
        for i, r in enumerate(rows):
            self.text(x, y + i * gap, r, size=size, fill=fill, **kw)

    def line(self, x1, y1, x2, y2, stroke=LINE2, sw=1.5, dash=None, arrow=False, op=1.0):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        a = ' marker-end="url(#arrow)"' if arrow else ""
        o = f' opacity="{op}"' if op != 1 else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" '
                 f'stroke-width="{sw}"{d}{a}{o}/>')

    def path(self, d, stroke=LINE2, sw=1.5, fill="none", arrow=False, dash=None, op=1.0):
        a = ' marker-end="url(#arrow)"' if arrow else ""
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' opacity="{op}"' if op != 1 else ""
        self.add(f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}"{a}{ds}{o}/>')

    def circle(self, x, y, r, fill=INK, stroke="none", sw=1.0):
        self.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def pill(self, x, y, label, color, size=13.0, h=24.0, filled=False, w=None):
        w = w or (len(label) * size * 0.62 + 22)
        if filled:
            self.rect(x, y, w, h, fill=color, rx=h / 2, op=0.16)
            self.rect(x, y, w, h, stroke=color, rx=h / 2, sw=1, op=0.7)
        else:
            self.rect(x, y, w, h, stroke=color, rx=h / 2, sw=1.2)
        self.text(x + w / 2, y + h / 2 + size * 0.36, label, size=size, fill=color, weight=600, anchor="middle",
                  mono=True)
        return w

    def kicker(self, x, y, s, color=BLUE_SOFT):
        self.text(x, y, s.upper(), size=14, fill=color, weight=600, mono=True, ls=1.5)

    def frame(self):
        self.rect(0.5, 0.5, self.w - 1, self.h - 1, fill=BG, stroke=LINE, rx=22)
        self.rect(0.5, 0.5, self.w - 1, self.h - 1, fill="url(#glow)", rx=22)

    def svg(self):
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                f'viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="t d">'
                f'<title id="t">{escape(self.title)}</title><desc id="d">{escape(self.desc)}</desc>'
                '<defs>'
                '<radialGradient id="glow" cx="22%" cy="-10%" r="85%">'
                f'<stop offset="0" stop-color="{BLUE}" stop-opacity="0.16"/>'
                f'<stop offset="0.55" stop-color="{BLUE}" stop-opacity="0.03"/>'
                f'<stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>'
                '<radialGradient id="glow2" cx="92%" cy="8%" r="45%">'
                f'<stop offset="0" stop-color="{GREEN}" stop-opacity="0.08"/>'
                f'<stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></radialGradient>'
                '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
                f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{INK2}"/></marker>'
                '</defs>')
        return head + "".join(self.parts) + "</svg>\n"


def card(s, x, y, w, h, accent=None, fill=CARD, rx=16.0, sw=1.0, dash=None):
    s.rect(x, y, w, h, fill=fill, stroke=accent or LINE2, rx=rx, sw=sw, dash=dash)


