# Calcular o horário do término de um processo.

import datetime as dt

while True:
    # Programa principal!
    qpd = int(input('\nQuantidade produzida: '))  # qpd = Quantidade Produzida
    qpg = int(input('Quantidade programada: '))  # qpg = Quantidade Programada
    qrs = qpg - qpd  # qrs = Quantidade Restante
    qpc = qrs / 550  # qpc = Quantidade por Carro
    mrs = int(qpc * 18)  # mrs = Minutos Restantes
    if mrs > 60:
        hora = mrs // 60  # hora = Horas até o término da solução
        minuto = mrs % 60  # minuto = Minuto até o término da solução
        print(f'Faltam, aproximadamente, {hora} horas e {minuto} minutos para'
            ' o término da solução.')
    else:
        print(f'Faltam, aproximadamente, {mrs} minutos para'
            ' o término da solução.')
    hora_atual = dt.datetime.now()
    hora_final = hora_atual + dt.timedelta(minutes = mrs)
    hora_atual = hora_atual.strftime("%H:%M:%S")
    hora_final = hora_final.strftime("%H:%M:%S")
    print(f"\n\033[0;33mA hora atual é {hora_atual}.\033[m")
    print(f"\033[0;32mO horário final do processo é {hora_final}.\033[m\n")
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")