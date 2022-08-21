import random
# Remover elemento de uma lista usando pop para sortear.
elemento = int(input('\nInforme o número de valores para a lista: '))
print()
lista = [input("Valor: ") for i in range(elemento)]
prime_numbers = lista
# Remove um valor sorteado.
removed_element = prime_numbers.pop(random.randrange(len(prime_numbers))) 
print(f'\n\033[0;33mElemento sorteado para ser removido: {removed_element}\033[m')
print(f'\n\033[0;34mLista atualizada: {prime_numbers}\033[m\n')