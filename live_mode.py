import random
from emotion import load_emotion
from bond import load_bond

TEMAS = {
    "study": [
        "se você está estudando agora, continua… você está indo bem",
        "cada minuto focado conta mais do que parece",
        "respira fundo e volta para o que importa"
    ],
    "chill": [
        "às vezes desacelerar é a melhor decisão",
        "essa vibe é boa para organizar os pensamentos",
        "não precisa ter pressa agora"
    ],
    "chat": [
        "o chat anda quieto hoje...",
        "alguém aí ainda acordado?",
        "essa live tem uma energia diferente"
    ]
}

def gerar_fala_autonoma(modo="study"):
    emocao = load_emotion()
    vinculo = load_bond()

    base = random.choice(TEMAS.get(modo, TEMAS["study"]))

    # influência emocional
    if emocao == "animada":
        base += " 🔥"
    elif emocao == "reflexiva":
        base = "pensando aqui... " + base
    elif emocao == "cansada":
        base = "hm... " + base

    # influência de vínculo
    if vinculo > 60:
        base += " Wildson."

    return base
