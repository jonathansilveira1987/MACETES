# Jogo da Adivinhação.

from random import randint
from time import sleep

computador = randint(0, 10)

print("\nSou seu computador... Acabei de pensar em um número entre 0 e 10.")
sleep(3)
print("Será que você consegue adivinhar qual foi? ")
sleep(3)

acertou = False
palpites = 0

while not acertou:
    jogador = int(input("\nQual é o seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("\nMais... Tente mais uma vez.")
        elif jogador > computador:
            print("\nMenos... Tente mais uma vez.")
print("\n\033[0;32mAcertou com {} tentativas. Parabéns!\033[m\n".format(palpites))