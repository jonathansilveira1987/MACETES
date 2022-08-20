from random import randint
from time import sleep
def sorteia(lista):
    print()
    print('Sorteando 5 valores da lista:', end=' ')
    for cont in range(0, 5):
        n = randint(1, 1000)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(1)
    print('- PRONTO!')
numeros = list()
sorteia(numeros)
print('\nLista = ', numeros)



# Remover elemento de uma lista usando pop para sortear.
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
lista = [input("Dado: ") for i in range(elemento)]
prime_numbers = lista
# Remove o elemento sorteado.
removed_element = prime_numbers.pop(1)
print(f'\n\033[0;34mElemento sorteado para ser removido: {removed_element}\033[m')
print(f'\n\033[0;35mLista atualizada: {prime_numbers}\033[m\n')