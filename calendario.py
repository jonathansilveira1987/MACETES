# Calendário.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

import calendar

while True:
    print(calendar.calendar(int(input('Ano: '))))   
    resp = " "
    while resp not in "10":
        resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")

'''
import calendar

year = int(input('Ano: '))

for i in range(1, 13):
    print(calendar.month(year, i))
'''


'''
import calendar

# Janeiro

year = 2021     #Ano
month = 1       #Mês
print (calendar.month(year, month))

# Fevereiro
year = 2021     #Ano
month = 2       #Mês
print (calendar.month(year, month))

# Março
year = 2021     #Ano
month = 3       #Mês
print (calendar.month(year, month))

# Abril
year = 2021     #Ano
month = 4       #Mês
print (calendar.month(year, month))

# Maio
year = 2021     #Ano
month = 5       #Mês
print (calendar.month(year, month))

# Junho
year = 2021     #Ano
month = 6       #Mês
print (calendar.month(year, month))

# Julho
year = 2021     #Ano
month = 7       #Mês
print (calendar.month(year, month))

# Agosto
year = 2021     #Ano
month = 8       #Mês
print (calendar.month(year, month))

# Setembro
year = 2021     #Ano
month = 9       #Mês
print (calendar.month(year, month))

# Outubro
year = 2021     #Ano
month = 10      #Mês
print (calendar.month(year, month))

# Novembro
year = 2021     #Ano
month = 11      #Mês
print (calendar.month(year, month))

# Dezembro
year = 2021     #Ano
month = 12      #Mês
print (calendar.month(year, month))
'''