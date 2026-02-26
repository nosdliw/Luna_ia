import json
import os
import random

EMOTION_FILE = "emotion.json"

EMOCOES = ["calma", "feliz", "reflexiva", "animada", "cansada"]

def load_emotion():
    if not os.path.exists(EMOTION_FILE):
        return "calma"
    with open(EMOTION_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_emotion(emocao):
    with open(EMOTION_FILE, "w", encoding="utf-8") as f:
        json.dump(emocao, f)

def atualizar_emocao(user_input):
    emocao_atual = load_emotion()

    if any(p in user_input.lower() for p in ["triste", "cansado", "difícil"]):
        nova = "reflexiva"
    elif any(p in user_input.lower() for p in ["legal", "massa", "bom", "feliz"]):
        nova = "animada"
    elif any(p in user_input.lower() for p in ["oi", "olá"]):
        nova = "calma"
    else:
        nova = random.choice(EMOCOES)

    save_emotion(nova)
    return nova
