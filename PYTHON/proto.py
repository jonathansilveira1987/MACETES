from datetime import datetime
import time

# Obter a hora atual em Python.
print('\n\033[0;32mSegue data e hora nesse momento...\033[m')
a, b = time.strftime('%d-%m-%Y', time.localtime()), time.strftime('%H:%M:%S', time.localtime())
print(f'\033[0;32m{a}\033[m')
print(f'\033[0;32m{b}\033[m')

# Obter o dia da semana, mês, dia, hora e ano.
c = time.ctime()
c = c.split()
print()
print(f'\033[0;31m{c}\033[m')
print()

from datetime import datetime
now = datetime.now()
print('Dia      = ', now.day)
print('Mês      = ', now.month)
print('Ano      = ', now.year)
print('Hora     = ', now.hour)
print('Minuto(s)   = ', now.minute)
print('Segundo(s) = ', now.second)
print()

a = 300 * (1 + 0.04) ** 2
print(f'\n{a}')
print(f'\n{a} é um dado tipo {type(a)}\n')