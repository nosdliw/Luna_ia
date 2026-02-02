import pyttsx3

engine = pyttsx3.init()

# Ajustes de voz
engine.setProperty("rate", 165)   # velocidade (150–180 é ideal)
engine.setProperty("volume", 0.9) # volume (0.0 a 1.0)

# Tentar selecionar voz feminina
voices = engine.getProperty("voices")
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break

def falar(texto):
    engine.say(texto)
    engine.runAndWait()
