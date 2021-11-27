# Calendário.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

import calendar
from datetime import date

while True:
    print("\n\033[0;32;1;4mDigite 0 para imprimir o calendário do ano atual.\033[m\n")
    ano = int(input("\033[0;33;1;4mOu informe o ano que deseja imprimir o calendário:\033[m "))
    if ano == 0:
        ano_atual = date.today().year
        print(calendar.calendar(ano_atual))   
    else:
        print(calendar.calendar(ano))
    resp = " "
    while resp not in "10":
        resp = str(input("\nDeseja continuar [1 - SIM / 0 - NÃO]? ")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")



'''
# Ano Bissexto

from datetime import date

print("Coloque 0 para analisar o ano atual")
ano = int(input("Ou informe o ano a ser analisado: "))

if ano == 0:
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO.".format(ano))
else:
    print("O ano {} NÃO É BISSEXTO.".format(ano))
'''