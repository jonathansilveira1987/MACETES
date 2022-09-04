# Lista de fusos horários.
import pytz
print()
for tz in pytz.all_timezones:
    print(f'\033[0;33m{tz}\033[m')
print()

# Escrever arquivo em Python.
fuso_horario = [tz]
with open('lista_de_fuso_horario.txt', 'a') as arquivo:
    for fuso_horario in fuso_horario:
        arquivo.write(fuso_horario + '\n')