# Calendário.
# Desenvolvido por Jonathan Silveira - Instagram: @ jonathandev01

import calendar
from datetime import date

while True:
    # Programa principal!
    print("\n\033[0;33mDigite 0 para imprimir o calendário do ano atual ou informe o ano desejado.\033[m\n")
    ano = int(input("\033[0;32m> "))
    print('\033[m')
    if ano == 0:
        ano_atual = date.today().year
        print(calendar.calendar(ano_atual))   
    if ano == ano:
        print(calendar.calendar(ano))
    else:
        # Aqui vai o "Tente novamente!"
        ano != 'int'
        print("\n\033[0;31mValor incorreto, tente novamente.\033[m\n", end=" ")
        continue
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\n\033[0;33mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")