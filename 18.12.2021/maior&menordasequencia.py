# Maior e menor da sequência.

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