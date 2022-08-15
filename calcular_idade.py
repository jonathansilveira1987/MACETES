from time import sleep
from datetime import date
import datetime as dt
import datetime

while True:
    # Programa principal!
    dia = int(input('\n\033[0;31mDia de Nascimento: \033[m'))
    mes = int(input('\033[0;31mMês de Nascimento: \033[m'))
    ano = int(input('\033[0;31mAno de Nascimento: \033[m'))

    print('\nCalculando, por favor aguarde...')
    sleep(3)

    # Calcular dias desde nascimento.
    dias = date.today() - date(ano, mes, dia)
    # print(f'\nJá se passaram \033[0;33m{dias.days}\033[m dias desde seu nascimento.')
    print("\nJá se passaram \033[0;32m{0:,}\033[m dias desde seu nascimento.".format(dias.days).replace(",", "."))

    # Calcular Idade.
    sleep(2)
    current_date = date.today()
    data_nascimento = ano
    data_actual = current_date.year
    idade = data_actual - data_nascimento
    print('\nNesse ano você completa(ou) \033[0;33m{}\033[m ano(s).'.format(idade))

    # Contar data.
    sleep(2)
    a1 = dia
    a2 = mes
    a3 = ano
    a4 = datetime.datetime(a3,a2,a1)
    a5 = datetime.datetime.now()
    diff = a5 - a4
    days = diff.days
    years, days = days // 365, days % 365
    months, days = days // 30, days % 30
    seconds = diff.seconds
    hours, seconds = seconds // 3600, seconds % 3600
    minutes, seconds = seconds // 60, seconds % 60
    print("\n\033[0;34mDesde {}/{}/{} passaram-se {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos.\033[0m\n".format(a1, a2, a3, years, months, days, hours, minutes, seconds))    
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("Continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")