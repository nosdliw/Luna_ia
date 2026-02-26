from openai import OpenAI
import os
import tempfile
import pygame
import threading

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
voice_lock = threading.Lock()

pygame.mixer.init()

def falar(texto):
    with voice_lock:
        try:
            response = client.audio.speech.create(
                model="gpt-4o-mini-tts",
                voice="nova",  # voz feminina natural
                input=texto
            )

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
                f.write(response.read())
                temp_path = f.name

            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                continue

        except Exception as e:
            print(f"[ERRO VOZ] {e}")
