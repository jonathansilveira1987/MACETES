# Remover elemento de uma lista.
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
lista = [input("Dado: ") for i in range(elemento)]
prime_numbers = lista
print()
print(f'\n\033[0;31m{prime_numbers}\033[m')
e = input('Qual elemento da lista acima você deseja remover? ')
removed_element = prime_numbers.remove(e)
print(f'\n\033[0;33mElemento removido: {e}\033[m')
print(f'\n\033[0;32mLista atualizada: {prime_numbers}\033[m')

# Remover elemento de uma lista usando pop para sortear.
elemento = int(input('\nInforme o número de elementos para a lista: '))
print()
lista = [input("Dado: ") for i in range(elemento)]
prime_numbers = lista
# Remove o elemento sorteado.
removed_element = prime_numbers.pop()
print(f'\n\033[0;34mElemento sorteado para ser removido: {removed_element}\033[m')
print(f'\n\033[0;35mLista atualizada: {prime_numbers}\033[m\n')