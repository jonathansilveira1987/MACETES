# Remover elemento de uma lista.
from time import sleep
print('Disponibilizando ferramenta, por favor aguarde...')
sleep(2)
print('\nAbaixo segue modelo de execução do método POP de remoção de um elemento em uma lista!')
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]
print('\n\033[0;32mLista =', prime_numbers)
# remove the element at index 2
removed_element = prime_numbers.pop(2)
print('\nElemento Removido:', removed_element)
print('Lista atualizada:', prime_numbers)
# Output: 
# Removed Element: 5
# Updated List: [2, 3, 7]
print('\033[m')

print('Aqui vamos utilizar o método REMOVE!')
a = input('\nElemento A: ')
b = input('Elemento B: ')
c = input('Elemento C: ')
d = input('Elemento D: ')

prime_numbers = [a, b, c, d]
print()
print(prime_numbers)

e = input('Qual elemento da lista acima você deseja remover? ')
removed_element = prime_numbers.remove(e)

print('\nElemento removido:', e)
print('Lista atualizada:', prime_numbers)