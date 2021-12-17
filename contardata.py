# Contar data.

import datetime

while True:
    # Aqui vai o programa principal!
    a1 = int(input('\n\033[0;32mDia de Nascimento: \033[m'))
    a2 = int(input('\033[0;32mMês de Nascimento: \033[m'))
    a3 = int(input('\033[0;32mAno de Nascimento: \033[m'))
    a4 = datetime.datetime(a3,a2,a1)
    a5 = datetime.datetime.now()

    diff = a5 - a4

    days = diff.days
    years, days = days // 365, days % 365
    months, days = days // 30, days % 30

    seconds = diff.seconds
    hours, seconds = seconds // 3600, seconds % 3600
    minutes, seconds = seconds // 60, seconds % 60
    print("\n\033[0;31mDesde {}/{}/{} passaram-se {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos.\033[0m".format(a1, a2, a3, years, months, days, hours, minutes, seconds))
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")















































'''
import datetime

d1 = datetime.datetime(1987,10,2,)
d2 = datetime.datetime.now()

diff = d2 - d1

days = diff.days
years, days = days // 365, days % 365
months, days = days // 30, days % 30

seconds = diff.seconds
hours, seconds = seconds // 3600, seconds % 3600
minutes, seconds = seconds // 60, seconds % 60

print("Desde {} passaram {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos".format(d1, years, months, days, hours, minutes, seconds))
'''