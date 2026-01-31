from prompt import SYSTEM_PROMPT
from openai import OpenAI

client = OpenAI()

def generate_response(user_text, mood="neutra"):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Humor atual: {mood}\nMensagem: {user_text}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7,
        max_tokens=120
    )

    return response.choices[0].message.content
