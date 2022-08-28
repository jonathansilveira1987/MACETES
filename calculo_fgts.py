mp = float(input('\nValor guardado Mercado Pago: '))
pp = float(input('Valor guardado PicPay: '))
nb = float(input('Valor guardado NuBank: '))
result = mp + pp + nb
a = result
b = float(input('Valor FGTS depositado em outubro: '))
c = float(input('Valor CNH: '))
d = float(input('Valor FGTS atual: '))

e = a - c
valor_real1 = '\033[0;31mR$ {:,.2f}\033[m'.format(e).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nValor guardado - valor CNH = {valor_real1}.')

f = e + b
valor_real2 = '\033[0;32mR$ {:,.2f}\033[m'.format(f).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\n(Saldo Valor guardado - valor CNH) + FGTS depositado em outubro = {valor_real2}.')

g = d - b
valor_real3 = '\033[0;33mR$ {:,.2f}\033[m'.format(g).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nFGTS atual - FGTS depositado em outubro = {valor_real3}.')

h = f + g
valor_real4 = '\033[0;34mR$ {:,.2f}\033[m'.format(h).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\n(FGTS atual - FGTS depositado em outubro) + Valor guardado atualizado = {valor_real4}.')

i = (28 * g / 100)
j = h - i
valor_real5 = '\033[0;35mR$ {:,.2f}\033[m'.format(j).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nValor Final - Juros empréstimo FGTS = {valor_real5}.')

moto = float(input('\nValor da moto: '))
cnh = float(input('Valor da CNH: '))

k = j - moto - cnh
valor_real6 = '\033[0;36mR$ {:,.2f}\033[m'.format(k).replace(",", "X").replace(".", ",").replace("X", ".")
print(f'\nApós comprar a moto e retirar CNH restará um saldo de = {valor_real6}.\n')