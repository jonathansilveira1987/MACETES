num = int(input('\nInforme o número de dados para a lista: '))
print()
lista = [input("Dado: ") for i in range(num)]
print(f'\n\033[0;32m{lista}\033[m\n')