# Idade.

from datetime import date

while True:
    # Programa principal!
    current_date = date.today()
    data_nascimento= int(input("\nAno de nascimento: "))
    data_actual = current_date.year
    idade = data_actual - data_nascimento
    print('\nVocê tem \033[0;33m{}\033[m ano(s).\n'.format(idade))
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")