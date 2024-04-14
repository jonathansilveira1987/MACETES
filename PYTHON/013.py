lista = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'\nLista atual: {lista}')
remover = int(input('Qual elemento da lista acima você deseja remover? '))
elemento_removido = lista.remove(remover)
print(f'\nElemento removido: {remover}')
print(f'\nLista atualizada: {lista}')

elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
lista = [input("Dado: ") for i in range(elemento)]
numeros = lista
print()
print(f'\n{numeros}')
remover = input('Qual elemento da lista acima você deseja remover? ')
elemento_removido = numeros.remove(remover)
print(f'\nElemento removido: {remover}')
print(f'\nLista atualizada: {numeros}')

a = int(input('\nValor 1: '))
b = int(input('Valor 2: '))
print()
for numero in range(a, b):
    if numero == 3:
        continue
    produto = numero * 2
    print(numero, '* 2 = ', produto)
print('Loop Completo\n')