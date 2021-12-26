# Calcular tempo de percurso.
import datetime as dt
inicio = dt.datetime.now()
inicio = inicio.strftime('%H:%M:%S')
fim = input('\nInforme o horário de chegada (exemplo 13:10:20): ')
horario_inicio = dt.datetime.strptime(inicio, '%H:%M:%S')
horario_fim = dt.datetime.strptime(fim, '%H:%M:%S')
diferenca = (horario_fim - horario_inicio) 
diferenca.seconds/60
print(f'\n\033[0;33mAgora são {inicio}.\033[m')
print(f'\n\033[0;32mO tempo de percurso será de {diferenca}.\033[m\n')


# Calcular o intervalo de tempo entre duas seqüências de tempo.
inicio = input('\nInforme o horário de saída (exemplo 13:10:20): ')
fim = input('Informe o horário de chegada (exemplo 13:10:20): ')
horario_inicio = dt.datetime.strptime(inicio, '%H:%M:%S')
horario_fim = dt.datetime.strptime(fim, '%H:%M:%S')
diferenca = (horario_fim - horario_inicio) 
diferenca.seconds/60
print(f'\nO trajeto terá duração de {diferenca}.\n')





'''
# Vetor estável.
import datetime as dt
inicio = "09:35:23"
fim = "22:23:00"
horario_inicio = dt.datetime.strptime(inicio, '%H:%M:%S')
horario_fim = dt.datetime.strptime(fim, '%H:%M:%S')
diferenca = (horario_fim - horario_inicio) 
diferenca.seconds/60
print(diferenca)
inicio = input('\nInforme o horário de saída: ')
fim = input('Informe o horário de chegada: ')
horario_inicio = dt.datetime.strptime(inicio, '%H:%M:%S')
horario_fim = dt.datetime.strptime(fim, '%H:%M:%S')
diferenca = (horario_fim - horario_inicio) 
diferenca.seconds/60
print(f'\n\033[0;32mO tempo de precurso será de {diferenca}.\033[m\n')
'''