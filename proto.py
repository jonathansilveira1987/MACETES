import calendar
yy = int(input('\nAno: '))
mm = int(input('Mês: '))
print('\033[0;33m')
print(calendar.month(yy, mm))
print('\033[m')