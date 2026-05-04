from pathlib import Path
import whisper

# 1) Locate your audio file (same one you used before)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
# audio_file = PROJECT_ROOT / "audio" / "frase_principito.wav"
audio_file = PROJECT_ROOT / "audio" / "frase_principito_valentina.ogg"

# 2) Load a small Whisper model
print("Loading Whisper model...")

model_tiny = whisper.load_model("tiny")
model_small = whisper.load_model("small")
model_medium = whisper.load_model("medium")


model = model_medium # or "tiny", "small", ...

# 3) Transcribe the audio, forcing Spanish
print("Transcribing...")
result = model.transcribe(
    str(audio_file),
    language="es",        # force Spanish (ISO code)
    task="transcribe",    # keep it in Spanish (no translation)
)

print("\n--- TRANSCRIPCIÓN ---")
print(result["text"])
