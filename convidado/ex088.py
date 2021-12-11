# Palpites para a Mega Sena.

from random import randint
lista = list()
cont = 0
while True:
    num = randint(1, 60)
    if num in lista:
        lista.append(num)
        cont = cont + 1
    if cont >= 6:
        break
print(f"Os números sorteados foram {lista}")




