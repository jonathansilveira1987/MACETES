# Lista de fusos horários.
import pytz
print()
for tz in pytz.all_timezones:
    print(f'\033[0;33m{tz}\033[m')
print()

# Escrever arquivo em Python.
with open('lista_de_fuso_horario.txt', 'a') as arquivo:
    for tz in tz:
        arquivo.write(tz + '\n')