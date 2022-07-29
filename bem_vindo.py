from operator import index


print('\nOlá Mundo!')

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

f = '\033[0;36mMeu livro favroito chama-se "Código Limpo".\033[m'
print(f'\n{f}')

fruta = " Banana\033[m"
tipo  = "\n\033[0;30mBolo de"
print(tipo + fruta)

# nome = "\033[0;32m0 1 0 1 \033[m"
# print(nome * 1000)

g = 'meu_email@email.com\n'
print(g[::-1])

h = 5
print(f'\n{h} multiplicado por 2 é: {h * 2}')

i = 'JONATHAN DA COSTA SILVEIRA'
print(f'\n{i.lower()}')

