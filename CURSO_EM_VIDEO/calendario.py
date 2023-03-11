# Calendário.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

import calendar
from datetime import date

# Validando entrada de dados em Python.

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        ano = int(input(msg))
        if ano.isnumeric():
            valor = int(ano)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

# Programa Principal
while True:
    print("\n\033[0;33mDigite 0 para imprimir o calendário do ano atual ou informe o ano desejado.\033[m\n")
    ano = int(input("\033[0;32m> "))
    print('\033[m')
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