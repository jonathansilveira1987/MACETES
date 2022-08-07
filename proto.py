from datetime import datetime
import time
from xmlrpc.client import NOT_WELLFORMED_ERROR

# Obter a hora atual em Python.
a, b = time.strftime('%d-%m-%Y', time.localtime()), time.strftime('%H:%M:%S', time.localtime())
print()
print(a)
print(b)

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
print('Minuto   = ', now.minute)
print('Segundos = ', now.second)
