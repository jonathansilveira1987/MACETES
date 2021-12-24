# Calcular tempo de uma viagem.

while True:
    # Programa principal!
    distância = float(input("\nDigite a distância em km: "))
    velocidade_média = float(input("Digite a velocidade média em km/h: "))
    tempo = distância / velocidade_média
    tempo_s = int(tempo * 3600)  # convertemos de horas para segundos
    horas = int(tempo_s / 3600)  # parte inteira
    tempo_s = int(tempo_s % 3600)  # o resto
    minutos = int(tempo_s / 60)
    segundos = int(tempo_s % 60)
    milesimosegundos = int(tempo_s % 60)
    # Imprimir o tempo em horas, minutos, segundos e milésimos de segundos.
    print("\n\033[0;32mO tempo estimado de viagem é de %04d hora(s) %02d minuto(s) %02d segundo(s) & %02d milésimos de segundo(s).\033[m" % (horas, minutos, segundos, milesimosegundos))
    # Imprimir o tempo em horas, minutos, segundos.
    print("\n\033[0;33m%04d hora(s) %02d minuto(s) & %02d segundo(s).\033[m\n" % (horas, minutos, segundos))
    
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")




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
    hora_atual = hora_atual.strftime("%H:%M")
    hora_final = hora_final.strftime("%H:%M")
    print(f"\n\033[0;33mA hora atual é {hora_atual}.\033[m")
    print(f"\033[0;32mO horário final do processo é {hora_final}.\033[m\n")
    # Aqui vai o "Deseja continuar?"
    resp = " "
    while resp not in "10":
        resp = str(input("\033[0;34mDeseja continuar [1 - SIM / 0 - NÃO]? \033[m")).strip().upper()[0]
    if resp == "0":
        break    
print("\033[0;36;1;4m\nVocê optou por finalizar!\033[m\n")