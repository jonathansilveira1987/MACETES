


# Listas com pares e ímpares.
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print("-=" * 30)
num[0].sort()
num[1].sort()
print(f"Os valores pares digitados foram: {num[0]}")
print(f"Os valores ímpares digitados foram: {num[1]}")


# Valores únicos em uma Lista.
numeros = list()
while True:
    
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não vou adicionar...")
    
    r = str(input("Deseja continuar [S - Sim / N - Não ]? "))
    if r in "Nn":
        break

print("-=" * 30)
numeros.sort()
print(f"Você digitou os valores {numeros}.")
print("-=" * 30)


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


# Lista ordenada sem repetições.
lista = []

for c in range(0, 5):
    n = int(input("Digite um valor: "))

    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print("Adiconado ao final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Adiconado na posição {pos} da lista.")
                break
            
            pos = pos + 1
            
print("-=" * 30)
print(f"Os valores digitados em ordem foram {lista}")
print("-=" * 30)


# Extraindo dados de uma Lista.
valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Deseja continuar [S/N]? "))
    if resp in "Nn":
        break
print("-=" * 30)
print(f"Você digitou {len(valores)} elementos.")
valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {valores}.")
if 5 in valores:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")


# Dividindo valores em várias listas.
num = list()
pares = list()
impares = list()

while True:
    num.append(int(input("Digite um número: ")))
    resp = str(input("Quer continuar [S/N]? "))
    if resp in "Nn":
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
        
print("-=" * 30)
print(f"A lista compelta é {num}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares {impares}")


# Lista composta e análise de dados.
temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Quer continuar [S/N]? "))
    if resp in "Nn":
        break
print("-=" * 30)
print(f"Ao todo, você cadastrou {len(princ)} pessoas.")
print(f"O maior peso foi de {maior} kilos. Peso de ",end="")
for p in princ:
    if p[1] == maior:
        print(f"[{p[0]}]", end=" ")
print()
print(f"O menor peso foi de {menor} kilos. Peso de ",end="")
for p in princ:
    if p[1] == menor:
        print(f"[{p[0]}]", end="")