import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação de Samuel")
    print("Estou pensando em um número entre 1 e 150.")

    numero_secreto = random.randint(1, 150)
    tentativas = 0

    while True:
        palpite = input("Digite seu palpite (ou 'sair' para encerrar o jogo): ")

        if palpite.lower() == 'sair':
            print("Obrigado por jogar! Até a próxima.")
            break

        try:
            palpite = int(palpite)
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break
if __name__ == "__main__":
    jogo_adivinhacao()

