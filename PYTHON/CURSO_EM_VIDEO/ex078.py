# Maior e Menor valores na Lista.

listanum = [1]
maior = menor = 1

for c in range(1, 6):
    listanum.append(int(input(f"Digite um valor para a Posição {c}: ")))
    if c == 1:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print("=-" * 30)
print(f"Você digitou os valores {listanum}")
print("=-" * 30)
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for i, v in enumerate(listanum):
    if v == maior:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi {menor} nas posições ", end="")
for i, v in enumerate(listanum):
    if v == menor:
        print(f"{i}...", end="")
print()