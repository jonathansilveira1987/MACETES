lista = [[]]
n = 0
quantidade = int(input('\nInforme a quantidade de números da lista: '))
print()
for c in range(1, quantidade+1):
    n = int(input(f'{c}º valor: '))
    lista[0].append(n)
print(f'\n\033[0;32m{lista[0]}\033[m\n')