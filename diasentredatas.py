from datetime import date

# 10/10/2021 - 02/10/1987

ano = int(input('\nAno de Nascimento? '))
mes = int(input('Mês de Nascimento? '))
dia = int(input('Dia de Nascimento? '))

dias = date.today() - date(ano, mes, dia)

print(f'\nJá se passaram \033[0;34m{dias.days}\033[m dias desde seu nascimento.\n')
# 12427 days