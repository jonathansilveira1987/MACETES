# Maior e Menor valor v1.0.
# Programa principal.
a = int(input("\n1º valor: "))
b = int(input("2º valor: "))
c = int(input("3º valor: "))
# Verificando quem é o menor.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando que é o maior.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("\nO menor valor digitado foi \033[0;32m{}\033[m.".format(menor))
print("\nO maior valor digitado foi \033[0;33m{}\033[m.\n".format(maior))


# Maior e Menor valor v2.0.
resp = "S"
soma = quant = media = maior = menor = 0
while resp in "Ss":
    num = int(input("Digite um número: "))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / quant
print("\nVocê digitou {} números e a média foi {}.".format(quant, media))
print("\nO maior valor foi {} e o menor valor foi {}.\n".format(maior, menor))


# Maior e Menor valor em Tupla v3.0.
from random import randint
numeros = (randint(1, 10), randint(1, 10), 
    randint(1, 10), randint(1, 10), randint(1, 10))
print(f"\nOs valores sorteados foram: ", end="")
for n in numeros:
    print(f"{n} ", end="")
print(f"\nO maior valor sorteado foi {max(numeros)}.")
print(f"O menor valor sorteado foi {min(numeros)}.\n")


# Maior e menor valor da sequência v4.0.
maior = 0
menor = 0
for pessoas in range(1, 5):
    peso = float(input("Peso da {}ª pessoa: ".format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else: # Teste de possibilidades.
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("\nO maior peso lido foi {} kg.".format(maior))
print("O menor peso lido foi {} kg.\n".format(menor))