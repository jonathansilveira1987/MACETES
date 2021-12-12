# Jogo do Par ou Ímpar.

from random import randint

v = 0

while True:
    jogador = int(input("Informe um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar [P para PAR / I para ÍMPAR]? ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total}.")
    if tipo == "P":
        if total % 2 == 0:
            print("VOCÊ VENCEU!")
            v = v + 1
        else:
            print("VOCÊ PERDEU!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("VOCÊ VENCEU!")
            v = v + 1
        else:
            print("VOCÊ PERDEU!")
            break
        print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {v} vezes.")