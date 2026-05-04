from pathlib import Path
from PIL import Image, ImageOps
# from IPython.display import display
import pytesseract

PROJECT_ROOT = Path(__file__).resolve().parents[2]
image_path = PROJECT_ROOT / "images" / "text3.png"

img = Image.open(image_path)
w, h = img.size
print("Image size:", w, h)

# 1) Crop the band with text
crop_top = int(h * 0.70)
text_region = img.crop((0, crop_top, w, h))

# 2) Preprocess: grayscale -> contrast -> upscale -> hard threshold
gray = text_region.convert("L")
gray = ImageOps.autocontrast(gray)

# upscale to make letters “fatter”
scale = 3
big = gray.resize((gray.width * scale, gray.height * scale), Image.LANCZOS)

# hard threshold to get clean white text on black background
th = big.point(lambda x: 0 if x < 200 else 255, mode="1")

# 👀 see what Tesseract sees
th.show()   # or th.show() in a script

# 3) OCR
config = "--oem 3 --psm 7"
text = pytesseract.image_to_string(th, lang="spa", config=config)

print("\n--- TEXTO DETECTADO ---")
print(repr(text))
print("\nLimpio:")
print(text.strip())
