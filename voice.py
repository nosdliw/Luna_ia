import os
import threading
import tempfile
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
import pygame

from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

print("API KEY:", os.getenv("ELEVEN_API_KEY"))

client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

pygame.mixer.init()
voice_lock = threading.Lock()

def falar(texto):
    with voice_lock:
        try:
            audio_generator = client.text_to_speech.convert(
                 voice_id="21m00Tcm4TlvDq8ikWAM",
                 model_id="eleven_multilingual_v2",
                 text=texto,
                 voice_settings={
                     "stability": 0.25,
                     "similarity_boost": 0.85,
                     "style": 0.85,
                     "use_speaker_boost": True
                     }
            )    

            # juntar todos os chunks em bytes
            audio_bytes = b"".join(audio_generator)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
                f.write(audio_bytes)
                temp_path = f.name

            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                continue

        except Exception as e:
            print(f"[ERRO VOZ] {e}")
