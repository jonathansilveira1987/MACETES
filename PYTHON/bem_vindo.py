from operator import index
from ast import main
from time import sleep

print('\nOlá Mundo!')

sleep(1.5)
a = type('meu_email@email.com')
b = type(15)
c = type(0.26)
d = type(True)
e = type(4+5j)
print(f'\n\033[0;31m{a}\033[m')
print(f'\033[0;32m{b}\033[m')
print(f'\033[0;33m{c}\033[m')
print(f'\033[0;34m{d}\033[m')
print(f'\033[0;35m{e}\033[m')

sleep(1.5)
f = '\033[0;36mMeu livro favorito chama-se "Código Limpo".\033[m'
print(f'\n{f}')

sleep(1.5)
fruta = " Banana\033[m"
tipo  = "\n\033[0;30mBolo de"
print(tipo + fruta)

# nome = "\033[0;32m0 1 0 1 \033[m"
# print(nome * 1000)

sleep(1.5)
g = 'meu_email@email.com\n'
print(g[::-1])

sleep(1.5)
h = 5
print(f'\n{h} multiplicado por 2 é: {h * 2}')

sleep(1.5)
i = 'JONATHAN DA COSTA SILVEIRA'
j = [10, 20, 30, 40]
print(f'\n{i.upper()}') # Todas letras maiúsculas.
print(f'{i.lower()}') # Todas letras minúsculas.
print(f'{i.capitalize()}') # Apenas primeira letra minúscula.

sleep(1.5)
k = [1, 2, 3, 4, 5, 6, 7, 8]
print(f'\n{k} lista com {len(k)} ítens.')
l = ['a', 'b', 'c', 'd']
print(f'\n{l} lista com {len(l)} ítens.')
m = [3.4, 2.4, 2.6, 6.5, 9.0, 1.5, 8.3]
print(f'\n{m} lista com {len(m)} ítens.')

sleep(1.5)
n = [1, 2, 3, 4]
o = input('\nInformação: ')
n.append(o)
print(f'\n{n}')

sleep(1.5)
print(f'\n{k[5]}')
print(f'{k[0:3]}')
print(f'{k[::6]}')
print(f'{k[::-2]}')
print(f'{k[7:1:-1]}\n')