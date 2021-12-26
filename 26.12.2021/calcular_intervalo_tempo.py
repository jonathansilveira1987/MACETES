import datetime as dt

# Calcular o intervalo de tempo entre duas seqüências de tempo.
inicio = input('\nInforme o horário de saída (exemplo 13:10:20): ')
fim = input('Informe o horário de chegada (exemplo 13:10:20): ')
horario_inicio = dt.datetime.strptime(inicio, '%H:%M:%S')
horario_fim = dt.datetime.strptime(fim, '%H:%M:%S')
diferenca = (horario_fim - horario_inicio) 
diferenca.seconds/60
print(f'A viagem terá duração de {diferenca}.')