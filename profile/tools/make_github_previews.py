from pathlib import Path
from PIL import Image,ImageOps
from typing import cast
root=Path(__file__).resolve().parents[2]
source=root/'profile/assets/allen-banner.jpg'
im=Image.open(source).convert('RGB')
out=root/'profile/assets';out.mkdir(exist_ok=True)
# Preserve renderer pixels and aspect ratio; letterbox to GitHub's recommended social-preview canvas.
canvas=Image.new('RGB',(1280,640),(6,8,18))
fit=ImageOps.contain(im,(1280,640),Image.Resampling.LANCZOS)
canvas.paste(fit,((1280-fit.width)//2,(640-fit.height)//2))
canvas.save(out/'aienos-social-preview.png',optimize=True)
# A square crop of the actual renderer's central orb, not invented or generated artwork.
# Measure the central orb's brightest rendered pixel; exclude the lower UI caption.
pixels=im.load()
assert pixels is not None
candidates=[(sum(cast(tuple[int,int,int],pixels[x,y])),x,y) for y in range(80,450) for x in range(im.width//3,2*im.width//3)]
_,cx,cy=max(candidates);side=360
avatar=im.crop((cx-side//2,cy-side//2,cx+side//2,cy+side//2)).resize((1024,1024),Image.Resampling.LANCZOS)
print('measured orb centre',cx,cy,'crop side',side)
avatar.save(out/'allen-avatar.png',optimize=True)
for p in out.glob('*.png'):
 pic=Image.open(p);print(p.name,pic.size,p.stat().st_size);assert p.stat().st_size<1_000_000
