import calendar

ano = int(input('\nAno: '))
mes = int(input('Mês: '))
print(f'\n{calendar.month(ano, mes)}')

colunas = int(input('Colunas: '))
for i in range(colunas + 1):
    for j in range(i):
        print(i, end=' ')
    print('')
print()

colunas = int(input('Colunas: '))
print()
for i in range(1, colunas + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
print()