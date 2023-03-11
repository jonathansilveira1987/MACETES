# Maior e Menor valores.

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
print("\nO maior valor foi {} e o menor valor foi {}\n.".format(maior, menor))