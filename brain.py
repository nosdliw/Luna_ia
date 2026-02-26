from openai import OpenAI
import os
import random
from memory import load_memory, add_to_memory
from persona import IDENTIDADE_LUNA
from emotion import load_emotion, atualizar_emocao
from bond import load_bond, update_bond
from live_mode import gerar_fala_autonoma

# Inicializa cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

FALAS_ESPONTANEAS = [
    "essa música ajuda a desacelerar",
    "às vezes é bom só deixar o tempo passar",
    "se alguém estiver estudando, boa concentração",
    "o silêncio também faz parte da conversa",
    "essa live é um bom lugar pra respirar um pouco"
]

def fala_sozinha(modo="study"):
     return gerar_fala_autonoma(modo)


def generate_response(user_input):
    # 🔥 Atualiza emoção com base no que o usuário disse
    emocao = atualizar_emocao(user_input)

    memory = load_memory()

    # 🔥 Injeta emoção no system prompt
    messages = [{
        "role": "system",
        "content": IDENTIDADE_LUNA + f"\n\nEstado emocional atual: {emocao}. Ajuste seu tom de acordo com isso."
    }]

    messages += memory[-10:]
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    resposta = response.choices[0].message.content

    # 🔥 Memória seletiva
    if any(p in user_input.lower() for p in ["meu nome", "eu sou", "eu gosto", "estou estudando", "quero criar"]):
        add_to_memory("user", user_input)
        add_to_memory("assistant", resposta)

    print(f"[EMOÇÃO ATUAL] {emocao}")

    bond_level = update_bond(user_input)

    messages = [{
    "role": "system",
    "content": IDENTIDADE_LUNA +
               f"\n\nEstado emocional atual: {emocao}." +
               f"\nNível de vínculo com Wildson: {bond_level}/100." +
               "\nAjuste sua proximidade com base nisso."
    }]

    print(f"[VÍNCULO] {bond_level}")


    return resposta








