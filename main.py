import os
from dotenv import load_dotenv
from brain import generate_response, fala_sozinha
from voice import falar

# ==============================
# CONFIGURAÇÃO INICIAL
# ==============================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

if not OPENAI_API_KEY:
    print("❌ OPENAI_API_KEY não encontrada.")
    exit()

if not ELEVEN_API_KEY:
    print("❌ ELEVEN_API_KEY não encontrada.")
    exit()

print("LUNA.exe iniciada. Digite algo (Ctrl+C para sair):")

# ==============================
# LOOP PRINCIPAL
# ==============================

while True:
    try:
        user_input = input("Você: ")

        if user_input.lower() in ["sair", "exit", "quit"]:
            print("LUNA.exe finalizada.")
            break

        resposta = generate_response(user_input)

        print(f"LUNA: {resposta}")

        try:
            falar(resposta)
        except Exception as e:
            print(f"[ERRO VOZ] {e}")

    except KeyboardInterrupt:
        print("\nLUNA.exe finalizada.")
        break
