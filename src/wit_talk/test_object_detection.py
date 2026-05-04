from pathlib import Path

from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# 1) Paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
image_path = PROJECT_ROOT / "images" / "classroom.jpg"  # <- change name if needed
print("Image:", image_path)
assert image_path.exists(), "Image file not found!"

# 2) Load a small YOLOv8 model (good for CPU demo)
model = YOLO("yolov8n.pt")   # 'n' = nano; can also try 's' (small)

# 3) Run inference
results = model(str(image_path), conf=0.6)[0] # take first (and only) result

# 4) Print detected objects
print("\n--- DETECTIONS ---")
for box in results.boxes:
    cls_id = int(box.cls)
    cls_name = model.names[cls_id]
    conf = float(box.conf)
    print(f"{cls_name:15s} {conf:.2f}")

# 5) Show image with bounding boxes
annotated = results.plot()  # BGR NumPy array

annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8, 6))
plt.imshow(annotated_rgb)
plt.axis("off")
plt.tight_layout()
plt.show()
