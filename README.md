# See, Hear, and Read: Multimodal AI Made Simple

Workshop demos prepared for the **Women in Tech Conference** held on November 22, 2025 in Medellín, Colombia.

These demos showcase multimodal capabilities using only Python libraries — no cloud APIs required, to demonstrate how much you can do by just calling Python packages.

## What's covered

| Capability | Library | Script |
|---|---|---|
| Text to Speech | `pyttsx3` | `test_text_to_speech.py` |
| Speech Transcription | `openai-whisper` | `test_speech_transcription.py` |
| OCR (image to text) | `pytesseract` + `Pillow` | `test_OCR.py`, `test_OCR2.py` |
| Object Detection | `ultralytics` (YOLOv8) + `opencv` | `test_object_detection.py` |

## Setup

Requires Python 3.13+. Uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
uv sync
```

Or with pip:
```bash
pip install openai-whisper pytesseract pyttsx3 ultralytics opencv-python pillow matplotlib
```

> For OCR, Tesseract must be installed on your system:
> - macOS: `brew install tesseract tesseract-lang`
> - Ubuntu: `sudo apt install tesseract-ocr tesseract-ocr-spa`

## Running the demos

```bash
# Text to speech
uv run python src/wit_talk/test_text_to_speech.py

# Speech transcription
uv run python src/wit_talk/test_speech_transcription.py

# OCR
uv run python src/wit_talk/test_OCR.py

# Object detection
uv run python src/wit_talk/test_object_detection.py
```

## Project structure

```
wit_talk/
├── audio/          # Sample audio files (Spanish phrases)
├── images/         # Sample images for OCR and object detection
├── presentations/  # Quarto/reveal.js slide deck
└── src/wit_talk/   # Demo scripts
```
