# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a 
# quantidade de números pares e a quantidade de números impares.
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

import math
numero = [[], []]
valor = 10
for c in range(1, 11):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 ==0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)

numero[0].sort()
numero[1].sort()
print(f"Os valores digitados são: {numero}")
print(f"Os valores pares digitados são: {numero[0]}")
print(f"Os valores ímpares digitados são: {numero[1]}")