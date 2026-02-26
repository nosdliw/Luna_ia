import time
import random
import threading
from brain import generate_response, fala_sozinha
from voice import falar
MODO_LIVE = "study"  # pode ser "study", "chill", "chat"


def loop_fala_sozinha():
    time.sleep(10)  # fala inicial após 10s

    while True:
        intervalo = random.randint(25, 90)  # intervalo variável

        frase = fala_sozinha(MODO_LIVE)
        print(f"\nLUNA: {frase}\nVocê: ", end="")
        falar(frase)

        time.sleep(intervalo)



def main():
    print("LUNA.exe iniciada. Digite algo (Ctrl+C para sair):")

    thread_fala = threading.Thread(target=loop_fala_sozinha, daemon=True)
    thread_fala.start()

    try:
        while True:
            user_input = input("Você: ")
            if user_input.strip():
                resposta = generate_response(user_input)
                print(f"LUNA: {resposta}")
                falar(resposta)
    except KeyboardInterrupt:
        print("\nLUNA.exe finalizada.")

if __name__ == "__main__":
    main()
