"""Regenerate A Gift icon PNGs from the cream-on-walnut spec.
Run: python3 icon.py
Tweak BG / FG / FONT_INDEX / SIZES below to customise.
"""
from PIL import Image, ImageDraw, ImageFont

BG = (107, 85, 68)     # walnut #6B5544
FG = (252, 252, 251)   # cream #FCFCFB
FONT_PATH = '/System/Library/Fonts/Supplemental/Songti.ttc'
FONT_INDEX = 6         # Songti SC Regular (try 0=Black, 1=Bold, 3=Light, 6=Regular)
CHAR = '礼'
SIZES = [180, 192, 512]

for size in SIZES:
    img = Image.new('RGB', (size, size), BG)
    draw = ImageDraw.Draw(img)
    fs = int(size * 0.66)
    font = ImageFont.truetype(FONT_PATH, fs, index=FONT_INDEX)
    bbox = draw.textbbox((0, 0), CHAR, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - w) // 2 - bbox[0]
    y = (size - h) // 2 - bbox[1] - int(size * 0.015)
    draw.text((x, y), CHAR, font=font, fill=FG)
    img.save(f'icon-{size}.png', optimize=True)
    print(f'wrote icon-{size}.png  ({size}×{size})')
