# GAME: Pedra Papel e Tesoura.

from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print('''Sua opção:
[ 0 ] - PEDRA.
[ 1 ] - PAPEL.
[ 2 ] - TESOURA.''')
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!!!!")
print("-=" * 15)
print("Computador jogou: {}.".format(itens[computador]))
print("Jogador jogou: {}.".format(itens[computador]))
# print("O computador escolheu: {}".format(itens[computador]))
print("-=" * 15)
# Computador jogou PEDRA.
if computador == 0:
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCE!")
    elif jogador == 2:
        print("COMPUTADOR VENCE!")
    else:
        print("JOGADA INVÁLIDA!")
# Computador jogou PAPEL
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("JOGADOR VENCE!")
    else:
        print("JOGADA INVÁLIDA!")
# Computador jogou TESOURA
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE!")    
    elif jogador == 1:
        print("COMPUADOR VENCE!")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("JOGADA INVÁLIDA!")