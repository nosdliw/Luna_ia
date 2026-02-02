# from openai import OpenAI
# from persona import LUNA_PERSONA

# client = OpenAI()

# def generate_response(user_input):
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": LUNA_PERSONA},
#             {"role": "user", "content": user_input}
#         ],
#         temperature=0.6,
#         max_tokens=100
#     )

#     return response.choices[0].message.content.strip()

import random
import time

FALAS_ESPONTANEAS = [
    "essa música ajuda a desacelerar",
    "às vezes é bom só deixar o tempo passar",
    "se alguém estiver estudando, boa concentração",
    "o silêncio também faz parte da conversa",
    "essa live é um bom lugar pra respirar um pouco"
]

def fala_sozinha():
    return random.choice(FALAS_ESPONTANEAS)


def generate_response(user_input):
    texto = user_input.lower()

    if any(p in texto for p in ["oi", "olá", "ola", "eai", "e aí"]):
        return random.choice([
            "oi 😊 seja bem-vindo",
            "olá, que bom te ver por aqui",
            "e aí, fica à vontade"
        ])

    if "tudo bem" in texto:
        return random.choice([
            "tudo tranquilo por aqui",
            "indo bem, e você?",
            "tudo certo 😊"
        ])

    return random.choice([
        "fica à vontade por aqui",
        "essa live é bem tranquila"
    ])

