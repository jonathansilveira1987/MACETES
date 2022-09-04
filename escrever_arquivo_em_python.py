# Escrever arquivo em Python.
elemento = int(input('\nInforme o número de elementos para o arquivo: '))
print()
palavras = [input("Dado: ") for i in range(elemento)]
print(f'\n\033[0;32m{palavras}\033[m')
print('\n\033[0;36mOs dados informados foram salvos no arquivo data_base.txt!\033[m\n')
with open('data_base.txt', 'a') as arquivo:
    for palavras in palavras:
        arquivo.write(palavras + '\n')

'''
# Excluir arquivo em Python.
import os
if os.path.exists('data_base.txt'):
    os.remove('data_base.txt')
else:
    print('\nO arquivo informado não existe!\n')
'''