from pathlib import Path
import pyttsx3

# folder: WIT_TALK/audio
PROJECT_ROOT = Path(__file__).resolve().parents[2]   # go up from src/wit_talk
audio_dir = PROJECT_ROOT / "audio"
audio_dir.mkdir(exist_ok=True)

audio_file = audio_dir / "frase_principito.wav"

engine = pyttsx3.init()

# set the Spanish (Mexico) Shelley voice
engine.setProperty("voice", "com.apple.eloquence.es-MX.Shelley")

text = "Es una locura odiar a todas las rosas sólo porque una te pinchó. Renunciar a todos tus sueños sólo porque uno de ellos no se cumplió."
engine.save_to_file(text, str(audio_file))
engine.runAndWait()

print("Saved to:", audio_file)
