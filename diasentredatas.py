from datetime import date

# 10/10/2021 - 02/10/1987

ano = int(input('Ano de Nascimento? '))
mes = int(input('Mês de Nascimento? '))
dia = int(input('Dia de Nascimento? '))

dias = date.today() - date(ano, mes, dia)

print(f'Já se passaram {dias.days} dias desde seu nascimento.')
# 12427 days