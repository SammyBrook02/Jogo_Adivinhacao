import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação de Samuel")
    numero_secreto = random.radiant(1,200)
    tentativas = 0
    acertou = False
   
    print("Estou pensando em um número entre 1 e 200...")

    while not acertou:
        try:
            palpite = int(input("Qual é o seu número: "))
            tentativas += 1

            if palpite < numero_secreto:
                print(" o número  oculto é maior")
            elif palpite > numero_secreto:
                print("o número oculto é menor")
            else:
                print(f"Parabéns, você acertou o número oculto em {tentativas} tentativas")
                acertou = True
        except ValueError:
            print("Informe um número válido")
jogo_adivinhacao()


        


