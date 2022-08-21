num = [[]]
valor = 0
quantidade = int(input('\nInforme a quantidade de números da lista: '))
print()
for c in range(1, quantidade+1):
    valor = int(input(f"{c}º valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'\n{num}\n')