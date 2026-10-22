#!/usr/bin/env python3
"""Self-contained wordmarks using actual Allen renderer pixels, no remote fonts."""
import base64
import hashlib
import io
from pathlib import Path
from PIL import Image

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
source = ASSETS / 'allen-avatar.png'
image = Image.open(source).convert('RGB')
# Magnify the central rendered point cloud; no astronomical points are synthesized.
w, h = image.size
side = min(w, h) // 2
left, top = (w - side) // 2, (h - side) // 2
image = image.crop((left, top, left + side, top + side))
image = image.resize((192, 192), Image.Resampling.LANCZOS)
stream = io.BytesIO()
image.save(stream, format='PNG', optimize=True)
encoded = base64.b64encode(stream.getvalue()).decode('ascii')
for theme in ('dark', 'light'):
    dark = theme == 'dark'
    start, end = ('#d2daff', '#96aaff') if dark else ('#344476', '#586bb4')
    subtitle = '#96a0c4' if dark else '#59658b'
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="120" viewBox="0 0 400 120" role="img" aria-label="AienOS: the core tree of AIEN">
  <title>AienOS</title>
  <desc>Allen's actual kernel-rendered orb, with a light-weight blue wordmark. The orb is cropped from the existing renderer-derived avatar; it is not generated artwork.</desc>
  <!-- Reproduce with profile/tools/make_wordmarks.py. Source PNG SHA256 {hashlib.sha256(source.read_bytes()).hexdigest()} -->
  <defs>
    <clipPath id="orb-{theme}"><circle cx="70" cy="60" r="39"/></clipPath>
    <linearGradient id="ink-{theme}" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{start}"/><stop offset="1" stop-color="{end}"/></linearGradient>
    <filter id="glow-{theme}" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="1.1"/></filter>
  </defs>
  <circle cx="70" cy="60" r="43" fill="none" stroke="#96aaff" stroke-opacity=".18" stroke-width=".8"/>
  <image x="31" y="21" width="78" height="78" clip-path="url(#orb-{theme})" href="data:image/png;base64,{encoded}"/>
  <g font-family="'Avenir Next', Avenir, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="64" font-weight="300" letter-spacing="1.2">
    <text x="132" y="76" fill="{end}" opacity=".18" filter="url(#glow-{theme})">AienOS</text>
    <text x="132" y="76" fill="url(#ink-{theme})">AienOS</text>
  </g>
  <text x="136" y="100" font-family="'Avenir Next', Avenir, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="12.5" font-weight="400" letter-spacing="2.5" fill="{subtitle}">THE CORE TREE OF AIEN</text>
</svg>
'''
    target = ASSETS / f'aienos-wordmark-{theme}.svg'
    target.write_text(svg)
    print(target.name, target.stat().st_size)
