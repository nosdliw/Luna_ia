from brain import generate_response

print("LUNA.exe iniciada. Digite algo:")

while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit"]:
        break

    resposta = generate_response(user_input)
    print("LUNA.exe:", resposta)
