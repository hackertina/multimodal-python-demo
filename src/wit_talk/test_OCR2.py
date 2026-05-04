from pathlib import Path
from PIL import Image

# from IPython.display import display
import numpy as np
import pytesseract

PROJECT_ROOT = Path(__file__).resolve().parents[2]
image_path = PROJECT_ROOT / "images" / "text4.png"

# 1) Load and crop
img = Image.open(image_path).convert("RGB")
w, h = img.size
print("Image size:", w, h)

crop_top = int(h * 0.70)
crop = img.crop((0, crop_top, w, h))

# 2) Convert to HSV to isolate yellow
hsv = crop.convert("HSV")
h_chan, s_chan, v_chan = [np.array(c) for c in hsv.split()]

# Rough HSV range for yellow/orange text
# (these values may need a bit of tweaking)
h_low, h_high = 15, 60   # hue range
s_min, v_min = 80, 80    # ignore very desaturated / dark pixels

mask = (
    (h_chan >= h_low) & (h_chan <= h_high) &
    (s_chan >= s_min) & (v_chan >= v_min)
)

# 3) Build a black/white image from the mask
mask_img = Image.fromarray(mask.astype("uint8") * 255)

print("Mask preview:")
mask_img.show()   # or mask_img.show() in a script

# 4) OCR on the mask
config = "--oem 3 --psm 7"  # LSTM engine, single line
text = pytesseract.image_to_string(mask_img, lang="spa", config=config)

print("\n--- TEXTO DETECTADO ---")
print(repr(text))
print("\nLimpio:")
print(text.strip())
